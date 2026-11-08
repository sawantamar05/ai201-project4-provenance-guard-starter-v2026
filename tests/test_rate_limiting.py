"""Rate-limit instruments are tested separately from isolated route contracts."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import app as appmod
import audit
import config
import detector

TEXT = 'This writing sample has enough words for the local service to score it safely.'


class RateLimitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        for name, value in [('LOG_DIR', Path(self.temp.name)),
                            ('AUDIT_LOG', Path(self.temp.name) / 'audit.jsonl')]:
            p = patch.object(config, name, value)
            p.start()
            self.addCleanup(p.stop)
        self.model_patch = patch.object(detector, 'model_signal', return_value=0.5)
        self.model = self.model_patch.start()
        self.addCleanup(self.model_patch.stop)
        self.previous_enabled = appmod.limiter.enabled
        appmod.limiter.enabled = True
        appmod.limiter.reset()
        self.addCleanup(self.restore)
        self.client = appmod.app.test_client()

    def restore(self):
        appmod.limiter.reset()
        appmod.limiter.enabled = self.previous_enabled

    def submit(self, creator='burst', address='127.0.0.1'):
        return self.client.post('/submit', json={'text': TEXT, 'creator_id': creator},
                                environ_overrides={'REMOTE_ADDR': address})

    def test_burst_blocks_five_requests_without_scoring_them(self):
        codes = [self.submit().status_code for _ in range(15)]
        self.assertEqual(codes, [200] * 10 + [429] * 5)
        self.assertEqual(self.model.call_count, 10)
        entries = audit.read_entries()
        self.assertEqual(len(entries), 15)
        for entry in entries[:10]:
            self.assertTrue({'timestamp', 'content_id', 'creator_id', 'guess', 'model_score',
                             'style_score', 'combined_score', 'label', 'status'} <= entry.keys())
        for entry in entries[10:]:
            self.assertEqual(entry['creator_id'], 'burst')
            self.assertEqual(entry['rate_limit_bucket'], 'creator:burst')
            self.assertEqual(entry['http_status'], 429)
            self.assertEqual(entry['reason'], 'rate_limited')
            self.assertIn('10 per 1 minute', entry['limit'])

    def test_same_creator_shares_quota_across_addresses(self):
        for _ in range(10):
            self.assertEqual(self.submit('shared').status_code, 200)
        self.assertEqual(self.submit('shared', '127.0.0.2').status_code, 429)
        self.assertEqual(self.submit('different').status_code, 200)

    def test_missing_creator_uses_address_and_records_rejections(self):
        for _ in range(10):
            response = self.client.post('/submit', json={'text': TEXT})
            self.assertEqual(response.status_code, 400)
        response = self.client.post('/submit', json={'text': TEXT})
        self.assertEqual(response.status_code, 429)
        self.assertEqual(self.client.post('/submit', json={'text': TEXT},
                         environ_overrides={'REMOTE_ADDR': '127.0.0.2'}).status_code, 400)
        self.model.assert_not_called()
        self.assertTrue(all(row['status'] == 'rejected' for row in audit.read_entries()))
        self.assertEqual(audit.read_entries()[10]['rate_limit_bucket'], 'address:127.0.0.1')

    def test_daily_limit_survives_minute_window_changes(self):
        clock = [1700000000.0]
        with patch('time.time', side_effect=lambda: clock[0]):
            for i in range(200):
                if i and i % 10 == 0:
                    clock[0] += 61
                self.assertEqual(self.submit('daily').status_code, 200)
            clock[0] += 61
            response = self.submit('daily')
            self.assertEqual(response.status_code, 429)
        self.assertEqual(self.model.call_count, 200)
        self.assertIn('200 per 1 day', audit.read_entries()[-1]['limit'])


if __name__ == '__main__':
    unittest.main()

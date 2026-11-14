"""Request traces cover early failures and never retain writing/reasoning."""

from datetime import datetime, timedelta
import json
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import uuid

import app as appmod
import audit
import config
import detector
import telemetry


TEXT = 'This private paragraph has enough words for the local model to score.'


class TelemetryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        for key, value in (('LOG_DIR', self.directory),
                           ('AUDIT_LOG', self.directory / 'audit.jsonl')):
            setting = patch.object(config, key, value)
            setting.start()
            self.addCleanup(setting.stop)
        model = patch.object(detector, 'model_signal', return_value=0.60)
        self.model = model.start()
        self.addCleanup(model.stop)
        self.old_enabled = appmod.limiter.enabled
        appmod.limiter.enabled = True
        appmod.limiter.reset()
        self.addCleanup(self.restore_limiter)
        self.client = appmod.app.test_client()

    def restore_limiter(self):
        appmod.limiter.reset()
        appmod.limiter.enabled = self.old_enabled

    def rows(self):
        if not telemetry.log_path().exists():
            return []
        return [json.loads(x) for x in telemetry.log_path().read_text().splitlines()]

    def submit(self, creator='private-writer', **kwargs):
        return self.client.post('/submit', json={'text': TEXT, 'creator_id': creator}, **kwargs)

    def assert_completion(self, row, response, path):
        self.assertEqual(row['event'], 'request_completed')
        self.assertEqual(row['request_id'], response.headers['X-Request-ID'])
        uuid.UUID(row['request_id'])
        self.assertEqual(datetime.fromisoformat(row['timestamp']).utcoffset(), timedelta(0))
        self.assertEqual(row['path'], path)
        self.assertEqual(row['http_status'], response.status_code)
        for name in ('duration_ms', 'cpu_seconds'):
            self.assertIsInstance(row[name], (int, float))
            self.assertTrue(math.isfinite(row[name]))
            self.assertGreaterEqual(row[name], 0)

    def test_success_is_correlated_durable_and_separate_from_audit(self):
        response = self.submit()
        self.assertEqual(response.status_code, 200)
        rows = self.rows()
        self.assertEqual(len(rows), 1)
        self.assert_completion(rows[0], response, '/submit')
        self.assertEqual(rows[0]['method'], 'POST')
        self.assertEqual(rows[0]['input_summary']['field_names'], ['creator_id', 'text'])
        self.assertEqual(rows[0]['input_summary']['text_characters'], len(TEXT))
        self.assertGreater(rows[0]['input_summary']['body_bytes'], len(TEXT))
        body = response.get_json()
        self.assertEqual(rows[0]['output_summary']['content_id'], body['content_id'])
        self.assertEqual(rows[0]['output_summary']['guess'], body['guess'])
        self.assertEqual(len(audit.read_entries()), 1)
        self.assertNotIn('event', audit.read_entries()[0])
        self.assertNotIn(TEXT, telemetry.log_path().read_text())
        self.assertNotIn('private-writer', telemetry.log_path().read_text())

    def test_request_ids_are_unique_and_client_id_is_not_trusted(self):
        first = self.submit(headers={'X-Request-ID': 'client-forged-request-id'})
        second = self.submit()
        ids = [row['request_id'] for row in self.rows()]
        self.assertEqual(len(set(ids)), 2)
        self.assertNotIn('client-forged-request-id', ids)
        self.assertNotEqual(first.headers['X-Request-ID'], second.headers['X-Request-ID'])

    def test_quota_response_leaves_one_completion_without_scoring(self):
        responses = [self.submit() for _ in range(11)]
        self.assertEqual([r.status_code for r in responses], [200] * 10 + [429])
        rows = self.rows()
        self.assertEqual(len(rows), 11)
        self.assert_completion(rows[-1], responses[-1], '/submit')
        self.assertEqual(rows[-1]['output_summary']['error'], 'rate_limited')
        self.assertEqual(self.model.call_count, 10)

    def test_validation_failure_is_recorded_with_redacted_input(self):
        response = self.client.post('/submit', json={'text': '', 'creator_id': 'writer'})
        self.assertEqual(response.status_code, 400)
        row, = self.rows()
        self.assert_completion(row, response, '/submit')
        self.assertEqual(row['input_summary']['text_characters'], 0)
        self.assertEqual(row['output_summary']['error'], 'invalid_text')
        self.model.assert_not_called()

    def test_appeal_reason_is_preserved_in_audit_but_absent_from_completion_log(self):
        original = self.submit().get_json()
        reason = '  Private appeal: inspect my personal draft evidence.  '
        response = self.client.post('/appeal', json={
            'content_id': original['content_id'], 'reasoning': reason,
        })
        self.assertEqual(response.status_code, 200)
        row = self.rows()[-1]
        self.assert_completion(row, response, '/appeal')
        self.assertEqual(row['output_summary']['status'], 'under_review')
        self.assertEqual(audit.read_entries()[-1]['reasoning'], reason)
        self.assertNotIn(reason.strip(), telemetry.log_path().read_text())

    def test_not_found_and_detector_failure_have_completion_records(self):
        unknown = '00000000-0000-4000-8000-000000000099'
        missing = self.client.get('/content/' + unknown)
        self.assertEqual(missing.status_code, 404)
        self.assert_completion(self.rows()[-1], missing, '/content/' + unknown)
        self.model.side_effect = detector.DetectorUnavailable('test unavailable')
        failed = self.submit()
        self.assertEqual(failed.status_code, 503)
        self.assert_completion(self.rows()[-1], failed, '/submit')
        self.assertEqual(self.rows()[-1]['output_summary']['error'], 'detector_unavailable')

    def test_oversized_body_is_summarized_without_body_read(self):
        with appmod.app.test_request_context('/submit', method='POST', data='x' * 65537,
                                             content_type='text/plain'):
            with patch('telemetry.request.get_data', side_effect=AssertionError('must not read')):
                summary = telemetry.input_summary()
        self.assertEqual(summary['body_bytes'], 65537)
        self.assertEqual(summary['parsing'], 'oversized_not_parsed')
        response = self.client.post('/submit', data='x' * 65537, content_type='text/plain')
        self.assertEqual(response.status_code, 413)
        row, = self.rows()
        self.assert_completion(row, response, '/submit')
        self.assertEqual(row['input_summary']['parsing'], 'oversized_not_parsed')

    def test_invalid_and_non_object_json_are_distinguished(self):
        for body, parsing in (('{', 'invalid_json'), ('null', 'non_object_json'),
                              ('[]', 'non_object_json')):
            with self.subTest(body=body):
                response = self.client.post('/submit', data=body, content_type='application/json')
                self.assertEqual(response.status_code, 400)
                self.assertEqual(self.rows()[-1]['input_summary']['parsing'], parsing)

    def test_write_failure_is_explicit_and_does_not_fabricate_a_completion(self):
        with patch.object(telemetry, 'append', side_effect=OSError('test full disk')):
            with self.assertLogs(appmod.app.logger, level='ERROR'):
                response = self.submit()
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.get_json()['error'], 'request_log_unavailable')
        self.assertTrue(response.headers['X-Request-ID'])
        self.assertEqual(self.rows(), [])
        # Route already ran before the completion append failed. Preserve that
        # reality rather than falsely promising the operation was rolled back.
        self.assertEqual(len(audit.read_entries()), 1)


if __name__ == '__main__':
    unittest.main()

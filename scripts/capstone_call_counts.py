#!/usr/bin/env python3
"""Isolated, mocked invocation evidence accompanying real capstone HTTP trials.

No model is loaded. Flask's test client executes the actual route/limiter code;
the same frozen requests are used, and every mock call count is saved explicitly.
This is not latency evidence or independent authorship validation.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.capstone_protocol import HUMAN, UNKNOWN_ID, matrix_cases, reasoning


def capture(response):
    return {'status_code': response.status_code, 'response_json': response.get_json(silent=True)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--criterion', type=int, required=True, choices=(1, 2, 5))
    parser.add_argument('--trial', type=int, required=True)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='capstone-mocked-calls-') as folder:
        os.environ['AI201_LOG_DIR'] = folder
        os.environ['AI201_RATE_LIMITS'] = '1'
        import app as service
        import audit
        import config
        import detector
        service.app.config['TESTING'] = True
        client = service.app.test_client()
        out = {'criterion': args.criterion, 'trial': args.trial,
               'kind': 'mocked isolated detector invocation check',
               'real_model_loaded': detector._model is not None, 'conditions': []}
        with patch.object(detector, 'model_signal', return_value=0.6) as model:
            def reset(name):
                directory = Path(folder) / name
                config.LOG_DIR = directory
                config.AUDIT_LOG = directory / 'audit.jsonl'
                service.limiter.reset()
                model.reset_mock()

            def submit(creator='mocked-writer', text=None):
                return client.post('/submit', json={'text': HUMAN[0]['text'] if text is None else text,
                                                    'creator_id': creator})

            if args.criterion == 1:
                for pressure in (False, True):
                    reset('pressure' if pressure else 'ordinary')
                    creator = f'mocked-c1-t{args.trial}'
                    pressure_rows = []
                    if pressure:
                        pressure_rows = [capture(submit(creator)) for _ in range(12)]
                        pressure_rows += [capture(client.post('/submit', json={'text': HUMAN[0]['text']}))
                                          for _ in range(12)]
                    calls_before = model.call_count
                    success_before = [r for r in audit.read_entries() if r.get('status') in ('decided', 'under_review')]
                    cases = []
                    for case in matrix_cases(creator):
                        before = model.call_count
                        response = client.post('/submit', **case['kwargs'])
                        cases.append({'case': case['case'], 'expected_status': case['expected_status'],
                                      **capture(response), 'detector_calls': model.call_count - before})
                    success_after = [r for r in audit.read_entries() if r.get('status') in ('decided', 'under_review')]
                    out['conditions'].append({'pressure': pressure, 'pressure_responses': pressure_rows,
                                              'pressure_detector_calls': calls_before, 'cases': cases,
                                              'matrix_detector_calls': model.call_count - calls_before,
                                              'successful_events_unchanged': success_before == success_after})
                out['passed'] = all(c['matrix_detector_calls'] == 0 and c['successful_events_unchanged']
                                    and all(r['detector_calls'] == 0 for r in c['cases'])
                                    for c in out['conditions'])
            elif args.criterion == 2:
                reset('allowance')
                creator = f'mocked-c2-t{args.trial}'
                rows = []
                for invalid in (True, False):
                    for index in range(12):
                        before = model.call_count
                        response = submit(creator, '' if invalid else None)
                        rows.append({'kind': 'invalid' if invalid else 'valid', 'index': index + 1,
                                     **capture(response), 'detector_calls': model.call_count - before})
                expected_statuses = [400] * 12 + [200] * 10 + [429] * 2
                expected_calls = [0] * 12 + [1] * 10 + [0] * 2
                out.update(requests=rows, total_detector_calls=model.call_count,
                           expected_statuses=expected_statuses, expected_calls=expected_calls,
                           passed=[r['status_code'] for r in rows] == expected_statuses
                           and [r['detector_calls'] for r in rows] == expected_calls
                           and model.call_count == 10)
            else:
                reset('appeals')
                setup = [capture(submit(f'mocked-c5-{i}', item['text']))
                         for i, item in enumerate(HUMAN, 1)]
                submissions = [row['response_json'] for row in setup]
                submission_calls = model.call_count
                originals = audit.read_entries()
                model.reset_mock()
                appeals, lookups = [], []
                for i, original in enumerate(submissions, 1):
                    appeals.append(capture(client.post('/appeal', json={
                        'content_id': original['content_id'], 'reasoning': reasoning(i)})))
                    lookups.append(capture(client.get('/content/' + original['content_id'])))
                unknown = capture(client.post('/appeal', json={'content_id': UNKNOWN_ID,
                                                               'reasoning': reasoning(99)}))
                history = audit.read_entries()
                original_unchanged = [r for r in history if r.get('status') == 'decided'] == originals
                fresh_code = '''
import json, sys
from unittest.mock import patch
import app, detector
with patch.object(detector, "model_signal", side_effect=AssertionError("lookup must not score")) as model:
    client = app.app.test_client()
    rows = [client.get("/content/" + identity) for identity in sys.argv[1:]]
    print(json.dumps({"detector_calls": model.call_count, "detector_loaded": detector._model is not None,
                      "statuses": [row.status_code for row in rows], "items": [row.get_json() for row in rows]}))
'''
                environment = os.environ.copy()
                environment['AI201_LOG_DIR'] = str(config.LOG_DIR)
                fresh = subprocess.run([sys.executable, '-c', fresh_code,
                                        *[row['content_id'] for row in submissions]],
                                       cwd=ROOT, env=environment, capture_output=True, text=True, check=True)
                restarted = json.loads(fresh.stdout)
                exact = all(r['status_code'] == 200 and r['response_json'].get('reasoning') == reasoning(i)
                            and r['response_json'].get('status') == 'under_review'
                            for i, r in enumerate(appeals, 1))
                persisted = all(item.get('status') == 'under_review'
                                and item['appeals'][0]['reasoning'] == reasoning(i)
                                and all(item.get(key) == value for key, value in submissions[i - 1].items()
                                        if key != 'status')
                                for i, item in enumerate(restarted['items'], 1))
                immediate = all(row['status_code'] == 200 and row['response_json'].get('status') == 'under_review'
                                and row['response_json']['appeals'][0]['reasoning'] == reasoning(i)
                                and all(row['response_json'].get(key) == value
                                        for key, value in submissions[i - 1].items() if key != 'status')
                                for i, row in enumerate(lookups, 1))
                setup_ok = submission_calls == 10 and all(row['status_code'] == 200
                            and row['response_json'].get('status') == 'decided' for row in setup)
                out.update(submission_detector_calls=submission_calls, setup=setup, appeals=appeals, lookups=lookups,
                           unknown=unknown, appeal_lookup_detector_calls=model.call_count,
                           original_unchanged=original_unchanged, restarted=restarted,
                           passed=setup_ok and exact and immediate and persisted and original_unchanged and model.call_count == 0
                           and restarted['detector_calls'] == 0 and not restarted['detector_loaded']
                           and restarted['statuses'] == [200] * 10 and unknown['status_code'] == 404
                           and len([r for r in history if r.get('event') == 'appeal']) == 10)
        out['real_model_loaded'] = detector._model is not None
        print(json.dumps(out, ensure_ascii=True, allow_nan=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

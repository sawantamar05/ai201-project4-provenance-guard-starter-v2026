#!/usr/bin/env python3
"""Run the registered capstone over real local HTTP without replacing missed results.

Every condition uses a separate one-worker Gunicorn process and isolated logs.
The detector is real and offline. Companion call counts are explicitly mocked.
A completed campaign exits successfully even when acceptance targets are missed.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
import math
import os
from pathlib import Path
import platform
import socket
import statistics
import subprocess
import sys
import time
import traceback
import uuid

import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.capstone_protocol import (  # noqa: E402
    HUMAN, UNKNOWN_ID, json_error, jsonl, matrix_cases, reasoning, successful_submission,
)

NAMES = {
    1: 'Validation errors under quota pressure',
    2: 'Malformed requests preserve scoring allowance',
    3: 'Complete durable request records',
    4: 'Warm submission response time',
    5: 'Appeals survive server restart',
}
TARGETS = {
    1: '20/20 exact JSON validation responses; no malformed scoring/success events',
    2: '12/12 invalid400; then ten200 and two429; exactly10 isolated detector calls',
    3: '23/23 durable unique correlated completion records with required redacted fields',
    4: '10/10 complete decisions; at least9/10 warm requests below5.0s',
    5: '10/10 exact persistent appeals; unchanged originals; unknown404; zero rescoring',
}
SOURCE_FILES = (
    'criteria.md', 'docs/criteria_parts1_2.md', 'app.py', 'audit.py', 'config.py',
    'detector.py', 'scoring.py', 'stylometry.py', 'telemetry.py',
    'scripts/run_capstone.py', 'scripts/capstone_protocol.py',
    'scripts/capstone_call_counts.py', 'data/evaluation_inputs.json',
)


def now():
    return datetime.now(timezone.utc).isoformat()


def relative(path):
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(Path(path).resolve())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=True, allow_nan=False) + '\n')
    temporary.replace(path)


def free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


class Server:
    def __init__(self, directory, starts=None):
        self.directory = directory.resolve()
        self.directory.mkdir(parents=True, exist_ok=True)
        self.starts = starts if starts is not None else []
        self.exchanges = []
        self.session = requests.Session()
        self.session.trust_env = False
        self.process = None
        self.output = None
        self.start_record = None

    def start(self):
        port = free_port()
        self.url = f'http://127.0.0.1:{port}'
        command = [sys.executable, '-m', 'gunicorn', '--workers', '1', '--threads', '1',
                   '--timeout', '120', '--bind', f'127.0.0.1:{port}', 'app:app']
        env = os.environ.copy()
        env.update(AI201_LOG_DIR=str(self.directory), AI201_RATE_LIMITS='1',
                   HF_HUB_OFFLINE='1',
                   HF_HOME=str(Path(os.environ.get('HF_HOME', ROOT / '.cache/huggingface')).resolve()))
        self.output = (self.directory / 'server.txt').open('a')
        self.process = subprocess.Popen(command, cwd=ROOT, env=env,
                                        stdout=self.output, stderr=subprocess.STDOUT)
        self.start_record = {'command': command, 'pid': self.process.pid,
                             'started_at_utc': now(), 'url': self.url,
                             'log_directory': relative(self.directory),
                             'environment_overrides': {key: env[key] for key in
                                                       ('AI201_LOG_DIR', 'AI201_RATE_LIMITS', 'HF_HUB_OFFLINE', 'HF_HOME')}}
        self.starts.append(self.start_record)
        deadline = time.monotonic() + 45
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f'Server exited {self.process.returncode}; see {self.directory}/server.txt')
            try:
                response = self.session.get(self.url + '/health', timeout=1)
                if response.status_code == 200:
                    self.start_record['health_at_start'] = response.json()
                    self.start_record['health_request_id'] = response.headers.get('X-Request-ID')
                    if not response.json().get('rate_limiting'):
                        raise RuntimeError('Rate limiting is disabled')
                    return self
            except requests.RequestException:
                pass
            time.sleep(0.1)
        raise RuntimeError('Server did not become healthy within45s')

    def send(self, method, path, *, name=None, timeout=120, **kwargs):
        record = {'name': name or path, 'method': method, 'path': path, 'sent_at_utc': now()}
        if 'json' in kwargs:
            record['request_json'] = kwargs['json']
        if 'data' in kwargs:
            record['request_body'] = kwargs['data']
        if 'headers' in kwargs:
            record['request_headers'] = kwargs['headers']
        started = time.perf_counter()
        try:
            response = self.session.request(method, self.url + path, timeout=timeout, **kwargs)
            record.update(status_code=response.status_code, response_headers=dict(response.headers),
                          request_id=response.headers.get('X-Request-ID'))
            try:
                record['response_json'] = response.json()
            except ValueError:
                record['response_text'] = response.text
            # requests consumes the body before .json(); timing includes both.
            record['elapsed_seconds'] = time.perf_counter() - started
            record['request_body_bytes'] = len(response.request.body or b'')
        except requests.RequestException as exc:
            record.update(status_code=None, elapsed_seconds=time.perf_counter() - started,
                          transport_error=f'{type(exc).__name__}: {exc}')
        self.exchanges.append(record)
        return record

    def submit(self, item, creator, name=None):
        return self.send('POST', '/submit', name=name, json={'text': item['text'], 'creator_id': creator})

    def warm(self, creator):
        response = self.submit(HUMAN[0], creator, 'disclosed cold-model warm-up')
        if not successful_submission(response):
            raise RuntimeError('Real-model warm-up failed: ' + json.dumps(response))
        self.start_record['cold_warmup'] = response
        return response

    def stop(self):
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=10)
                self.start_record['forced_stop'] = True
        if self.start_record is not None:
            self.start_record.update(stopped_at_utc=now(), returncode=self.process.returncode)
        if self.output is not None:
            self.output.close()
        if self.exchanges:
            # Preserve earlier exchanges when this log directory is restarted.
            path = self.directory / f'http_{len(self.starts):02d}.json'
            save_json(path, self.exchanges)
        self.session.close()


def companion(number, trial):
    path = ROOT / 'scripts/capstone_call_counts.py'
    if number not in (1, 2, 5):
        return {'required': False, 'passed': True}
    if not path.exists():
        return {'required': True, 'passed': False, 'error': 'Missing isolated call-count companion'}
    command = [sys.executable, str(path), '--criterion', str(number), '--trial', str(trial)]
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120)
    record = {'required': True, 'kind': 'mocked isolated invocation check; not real inference',
              'command': command, 'returncode': proc.returncode, 'stderr': proc.stderr}
    try:
        payload = json.loads(proc.stdout)
        record['result'] = payload
        record['passed'] = (proc.returncode == 0 and payload.get('passed') is True
                            and payload.get('criterion') == number and payload.get('trial') == trial)
    except (ValueError, AttributeError):
        record.update(passed=False, stdout=proc.stdout, error='Companion did not return a matching JSON result')
    return record


def audit_rows(directory):
    return jsonl(directory / 'audit.jsonl')


def successful_domain_events(rows):
    return [r for r in rows if r.get('status') in ('decided', 'under_review')]


def criterion_one(directory, prefix):
    conditions = []
    for pressure in (False, True):
        folder = directory / ('pressure' if pressure else 'ordinary')
        server = Server(folder)
        row = {'condition': 'pressure' if pressure else 'ordinary', 'starts': server.starts}
        try:
            server.start()
            row['warmup'] = server.warm(prefix + '-warm')
            began = time.perf_counter()
            if pressure:
                row['creator_pressure'] = [server.submit(HUMAN[0], prefix, f'creator pressure {i}') for i in range(1, 13)]
                row['address_pressure'] = [server.send('POST', '/submit', name=f'address pressure {i}',
                                                       json={'text': HUMAN[0]['text']}) for i in range(1, 13)]
            # Save the event boundary to establish that matrix requests do not save successful domain events.
            before, before_errors = audit_rows(folder)
            cases = []
            for case in matrix_cases(prefix):
                response = server.send('POST', '/submit', name=case['name'], **case['kwargs'])
                cases.append({k: v for k, v in case.items() if k != 'kwargs'} | {
                    'http': response, 'passed': json_error(response, case['expected_status'])})
            row['quota_sequence_seconds'] = time.perf_counter() - began
            after, after_errors = audit_rows(folder)
            row.update(cases=cases, audit_parse_errors=before_errors + after_errors,
                       successful_events_unchanged=successful_domain_events(before) == successful_domain_events(after))
            row['quota_window_valid'] = row['quota_sequence_seconds'] < 60
            row['passed'] = all(x['passed'] for x in cases) and row['successful_events_unchanged'] and not row['audit_parse_errors']
        finally:
            server.stop()
        conditions.append(row)
    count = sum(x['passed'] for c in conditions for x in c['cases'])
    return {'conditions': conditions, 'quota_window_valid': all(c['quota_window_valid'] for c in conditions),
            'http_passed': all(c['passed'] for c in conditions), 'exact_status_count': count,
            'summary': f'{count}/20 exact; no-success-events={all(c["successful_events_unchanged"] for c in conditions)}'}


def criterion_two(directory, prefix):
    server = Server(directory)
    result = {'starts': server.starts}
    try:
        server.start()
        result['warmup'] = server.warm(prefix + '-warm')
        began = time.perf_counter()
        invalid = [server.send('POST', '/submit', name=f'invalid allowance check {i}',
                               json={'text': '', 'creator_id': prefix}) for i in range(1, 13)]
        valid = [server.submit(HUMAN[0], prefix, f'valid allowance check {i}') for i in range(1, 13)]
        elapsed = time.perf_counter() - began
        result.update(invalid_requests=invalid, valid_requests=valid, quota_sequence_seconds=elapsed,
                      quota_window_valid=elapsed < 60)
    finally:
        server.stop()
    events, errors = audit_rows(directory)
    decisions = [row for row in events if row.get('creator_id') == prefix and row.get('status') == 'decided']
    invalid_count = sum(json_error(row, 400) for row in invalid)
    valid_count = sum(successful_submission(row) for row in valid[:10])
    last_count = sum(json_error(row, 429) for row in valid[10:])
    saved_ids = {row['content_id'] for row in decisions}
    expected_ids = {row.get('response_json', {}).get('content_id') for row in valid[:10] if successful_submission(row)}
    result.update(audit_parse_errors=errors, saved_decision_count=len(decisions),
                  invalid400_count=invalid_count, valid200_count=valid_count, throttled429_count=last_count,
                  http_passed=invalid_count == 12 and valid_count == 10 and last_count == 2
                  and len(decisions) == 10 and saved_ids == expected_ids and not errors,
                  summary=f'{invalid_count}/12 invalid400; {valid_count}/10 valid200; {last_count}/2 quota429')
    return result


def validate_completion(record, exchange):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    check(record.get('event') == 'request_completed', 'event type')
    check(record.get('request_id') == exchange.get('request_id'), 'request-ID correlation')
    check(record.get('method') == exchange['method'] and record.get('path') == exchange['path'], 'method/path')
    status = record.get('http_status')
    check(isinstance(status, int) and not isinstance(status, bool) and status == exchange.get('status_code'), 'HTTP status')
    try:
        parsed = datetime.fromisoformat(record.get('timestamp', '').replace('Z', '+00:00'))
        check(parsed.utcoffset() == timezone.utc.utcoffset(parsed), 'UTC timestamp')
    except (ValueError, TypeError):
        errors.append('parseable UTC timestamp')
    for key in ('duration_ms', 'cpu_seconds'):
        value = record.get(key)
        check(not isinstance(value, bool) and isinstance(value, (float, int)) and math.isfinite(value) and value >= 0, key)
    incoming, outgoing = record.get('input_summary'), record.get('output_summary')
    check(isinstance(incoming, dict), 'input summary object')
    check(isinstance(outgoing, dict), 'output summary object')
    if isinstance(incoming, dict):
        check(incoming.get('body_bytes') == exchange.get('request_body_bytes'), 'input body byte count')
        if isinstance(exchange.get('request_json'), dict):
            body = exchange['request_json']
            check(incoming.get('fields') == sorted(body), 'input field names')
            if isinstance(body.get('text'), str):
                check(incoming.get('text_length') == len(body['text']), 'input text character count')
    body = exchange.get('response_json', {})
    if isinstance(outgoing, dict):
        for key in ('content_id', 'guess', 'error'):
            if key in body:
                check(outgoing.get(key) == body[key], 'output ' + key)
    rendered = json.dumps(record, ensure_ascii=True)
    request_body = exchange.get('request_json', {})
    for field in ('text', 'reasoning'):
        value = request_body.get(field)
        if value:
            check(json.dumps(value, ensure_ascii=True)[1:-1] not in rendered, 'redaction of ' + field)
    return errors


def criterion_three(directory, prefix):
    server = Server(directory)
    result = {'starts': server.starts}
    measured = []
    try:
        server.start()
        result['warmup'] = server.warm(prefix + '-warm')
        began = time.perf_counter()
        submissions = [server.submit(item, prefix, f'observed valid {i}') for i, item in enumerate(HUMAN, 1)]
        measured.extend(submissions)
        measured.extend(server.submit(HUMAN[0], prefix, f'observed quota {i}') for i in range(1, 3))
        measured.extend(server.send('POST', '/submit', name=f'observed invalid {i}',
                                    json={'text': '', 'creator_id': prefix + '-invalid'}) for i in range(1, 6))
        for index, response in enumerate(submissions[:5], 1):
            identity = response.get('response_json', {}).get('content_id', UNKNOWN_ID)
            measured.append(server.send('POST', '/appeal', name=f'observed appeal {index}',
                                         json={'content_id': identity, 'reasoning': reasoning(index)}))
        measured.append(server.send('POST', '/appeal', name='observed unknown appeal',
                                    json={'content_id': UNKNOWN_ID, 'reasoning': reasoning(99)}))
        elapsed = time.perf_counter() - began
        result.update(quota_sequence_seconds=elapsed, quota_window_valid=elapsed < 60)
    finally:
        server.stop()
    rows, parse_errors = jsonl(directory / 'requests.jsonl')
    by_id = {}
    for row in rows:
        by_id.setdefault(row.get('request_id'), []).append(row)
    checked = []
    ids = [x.get('request_id') for x in measured]
    for exchange in measured:
        matches = by_id.get(exchange.get('request_id'), [])
        errors = []
        if not exchange.get('request_id') or ids.count(exchange.get('request_id')) != 1:
            errors.append('missing or repeated response request ID')
        if len(matches) != 1:
            errors.append(f'expected one durable completion, got{len(matches)}')
        if len(matches) == 1:
            errors.extend(validate_completion(matches[0], exchange))
        checked.append({'http': exchange, 'completion': matches[0] if len(matches) == 1 else matches,
                        'errors': errors, 'passed': not errors})
    expected_statuses = [200] * 10 + [429] * 2 + [400] * 5 + [200] * 5 + [404]
    statuses_ok = [x.get('status_code') for x in measured] == expected_statuses
    passed_count = sum(c['passed'] for c in checked)
    result.update(cases=checked, request_log_parse_errors=parse_errors,
                  expected_http_statuses=expected_statuses, actual_statuses=[x.get('status_code') for x in measured],
                  outcome_sequence_matches=statuses_ok, completion_count=passed_count,
                  http_passed=len(checked) == 23 and passed_count == 23 and not parse_errors and statuses_ok,
                  summary=f'{passed_count}/23 complete records; HTTP sequence={statuses_ok}')
    return result


def criterion_four(directory, prefix):
    server = Server(directory)
    result = {'starts': server.starts}
    try:
        server.start()
        result['cold_warmup'] = server.warm(prefix + '-warm')
        cases = [server.submit(item, prefix + '-' + item['id'], f'warm timed {item["id"]}') for item in HUMAN]
    finally:
        server.stop()
    successful = sum(successful_submission(row) for row in cases)
    quick = sum(successful_submission(row) and row['elapsed_seconds'] < 5.0 for row in cases)
    durations = [row['elapsed_seconds'] for row in cases]
    rows, errors = jsonl(directory / 'requests.jsonl')
    ids = {row.get('request_id') for row in cases}
    costs = [row['cpu_seconds'] for row in rows if row.get('request_id') in ids
             and isinstance(row.get('cpu_seconds'), (int, float)) and math.isfinite(row['cpu_seconds'])]
    result.update(cases=cases, valid_count=successful, under5_seconds_count=quick,
                  mean_wall_seconds=statistics.mean(durations), wall_seconds=durations,
                  cpu_seconds=costs, mean_cpu_seconds=statistics.mean(costs) if len(costs) == 10 else None,
                  request_log_parse_errors=errors, quota_window_valid=True,
                  http_passed=successful == 10 and quick >= 9,
                  summary=f'{successful}/10 decisions; {quick}/10<5s; mean{statistics.mean(durations):.4f}s')
    return result


def unchanged_decision(current, original):
    return all(current.get(key) == value for key, value in original.items() if key != 'status')


def criterion_five(directory, prefix):
    starts = []
    server = Server(directory, starts)
    result = {'starts': starts}
    try:
        server.start()
        submissions = [server.submit(item, prefix + '-' + item['id'], f'appeal setup {item["id"]}') for item in HUMAN]
        originals, original_errors = audit_rows(directory)
        original_bytes = (directory / 'audit.jsonl').read_bytes() if (directory / 'audit.jsonl').exists() else b''
        original_decisions = {x.get('content_id'): x for x in originals if x.get('status') == 'decided'}
        appeals = []
        for index, submission in enumerate(submissions, 1):
            identity = submission.get('response_json', {}).get('content_id', UNKNOWN_ID)
            response = server.send('POST', '/appeal', name=f'exact appeal {index}',
                                   json={'content_id': identity, 'reasoning': reasoning(index)})
            appeals.append({'content_id': identity, 'reasoning': reasoning(index), 'http': response})
    finally:
        server.stop()
    rows_before_restart, errors_before = audit_rows(directory)
    after_appeal_bytes = (directory / 'audit.jsonl').read_bytes() if (directory / 'audit.jsonl').exists() else b''
    restarted = Server(directory, starts)
    try:
        restarted.start()
        result['detector_unloaded_at_restart'] = starts[-1]['health_at_start'].get('detector_loaded') is False
        lookups = [restarted.send('GET', '/content/' + appeal['content_id'], name=f'persisted lookup {i}')
                   for i, appeal in enumerate(appeals, 1)]
        unknown = restarted.send('POST', '/appeal', name='unknown appeal after restart',
                                 json={'content_id': UNKNOWN_ID, 'reasoning': reasoning(99)})
        final_health = restarted.send('GET', '/health', name='health after appeals/lookups')
    finally:
        restarted.stop()
    final_rows, final_errors = audit_rows(directory)
    checked = []
    for submission, appeal, lookup in zip(submissions, appeals, lookups):
        identity = appeal['content_id']
        original = original_decisions.get(identity, {})
        history = [x for x in final_rows if x.get('content_id') == identity]
        body = lookup.get('response_json', {})
        appeal_body = appeal['http'].get('response_json', {})
        saved_appeals = body.get('appeals', [])
        okay = (successful_submission(submission) and appeal['http'].get('status_code') == 200
                and appeal_body.get('status') == 'under_review' and appeal_body.get('reasoning') == appeal['reasoning']
                and len(history) == 2 and history[0] == original and history[1].get('event') == 'appeal'
                and history[1].get('reasoning') == appeal['reasoning'] and lookup.get('status_code') == 200
                and body.get('status') == 'under_review' and bool(original) and unchanged_decision(body, original)
                and len(saved_appeals) == 1 and saved_appeals[0].get('reasoning') == appeal['reasoning'])
        checked.append({'submission': submission, 'appeal': appeal, 'lookup': lookup,
                        'original': original, 'history': history, 'passed': okay})
    unknown_ok = json_error(unknown, 404) and not any(x.get('content_id') == UNKNOWN_ID and x.get('event') == 'appeal' for x in final_rows)
    detector_unloaded = final_health.get('response_json', {}).get('detector_loaded') is False
    prefix_preserved = after_appeal_bytes.startswith(original_bytes) and bool(original_bytes)
    unchanged = successful_domain_events(rows_before_restart) == successful_domain_events(final_rows)
    errors = original_errors + errors_before + final_errors
    count = sum(x['passed'] for x in checked)
    result.update(cases=checked, unknown_id_response=unknown, unknown_id_passed=unknown_ok,
                  original_audit_bytes_sha256=hashlib.sha256(original_bytes).hexdigest(),
                  original_audit_bytes_remain_prefix=prefix_preserved,
                  successful_events_unchanged_after_restart=unchanged,
                  restart_health=starts[-1]['health_at_start'], final_health=final_health,
                  detector_unloaded_after_lookups=detector_unloaded, audit_parse_errors=errors,
                  quota_window_valid=True, persistent_appeal_count=count,
                  http_passed=len(checked) == 10 and count == 10 and unknown_ok and prefix_preserved
                  and unchanged and not errors and result['detector_unloaded_at_restart'] and detector_unloaded,
                  summary=f'{count}/10 persistent appeals; unknown404={unknown_ok}; model unloaded={detector_unloaded}')
    return result


FUNCTIONS = {1: criterion_one, 2: criterion_two, 3: criterion_three, 4: criterion_four, 5: criterion_five}


def table(report):
    lines = ['| Criterion | Target | Run1 | Run2 | Run3 | Verdict |', '|---|---|---|---|---|---|']
    for key, row in report['criteria'].items():
        trials = [next((t for t in row['trials'] if t['trial'] == i), None) for i in range(1, 4)]
        values = [(t['summary'] + ('; isolated=' + str(t['companion']['passed']) if t['companion']['required'] else '')) if t else 'PENDING' for t in trials]
        lines.append(f'| {key}. {row["name"]} | {row["target"]} | ' + ' | '.join(values) + f' | {row["verdict"]} |')
    return '\n'.join(lines)


def update_report(report, output):
    for criterion in report['criteria'].values():
        trials = criterion['trials']
        criterion['verdict'] = ('MET' if len(trials) == 3 and all(t['passed'] for t in trials) else
                                'MISSED' if len(trials) == 3 else 'PENDING')
    save_json(output / 'report.json', report)
    markdown = [f'# Capstone campaign — {report["label"]}', '',
                f'Criteria SHA-256: `{report["source_sha256"]["criteria.md"]}`.', '',
                'Real GPT-2 HTTP trials; isolated companion call counts are explicitly mocked.', '', table(report), '',
                '## Actual trial1 output', '']
    for key, row in report['criteria'].items():
        if not row['trials']:
            continue
        trial = row['trials'][0]
        markdown.extend([f'### Criterion{key}', '', f'Produced by `scripts/run_capstone.py::criterion_{["zero", "one", "two", "three", "four", "five"][int(key)]}`.', '',
                         '```json', json.dumps(trial, indent=2, ensure_ascii=True), '```', ''])
    (output / 'report.md').write_text('\n'.join(markdown))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--label', required=True, choices=('before', 'after'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = (args.output or ROOT / 'results/capstone' / args.label).resolve()
    if output.exists() and any(output.iterdir()):
        parser.error('Output directory already contains evidence; choose another --output instead of overwriting it.')
    output.mkdir(parents=True, exist_ok=True)
    versions = {}
    for package in ('flask', 'flask-limiter', 'gunicorn', 'requests', 'torch', 'transformers'):
        try:
            versions[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            versions[package] = None
    report = {'label': args.label, 'started_at_utc': now(), 'status': 'RUNNING',
              'source_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
              'source_sha256': {name: sha(ROOT / name) for name in SOURCE_FILES if (ROOT / name).exists()},
              'environment': {'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(),
                              'machine': platform.machine(), 'processor': platform.processor(), 'packages': versions,
                              'workers': 1, 'threads': 1, 'inference': 'real local GPT-2, cached offline files',
                              'cost_method': 'serial worker per-request time.process_time CPU seconds; client perf_counter wall seconds'},
              'input_provenance': 'Existing ten historical-human development excerpts; three repetitions test engineering consistency, not independent authorship accuracy.',
              'criteria': {str(n): {'name': NAMES[n], 'target': TARGETS[n], 'trials': [], 'verdict': 'PENDING'} for n in range(1, 6)}}
    update_report(report, output)
    try:
        for number in range(1, 6):
            for trial in range(1, 4):
                attempts = []
                for attempt in range(1, 4):
                    directory = output / f'c{number}_trial{trial}_attempt{attempt}'
                    prefix = f'cap-{args.label}-c{number}-t{trial}-a{attempt}'
                    print(f'{args.label}: criterion{number} trial{trial} attempt{attempt} started', flush=True)
                    result = FUNCTIONS[number](directory, prefix)
                    result.update(trial=trial, attempt=attempt, criterion=number, evidence_directory=relative(directory))
                    attempts.append(result)
                    save_json(directory / 'trial.json', result)
                    if result['quota_window_valid']:
                        break
                    result['invalid_attempt_reason'] = 'Registered quota sequence crossed60s; full attempt retained and entire trial repeated.'
                    save_json(directory / 'trial.json', result)
                    print(result['invalid_attempt_reason'], flush=True)
                else:
                    raise RuntimeError(f'Criterion{number} trial{trial} exhausted3 attempts outside registered quota window')
                result['companion'] = companion(number, trial)
                result['passed'] = result['http_passed'] and result['companion']['passed']
                result['verdict'] = 'MET' if result['passed'] else 'MISSED'
                result['invalid_attempts'] = [relative(output / f'c{number}_trial{trial}_attempt{i}' / 'trial.json') for i in range(1, attempt)]
                save_json(directory / 'trial.json', result)
                report['criteria'][str(number)]['trials'].append(result)
                update_report(report, output)
                print(f'{args.label}: criterion{number} trial{trial}: {result["summary"]}; {result["verdict"]}', flush=True)
        finished_hashes = {name: sha(ROOT / name) for name in SOURCE_FILES if (ROOT / name).exists()}
        report.update(status='COMPLETE', finished_at_utc=now(),
                      finished_source_sha256=finished_hashes,
                      source_unchanged_during_campaign=finished_hashes == report['source_sha256'])
        if not report['source_unchanged_during_campaign']:
            raise RuntimeError('Source files changed during the campaign; preserve results as interrupted evidence')
        update_report(report, output)
        print(table(report), flush=True)
        print(f'Full captures: {relative(output / "report.json")}', flush=True)
    except BaseException as exc:
        report.update(status='INTERRUPTED', interrupted_at_utc=now(), error=f'{type(exc).__name__}: {exc}', traceback=traceback.format_exc())
        update_report(report, output)
        raise


if __name__ == '__main__':
    main()

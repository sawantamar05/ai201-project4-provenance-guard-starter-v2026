#!/usr/bin/env python3
"""Independently recompute capstone evidence and documentation checks.

This reads committed/raw HTTP evidence and logs; it sends no requests, loads no
model, and never changes criteria. Honest acceptance misses do not fail this
submission audit. Incorrect verdicts or missing evidence do.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import statistics
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.run_capstone import table  # formatting only; scoring is recomputed below

ORIGINAL = 'e7aa922'
CRITERIA_COMMIT = 'ded63f6'
LABELS = ['What This Extends', 'The Shape', 'Running It', 'Instrumentation',
          'What It Costs', 'Run Log and Verdicts', 'The Improvement',
          "What's Still Broken", 'How I Used AI']
STATUSES = [400, 400, 400, 400, 400, 413, 400, 400, 415, 413]
UNKNOWN = '00000000-0000-4000-8000-000000000099'


def git(*args, binary=False):
    result = subprocess.check_output(['git', *args], cwd=ROOT)
    return result if binary else result.decode().strip()


def digest(content):
    return hashlib.sha256(content).hexdigest()


def read(path):
    return json.loads((ROOT / path).read_text())


def rows(path):
    path = ROOT / path
    result = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    assert all(isinstance(row, dict) for row in result), path
    return result


def numeric(value):
    return not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value) and value >= 0


def same_number(a, b):
    return numeric(a) and numeric(b) and math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)


def error_response(response, expected):
    body = response.get('response_json')
    return response.get('status_code') == expected and isinstance(body, dict) and all(
        isinstance(body.get(key), str) and body[key].strip() for key in ('error', 'message'))


def decision(response):
    body = response.get('response_json', {})
    return (response.get('status_code') == 200 and isinstance(body, dict)
            and body.get('status') == 'decided' and bool(body.get('content_id'))
            and body.get('guess') in ('human', 'unsure', 'ai')
            and all(numeric(body.get(key)) and body[key] <= 1 for key in
                    ('model_score', 'style_score', 'combined_score', 'confidence'))
            and body.get('confidence') == body.get('combined_score'))


def domain_decisions(events):
    return [row for row in events if row.get('status') == 'decided']


def companion(trial, number):
    record = trial['companion']
    if number not in (1, 2, 5):
        assert record['required'] is False and record['passed'] is True
        return True
    assert record['required'] is True and record['returncode'] == 0
    result = record['result']
    assert result['criterion'] == number and result['trial'] == trial['trial']
    assert result['real_model_loaded'] is False
    if number == 1:
        assert [condition['pressure'] for condition in result['conditions']] == [False, True]
        recomputed = all(len(condition['cases']) == 10
                         and [row['case'] for row in condition['cases']] == list(range(1, 11))
                         and all(row['detector_calls'] == 0 for row in condition['cases'])
                         and condition['matrix_detector_calls'] == 0
                         and condition['successful_events_unchanged']
                         for condition in result['conditions'])
    elif number == 2:
        requests = result['requests']
        assert len(requests) == 24
        assert result['total_detector_calls'] == sum(row['detector_calls'] for row in requests)
        recomputed = ([row['status_code'] for row in requests] == [400] * 12 + [200] * 10 + [429] * 2
                      and [row['detector_calls'] for row in requests] == [0] * 12 + [1] * 10 + [0] * 2
                      and result['total_detector_calls'] == 10)
    else:
        assert len(result['setup']) == len(result['appeals']) == len(result['lookups']) == 10
        fresh = result['restarted']
        exact = all(row['status_code'] == 200 and row['response_json'].get('status') == 'under_review'
                    and row['response_json'].get('reasoning') == f'  Capstone review {i}: please consider my drafts.  '
                    for i, row in enumerate(result['appeals'], 1))
        recomputed = (all(decision(row) for row in result['setup'])
                      and result['submission_detector_calls'] == 10 and exact
                      and result['appeal_lookup_detector_calls'] == 0 and result['original_unchanged']
                      and fresh['detector_calls'] == 0 and fresh['detector_loaded'] is False
                      and fresh['statuses'] == [200] * 10 and result['unknown']['status_code'] == 404
                      and all(item.get('status') == 'under_review'
                              and len(item.get('appeals', [])) == 1
                              and item['appeals'][0]['reasoning'] == f'  Capstone review {i}: please consider my drafts.  '
                              for i, item in enumerate(fresh['items'], 1)))
    assert result['passed'] == recomputed
    assert record['passed'] == recomputed
    return recomputed


def session_records(starts):
    assert starts
    for start in starts:
        assert isinstance(start['pid'], int) and start['pid'] > 0
        assert start['stopped_at_utc'] and start['returncode'] == 0
        assert start['health_at_start']['rate_limiting'] is True
        assert start['environment_overrides']['AI201_RATE_LIMITS'] == '1'
        assert start['environment_overrides']['HF_HUB_OFFLINE'] == '1'
        command = start['command']
        assert command[command.index('--workers') + 1] == '1'
        assert command[command.index('--threads') + 1] == '1'
        assert (ROOT / start['log_directory'] / 'server.txt').exists()


def check_one(trial):
    assert len(trial['conditions']) == 2
    recomputed, total = [], 0
    for condition in trial['conditions']:
        session_records(condition['starts'])
        cases = condition['cases']
        assert len(cases) == 10 and [c['case'] for c in cases] == list(range(1, 11))
        assert [c['expected_status'] for c in cases] == STATUSES
        actual = [error_response(c['http'], expected) for c, expected in zip(cases, STATUSES)]
        assert [c['passed'] for c in cases] == actual
        assert numeric(condition['quota_sequence_seconds']) and condition['quota_sequence_seconds'] < 60
        assert condition['quota_window_valid'] is True
        directory = condition['starts'][0]['log_directory']
        events = rows(Path(directory) / 'audit.jsonl')
        allowed = [condition['warmup']]
        if condition['condition'] == 'pressure':
            assert len(condition['creator_pressure']) == len(condition['address_pressure']) == 12
            allowed += condition['creator_pressure']
        expected_ids = {x['response_json']['content_id'] for x in allowed if decision(x)}
        saved_ids = {x['content_id'] for x in domain_decisions(events)}
        no_success = expected_ids == saved_ids and not any(x.get('event') == 'appeal' for x in events)
        assert condition['successful_events_unchanged'] == no_success
        recomputed.append(all(actual) and no_success and not condition['audit_parse_errors'])
        assert condition['passed'] == recomputed[-1]
        total += sum(actual)
    assert trial['exact_status_count'] == total
    return all(recomputed)


def check_two(trial):
    session_records(trial['starts'])
    invalid, valid = trial['invalid_requests'], trial['valid_requests']
    assert len(invalid) == len(valid) == 12
    invalid_count = sum(error_response(row, 400) for row in invalid)
    valid_count = sum(decision(row) for row in valid[:10])
    quota_count = sum(error_response(row, 429) for row in valid[10:])
    assert trial['invalid400_count'] == invalid_count
    assert trial['valid200_count'] == valid_count
    assert trial['throttled429_count'] == quota_count
    events = rows(Path(trial['evidence_directory']) / 'audit.jsonl')
    creator = invalid[0]['request_json']['creator_id']
    assert all(row['request_json'] == {'creator_id': creator, 'text': ''} for row in invalid)
    assert all(row['request_json']['creator_id'] == creator for row in valid)
    saved = [row for row in domain_decisions(events) if row.get('creator_id') == creator]
    expected_ids = {row['response_json']['content_id'] for row in valid[:10] if decision(row)}
    assert trial['saved_decision_count'] == len(saved)
    return (invalid_count == 12 and valid_count == 10 and quota_count == 2 and len(saved) == 10
            and {row['content_id'] for row in saved} == expected_ids and not trial['audit_parse_errors'])


def completion_matches(record, exchange):
    headers = {key.lower(): value for key, value in exchange.get('response_headers', {}).items()}
    if not exchange.get('request_id') or headers.get('x-request-id') != exchange['request_id']:
        return False
    if (record.get('event') != 'request_completed' or record.get('request_id') != exchange.get('request_id')
            or record.get('http_status') != exchange.get('status_code') or record.get('method') != exchange['method']
            or record.get('path') != exchange['path']):
        return False
    stamp = datetime.fromisoformat(record['timestamp'].replace('Z', '+00:00'))
    if stamp.tzinfo is None or stamp.utcoffset().total_seconds() != 0:
        return False
    if not all(numeric(record.get(key)) for key in ('duration_ms', 'cpu_seconds')):
        return False
    incoming, outgoing = record['input_summary'], record['output_summary']
    if incoming.get('body_bytes') != exchange['request_body_bytes']:
        return False
    body = exchange.get('request_json')
    if isinstance(body, dict):
        if incoming.get('field_names') != sorted(body):
            return False
        if isinstance(body.get('text'), str) and incoming.get('text_characters') != len(body['text']):
            return False
        rendered = json.dumps(record, ensure_ascii=True)
        for key in ('text', 'reasoning'):
            if body.get(key) and json.dumps(body[key], ensure_ascii=True)[1:-1] in rendered:
                return False
    response = exchange.get('response_json', {})
    if outgoing.get('outcome') != ('error' if 'error' in response else 'success'):
        return False
    return all(outgoing.get(key) == response[key] for key in ('content_id', 'guess', 'error', 'status') if key in response)


def check_three(trial):
    session_records(trial['starts'])
    cases = trial['cases']
    assert len(cases) == 23
    events = rows(Path(trial['evidence_directory']) / 'requests.jsonl')
    ids = [row['http']['request_id'] for row in cases]
    assert len(set(ids)) == 23 and all(ids)
    count = 0
    for case in cases:
        exchange = case['http']
        matches = [event for event in events if event.get('request_id') == exchange['request_id']]
        actual = len(matches) == 1 and completion_matches(matches[0], exchange)
        assert case['passed'] == actual
        if actual:
            assert case['completion'] == matches[0]
        count += actual
    actual_statuses = [row['http']['status_code'] for row in cases]
    expected = [200] * 10 + [429] * 2 + [400] * 5 + [200] * 5 + [404]
    assert trial['completion_count'] == count
    assert trial['actual_statuses'] == actual_statuses and trial['expected_http_statuses'] == expected
    assert trial['outcome_sequence_matches'] == (actual_statuses == expected)
    return count == 23 and actual_statuses == expected and not trial['request_log_parse_errors']


def check_four(trial):
    session_records(trial['starts'])
    cases = trial['cases']
    assert len(cases) == 10
    successful = sum(decision(row) for row in cases)
    quick = sum(decision(row) and numeric(row['elapsed_seconds']) and row['elapsed_seconds'] < 5 for row in cases)
    assert trial['valid_count'] == successful and trial['under5_seconds_count'] == quick
    assert same_number(trial['mean_wall_seconds'], statistics.mean(row['elapsed_seconds'] for row in cases))
    assert trial['wall_seconds'] == [row['elapsed_seconds'] for row in cases]
    return successful == 10 and quick >= 9


def check_five(trial):
    starts = trial['starts']
    assert len(starts) == 2 and starts[0]['pid'] != starts[1]['pid']
    session_records(starts)
    assert datetime.fromisoformat(starts[0]['stopped_at_utc']) <= datetime.fromisoformat(starts[1]['started_at_utc'])
    assert starts[1]['health_at_start']['detector_loaded'] is False
    assert trial['final_health']['response_json']['detector_loaded'] is False
    events = rows(Path(trial['evidence_directory']) / 'audit.jsonl')
    assert len(trial['cases']) == 10
    count = 0
    for i, case in enumerate(trial['cases'], 1):
        expected_reason = f'  Capstone review {i}: please consider my drafts.  '
        appeal, lookup = case['appeal']['http'], case['lookup']
        identity, original = case['appeal']['content_id'], case['original']
        history = [x for x in events if x.get('content_id') == identity]
        current = lookup['response_json']
        okay = (decision(case['submission']) and appeal['status_code'] == 200
                and appeal['response_json'].get('status') == 'under_review'
                and appeal['response_json'].get('reasoning') == expected_reason
                and lookup['status_code'] == 200 and current.get('status') == 'under_review'
                and len(history) == 2 and history[0] == original and history[1].get('event') == 'appeal'
                and history[1].get('reasoning') == expected_reason
                and all(current.get(key) == value for key, value in original.items() if key != 'status')
                and len(current.get('appeals', [])) == 1 and current['appeals'][0]['reasoning'] == expected_reason)
        assert case['passed'] == okay and case['history'] == history
        count += okay
    unknown_ok = error_response(trial['unknown_id_response'], 404) and not any(
        row.get('content_id') == UNKNOWN and row.get('event') == 'appeal' for row in events)
    assert trial['unknown_id_passed'] == unknown_ok
    assert trial['persistent_appeal_count'] == count
    assert trial['original_audit_bytes_remain_prefix']
    assert trial['successful_events_unchanged_after_restart']
    return count == 10 and unknown_ok and not trial['audit_parse_errors']


SCORERS = {1: check_one, 2: check_two, 3: check_three, 4: check_four, 5: check_five}


def nested_objects(value):
    yield value
    if isinstance(value, dict):
        for item in value.values():
            yield from nested_objects(item)
    elif isinstance(value, list):
        for item in value:
            yield from nested_objects(item)


def pasted_objects(text):
    result = []
    for block in re.findall(r'```(?:json|jsonl)\s*\n([\s\S]*?)\n```', text):
        try:
            value = json.loads(block)
            result.extend(value if isinstance(value, list) else [value])
        except ValueError:
            for line in block.splitlines():
                if line.strip():
                    result.append(json.loads(line))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'results/capstone/final_audit.json')
    args = parser.parse_args()
    checks, details = {}, {}
    try:
        before = read('results/capstone/before/report.json')
        after = read('results/capstone/after/report.json')
        for phase in (before, after):
            assert phase['status'] == 'COMPLETE' and phase['source_unchanged_during_campaign']
            assert phase['source_sha256'] == phase['finished_source_sha256']
            assert list(phase['criteria']) == list('12345')
            assert phase['environment']['workers'] == phase['environment']['threads'] == 1
            for number in range(1, 6):
                criterion = phase['criteria'][str(number)]
                assert [trial['trial'] for trial in criterion['trials']] == [1, 2, 3]
                outcomes = []
                for trial in criterion['trials']:
                    assert trial['criterion'] == number and trial['quota_window_valid'] is True
                    if number in (2, 3):
                        assert trial['quota_sequence_seconds'] < 60
                    raw = SCORERS[number](trial)
                    calls = companion(trial, number)
                    assert trial['http_passed'] == raw
                    outcomes.append(raw and calls)
                    assert trial['passed'] == outcomes[-1]
                    assert trial['verdict'] == ('MET' if outcomes[-1] else 'MISSED')
                    assert not trial['invalid_attempts'], 'Inspect and support any retained invalid attempts explicitly before accepting this audit'
                assert criterion['verdict'] == ('MET' if all(outcomes) else 'MISSED')
            details[phase['label']] = {key: row['verdict'] for key, row in phase['criteria'].items()}
        checks['five_criteria_three_real_trials_each_and_literal_verdicts_recomputed'] = True
        checks['isolated_detector_call_evidence_matches_targets_and_is_explicitly_mocked'] = True
        checks['durable_completion_records_and_real_appeal_restarts_match_raw_responses'] = True
        assert before['environment'] == after['environment']
        assert set(before['source_sha256']) == set(after['source_sha256'])
        changed = [name for name in before['source_sha256'] if before['source_sha256'][name] != after['source_sha256'][name]]
        assert changed == ['app.py'], changed
        for name, expected in after['source_sha256'].items():
            assert digest((ROOT / name).read_bytes()) == expected, name
        checks['same_environment_criteria_corpus_models_and_harness_only_app_changed'] = True
        current_criteria = digest((ROOT / 'criteria.md').read_bytes())
        assert current_criteria == digest(git('show', CRITERIA_COMMIT + ':criteria.md', binary=True))
        assert current_criteria == before['source_sha256']['criteria.md'] == after['source_sha256']['criteria.md']
        assert (ROOT / 'docs/criteria_parts1_2.md').read_bytes() == git('show', ORIGINAL + ':criteria.md', binary=True)
        checks['capstone_criteria_unchanged_since_first_criteria_commit_originals_archived_exactly'] = True
        original_paths = git('ls-tree', '-r', '--name-only', ORIGINAL, '--', 'results', 'logs/audit.jsonl', 'attack_set', 'data',
                             'scoring.py', 'detector.py', 'stylometry.py', 'audit.py').splitlines()
        for name in original_paths:
            assert (ROOT / name).read_bytes() == git('show', ORIGINAL + ':' + name, binary=True), name
        details['preserved_original_file_count'] = len(original_paths)
        checks['all_original_results_logs_attack_sets_data_and_detector_sources_preserved'] = True
        commits = git('log', '--reverse', '--format=%H%x09%s', ORIGINAL + '..HEAD').splitlines()
        assert len(commits) >= 8
        criteria_hash = git('rev-parse', CRITERIA_COMMIT)
        first_results = git('log', '--reverse', '--diff-filter=A', '--format=%H', ORIGINAL + '..HEAD', '--',
                            'results/capstone/before/report.json').splitlines()[0]
        hashes = [row.split('\t', 1)[0] for row in commits]
        assert hashes.index(criteria_hash) < hashes.index(first_results)
        criteria_message = git('show', '-s', '--format=%s', criteria_hash).lower()
        results_message = git('show', '-s', '--format=%s', first_results).lower()
        assert 'criteria' in criteria_message and 'results' in results_message and 'capstone' in results_message
        build_commits = hashes[hashes.index(criteria_hash) + 1:hashes.index(first_results)]
        assert len(build_commits) >= 3
        details.update(new_capstone_commits=len(commits), criteria_commit=criteria_hash,
                       first_results_commit=first_results, build_commits_before_results=build_commits)
        checks['eight_new_commits_criteria_before_named_results_and_three_build_commits'] = True
        readme = (ROOT / 'README.md').read_text()
        assert readme.count('\n## Capstone\n') == 1
        assert readme.rfind('\n## ') == readme.index('\n## Capstone\n')
        capstone = readme.split('\n## Capstone\n', 1)[1]
        for label in LABELS:
            assert capstone.count('**' + label + '**') == 1, label
        assert not re.search(r'^### ', capstone, re.M)
        assert table(before) in capstone and table(after) in capstone
        checks['final_capstone_heading_nine_bold_sections_and_both_complete_tables'] = True
        pasted = pasted_objects(capstone)
        actual = []
        for phase in ('before', 'after'):
            for path in (ROOT / 'results/capstone' / phase).glob('**/requests.jsonl'):
                actual += rows(path.relative_to(ROOT))
        completions = [obj for obj in pasted if isinstance(obj, dict) and obj.get('event') == 'request_completed']
        assert len({obj['request_id'] for obj in completions}) >= 11
        assert any(obj['http_status'] >= 400 for obj in completions)
        assert all(obj in actual for obj in completions)
        checks['at_least_ten_plus_one_failure_literal_completion_records_pasted'] = True
        trial_markers = list(re.finditer(r'^\*\*Criterion ([1-5])[^\n]*\*\*', capstone, re.M))
        assert {match.group(1) for match in trial_markers} == set('12345')
        for index, marker in enumerate(trial_markers):
            number = marker.group(1)
            section = capstone[marker.end():trial_markers[index + 1].start() if index + 1 < len(trial_markers) else len(capstone)]
            snippet_objects = pasted_objects(section)
            candidates = []
            for campaign in (before, after):
                trial = campaign['criteria'][number]['trials'][0]
                candidates.extend(obj['response_json'] for obj in nested_objects(trial)
                                  if isinstance(obj, dict) and 'response_json' in obj)
                candidates.extend(obj for obj in nested_objects(trial)
                                  if isinstance(obj, dict) and obj.get('event') == 'request_completed')
                for exchange in nested_objects(trial):
                    if isinstance(exchange, dict) and all(key in exchange for key in ('status_code', 'elapsed_seconds', 'response_json', 'request_id')):
                        candidates.append({key: exchange[key] for key in ('status_code', 'elapsed_seconds', 'response_json', 'request_id')})
            assert any(obj in candidates for obj in snippet_objects), 'Missing literal trial1 output for criterion' + number
            assert 'scripts/run_capstone.py' in section, 'Missing output producer for criterion' + number
        checks['each_criterion_has_literal_trial1_output_and_named_producer'] = True
        cost = read('results/capstone/cost.json')
        trial = after['criteria']['4']['trials'][0]
        ids = [exchange['request_id'] for exchange in trial['cases']]
        events = rows(Path(trial['evidence_directory']) / 'requests.jsonl')
        samples = []
        for identity in ids:
            matching = [event for event in events if event.get('request_id') == identity]
            assert len(matching) == 1 and numeric(matching[0]['cpu_seconds'])
            samples.append(matching[0]['cpu_seconds'])
        mean_cpu = statistics.mean(samples)
        mean_wall = statistics.mean(exchange['elapsed_seconds'] for exchange in trial['cases'])
        assert cost['sample_count'] == 10 and cost['cpu_samples'] == samples
        assert same_number(cost['mean_cpu_seconds'], mean_cpu)
        assert same_number(cost['hundred_per_day_cpu_seconds'], mean_cpu * 100)
        assert same_number(cost['mean_wall_seconds'], mean_wall)
        assert 'after' in cost['source_path'] and 'process_time' in json.dumps(cost)
        assert same_number(trial['mean_cpu_seconds'], mean_cpu) and not trial['cost_measurement_errors']
        cost_section = capstone.split('**What It Costs**', 1)[1].split('**Run Log and Verdicts**', 1)[0]
        assert '100' in cost_section and ('CPU' in cost_section or 'cpu' in cost_section)
        assert any(format(mean_cpu, f'.{places}f') in cost_section for places in range(4, 10))
        assert any(format(mean_cpu * 100, f'.{places}f') in cost_section for places in range(3, 10))
        checks['measured_ten_run_cpu_cost_and_hundred_a_day_arithmetic_recomputed'] = True
        details['cost'] = {'mean_cpu_seconds': mean_cpu, 'hundred_per_day_cpu_seconds': mean_cpu * 100,
                           'mean_wall_seconds': mean_wall}
        clean = read('results/capstone/clean_checkout.json')
        assert clean['all_checks_passed'] and all(clean['checks'].values())
        assert clean['source_commit'] and len(clean['sessions']) == 2
        for name, expected in after['source_sha256'].items():
            assert digest(git('show', clean['source_commit'] + ':' + name, binary=True)) == expected, ('clean checkout source', name)
        assert clean['environment']['all_exact'] and not clean['model']['download_exercised']
        assert clean['dependency_lock_sha256'] == digest((ROOT / 'requirements-lock.txt').read_bytes())
        checks['clean_checkout_fresh_environment_exact_lock_real_inference_restart_and_logs_verified'] = True
        for relative in ('README.md', 'RUNNING.md', 'criteria.md', 'SUBMISSION.md'):
            path = ROOT / relative
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' not in target and not target.startswith('#'):
                    assert (path.parent / target.split('#')[0]).exists(), (relative, target)
        checks['submission_document_local_links_resolve'] = True
    except Exception as exc:
        import traceback
        details['error'] = {'type': type(exc).__name__, 'message': str(exc), 'traceback': traceback.format_exc()}
    report = {'recorded_at_utc': datetime.now(timezone.utc).isoformat(), 'source_commit': git('rev-parse', 'HEAD'),
              'checks': checks, 'details': details, 'all_evidence_checks_passed': 'error' not in details,
              'scope': 'Read-only evidence/scoring audit; criterion misses are allowed when correctly reported. No models or HTTP requests executed.',
              'portal_submission': 'The user submits the existing GitHub repository URL through the Course Portal.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=True, allow_nan=False) + '\n')
    print(json.dumps(report, indent=2))
    return 0 if report['all_evidence_checks_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())

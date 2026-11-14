#!/usr/bin/env python3
"""Render the capstone README suffix from completed, preserved campaign evidence.

This does not run the service, change a target, or replace a campaign. Only the
README Capstone suffix and the derived cost measurement are written.
"""

import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.run_capstone import table  # noqa: E402


def read(relative):
    return json.loads((ROOT / relative).read_text())


def pretty(value):
    return '```json\n' + json.dumps(value, indent=2, ensure_ascii=True, allow_nan=False) + '\n```'


def completed_report(label):
    report = read(f'results/capstone/{label}/report.json')
    assert report['status'] == 'COMPLETE', f'{label} campaign is not complete'
    assert report['source_unchanged_during_campaign'] is True
    assert list(report['criteria']) == list('12345')
    for criterion in report['criteria'].values():
        assert [trial['trial'] for trial in criterion['trials']] == [1, 2, 3]
    return report


def cost_measurement(after):
    trial = after['criteria']['4']['trials'][0]
    assert not trial['cost_measurement_errors']
    cpu = trial['cpu_seconds']
    wall = trial['wall_seconds']
    assert len(cpu) == len(wall) == 10
    assert all(not isinstance(x, bool) and isinstance(x, (int, float))
               and math.isfinite(x) and x >= 0 for x in cpu + wall)
    mean_cpu = sum(cpu) / 10
    mean_wall = sum(wall) / 10
    assert math.isclose(mean_cpu, trial['mean_cpu_seconds'])
    assert math.isclose(mean_wall, trial['mean_wall_seconds'])
    return {
        'sample_count': 10,
        'source_path': trial['evidence_directory'],
        'source_report': 'results/capstone/after/report.json',
        'source_commit': after['source_commit'],
        'trial': 1,
        'request_ids': [row['request_id'] for row in trial['cases']],
        'cpu_samples': cpu,
        'wall_samples': wall,
        'sum_cpu_seconds': sum(cpu),
        'mean_cpu_seconds': mean_cpu,
        'mean_wall_seconds': mean_wall,
        'hundred_per_day_cpu_seconds': 100 * mean_cpu,
        'hundred_per_day_assumption': '100 people, one accepted warm submission per person per day',
        'method': ('Mean of ten real sequential accepted HTTP submissions. CPU uses '
                   'time.process_time deltas in one synchronous Gunicorn worker; '
                   'wall time uses client perf_counter through complete response/JSON parsing.'),
        'cpu_exclusions': ['initial model load', 'completion-log serialization and fsync',
                           'client/network CPU', 'additional appeals and other requests'],
        'money_measurement': 'No paid inference API called; electricity/hosting dollars were not measured.',
        'other_trials': [
            {'trial': row['trial'], 'sample_count': len(row['cpu_seconds']),
             'mean_cpu_seconds': row['mean_cpu_seconds'], 'mean_wall_seconds': row['mean_wall_seconds']}
            for row in after['criteria']['4']['trials'][1:]
        ],
    }


def snippet(label, phase, source, value):
    return f'**Criterion {label} — actual output ({phase})**\n\n{source}\n\n{pretty(value)}\n'


def evidence_snippets(report):
    """Paste literal evidence for all five criteria directly under each run log."""
    phase = report['label']
    base = f'results/capstone/{phase}'
    trials = {key: row['trials'][0] for key, row in report['criteria'].items()}
    validation = trials['1']['conditions'][1]['cases'][0]['http']
    allowance = trials['2']['valid_requests'][0]
    completion = trials['3']['cases'][0]['completion']
    timed = trials['4']['cases'][0]
    timed_projection = {key: timed[key] for key in ('status_code', 'elapsed_seconds', 'response_json', 'request_id')}
    persisted = trials['5']['cases'][0]['lookup']
    rows = [
        ('1', f'{phase.title()} trial 1, pressure case 1: expected HTTP 400, actual '
         f'HTTP {validation["status_code"]}. Produced by `scripts/run_capstone.py::criterion_one`; '
         f'complete request/response in [the pressure capture]({base}/c1_trial1_attempt1/pressure/http_01.json).',
         validation['response_json']),
        ('2', f'{phase.title()} trial 1, first valid request after 12 malformed requests: '
         f'HTTP {allowance["status_code"]}. Produced by `scripts/run_capstone.py::criterion_two`; '
         f'saved in [the trial capture]({base}/c2_trial1_attempt1/http_01.json).', allowance['response_json']),
        ('3', f'{phase.title()} trial 1, one actual durable completion. Produced by '
         '`telemetry.py::complete_request` and checked by `scripts/run_capstone.py::criterion_three`; '
         f'saved in [the request log]({base}/c3_trial1_attempt1/requests.jsonl).', completion),
        ('4', f'{phase.title()} trial 1, first timed warm response. This projection preserves '
         'the actual status, elapsed time, complete response JSON, and request ID. Produced by '
         '`scripts/run_capstone.py::criterion_four`; full capture in '
         f'[the trial HTTP record]({base}/c4_trial1_attempt1/http_01.json).', timed_projection),
        ('5', f'{phase.title()} trial 1, actual content response from the restarted server: '
         f'HTTP {persisted["status_code"]}. Produced by `scripts/run_capstone.py::criterion_five`; '
         f'saved in [the restarted-process capture]({base}/c5_trial1_attempt1/http_02.json).',
         persisted['response_json']),
    ]
    return '\n'.join(snippet(number, phase, source, value) for number, source, value in rows)


def render(before, after, cost):
    assert before['source_sha256']['criteria.md'] == after['source_sha256']['criteria.md']
    changed = [name for name in before['source_sha256']
               if before['source_sha256'][name] != after['source_sha256'].get(name)]
    assert changed == ['app.py'], changed
    assert [row['verdict'] for row in before['criteria'].values()] == ['MISSED', 'MISSED', 'MET', 'MET', 'MET']
    assert all(row['verdict'] == 'MET' for row in after['criteria'].values())
    observed = after['criteria']['3']['trials'][0]['cases']
    extract = [row['completion'] for row in observed[:13]]
    assert len(extract) == 13
    assert [row['http_status'] for row in extract] == [200] * 10 + [429, 429, 400]
    log_lines = '\n'.join(json.dumps(row, ensure_ascii=True, separators=(',', ':')) for row in extract)
    clean = read('results/capstone/clean_checkout.json')
    assert clean['all_checks_passed'] and len(clean['checks']) == 9 and all(clean['checks'].values())
    assert len(clean['environment']['packages']) == 40 and clean['environment']['all_exact']
    assert clean['model']['download_exercised'] is False
    after_max = max(row['elapsed_seconds'] for trial in after['criteria']['4']['trials'] for row in trial['cases'])
    assert after_max < 0.25, 'Choose an honest tighter future target based on the recorded distribution'
    before_means = [row['mean_wall_seconds'] for row in before['criteria']['4']['trials']]
    after_means = [row['mean_wall_seconds'] for row in after['criteria']['4']['trials']]
    cold_times = [row['cold_warmup']['elapsed_seconds'] for row in after['criteria']['4']['trials']]
    cpu = cost['mean_cpu_seconds']
    wall = cost['mean_wall_seconds']
    repeats = '; '.join(f"trial {row['trial']}: {row['mean_cpu_seconds']:.7f} CPU-s, {row['mean_wall_seconds']:.7f} wall-s"
                        for row in cost['other_trials'])
    side_by_side = '\n'.join([
        '| Criterion | Before, all three trials | After, all three trials | Change |',
        '|---|---|---|---|',
        '| 1. Validation under pressure | 10/20 exact; MISSED | 20/20 exact; MET | Pressure cases now return their validation code |',
        '| 2. Scoring allowance | 10/12 invalid 400; 0/10 valid 200; MISSED | 12/12 invalid 400; 10/10 valid 200; MET | Invalid requests no longer consume valid slots |',
        '| 3. Request completions | 23/23; MET | 23/23; MET | Complete records retained |',
        '| 4. Warm response time | 10/10 complete and below 5s; MET | 10/10 complete and below 5s; MET | Target retained; timing variation is not a claimed speedup |',
        '| 5. Persistent appeals | 10/10; MET | 10/10; MET | Appeal protection retained |',
    ])
    return f'''## Capstone

**What This Extends**

I extended the existing Provenance Guard Flask API with predictable validation
and quota handling, plus durable request completion records and measured run
cost. This is the same repository and detector from Project 4. The new targets
are in [criteria.md](criteria.md); the earlier targets are preserved unchanged in
[docs/criteria_parts1_2.md](docs/criteria_parts1_2.md). The criteria existed in Git
before capstone evaluation, and both campaigns record the identical criteria
SHA-256 `{after['source_sha256']['criteria.md']}`.

**The Shape**

I chose **B — Harden against failure**: malformed submissions should receive
their validation error without consuming the allowance for valid scoring.
Request timing, failure traces, and the local run path support that one change.
Model retraining, threshold changes, a new interface, public hosting,
authenticated identities, and shared quota storage stayed outside this unit.
No stretch work was declared. The before campaign is an instrumented baseline
with the old quota order, not the original uninstrumented starter.

**Running It**

I used **Path B — local with logs**. [RUNNING.md](RUNNING.md) gives the exact
single-worker Gunicorn start command, pinned setup, model preparation, isolated
log directories, and clean-checkout verification. The environment and model
inventory are recorded in [docs/capstone_environment.md](docs/capstone_environment.md).
Each trial started an actual local HTTP server outside the editor. Criterion 5
stopped that server and started a fresh process against the same saved audit.
The committed campaigns include the launch commands, process records, HTTP
captures, request logs, and both five-row run logs.

I also verified a [clean checkout](results/capstone/clean_checkout.json) at
commit `{clean['source_commit'][:7]}`: a fresh clone and new virtual environment
installed all **40 exact dependency pins**, and **all nine checks passed**,
including real inference, exact appeal persistence across a restart, and saved
request completions. This reused the previously downloaded GPT-2 cache
explicitly; it was not an online model-download test.

**Instrumentation**

`telemetry.start_request` starts before validation and rate limiting;
`telemetry.complete_request` writes one `request_completed` record to
`requests.jsonl`, separately from decision/appeal events in `audit.jsonl`.
Each completion contains a UTC timestamp, a generated request ID matching
`X-Request-ID`, method/path, response status, input/output summaries, wall
duration, and process CPU seconds. Input summaries retain byte counts, JSON
field names, parsing outcome, and text length; output summaries retain content
ID, guess, status, or error. Submission text and appeal-reasoning values are
omitted from this new log. The appeal audit still preserves reasoning exactly.

These **13 actual entries** are the first ten valid submissions, two quota
rejections, and one malformed-input rejection from after criterion 3, trial 1.
They are pasted from [that session's request log](results/capstone/after/c3_trial1_attempt1/requests.jsonl),
with their values unchanged:

```jsonl
{log_lines}
```

All 23 measured requests had exactly one correlated completion in each before
and after trial, including validation 400, quota 429, and unknown-appeal 404.
Healthy writable storage is part of this measurement: a failed log write cannot
produce a durable record. The service exposes that failure as JSON 503 and a
server error log, and the isolated telemetry tests check that behavior.

**What It Costs**

One run here means one accepted, warm paragraph submission. In after criterion
4, trial 1, I measured ten real requests: **{cpu:.7f} process CPU seconds per
run** and **{wall:.7f} seconds mean client wall time**. The CPU sample sum was
`{cost['sum_cpu_seconds']:.6f} / 10 = {cpu:.7f}`; the raw ten CPU and wall samples,
correlation IDs, method, and arithmetic are in
[results/capstone/cost.json](results/capstone/cost.json).

The worker uses `time.process_time()` before/after route handling and summary
preparation, before completion serialization/fsync. Client wall time includes
the complete response and JSON parsing, including the log append. CPU time
excludes initial model load, completion serialization/fsync, and client/network
CPU. Torch can use multiple CPU threads, so process CPU time can exceed wall
time even with one synchronous HTTP worker. Repeated measurements were {repeats}.
Cold model-loading requests were disclosed separately: {', '.join(f'{x:.4f}s' for x in cold_times)}
in the three after timing trials.

For **100 people per day, one accepted warm submission each**:
`100 × {cpu:.7f} = {cost['hundred_per_day_cpu_seconds']:.5f} process CPU seconds/day`.
Appeals, additional requests, and cold loads add work beyond this multiplication.
No paid inference API was called in these offline sessions. Electricity and
hosting dollars were not measured, so these numbers are a compute measurement
rather than a dollar-cost claim.

**Run Log and Verdicts**

The before campaign used commit `{before['source_commit'][:7]}`. I ran all five
criteria three times without changing the system between trials. A target had
to hold in every trial; the two missed criteria remain **MISSED** here.
Full outputs: [before JSON](results/capstone/before/report.json) and
[before run log](results/capstone/before/report.md).

{table(before)}

**Diagnosis of criterion 1:** the Flask-Limiter request hook ran before
`submit` reached validation. After ten valid submissions, the creator bucket
returned 429 for malformed requests with that ID. Separately, malformed requests
without a usable ID filled the address fallback bucket. All ten pressure-matrix
cases therefore received 429 rather than their required 400/413/415; all ten
ordinary cases were correct. The stage was quota enforcement, and the mechanism
was validation occurring after quota lookup and accounting.

**Diagnosis of criterion 2:** the same ordering charged the first ten empty-text
requests to the valid creator's ten-slot bucket. The last two malformed requests
then returned 429, and all twelve subsequent valid requests were throttled.
This left 10/12 invalid 400 responses and zero accepted valid requests in every
trial. Both misses were one request-ordering problem with two effects.

Criteria 3–5 were **MET**: completion records covered all 23 measured requests,
all ten warm submissions returned complete decisions below 5s, and all ten
appeals survived an actual restart without rescoring. Those results cover this
small serial local workload; they do not establish accuracy, production load
capacity, or durability when the disk itself cannot accept a write.

{evidence_snippets(before)}

**The Improvement**

I made **one runtime improvement**: validate cheap submission input before
Flask-Limiter checks/charges scoring quota. A request hook now calls
`app.py::_validate_submission` and caches the valid text/creator tuple in
`g.validated_submission`; `submit` reuses it. Invalid requests return their
400/413/415 immediately and do not consume the model-scoring allowance. Valid
requests still receive ten slots per minute and 200 per day, and the next two
valid requests in the registered burst still return 429.

Only `app.py` differs among the frozen runtime/harness/input source hashes
between the campaigns. Model, thresholds, signal weights, corpus, quotas,
telemetry, and the evaluation protocol remained unchanged. The after campaign
used commit `{after['source_commit'][:7]}` and repeated the full five criteria,
three trials each. Sources: [after JSON](results/capstone/after/report.json) and
[after run log](results/capstone/after/report.md).

{table(after)}

{side_by_side}

The improvement helped the diagnosed failure: exact validation responses rose
from 10/20 to 20/20, and accepted valid allowance requests rose from 0/10 to 10/10
in every trial. The other three criteria remained MET. Mean warm client times
were {', '.join(f'{x:.4f}s' for x in before_means)} before and
{', '.join(f'{x:.4f}s' for x in after_means)} after; this small variation does not
support a claim that validation ordering made model inference faster.

{evidence_snippets(after)}

**What's Still Broken**

All five after criteria were MET, but the warm-latency target was too generous
for this measured workload. The slowest of all 30 after warm requests was
{after_max:.7f}s. In a future registration I would tighten criterion 4 from 9/10
below 5s to **10/10 below 0.25s** on the same hardware and frozen passages. I have
kept the current target and both original result sets unchanged.

Creator IDs remain caller supplied and can be rotated to bypass a quota.
In-memory counters reset when the server restarts and do not coordinate
multiple workers. Invalid requests no longer spend scoring quota, so they need
a separate front-door abuse cap if this becomes a public service. Completion
logging depends on writable disk: an append failure can return 503 after a
decision has already been persisted, requiring operator inspection before a
retry. The detector remains a heuristic, not proof of authorship; these
historical passages and repeated engineering trials do not establish general
authorship accuracy. I stopped at the scoped validation/quota improvement and
kept the service local rather than expand this unit into an identity, hosting,
or storage redesign.

With another unit, I would first tie submission quotas to an authenticated
caller identity, because rotating a self-declared ID bypasses the present
control. I would validate that identity boundary before adding shared durable
quota storage, so persistence does not preserve the wrong ownership model.

**How I Used AI**

I asked Codex to compare my four CodePath systems against this brief. It
recommended Provenance Guard's existing API and recorded validation/quota miss;
I selected Shape B and kept model training and a new interface outside the scope.

I asked Codex to draft first-person criteria and told it that my instructor
permits this assistance. It supplied targets, reasons, and test procedures;
review clarified that creator and address quotas need separate pressure and
that request completions must be counted separately from decision/appeal audit
events. This was AI-assisted drafting and review, not unaided criteria writing
or a peer review session.

I then asked Codex to implement, instrument, and evaluate the bounded extension.
It produced the real-HTTP runner and explicitly mocked call-count companion.
The baseline showed two misses with the same quota-ordering mechanism, so the
measured change moved validation before quota accounting and retained both
result sets. AI also generated this write-up from the saved responses and CPU
samples; the JSON/JSONL artifacts, source hashes, and commit history are the
evidence behind the claims.
'''


def main():
    before = completed_report('before')
    after = completed_report('after')
    cost = cost_measurement(after)
    suffix = render(before, after, cost)
    readme_path = ROOT / 'README.md'
    content = readme_path.read_bytes()
    marker = b'\n## Capstone\n'
    assert content.count(marker) == 1, 'README must have exactly one Capstone suffix'
    prefix = content.split(marker, 1)[0]
    readme_path.write_bytes(prefix + b'\n' + suffix.encode())
    path = ROOT / 'results/capstone/cost.json'
    path.write_text(json.dumps(cost, indent=2, ensure_ascii=True, allow_nan=False) + '\n')
    print('Generated nine Capstone sections from two COMPLETE campaigns; preserved earlier README bytes.')
    print(f"Measured {cost['sample_count']} warm runs: {cost['mean_cpu_seconds']:.7f} CPU-s/run; "
          f"{cost['mean_wall_seconds']:.7f} wall-s/run.")


if __name__ == '__main__':
    main()

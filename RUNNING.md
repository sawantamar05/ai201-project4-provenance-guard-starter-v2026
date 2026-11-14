# Running Provenance Guard

Provenance Guard is a local JSON API. It combines a GPT-2 predictability signal
with stylometry, saves each decision, and records appeals for review. It needs
no API key. Model files download once; inference runs on your machine.

## Capstone — Path B: local with logs

This is the capstone run path. The later sections preserve the earlier project
instructions and results. The measured environment is **Python 3.13.3 on macOS
Apple Silicon**; a fresh installation on another Python version or platform has
not been verified for this capstone. Gunicorn uses the Flask WSGI callable
`app:app`, as documented by [Gunicorn](https://gunicorn.org/reference/settings/)
and [Flask](https://flask.palletsprojects.com/en/stable/deploying/index.html).

From a clean checkout, create a new environment and install the exact versions:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python -m pip check
```

The capstone uses all 40 pinned packages in `requirements-lock.txt`, including
Flask, Flask-Limiter, Gunicorn, PyTorch, Transformers, and Requests. The virtual
environment is not committed and is not copied from an existing checkout.

**Prepare model files once.** This command allows the initial GPT-2 download
into the project cache, then loads it without scoring an evaluation passage:

```bash
HF_HOME="$PWD/.cache/huggingface" HF_HUB_OFFLINE=0 .venv/bin/python -c 'import detector; print(detector.warm_up())'
```

The measured GPT-2 revision is
`607a30d783dfa663caf39e06633721c8d4cfcd7e`: seven snapshot files totaling
**550,959,861 bytes** (525.44 MiB), including 548,105,171 bytes of model weights.
The cache uses symlinks into blobs; these sizes count each snapshot file once.
See [the environment record](docs/capstone_environment.md) for the inventory.

To reuse an existing cache instead, set `HF_HOME` to the absolute directory
containing its `hub` folder before the following commands:

```bash
export HF_HOME="/absolute/path/to/existing/huggingface"
HF_HUB_OFFLINE=1 .venv/bin/python -c 'import detector; print(detector.warm_up())'
```

Cache reuse verifies offline model loading; it does not verify a new model
download or make dependency installation offline. If `HF_HOME` is unset, the
service defaults to this checkout's `.cache/huggingface` directory. Inference
needs no API key. A missing or unusable model returns JSON HTTP 503.

**Start the service with one command** from the project directory:

```bash
HF_HUB_OFFLINE=1 AI201_RATE_LIMITS=1 AI201_LOG_DIR="$PWD/logs/local" .venv/bin/gunicorn --workers 1 --threads 1 --bind 127.0.0.1:5054 --timeout 120 app:app
```

The address is `http://127.0.0.1:5054`. The explicit log directory preserves the
earlier project's `logs/audit.jsonl`. This session appends decision, rejection,
and appeal events to `logs/local/audit.jsonl`, and one `request_completed`
event per completed request to `logs/local/requests.jsonl`. The response's
`X-Request-ID` matches its completion record. Submitted writing and appeal
reasoning are omitted from completion records; the separate appeal audit
intentionally preserves the exact reasoning.

Each server process loads the model on its first valid submission. A separate
warm-up command has populated the disk cache, but has not loaded the model
into the running server. Report that first request separately from warm-request
latency. Completion `duration_ms` and `cpu_seconds` measure route work and
summary preparation up to the point before serializing, writing, and fsyncing
the completion record. They exclude that final logging work and client/network
time. Client timings in the evaluation include receiving and parsing the
complete response. CPU time is process CPU, so attributing it to one request
requires this single synchronous worker/thread and sequential requests.

**Exercise HTTP from a second terminal.** Inspect the returned content ID and
use it in the appeal request; the placeholder below is not a real saved ID.

```bash
curl -i http://127.0.0.1:5054/health
curl -i -X POST http://127.0.0.1:5054/submit \
  -H 'Content-Type: application/json' --data-binary @data/sample_submission.json
curl -i -X POST http://127.0.0.1:5054/appeal \
  -H 'Content-Type: application/json' \
  -d '{"content_id":"PASTE_RETURNED_CONTENT_ID","reasoning":"Please review my drafts."}'
curl -i -X POST http://127.0.0.1:5054/submit \
  -H 'Content-Type: application/json' -d '{"text":"","creator_id":"local-demo"}'
curl -i -X POST http://127.0.0.1:5054/appeal \
  -H 'Content-Type: application/json' \
  -d '{"content_id":"00000000-0000-4000-8000-000000000099","reasoning":"Unknown-ID check."}'
```

A successful submission returns 200; the valid appeal returns 200 with
`under_review`; the empty-text example should return 400; and the unused UUID
should return 404. Repeated valid submissions with the same creator ID are
limited to ten per minute and 200 per day. Keep all error responses and their
request records when checking these expectations.

Stop the first terminal with **Ctrl-C**, then run the exact same start command
again with the same log directory. `GET /content/PASTE_RETURNED_CONTENT_ID`
must reconstruct the original decision and appeal status from the saved audit.
The in-memory quota counters reset on restart; this persistence check concerns
decisions and appeals, not durable quotas.

**Reproduce the recorded campaigns without replacing evidence.**
`scripts/run_capstone.py` starts and stops isolated one-worker Gunicorn sessions
itself; no manually running server is needed. The committed `before` campaign
belongs to the instrumented baseline before the quota-order improvement. The
final code has different route behavior: running it with `--label before`
would not recreate that baseline. Use the baseline source commit recorded in
the report when reproducing it, and always select a new output directory:

```bash
.venv/bin/python scripts/run_capstone.py --label after --output results/capstone/recheck-after
```

That command runs all five registered criteria three times each, saves actual
HTTP responses and isolated session logs, and includes separately labelled
mocked detector-call evidence. The mocked checks are not latency evidence.
Targets are in [criteria.md](criteria.md); the earlier project's evaluator
still measures the archived [Part 1/2 targets](docs/criteria_parts1_2.md).

After committing the code being tested, verify startup from a new clone and a
new virtual environment:

```bash
.venv/bin/python scripts/verify_clean_checkout.py \
  --model-cache "$PWD/.cache/huggingface" \
  --output "$PWD/results/capstone/clean_checkout.json"
```

This installs the lock file in that new environment, starts an equivalent
Gunicorn command on a free loopback port, performs a real submission and appeal,
restarts the process, and checks persisted state and completion records. It
explicitly shares the previously downloaded model cache. The resulting JSON
identifies the source commit and retains setup/server logs in its temporary
checkout; inspect `all_checks_passed` before claiming success. Use a new output
filename for additional checks to retain the original record.

## Install and prepare the model

Use Python 3.11, 3.12, or 3.13. Run these commands from the project directory:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python test.py
python detector.py
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. If your `python3`
command points to another Python version, use an installed supported version
such as `python3.13` when creating the environment.

The first detector run downloads approximately 550 MB. By default, `config.py`
uses `.cache/huggingface` inside this project. An existing `HF_HOME` environment
setting overrides that default. The cache and virtual environment stay out of
version control. A detector failure returns HTTP 503; the service does not
substitute a made-up score.

To load the model without scoring a sample:

```bash
python -c 'import detector; print(detector.warm_up())'
```

## Start the service

In the first terminal, with the virtual environment active:

```bash
python app.py
```

The default address is `http://127.0.0.1:5000`. Debug mode is off. If port 5000
is occupied, start on another port and use that address in subsequent commands:

```bash
PORT=5054 python app.py
```

After the model has been downloaded, you can require cached files only:

```bash
HF_HUB_OFFLINE=1 PORT=5054 python app.py
```

Each server process loads its model on its first submission and reuses it for
later requests. Warming the cache in a separate command avoids another download;
the server still needs to load those files into its own memory.

## Send requests from a second terminal

Activate the same environment and run from the project directory. These
examples use the default port:

```bash
source .venv/bin/activate
curl http://127.0.0.1:5000/health
curl -X POST http://127.0.0.1:5000/ping \
  -H 'Content-Type: application/json' \
  -d '{"message":"hello"}'
```

`/ping` is the control route. `/health` reports `detector_loaded`, the model
name, rate-limit state, and the audit entry count. A separate process's warm-up
does not make the running server's `detector_loaded` field true.

Create a real submission-and-appeal demonstration:

```bash
python scripts/demo.py --url http://127.0.0.1:5000
```

The script submits the first explicitly AI-generated development passage,
appeals that returned content ID, and reads its log and current status. It
saves actual HTTP exchanges in `results/sample_run.json` and writes reusable
request bodies to `data/sample_submission.json` and `data/sample_appeal.json`.

You can send those saved bodies with curl:

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample_submission.json
curl -X POST http://127.0.0.1:5000/appeal \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample_appeal.json
curl 'http://127.0.0.1:5000/log?limit=5'
DEMO_CONTENT_ID=$(python -c 'import json; print(json.load(open("data/sample_appeal.json"))["content_id"])')
curl "http://127.0.0.1:5000/content/$DEMO_CONTENT_ID"
```

The saved appeal targets the demonstration's original content ID. A later
submission gets a new ID; use its returned ID to appeal that newer item.
Repeated appeals append separate events and keep the item `under_review`.

In PowerShell, use `curl.exe` on one line. File-based JSON bodies avoid shell
quoting differences; for example:

```powershell
curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" --data-binary "@data/sample_submission.json"
```

## API contract

| Route | Request | Response |
| --- | --- | --- |
| `POST /ping` | JSON with `message` | Control response with `ok`, `you_sent`, and service name |
| `GET /health` | No body | Service and detector status |
| `POST /submit` | JSON strings `text`, `creator_id` | UUID `content_id`, `guess`, `confidence`, `label`, both signal scores, combined score, style metrics, timestamp, and `decided` status |
| `POST /appeal` | JSON strings `content_id`, `reasoning` | Recorded reasoning, `under_review` status, and confirmation |
| `GET /content/<content_id>` | Existing content ID in the URL | Original decision fields, current status, and appeal history |
| `GET /log` | Optional `limit` query parameter | JSON audit entries and their count |

Higher `confidence` means stronger AI suspicion, rather than certainty in
whichever guess was returned. It equals `combined_score`. The score is a
heuristic, not a calibrated probability. See README for the exact labels,
weights, and threshold ranges.

Submission text needs at least 20 characters after trimming and at least five
word tokens. It may contain at most 10,000 characters. Creator IDs must be
nonempty strings of at most 128 characters. Appeal reasoning must be nonempty
and at most 2,000 characters. Request bodies are limited to 65,536 bytes.

Invalid fields, short text, malformed JSON, and non-object JSON produce HTTP
400. Unknown content IDs produce HTTP 404. Oversized text, reasoning, or
bodies produce HTTP 413; non-JSON content types produce HTTP 415. Error
responses contain `error` and `message`. A failed detector or audit write
produces HTTP 503. Invalid requests do not receive a saved successful decision. When a submission quota
is exhausted, HTTP429 can precede these validation responses; appeals are not
submission-rate limited.

## Verify the implementation

Environment and isolated checks:

```bash
python test.py
python -m unittest discover -s tests -v
```

Run the complete HTTP verification while the service is running:

```bash
python scripts/verify_project.py --url http://127.0.0.1:5000 --trials 3 --output results/development_current.json
```

This records all real responses in `results/development_current.json`, evaluates the
frozen development groups, sweeps 10,001 label scores, and checks appeals and
bad input. Read the saved verdicts; original targets are archived in
[docs/criteria_parts1_2.md](docs/criteria_parts1_2.md). The root `criteria.md`
now holds the new capstone targets; this legacy verifier does not evaluate them.
The isolated tests cover detector invocation counts, unavailable dependencies,
and reconstruction from the saved audit log. A fresh HTTP session by itself
does not verify a server restart.

To check persistence directly, stop the server with Ctrl-C, start it again
using the same project directory, and repeat the `/content` request for
`DEMO_CONTENT_ID`. Its status is reconstructed from `logs/audit.jsonl`.

## Part 2: full before/after evidence

Rate limiting is enabled by default: **10 submissions per minute and 200 per
day**, per usable creator ID, with an address fallback for missing/invalid IDs.
The local in-memory counters reset on a server restart. IDs are caller-supplied;
changing an ID can evade this teaching control. Production needs authenticated
identity and shared durable limit storage.

With the server running, the course commands are:

```bash
python run_attacks.py --flood 15 --creator my-flood-check --url http://127.0.0.1:5000
python run_attacks.py --set attack_set --label before --url http://127.0.0.1:5000
python run_eval.py --label before --url http://127.0.0.1:5000
```

The submitted before run used the Part 2 instrumented baseline at commit
`6d42fc9`. The current configuration includes the measured improvement:
`AI_THRESHOLD = 0.80`, raised from `0.75`. Re-running a command labeled
`before` on the current code does not reproduce the old threshold. Preserve
archived results rather than replacing them with a mislabeled new capture.

After the single change and service restart, the recorded after commands were:

```bash
python run_attacks.py --set attack_set --label after --url http://127.0.0.1:5000
python run_eval.py --label after --url http://127.0.0.1:5000
python scripts/part2_attack_review.py --label after
```

Use port 5054 in all URLs if that is where your server runs. Let the address
minute window expire after the attack run before a clean evaluation campaign;
keep the limiter enabled and do not reset or change settings between its three
trials. The submitted campaigns each began after an idle minute. Quota state
still changes during the trials; that is recorded rather than silently retried.

`scenarios.py` defines exactly the five original criteria. `run_eval.py` now
runs submissions, score comparisons, the complete label sweep, ten appeals
per trial, fresh-process persistence checks, and all eighteen validation groups.
Its JSON saves all three trials; the Markdown report includes a five-row table
and full trial-1 output for every criterion. A missed target is recorded as
MISSED and does not mean the test runner failed to execute.

Every attack has raw request/response captures and a separate reviewed judgment.
`part2_attack_review.py` records the explicit goal-based judgment policy. It
does not establish human authorship independently. The two source CSVs and
original ZIP remain byte-for-byte unchanged, with hashes in
`attack_set/provenance.json`. Do not edit them to improve a result.

The legacy Part 1 verifier can write a separate development capture:

```bash
python scripts/verify_project.py --url http://127.0.0.1:5000 --output results/development_current.json
```

Official Part 2 evidence always keeps limiting enabled. Some invalid requests
will receive 429 when an address bucket is exhausted; this is the documented
miss against the original exact-validation-code target.

## Files and operating limits

| File | Purpose |
| --- | --- |
| `app.py` | Input validation, routes, enabled limits, decision and appeal flow |
| `detector.py` | Cached local GPT-2 predictability signal |
| `stylometry.py` | Sentence-length spread, word variety, and punctuation measures |
| `scoring.py` | Signal combination and complete label mapping |
| `config.py` | Weights, thresholds, limits, cache, and server settings |
| `audit.py` | Append-only decision, appeal, and rejection events |
| `data/evaluation_inputs.json` | Frozen inputs with source and generation provenance |
| `docs/criteria_parts1_2.md` | Five original acceptance targets and their reasons |
| `criteria.md` | Five new capstone targets, committed before capstone evaluation |
| `logs/audit.jsonl` | Saved event history, included as project evidence |
| `results/` | Captured demonstration and verification outputs |

GPT-2 examines at most the first 400 tokens; stylometry examines the accepted
text in full. Predictable human writing can be flagged, and unusual AI writing
can pass. Appeals record a review request without automatically rerunning the
detector or proving authorship.

The default loopback service has no authentication. Creator IDs and appeals
are unverified, and `/log` exposes locally saved metadata and appeal reasoning
to anyone who can reach the service. It does not save submission text. Keep
this development service local; public hosting needs access controls and a
review of logging and retention.

If a request fails, check `/ping`, then `/health`. For `Address already in
use`, stop your earlier server or choose another port. For detector download
errors, check the connection and available disk space, then rerun the detector
command. The first request after starting a process may take longer while the
model loads. Logs and result files are project evidence; retain the repository
and its history for the next unit.

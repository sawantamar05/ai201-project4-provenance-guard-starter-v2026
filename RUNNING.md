# Running Provenance Guard

Provenance Guard is a local JSON API. It combines a GPT-2 predictability signal
with stylometry, saves each decision, and records appeals for review. It needs
no API key. Model files download once; inference runs on your machine.

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
produces HTTP 503. Invalid requests do not receive a saved successful decision.

## Verify the implementation

Environment and isolated checks:

```bash
python test.py
python -m unittest discover -s tests -v
```

Run the complete HTTP verification while the service is running:

```bash
python scripts/verify_project.py --url http://127.0.0.1:5000 --trials 3
```

This records all real responses in `results/verification.json`, evaluates the
frozen development groups, sweeps 10,001 label scores, and checks appeals and
bad input. Read the saved verdicts; targets are specified in `criteria.md`.
The isolated tests cover detector invocation counts, unavailable dependencies,
and reconstruction from the saved audit log. A fresh HTTP session by itself
does not verify a server restart.

To check persistence directly, stop the server with Ctrl-C, start it again
using the same project directory, and repeat the `/content` request for
`DEMO_CONTENT_ID`. Its status is reconstructed from `logs/audit.jsonl`.

For the next unit's submission-only scenario runner:

```bash
python run_eval.py --url http://127.0.0.1:5000 --label development --trials 3
```

`scenarios.py` loads the frozen sourced-human and generated-AI passages plus
invalid submission bodies. `run_eval.py` sends only `POST /submit` and saves
a report for interpretation. Use `scripts/verify_project.py` for appeal checks,
the complete validation matrix, and automated criterion verdicts.

## Optional rate limiting and attack tools

Start with limiting enabled when testing the next unit's controls:

```bash
AI201_RATE_LIMITS=1 python app.py
python run_attacks.py --url http://127.0.0.1:5000 --flood 15
```

`config.py` sets 10 submissions per minute and 200 per day. Limits are already
wired into `/submit`; no code editing is needed to enable them. They use
in-memory storage and reset on restart. The key uses the supplied creator ID,
with a remote-address fallback. A caller can change that unverified ID, so
this is a development control. Keep limiting off for the ordinary three-trial
verification run.

`run_attacks.py --set` accepts an externally provided attack-set directory.
Its `--show` option displays an attack without sending it. The frozen
development passages are not an independent attack set.

## Files and operating limits

| File | Purpose |
| --- | --- |
| `app.py` | Input validation, routes, optional limits, decision and appeal flow |
| `detector.py` | Cached local GPT-2 predictability signal |
| `stylometry.py` | Sentence-length spread, word variety, and punctuation measures |
| `scoring.py` | Signal combination and complete label mapping |
| `config.py` | Weights, thresholds, limits, cache, and server settings |
| `audit.py` | Append-only decision, appeal, and rejection events |
| `data/evaluation_inputs.json` | Frozen inputs with source and generation provenance |
| `criteria.md` | Five acceptance targets and their reasons |
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

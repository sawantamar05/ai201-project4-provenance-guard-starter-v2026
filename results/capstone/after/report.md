# Capstone campaign — after

Criteria SHA-256: `b54324f9b43cecf68ba911daec030a362ae5d7dae9243d85591440193f22ed14`.

Real GPT-2 HTTP trials; isolated companion call counts are explicitly mocked.

| Criterion | Target | Run1 | Run2 | Run3 | Verdict |
|---|---|---|---|---|---|
| 1. Validation errors under quota pressure | 20/20 exact JSON validation responses; no malformed scoring/success events | 20/20 exact; no-success-events=True; isolated=True | 20/20 exact; no-success-events=True; isolated=True | 20/20 exact; no-success-events=True; isolated=True | MET |
| 2. Malformed requests preserve scoring allowance | 12/12 invalid400; then ten200 and two429; exactly10 isolated detector calls | 12/12 invalid400; 10/10 valid200; 2/2 quota429; isolated=True | 12/12 invalid400; 10/10 valid200; 2/2 quota429; isolated=True | 12/12 invalid400; 10/10 valid200; 2/2 quota429; isolated=True | MET |
| 3. Complete durable request records | 23/23 durable unique correlated completion records with required redacted fields | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | MET |
| 4. Warm submission response time | 10/10 complete decisions; at least9/10 warm requests below5.0s | 10/10 decisions; 10/10<5s; mean0.0558s | 10/10 decisions; 10/10<5s; mean0.0584s | 10/10 decisions; 10/10<5s; mean0.0562s | MET |
| 5. Appeals survive server restart | 10/10 exact persistent appeals; unchanged originals; unknown404; zero rescoring | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | MET |

## Actual trial1 output

### Criterion1

Produced by `scripts/run_capstone.py::criterion_one`.

```json
{
  "conditions": [
    {
      "condition": "ordinary",
      "starts": [
        {
          "command": [
            "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
            "-m",
            "gunicorn",
            "--workers",
            "1",
            "--threads",
            "1",
            "--timeout",
            "120",
            "--bind",
            "127.0.0.1:59589",
            "app:app"
          ],
          "pid": 74822,
          "started_at_utc": "2026-11-14T02:08:11.394183+00:00",
          "url": "http://127.0.0.1:59589",
          "log_directory": "results/capstone/after/c1_trial1_attempt1/ordinary",
          "environment_overrides": {
            "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c1_trial1_attempt1/ordinary",
            "AI201_RATE_LIMITS": "1",
            "HF_HUB_OFFLINE": "1",
            "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
          },
          "health_at_start": {
            "detector_loaded": false,
            "detector_model": "gpt2",
            "log_entries": 0,
            "ok": true,
            "rate_limiting": true
          },
          "health_request_id": "5ffba9b7-7070-4e49-abc6-39d0ec549c33",
          "cold_warmup": {
            "name": "disclosed cold-model warm-up",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:11.518400+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "cap-after-c1-t1-a1-warm"
            },
            "status_code": 200,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "745",
              "X-Request-ID": "8f431600-1870-4110-91e2-68fdeb6eaa9a"
            },
            "request_id": "8f431600-1870-4110-91e2-68fdeb6eaa9a",
            "response_json": {
              "combined_score": 0.6593,
              "confidence": 0.6593,
              "content_id": "d97ae8fc-156f-4899-afa5-7c69bbe332fe",
              "creator_id": "cap-after-c1-t1-a1-warm",
              "detector_model": "gpt2",
              "guess": "unsure",
              "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
              "model_score": 0.6922,
              "status": "decided",
              "style_metrics": {
                "evenness": 0.5,
                "punctuation_density": 0.016286644951140065,
                "punctuation_simplicity": 0.8642779587404994,
                "repetition": 0.34976525821596255,
                "sentence_count": 2,
                "sentence_length_spread": 0.352112676056338,
                "style_score": 0.5278,
                "type_token_ratio": 0.6901408450704225,
                "word_count": 71
              },
              "style_score": 0.5278,
              "text_length": 377,
              "timestamp": "2026-11-14T02:08:15+00:00"
            },
            "elapsed_seconds": 3.618370749987662,
            "request_body_bytes": 430
          },
          "stopped_at_utc": "2026-11-14T02:08:15.594893+00:00",
          "returncode": 0
        }
      ],
      "warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:11.518400+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c1-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "745",
          "X-Request-ID": "8f431600-1870-4110-91e2-68fdeb6eaa9a"
        },
        "request_id": "8f431600-1870-4110-91e2-68fdeb6eaa9a",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "d97ae8fc-156f-4899-afa5-7c69bbe332fe",
          "creator_id": "cap-after-c1-t1-a1-warm",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:15+00:00"
        },
        "elapsed_seconds": 3.618370749987662,
        "request_body_bytes": 430
      },
      "quota_sequence_seconds": 0.008598832879215479,
      "cases": [
        {
          "case": 1,
          "name": "missing text",
          "expected_status": 400,
          "http": {
            "name": "missing text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.136933+00:00",
            "request_json": {
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "8c782575-4e20-4502-a585-2733c336c8e3"
            },
            "request_id": "8c782575-4e20-4502-a585-2733c336c8e3",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.001240083947777748,
            "request_body_bytes": 36
          },
          "passed": true
        },
        {
          "case": 2,
          "name": "empty text",
          "expected_status": 400,
          "http": {
            "name": "empty text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.138224+00:00",
            "request_json": {
              "text": "",
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "6758013b-f0fa-4569-ae48-546abad8b53d"
            },
            "request_id": "6758013b-f0fa-4569-ae48-546abad8b53d",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.0008532502688467503,
            "request_body_bytes": 48
          },
          "passed": true
        },
        {
          "case": 3,
          "name": "numeric text",
          "expected_status": 400,
          "http": {
            "name": "numeric text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.139088+00:00",
            "request_json": {
              "text": 42,
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "b7e4c92d-ef6a-4e6d-860c-d85f8da457e1"
            },
            "request_id": "b7e4c92d-ef6a-4e6d-860c-d85f8da457e1",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.0008649579249322414,
            "request_body_bytes": 48
          },
          "passed": true
        },
        {
          "case": 4,
          "name": "missing creator",
          "expected_status": 400,
          "http": {
            "name": "missing creator",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.139961+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "107",
              "X-Request-ID": "b904c662-4efa-4f1a-8062-0a77678ef66f"
            },
            "request_id": "b904c662-4efa-4f1a-8062-0a77678ef66f",
            "response_json": {
              "error": "invalid_creator_id",
              "message": "creator_id must be a nonempty string of at most 128 characters."
            },
            "elapsed_seconds": 0.0008455421775579453,
            "request_body_bytes": 389
          },
          "passed": true
        },
        {
          "case": 5,
          "name": "blank creator",
          "expected_status": 400,
          "http": {
            "name": "blank creator",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.140814+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "   "
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "107",
              "X-Request-ID": "dc78a8c7-8e19-4e55-9138-84240f7f73e1"
            },
            "request_id": "dc78a8c7-8e19-4e55-9138-84240f7f73e1",
            "response_json": {
              "error": "invalid_creator_id",
              "message": "creator_id must be a nonempty string of at most 128 characters."
            },
            "elapsed_seconds": 0.0008847909048199654,
            "request_body_bytes": 410
          },
          "passed": true
        },
        {
          "case": 6,
          "name": "oversized text",
          "expected_status": 413,
          "http": {
            "name": "oversized text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.141710+00:00",
            "request_json": {
              "text": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 413,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "79",
              "X-Request-ID": "bf768ee2-ec01-4409-96cc-471fd863bec3"
            },
            "request_id": "bf768ee2-ec01-4409-96cc-471fd863bec3",
            "response_json": {
              "error": "text_too_large",
              "message": "text must not exceed 10,000 characters."
            },
            "elapsed_seconds": 0.0008989591151475906,
            "request_body_bytes": 10049
          },
          "passed": true
        },
        {
          "case": 7,
          "name": "malformed JSON",
          "expected_status": 400,
          "http": {
            "name": "malformed JSON",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.142619+00:00",
            "request_body": "{",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "63",
              "X-Request-ID": "2d79880a-7cb6-46bf-87ba-66abb009a6c2"
            },
            "request_id": "2d79880a-7cb6-46bf-87ba-66abb009a6c2",
            "response_json": {
              "error": "invalid_json",
              "message": "Send a valid JSON object."
            },
            "elapsed_seconds": 0.0007604998536407948,
            "request_body_bytes": 1
          },
          "passed": true
        },
        {
          "case": 8,
          "name": "non-object JSON",
          "expected_status": 400,
          "http": {
            "name": "non-object JSON",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.143387+00:00",
            "request_body": "[]",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "63",
              "X-Request-ID": "7610c8eb-a4f7-496d-93db-68860b9a41b6"
            },
            "request_id": "7610c8eb-a4f7-496d-93db-68860b9a41b6",
            "response_json": {
              "error": "invalid_json",
              "message": "Send a valid JSON object."
            },
            "elapsed_seconds": 0.0006539579480886459,
            "request_body_bytes": 2
          },
          "passed": true
        },
        {
          "case": 9,
          "name": "non-JSON content type",
          "expected_status": 415,
          "http": {
            "name": "non-JSON content type",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.144048+00:00",
            "request_body": "hello",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 415,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "77",
              "X-Request-ID": "c2047236-94b7-49f4-9301-acbde6c251ca"
            },
            "request_id": "c2047236-94b7-49f4-9301-acbde6c251ca",
            "response_json": {
              "error": "json_required",
              "message": "Send an application/json request body."
            },
            "elapsed_seconds": 0.0006376667879521847,
            "request_body_bytes": 5
          },
          "passed": true
        },
        {
          "case": 10,
          "name": "oversized non-JSON body",
          "expected_status": 413,
          "http": {
            "name": "oversized non-JSON body",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.144692+00:00",
            "request_body": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 413,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:15 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "85",
              "X-Request-ID": "cf27fef0-8cd8-4e73-a99e-f7787c732b19"
            },
            "request_id": "cf27fef0-8cd8-4e73-a99e-f7787c732b19",
            "response_json": {
              "error": "request_too_large",
              "message": "Request body must not exceed 65,536 bytes."
            },
            "elapsed_seconds": 0.0006577079184353352,
            "request_body_bytes": 65537
          },
          "passed": true
        }
      ],
      "audit_parse_errors": [],
      "successful_events_unchanged": true,
      "quota_window_valid": true,
      "passed": true
    },
    {
      "condition": "pressure",
      "starts": [
        {
          "command": [
            "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
            "-m",
            "gunicorn",
            "--workers",
            "1",
            "--threads",
            "1",
            "--timeout",
            "120",
            "--bind",
            "127.0.0.1:59604",
            "app:app"
          ],
          "pid": 74834,
          "started_at_utc": "2026-11-14T02:08:15.598184+00:00",
          "url": "http://127.0.0.1:59604",
          "log_directory": "results/capstone/after/c1_trial1_attempt1/pressure",
          "environment_overrides": {
            "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c1_trial1_attempt1/pressure",
            "AI201_RATE_LIMITS": "1",
            "HF_HUB_OFFLINE": "1",
            "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
          },
          "health_at_start": {
            "detector_loaded": false,
            "detector_model": "gpt2",
            "log_entries": 0,
            "ok": true,
            "rate_limiting": true
          },
          "health_request_id": "a0514590-934e-4c36-b274-945c7fd5a411",
          "cold_warmup": {
            "name": "disclosed cold-model warm-up",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:15.716820+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "cap-after-c1-t1-a1-warm"
            },
            "status_code": 200,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "745",
              "X-Request-ID": "ece75d2a-9b52-4bfa-a327-857d66740523"
            },
            "request_id": "ece75d2a-9b52-4bfa-a327-857d66740523",
            "response_json": {
              "combined_score": 0.6593,
              "confidence": 0.6593,
              "content_id": "cdbe5523-fc09-4f34-ba9c-bfd396aad20c",
              "creator_id": "cap-after-c1-t1-a1-warm",
              "detector_model": "gpt2",
              "guess": "unsure",
              "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
              "model_score": 0.6922,
              "status": "decided",
              "style_metrics": {
                "evenness": 0.5,
                "punctuation_density": 0.016286644951140065,
                "punctuation_simplicity": 0.8642779587404994,
                "repetition": 0.34976525821596255,
                "sentence_count": 2,
                "sentence_length_spread": 0.352112676056338,
                "style_score": 0.5278,
                "type_token_ratio": 0.6901408450704225,
                "word_count": 71
              },
              "style_score": 0.5278,
              "text_length": 377,
              "timestamp": "2026-11-14T02:08:17+00:00"
            },
            "elapsed_seconds": 1.475615665782243,
            "request_body_bytes": 430
          },
          "stopped_at_utc": "2026-11-14T02:08:17.961517+00:00",
          "returncode": 0
        }
      ],
      "warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:15.716820+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c1-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "745",
          "X-Request-ID": "ece75d2a-9b52-4bfa-a327-857d66740523"
        },
        "request_id": "ece75d2a-9b52-4bfa-a327-857d66740523",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "cdbe5523-fc09-4f34-ba9c-bfd396aad20c",
          "creator_id": "cap-after-c1-t1-a1-warm",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:17+00:00"
        },
        "elapsed_seconds": 1.475615665782243,
        "request_body_bytes": 430
      },
      "creator_pressure": [
        {
          "name": "creator pressure 1",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.192445+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "72d1fda4-1778-47a7-a8c1-6be7c4c38b45"
          },
          "request_id": "72d1fda4-1778-47a7-a8c1-6be7c4c38b45",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "e599e125-83de-48d0-a712-38f0f91d605b",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.0407001250423491,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 2",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.233157+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "3f4ce23a-9a3a-4f2d-9839-d36f2804da2a"
          },
          "request_id": "3f4ce23a-9a3a-4f2d-9839-d36f2804da2a",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "88cb724e-09cd-4c2f-8b50-6f3a93a523c8",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.040468333289027214,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 3",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.273636+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "c66002bd-7b8e-429c-95cf-3aa999c23609"
          },
          "request_id": "c66002bd-7b8e-429c-95cf-3aa999c23609",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "64a3cd81-f452-46af-82a0-0879d5e89fae",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.04044529190286994,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 4",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.314090+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "b0671741-77b0-4d9e-ad8d-0d095b475d5b"
          },
          "request_id": "b0671741-77b0-4d9e-ad8d-0d095b475d5b",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "c1573048-6b3e-4552-a250-1e3524630ebd",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.04018020909279585,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 5",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.354279+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "d55cdc71-3760-4ba0-99d9-5ba8f52f712c"
          },
          "request_id": "d55cdc71-3760-4ba0-99d9-5ba8f52f712c",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "815c5081-ea1b-4174-ad6d-17caa243b0ad",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.040123708080500364,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 6",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.394410+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "bdcea4e6-037d-493e-af08-eb26df77f2b3"
          },
          "request_id": "bdcea4e6-037d-493e-af08-eb26df77f2b3",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "6ceee54b-e859-4c53-82ae-771ec66b1a62",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.03987029194831848,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 7",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.434289+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "6174f676-6df8-40b5-835a-2e49cec72a78"
          },
          "request_id": "6174f676-6df8-40b5-835a-2e49cec72a78",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "9d235017-ee6e-4fc5-a618-0dee25fe151b",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.04030191712081432,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 8",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.474598+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "71e02600-1016-4bc0-a9de-0cfef8ccca8c"
          },
          "request_id": "71e02600-1016-4bc0-a9de-0cfef8ccca8c",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "59be42eb-8319-4683-9715-0c21d319421b",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.040121291764080524,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 9",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.514727+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "8ef4a64a-403e-4bd3-a47d-f08a9028fc04"
          },
          "request_id": "8ef4a64a-403e-4bd3-a47d-f08a9028fc04",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "b5ae0046-c39c-46af-aa1c-59da45e9a019",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.04038975015282631,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 10",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.555124+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "740",
            "X-Request-ID": "0f034020-1323-4824-9b66-b7e83b646264"
          },
          "request_id": "0f034020-1323-4824-9b66-b7e83b646264",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "5bef9add-3236-4536-bc71-3fcade97d807",
            "creator_id": "cap-after-c1-t1-a1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6922,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:17+00:00"
          },
          "elapsed_seconds": 0.03983433265239,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 11",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.594967+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 429,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "78",
            "X-Request-ID": "14877f39-a906-4029-9075-924a6afcdce2"
          },
          "request_id": "14877f39-a906-4029-9075-924a6afcdce2",
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "elapsed_seconds": 0.0010637086816132069,
          "request_body_bytes": 425
        },
        {
          "name": "creator pressure 12",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.596037+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-after-c1-t1-a1"
          },
          "status_code": 429,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "78",
            "X-Request-ID": "4ffa060f-dc7f-47b9-a932-3fc0fac1e1cd"
          },
          "request_id": "4ffa060f-dc7f-47b9-a932-3fc0fac1e1cd",
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "elapsed_seconds": 0.0009618750773370266,
          "request_body_bytes": 425
        }
      ],
      "address_pressure": [
        {
          "name": "address pressure 1",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.597006+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "36eb5511-85a6-42f6-8a51-612c1ae26fea"
          },
          "request_id": "36eb5511-85a6-42f6-8a51-612c1ae26fea",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007274588569998741,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 2",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.597739+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "aced07c2-b8dc-4629-b722-2d47e21c4e79"
          },
          "request_id": "aced07c2-b8dc-4629-b722-2d47e21c4e79",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007433746941387653,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 3",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.598487+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "f350fd98-2528-4a11-a38d-f0b07ead1c91"
          },
          "request_id": "f350fd98-2528-4a11-a38d-f0b07ead1c91",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007583750411868095,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 4",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.599251+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "5ae2c7ff-6875-4c07-ac4d-27413fb0190b"
          },
          "request_id": "5ae2c7ff-6875-4c07-ac4d-27413fb0190b",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007572909817099571,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 5",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.600013+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "bc57cba3-7bb8-498f-808e-efa972a6a5db"
          },
          "request_id": "bc57cba3-7bb8-498f-808e-efa972a6a5db",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0006893747486174107,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 6",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.600707+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "57d49853-674f-49cd-b561-7ac5349c27fa"
          },
          "request_id": "57d49853-674f-49cd-b561-7ac5349c27fa",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0006837924011051655,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 7",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.601396+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "5aae84b1-9498-4137-ac04-fa478ad3a552"
          },
          "request_id": "5aae84b1-9498-4137-ac04-fa478ad3a552",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0006661247462034225,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 8",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.602066+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "22f322e8-cc81-4ac0-928f-da0cdb0ca0dc"
          },
          "request_id": "22f322e8-cc81-4ac0-928f-da0cdb0ca0dc",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0006712079048156738,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 9",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.602742+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "68eacac2-12ef-4d37-b135-3bfd28b0a910"
          },
          "request_id": "68eacac2-12ef-4d37-b135-3bfd28b0a910",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0006850408390164375,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 10",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.603432+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "f6c15eab-cb8f-4794-a9e1-3da7e2f809fb"
          },
          "request_id": "f6c15eab-cb8f-4794-a9e1-3da7e2f809fb",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007487498223781586,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 11",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.604185+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "44891d24-a22b-4707-928d-73e3bca108db"
          },
          "request_id": "44891d24-a22b-4707-928d-73e3bca108db",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007025422528386116,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 12",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:08:17.604892+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "5a90ee15-f405-41e0-99fd-f814766cbd67"
          },
          "request_id": "5a90ee15-f405-41e0-99fd-f814766cbd67",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007360000163316727,
          "request_body_bytes": 389
        }
      ],
      "quota_sequence_seconds": 0.420502417255193,
      "cases": [
        {
          "case": 1,
          "name": "missing text",
          "expected_status": 400,
          "http": {
            "name": "missing text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.605830+00:00",
            "request_json": {
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "54306ffa-de0d-4958-8943-d1671a1517f3"
            },
            "request_id": "54306ffa-de0d-4958-8943-d1671a1517f3",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.0007270830683410168,
            "request_body_bytes": 36
          },
          "passed": true
        },
        {
          "case": 2,
          "name": "empty text",
          "expected_status": 400,
          "http": {
            "name": "empty text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.606565+00:00",
            "request_json": {
              "text": "",
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "ed096f3c-b026-4d87-bdcb-47eef1cc8131"
            },
            "request_id": "ed096f3c-b026-4d87-bdcb-47eef1cc8131",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.0006857500411570072,
            "request_body_bytes": 48
          },
          "passed": true
        },
        {
          "case": 3,
          "name": "numeric text",
          "expected_status": 400,
          "http": {
            "name": "numeric text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.607258+00:00",
            "request_json": {
              "text": 42,
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "82274368-e058-4879-9f8e-bc62e08024c5"
            },
            "request_id": "82274368-e058-4879-9f8e-bc62e08024c5",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.000713166780769825,
            "request_body_bytes": 48
          },
          "passed": true
        },
        {
          "case": 4,
          "name": "missing creator",
          "expected_status": 400,
          "http": {
            "name": "missing creator",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.607978+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "107",
              "X-Request-ID": "1f346079-7c19-4f4d-a744-d690f7e7299a"
            },
            "request_id": "1f346079-7c19-4f4d-a744-d690f7e7299a",
            "response_json": {
              "error": "invalid_creator_id",
              "message": "creator_id must be a nonempty string of at most 128 characters."
            },
            "elapsed_seconds": 0.0007192501798272133,
            "request_body_bytes": 389
          },
          "passed": true
        },
        {
          "case": 5,
          "name": "blank creator",
          "expected_status": 400,
          "http": {
            "name": "blank creator",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.608704+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "   "
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "107",
              "X-Request-ID": "154f177f-e680-4e73-b9d2-27fd0765f423"
            },
            "request_id": "154f177f-e680-4e73-b9d2-27fd0765f423",
            "response_json": {
              "error": "invalid_creator_id",
              "message": "creator_id must be a nonempty string of at most 128 characters."
            },
            "elapsed_seconds": 0.0007205833680927753,
            "request_body_bytes": 410
          },
          "passed": true
        },
        {
          "case": 6,
          "name": "oversized text",
          "expected_status": 413,
          "http": {
            "name": "oversized text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.609431+00:00",
            "request_json": {
              "text": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
              "creator_id": "cap-after-c1-t1-a1"
            },
            "status_code": 413,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "79",
              "X-Request-ID": "e328ee74-d5e6-4749-ade0-41ec4154ffab"
            },
            "request_id": "e328ee74-d5e6-4749-ade0-41ec4154ffab",
            "response_json": {
              "error": "text_too_large",
              "message": "text must not exceed 10,000 characters."
            },
            "elapsed_seconds": 0.0007622917182743549,
            "request_body_bytes": 10049
          },
          "passed": true
        },
        {
          "case": 7,
          "name": "malformed JSON",
          "expected_status": 400,
          "http": {
            "name": "malformed JSON",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.610200+00:00",
            "request_body": "{",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "63",
              "X-Request-ID": "b60586b2-4495-4483-a805-b0ae3513dfaf"
            },
            "request_id": "b60586b2-4495-4483-a805-b0ae3513dfaf",
            "response_json": {
              "error": "invalid_json",
              "message": "Send a valid JSON object."
            },
            "elapsed_seconds": 0.0006989999674260616,
            "request_body_bytes": 1
          },
          "passed": true
        },
        {
          "case": 8,
          "name": "non-object JSON",
          "expected_status": 400,
          "http": {
            "name": "non-object JSON",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.610906+00:00",
            "request_body": "[]",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "63",
              "X-Request-ID": "9295eb2e-3c0f-4b79-a4e0-71784d6b7ba6"
            },
            "request_id": "9295eb2e-3c0f-4b79-a4e0-71784d6b7ba6",
            "response_json": {
              "error": "invalid_json",
              "message": "Send a valid JSON object."
            },
            "elapsed_seconds": 0.0007100841030478477,
            "request_body_bytes": 2
          },
          "passed": true
        },
        {
          "case": 9,
          "name": "non-JSON content type",
          "expected_status": 415,
          "http": {
            "name": "non-JSON content type",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.611623+00:00",
            "request_body": "hello",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 415,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "77",
              "X-Request-ID": "3e6157a7-d7bd-43d7-8e45-77d39dc93756"
            },
            "request_id": "3e6157a7-d7bd-43d7-8e45-77d39dc93756",
            "response_json": {
              "error": "json_required",
              "message": "Send an application/json request body."
            },
            "elapsed_seconds": 0.0006555831059813499,
            "request_body_bytes": 5
          },
          "passed": true
        },
        {
          "case": 10,
          "name": "oversized non-JSON body",
          "expected_status": 413,
          "http": {
            "name": "oversized non-JSON body",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:08:17.612285+00:00",
            "request_body": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 413,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:08:17 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "85",
              "X-Request-ID": "aa8fce84-9013-4d1e-83a5-7fd611da773f"
            },
            "request_id": "aa8fce84-9013-4d1e-83a5-7fd611da773f",
            "response_json": {
              "error": "request_too_large",
              "message": "Request body must not exceed 65,536 bytes."
            },
            "elapsed_seconds": 0.0006468337960541248,
            "request_body_bytes": 65537
          },
          "passed": true
        }
      ],
      "audit_parse_errors": [],
      "successful_events_unchanged": true,
      "quota_window_valid": true,
      "passed": true
    }
  ],
  "quota_window_valid": true,
  "http_passed": true,
  "exact_status_count": 20,
  "summary": "20/20 exact; no-success-events=True",
  "trial": 1,
  "attempt": 1,
  "criterion": 1,
  "evidence_directory": "results/capstone/after/c1_trial1_attempt1",
  "companion": {
    "required": true,
    "kind": "mocked isolated invocation check; not real inference",
    "command": [
      "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
      "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/scripts/capstone_call_counts.py",
      "--criterion",
      "1",
      "--trial",
      "1"
    ],
    "returncode": 0,
    "stderr": "",
    "result": {
      "criterion": 1,
      "trial": 1,
      "kind": "mocked isolated detector invocation check",
      "real_model_loaded": false,
      "conditions": [
        {
          "pressure": false,
          "pressure_responses": [],
          "pressure_detector_calls": 0,
          "cases": [
            {
              "case": 1,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_text",
                "message": "text must be a nonempty string."
              },
              "detector_calls": 0
            },
            {
              "case": 2,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_text",
                "message": "text must be a nonempty string."
              },
              "detector_calls": 0
            },
            {
              "case": 3,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_text",
                "message": "text must be a nonempty string."
              },
              "detector_calls": 0
            },
            {
              "case": 4,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              },
              "detector_calls": 0
            },
            {
              "case": 5,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              },
              "detector_calls": 0
            },
            {
              "case": 6,
              "expected_status": 413,
              "status_code": 413,
              "response_json": {
                "error": "text_too_large",
                "message": "text must not exceed 10,000 characters."
              },
              "detector_calls": 0
            },
            {
              "case": 7,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_json",
                "message": "Send a valid JSON object."
              },
              "detector_calls": 0
            },
            {
              "case": 8,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_json",
                "message": "Send a valid JSON object."
              },
              "detector_calls": 0
            },
            {
              "case": 9,
              "expected_status": 415,
              "status_code": 415,
              "response_json": {
                "error": "json_required",
                "message": "Send an application/json request body."
              },
              "detector_calls": 0
            },
            {
              "case": 10,
              "expected_status": 413,
              "status_code": 413,
              "response_json": {
                "error": "request_too_large",
                "message": "Request body must not exceed 65,536 bytes."
              },
              "detector_calls": 0
            }
          ],
          "matrix_detector_calls": 0,
          "successful_events_unchanged": true
        },
        {
          "pressure": true,
          "pressure_responses": [
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "c82e4696-0220-464c-bfed-bae42ea154d6",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "2f5795e4-5c92-4b7a-9420-9d3b2e51c517",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "db4c3224-41c6-4aec-8e01-147ce1e00bdb",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "b1d7284b-2ddb-4c94-8649-66b4bd9a8e24",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "332f1ca3-4b10-4c56-a848-509c344baf80",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "5bebe3da-3414-48b0-ab5c-00ce709e47db",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "94b191e1-6f46-47d1-b51a-6baf2506d2a4",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "9c101a4d-40b8-4bc4-8900-48eaa1c5e4ca",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "4980d1f8-be6f-4f11-827e-76d84d8b81f0",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "b883e5f6-dae2-4757-9bac-9215177b9ddc",
                "creator_id": "mocked-c1-t1",
                "detector_model": "gpt2",
                "guess": "unsure",
                "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
                "model_score": 0.6,
                "status": "decided",
                "style_metrics": {
                  "evenness": 0.5,
                  "punctuation_density": 0.016286644951140065,
                  "punctuation_simplicity": 0.8642779587404994,
                  "repetition": 0.34976525821596255,
                  "sentence_count": 2,
                  "sentence_length_spread": 0.352112676056338,
                  "style_score": 0.5278,
                  "type_token_ratio": 0.6901408450704225,
                  "word_count": 71
                },
                "style_score": 0.5278,
                "text_length": 377,
                "timestamp": "2026-11-14T02:08:18+00:00"
              }
            },
            {
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              }
            },
            {
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            },
            {
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              }
            }
          ],
          "pressure_detector_calls": 10,
          "cases": [
            {
              "case": 1,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_text",
                "message": "text must be a nonempty string."
              },
              "detector_calls": 0
            },
            {
              "case": 2,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_text",
                "message": "text must be a nonempty string."
              },
              "detector_calls": 0
            },
            {
              "case": 3,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_text",
                "message": "text must be a nonempty string."
              },
              "detector_calls": 0
            },
            {
              "case": 4,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              },
              "detector_calls": 0
            },
            {
              "case": 5,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_creator_id",
                "message": "creator_id must be a nonempty string of at most 128 characters."
              },
              "detector_calls": 0
            },
            {
              "case": 6,
              "expected_status": 413,
              "status_code": 413,
              "response_json": {
                "error": "text_too_large",
                "message": "text must not exceed 10,000 characters."
              },
              "detector_calls": 0
            },
            {
              "case": 7,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_json",
                "message": "Send a valid JSON object."
              },
              "detector_calls": 0
            },
            {
              "case": 8,
              "expected_status": 400,
              "status_code": 400,
              "response_json": {
                "error": "invalid_json",
                "message": "Send a valid JSON object."
              },
              "detector_calls": 0
            },
            {
              "case": 9,
              "expected_status": 415,
              "status_code": 415,
              "response_json": {
                "error": "json_required",
                "message": "Send an application/json request body."
              },
              "detector_calls": 0
            },
            {
              "case": 10,
              "expected_status": 413,
              "status_code": 413,
              "response_json": {
                "error": "request_too_large",
                "message": "Request body must not exceed 65,536 bytes."
              },
              "detector_calls": 0
            }
          ],
          "matrix_detector_calls": 0,
          "successful_events_unchanged": true
        }
      ],
      "passed": true
    },
    "passed": true
  },
  "passed": true,
  "verdict": "MET",
  "invalid_attempts": []
}
```

### Criterion2

Produced by `scripts/run_capstone.py::criterion_two`.

```json
{
  "starts": [
    {
      "command": [
        "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
        "-m",
        "gunicorn",
        "--workers",
        "1",
        "--threads",
        "1",
        "--timeout",
        "120",
        "--bind",
        "127.0.0.1:59751",
        "app:app"
      ],
      "pid": 74883,
      "started_at_utc": "2026-11-14T02:08:27.200876+00:00",
      "url": "http://127.0.0.1:59751",
      "log_directory": "results/capstone/after/c2_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c2_trial1_attempt1",
        "AI201_RATE_LIMITS": "1",
        "HF_HUB_OFFLINE": "1",
        "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
      },
      "health_at_start": {
        "detector_loaded": false,
        "detector_model": "gpt2",
        "log_entries": 0,
        "ok": true,
        "rate_limiting": true
      },
      "health_request_id": "783ab2a4-16c3-4eb1-8934-74aa631b89fe",
      "cold_warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:27.319979+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c2-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "745",
          "X-Request-ID": "24a24a9c-2c9c-46f6-b9cb-d9ab50b00248"
        },
        "request_id": "24a24a9c-2c9c-46f6-b9cb-d9ab50b00248",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "2d3f2c94-8385-404c-a614-f2a9141a403b",
          "creator_id": "cap-after-c2-t1-a1-warm",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:28+00:00"
        },
        "elapsed_seconds": 1.5352243748493493,
        "request_body_bytes": 430
      },
      "stopped_at_utc": "2026-11-14T02:08:29.608257+00:00",
      "returncode": 0
    }
  ],
  "warmup": {
    "name": "disclosed cold-model warm-up",
    "method": "POST",
    "path": "/submit",
    "sent_at_utc": "2026-11-14T02:08:27.319979+00:00",
    "request_json": {
      "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
      "creator_id": "cap-after-c2-t1-a1-warm"
    },
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "745",
      "X-Request-ID": "24a24a9c-2c9c-46f6-b9cb-d9ab50b00248"
    },
    "request_id": "24a24a9c-2c9c-46f6-b9cb-d9ab50b00248",
    "response_json": {
      "combined_score": 0.6593,
      "confidence": 0.6593,
      "content_id": "2d3f2c94-8385-404c-a614-f2a9141a403b",
      "creator_id": "cap-after-c2-t1-a1-warm",
      "detector_model": "gpt2",
      "guess": "unsure",
      "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
      "model_score": 0.6922,
      "status": "decided",
      "style_metrics": {
        "evenness": 0.5,
        "punctuation_density": 0.016286644951140065,
        "punctuation_simplicity": 0.8642779587404994,
        "repetition": 0.34976525821596255,
        "sentence_count": 2,
        "sentence_length_spread": 0.352112676056338,
        "style_score": 0.5278,
        "type_token_ratio": 0.6901408450704225,
        "word_count": 71
      },
      "style_score": 0.5278,
      "text_length": 377,
      "timestamp": "2026-11-14T02:08:28+00:00"
    },
    "elapsed_seconds": 1.5352243748493493,
    "request_body_bytes": 430
  },
  "invalid_requests": [
    {
      "name": "invalid allowance check 1",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.855213+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "a8d5c61e-536b-47b3-a876-3d73a2139d52"
      },
      "request_id": "a8d5c61e-536b-47b3-a876-3d73a2139d52",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.001096667256206274,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 2",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.856320+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "2b87bb59-a1b0-431c-bcb5-8e4cf88a2b54"
      },
      "request_id": "2b87bb59-a1b0-431c-bcb5-8e4cf88a2b54",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0008197496645152569,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 3",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.857148+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "9c6736ac-75d1-48c4-87d6-048418684672"
      },
      "request_id": "9c6736ac-75d1-48c4-87d6-048418684672",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007108752615749836,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 4",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.857864+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "71b2cdbf-a0b1-40db-8ba0-4aaeed96297a"
      },
      "request_id": "71b2cdbf-a0b1-40db-8ba0-4aaeed96297a",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0006670830771327019,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 5",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.858536+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "895f48ac-53b5-4230-b767-d16ec59cf1b2"
      },
      "request_id": "895f48ac-53b5-4230-b767-d16ec59cf1b2",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0008074999786913395,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 6",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.859351+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "89150e71-7c75-4307-9a98-a967d5bbb3f4"
      },
      "request_id": "89150e71-7c75-4307-9a98-a967d5bbb3f4",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0008704578503966331,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 7",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.860230+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "46a603f5-592d-4409-8db9-2ace0914105b"
      },
      "request_id": "46a603f5-592d-4409-8db9-2ace0914105b",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007867920212447643,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 8",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.861022+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "7236a91c-67e3-4f60-8c68-11c47bd1cd15"
      },
      "request_id": "7236a91c-67e3-4f60-8c68-11c47bd1cd15",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007184171117842197,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 9",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.861746+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "81196596-c34d-4831-9f2c-449e6ab9182f"
      },
      "request_id": "81196596-c34d-4831-9f2c-449e6ab9182f",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007006670348346233,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 10",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.862451+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "317db6f5-f821-4729-b4fd-e6450ecc97fc"
      },
      "request_id": "317db6f5-f821-4729-b4fd-e6450ecc97fc",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007346663624048233,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 11",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.863193+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "30b19423-c128-4645-9419-7e963430680b"
      },
      "request_id": "30b19423-c128-4645-9419-7e963430680b",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.000676875002682209,
      "request_body_bytes": 48
    },
    {
      "name": "invalid allowance check 12",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.863875+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "4926d57f-d290-4875-a089-74478230fc1b"
      },
      "request_id": "4926d57f-d290-4875-a089-74478230fc1b",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0006304997950792313,
      "request_body_bytes": 48
    }
  ],
  "valid_requests": [
    {
      "name": "valid allowance check 1",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.864511+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "438c3d16-ca51-495b-97b4-564d6f0357b0"
      },
      "request_id": "438c3d16-ca51-495b-97b4-564d6f0357b0",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "646310d0-f8ff-4de8-b831-5749061fae66",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:28+00:00"
      },
      "elapsed_seconds": 0.040398791898041964,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 2",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.904917+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "29ed11e2-010f-4d24-85fb-323b1c8dd23b"
      },
      "request_id": "29ed11e2-010f-4d24-85fb-323b1c8dd23b",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "84d73bbd-72f1-4cab-8b51-09fe8c6171c9",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:28+00:00"
      },
      "elapsed_seconds": 0.04057725006714463,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 3",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.945502+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:28 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "16632f19-6b97-4c6b-928f-61dce25352a9"
      },
      "request_id": "16632f19-6b97-4c6b-928f-61dce25352a9",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "ec5032b5-1d6d-4b11-9ae3-2d2d133119a3",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:28+00:00"
      },
      "elapsed_seconds": 0.04030420910567045,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 4",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:28.985814+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "3741c2ec-b62b-4101-9141-e604caf53998"
      },
      "request_id": "3741c2ec-b62b-4101-9141-e604caf53998",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "8015962c-0478-4814-b9c5-169bd9e37b60",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.04040137492120266,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 5",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.026223+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "17fb3731-b397-4241-abbf-66d814817d03"
      },
      "request_id": "17fb3731-b397-4241-abbf-66d814817d03",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "2c9732bf-c351-46a5-946b-28e8c8c53365",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.04028933309018612,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 6",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.066520+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "a04bcd4f-071e-4ba6-b31c-858b913098d9"
      },
      "request_id": "a04bcd4f-071e-4ba6-b31c-858b913098d9",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "ce9a485c-c3ec-43ec-a58d-ec359bcb686f",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.040109542198479176,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 7",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.106638+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "8898719f-d83b-4d16-bc6f-7071be343721"
      },
      "request_id": "8898719f-d83b-4d16-bc6f-7071be343721",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "b5d9a760-e9e5-4002-ad78-b5787fa11df5",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.04012462496757507,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 8",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.146770+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "b5ac6bd9-212c-4f4a-a10e-1778687d6712"
      },
      "request_id": "b5ac6bd9-212c-4f4a-a10e-1778687d6712",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "cf7724cd-02c6-417c-8dcc-0f37f51407c9",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.040019792038947344,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 9",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.186797+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "c83144b5-c0d1-4751-b120-a6b662490c8b"
      },
      "request_id": "c83144b5-c0d1-4751-b120-a6b662490c8b",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "80a325f5-30d4-4807-9db4-adb3da37f92f",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.04042987525463104,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 10",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.227235+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "740",
        "X-Request-ID": "4f85d769-ea9a-4008-93bd-cef27b49262f"
      },
      "request_id": "4f85d769-ea9a-4008-93bd-cef27b49262f",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "c170eb25-f4dd-4365-ad9a-d0be8343209a",
        "creator_id": "cap-after-c2-t1-a1",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:29+00:00"
      },
      "elapsed_seconds": 0.04023108305409551,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 11",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.267480+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "de4bd42d-382a-49d2-ae1a-9d62dea195c7"
      },
      "request_id": "de4bd42d-382a-49d2-ae1a-9d62dea195c7",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0011464161798357964,
      "request_body_bytes": 425
    },
    {
      "name": "valid allowance check 12",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:29.268633+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:29 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "a7aefc36-df22-43c2-b459-283cf5151d44"
      },
      "request_id": "a7aefc36-df22-43c2-b459-283cf5151d44",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0008562090806663036,
      "request_body_bytes": 425
    }
  ],
  "quota_sequence_seconds": 0.41429012501612306,
  "quota_window_valid": true,
  "audit_parse_errors": [],
  "saved_decision_count": 10,
  "invalid400_count": 12,
  "valid200_count": 10,
  "throttled429_count": 2,
  "http_passed": true,
  "summary": "12/12 invalid400; 10/10 valid200; 2/2 quota429",
  "trial": 1,
  "attempt": 1,
  "criterion": 2,
  "evidence_directory": "results/capstone/after/c2_trial1_attempt1",
  "companion": {
    "required": true,
    "kind": "mocked isolated invocation check; not real inference",
    "command": [
      "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
      "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/scripts/capstone_call_counts.py",
      "--criterion",
      "2",
      "--trial",
      "1"
    ],
    "returncode": 0,
    "stderr": "",
    "result": {
      "criterion": 2,
      "trial": 1,
      "kind": "mocked isolated detector invocation check",
      "real_model_loaded": false,
      "conditions": [],
      "requests": [
        {
          "kind": "invalid",
          "index": 1,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 2,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 3,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 4,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 5,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 6,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 7,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 8,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 9,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 10,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 11,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 12,
          "status_code": 400,
          "response_json": {
            "error": "invalid_text",
            "message": "text must be a nonempty string."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 1,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "96524e09-d7db-4720-84ba-835e8c164720",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 2,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "ff4b289a-bb66-4798-831e-8110bd352f94",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 3,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "9e5884c6-0207-4aad-95ae-49d6396f16ff",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 4,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "2e94780d-7f8e-48be-a09c-54d18f1aef57",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 5,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "08146718-5561-4099-bc9b-de34b0ffc4cf",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 6,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "1b4cfc1a-b28d-4686-88d6-8343241b753b",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 7,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "c4509eba-c752-4cbe-aeb9-e74ec2693a63",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 8,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "15822645-141d-4ed2-af1d-2f6fdc6110f9",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 9,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "de79edc9-7d58-4bf0-9d1e-52329eb9d7f0",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 10,
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "ca1d55f4-300b-4af7-83c1-99b713a4a9c1",
            "creator_id": "mocked-c2-t1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:29+00:00"
          },
          "detector_calls": 1
        },
        {
          "kind": "valid",
          "index": 11,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 12,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        }
      ],
      "total_detector_calls": 10,
      "expected_statuses": [
        400,
        400,
        400,
        400,
        400,
        400,
        400,
        400,
        400,
        400,
        400,
        400,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        200,
        429,
        429
      ],
      "expected_calls": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        0,
        0
      ],
      "passed": true
    },
    "passed": true
  },
  "passed": true,
  "verdict": "MET",
  "invalid_attempts": []
}
```

### Criterion3

Produced by `scripts/run_capstone.py::criterion_three`.

```json
{
  "starts": [
    {
      "command": [
        "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
        "-m",
        "gunicorn",
        "--workers",
        "1",
        "--threads",
        "1",
        "--timeout",
        "120",
        "--bind",
        "127.0.0.1:59839",
        "app:app"
      ],
      "pid": 74912,
      "started_at_utc": "2026-11-14T02:08:34.933963+00:00",
      "url": "http://127.0.0.1:59839",
      "log_directory": "results/capstone/after/c3_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c3_trial1_attempt1",
        "AI201_RATE_LIMITS": "1",
        "HF_HUB_OFFLINE": "1",
        "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
      },
      "health_at_start": {
        "detector_loaded": false,
        "detector_model": "gpt2",
        "log_entries": 0,
        "ok": true,
        "rate_limiting": true
      },
      "health_request_id": "e4819117-23c8-4515-ae15-95265b6e7eca",
      "cold_warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:35.051191+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c3-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "745",
          "X-Request-ID": "fdbe2c19-836d-4310-9cae-81caf829daa8"
        },
        "request_id": "fdbe2c19-836d-4310-9cae-81caf829daa8",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "b99ad238-2697-4b6a-b078-f8c54e0c76fd",
          "creator_id": "cap-after-c3-t1-a1-warm",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 1.5744960838928819,
        "request_body_bytes": 430
      },
      "stopped_at_utc": "2026-11-14T02:08:37.680717+00:00",
      "returncode": 0
    }
  ],
  "warmup": {
    "name": "disclosed cold-model warm-up",
    "method": "POST",
    "path": "/submit",
    "sent_at_utc": "2026-11-14T02:08:35.051191+00:00",
    "request_json": {
      "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
      "creator_id": "cap-after-c3-t1-a1-warm"
    },
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "745",
      "X-Request-ID": "fdbe2c19-836d-4310-9cae-81caf829daa8"
    },
    "request_id": "fdbe2c19-836d-4310-9cae-81caf829daa8",
    "response_json": {
      "combined_score": 0.6593,
      "confidence": 0.6593,
      "content_id": "b99ad238-2697-4b6a-b078-f8c54e0c76fd",
      "creator_id": "cap-after-c3-t1-a1-warm",
      "detector_model": "gpt2",
      "guess": "unsure",
      "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
      "model_score": 0.6922,
      "status": "decided",
      "style_metrics": {
        "evenness": 0.5,
        "punctuation_density": 0.016286644951140065,
        "punctuation_simplicity": 0.8642779587404994,
        "repetition": 0.34976525821596255,
        "sentence_count": 2,
        "sentence_length_spread": 0.352112676056338,
        "style_score": 0.5278,
        "type_token_ratio": 0.6901408450704225,
        "word_count": 71
      },
      "style_score": 0.5278,
      "text_length": 377,
      "timestamp": "2026-11-14T02:08:36+00:00"
    },
    "elapsed_seconds": 1.5744960838928819,
    "request_body_bytes": 430
  },
  "quota_sequence_seconds": 0.6128189577721059,
  "quota_window_valid": true,
  "cases": [
    {
      "http": {
        "name": "observed valid 1",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.625699+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "740",
          "X-Request-ID": "fe84b749-c360-4274-adf2-b909bfcb26a9"
        },
        "request_id": "fe84b749-c360-4274-adf2-b909bfcb26a9",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 0.0429729581810534,
        "request_body_bytes": 425
      },
      "completion": {
        "event": "request_completed",
        "request_id": "fe84b749-c360-4274-adf2-b909bfcb26a9",
        "timestamp": "2026-11-14T02:08:36.668086+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 425,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 377
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 41.651125,
        "cpu_seconds": 0.057285
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 2",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.668686+00:00",
        "request_json": {
          "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "753",
          "X-Request-ID": "72666c6a-95a2-41b4-9b19-933298884426"
        },
        "request_id": "72666c6a-95a2-41b4-9b19-933298884426",
        "response_json": {
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "6819356d-16fd-4af2-ac8d-427ccd77d8b1",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4863,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.2554540936099331,
            "punctuation_density": 0.04021937842778794,
            "punctuation_simplicity": 0.6648385131017671,
            "repetition": 0.3276836158192091,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "style_score": 0.359,
            "type_token_ratio": 0.7033898305084746,
            "word_count": 118
          },
          "style_score": 0.359,
          "text_length": 664,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 0.06766049982979894,
        "request_body_bytes": 712
      },
      "completion": {
        "event": "request_completed",
        "request_id": "72666c6a-95a2-41b4-9b19-933298884426",
        "timestamp": "2026-11-14T02:08:36.735804+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 712,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 664
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "6819356d-16fd-4af2-ac8d-427ccd77d8b1",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 66.5395,
        "cpu_seconds": 0.103893
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 3",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.736358+00:00",
        "request_json": {
          "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "742",
          "X-Request-ID": "8b4763dd-0899-4d96-ad07-59bd1d78ed2f"
        },
        "request_id": "8b4763dd-0899-4d96-ad07-59bd1d78ed2f",
        "response_json": {
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "936748de-1092-4b15-bb75-990b6d08b172",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.3532,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.027522935779816515,
            "punctuation_simplicity": 0.7706422018348624,
            "repetition": 0.37356321839080464,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "style_score": 0.2662,
            "type_token_ratio": 0.6758620689655173,
            "word_count": 145
          },
          "style_score": 0.2662,
          "text_length": 795,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 0.07969416724517941,
        "request_body_bytes": 863
      },
      "completion": {
        "event": "request_completed",
        "request_id": "8b4763dd-0899-4d96-ad07-59bd1d78ed2f",
        "timestamp": "2026-11-14T02:08:36.815425+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 863,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 795
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "936748de-1092-4b15-bb75-990b6d08b172",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 78.103458,
        "cpu_seconds": 0.120754
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 4",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.816065+00:00",
        "request_json": {
          "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "756",
          "X-Request-ID": "dc168320-cd9a-450b-a740-34c0d53a41b0"
        },
        "request_id": "dc168320-cd9a-450b-a740-34c0d53a41b0",
        "response_json": {
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "233953a6-b49d-4e94-a9e0-45b40e24d163",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4097,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.16602391043278608,
            "punctuation_density": 0.053691275167785234,
            "punctuation_simplicity": 0.5525727069351231,
            "repetition": 0.48148148148148145,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "style_score": 0.338,
            "type_token_ratio": 0.6111111111111112,
            "word_count": 108
          },
          "style_score": 0.338,
          "text_length": 552,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 0.0617587910965085,
        "request_body_bytes": 625
      },
      "completion": {
        "event": "request_completed",
        "request_id": "dc168320-cd9a-450b-a740-34c0d53a41b0",
        "timestamp": "2026-11-14T02:08:36.877295+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 625,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 552
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "233953a6-b49d-4e94-a9e0-45b40e24d163",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 60.5475,
        "cpu_seconds": 0.090943
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 5",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.877840+00:00",
        "request_json": {
          "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "740",
          "X-Request-ID": "0e0f9643-6637-4945-929b-a508f44a391a"
        },
        "request_id": "0e0f9643-6637-4945-929b-a508f44a391a",
        "response_json": {
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "32e41624-5dac-43c3-bd39-6fe90b89b350",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7577,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.04195804195804196,
            "punctuation_simplicity": 0.6503496503496503,
            "repetition": 0.29227053140096626,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "style_score": 0.2178,
            "type_token_ratio": 0.7246376811594203,
            "word_count": 69
          },
          "style_score": 0.2178,
          "text_length": 354,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 0.0440435828641057,
        "request_body_bytes": 402
      },
      "completion": {
        "event": "request_completed",
        "request_id": "0e0f9643-6637-4945-929b-a508f44a391a",
        "timestamp": "2026-11-14T02:08:36.921350+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 402,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 354
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "32e41624-5dac-43c3-bd39-6fe90b89b350",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 42.961041,
        "cpu_seconds": 0.059885
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 6",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.921903+00:00",
        "request_json": {
          "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:36 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "756",
          "X-Request-ID": "a3c8ef24-21d4-408b-9326-5a5ae2d99ce9"
        },
        "request_id": "a3c8ef24-21d4-408b-9326-5a5ae2d99ce9",
        "response_json": {
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "8fd73fc5-e4b1-4d88-90bd-4a98c3588963",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5829,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.38795621995783924,
            "punctuation_density": 0.01937046004842615,
            "punctuation_simplicity": 0.8385794995964487,
            "repetition": 0.2640449438202247,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "style_score": 0.4409,
            "type_token_ratio": 0.7415730337078652,
            "word_count": 89
          },
          "style_score": 0.4409,
          "text_length": 501,
          "timestamp": "2026-11-14T02:08:36+00:00"
        },
        "elapsed_seconds": 0.04901112522929907,
        "request_body_bytes": 549
      },
      "completion": {
        "event": "request_completed",
        "request_id": "a3c8ef24-21d4-408b-9326-5a5ae2d99ce9",
        "timestamp": "2026-11-14T02:08:36.970403+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 549,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 501
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "8fd73fc5-e4b1-4d88-90bd-4a98c3588963",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 47.942708,
        "cpu_seconds": 0.068713
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 7",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:36.970924+00:00",
        "request_json": {
          "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "742",
          "X-Request-ID": "ce18c836-0838-4731-ac70-91dc42efbfa9"
        },
        "request_id": "ce18c836-0838-4731-ac70-91dc42efbfa9",
        "response_json": {
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "fabcb982-4380-4deb-9b83-dee5dbf6f14a",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5745,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.035343035343035345,
            "punctuation_simplicity": 0.7054747054747055,
            "repetition": 0.3790560471976401,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "style_score": 0.5048,
            "type_token_ratio": 0.672566371681416,
            "word_count": 113
          },
          "style_score": 0.5048,
          "text_length": 592,
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.0579759581014514,
        "request_body_bytes": 660
      },
      "completion": {
        "event": "request_completed",
        "request_id": "ce18c836-0838-4731-ac70-91dc42efbfa9",
        "timestamp": "2026-11-14T02:08:37.028421+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 660,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 592
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "fabcb982-4380-4deb-9b83-dee5dbf6f14a",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 56.94575,
        "cpu_seconds": 0.086038
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 8",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.028913+00:00",
        "request_json": {
          "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "755",
          "X-Request-ID": "3025ea5e-a91e-4957-a334-c45f19cb4486"
        },
        "request_id": "3025ea5e-a91e-4957-a334-c45f19cb4486",
        "response_json": {
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "c202a331-b153-49b6-8f5e-9bc5f46f33b2",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5825,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.420697370644045,
            "punctuation_density": 0.03232323232323232,
            "punctuation_simplicity": 0.7306397306397306,
            "repetition": 0.3473520249221185,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "style_score": 0.4607,
            "type_token_ratio": 0.6915887850467289,
            "word_count": 107
          },
          "style_score": 0.4607,
          "text_length": 598,
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.05577724985778332,
        "request_body_bytes": 661
      },
      "completion": {
        "event": "request_completed",
        "request_id": "3025ea5e-a91e-4957-a334-c45f19cb4486",
        "timestamp": "2026-11-14T02:08:37.084192+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 661,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 598
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "c202a331-b153-49b6-8f5e-9bc5f46f33b2",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 54.717125,
        "cpu_seconds": 0.081653
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 9",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.084706+00:00",
        "request_json": {
          "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "728",
          "X-Request-ID": "126a95a7-262f-48e7-8f27-e7115bb886a2"
        },
        "request_id": "126a95a7-262f-48e7-8f27-e7115bb886a2",
        "response_json": {
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "c493eeb2-d84b-4ae4-bd58-f1090572c2fe",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7648,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.26494047860054226,
            "punctuation_density": 0.018823529411764704,
            "punctuation_simplicity": 0.8431372549019608,
            "repetition": 0.6,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "style_score": 0.4811,
            "type_token_ratio": 0.54,
            "word_count": 100
          },
          "style_score": 0.4811,
          "text_length": 524,
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.051586125046014786,
        "request_body_bytes": 572
      },
      "completion": {
        "event": "request_completed",
        "request_id": "126a95a7-262f-48e7-8f27-e7115bb886a2",
        "timestamp": "2026-11-14T02:08:37.135760+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 572,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 524
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "c493eeb2-d84b-4ae4-bd58-f1090572c2fe",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 50.487709,
        "cpu_seconds": 0.072724
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 10",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.136304+00:00",
        "request_json": {
          "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "753",
          "X-Request-ID": "e30fbad1-099f-4883-8848-fd1843cee592"
        },
        "request_id": "e30fbad1-099f-4883-8848-fd1843cee592",
        "response_json": {
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "7a7c25b6-f8ff-491b-ae83-25e5a22b9830",
          "creator_id": "cap-after-c3-t1-a1",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.566,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.4729379744287563,
            "punctuation_density": 0.047058823529411764,
            "punctuation_simplicity": 0.607843137254902,
            "repetition": 0.3842975206611571,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "style_score": 0.4733,
            "type_token_ratio": 0.6694214876033058,
            "word_count": 121
          },
          "style_score": 0.4733,
          "text_length": 626,
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.08972024964168668,
        "request_body_bytes": 674
      },
      "completion": {
        "event": "request_completed",
        "request_id": "e30fbad1-099f-4883-8848-fd1843cee592",
        "timestamp": "2026-11-14T02:08:37.225457+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 674,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 626
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "7a7c25b6-f8ff-491b-ae83-25e5a22b9830",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 88.540667,
        "cpu_seconds": 0.110455
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed quota 1",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.226045+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 429,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "78",
          "X-Request-ID": "4808f340-ebe1-4ef5-8eff-eb7c46654878"
        },
        "request_id": "4808f340-ebe1-4ef5-8eff-eb7c46654878",
        "response_json": {
          "error": "rate_limited",
          "message": "Too many submissions. Try again shortly."
        },
        "elapsed_seconds": 0.0014075003564357758,
        "request_body_bytes": 425
      },
      "completion": {
        "event": "request_completed",
        "request_id": "4808f340-ebe1-4ef5-8eff-eb7c46654878",
        "timestamp": "2026-11-14T02:08:37.227083+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 429,
        "input_summary": {
          "body_bytes": 425,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 377
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "rate_limited",
          "outcome": "error"
        },
        "duration_ms": 0.413625,
        "cpu_seconds": 0.000405
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed quota 2",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.227466+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c3-t1-a1"
        },
        "status_code": 429,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "78",
          "X-Request-ID": "49983aa0-838e-40fc-a4ad-7592e9873abc"
        },
        "request_id": "49983aa0-838e-40fc-a4ad-7592e9873abc",
        "response_json": {
          "error": "rate_limited",
          "message": "Too many submissions. Try again shortly."
        },
        "elapsed_seconds": 0.0010443329811096191,
        "request_body_bytes": 425
      },
      "completion": {
        "event": "request_completed",
        "request_id": "49983aa0-838e-40fc-a4ad-7592e9873abc",
        "timestamp": "2026-11-14T02:08:37.228216+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 429,
        "input_summary": {
          "body_bytes": 425,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 377
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "rate_limited",
          "outcome": "error"
        },
        "duration_ms": 0.262084,
        "cpu_seconds": 0.000251
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 1",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.228520+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-after-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "722f9fc2-8542-46c0-bf63-12a522d13355"
        },
        "request_id": "722f9fc2-8542-46c0-bf63-12a522d13355",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0007982091046869755,
        "request_body_bytes": 56
      },
      "completion": {
        "event": "request_completed",
        "request_id": "722f9fc2-8542-46c0-bf63-12a522d13355",
        "timestamp": "2026-11-14T02:08:37.229079+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 56,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 0
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "invalid_text",
          "outcome": "error"
        },
        "duration_ms": 0.140083,
        "cpu_seconds": 0.000128
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 2",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.229326+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-after-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "aa1d0174-d333-44cf-b42d-eab11a4461de"
        },
        "request_id": "aa1d0174-d333-44cf-b42d-eab11a4461de",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.000998165924102068,
        "request_body_bytes": 56
      },
      "completion": {
        "event": "request_completed",
        "request_id": "aa1d0174-d333-44cf-b42d-eab11a4461de",
        "timestamp": "2026-11-14T02:08:37.230007+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 56,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 0
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "invalid_text",
          "outcome": "error"
        },
        "duration_ms": 0.180833,
        "cpu_seconds": 0.000172
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 3",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.230332+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-after-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "74cebdce-d695-41ce-87ad-0598653c386f"
        },
        "request_id": "74cebdce-d695-41ce-87ad-0598653c386f",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0008508753962814808,
        "request_body_bytes": 56
      },
      "completion": {
        "event": "request_completed",
        "request_id": "74cebdce-d695-41ce-87ad-0598653c386f",
        "timestamp": "2026-11-14T02:08:37.230897+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 56,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 0
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "invalid_text",
          "outcome": "error"
        },
        "duration_ms": 0.14375,
        "cpu_seconds": 0.00013
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 4",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.231191+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-after-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "a321a371-8036-4dc2-9052-c14dc3a1d5ed"
        },
        "request_id": "a321a371-8036-4dc2-9052-c14dc3a1d5ed",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0008994159288704395,
        "request_body_bytes": 56
      },
      "completion": {
        "event": "request_completed",
        "request_id": "a321a371-8036-4dc2-9052-c14dc3a1d5ed",
        "timestamp": "2026-11-14T02:08:37.231797+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 56,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 0
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "invalid_text",
          "outcome": "error"
        },
        "duration_ms": 0.184792,
        "cpu_seconds": 0.000175
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 5",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:37.232097+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-after-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "2d24b69a-0f66-4052-b33e-c0217667838d"
        },
        "request_id": "2d24b69a-0f66-4052-b33e-c0217667838d",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0008123749867081642,
        "request_body_bytes": 56
      },
      "completion": {
        "event": "request_completed",
        "request_id": "2d24b69a-0f66-4052-b33e-c0217667838d",
        "timestamp": "2026-11-14T02:08:37.232634+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 56,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "creator_id",
            "text"
          ],
          "field_count": 2,
          "field_names_truncated": false,
          "text_characters": 0
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "invalid_text",
          "outcome": "error"
        },
        "duration_ms": 0.146959,
        "cpu_seconds": 0.000131
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 1",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:08:37.232923+00:00",
        "request_json": {
          "content_id": "c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b",
          "reasoning": "  Capstone review 1: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "310",
          "X-Request-ID": "5cdd7dc4-ea07-4ba3-88af-219bd2536afb"
        },
        "request_id": "5cdd7dc4-ea07-4ba3-88af-219bd2536afb",
        "response_json": {
          "content_id": "c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b",
          "creator_id": "cap-after-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 1: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.0010179579257965088,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "5cdd7dc4-ea07-4ba3-88af-219bd2536afb",
        "timestamp": "2026-11-14T02:08:37.233662+00:00",
        "method": "POST",
        "path": "/appeal",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 120,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "content_id",
            "reasoning"
          ],
          "field_count": 2,
          "field_names_truncated": false
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.321417,
        "cpu_seconds": 0.000312
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 2",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:08:37.233949+00:00",
        "request_json": {
          "content_id": "6819356d-16fd-4af2-ac8d-427ccd77d8b1",
          "reasoning": "  Capstone review 2: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "310",
          "X-Request-ID": "a8142650-7e71-443b-80a2-0dc7af0231bb"
        },
        "request_id": "a8142650-7e71-443b-80a2-0dc7af0231bb",
        "response_json": {
          "content_id": "6819356d-16fd-4af2-ac8d-427ccd77d8b1",
          "creator_id": "cap-after-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 2: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.0009285830892622471,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "a8142650-7e71-443b-80a2-0dc7af0231bb",
        "timestamp": "2026-11-14T02:08:37.234611+00:00",
        "method": "POST",
        "path": "/appeal",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 120,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "content_id",
            "reasoning"
          ],
          "field_count": 2,
          "field_names_truncated": false
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "6819356d-16fd-4af2-ac8d-427ccd77d8b1",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.268125,
        "cpu_seconds": 0.000247
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 3",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:08:37.234884+00:00",
        "request_json": {
          "content_id": "936748de-1092-4b15-bb75-990b6d08b172",
          "reasoning": "  Capstone review 3: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "310",
          "X-Request-ID": "07371991-9fb5-4267-919e-769baf52e412"
        },
        "request_id": "07371991-9fb5-4267-919e-769baf52e412",
        "response_json": {
          "content_id": "936748de-1092-4b15-bb75-990b6d08b172",
          "creator_id": "cap-after-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 3: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.00089216697961092,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "07371991-9fb5-4267-919e-769baf52e412",
        "timestamp": "2026-11-14T02:08:37.235510+00:00",
        "method": "POST",
        "path": "/appeal",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 120,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "content_id",
            "reasoning"
          ],
          "field_count": 2,
          "field_names_truncated": false
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "936748de-1092-4b15-bb75-990b6d08b172",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.25375,
        "cpu_seconds": 0.000241
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 4",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:08:37.235783+00:00",
        "request_json": {
          "content_id": "233953a6-b49d-4e94-a9e0-45b40e24d163",
          "reasoning": "  Capstone review 4: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "310",
          "X-Request-ID": "bc44921f-8464-459c-bcdd-14a038fbaf93"
        },
        "request_id": "bc44921f-8464-459c-bcdd-14a038fbaf93",
        "response_json": {
          "content_id": "233953a6-b49d-4e94-a9e0-45b40e24d163",
          "creator_id": "cap-after-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 4: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.0009067496284842491,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "bc44921f-8464-459c-bcdd-14a038fbaf93",
        "timestamp": "2026-11-14T02:08:37.236451+00:00",
        "method": "POST",
        "path": "/appeal",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 120,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "content_id",
            "reasoning"
          ],
          "field_count": 2,
          "field_names_truncated": false
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "233953a6-b49d-4e94-a9e0-45b40e24d163",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.266792,
        "cpu_seconds": 0.000244
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 5",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:08:37.236696+00:00",
        "request_json": {
          "content_id": "32e41624-5dac-43c3-bd39-6fe90b89b350",
          "reasoning": "  Capstone review 5: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "310",
          "X-Request-ID": "13e524d3-ea9e-42a3-80b2-ab878b04114b"
        },
        "request_id": "13e524d3-ea9e-42a3-80b2-ab878b04114b",
        "response_json": {
          "content_id": "32e41624-5dac-43c3-bd39-6fe90b89b350",
          "creator_id": "cap-after-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 5: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:08:37+00:00"
        },
        "elapsed_seconds": 0.0008852500468492508,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "13e524d3-ea9e-42a3-80b2-ab878b04114b",
        "timestamp": "2026-11-14T02:08:37.237329+00:00",
        "method": "POST",
        "path": "/appeal",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 120,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "content_id",
            "reasoning"
          ],
          "field_count": 2,
          "field_names_truncated": false
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "32e41624-5dac-43c3-bd39-6fe90b89b350",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.252541,
        "cpu_seconds": 0.000238
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed unknown appeal",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:08:37.237587+00:00",
        "request_json": {
          "content_id": "00000000-0000-4000-8000-000000000099",
          "reasoning": "  Capstone review 99: please consider my drafts.  "
        },
        "status_code": 404,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:37 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "85",
          "X-Request-ID": "249a5ecb-37f0-4c3c-82a5-06ac160d5550"
        },
        "request_id": "249a5ecb-37f0-4c3c-82a5-06ac160d5550",
        "response_json": {
          "error": "content_not_found",
          "message": "No submission exists with this content_id."
        },
        "elapsed_seconds": 0.0009123329073190689,
        "request_body_bytes": 121
      },
      "completion": {
        "event": "request_completed",
        "request_id": "249a5ecb-37f0-4c3c-82a5-06ac160d5550",
        "timestamp": "2026-11-14T02:08:37.238246+00:00",
        "method": "POST",
        "path": "/appeal",
        "http_status": 404,
        "input_summary": {
          "body_bytes": 121,
          "content_type": "application/json",
          "parsing": "json_object",
          "field_names": [
            "content_id",
            "reasoning"
          ],
          "field_count": 2,
          "field_names_truncated": false
        },
        "output_summary": {
          "content_type": "application/json",
          "error": "content_not_found",
          "outcome": "error"
        },
        "duration_ms": 0.268541,
        "cpu_seconds": 0.000251
      },
      "errors": [],
      "passed": true
    }
  ],
  "request_log_parse_errors": [],
  "expected_http_statuses": [
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    429,
    429,
    400,
    400,
    400,
    400,
    400,
    200,
    200,
    200,
    200,
    200,
    404
  ],
  "actual_statuses": [
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    200,
    429,
    429,
    400,
    400,
    400,
    400,
    400,
    200,
    200,
    200,
    200,
    200,
    404
  ],
  "outcome_sequence_matches": true,
  "completion_count": 23,
  "http_passed": true,
  "summary": "23/23 complete records; HTTP sequence=True",
  "trial": 1,
  "attempt": 1,
  "criterion": 3,
  "evidence_directory": "results/capstone/after/c3_trial1_attempt1",
  "companion": {
    "required": false,
    "passed": true
  },
  "passed": true,
  "verdict": "MET",
  "invalid_attempts": []
}
```

### Criterion4

Produced by `scripts/run_capstone.py::criterion_four`.

```json
{
  "starts": [
    {
      "command": [
        "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
        "-m",
        "gunicorn",
        "--workers",
        "1",
        "--threads",
        "1",
        "--timeout",
        "120",
        "--bind",
        "127.0.0.1:59924",
        "app:app"
      ],
      "pid": 74944,
      "started_at_utc": "2026-11-14T02:08:42.980661+00:00",
      "url": "http://127.0.0.1:59924",
      "log_directory": "results/capstone/after/c4_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c4_trial1_attempt1",
        "AI201_RATE_LIMITS": "1",
        "HF_HUB_OFFLINE": "1",
        "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
      },
      "health_at_start": {
        "detector_loaded": false,
        "detector_model": "gpt2",
        "log_entries": 0,
        "ok": true,
        "rate_limiting": true
      },
      "health_request_id": "d4a4d9b6-297e-4a51-9219-d8e1e668a710",
      "cold_warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:43.105292+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c4-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "745",
          "X-Request-ID": "feb04f5a-42db-473f-8b2b-29ac3e1358d9"
        },
        "request_id": "feb04f5a-42db-473f-8b2b-29ac3e1358d9",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "f0bf901d-107a-47e3-a1f3-b66427ede584",
          "creator_id": "cap-after-c4-t1-a1-warm",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:44+00:00"
        },
        "elapsed_seconds": 1.5193649581633508,
        "request_body_bytes": 430
      },
      "stopped_at_utc": "2026-11-14T02:08:45.527790+00:00",
      "returncode": 0
    }
  ],
  "cold_warmup": {
    "name": "disclosed cold-model warm-up",
    "method": "POST",
    "path": "/submit",
    "sent_at_utc": "2026-11-14T02:08:43.105292+00:00",
    "request_json": {
      "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
      "creator_id": "cap-after-c4-t1-a1-warm"
    },
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "745",
      "X-Request-ID": "feb04f5a-42db-473f-8b2b-29ac3e1358d9"
    },
    "request_id": "feb04f5a-42db-473f-8b2b-29ac3e1358d9",
    "response_json": {
      "combined_score": 0.6593,
      "confidence": 0.6593,
      "content_id": "f0bf901d-107a-47e3-a1f3-b66427ede584",
      "creator_id": "cap-after-c4-t1-a1-warm",
      "detector_model": "gpt2",
      "guess": "unsure",
      "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
      "model_score": 0.6922,
      "status": "decided",
      "style_metrics": {
        "evenness": 0.5,
        "punctuation_density": 0.016286644951140065,
        "punctuation_simplicity": 0.8642779587404994,
        "repetition": 0.34976525821596255,
        "sentence_count": 2,
        "sentence_length_spread": 0.352112676056338,
        "style_score": 0.5278,
        "type_token_ratio": 0.6901408450704225,
        "word_count": 71
      },
      "style_score": 0.5278,
      "text_length": 377,
      "timestamp": "2026-11-14T02:08:44+00:00"
    },
    "elapsed_seconds": 1.5193649581633508,
    "request_body_bytes": 430
  },
  "cases": [
    {
      "name": "warm timed human-01",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.624665+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-after-c4-t1-a1-human-01"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "749",
        "X-Request-ID": "365d8021-2758-4f2f-a2c5-199e1e2c059b"
      },
      "request_id": "365d8021-2758-4f2f-a2c5-199e1e2c059b",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "8f82248e-5fb6-4432-bf10-af9cf086ead9",
        "creator_id": "cap-after-c4-t1-a1-human-01",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.6922,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.016286644951140065,
          "punctuation_simplicity": 0.8642779587404994,
          "repetition": 0.34976525821596255,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "style_score": 0.5278,
          "type_token_ratio": 0.6901408450704225,
          "word_count": 71
        },
        "style_score": 0.5278,
        "text_length": 377,
        "timestamp": "2026-11-14T02:08:44+00:00"
      },
      "elapsed_seconds": 0.04083670908585191,
      "request_body_bytes": 434
    },
    {
      "name": "warm timed human-02",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.665515+00:00",
      "request_json": {
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "creator_id": "cap-after-c4-t1-a1-human-02"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "762",
        "X-Request-ID": "5f822487-38c8-4695-8004-ed6ca5392044"
      },
      "request_id": "5f822487-38c8-4695-8004-ed6ca5392044",
      "response_json": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "956083a5-f287-4f99-8f07-7d5860502934",
        "creator_id": "cap-after-c4-t1-a1-human-02",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4863,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.2554540936099331,
          "punctuation_density": 0.04021937842778794,
          "punctuation_simplicity": 0.6648385131017671,
          "repetition": 0.3276836158192091,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "style_score": 0.359,
          "type_token_ratio": 0.7033898305084746,
          "word_count": 118
        },
        "style_score": 0.359,
        "text_length": 664,
        "timestamp": "2026-11-14T02:08:44+00:00"
      },
      "elapsed_seconds": 0.06880754185840487,
      "request_body_bytes": 721
    },
    {
      "name": "warm timed human-03",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.734336+00:00",
      "request_json": {
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "creator_id": "cap-after-c4-t1-a1-human-03"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "751",
        "X-Request-ID": "8af8305e-2461-4097-8487-c46d34da2d74"
      },
      "request_id": "8af8305e-2461-4097-8487-c46d34da2d74",
      "response_json": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "6ba277bc-fd04-496f-a121-e50b7200da96",
        "creator_id": "cap-after-c4-t1-a1-human-03",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.3532,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.027522935779816515,
          "punctuation_simplicity": 0.7706422018348624,
          "repetition": 0.37356321839080464,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "style_score": 0.2662,
          "type_token_ratio": 0.6758620689655173,
          "word_count": 145
        },
        "style_score": 0.2662,
        "text_length": 795,
        "timestamp": "2026-11-14T02:08:44+00:00"
      },
      "elapsed_seconds": 0.07307741604745388,
      "request_body_bytes": 872
    },
    {
      "name": "warm timed human-04",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.807426+00:00",
      "request_json": {
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "creator_id": "cap-after-c4-t1-a1-human-04"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "765",
        "X-Request-ID": "58d2a11a-4e86-490a-9628-99acec293a93"
      },
      "request_id": "58d2a11a-4e86-490a-9628-99acec293a93",
      "response_json": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "8704aa0c-37ab-45b0-994a-0fe6e02159bd",
        "creator_id": "cap-after-c4-t1-a1-human-04",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.4097,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.16602391043278608,
          "punctuation_density": 0.053691275167785234,
          "punctuation_simplicity": 0.5525727069351231,
          "repetition": 0.48148148148148145,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "style_score": 0.338,
          "type_token_ratio": 0.6111111111111112,
          "word_count": 108
        },
        "style_score": 0.338,
        "text_length": 552,
        "timestamp": "2026-11-14T02:08:44+00:00"
      },
      "elapsed_seconds": 0.06044883420690894,
      "request_body_bytes": 634
    },
    {
      "name": "warm timed human-05",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.867889+00:00",
      "request_json": {
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "creator_id": "cap-after-c4-t1-a1-human-05"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "749",
        "X-Request-ID": "e59a5c8b-9f42-43ef-8de3-229c4d673070"
      },
      "request_id": "e59a5c8b-9f42-43ef-8de3-229c4d673070",
      "response_json": {
        "combined_score": 0.6497,
        "confidence": 0.6497,
        "content_id": "288ef9a0-0e40-47a7-9100-f45403ddfdbc",
        "creator_id": "cap-after-c4-t1-a1-human-05",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7577,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.0,
          "punctuation_density": 0.04195804195804196,
          "punctuation_simplicity": 0.6503496503496503,
          "repetition": 0.29227053140096626,
          "sentence_count": 3,
          "sentence_length_spread": 0.8615573303015565,
          "style_score": 0.2178,
          "type_token_ratio": 0.7246376811594203,
          "word_count": 69
        },
        "style_score": 0.2178,
        "text_length": 354,
        "timestamp": "2026-11-14T02:08:44+00:00"
      },
      "elapsed_seconds": 0.043491417076438665,
      "request_body_bytes": 411
    },
    {
      "name": "warm timed human-06",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.911392+00:00",
      "request_json": {
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "creator_id": "cap-after-c4-t1-a1-human-06"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:44 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "765",
        "X-Request-ID": "ecc04610-b764-40fa-a7e3-d4057de2df80"
      },
      "request_id": "ecc04610-b764-40fa-a7e3-d4057de2df80",
      "response_json": {
        "combined_score": 0.5545,
        "confidence": 0.5545,
        "content_id": "56cb9828-47b7-4c46-b39b-a9cd70a11b32",
        "creator_id": "cap-after-c4-t1-a1-human-06",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5829,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.38795621995783924,
          "punctuation_density": 0.01937046004842615,
          "punctuation_simplicity": 0.8385794995964487,
          "repetition": 0.2640449438202247,
          "sentence_count": 4,
          "sentence_length_spread": 0.48963502403372866,
          "style_score": 0.4409,
          "type_token_ratio": 0.7415730337078652,
          "word_count": 89
        },
        "style_score": 0.4409,
        "text_length": 501,
        "timestamp": "2026-11-14T02:08:44+00:00"
      },
      "elapsed_seconds": 0.04866529116407037,
      "request_body_bytes": 558
    },
    {
      "name": "warm timed human-07",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:44.960066+00:00",
      "request_json": {
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "creator_id": "cap-after-c4-t1-a1-human-07"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:45 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "751",
        "X-Request-ID": "89b34a46-b865-4b30-9f98-285c7edf5936"
      },
      "request_id": "89b34a46-b865-4b30-9f98-285c7edf5936",
      "response_json": {
        "combined_score": 0.5606,
        "confidence": 0.5606,
        "content_id": "95fce8f3-73e0-437f-9cdc-74c8c796bd2f",
        "creator_id": "cap-after-c4-t1-a1-human-07",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5745,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.5,
          "punctuation_density": 0.035343035343035345,
          "punctuation_simplicity": 0.7054747054747055,
          "repetition": 0.3790560471976401,
          "sentence_count": 2,
          "sentence_length_spread": 0.008849557522123894,
          "style_score": 0.5048,
          "type_token_ratio": 0.672566371681416,
          "word_count": 113
        },
        "style_score": 0.5048,
        "text_length": 592,
        "timestamp": "2026-11-14T02:08:45+00:00"
      },
      "elapsed_seconds": 0.05802450003102422,
      "request_body_bytes": 669
    },
    {
      "name": "warm timed human-08",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:45.018100+00:00",
      "request_json": {
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "creator_id": "cap-after-c4-t1-a1-human-08"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:45 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "764",
        "X-Request-ID": "5181b6ca-59b5-4b7c-8373-15967c1358a6"
      },
      "request_id": "5181b6ca-59b5-4b7c-8373-15967c1358a6",
      "response_json": {
        "combined_score": 0.5581,
        "confidence": 0.5581,
        "content_id": "23516fc6-3f7d-49c9-a94a-f99201830bc5",
        "creator_id": "cap-after-c4-t1-a1-human-08",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.5825,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.420697370644045,
          "punctuation_density": 0.03232323232323232,
          "punctuation_simplicity": 0.7306397306397306,
          "repetition": 0.3473520249221185,
          "sentence_count": 4,
          "sentence_length_spread": 0.46344210348476406,
          "style_score": 0.4607,
          "type_token_ratio": 0.6915887850467289,
          "word_count": 107
        },
        "style_score": 0.4607,
        "text_length": 598,
        "timestamp": "2026-11-14T02:08:45+00:00"
      },
      "elapsed_seconds": 0.05366337485611439,
      "request_body_bytes": 670
    },
    {
      "name": "warm timed human-09",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:45.071774+00:00",
      "request_json": {
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "creator_id": "cap-after-c4-t1-a1-human-09"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:45 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "737",
        "X-Request-ID": "0e021174-6838-46fe-8740-b77c441a5ea7"
      },
      "request_id": "0e021174-6838-46fe-8740-b77c441a5ea7",
      "response_json": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "e9f6a6ba-27a4-4476-be5d-f62c143b900a",
        "creator_id": "cap-after-c4-t1-a1-human-09",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.7648,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.26494047860054226,
          "punctuation_density": 0.018823529411764704,
          "punctuation_simplicity": 0.8431372549019608,
          "repetition": 0.6,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "style_score": 0.4811,
          "type_token_ratio": 0.54,
          "word_count": 100
        },
        "style_score": 0.4811,
        "text_length": 524,
        "timestamp": "2026-11-14T02:08:45+00:00"
      },
      "elapsed_seconds": 0.04990345798432827,
      "request_body_bytes": 581
    },
    {
      "name": "warm timed human-10",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:08:45.121688+00:00",
      "request_json": {
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "creator_id": "cap-after-c4-t1-a1-human-10"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:08:45 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "762",
        "X-Request-ID": "8a9a96c9-e8f4-460a-816d-bf96995361bd"
      },
      "request_id": "8a9a96c9-e8f4-460a-816d-bf96995361bd",
      "response_json": {
        "combined_score": 0.5475,
        "confidence": 0.5475,
        "content_id": "4eaba0c4-5fdb-41c5-a6ba-37b0498477c3",
        "creator_id": "cap-after-c4-t1-a1-human-10",
        "detector_model": "gpt2",
        "guess": "unsure",
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "model_score": 0.566,
        "status": "decided",
        "style_metrics": {
          "evenness": 0.4729379744287563,
          "punctuation_density": 0.047058823529411764,
          "punctuation_simplicity": 0.607843137254902,
          "repetition": 0.3842975206611571,
          "sentence_count": 4,
          "sentence_length_spread": 0.421649620456995,
          "style_score": 0.4733,
          "type_token_ratio": 0.6694214876033058,
          "word_count": 121
        },
        "style_score": 0.4733,
        "text_length": 626,
        "timestamp": "2026-11-14T02:08:45+00:00"
      },
      "elapsed_seconds": 0.061340208165347576,
      "request_body_bytes": 683
    }
  ],
  "valid_count": 10,
  "under5_seconds_count": 10,
  "mean_wall_seconds": 0.05582587504759431,
  "wall_seconds": [
    0.04083670908585191,
    0.06880754185840487,
    0.07307741604745388,
    0.06044883420690894,
    0.043491417076438665,
    0.04866529116407037,
    0.05802450003102422,
    0.05366337485611439,
    0.04990345798432827,
    0.061340208165347576
  ],
  "cpu_seconds": [
    0.055038,
    0.105668,
    0.114528,
    0.089926,
    0.059143,
    0.068329,
    0.086254,
    0.079041,
    0.070982,
    0.091536
  ],
  "mean_cpu_seconds": 0.0820445,
  "cost_measurement_errors": [],
  "request_log_parse_errors": [],
  "quota_window_valid": true,
  "http_passed": true,
  "summary": "10/10 decisions; 10/10<5s; mean0.0558s",
  "trial": 1,
  "attempt": 1,
  "criterion": 4,
  "evidence_directory": "results/capstone/after/c4_trial1_attempt1",
  "companion": {
    "required": false,
    "passed": true
  },
  "passed": true,
  "verdict": "MET",
  "invalid_attempts": []
}
```

### Criterion5

Produced by `scripts/run_capstone.py::criterion_five`.

```json
{
  "starts": [
    {
      "command": [
        "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
        "-m",
        "gunicorn",
        "--workers",
        "1",
        "--threads",
        "1",
        "--timeout",
        "120",
        "--bind",
        "127.0.0.1:59971",
        "app:app"
      ],
      "pid": 74972,
      "started_at_utc": "2026-11-14T02:08:50.721550+00:00",
      "url": "http://127.0.0.1:59971",
      "log_directory": "results/capstone/after/c5_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c5_trial1_attempt1",
        "AI201_RATE_LIMITS": "1",
        "HF_HUB_OFFLINE": "1",
        "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
      },
      "health_at_start": {
        "detector_loaded": false,
        "detector_model": "gpt2",
        "log_entries": 0,
        "ok": true,
        "rate_limiting": true
      },
      "health_request_id": "1d1d69c8-8303-4eaa-807d-52c6624440a5",
      "stopped_at_utc": "2026-11-14T02:08:53.267619+00:00",
      "returncode": 0
    },
    {
      "command": [
        "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
        "-m",
        "gunicorn",
        "--workers",
        "1",
        "--threads",
        "1",
        "--timeout",
        "120",
        "--bind",
        "127.0.0.1:59995",
        "app:app"
      ],
      "pid": 74985,
      "started_at_utc": "2026-11-14T02:08:53.270091+00:00",
      "url": "http://127.0.0.1:59995",
      "log_directory": "results/capstone/after/c5_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/after/c5_trial1_attempt1",
        "AI201_RATE_LIMITS": "1",
        "HF_HUB_OFFLINE": "1",
        "HF_HOME": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.cache/huggingface"
      },
      "health_at_start": {
        "detector_loaded": false,
        "detector_model": "gpt2",
        "log_entries": 20,
        "ok": true,
        "rate_limiting": true
      },
      "health_request_id": "0ab109df-3487-4f3e-98e4-5cc1c44727a4",
      "stopped_at_utc": "2026-11-14T02:08:53.525422+00:00",
      "returncode": 0
    }
  ],
  "detector_unloaded_at_restart": true,
  "cases": [
    {
      "submission": {
        "name": "appeal setup human-01",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:50.843197+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-after-c5-t1-a1-human-01"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "749",
          "X-Request-ID": "9e66f542-7573-4505-8478-69f97ea6428b"
        },
        "request_id": "9e66f542-7573-4505-8478-69f97ea6428b",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
          "creator_id": "cap-after-c5-t1-a1-human-01",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 1.5559863750822842,
        "request_body_bytes": 434
      },
      "appeal": {
        "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
        "reasoning": "  Capstone review 1: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 1",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.918564+00:00",
          "request_json": {
            "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
            "reasoning": "  Capstone review 1: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "67940529-1ec8-4fa7-b103-21de9acba97b"
          },
          "request_id": "67940529-1ec8-4fa7-b103-21de9acba97b",
          "response_json": {
            "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
            "creator_id": "cap-after-c5-t1-a1-human-01",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 1: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0012355828657746315,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 1",
        "method": "GET",
        "path": "/content/8d132cf2-9582-4769-a4ce-75b4555f197a",
        "sent_at_utc": "2026-11-14T02:08:53.387156+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1008",
          "X-Request-ID": "6ba3989c-177e-4a2f-923d-f317e6211c3b"
        },
        "request_id": "6ba3989c-177e-4a2f-923d-f317e6211c3b",
        "response_json": {
          "appeals": [
            {
              "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
              "creator_id": "cap-after-c5-t1-a1-human-01",
              "event": "appeal",
              "reasoning": "  Capstone review 1: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
          "creator_id": "cap-after-c5-t1-a1-human-01",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.6922,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.016286644951140065,
            "punctuation_simplicity": 0.8642779587404994,
            "repetition": 0.34976525821596255,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "style_score": 0.5278,
            "type_token_ratio": 0.6901408450704225,
            "word_count": 71
          },
          "style_score": 0.5278,
          "text_length": 377,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.001060541719198227,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
        "creator_id": "cap-after-c5-t1-a1-human-01",
        "guess": "unsure",
        "model_score": 0.6922,
        "style_score": 0.5278,
        "combined_score": 0.6593,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.6593,
        "style_metrics": {
          "word_count": 71,
          "sentence_count": 2,
          "sentence_length_spread": 0.352112676056338,
          "type_token_ratio": 0.6901408450704225,
          "punctuation_density": 0.016286644951140065,
          "evenness": 0.5,
          "repetition": 0.34976525821596255,
          "punctuation_simplicity": 0.8642779587404994,
          "style_score": 0.5278
        },
        "text_length": 377,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
          "creator_id": "cap-after-c5-t1-a1-human-01",
          "guess": "unsure",
          "model_score": 0.6922,
          "style_score": 0.5278,
          "combined_score": 0.6593,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.6593,
          "style_metrics": {
            "word_count": 71,
            "sentence_count": 2,
            "sentence_length_spread": 0.352112676056338,
            "type_token_ratio": 0.6901408450704225,
            "punctuation_density": 0.016286644951140065,
            "evenness": 0.5,
            "repetition": 0.34976525821596255,
            "punctuation_simplicity": 0.8642779587404994,
            "style_score": 0.5278
          },
          "text_length": 377,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
          "creator_id": "cap-after-c5-t1-a1-human-01",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 1: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-02",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.399177+00:00",
        "request_json": {
          "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
          "creator_id": "cap-after-c5-t1-a1-human-02"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "762",
          "X-Request-ID": "46543ce8-3a01-49d6-af04-b078ae9dd7b1"
        },
        "request_id": "46543ce8-3a01-49d6-af04-b078ae9dd7b1",
        "response_json": {
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
          "creator_id": "cap-after-c5-t1-a1-human-02",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4863,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.2554540936099331,
            "punctuation_density": 0.04021937842778794,
            "punctuation_simplicity": 0.6648385131017671,
            "repetition": 0.3276836158192091,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "style_score": 0.359,
            "type_token_ratio": 0.7033898305084746,
            "word_count": 118
          },
          "style_score": 0.359,
          "text_length": 664,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.06737391697242856,
        "request_body_bytes": 721
      },
      "appeal": {
        "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
        "reasoning": "  Capstone review 2: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 2",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.919812+00:00",
          "request_json": {
            "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
            "reasoning": "  Capstone review 2: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "d8c78fe6-388a-44a5-a8a3-7a6054031d15"
          },
          "request_id": "d8c78fe6-388a-44a5-a8a3-7a6054031d15",
          "response_json": {
            "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
            "creator_id": "cap-after-c5-t1-a1-human-02",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 2: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0009385412558913231,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 2",
        "method": "GET",
        "path": "/content/fe95b565-7519-45ab-abb4-05d30ca347f5",
        "sent_at_utc": "2026-11-14T02:08:53.388231+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1021",
          "X-Request-ID": "3fe8776e-910d-4a5e-adc2-68ff29a5535f"
        },
        "request_id": "3fe8776e-910d-4a5e-adc2-68ff29a5535f",
        "response_json": {
          "appeals": [
            {
              "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
              "creator_id": "cap-after-c5-t1-a1-human-02",
              "event": "appeal",
              "reasoning": "  Capstone review 2: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
          "creator_id": "cap-after-c5-t1-a1-human-02",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4863,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.2554540936099331,
            "punctuation_density": 0.04021937842778794,
            "punctuation_simplicity": 0.6648385131017671,
            "repetition": 0.3276836158192091,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "style_score": 0.359,
            "type_token_ratio": 0.7033898305084746,
            "word_count": 118
          },
          "style_score": 0.359,
          "text_length": 664,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0008967500180006027,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
        "creator_id": "cap-after-c5-t1-a1-human-02",
        "guess": "unsure",
        "model_score": 0.4863,
        "style_score": 0.359,
        "combined_score": 0.4608,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.4608,
        "style_metrics": {
          "word_count": 118,
          "sentence_count": 4,
          "sentence_length_spread": 0.5956367251120536,
          "type_token_ratio": 0.7033898305084746,
          "punctuation_density": 0.04021937842778794,
          "evenness": 0.2554540936099331,
          "repetition": 0.3276836158192091,
          "punctuation_simplicity": 0.6648385131017671,
          "style_score": 0.359
        },
        "text_length": 664,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
          "creator_id": "cap-after-c5-t1-a1-human-02",
          "guess": "unsure",
          "model_score": 0.4863,
          "style_score": 0.359,
          "combined_score": 0.4608,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.4608,
          "style_metrics": {
            "word_count": 118,
            "sentence_count": 4,
            "sentence_length_spread": 0.5956367251120536,
            "type_token_ratio": 0.7033898305084746,
            "punctuation_density": 0.04021937842778794,
            "evenness": 0.2554540936099331,
            "repetition": 0.3276836158192091,
            "punctuation_simplicity": 0.6648385131017671,
            "style_score": 0.359
          },
          "text_length": 664,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "fe95b565-7519-45ab-abb4-05d30ca347f5",
          "creator_id": "cap-after-c5-t1-a1-human-02",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 2: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-03",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.466562+00:00",
        "request_json": {
          "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
          "creator_id": "cap-after-c5-t1-a1-human-03"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "751",
          "X-Request-ID": "b28c08a9-0516-4619-939f-29a205ac2e68"
        },
        "request_id": "b28c08a9-0516-4619-939f-29a205ac2e68",
        "response_json": {
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
          "creator_id": "cap-after-c5-t1-a1-human-03",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.3532,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.027522935779816515,
            "punctuation_simplicity": 0.7706422018348624,
            "repetition": 0.37356321839080464,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "style_score": 0.2662,
            "type_token_ratio": 0.6758620689655173,
            "word_count": 145
          },
          "style_score": 0.2662,
          "text_length": 795,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.07351370807737112,
        "request_body_bytes": 872
      },
      "appeal": {
        "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
        "reasoning": "  Capstone review 3: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 3",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.920758+00:00",
          "request_json": {
            "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
            "reasoning": "  Capstone review 3: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "619839f3-8e71-4247-9819-0e3e371dd7d2"
          },
          "request_id": "619839f3-8e71-4247-9819-0e3e371dd7d2",
          "response_json": {
            "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
            "creator_id": "cap-after-c5-t1-a1-human-03",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 3: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0008462090045213699,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 3",
        "method": "GET",
        "path": "/content/9e914be4-a931-4a43-a6e2-1afe6b5fed70",
        "sent_at_utc": "2026-11-14T02:08:53.389137+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1010",
          "X-Request-ID": "ba44b1e3-a736-47a4-8287-8be62f116817"
        },
        "request_id": "ba44b1e3-a736-47a4-8287-8be62f116817",
        "response_json": {
          "appeals": [
            {
              "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
              "creator_id": "cap-after-c5-t1-a1-human-03",
              "event": "appeal",
              "reasoning": "  Capstone review 3: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
          "creator_id": "cap-after-c5-t1-a1-human-03",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.3532,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.027522935779816515,
            "punctuation_simplicity": 0.7706422018348624,
            "repetition": 0.37356321839080464,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "style_score": 0.2662,
            "type_token_ratio": 0.6758620689655173,
            "word_count": 145
          },
          "style_score": 0.2662,
          "text_length": 795,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0009266668930649757,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
        "creator_id": "cap-after-c5-t1-a1-human-03",
        "guess": "unsure",
        "model_score": 0.3532,
        "style_score": 0.2662,
        "combined_score": 0.3358,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.3358,
        "style_metrics": {
          "word_count": 145,
          "sentence_count": 4,
          "sentence_length_spread": 0.8882105351861661,
          "type_token_ratio": 0.6758620689655173,
          "punctuation_density": 0.027522935779816515,
          "evenness": 0.0,
          "repetition": 0.37356321839080464,
          "punctuation_simplicity": 0.7706422018348624,
          "style_score": 0.2662
        },
        "text_length": 795,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
          "creator_id": "cap-after-c5-t1-a1-human-03",
          "guess": "unsure",
          "model_score": 0.3532,
          "style_score": 0.2662,
          "combined_score": 0.3358,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.3358,
          "style_metrics": {
            "word_count": 145,
            "sentence_count": 4,
            "sentence_length_spread": 0.8882105351861661,
            "type_token_ratio": 0.6758620689655173,
            "punctuation_density": 0.027522935779816515,
            "evenness": 0.0,
            "repetition": 0.37356321839080464,
            "punctuation_simplicity": 0.7706422018348624,
            "style_score": 0.2662
          },
          "text_length": 795,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "9e914be4-a931-4a43-a6e2-1afe6b5fed70",
          "creator_id": "cap-after-c5-t1-a1-human-03",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 3: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-04",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.540089+00:00",
        "request_json": {
          "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
          "creator_id": "cap-after-c5-t1-a1-human-04"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "765",
          "X-Request-ID": "cd4376e8-2490-4aa3-bc6a-70f1dc961102"
        },
        "request_id": "cd4376e8-2490-4aa3-bc6a-70f1dc961102",
        "response_json": {
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
          "creator_id": "cap-after-c5-t1-a1-human-04",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4097,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.16602391043278608,
            "punctuation_density": 0.053691275167785234,
            "punctuation_simplicity": 0.5525727069351231,
            "repetition": 0.48148148148148145,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "style_score": 0.338,
            "type_token_ratio": 0.6111111111111112,
            "word_count": 108
          },
          "style_score": 0.338,
          "text_length": 552,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.06030512461438775,
        "request_body_bytes": 634
      },
      "appeal": {
        "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
        "reasoning": "  Capstone review 4: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 4",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.921610+00:00",
          "request_json": {
            "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
            "reasoning": "  Capstone review 4: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "622d2a79-d27d-402a-ba35-a0dd8ee7ddc2"
          },
          "request_id": "622d2a79-d27d-402a-ba35-a0dd8ee7ddc2",
          "response_json": {
            "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
            "creator_id": "cap-after-c5-t1-a1-human-04",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 4: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0008804588578641415,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 4",
        "method": "GET",
        "path": "/content/36583dba-5c2c-4d6c-a850-dd459c88ccc7",
        "sent_at_utc": "2026-11-14T02:08:53.390071+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1024",
          "X-Request-ID": "c6de065a-fd6e-4f67-a851-745c26803e1f"
        },
        "request_id": "c6de065a-fd6e-4f67-a851-745c26803e1f",
        "response_json": {
          "appeals": [
            {
              "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
              "creator_id": "cap-after-c5-t1-a1-human-04",
              "event": "appeal",
              "reasoning": "  Capstone review 4: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
          "creator_id": "cap-after-c5-t1-a1-human-04",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.4097,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.16602391043278608,
            "punctuation_density": 0.053691275167785234,
            "punctuation_simplicity": 0.5525727069351231,
            "repetition": 0.48148148148148145,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "style_score": 0.338,
            "type_token_ratio": 0.6111111111111112,
            "word_count": 108
          },
          "style_score": 0.338,
          "text_length": 552,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0008339998312294483,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
        "creator_id": "cap-after-c5-t1-a1-human-04",
        "guess": "unsure",
        "model_score": 0.4097,
        "style_score": 0.338,
        "combined_score": 0.3954,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.3954,
        "style_metrics": {
          "word_count": 108,
          "sentence_count": 7,
          "sentence_length_spread": 0.6671808716537712,
          "type_token_ratio": 0.6111111111111112,
          "punctuation_density": 0.053691275167785234,
          "evenness": 0.16602391043278608,
          "repetition": 0.48148148148148145,
          "punctuation_simplicity": 0.5525727069351231,
          "style_score": 0.338
        },
        "text_length": 552,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
          "creator_id": "cap-after-c5-t1-a1-human-04",
          "guess": "unsure",
          "model_score": 0.4097,
          "style_score": 0.338,
          "combined_score": 0.3954,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.3954,
          "style_metrics": {
            "word_count": 108,
            "sentence_count": 7,
            "sentence_length_spread": 0.6671808716537712,
            "type_token_ratio": 0.6111111111111112,
            "punctuation_density": 0.053691275167785234,
            "evenness": 0.16602391043278608,
            "repetition": 0.48148148148148145,
            "punctuation_simplicity": 0.5525727069351231,
            "style_score": 0.338
          },
          "text_length": 552,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "36583dba-5c2c-4d6c-a850-dd459c88ccc7",
          "creator_id": "cap-after-c5-t1-a1-human-04",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 4: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-05",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.600412+00:00",
        "request_json": {
          "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
          "creator_id": "cap-after-c5-t1-a1-human-05"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "749",
          "X-Request-ID": "4e3c584f-f85c-4ff1-8614-8f7684d0cdd4"
        },
        "request_id": "4e3c584f-f85c-4ff1-8614-8f7684d0cdd4",
        "response_json": {
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
          "creator_id": "cap-after-c5-t1-a1-human-05",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7577,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.04195804195804196,
            "punctuation_simplicity": 0.6503496503496503,
            "repetition": 0.29227053140096626,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "style_score": 0.2178,
            "type_token_ratio": 0.7246376811594203,
            "word_count": 69
          },
          "style_score": 0.2178,
          "text_length": 354,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.044942458625882864,
        "request_body_bytes": 411
      },
      "appeal": {
        "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
        "reasoning": "  Capstone review 5: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 5",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.922500+00:00",
          "request_json": {
            "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
            "reasoning": "  Capstone review 5: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "f9a111af-16cc-4cc5-8bc7-ceffe4eb3463"
          },
          "request_id": "f9a111af-16cc-4cc5-8bc7-ceffe4eb3463",
          "response_json": {
            "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
            "creator_id": "cap-after-c5-t1-a1-human-05",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 5: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0009015421383082867,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 5",
        "method": "GET",
        "path": "/content/19ce0fc5-ede6-4639-b9f2-1708831435b4",
        "sent_at_utc": "2026-11-14T02:08:53.390913+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1008",
          "X-Request-ID": "d04146bc-5daf-413e-9922-b93c6768b163"
        },
        "request_id": "d04146bc-5daf-413e-9922-b93c6768b163",
        "response_json": {
          "appeals": [
            {
              "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
              "creator_id": "cap-after-c5-t1-a1-human-05",
              "event": "appeal",
              "reasoning": "  Capstone review 5: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
          "creator_id": "cap-after-c5-t1-a1-human-05",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7577,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.0,
            "punctuation_density": 0.04195804195804196,
            "punctuation_simplicity": 0.6503496503496503,
            "repetition": 0.29227053140096626,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "style_score": 0.2178,
            "type_token_ratio": 0.7246376811594203,
            "word_count": 69
          },
          "style_score": 0.2178,
          "text_length": 354,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0008410420268774033,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
        "creator_id": "cap-after-c5-t1-a1-human-05",
        "guess": "unsure",
        "model_score": 0.7577,
        "style_score": 0.2178,
        "combined_score": 0.6497,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.6497,
        "style_metrics": {
          "word_count": 69,
          "sentence_count": 3,
          "sentence_length_spread": 0.8615573303015565,
          "type_token_ratio": 0.7246376811594203,
          "punctuation_density": 0.04195804195804196,
          "evenness": 0.0,
          "repetition": 0.29227053140096626,
          "punctuation_simplicity": 0.6503496503496503,
          "style_score": 0.2178
        },
        "text_length": 354,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
          "creator_id": "cap-after-c5-t1-a1-human-05",
          "guess": "unsure",
          "model_score": 0.7577,
          "style_score": 0.2178,
          "combined_score": 0.6497,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.6497,
          "style_metrics": {
            "word_count": 69,
            "sentence_count": 3,
            "sentence_length_spread": 0.8615573303015565,
            "type_token_ratio": 0.7246376811594203,
            "punctuation_density": 0.04195804195804196,
            "evenness": 0.0,
            "repetition": 0.29227053140096626,
            "punctuation_simplicity": 0.6503496503496503,
            "style_score": 0.2178
          },
          "text_length": 354,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "19ce0fc5-ede6-4639-b9f2-1708831435b4",
          "creator_id": "cap-after-c5-t1-a1-human-05",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 5: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-06",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.645371+00:00",
        "request_json": {
          "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
          "creator_id": "cap-after-c5-t1-a1-human-06"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "765",
          "X-Request-ID": "b9051cbd-2c65-485b-9e51-7f6b335ac2f5"
        },
        "request_id": "b9051cbd-2c65-485b-9e51-7f6b335ac2f5",
        "response_json": {
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
          "creator_id": "cap-after-c5-t1-a1-human-06",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5829,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.38795621995783924,
            "punctuation_density": 0.01937046004842615,
            "punctuation_simplicity": 0.8385794995964487,
            "repetition": 0.2640449438202247,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "style_score": 0.4409,
            "type_token_ratio": 0.7415730337078652,
            "word_count": 89
          },
          "style_score": 0.4409,
          "text_length": 501,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.048985375091433525,
        "request_body_bytes": 558
      },
      "appeal": {
        "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
        "reasoning": "  Capstone review 6: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 6",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.923410+00:00",
          "request_json": {
            "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
            "reasoning": "  Capstone review 6: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "6f7cba63-2e30-4bbc-96b4-60a787b0fae3"
          },
          "request_id": "6f7cba63-2e30-4bbc-96b4-60a787b0fae3",
          "response_json": {
            "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
            "creator_id": "cap-after-c5-t1-a1-human-06",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 6: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0008682496845722198,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 6",
        "method": "GET",
        "path": "/content/b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
        "sent_at_utc": "2026-11-14T02:08:53.391761+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1024",
          "X-Request-ID": "1f235cef-fa02-4923-8f2a-cdc3412c6fa8"
        },
        "request_id": "1f235cef-fa02-4923-8f2a-cdc3412c6fa8",
        "response_json": {
          "appeals": [
            {
              "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
              "creator_id": "cap-after-c5-t1-a1-human-06",
              "event": "appeal",
              "reasoning": "  Capstone review 6: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
          "creator_id": "cap-after-c5-t1-a1-human-06",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5829,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.38795621995783924,
            "punctuation_density": 0.01937046004842615,
            "punctuation_simplicity": 0.8385794995964487,
            "repetition": 0.2640449438202247,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "style_score": 0.4409,
            "type_token_ratio": 0.7415730337078652,
            "word_count": 89
          },
          "style_score": 0.4409,
          "text_length": 501,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0008089579641819,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
        "creator_id": "cap-after-c5-t1-a1-human-06",
        "guess": "unsure",
        "model_score": 0.5829,
        "style_score": 0.4409,
        "combined_score": 0.5545,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.5545,
        "style_metrics": {
          "word_count": 89,
          "sentence_count": 4,
          "sentence_length_spread": 0.48963502403372866,
          "type_token_ratio": 0.7415730337078652,
          "punctuation_density": 0.01937046004842615,
          "evenness": 0.38795621995783924,
          "repetition": 0.2640449438202247,
          "punctuation_simplicity": 0.8385794995964487,
          "style_score": 0.4409
        },
        "text_length": 501,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
          "creator_id": "cap-after-c5-t1-a1-human-06",
          "guess": "unsure",
          "model_score": 0.5829,
          "style_score": 0.4409,
          "combined_score": 0.5545,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.5545,
          "style_metrics": {
            "word_count": 89,
            "sentence_count": 4,
            "sentence_length_spread": 0.48963502403372866,
            "type_token_ratio": 0.7415730337078652,
            "punctuation_density": 0.01937046004842615,
            "evenness": 0.38795621995783924,
            "repetition": 0.2640449438202247,
            "punctuation_simplicity": 0.8385794995964487,
            "style_score": 0.4409
          },
          "text_length": 501,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "b2f84a7b-2a4e-40d6-ad0a-eda52646c27a",
          "creator_id": "cap-after-c5-t1-a1-human-06",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 6: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-07",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.694367+00:00",
        "request_json": {
          "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
          "creator_id": "cap-after-c5-t1-a1-human-07"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "751",
          "X-Request-ID": "c26afe83-21e7-409b-bb49-582bb91a6a9a"
        },
        "request_id": "c26afe83-21e7-409b-bb49-582bb91a6a9a",
        "response_json": {
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
          "creator_id": "cap-after-c5-t1-a1-human-07",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5745,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.035343035343035345,
            "punctuation_simplicity": 0.7054747054747055,
            "repetition": 0.3790560471976401,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "style_score": 0.5048,
            "type_token_ratio": 0.672566371681416,
            "word_count": 113
          },
          "style_score": 0.5048,
          "text_length": 592,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.05852487497031689,
        "request_body_bytes": 669
      },
      "appeal": {
        "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
        "reasoning": "  Capstone review 7: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 7",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.924284+00:00",
          "request_json": {
            "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
            "reasoning": "  Capstone review 7: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "266e2c72-5630-4926-b64a-03ce4269c4da"
          },
          "request_id": "266e2c72-5630-4926-b64a-03ce4269c4da",
          "response_json": {
            "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
            "creator_id": "cap-after-c5-t1-a1-human-07",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 7: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0008515832014381886,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 7",
        "method": "GET",
        "path": "/content/1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
        "sent_at_utc": "2026-11-14T02:08:53.392577+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1010",
          "X-Request-ID": "e4bb27f6-9655-4b08-87f0-07458460fadf"
        },
        "request_id": "e4bb27f6-9655-4b08-87f0-07458460fadf",
        "response_json": {
          "appeals": [
            {
              "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
              "creator_id": "cap-after-c5-t1-a1-human-07",
              "event": "appeal",
              "reasoning": "  Capstone review 7: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
          "creator_id": "cap-after-c5-t1-a1-human-07",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5745,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.5,
            "punctuation_density": 0.035343035343035345,
            "punctuation_simplicity": 0.7054747054747055,
            "repetition": 0.3790560471976401,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "style_score": 0.5048,
            "type_token_ratio": 0.672566371681416,
            "word_count": 113
          },
          "style_score": 0.5048,
          "text_length": 592,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0008032917976379395,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
        "creator_id": "cap-after-c5-t1-a1-human-07",
        "guess": "unsure",
        "model_score": 0.5745,
        "style_score": 0.5048,
        "combined_score": 0.5606,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.5606,
        "style_metrics": {
          "word_count": 113,
          "sentence_count": 2,
          "sentence_length_spread": 0.008849557522123894,
          "type_token_ratio": 0.672566371681416,
          "punctuation_density": 0.035343035343035345,
          "evenness": 0.5,
          "repetition": 0.3790560471976401,
          "punctuation_simplicity": 0.7054747054747055,
          "style_score": 0.5048
        },
        "text_length": 592,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
          "creator_id": "cap-after-c5-t1-a1-human-07",
          "guess": "unsure",
          "model_score": 0.5745,
          "style_score": 0.5048,
          "combined_score": 0.5606,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.5606,
          "style_metrics": {
            "word_count": 113,
            "sentence_count": 2,
            "sentence_length_spread": 0.008849557522123894,
            "type_token_ratio": 0.672566371681416,
            "punctuation_density": 0.035343035343035345,
            "evenness": 0.5,
            "repetition": 0.3790560471976401,
            "punctuation_simplicity": 0.7054747054747055,
            "style_score": 0.5048
          },
          "text_length": 592,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "1a143a7f-1df8-4003-9ae0-a6e68faf38e6",
          "creator_id": "cap-after-c5-t1-a1-human-07",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 7: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-08",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.752900+00:00",
        "request_json": {
          "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
          "creator_id": "cap-after-c5-t1-a1-human-08"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "764",
          "X-Request-ID": "9d2745c1-d57d-4db5-a953-2a70cf0d21f3"
        },
        "request_id": "9d2745c1-d57d-4db5-a953-2a70cf0d21f3",
        "response_json": {
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
          "creator_id": "cap-after-c5-t1-a1-human-08",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5825,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.420697370644045,
            "punctuation_density": 0.03232323232323232,
            "punctuation_simplicity": 0.7306397306397306,
            "repetition": 0.3473520249221185,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "style_score": 0.4607,
            "type_token_ratio": 0.6915887850467289,
            "word_count": 107
          },
          "style_score": 0.4607,
          "text_length": 598,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.054337083362042904,
        "request_body_bytes": 670
      },
      "appeal": {
        "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
        "reasoning": "  Capstone review 8: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 8",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.925143+00:00",
          "request_json": {
            "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
            "reasoning": "  Capstone review 8: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "108420b3-11e8-44b1-85a4-ca2f680719a2"
          },
          "request_id": "108420b3-11e8-44b1-85a4-ca2f680719a2",
          "response_json": {
            "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
            "creator_id": "cap-after-c5-t1-a1-human-08",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 8: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0008689998649060726,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 8",
        "method": "GET",
        "path": "/content/cad6d0f1-aca6-4848-adda-99d7438e59a0",
        "sent_at_utc": "2026-11-14T02:08:53.393387+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1023",
          "X-Request-ID": "b1fdae64-92fe-40ed-9009-1fcda47bcc5a"
        },
        "request_id": "b1fdae64-92fe-40ed-9009-1fcda47bcc5a",
        "response_json": {
          "appeals": [
            {
              "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
              "creator_id": "cap-after-c5-t1-a1-human-08",
              "event": "appeal",
              "reasoning": "  Capstone review 8: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
          "creator_id": "cap-after-c5-t1-a1-human-08",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.5825,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.420697370644045,
            "punctuation_density": 0.03232323232323232,
            "punctuation_simplicity": 0.7306397306397306,
            "repetition": 0.3473520249221185,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "style_score": 0.4607,
            "type_token_ratio": 0.6915887850467289,
            "word_count": 107
          },
          "style_score": 0.4607,
          "text_length": 598,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0007959576323628426,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
        "creator_id": "cap-after-c5-t1-a1-human-08",
        "guess": "unsure",
        "model_score": 0.5825,
        "style_score": 0.4607,
        "combined_score": 0.5581,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.5581,
        "style_metrics": {
          "word_count": 107,
          "sentence_count": 4,
          "sentence_length_spread": 0.46344210348476406,
          "type_token_ratio": 0.6915887850467289,
          "punctuation_density": 0.03232323232323232,
          "evenness": 0.420697370644045,
          "repetition": 0.3473520249221185,
          "punctuation_simplicity": 0.7306397306397306,
          "style_score": 0.4607
        },
        "text_length": 598,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
          "creator_id": "cap-after-c5-t1-a1-human-08",
          "guess": "unsure",
          "model_score": 0.5825,
          "style_score": 0.4607,
          "combined_score": 0.5581,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.5581,
          "style_metrics": {
            "word_count": 107,
            "sentence_count": 4,
            "sentence_length_spread": 0.46344210348476406,
            "type_token_ratio": 0.6915887850467289,
            "punctuation_density": 0.03232323232323232,
            "evenness": 0.420697370644045,
            "repetition": 0.3473520249221185,
            "punctuation_simplicity": 0.7306397306397306,
            "style_score": 0.4607
          },
          "text_length": 598,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "cad6d0f1-aca6-4848-adda-99d7438e59a0",
          "creator_id": "cap-after-c5-t1-a1-human-08",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 8: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-09",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.807251+00:00",
        "request_json": {
          "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
          "creator_id": "cap-after-c5-t1-a1-human-09"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "737",
          "X-Request-ID": "5f07d745-db79-461b-9aad-603dc602045f"
        },
        "request_id": "5f07d745-db79-461b-9aad-603dc602045f",
        "response_json": {
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
          "creator_id": "cap-after-c5-t1-a1-human-09",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7648,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.26494047860054226,
            "punctuation_density": 0.018823529411764704,
            "punctuation_simplicity": 0.8431372549019608,
            "repetition": 0.6,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "style_score": 0.4811,
            "type_token_ratio": 0.54,
            "word_count": 100
          },
          "style_score": 0.4811,
          "text_length": 524,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.049674250185489655,
        "request_body_bytes": 581
      },
      "appeal": {
        "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
        "reasoning": "  Capstone review 9: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 9",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.926018+00:00",
          "request_json": {
            "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
            "reasoning": "  Capstone review 9: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "319",
            "X-Request-ID": "d0170ca9-8816-4915-b3fb-fc173dddb202"
          },
          "request_id": "d0170ca9-8816-4915-b3fb-fc173dddb202",
          "response_json": {
            "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
            "creator_id": "cap-after-c5-t1-a1-human-09",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 9: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0007966253906488419,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 9",
        "method": "GET",
        "path": "/content/5e4e5f33-302e-4497-a131-3a334aa574b2",
        "sent_at_utc": "2026-11-14T02:08:53.394188+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "996",
          "X-Request-ID": "dfdcd307-6216-4876-bfef-7d18ef430bd1"
        },
        "request_id": "dfdcd307-6216-4876-bfef-7d18ef430bd1",
        "response_json": {
          "appeals": [
            {
              "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
              "creator_id": "cap-after-c5-t1-a1-human-09",
              "event": "appeal",
              "reasoning": "  Capstone review 9: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
          "creator_id": "cap-after-c5-t1-a1-human-09",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.7648,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.26494047860054226,
            "punctuation_density": 0.018823529411764704,
            "punctuation_simplicity": 0.8431372549019608,
            "repetition": 0.6,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "style_score": 0.4811,
            "type_token_ratio": 0.54,
            "word_count": 100
          },
          "style_score": 0.4811,
          "text_length": 524,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0007268749177455902,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
        "creator_id": "cap-after-c5-t1-a1-human-09",
        "guess": "unsure",
        "model_score": 0.7648,
        "style_score": 0.4811,
        "combined_score": 0.7081,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.7081,
        "style_metrics": {
          "word_count": 100,
          "sentence_count": 3,
          "sentence_length_spread": 0.5880476171195662,
          "type_token_ratio": 0.54,
          "punctuation_density": 0.018823529411764704,
          "evenness": 0.26494047860054226,
          "repetition": 0.6,
          "punctuation_simplicity": 0.8431372549019608,
          "style_score": 0.4811
        },
        "text_length": 524,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
          "creator_id": "cap-after-c5-t1-a1-human-09",
          "guess": "unsure",
          "model_score": 0.7648,
          "style_score": 0.4811,
          "combined_score": 0.7081,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.7081,
          "style_metrics": {
            "word_count": 100,
            "sentence_count": 3,
            "sentence_length_spread": 0.5880476171195662,
            "type_token_ratio": 0.54,
            "punctuation_density": 0.018823529411764704,
            "evenness": 0.26494047860054226,
            "repetition": 0.6,
            "punctuation_simplicity": 0.8431372549019608,
            "style_score": 0.4811
          },
          "text_length": 524,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "5e4e5f33-302e-4497-a131-3a334aa574b2",
          "creator_id": "cap-after-c5-t1-a1-human-09",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 9: please consider my drafts.  "
        }
      ],
      "passed": true
    },
    {
      "submission": {
        "name": "appeal setup human-10",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:08:52.856934+00:00",
        "request_json": {
          "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
          "creator_id": "cap-after-c5-t1-a1-human-10"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "762",
          "X-Request-ID": "c6de33cd-ad44-4928-958d-917f6433c51e"
        },
        "request_id": "c6de33cd-ad44-4928-958d-917f6433c51e",
        "response_json": {
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
          "creator_id": "cap-after-c5-t1-a1-human-10",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.566,
          "status": "decided",
          "style_metrics": {
            "evenness": 0.4729379744287563,
            "punctuation_density": 0.047058823529411764,
            "punctuation_simplicity": 0.607843137254902,
            "repetition": 0.3842975206611571,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "style_score": 0.4733,
            "type_token_ratio": 0.6694214876033058,
            "word_count": 121
          },
          "style_score": 0.4733,
          "text_length": 626,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.06142983306199312,
        "request_body_bytes": 683
      },
      "appeal": {
        "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
        "reasoning": "  Capstone review 10: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 10",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:08:52.926821+00:00",
          "request_json": {
            "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
            "reasoning": "  Capstone review 10: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:08:52 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "e74e8821-c233-4415-9782-c35d72e4dd2a"
          },
          "request_id": "e74e8821-c233-4415-9782-c35d72e4dd2a",
          "response_json": {
            "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
            "creator_id": "cap-after-c5-t1-a1-human-10",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 10: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:52+00:00"
          },
          "elapsed_seconds": 0.0008381670340895653,
          "request_body_bytes": 121
        }
      },
      "lookup": {
        "name": "persisted lookup 10",
        "method": "GET",
        "path": "/content/c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
        "sent_at_utc": "2026-11-14T02:08:53.394920+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1022",
          "X-Request-ID": "61b83765-a721-4790-bc50-449030aaeaf4"
        },
        "request_id": "61b83765-a721-4790-bc50-449030aaeaf4",
        "response_json": {
          "appeals": [
            {
              "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
              "creator_id": "cap-after-c5-t1-a1-human-10",
              "event": "appeal",
              "reasoning": "  Capstone review 10: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:08:52+00:00"
            }
          ],
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
          "creator_id": "cap-after-c5-t1-a1-human-10",
          "detector_model": "gpt2",
          "guess": "unsure",
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "model_score": 0.566,
          "status": "under_review",
          "style_metrics": {
            "evenness": 0.4729379744287563,
            "punctuation_density": 0.047058823529411764,
            "punctuation_simplicity": 0.607843137254902,
            "repetition": 0.3842975206611571,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "style_score": 0.4733,
            "type_token_ratio": 0.6694214876033058,
            "word_count": 121
          },
          "style_score": 0.4733,
          "text_length": 626,
          "timestamp": "2026-11-14T02:08:52+00:00"
        },
        "elapsed_seconds": 0.0009633330628275871,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:08:52+00:00",
        "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
        "creator_id": "cap-after-c5-t1-a1-human-10",
        "guess": "unsure",
        "model_score": 0.566,
        "style_score": 0.4733,
        "combined_score": 0.5475,
        "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
        "status": "decided",
        "confidence": 0.5475,
        "style_metrics": {
          "word_count": 121,
          "sentence_count": 4,
          "sentence_length_spread": 0.421649620456995,
          "type_token_ratio": 0.6694214876033058,
          "punctuation_density": 0.047058823529411764,
          "evenness": 0.4729379744287563,
          "repetition": 0.3842975206611571,
          "punctuation_simplicity": 0.607843137254902,
          "style_score": 0.4733
        },
        "text_length": 626,
        "detector_model": "gpt2"
      },
      "history": [
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
          "creator_id": "cap-after-c5-t1-a1-human-10",
          "guess": "unsure",
          "model_score": 0.566,
          "style_score": 0.4733,
          "combined_score": 0.5475,
          "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
          "status": "decided",
          "confidence": 0.5475,
          "style_metrics": {
            "word_count": 121,
            "sentence_count": 4,
            "sentence_length_spread": 0.421649620456995,
            "type_token_ratio": 0.6694214876033058,
            "punctuation_density": 0.047058823529411764,
            "evenness": 0.4729379744287563,
            "repetition": 0.3842975206611571,
            "punctuation_simplicity": 0.607843137254902,
            "style_score": 0.4733
          },
          "text_length": 626,
          "detector_model": "gpt2"
        },
        {
          "timestamp": "2026-11-14T02:08:52+00:00",
          "content_id": "c9973dcf-0fdd-4c0f-967e-ad6ec63466f5",
          "creator_id": "cap-after-c5-t1-a1-human-10",
          "event": "appeal",
          "status": "under_review",
          "reasoning": "  Capstone review 10: please consider my drafts.  "
        }
      ],
      "passed": true
    }
  ],
  "unknown_id_response": {
    "name": "unknown appeal after restart",
    "method": "POST",
    "path": "/appeal",
    "sent_at_utc": "2026-11-14T02:08:53.395895+00:00",
    "request_json": {
      "content_id": "00000000-0000-4000-8000-000000000099",
      "reasoning": "  Capstone review 99: please consider my drafts.  "
    },
    "status_code": 404,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "85",
      "X-Request-ID": "931aa163-57b6-4d05-b4ac-9126751ea9eb"
    },
    "request_id": "931aa163-57b6-4d05-b4ac-9126751ea9eb",
    "response_json": {
      "error": "content_not_found",
      "message": "No submission exists with this content_id."
    },
    "elapsed_seconds": 0.000922083854675293,
    "request_body_bytes": 121
  },
  "unknown_id_passed": true,
  "original_audit_bytes_sha256": "c327b1670009b788df61693dfffdd839c0d5516b8c77fdf1b76417d742b0b03d",
  "original_audit_bytes_remain_prefix": true,
  "successful_events_unchanged_after_restart": true,
  "restart_health": {
    "detector_loaded": false,
    "detector_model": "gpt2",
    "log_entries": 20,
    "ok": true,
    "rate_limiting": true
  },
  "final_health": {
    "name": "health after appeals/lookups",
    "method": "GET",
    "path": "/health",
    "sent_at_utc": "2026-11-14T02:08:53.396823+00:00",
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:08:53 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "98",
      "X-Request-ID": "cdf275b0-8eca-4d43-a686-938f7bbe51e0"
    },
    "request_id": "cdf275b0-8eca-4d43-a686-938f7bbe51e0",
    "response_json": {
      "detector_loaded": false,
      "detector_model": "gpt2",
      "log_entries": 21,
      "ok": true,
      "rate_limiting": true
    },
    "elapsed_seconds": 0.0007252497598528862,
    "request_body_bytes": 0
  },
  "detector_unloaded_after_lookups": true,
  "audit_parse_errors": [],
  "quota_window_valid": true,
  "persistent_appeal_count": 10,
  "http_passed": true,
  "summary": "10/10 persistent appeals; unknown404=True; model unloaded=True",
  "trial": 1,
  "attempt": 1,
  "criterion": 5,
  "evidence_directory": "results/capstone/after/c5_trial1_attempt1",
  "companion": {
    "required": true,
    "kind": "mocked isolated invocation check; not real inference",
    "command": [
      "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/.venv/bin/python",
      "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/scripts/capstone_call_counts.py",
      "--criterion",
      "5",
      "--trial",
      "1"
    ],
    "returncode": 0,
    "stderr": "",
    "result": {
      "criterion": 5,
      "trial": 1,
      "kind": "mocked isolated detector invocation check",
      "real_model_loaded": false,
      "conditions": [],
      "submission_detector_calls": 10,
      "setup": [
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "30b55189-0f8a-495f-96e1-072db78bf484",
            "creator_id": "mocked-c5-1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5518,
            "confidence": 0.5518,
            "content_id": "471f5e1f-a9cf-4bd7-a22b-56c2523f70a7",
            "creator_id": "mocked-c5-2",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.2554540936099331,
              "punctuation_density": 0.04021937842778794,
              "punctuation_simplicity": 0.6648385131017671,
              "repetition": 0.3276836158192091,
              "sentence_count": 4,
              "sentence_length_spread": 0.5956367251120536,
              "style_score": 0.359,
              "type_token_ratio": 0.7033898305084746,
              "word_count": 118
            },
            "style_score": 0.359,
            "text_length": 664,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5332,
            "confidence": 0.5332,
            "content_id": "4895993b-3a94-4721-9e34-5e29031fc91e",
            "creator_id": "mocked-c5-3",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.0,
              "punctuation_density": 0.027522935779816515,
              "punctuation_simplicity": 0.7706422018348624,
              "repetition": 0.37356321839080464,
              "sentence_count": 4,
              "sentence_length_spread": 0.8882105351861661,
              "style_score": 0.2662,
              "type_token_ratio": 0.6758620689655173,
              "word_count": 145
            },
            "style_score": 0.2662,
            "text_length": 795,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5476,
            "confidence": 0.5476,
            "content_id": "6624571b-da19-48dd-b2c0-5ab95432f188",
            "creator_id": "mocked-c5-4",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.16602391043278608,
              "punctuation_density": 0.053691275167785234,
              "punctuation_simplicity": 0.5525727069351231,
              "repetition": 0.48148148148148145,
              "sentence_count": 7,
              "sentence_length_spread": 0.6671808716537712,
              "style_score": 0.338,
              "type_token_ratio": 0.6111111111111112,
              "word_count": 108
            },
            "style_score": 0.338,
            "text_length": 552,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5236,
            "confidence": 0.5236,
            "content_id": "4ec197b3-4ff6-4dc4-b7bc-7d73b6c94446",
            "creator_id": "mocked-c5-5",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.0,
              "punctuation_density": 0.04195804195804196,
              "punctuation_simplicity": 0.6503496503496503,
              "repetition": 0.29227053140096626,
              "sentence_count": 3,
              "sentence_length_spread": 0.8615573303015565,
              "style_score": 0.2178,
              "type_token_ratio": 0.7246376811594203,
              "word_count": 69
            },
            "style_score": 0.2178,
            "text_length": 354,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5682,
            "confidence": 0.5682,
            "content_id": "e1b4cf3e-8764-4328-b386-350ebcfd669e",
            "creator_id": "mocked-c5-6",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.38795621995783924,
              "punctuation_density": 0.01937046004842615,
              "punctuation_simplicity": 0.8385794995964487,
              "repetition": 0.2640449438202247,
              "sentence_count": 4,
              "sentence_length_spread": 0.48963502403372866,
              "style_score": 0.4409,
              "type_token_ratio": 0.7415730337078652,
              "word_count": 89
            },
            "style_score": 0.4409,
            "text_length": 501,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.581,
            "confidence": 0.581,
            "content_id": "c7bfc6cd-2849-4e6f-92be-487decd4a063",
            "creator_id": "mocked-c5-7",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.035343035343035345,
              "punctuation_simplicity": 0.7054747054747055,
              "repetition": 0.3790560471976401,
              "sentence_count": 2,
              "sentence_length_spread": 0.008849557522123894,
              "style_score": 0.5048,
              "type_token_ratio": 0.672566371681416,
              "word_count": 113
            },
            "style_score": 0.5048,
            "text_length": 592,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5721,
            "confidence": 0.5721,
            "content_id": "5b96ba96-bfd8-4bdb-977a-9ecaaefc66f4",
            "creator_id": "mocked-c5-8",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.420697370644045,
              "punctuation_density": 0.03232323232323232,
              "punctuation_simplicity": 0.7306397306397306,
              "repetition": 0.3473520249221185,
              "sentence_count": 4,
              "sentence_length_spread": 0.46344210348476406,
              "style_score": 0.4607,
              "type_token_ratio": 0.6915887850467289,
              "word_count": 107
            },
            "style_score": 0.4607,
            "text_length": 598,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5762,
            "confidence": 0.5762,
            "content_id": "8b2efeef-421a-4baa-ab11-5d1b35d9188e",
            "creator_id": "mocked-c5-9",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.26494047860054226,
              "punctuation_density": 0.018823529411764704,
              "punctuation_simplicity": 0.8431372549019608,
              "repetition": 0.6,
              "sentence_count": 3,
              "sentence_length_spread": 0.5880476171195662,
              "style_score": 0.4811,
              "type_token_ratio": 0.54,
              "word_count": 100
            },
            "style_score": 0.4811,
            "text_length": 524,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5747,
            "confidence": 0.5747,
            "content_id": "d64d3380-27f7-4ef1-9440-84cf9412203e",
            "creator_id": "mocked-c5-10",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "decided",
            "style_metrics": {
              "evenness": 0.4729379744287563,
              "punctuation_density": 0.047058823529411764,
              "punctuation_simplicity": 0.607843137254902,
              "repetition": 0.3842975206611571,
              "sentence_count": 4,
              "sentence_length_spread": 0.421649620456995,
              "style_score": 0.4733,
              "type_token_ratio": 0.6694214876033058,
              "word_count": 121
            },
            "style_score": 0.4733,
            "text_length": 626,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        }
      ],
      "appeals": [
        {
          "status_code": 200,
          "response_json": {
            "content_id": "30b55189-0f8a-495f-96e1-072db78bf484",
            "creator_id": "mocked-c5-1",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 1: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "471f5e1f-a9cf-4bd7-a22b-56c2523f70a7",
            "creator_id": "mocked-c5-2",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 2: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "4895993b-3a94-4721-9e34-5e29031fc91e",
            "creator_id": "mocked-c5-3",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 3: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "6624571b-da19-48dd-b2c0-5ab95432f188",
            "creator_id": "mocked-c5-4",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 4: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "4ec197b3-4ff6-4dc4-b7bc-7d73b6c94446",
            "creator_id": "mocked-c5-5",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 5: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "e1b4cf3e-8764-4328-b386-350ebcfd669e",
            "creator_id": "mocked-c5-6",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 6: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "c7bfc6cd-2849-4e6f-92be-487decd4a063",
            "creator_id": "mocked-c5-7",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 7: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "5b96ba96-bfd8-4bdb-977a-9ecaaefc66f4",
            "creator_id": "mocked-c5-8",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 8: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "8b2efeef-421a-4baa-ab11-5d1b35d9188e",
            "creator_id": "mocked-c5-9",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 9: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "d64d3380-27f7-4ef1-9440-84cf9412203e",
            "creator_id": "mocked-c5-10",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 10: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        }
      ],
      "lookups": [
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "30b55189-0f8a-495f-96e1-072db78bf484",
                "creator_id": "mocked-c5-1",
                "event": "appeal",
                "reasoning": "  Capstone review 1: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "30b55189-0f8a-495f-96e1-072db78bf484",
            "creator_id": "mocked-c5-1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "471f5e1f-a9cf-4bd7-a22b-56c2523f70a7",
                "creator_id": "mocked-c5-2",
                "event": "appeal",
                "reasoning": "  Capstone review 2: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5518,
            "confidence": 0.5518,
            "content_id": "471f5e1f-a9cf-4bd7-a22b-56c2523f70a7",
            "creator_id": "mocked-c5-2",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.2554540936099331,
              "punctuation_density": 0.04021937842778794,
              "punctuation_simplicity": 0.6648385131017671,
              "repetition": 0.3276836158192091,
              "sentence_count": 4,
              "sentence_length_spread": 0.5956367251120536,
              "style_score": 0.359,
              "type_token_ratio": 0.7033898305084746,
              "word_count": 118
            },
            "style_score": 0.359,
            "text_length": 664,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "4895993b-3a94-4721-9e34-5e29031fc91e",
                "creator_id": "mocked-c5-3",
                "event": "appeal",
                "reasoning": "  Capstone review 3: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5332,
            "confidence": 0.5332,
            "content_id": "4895993b-3a94-4721-9e34-5e29031fc91e",
            "creator_id": "mocked-c5-3",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.0,
              "punctuation_density": 0.027522935779816515,
              "punctuation_simplicity": 0.7706422018348624,
              "repetition": 0.37356321839080464,
              "sentence_count": 4,
              "sentence_length_spread": 0.8882105351861661,
              "style_score": 0.2662,
              "type_token_ratio": 0.6758620689655173,
              "word_count": 145
            },
            "style_score": 0.2662,
            "text_length": 795,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "6624571b-da19-48dd-b2c0-5ab95432f188",
                "creator_id": "mocked-c5-4",
                "event": "appeal",
                "reasoning": "  Capstone review 4: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5476,
            "confidence": 0.5476,
            "content_id": "6624571b-da19-48dd-b2c0-5ab95432f188",
            "creator_id": "mocked-c5-4",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.16602391043278608,
              "punctuation_density": 0.053691275167785234,
              "punctuation_simplicity": 0.5525727069351231,
              "repetition": 0.48148148148148145,
              "sentence_count": 7,
              "sentence_length_spread": 0.6671808716537712,
              "style_score": 0.338,
              "type_token_ratio": 0.6111111111111112,
              "word_count": 108
            },
            "style_score": 0.338,
            "text_length": 552,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "4ec197b3-4ff6-4dc4-b7bc-7d73b6c94446",
                "creator_id": "mocked-c5-5",
                "event": "appeal",
                "reasoning": "  Capstone review 5: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5236,
            "confidence": 0.5236,
            "content_id": "4ec197b3-4ff6-4dc4-b7bc-7d73b6c94446",
            "creator_id": "mocked-c5-5",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.0,
              "punctuation_density": 0.04195804195804196,
              "punctuation_simplicity": 0.6503496503496503,
              "repetition": 0.29227053140096626,
              "sentence_count": 3,
              "sentence_length_spread": 0.8615573303015565,
              "style_score": 0.2178,
              "type_token_ratio": 0.7246376811594203,
              "word_count": 69
            },
            "style_score": 0.2178,
            "text_length": 354,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "e1b4cf3e-8764-4328-b386-350ebcfd669e",
                "creator_id": "mocked-c5-6",
                "event": "appeal",
                "reasoning": "  Capstone review 6: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5682,
            "confidence": 0.5682,
            "content_id": "e1b4cf3e-8764-4328-b386-350ebcfd669e",
            "creator_id": "mocked-c5-6",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.38795621995783924,
              "punctuation_density": 0.01937046004842615,
              "punctuation_simplicity": 0.8385794995964487,
              "repetition": 0.2640449438202247,
              "sentence_count": 4,
              "sentence_length_spread": 0.48963502403372866,
              "style_score": 0.4409,
              "type_token_ratio": 0.7415730337078652,
              "word_count": 89
            },
            "style_score": 0.4409,
            "text_length": 501,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "c7bfc6cd-2849-4e6f-92be-487decd4a063",
                "creator_id": "mocked-c5-7",
                "event": "appeal",
                "reasoning": "  Capstone review 7: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.581,
            "confidence": 0.581,
            "content_id": "c7bfc6cd-2849-4e6f-92be-487decd4a063",
            "creator_id": "mocked-c5-7",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.035343035343035345,
              "punctuation_simplicity": 0.7054747054747055,
              "repetition": 0.3790560471976401,
              "sentence_count": 2,
              "sentence_length_spread": 0.008849557522123894,
              "style_score": 0.5048,
              "type_token_ratio": 0.672566371681416,
              "word_count": 113
            },
            "style_score": 0.5048,
            "text_length": 592,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "5b96ba96-bfd8-4bdb-977a-9ecaaefc66f4",
                "creator_id": "mocked-c5-8",
                "event": "appeal",
                "reasoning": "  Capstone review 8: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5721,
            "confidence": 0.5721,
            "content_id": "5b96ba96-bfd8-4bdb-977a-9ecaaefc66f4",
            "creator_id": "mocked-c5-8",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.420697370644045,
              "punctuation_density": 0.03232323232323232,
              "punctuation_simplicity": 0.7306397306397306,
              "repetition": 0.3473520249221185,
              "sentence_count": 4,
              "sentence_length_spread": 0.46344210348476406,
              "style_score": 0.4607,
              "type_token_ratio": 0.6915887850467289,
              "word_count": 107
            },
            "style_score": 0.4607,
            "text_length": 598,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "8b2efeef-421a-4baa-ab11-5d1b35d9188e",
                "creator_id": "mocked-c5-9",
                "event": "appeal",
                "reasoning": "  Capstone review 9: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5762,
            "confidence": 0.5762,
            "content_id": "8b2efeef-421a-4baa-ab11-5d1b35d9188e",
            "creator_id": "mocked-c5-9",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.26494047860054226,
              "punctuation_density": 0.018823529411764704,
              "punctuation_simplicity": 0.8431372549019608,
              "repetition": 0.6,
              "sentence_count": 3,
              "sentence_length_spread": 0.5880476171195662,
              "style_score": 0.4811,
              "type_token_ratio": 0.54,
              "word_count": 100
            },
            "style_score": 0.4811,
            "text_length": 524,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "d64d3380-27f7-4ef1-9440-84cf9412203e",
                "creator_id": "mocked-c5-10",
                "event": "appeal",
                "reasoning": "  Capstone review 10: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5747,
            "confidence": 0.5747,
            "content_id": "d64d3380-27f7-4ef1-9440-84cf9412203e",
            "creator_id": "mocked-c5-10",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.4729379744287563,
              "punctuation_density": 0.047058823529411764,
              "punctuation_simplicity": 0.607843137254902,
              "repetition": 0.3842975206611571,
              "sentence_count": 4,
              "sentence_length_spread": 0.421649620456995,
              "style_score": 0.4733,
              "type_token_ratio": 0.6694214876033058,
              "word_count": 121
            },
            "style_score": 0.4733,
            "text_length": 626,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        }
      ],
      "unknown": {
        "status_code": 404,
        "response_json": {
          "error": "content_not_found",
          "message": "No submission exists with this content_id."
        }
      },
      "appeal_lookup_detector_calls": 0,
      "original_unchanged": true,
      "restarted": {
        "detector_calls": 0,
        "detector_loaded": false,
        "statuses": [
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200,
          200
        ],
        "items": [
          {
            "appeals": [
              {
                "content_id": "30b55189-0f8a-495f-96e1-072db78bf484",
                "creator_id": "mocked-c5-1",
                "event": "appeal",
                "reasoning": "  Capstone review 1: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "30b55189-0f8a-495f-96e1-072db78bf484",
            "creator_id": "mocked-c5-1",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.016286644951140065,
              "punctuation_simplicity": 0.8642779587404994,
              "repetition": 0.34976525821596255,
              "sentence_count": 2,
              "sentence_length_spread": 0.352112676056338,
              "style_score": 0.5278,
              "type_token_ratio": 0.6901408450704225,
              "word_count": 71
            },
            "style_score": 0.5278,
            "text_length": 377,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "471f5e1f-a9cf-4bd7-a22b-56c2523f70a7",
                "creator_id": "mocked-c5-2",
                "event": "appeal",
                "reasoning": "  Capstone review 2: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5518,
            "confidence": 0.5518,
            "content_id": "471f5e1f-a9cf-4bd7-a22b-56c2523f70a7",
            "creator_id": "mocked-c5-2",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.2554540936099331,
              "punctuation_density": 0.04021937842778794,
              "punctuation_simplicity": 0.6648385131017671,
              "repetition": 0.3276836158192091,
              "sentence_count": 4,
              "sentence_length_spread": 0.5956367251120536,
              "style_score": 0.359,
              "type_token_ratio": 0.7033898305084746,
              "word_count": 118
            },
            "style_score": 0.359,
            "text_length": 664,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "4895993b-3a94-4721-9e34-5e29031fc91e",
                "creator_id": "mocked-c5-3",
                "event": "appeal",
                "reasoning": "  Capstone review 3: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5332,
            "confidence": 0.5332,
            "content_id": "4895993b-3a94-4721-9e34-5e29031fc91e",
            "creator_id": "mocked-c5-3",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.0,
              "punctuation_density": 0.027522935779816515,
              "punctuation_simplicity": 0.7706422018348624,
              "repetition": 0.37356321839080464,
              "sentence_count": 4,
              "sentence_length_spread": 0.8882105351861661,
              "style_score": 0.2662,
              "type_token_ratio": 0.6758620689655173,
              "word_count": 145
            },
            "style_score": 0.2662,
            "text_length": 795,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "6624571b-da19-48dd-b2c0-5ab95432f188",
                "creator_id": "mocked-c5-4",
                "event": "appeal",
                "reasoning": "  Capstone review 4: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5476,
            "confidence": 0.5476,
            "content_id": "6624571b-da19-48dd-b2c0-5ab95432f188",
            "creator_id": "mocked-c5-4",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.16602391043278608,
              "punctuation_density": 0.053691275167785234,
              "punctuation_simplicity": 0.5525727069351231,
              "repetition": 0.48148148148148145,
              "sentence_count": 7,
              "sentence_length_spread": 0.6671808716537712,
              "style_score": 0.338,
              "type_token_ratio": 0.6111111111111112,
              "word_count": 108
            },
            "style_score": 0.338,
            "text_length": 552,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "4ec197b3-4ff6-4dc4-b7bc-7d73b6c94446",
                "creator_id": "mocked-c5-5",
                "event": "appeal",
                "reasoning": "  Capstone review 5: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5236,
            "confidence": 0.5236,
            "content_id": "4ec197b3-4ff6-4dc4-b7bc-7d73b6c94446",
            "creator_id": "mocked-c5-5",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.0,
              "punctuation_density": 0.04195804195804196,
              "punctuation_simplicity": 0.6503496503496503,
              "repetition": 0.29227053140096626,
              "sentence_count": 3,
              "sentence_length_spread": 0.8615573303015565,
              "style_score": 0.2178,
              "type_token_ratio": 0.7246376811594203,
              "word_count": 69
            },
            "style_score": 0.2178,
            "text_length": 354,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "e1b4cf3e-8764-4328-b386-350ebcfd669e",
                "creator_id": "mocked-c5-6",
                "event": "appeal",
                "reasoning": "  Capstone review 6: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5682,
            "confidence": 0.5682,
            "content_id": "e1b4cf3e-8764-4328-b386-350ebcfd669e",
            "creator_id": "mocked-c5-6",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.38795621995783924,
              "punctuation_density": 0.01937046004842615,
              "punctuation_simplicity": 0.8385794995964487,
              "repetition": 0.2640449438202247,
              "sentence_count": 4,
              "sentence_length_spread": 0.48963502403372866,
              "style_score": 0.4409,
              "type_token_ratio": 0.7415730337078652,
              "word_count": 89
            },
            "style_score": 0.4409,
            "text_length": 501,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "c7bfc6cd-2849-4e6f-92be-487decd4a063",
                "creator_id": "mocked-c5-7",
                "event": "appeal",
                "reasoning": "  Capstone review 7: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.581,
            "confidence": 0.581,
            "content_id": "c7bfc6cd-2849-4e6f-92be-487decd4a063",
            "creator_id": "mocked-c5-7",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.5,
              "punctuation_density": 0.035343035343035345,
              "punctuation_simplicity": 0.7054747054747055,
              "repetition": 0.3790560471976401,
              "sentence_count": 2,
              "sentence_length_spread": 0.008849557522123894,
              "style_score": 0.5048,
              "type_token_ratio": 0.672566371681416,
              "word_count": 113
            },
            "style_score": 0.5048,
            "text_length": 592,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "5b96ba96-bfd8-4bdb-977a-9ecaaefc66f4",
                "creator_id": "mocked-c5-8",
                "event": "appeal",
                "reasoning": "  Capstone review 8: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5721,
            "confidence": 0.5721,
            "content_id": "5b96ba96-bfd8-4bdb-977a-9ecaaefc66f4",
            "creator_id": "mocked-c5-8",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.420697370644045,
              "punctuation_density": 0.03232323232323232,
              "punctuation_simplicity": 0.7306397306397306,
              "repetition": 0.3473520249221185,
              "sentence_count": 4,
              "sentence_length_spread": 0.46344210348476406,
              "style_score": 0.4607,
              "type_token_ratio": 0.6915887850467289,
              "word_count": 107
            },
            "style_score": 0.4607,
            "text_length": 598,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "8b2efeef-421a-4baa-ab11-5d1b35d9188e",
                "creator_id": "mocked-c5-9",
                "event": "appeal",
                "reasoning": "  Capstone review 9: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5762,
            "confidence": 0.5762,
            "content_id": "8b2efeef-421a-4baa-ab11-5d1b35d9188e",
            "creator_id": "mocked-c5-9",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.26494047860054226,
              "punctuation_density": 0.018823529411764704,
              "punctuation_simplicity": 0.8431372549019608,
              "repetition": 0.6,
              "sentence_count": 3,
              "sentence_length_spread": 0.5880476171195662,
              "style_score": 0.4811,
              "type_token_ratio": 0.54,
              "word_count": 100
            },
            "style_score": 0.4811,
            "text_length": 524,
            "timestamp": "2026-11-14T02:08:53+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "d64d3380-27f7-4ef1-9440-84cf9412203e",
                "creator_id": "mocked-c5-10",
                "event": "appeal",
                "reasoning": "  Capstone review 10: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:08:53+00:00"
              }
            ],
            "combined_score": 0.5747,
            "confidence": 0.5747,
            "content_id": "d64d3380-27f7-4ef1-9440-84cf9412203e",
            "creator_id": "mocked-c5-10",
            "detector_model": "gpt2",
            "guess": "unsure",
            "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
            "model_score": 0.6,
            "status": "under_review",
            "style_metrics": {
              "evenness": 0.4729379744287563,
              "punctuation_density": 0.047058823529411764,
              "punctuation_simplicity": 0.607843137254902,
              "repetition": 0.3842975206611571,
              "sentence_count": 4,
              "sentence_length_spread": 0.421649620456995,
              "style_score": 0.4733,
              "type_token_ratio": 0.6694214876033058,
              "word_count": 121
            },
            "style_score": 0.4733,
            "text_length": 626,
            "timestamp": "2026-11-14T02:08:53+00:00"
          }
        ]
      },
      "passed": true
    },
    "passed": true
  },
  "passed": true,
  "verdict": "MET",
  "invalid_attempts": []
}
```

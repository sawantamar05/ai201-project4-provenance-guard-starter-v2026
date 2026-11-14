# Capstone campaign — before

Criteria SHA-256: `b54324f9b43cecf68ba911daec030a362ae5d7dae9243d85591440193f22ed14`.

Real GPT-2 HTTP trials; isolated companion call counts are explicitly mocked.

| Criterion | Target | Run1 | Run2 | Run3 | Verdict |
|---|---|---|---|---|---|
| 1. Validation errors under quota pressure | 20/20 exact JSON validation responses; no malformed scoring/success events | 10/20 exact; no-success-events=True; isolated=True | 10/20 exact; no-success-events=True; isolated=True | 10/20 exact; no-success-events=True; isolated=True | MISSED |
| 2. Malformed requests preserve scoring allowance | 12/12 invalid400; then ten200 and two429; exactly10 isolated detector calls | 10/12 invalid400; 0/10 valid200; 2/2 quota429; isolated=False | 10/12 invalid400; 0/10 valid200; 2/2 quota429; isolated=False | 10/12 invalid400; 0/10 valid200; 2/2 quota429; isolated=False | MISSED |
| 3. Complete durable request records | 23/23 durable unique correlated completion records with required redacted fields | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | MET |
| 4. Warm submission response time | 10/10 complete decisions; at least9/10 warm requests below5.0s | 10/10 decisions; 10/10<5s; mean0.0579s | 10/10 decisions; 10/10<5s; mean0.0548s | 10/10 decisions; 10/10<5s; mean0.0710s | MET |
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
            "127.0.0.1:59035",
            "app:app"
          ],
          "pid": 74310,
          "started_at_utc": "2026-11-14T02:04:39.919531+00:00",
          "url": "http://127.0.0.1:59035",
          "log_directory": "results/capstone/before/c1_trial1_attempt1/ordinary",
          "environment_overrides": {
            "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c1_trial1_attempt1/ordinary",
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
          "health_request_id": "edcd1ff5-d18d-4865-acf7-59d03267287b",
          "cold_warmup": {
            "name": "disclosed cold-model warm-up",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:40.111851+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "cap-before-c1-t1-a1-warm"
            },
            "status_code": 200,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "746",
              "X-Request-ID": "36ad6118-aee3-4e26-b221-d515e6e07bc6"
            },
            "request_id": "36ad6118-aee3-4e26-b221-d515e6e07bc6",
            "response_json": {
              "combined_score": 0.6593,
              "confidence": 0.6593,
              "content_id": "f33fb4c8-db5d-44f4-8728-6f80a03c121f",
              "creator_id": "cap-before-c1-t1-a1-warm",
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
              "timestamp": "2026-11-14T02:04:46+00:00"
            },
            "elapsed_seconds": 6.673412750009447,
            "request_body_bytes": 431
          },
          "stopped_at_utc": "2026-11-14T02:04:47.150764+00:00",
          "returncode": 0
        }
      ],
      "warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:04:40.111851+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c1-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "746",
          "X-Request-ID": "36ad6118-aee3-4e26-b221-d515e6e07bc6"
        },
        "request_id": "36ad6118-aee3-4e26-b221-d515e6e07bc6",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "f33fb4c8-db5d-44f4-8728-6f80a03c121f",
          "creator_id": "cap-before-c1-t1-a1-warm",
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
          "timestamp": "2026-11-14T02:04:46+00:00"
        },
        "elapsed_seconds": 6.673412750009447,
        "request_body_bytes": 431
      },
      "quota_sequence_seconds": 0.014375458005815744,
      "cases": [
        {
          "case": 1,
          "name": "missing text",
          "expected_status": 400,
          "http": {
            "name": "missing text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:46.785522+00:00",
            "request_json": {
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "20275d1c-2497-4f8a-add3-b84ff74c6b02"
            },
            "request_id": "20275d1c-2497-4f8a-add3-b84ff74c6b02",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.0018562087789177895,
            "request_body_bytes": 37
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
            "sent_at_utc": "2026-11-14T02:04:46.787394+00:00",
            "request_json": {
              "text": "",
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "11ba3c83-fd20-4ddc-8c62-b100b7ad6df5"
            },
            "request_id": "11ba3c83-fd20-4ddc-8c62-b100b7ad6df5",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.0015530833043158054,
            "request_body_bytes": 49
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
            "sent_at_utc": "2026-11-14T02:04:46.788959+00:00",
            "request_json": {
              "text": 42,
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "69",
              "X-Request-ID": "db6df697-a620-4057-bf74-50407587e156"
            },
            "request_id": "db6df697-a620-4057-bf74-50407587e156",
            "response_json": {
              "error": "invalid_text",
              "message": "text must be a nonempty string."
            },
            "elapsed_seconds": 0.001225542277097702,
            "request_body_bytes": 49
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
            "sent_at_utc": "2026-11-14T02:04:46.790196+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "107",
              "X-Request-ID": "a1e78287-0ce1-4635-a288-8922d191d712"
            },
            "request_id": "a1e78287-0ce1-4635-a288-8922d191d712",
            "response_json": {
              "error": "invalid_creator_id",
              "message": "creator_id must be a nonempty string of at most 128 characters."
            },
            "elapsed_seconds": 0.0028208750300109386,
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
            "sent_at_utc": "2026-11-14T02:04:46.793027+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "   "
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "107",
              "X-Request-ID": "b0276ba6-f8ff-49f9-8988-84ce95fc3047"
            },
            "request_id": "b0276ba6-f8ff-49f9-8988-84ce95fc3047",
            "response_json": {
              "error": "invalid_creator_id",
              "message": "creator_id must be a nonempty string of at most 128 characters."
            },
            "elapsed_seconds": 0.0019810409285128117,
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
            "sent_at_utc": "2026-11-14T02:04:46.795037+00:00",
            "request_json": {
              "text": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 413,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "79",
              "X-Request-ID": "a8a44ca4-ccaf-4ad4-ac71-4f1195349bd2"
            },
            "request_id": "a8a44ca4-ccaf-4ad4-ac71-4f1195349bd2",
            "response_json": {
              "error": "text_too_large",
              "message": "text must not exceed 10,000 characters."
            },
            "elapsed_seconds": 0.001016582828015089,
            "request_body_bytes": 10050
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
            "sent_at_utc": "2026-11-14T02:04:46.796063+00:00",
            "request_body": "{",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "63",
              "X-Request-ID": "7ac537e7-ccae-4107-9df2-5a74371ac246"
            },
            "request_id": "7ac537e7-ccae-4107-9df2-5a74371ac246",
            "response_json": {
              "error": "invalid_json",
              "message": "Send a valid JSON object."
            },
            "elapsed_seconds": 0.0009237919002771378,
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
            "sent_at_utc": "2026-11-14T02:04:46.796997+00:00",
            "request_body": "[]",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 400,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "63",
              "X-Request-ID": "9e0e01d6-bae0-4543-be62-2602a391105c"
            },
            "request_id": "9e0e01d6-bae0-4543-be62-2602a391105c",
            "response_json": {
              "error": "invalid_json",
              "message": "Send a valid JSON object."
            },
            "elapsed_seconds": 0.0009821252897381783,
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
            "sent_at_utc": "2026-11-14T02:04:46.797986+00:00",
            "request_body": "hello",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 415,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "77",
              "X-Request-ID": "eff0ffd8-ad91-4cce-a3f6-63e04c851731"
            },
            "request_id": "eff0ffd8-ad91-4cce-a3f6-63e04c851731",
            "response_json": {
              "error": "json_required",
              "message": "Send an application/json request body."
            },
            "elapsed_seconds": 0.0008276249282062054,
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
            "sent_at_utc": "2026-11-14T02:04:46.798821+00:00",
            "request_body": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 413,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:46 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "85",
              "X-Request-ID": "cee1991d-8c95-4526-af0b-d8826f8b00d2"
            },
            "request_id": "cee1991d-8c95-4526-af0b-d8826f8b00d2",
            "response_json": {
              "error": "request_too_large",
              "message": "Request body must not exceed 65,536 bytes."
            },
            "elapsed_seconds": 0.0008380417712032795,
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
            "127.0.0.1:59053",
            "app:app"
          ],
          "pid": 74320,
          "started_at_utc": "2026-11-14T02:04:47.153447+00:00",
          "url": "http://127.0.0.1:59053",
          "log_directory": "results/capstone/before/c1_trial1_attempt1/pressure",
          "environment_overrides": {
            "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c1_trial1_attempt1/pressure",
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
          "health_request_id": "b6a775f4-5840-4f46-ad72-e7054ba9cb2a",
          "cold_warmup": {
            "name": "disclosed cold-model warm-up",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:47.308486+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "cap-before-c1-t1-a1-warm"
            },
            "status_code": 200,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:48 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "746",
              "X-Request-ID": "a459b606-433e-4e8d-86d1-2e6b1d8c0dd9"
            },
            "request_id": "a459b606-433e-4e8d-86d1-2e6b1d8c0dd9",
            "response_json": {
              "combined_score": 0.6593,
              "confidence": 0.6593,
              "content_id": "88b7d83a-5380-4af9-a701-967136b2f02d",
              "creator_id": "cap-before-c1-t1-a1-warm",
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
              "timestamp": "2026-11-14T02:04:48+00:00"
            },
            "elapsed_seconds": 1.58771758293733,
            "request_body_bytes": 431
          },
          "stopped_at_utc": "2026-11-14T02:04:49.667752+00:00",
          "returncode": 0
        }
      ],
      "warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:04:47.308486+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c1-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:04:48 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "746",
          "X-Request-ID": "a459b606-433e-4e8d-86d1-2e6b1d8c0dd9"
        },
        "request_id": "a459b606-433e-4e8d-86d1-2e6b1d8c0dd9",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "88b7d83a-5380-4af9-a701-967136b2f02d",
          "creator_id": "cap-before-c1-t1-a1-warm",
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
          "timestamp": "2026-11-14T02:04:48+00:00"
        },
        "elapsed_seconds": 1.58771758293733,
        "request_body_bytes": 431
      },
      "creator_pressure": [
        {
          "name": "creator pressure 1",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:48.896214+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:48 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "66c96e7f-8c58-457a-88b8-ba2bdfd7b58f"
          },
          "request_id": "66c96e7f-8c58-457a-88b8-ba2bdfd7b58f",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "0eb22658-bf8b-4ee6-9765-f67025c628e6",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:48+00:00"
          },
          "elapsed_seconds": 0.04248737497255206,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 2",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:48.938719+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:48 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "def70d7a-0223-42de-b917-6555d2fbaebf"
          },
          "request_id": "def70d7a-0223-42de-b917-6555d2fbaebf",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "298c8a98-1268-4fb7-96e4-7d399acfb25d",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:48+00:00"
          },
          "elapsed_seconds": 0.040405791252851486,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 3",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:48.979138+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "a4aca5a8-9e9e-4022-855e-d73fbd97cc55"
          },
          "request_id": "a4aca5a8-9e9e-4022-855e-d73fbd97cc55",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "bff60310-d87d-41ce-80a1-db546d2abc11",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.040370958391577005,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 4",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.019523+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "67058d7a-153f-4264-9ab6-856d792ffc58"
          },
          "request_id": "67058d7a-153f-4264-9ab6-856d792ffc58",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "989459d3-92b7-4f2d-b6af-582684cd016e",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.03966191690415144,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 5",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.059194+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "eee6c764-cd08-4314-93e3-4d6a27011664"
          },
          "request_id": "eee6c764-cd08-4314-93e3-4d6a27011664",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "8aa37c32-66c5-464d-90ac-a8315db3d598",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.03981708409264684,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 6",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.099021+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "7667875a-7a6a-4eba-add5-6c55a1d6b393"
          },
          "request_id": "7667875a-7a6a-4eba-add5-6c55a1d6b393",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "ef802c80-3564-40a1-bc7e-792ac2c7f02b",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.039762749802321196,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 7",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.138793+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "f660acf0-f2f9-47c5-9b0a-e47d1b86283f"
          },
          "request_id": "f660acf0-f2f9-47c5-9b0a-e47d1b86283f",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "756bae08-3fa0-444f-a48e-a314d9658625",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.03969124983996153,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 8",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.178493+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "0f90b5f3-e3f1-4cf4-adb4-994759fe6e7f"
          },
          "request_id": "0f90b5f3-e3f1-4cf4-adb4-994759fe6e7f",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "98254727-cd1e-4e8e-8416-058eca13b025",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.039557499811053276,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 9",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.218058+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "299b9afd-b16f-492d-9b02-05a8b1199a4e"
          },
          "request_id": "299b9afd-b16f-492d-9b02-05a8b1199a4e",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "167e8b73-2da5-4edf-bba0-1858ee4882a4",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.040260291658341885,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 10",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.258326+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "741",
            "X-Request-ID": "6fbcc7ac-862c-49a1-9062-39e393b3a7f5"
          },
          "request_id": "6fbcc7ac-862c-49a1-9062-39e393b3a7f5",
          "response_json": {
            "combined_score": 0.6593,
            "confidence": 0.6593,
            "content_id": "e8e33e54-03e3-4781-b8d1-bf977725109f",
            "creator_id": "cap-before-c1-t1-a1",
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
            "timestamp": "2026-11-14T02:04:49+00:00"
          },
          "elapsed_seconds": 0.039536832831799984,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 11",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.297870+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 429,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "78",
            "X-Request-ID": "c87b546b-a3fd-449a-98eb-e7163eb688ef"
          },
          "request_id": "c87b546b-a3fd-449a-98eb-e7163eb688ef",
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "elapsed_seconds": 0.0010454999282956123,
          "request_body_bytes": 426
        },
        {
          "name": "creator pressure 12",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.298922+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
            "creator_id": "cap-before-c1-t1-a1"
          },
          "status_code": 429,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "78",
            "X-Request-ID": "6c730e8e-0f4c-4b57-8882-fe3fcdfae310"
          },
          "request_id": "6c730e8e-0f4c-4b57-8882-fe3fcdfae310",
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "elapsed_seconds": 0.0008349581621587276,
          "request_body_bytes": 426
        }
      ],
      "address_pressure": [
        {
          "name": "address pressure 1",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.299766+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "1e161f60-95f4-4308-80cd-288feb4c2092"
          },
          "request_id": "1e161f60-95f4-4308-80cd-288feb4c2092",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0008681248873472214,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 2",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.300641+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "100a4db7-1b16-4fa9-9846-a7e0c0726a81"
          },
          "request_id": "100a4db7-1b16-4fa9-9846-a7e0c0726a81",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007625836879014969,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 3",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.301408+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "2244c4c0-3c0e-4a9c-87fa-3a62280bf8dd"
          },
          "request_id": "2244c4c0-3c0e-4a9c-87fa-3a62280bf8dd",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007692920044064522,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 4",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.302183+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "97f8a8f3-b09c-4788-aac6-e5a332759c3c"
          },
          "request_id": "97f8a8f3-b09c-4788-aac6-e5a332759c3c",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0008002081885933876,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 5",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.302989+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "6025af7c-d95d-4323-ac77-100925a850af"
          },
          "request_id": "6025af7c-d95d-4323-ac77-100925a850af",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007429579272866249,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 6",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.303737+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "711034e8-43b0-4552-88b0-3cce09b38632"
          },
          "request_id": "711034e8-43b0-4552-88b0-3cce09b38632",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007764589972794056,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 7",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.304518+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "69c62882-94c8-4b45-93a3-7923b7af8fd0"
          },
          "request_id": "69c62882-94c8-4b45-93a3-7923b7af8fd0",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007222089916467667,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 8",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.305245+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "2ee016c7-5912-4d4d-a3fe-a31fc7b68910"
          },
          "request_id": "2ee016c7-5912-4d4d-a3fe-a31fc7b68910",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.000756249763071537,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 9",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.306007+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "eacba2e5-8153-4545-bfd8-aa18b8adfbcf"
          },
          "request_id": "eacba2e5-8153-4545-bfd8-aa18b8adfbcf",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.0007674167864024639,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 10",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.306780+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 400,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "107",
            "X-Request-ID": "99673f90-1ad1-40bc-8ce4-4ed395108753"
          },
          "request_id": "99673f90-1ad1-40bc-8ce4-4ed395108753",
          "response_json": {
            "error": "invalid_creator_id",
            "message": "creator_id must be a nonempty string of at most 128 characters."
          },
          "elapsed_seconds": 0.000761999748647213,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 11",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.307546+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 429,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "78",
            "X-Request-ID": "32658018-0ad0-4b00-8b67-b1f16e3d383e"
          },
          "request_id": "32658018-0ad0-4b00-8b67-b1f16e3d383e",
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "elapsed_seconds": 0.0007507079280912876,
          "request_body_bytes": 389
        },
        {
          "name": "address pressure 12",
          "method": "POST",
          "path": "/submit",
          "sent_at_utc": "2026-11-14T02:04:49.308302+00:00",
          "request_json": {
            "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
          },
          "status_code": 429,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "78",
            "X-Request-ID": "80d9cd6e-3678-4d6f-a689-cf414312adff"
          },
          "request_id": "80d9cd6e-3678-4d6f-a689-cf414312adff",
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "elapsed_seconds": 0.0007579587399959564,
          "request_body_bytes": 389
        }
      ],
      "quota_sequence_seconds": 0.4205812909640372,
      "cases": [
        {
          "case": 1,
          "name": "missing text",
          "expected_status": 400,
          "http": {
            "name": "missing text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.309310+00:00",
            "request_json": {
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "75d50487-29e7-4e7d-abf6-7a19bc279d60"
            },
            "request_id": "75d50487-29e7-4e7d-abf6-7a19bc279d60",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0008078329265117645,
            "request_body_bytes": 37
          },
          "passed": false
        },
        {
          "case": 2,
          "name": "empty text",
          "expected_status": 400,
          "http": {
            "name": "empty text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.310124+00:00",
            "request_json": {
              "text": "",
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "2f5c2e42-06d0-43d1-a925-b200422b3b69"
            },
            "request_id": "2f5c2e42-06d0-43d1-a925-b200422b3b69",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0007262500002980232,
            "request_body_bytes": 49
          },
          "passed": false
        },
        {
          "case": 3,
          "name": "numeric text",
          "expected_status": 400,
          "http": {
            "name": "numeric text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.310857+00:00",
            "request_json": {
              "text": 42,
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "5f470208-cab5-4bf0-b247-440952d0f11a"
            },
            "request_id": "5f470208-cab5-4bf0-b247-440952d0f11a",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0007762918248772621,
            "request_body_bytes": 49
          },
          "passed": false
        },
        {
          "case": 4,
          "name": "missing creator",
          "expected_status": 400,
          "http": {
            "name": "missing creator",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.311639+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters."
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "1c541548-f256-4de4-8dbd-9791a43adf78"
            },
            "request_id": "1c541548-f256-4de4-8dbd-9791a43adf78",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0006928746588528156,
            "request_body_bytes": 389
          },
          "passed": false
        },
        {
          "case": 5,
          "name": "blank creator",
          "expected_status": 400,
          "http": {
            "name": "blank creator",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.312337+00:00",
            "request_json": {
              "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
              "creator_id": "   "
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "c6486fc6-5685-47fb-9953-1f1c7dc24e85"
            },
            "request_id": "c6486fc6-5685-47fb-9953-1f1c7dc24e85",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0006948751397430897,
            "request_body_bytes": 410
          },
          "passed": false
        },
        {
          "case": 6,
          "name": "oversized text",
          "expected_status": 413,
          "http": {
            "name": "oversized text",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.313037+00:00",
            "request_json": {
              "text": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
              "creator_id": "cap-before-c1-t1-a1"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "73fad68c-0712-4370-ab4b-f1f600dae210"
            },
            "request_id": "73fad68c-0712-4370-ab4b-f1f600dae210",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.000803791917860508,
            "request_body_bytes": 10050
          },
          "passed": false
        },
        {
          "case": 7,
          "name": "malformed JSON",
          "expected_status": 400,
          "http": {
            "name": "malformed JSON",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.313846+00:00",
            "request_body": "{",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "0d8631e2-9eac-4145-9a07-4be1415a0694"
            },
            "request_id": "0d8631e2-9eac-4145-9a07-4be1415a0694",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.000741083174943924,
            "request_body_bytes": 1
          },
          "passed": false
        },
        {
          "case": 8,
          "name": "non-object JSON",
          "expected_status": 400,
          "http": {
            "name": "non-object JSON",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.314594+00:00",
            "request_body": "[]",
            "request_headers": {
              "Content-Type": "application/json"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "8be2a33a-1a53-47e6-a911-5eac18043104"
            },
            "request_id": "8be2a33a-1a53-47e6-a911-5eac18043104",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0007330840453505516,
            "request_body_bytes": 2
          },
          "passed": false
        },
        {
          "case": 9,
          "name": "non-JSON content type",
          "expected_status": 415,
          "http": {
            "name": "non-JSON content type",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.315333+00:00",
            "request_body": "hello",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "89fa4e5a-75ff-4a36-9ad5-6babf0f45c59"
            },
            "request_id": "89fa4e5a-75ff-4a36-9ad5-6babf0f45c59",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0007084589451551437,
            "request_body_bytes": 5
          },
          "passed": false
        },
        {
          "case": 10,
          "name": "oversized non-JSON body",
          "expected_status": 413,
          "http": {
            "name": "oversized non-JSON body",
            "method": "POST",
            "path": "/submit",
            "sent_at_utc": "2026-11-14T02:04:49.316047+00:00",
            "request_body": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "request_headers": {
              "Content-Type": "text/plain"
            },
            "status_code": 429,
            "response_headers": {
              "Server": "gunicorn",
              "Date": "Sat, 14 Nov 2026 02:04:49 GMT",
              "Connection": "close",
              "Content-Type": "application/json",
              "Content-Length": "78",
              "X-Request-ID": "4efb51ae-2bd4-4335-a6c3-7e2bbd813904"
            },
            "request_id": "4efb51ae-2bd4-4335-a6c3-7e2bbd813904",
            "response_json": {
              "error": "rate_limited",
              "message": "Too many submissions. Try again shortly."
            },
            "elapsed_seconds": 0.0007319170981645584,
            "request_body_bytes": 65537
          },
          "passed": false
        }
      ],
      "audit_parse_errors": [],
      "successful_events_unchanged": true,
      "quota_window_valid": true,
      "passed": false
    }
  ],
  "quota_window_valid": true,
  "http_passed": false,
  "exact_status_count": 10,
  "summary": "10/20 exact; no-success-events=True",
  "trial": 1,
  "attempt": 1,
  "criterion": 1,
  "evidence_directory": "results/capstone/before/c1_trial1_attempt1",
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
                "content_id": "45e4ac2a-89e9-43e2-9ae7-206fb6727986",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "94c0347f-aa54-468f-821c-942f40985160",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "4485dbc7-b1c2-4dec-b90a-5f24d7ea58df",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "9785f5cb-1b64-469c-a425-ff5b2abe440e",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "dd1c405b-466a-4352-b2f7-e608e44aae16",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "ac37da3f-0428-4966-8ec4-03d1fc2e0499",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "dfe2989e-0588-472c-b21b-59768ab0afc1",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "e0f1512b-410c-4e8c-afe6-cb3d2b7797d3",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "cf42c415-5302-4129-9dc1-22432f4bf354",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
              }
            },
            {
              "status_code": 200,
              "response_json": {
                "combined_score": 0.5856,
                "confidence": 0.5856,
                "content_id": "9b0f1912-8a28-4173-a840-959cb7d60b55",
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
                "timestamp": "2026-11-14T02:04:49+00:00"
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
            }
          ],
          "pressure_detector_calls": 10,
          "cases": [
            {
              "case": 1,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 2,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 3,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 4,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 5,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 6,
              "expected_status": 413,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 7,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 8,
              "expected_status": 400,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 9,
              "expected_status": 415,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
              },
              "detector_calls": 0
            },
            {
              "case": 10,
              "expected_status": 413,
              "status_code": 429,
              "response_json": {
                "error": "rate_limited",
                "message": "Too many submissions. Try again shortly."
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
  "passed": false,
  "verdict": "MISSED",
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
        "127.0.0.1:59200",
        "app:app"
      ],
      "pid": 74356,
      "started_at_utc": "2026-11-14T02:04:59.141486+00:00",
      "url": "http://127.0.0.1:59200",
      "log_directory": "results/capstone/before/c2_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c2_trial1_attempt1",
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
      "health_request_id": "e5ad0baa-f141-4dc5-9580-3c62a655d485",
      "cold_warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:04:59.259531+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c2-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "746",
          "X-Request-ID": "6c3933c3-249e-4dc8-9810-202f96a42f1c"
        },
        "request_id": "6c3933c3-249e-4dc8-9810-202f96a42f1c",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "d345f138-2886-497b-8453-9b17bb5c1bc6",
          "creator_id": "cap-before-c2-t1-a1-warm",
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
          "timestamp": "2026-11-14T02:05:00+00:00"
        },
        "elapsed_seconds": 1.5208025840111077,
        "request_body_bytes": 431
      },
      "stopped_at_utc": "2026-11-14T02:05:01.145637+00:00",
      "returncode": 0
    }
  ],
  "warmup": {
    "name": "disclosed cold-model warm-up",
    "method": "POST",
    "path": "/submit",
    "sent_at_utc": "2026-11-14T02:04:59.259531+00:00",
    "request_json": {
      "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
      "creator_id": "cap-before-c2-t1-a1-warm"
    },
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "746",
      "X-Request-ID": "6c3933c3-249e-4dc8-9810-202f96a42f1c"
    },
    "request_id": "6c3933c3-249e-4dc8-9810-202f96a42f1c",
    "response_json": {
      "combined_score": 0.6593,
      "confidence": 0.6593,
      "content_id": "d345f138-2886-497b-8453-9b17bb5c1bc6",
      "creator_id": "cap-before-c2-t1-a1-warm",
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
      "timestamp": "2026-11-14T02:05:00+00:00"
    },
    "elapsed_seconds": 1.5208025840111077,
    "request_body_bytes": 431
  },
  "invalid_requests": [
    {
      "name": "invalid allowance check 1",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.780344+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "88116d1f-3a3a-415d-b304-58fed9821c6e"
      },
      "request_id": "88116d1f-3a3a-415d-b304-58fed9821c6e",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0012204158119857311,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 2",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.781575+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "07be9de7-8f74-4f25-865e-45fae63e4654"
      },
      "request_id": "07be9de7-8f74-4f25-865e-45fae63e4654",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0009142500348389149,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 3",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.782496+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "2e7ad3e9-0999-4b4d-a566-663cb9983901"
      },
      "request_id": "2e7ad3e9-0999-4b4d-a566-663cb9983901",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007802918553352356,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 4",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.783281+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "224a6061-358d-445e-961b-338eff0e98e5"
      },
      "request_id": "224a6061-358d-445e-961b-338eff0e98e5",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007313336245715618,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 5",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.784020+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "d6d90cc0-4902-4e66-8776-d6e959d6b7a7"
      },
      "request_id": "d6d90cc0-4902-4e66-8776-d6e959d6b7a7",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.000832791905850172,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 6",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.784858+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "f227373a-7306-4e4d-a110-7a144d98cf7a"
      },
      "request_id": "f227373a-7306-4e4d-a110-7a144d98cf7a",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.000842084176838398,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 7",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.785706+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "954a9392-05bc-4a3c-b58a-b5941a94bb7a"
      },
      "request_id": "954a9392-05bc-4a3c-b58a-b5941a94bb7a",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0010234997607767582,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 8",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.786735+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "816b82e5-2a29-4146-8a98-ed8094962398"
      },
      "request_id": "816b82e5-2a29-4146-8a98-ed8094962398",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0009238747879862785,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 9",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.787664+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "1b51a08e-5671-452e-b161-c7e91fc2eb79"
      },
      "request_id": "1b51a08e-5671-452e-b161-c7e91fc2eb79",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007830420508980751,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 10",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.788452+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 400,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "69",
        "X-Request-ID": "4f150e9d-72eb-4b9f-bb29-dc0eec50dcaf"
      },
      "request_id": "4f150e9d-72eb-4b9f-bb29-dc0eec50dcaf",
      "response_json": {
        "error": "invalid_text",
        "message": "text must be a nonempty string."
      },
      "elapsed_seconds": 0.0007446669042110443,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 11",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.789203+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "6bc79fe5-fa32-48e8-9f74-2a5e83b69d38"
      },
      "request_id": "6bc79fe5-fa32-48e8-9f74-2a5e83b69d38",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007888749241828918,
      "request_body_bytes": 49
    },
    {
      "name": "invalid allowance check 12",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.789995+00:00",
      "request_json": {
        "text": "",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "45b96d41-f68a-4261-8e41-b887e3ee4d99"
      },
      "request_id": "45b96d41-f68a-4261-8e41-b887e3ee4d99",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007488341070711613,
      "request_body_bytes": 49
    }
  ],
  "valid_requests": [
    {
      "name": "valid allowance check 1",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.790750+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "829418d1-1344-44f9-927d-67ebbb68c226"
      },
      "request_id": "829418d1-1344-44f9-927d-67ebbb68c226",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007788334041833878,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 2",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.791534+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "b9c9985d-840b-471a-82b6-443b360f3b6c"
      },
      "request_id": "b9c9985d-840b-471a-82b6-443b360f3b6c",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.000734957866370678,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 3",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.792274+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "cca0ef0d-28b8-4fb4-bda0-69a832dc564e"
      },
      "request_id": "cca0ef0d-28b8-4fb4-bda0-69a832dc564e",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007072081789374352,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 4",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.792985+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "435bf79c-5382-4d7f-9f26-5ac7b16fb2e9"
      },
      "request_id": "435bf79c-5382-4d7f-9f26-5ac7b16fb2e9",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0006870422512292862,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 5",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.793676+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "f4da3935-5e9e-4652-8737-52bc3b67f7b5"
      },
      "request_id": "f4da3935-5e9e-4652-8737-52bc3b67f7b5",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007772920653223991,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 6",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.794458+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "c8b4fdda-1a6c-42ea-b495-7c199559867a"
      },
      "request_id": "c8b4fdda-1a6c-42ea-b495-7c199559867a",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007575410418212414,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 7",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.795220+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "670f4454-cc62-43de-9a96-7bfcacac5472"
      },
      "request_id": "670f4454-cc62-43de-9a96-7bfcacac5472",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0006921668536961079,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 8",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.795916+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "551a9b98-a4ec-4c17-aa96-0bcdd9ab6019"
      },
      "request_id": "551a9b98-a4ec-4c17-aa96-0bcdd9ab6019",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007229172624647617,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 9",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.796643+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "7b996af3-c755-45e1-a78b-b156454a58e4"
      },
      "request_id": "7b996af3-c755-45e1-a78b-b156454a58e4",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007043746300041676,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 10",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.797352+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "40a14d4c-6c36-4861-b4ef-06633e188e4d"
      },
      "request_id": "40a14d4c-6c36-4861-b4ef-06633e188e4d",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007118750363588333,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 11",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.798067+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "4383c303-627a-41fb-a2d8-e3dd19767014"
      },
      "request_id": "4383c303-627a-41fb-a2d8-e3dd19767014",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007033329457044601,
      "request_body_bytes": 426
    },
    {
      "name": "valid allowance check 12",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:00.798775+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c2-t1-a1"
      },
      "status_code": 429,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:00 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "78",
        "X-Request-ID": "03f690c1-793c-402a-98c9-18face4a466d"
      },
      "request_id": "03f690c1-793c-402a-98c9-18face4a466d",
      "response_json": {
        "error": "rate_limited",
        "message": "Too many submissions. Try again shortly."
      },
      "elapsed_seconds": 0.0007852921262383461,
      "request_body_bytes": 426
    }
  ],
  "quota_sequence_seconds": 0.01922391587868333,
  "quota_window_valid": true,
  "audit_parse_errors": [],
  "saved_decision_count": 0,
  "invalid400_count": 10,
  "valid200_count": 0,
  "throttled429_count": 2,
  "http_passed": false,
  "summary": "10/12 invalid400; 0/10 valid200; 2/2 quota429",
  "trial": 1,
  "attempt": 1,
  "criterion": 2,
  "evidence_directory": "results/capstone/before/c2_trial1_attempt1",
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
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "invalid",
          "index": 12,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 1,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 2,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 3,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 4,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 5,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 6,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 7,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 8,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 9,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
        },
        {
          "kind": "valid",
          "index": 10,
          "status_code": 429,
          "response_json": {
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly."
          },
          "detector_calls": 0
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
      "total_detector_calls": 0,
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
      "passed": false
    },
    "passed": false
  },
  "passed": false,
  "verdict": "MISSED",
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
        "127.0.0.1:59289",
        "app:app"
      ],
      "pid": 74378,
      "started_at_utc": "2026-11-14T02:05:05.928088+00:00",
      "url": "http://127.0.0.1:59289",
      "log_directory": "results/capstone/before/c3_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c3_trial1_attempt1",
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
      "health_request_id": "53ab3312-f70a-4ca0-b4d4-be2c9518e3c1",
      "cold_warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:06.043749+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c3-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "746",
          "X-Request-ID": "b569cafe-cb8c-47dc-881b-15e4ae2dbb51"
        },
        "request_id": "b569cafe-cb8c-47dc-881b-15e4ae2dbb51",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "1c3cc853-38b3-424b-b6e5-716b0ccf1912",
          "creator_id": "cap-before-c3-t1-a1-warm",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 1.520980291068554,
        "request_body_bytes": 431
      },
      "stopped_at_utc": "2026-11-14T02:05:08.482631+00:00",
      "returncode": 0
    }
  ],
  "warmup": {
    "name": "disclosed cold-model warm-up",
    "method": "POST",
    "path": "/submit",
    "sent_at_utc": "2026-11-14T02:05:06.043749+00:00",
    "request_json": {
      "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
      "creator_id": "cap-before-c3-t1-a1-warm"
    },
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "746",
      "X-Request-ID": "b569cafe-cb8c-47dc-881b-15e4ae2dbb51"
    },
    "request_id": "b569cafe-cb8c-47dc-881b-15e4ae2dbb51",
    "response_json": {
      "combined_score": 0.6593,
      "confidence": 0.6593,
      "content_id": "1c3cc853-38b3-424b-b6e5-716b0ccf1912",
      "creator_id": "cap-before-c3-t1-a1-warm",
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
      "timestamp": "2026-11-14T02:05:07+00:00"
    },
    "elapsed_seconds": 1.520980291068554,
    "request_body_bytes": 431
  },
  "quota_sequence_seconds": 0.5668672500178218,
  "quota_window_valid": true,
  "cases": [
    {
      "http": {
        "name": "observed valid 1",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.564740+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "741",
          "X-Request-ID": "242e68d0-8474-453e-91f2-8619384ac3d4"
        },
        "request_id": "242e68d0-8474-453e-91f2-8619384ac3d4",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "44ae0c19-92ce-45a7-9ce8-78f693d63907",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.04063479183241725,
        "request_body_bytes": 426
      },
      "completion": {
        "event": "request_completed",
        "request_id": "242e68d0-8474-453e-91f2-8619384ac3d4",
        "timestamp": "2026-11-14T02:05:07.604929+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 426,
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
          "content_id": "44ae0c19-92ce-45a7-9ce8-78f693d63907",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 39.614958,
        "cpu_seconds": 0.054686
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 2",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.605392+00:00",
        "request_json": {
          "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "754",
          "X-Request-ID": "2aeed522-8190-4d21-ace3-09ab6b28dd1e"
        },
        "request_id": "2aeed522-8190-4d21-ace3-09ab6b28dd1e",
        "response_json": {
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "091b0960-65ad-47a8-8d50-fc181018dc0e",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.06772245792672038,
        "request_body_bytes": 713
      },
      "completion": {
        "event": "request_completed",
        "request_id": "2aeed522-8190-4d21-ace3-09ab6b28dd1e",
        "timestamp": "2026-11-14T02:05:07.672612+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 713,
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
          "content_id": "091b0960-65ad-47a8-8d50-fc181018dc0e",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 66.700666,
        "cpu_seconds": 0.105749
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 3",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.673123+00:00",
        "request_json": {
          "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "743",
          "X-Request-ID": "ba33c364-e6c1-4c02-8bd4-e9ad23780e8e"
        },
        "request_id": "ba33c364-e6c1-4c02-8bd4-e9ad23780e8e",
        "response_json": {
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "5444233e-2536-4567-a377-3a792606fe6a",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.07616783306002617,
        "request_body_bytes": 864
      },
      "completion": {
        "event": "request_completed",
        "request_id": "ba33c364-e6c1-4c02-8bd4-e9ad23780e8e",
        "timestamp": "2026-11-14T02:05:07.748717+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 864,
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
          "content_id": "5444233e-2536-4567-a377-3a792606fe6a",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 75.018083,
        "cpu_seconds": 0.119632
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 4",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.749301+00:00",
        "request_json": {
          "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "757",
          "X-Request-ID": "4d8af56b-16c7-4348-a8eb-3c2faf3b71b5"
        },
        "request_id": "4d8af56b-16c7-4348-a8eb-3c2faf3b71b5",
        "response_json": {
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "2c27184f-2a52-4750-8125-f959368be8fe",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.059267541859298944,
        "request_body_bytes": 626
      },
      "completion": {
        "event": "request_completed",
        "request_id": "4d8af56b-16c7-4348-a8eb-3c2faf3b71b5",
        "timestamp": "2026-11-14T02:05:07.808112+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 626,
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
          "content_id": "2c27184f-2a52-4750-8125-f959368be8fe",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 58.176458,
        "cpu_seconds": 0.089038
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 5",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.808583+00:00",
        "request_json": {
          "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "741",
          "X-Request-ID": "45dd6a52-40be-41bb-84ad-0e66726755a0"
        },
        "request_id": "45dd6a52-40be-41bb-84ad-0e66726755a0",
        "response_json": {
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "c427bab5-ce98-4b46-8ac2-d18ea34d1390",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.04328824998810887,
        "request_body_bytes": 403
      },
      "completion": {
        "event": "request_completed",
        "request_id": "45dd6a52-40be-41bb-84ad-0e66726755a0",
        "timestamp": "2026-11-14T02:05:07.851367+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 403,
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
          "content_id": "c427bab5-ce98-4b46-8ac2-d18ea34d1390",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 42.254541,
        "cpu_seconds": 0.059145
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 6",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.851888+00:00",
        "request_json": {
          "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "757",
          "X-Request-ID": "232ad02c-735b-4281-a0db-8cae1b9d81bc"
        },
        "request_id": "232ad02c-735b-4281-a0db-8cae1b9d81bc",
        "response_json": {
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "11206aa4-d345-40d3-85f4-d94cb9969aca",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.04790245881304145,
        "request_body_bytes": 550
      },
      "completion": {
        "event": "request_completed",
        "request_id": "232ad02c-735b-4281-a0db-8cae1b9d81bc",
        "timestamp": "2026-11-14T02:05:07.899317+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 550,
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
          "content_id": "11206aa4-d345-40d3-85f4-d94cb9969aca",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 46.923083,
        "cpu_seconds": 0.06786
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 7",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.899802+00:00",
        "request_json": {
          "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:07 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "743",
          "X-Request-ID": "0dff28f8-3b27-4f1e-9b7d-ef06eca72114"
        },
        "request_id": "0dff28f8-3b27-4f1e-9b7d-ef06eca72114",
        "response_json": {
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "54d31d08-a1c2-41ca-bbc8-9eb7f491405f",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:07+00:00"
        },
        "elapsed_seconds": 0.057367583736777306,
        "request_body_bytes": 661
      },
      "completion": {
        "event": "request_completed",
        "request_id": "0dff28f8-3b27-4f1e-9b7d-ef06eca72114",
        "timestamp": "2026-11-14T02:05:07.956728+00:00",
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
          "text_characters": 592
        },
        "output_summary": {
          "content_type": "application/json",
          "content_id": "54d31d08-a1c2-41ca-bbc8-9eb7f491405f",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 56.430083,
        "cpu_seconds": 0.085672
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 8",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:07.957177+00:00",
        "request_json": {
          "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "756",
          "X-Request-ID": "7822c843-fd6f-4d52-96bc-37a559bc83dc"
        },
        "request_id": "7822c843-fd6f-4d52-96bc-37a559bc83dc",
        "response_json": {
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "0b2aa426-3079-4167-aec4-4303f987f777",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.053116665687412024,
        "request_body_bytes": 662
      },
      "completion": {
        "event": "request_completed",
        "request_id": "7822c843-fd6f-4d52-96bc-37a559bc83dc",
        "timestamp": "2026-11-14T02:05:08.009774+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 662,
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
          "content_id": "0b2aa426-3079-4167-aec4-4303f987f777",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 52.114625,
        "cpu_seconds": 0.078547
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 9",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.010304+00:00",
        "request_json": {
          "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "729",
          "X-Request-ID": "ffba55a8-fa34-434a-bbbd-f469682a59ee"
        },
        "request_id": "ffba55a8-fa34-434a-bbbd-f469682a59ee",
        "response_json": {
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "cbd60647-25e5-489f-b351-490bb2521003",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.04912954196333885,
        "request_body_bytes": 573
      },
      "completion": {
        "event": "request_completed",
        "request_id": "ffba55a8-fa34-434a-bbbd-f469682a59ee",
        "timestamp": "2026-11-14T02:05:08.058921+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 573,
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
          "content_id": "cbd60647-25e5-489f-b351-490bb2521003",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 48.035792,
        "cpu_seconds": 0.070355
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed valid 10",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.059445+00:00",
        "request_json": {
          "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "754",
          "X-Request-ID": "ba59448b-210d-42db-9466-40cb3475f70d"
        },
        "request_id": "ba59448b-210d-42db-9466-40cb3475f70d",
        "response_json": {
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "186651e6-ae80-4f88-b618-b6f03f8c108d",
          "creator_id": "cap-before-c3-t1-a1",
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
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.06047499971464276,
        "request_body_bytes": 675
      },
      "completion": {
        "event": "request_completed",
        "request_id": "ba59448b-210d-42db-9466-40cb3475f70d",
        "timestamp": "2026-11-14T02:05:08.119451+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 200,
        "input_summary": {
          "body_bytes": 675,
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
          "content_id": "186651e6-ae80-4f88-b618-b6f03f8c108d",
          "guess": "unsure",
          "status": "decided",
          "outcome": "success"
        },
        "duration_ms": 59.441542,
        "cpu_seconds": 0.090831
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed quota 1",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.119938+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 429,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "78",
          "X-Request-ID": "9b84f980-ba20-41ff-954f-e8e0a0170675"
        },
        "request_id": "9b84f980-ba20-41ff-954f-e8e0a0170675",
        "response_json": {
          "error": "rate_limited",
          "message": "Too many submissions. Try again shortly."
        },
        "elapsed_seconds": 0.001154707744717598,
        "request_body_bytes": 426
      },
      "completion": {
        "event": "request_completed",
        "request_id": "9b84f980-ba20-41ff-954f-e8e0a0170675",
        "timestamp": "2026-11-14T02:05:08.120834+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 429,
        "input_summary": {
          "body_bytes": 426,
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
        "duration_ms": 0.343833,
        "cpu_seconds": 0.000333
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed quota 2",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.121105+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c3-t1-a1"
        },
        "status_code": 429,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "78",
          "X-Request-ID": "f6bdc2a6-1129-4b17-92db-c708d966250a"
        },
        "request_id": "f6bdc2a6-1129-4b17-92db-c708d966250a",
        "response_json": {
          "error": "rate_limited",
          "message": "Too many submissions. Try again shortly."
        },
        "elapsed_seconds": 0.0008711656555533409,
        "request_body_bytes": 426
      },
      "completion": {
        "event": "request_completed",
        "request_id": "f6bdc2a6-1129-4b17-92db-c708d966250a",
        "timestamp": "2026-11-14T02:05:08.121719+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 429,
        "input_summary": {
          "body_bytes": 426,
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
        "duration_ms": 0.20225,
        "cpu_seconds": 0.000186
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 1",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.121983+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-before-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "15b31b4f-7e30-470a-b30f-018e569a89b1"
        },
        "request_id": "15b31b4f-7e30-470a-b30f-018e569a89b1",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0008040829561650753,
        "request_body_bytes": 57
      },
      "completion": {
        "event": "request_completed",
        "request_id": "15b31b4f-7e30-470a-b30f-018e569a89b1",
        "timestamp": "2026-11-14T02:05:08.122552+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 57,
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
        "duration_ms": 0.188541,
        "cpu_seconds": 0.000182
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 2",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.122792+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-before-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "fdc242b5-d6d5-4eec-a8ce-df6b198c505c"
        },
        "request_id": "fdc242b5-d6d5-4eec-a8ce-df6b198c505c",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0009050830267369747,
        "request_body_bytes": 57
      },
      "completion": {
        "event": "request_completed",
        "request_id": "fdc242b5-d6d5-4eec-a8ce-df6b198c505c",
        "timestamp": "2026-11-14T02:05:08.123395+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 57,
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
        "duration_ms": 0.218333,
        "cpu_seconds": 0.000206
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 3",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.123704+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-before-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "051c8844-1b07-430f-8b3d-42f6a20e83a5"
        },
        "request_id": "051c8844-1b07-430f-8b3d-42f6a20e83a5",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.000874791294336319,
        "request_body_bytes": 57
      },
      "completion": {
        "event": "request_completed",
        "request_id": "051c8844-1b07-430f-8b3d-42f6a20e83a5",
        "timestamp": "2026-11-14T02:05:08.124330+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 57,
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
        "duration_ms": 0.19375,
        "cpu_seconds": 0.000187
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 4",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.124586+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-before-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "64d62e5a-5db2-451f-a65c-ec978a94146b"
        },
        "request_id": "64d62e5a-5db2-451f-a65c-ec978a94146b",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0008028340525925159,
        "request_body_bytes": 57
      },
      "completion": {
        "event": "request_completed",
        "request_id": "64d62e5a-5db2-451f-a65c-ec978a94146b",
        "timestamp": "2026-11-14T02:05:08.125164+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 57,
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
        "duration_ms": 0.182875,
        "cpu_seconds": 0.000176
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed invalid 5",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:08.125394+00:00",
        "request_json": {
          "text": "",
          "creator_id": "cap-before-c3-t1-a1-invalid"
        },
        "status_code": 400,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "69",
          "X-Request-ID": "76b23a04-41dd-41bd-a041-fe523197d791"
        },
        "request_id": "76b23a04-41dd-41bd-a041-fe523197d791",
        "response_json": {
          "error": "invalid_text",
          "message": "text must be a nonempty string."
        },
        "elapsed_seconds": 0.0008475002832710743,
        "request_body_bytes": 57
      },
      "completion": {
        "event": "request_completed",
        "request_id": "76b23a04-41dd-41bd-a041-fe523197d791",
        "timestamp": "2026-11-14T02:05:08.125938+00:00",
        "method": "POST",
        "path": "/submit",
        "http_status": 400,
        "input_summary": {
          "body_bytes": 57,
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
        "duration_ms": 0.16225,
        "cpu_seconds": 0.000154
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 1",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:05:08.126254+00:00",
        "request_json": {
          "content_id": "44ae0c19-92ce-45a7-9ce8-78f693d63907",
          "reasoning": "  Capstone review 1: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "311",
          "X-Request-ID": "e9bbda8f-c85f-4220-8adf-fcb6d8879b7a"
        },
        "request_id": "e9bbda8f-c85f-4220-8adf-fcb6d8879b7a",
        "response_json": {
          "content_id": "44ae0c19-92ce-45a7-9ce8-78f693d63907",
          "creator_id": "cap-before-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 1: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.0010115411132574081,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "e9bbda8f-c85f-4220-8adf-fcb6d8879b7a",
        "timestamp": "2026-11-14T02:05:08.127009+00:00",
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
          "content_id": "44ae0c19-92ce-45a7-9ce8-78f693d63907",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.282959,
        "cpu_seconds": 0.000276
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 2",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:05:08.127276+00:00",
        "request_json": {
          "content_id": "091b0960-65ad-47a8-8d50-fc181018dc0e",
          "reasoning": "  Capstone review 2: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "311",
          "X-Request-ID": "b540cc61-2e60-4214-9216-af4ca0fb039e"
        },
        "request_id": "b540cc61-2e60-4214-9216-af4ca0fb039e",
        "response_json": {
          "content_id": "091b0960-65ad-47a8-8d50-fc181018dc0e",
          "creator_id": "cap-before-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 2: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.0009191250428557396,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "b540cc61-2e60-4214-9216-af4ca0fb039e",
        "timestamp": "2026-11-14T02:05:08.127924+00:00",
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
          "content_id": "091b0960-65ad-47a8-8d50-fc181018dc0e",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.242625,
        "cpu_seconds": 0.000229
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 3",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:05:08.128202+00:00",
        "request_json": {
          "content_id": "5444233e-2536-4567-a377-3a792606fe6a",
          "reasoning": "  Capstone review 3: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "311",
          "X-Request-ID": "0d499daa-3d08-467e-9379-1446aeea4092"
        },
        "request_id": "0d499daa-3d08-467e-9379-1446aeea4092",
        "response_json": {
          "content_id": "5444233e-2536-4567-a377-3a792606fe6a",
          "creator_id": "cap-before-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 3: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.0008541671559214592,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "0d499daa-3d08-467e-9379-1446aeea4092",
        "timestamp": "2026-11-14T02:05:08.128831+00:00",
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
          "content_id": "5444233e-2536-4567-a377-3a792606fe6a",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.24575,
        "cpu_seconds": 0.000232
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 4",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:05:08.129063+00:00",
        "request_json": {
          "content_id": "2c27184f-2a52-4750-8125-f959368be8fe",
          "reasoning": "  Capstone review 4: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "311",
          "X-Request-ID": "a37b08c4-36f8-4ec2-bd10-123d7ddf09b0"
        },
        "request_id": "a37b08c4-36f8-4ec2-bd10-123d7ddf09b0",
        "response_json": {
          "content_id": "2c27184f-2a52-4750-8125-f959368be8fe",
          "creator_id": "cap-before-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 4: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.0008396250195801258,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "a37b08c4-36f8-4ec2-bd10-123d7ddf09b0",
        "timestamp": "2026-11-14T02:05:08.129666+00:00",
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
          "content_id": "2c27184f-2a52-4750-8125-f959368be8fe",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.227458,
        "cpu_seconds": 0.000213
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed appeal 5",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:05:08.129908+00:00",
        "request_json": {
          "content_id": "c427bab5-ce98-4b46-8ac2-d18ea34d1390",
          "reasoning": "  Capstone review 5: please consider my drafts.  "
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "311",
          "X-Request-ID": "9f46d08d-3902-4501-a1b1-988ce9bd3ae8"
        },
        "request_id": "9f46d08d-3902-4501-a1b1-988ce9bd3ae8",
        "response_json": {
          "content_id": "c427bab5-ce98-4b46-8ac2-d18ea34d1390",
          "creator_id": "cap-before-c3-t1-a1",
          "event": "appeal",
          "message": "Your appeal has been recorded. This writing is now under review.",
          "reasoning": "  Capstone review 5: please consider my drafts.  ",
          "status": "under_review",
          "timestamp": "2026-11-14T02:05:08+00:00"
        },
        "elapsed_seconds": 0.0008417093195021152,
        "request_body_bytes": 120
      },
      "completion": {
        "event": "request_completed",
        "request_id": "9f46d08d-3902-4501-a1b1-988ce9bd3ae8",
        "timestamp": "2026-11-14T02:05:08.130515+00:00",
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
          "content_id": "c427bab5-ce98-4b46-8ac2-d18ea34d1390",
          "status": "under_review",
          "outcome": "success"
        },
        "duration_ms": 0.239125,
        "cpu_seconds": 0.000231
      },
      "errors": [],
      "passed": true
    },
    {
      "http": {
        "name": "observed unknown appeal",
        "method": "POST",
        "path": "/appeal",
        "sent_at_utc": "2026-11-14T02:05:08.130755+00:00",
        "request_json": {
          "content_id": "00000000-0000-4000-8000-000000000099",
          "reasoning": "  Capstone review 99: please consider my drafts.  "
        },
        "status_code": 404,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:08 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "85",
          "X-Request-ID": "87a6f365-ae94-4b10-9de9-de439ff4a4b8"
        },
        "request_id": "87a6f365-ae94-4b10-9de9-de439ff4a4b8",
        "response_json": {
          "error": "content_not_found",
          "message": "No submission exists with this content_id."
        },
        "elapsed_seconds": 0.0008334997110068798,
        "request_body_bytes": 121
      },
      "completion": {
        "event": "request_completed",
        "request_id": "87a6f365-ae94-4b10-9de9-de439ff4a4b8",
        "timestamp": "2026-11-14T02:05:08.131372+00:00",
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
        "duration_ms": 0.236042,
        "cpu_seconds": 0.00023
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
  "evidence_directory": "results/capstone/before/c3_trial1_attempt1",
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
        "127.0.0.1:59373",
        "app:app"
      ],
      "pid": 74397,
      "started_at_utc": "2026-11-14T02:05:13.927229+00:00",
      "url": "http://127.0.0.1:59373",
      "log_directory": "results/capstone/before/c4_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c4_trial1_attempt1",
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
      "health_request_id": "b53ce0c2-6c9e-4d4e-8b3f-12a3f5fcad96",
      "cold_warmup": {
        "name": "disclosed cold-model warm-up",
        "method": "POST",
        "path": "/submit",
        "sent_at_utc": "2026-11-14T02:05:14.053464+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c4-t1-a1-warm"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "746",
          "X-Request-ID": "2c188df2-19c9-43c8-a29c-dd54de7d2ee7"
        },
        "request_id": "2c188df2-19c9-43c8-a29c-dd54de7d2ee7",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "54b73c88-01ca-4d10-94b9-5bf5bf664574",
          "creator_id": "cap-before-c4-t1-a1-warm",
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
          "timestamp": "2026-11-14T02:05:15+00:00"
        },
        "elapsed_seconds": 1.5754188331775367,
        "request_body_bytes": 431
      },
      "stopped_at_utc": "2026-11-14T02:05:16.558525+00:00",
      "returncode": 0
    }
  ],
  "cold_warmup": {
    "name": "disclosed cold-model warm-up",
    "method": "POST",
    "path": "/submit",
    "sent_at_utc": "2026-11-14T02:05:14.053464+00:00",
    "request_json": {
      "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
      "creator_id": "cap-before-c4-t1-a1-warm"
    },
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "746",
      "X-Request-ID": "2c188df2-19c9-43c8-a29c-dd54de7d2ee7"
    },
    "request_id": "2c188df2-19c9-43c8-a29c-dd54de7d2ee7",
    "response_json": {
      "combined_score": 0.6593,
      "confidence": 0.6593,
      "content_id": "54b73c88-01ca-4d10-94b9-5bf5bf664574",
      "creator_id": "cap-before-c4-t1-a1-warm",
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
      "timestamp": "2026-11-14T02:05:15+00:00"
    },
    "elapsed_seconds": 1.5754188331775367,
    "request_body_bytes": 431
  },
  "cases": [
    {
      "name": "warm timed human-01",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.628896+00:00",
      "request_json": {
        "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
        "creator_id": "cap-before-c4-t1-a1-human-01"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "750",
        "X-Request-ID": "095de458-c1b0-4120-bfc4-e3288678c2ee"
      },
      "request_id": "095de458-c1b0-4120-bfc4-e3288678c2ee",
      "response_json": {
        "combined_score": 0.6593,
        "confidence": 0.6593,
        "content_id": "d8d35d00-40e2-4ef5-950f-63dcdaba0d89",
        "creator_id": "cap-before-c4-t1-a1-human-01",
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
        "timestamp": "2026-11-14T02:05:15+00:00"
      },
      "elapsed_seconds": 0.04311654111370444,
      "request_body_bytes": 435
    },
    {
      "name": "warm timed human-02",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.672030+00:00",
      "request_json": {
        "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
        "creator_id": "cap-before-c4-t1-a1-human-02"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "763",
        "X-Request-ID": "d96f3dde-947d-4f0a-b10f-c5d92914dad6"
      },
      "request_id": "d96f3dde-947d-4f0a-b10f-c5d92914dad6",
      "response_json": {
        "combined_score": 0.4608,
        "confidence": 0.4608,
        "content_id": "ccfa0416-2c0a-4d8b-8a5c-ebe056799656",
        "creator_id": "cap-before-c4-t1-a1-human-02",
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
        "timestamp": "2026-11-14T02:05:15+00:00"
      },
      "elapsed_seconds": 0.0688141668215394,
      "request_body_bytes": 722
    },
    {
      "name": "warm timed human-03",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.740855+00:00",
      "request_json": {
        "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
        "creator_id": "cap-before-c4-t1-a1-human-03"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "752",
        "X-Request-ID": "d764a9a1-d3c5-479b-855f-06989745a376"
      },
      "request_id": "d764a9a1-d3c5-479b-855f-06989745a376",
      "response_json": {
        "combined_score": 0.3358,
        "confidence": 0.3358,
        "content_id": "7f350f81-9470-480d-9bb1-22e094d0e13f",
        "creator_id": "cap-before-c4-t1-a1-human-03",
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
        "timestamp": "2026-11-14T02:05:15+00:00"
      },
      "elapsed_seconds": 0.07999724987894297,
      "request_body_bytes": 873
    },
    {
      "name": "warm timed human-04",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.820870+00:00",
      "request_json": {
        "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
        "creator_id": "cap-before-c4-t1-a1-human-04"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "766",
        "X-Request-ID": "3c45cd4c-8665-41ff-aa79-6a961b542a71"
      },
      "request_id": "3c45cd4c-8665-41ff-aa79-6a961b542a71",
      "response_json": {
        "combined_score": 0.3954,
        "confidence": 0.3954,
        "content_id": "9635aca8-9659-4a98-8e9d-a53b846f4aa8",
        "creator_id": "cap-before-c4-t1-a1-human-04",
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
        "timestamp": "2026-11-14T02:05:15+00:00"
      },
      "elapsed_seconds": 0.06079066591337323,
      "request_body_bytes": 635
    },
    {
      "name": "warm timed human-05",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.881676+00:00",
      "request_json": {
        "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
        "creator_id": "cap-before-c4-t1-a1-human-05"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "750",
        "X-Request-ID": "61105841-fb70-457a-8e43-187e8323c7fa"
      },
      "request_id": "61105841-fb70-457a-8e43-187e8323c7fa",
      "response_json": {
        "combined_score": 0.6497,
        "confidence": 0.6497,
        "content_id": "38409e86-6a3c-4ed3-a4cb-a3b196cfd30c",
        "creator_id": "cap-before-c4-t1-a1-human-05",
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
        "timestamp": "2026-11-14T02:05:15+00:00"
      },
      "elapsed_seconds": 0.044863749761134386,
      "request_body_bytes": 412
    },
    {
      "name": "warm timed human-06",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.926557+00:00",
      "request_json": {
        "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
        "creator_id": "cap-before-c4-t1-a1-human-06"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:15 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "766",
        "X-Request-ID": "0f7d4c16-12f5-4a9a-b912-f718ec9a69b4"
      },
      "request_id": "0f7d4c16-12f5-4a9a-b912-f718ec9a69b4",
      "response_json": {
        "combined_score": 0.5545,
        "confidence": 0.5545,
        "content_id": "43ccd5e5-b69f-46d9-801a-5ec5c2dd3e36",
        "creator_id": "cap-before-c4-t1-a1-human-06",
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
        "timestamp": "2026-11-14T02:05:15+00:00"
      },
      "elapsed_seconds": 0.05022404156625271,
      "request_body_bytes": 559
    },
    {
      "name": "warm timed human-07",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:15.976793+00:00",
      "request_json": {
        "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
        "creator_id": "cap-before-c4-t1-a1-human-07"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:16 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "752",
        "X-Request-ID": "8749a361-2606-42c4-81be-19b9c7c85ffe"
      },
      "request_id": "8749a361-2606-42c4-81be-19b9c7c85ffe",
      "response_json": {
        "combined_score": 0.5606,
        "confidence": 0.5606,
        "content_id": "5df3ca7f-0225-4e0f-b232-da7afdddb21f",
        "creator_id": "cap-before-c4-t1-a1-human-07",
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
        "timestamp": "2026-11-14T02:05:16+00:00"
      },
      "elapsed_seconds": 0.06016983324661851,
      "request_body_bytes": 670
    },
    {
      "name": "warm timed human-08",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:16.036975+00:00",
      "request_json": {
        "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
        "creator_id": "cap-before-c4-t1-a1-human-08"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:16 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "765",
        "X-Request-ID": "3e58a35a-abdf-4872-b8cd-a3e4c72a1732"
      },
      "request_id": "3e58a35a-abdf-4872-b8cd-a3e4c72a1732",
      "response_json": {
        "combined_score": 0.5581,
        "confidence": 0.5581,
        "content_id": "649df9d6-3e65-4d5f-84de-7a93556b045e",
        "creator_id": "cap-before-c4-t1-a1-human-08",
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
        "timestamp": "2026-11-14T02:05:16+00:00"
      },
      "elapsed_seconds": 0.05453616613522172,
      "request_body_bytes": 671
    },
    {
      "name": "warm timed human-09",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:16.091522+00:00",
      "request_json": {
        "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
        "creator_id": "cap-before-c4-t1-a1-human-09"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:16 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "738",
        "X-Request-ID": "c3e76bb1-f8cb-45af-ad15-5ce15253c32a"
      },
      "request_id": "c3e76bb1-f8cb-45af-ad15-5ce15253c32a",
      "response_json": {
        "combined_score": 0.7081,
        "confidence": 0.7081,
        "content_id": "83d9ba8e-2bcd-44f4-ad14-555b8e08df60",
        "creator_id": "cap-before-c4-t1-a1-human-09",
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
        "timestamp": "2026-11-14T02:05:16+00:00"
      },
      "elapsed_seconds": 0.05202266667038202,
      "request_body_bytes": 582
    },
    {
      "name": "warm timed human-10",
      "method": "POST",
      "path": "/submit",
      "sent_at_utc": "2026-11-14T02:05:16.143556+00:00",
      "request_json": {
        "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
        "creator_id": "cap-before-c4-t1-a1-human-10"
      },
      "status_code": 200,
      "response_headers": {
        "Server": "gunicorn",
        "Date": "Sat, 14 Nov 2026 02:05:16 GMT",
        "Connection": "close",
        "Content-Type": "application/json",
        "Content-Length": "763",
        "X-Request-ID": "bf26441b-975f-4bdd-bc8f-386179b4f298"
      },
      "request_id": "bf26441b-975f-4bdd-bc8f-386179b4f298",
      "response_json": {
        "combined_score": 0.5475,
        "confidence": 0.5475,
        "content_id": "41a59b2f-65ef-47a5-8b85-fd919c98b76d",
        "creator_id": "cap-before-c4-t1-a1-human-10",
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
        "timestamp": "2026-11-14T02:05:16+00:00"
      },
      "elapsed_seconds": 0.06398366671055555,
      "request_body_bytes": 684
    }
  ],
  "valid_count": 10,
  "under5_seconds_count": 10,
  "mean_wall_seconds": 0.05785187478177249,
  "wall_seconds": [
    0.04311654111370444,
    0.0688141668215394,
    0.07999724987894297,
    0.06079066591337323,
    0.044863749761134386,
    0.05022404156625271,
    0.06016983324661851,
    0.05453616613522172,
    0.05202266667038202,
    0.06398366671055555
  ],
  "cpu_seconds": [
    0.057343,
    0.107554,
    0.122621,
    0.090131,
    0.0605,
    0.07067,
    0.088362,
    0.079342,
    0.073219,
    0.094192
  ],
  "mean_cpu_seconds": 0.0843934,
  "cost_measurement_errors": [],
  "request_log_parse_errors": [],
  "quota_window_valid": true,
  "http_passed": true,
  "summary": "10/10 decisions; 10/10<5s; mean0.0579s",
  "trial": 1,
  "attempt": 1,
  "criterion": 4,
  "evidence_directory": "results/capstone/before/c4_trial1_attempt1",
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
        "127.0.0.1:59418",
        "app:app"
      ],
      "pid": 74421,
      "started_at_utc": "2026-11-14T02:05:21.866523+00:00",
      "url": "http://127.0.0.1:59418",
      "log_directory": "results/capstone/before/c5_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c5_trial1_attempt1",
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
      "health_request_id": "b5e250aa-e97d-4c06-968e-b0faec246ae0",
      "stopped_at_utc": "2026-11-14T02:05:25.219789+00:00",
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
        "127.0.0.1:59446",
        "app:app"
      ],
      "pid": 74476,
      "started_at_utc": "2026-11-14T02:05:25.222464+00:00",
      "url": "http://127.0.0.1:59446",
      "log_directory": "results/capstone/before/c5_trial1_attempt1",
      "environment_overrides": {
        "AI201_LOG_DIR": "/Users/amarsawant/Downloads/Codepath/AI 201/ai201-project4-provenance-guard-starter-v2026/results/capstone/before/c5_trial1_attempt1",
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
      "health_request_id": "e8bf119c-edd5-40e6-b205-4002384723cf",
      "stopped_at_utc": "2026-11-14T02:05:25.570505+00:00",
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
        "sent_at_utc": "2026-11-14T02:05:21.984184+00:00",
        "request_json": {
          "text": "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters.",
          "creator_id": "cap-before-c5-t1-a1-human-01"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:23 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "750",
          "X-Request-ID": "4122c76a-acdf-4ce1-a686-1ea441917749"
        },
        "request_id": "4122c76a-acdf-4ce1-a686-1ea441917749",
        "response_json": {
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
          "creator_id": "cap-before-c5-t1-a1-human-01",
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
          "timestamp": "2026-11-14T02:05:23+00:00"
        },
        "elapsed_seconds": 1.7930461666546762,
        "request_body_bytes": 435
      },
      "appeal": {
        "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
        "reasoning": "  Capstone review 1: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 1",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.642311+00:00",
          "request_json": {
            "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
            "reasoning": "  Capstone review 1: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "bb767097-57f9-4901-9efb-6fa5bfddba64"
          },
          "request_id": "bb767097-57f9-4901-9efb-6fa5bfddba64",
          "response_json": {
            "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
            "creator_id": "cap-before-c5-t1-a1-human-01",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 1: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0026072501204907894,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 1",
        "method": "GET",
        "path": "/content/23706e24-26fa-4ac4-ae8c-7dedc0951a30",
        "sent_at_utc": "2026-11-14T02:05:25.433631+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1010",
          "X-Request-ID": "daaaa2df-6282-4dfe-bfc0-3effdabac59d"
        },
        "request_id": "daaaa2df-6282-4dfe-bfc0-3effdabac59d",
        "response_json": {
          "appeals": [
            {
              "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
              "creator_id": "cap-before-c5-t1-a1-human-01",
              "event": "appeal",
              "reasoning": "  Capstone review 1: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.6593,
          "confidence": 0.6593,
          "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
          "creator_id": "cap-before-c5-t1-a1-human-01",
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
          "timestamp": "2026-11-14T02:05:23+00:00"
        },
        "elapsed_seconds": 0.0010995417833328247,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:23+00:00",
        "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
        "creator_id": "cap-before-c5-t1-a1-human-01",
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
          "timestamp": "2026-11-14T02:05:23+00:00",
          "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
          "creator_id": "cap-before-c5-t1-a1-human-01",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
          "creator_id": "cap-before-c5-t1-a1-human-01",
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
        "sent_at_utc": "2026-11-14T02:05:23.777218+00:00",
        "request_json": {
          "text": "There was no possibility of taking a walk that day. We had been wandering, indeed, in the leafless shrubbery an hour in the morning; but since dinner (Mrs. Reed, when there was no company, dined early) the cold winter wind had brought with it clouds so sombre, and a rain so penetrating, that further outdoor exercise was now out of the question. I was glad of it: I never liked long walks, especially on chilly afternoons: dreadful to me was the coming home in the raw twilight, with nipped fingers and toes, and a heart saddened by the chidings of Bessie, the nurse, and humbled by the consciousness of my physical inferiority to Eliza, John, and Georgiana Reed.",
          "creator_id": "cap-before-c5-t1-a1-human-02"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:23 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "763",
          "X-Request-ID": "06c5e26d-7d9e-4914-9689-d781f7749f2c"
        },
        "request_id": "06c5e26d-7d9e-4914-9689-d781f7749f2c",
        "response_json": {
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "f537c753-b876-4891-8094-95324f803aa4",
          "creator_id": "cap-before-c5-t1-a1-human-02",
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
          "timestamp": "2026-11-14T02:05:23+00:00"
        },
        "elapsed_seconds": 0.0879497081041336,
        "request_body_bytes": 722
      },
      "appeal": {
        "content_id": "f537c753-b876-4891-8094-95324f803aa4",
        "reasoning": "  Capstone review 2: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 2",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.644932+00:00",
          "request_json": {
            "content_id": "f537c753-b876-4891-8094-95324f803aa4",
            "reasoning": "  Capstone review 2: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "44c7350e-b26d-4063-b90d-0f3b470f2b12"
          },
          "request_id": "44c7350e-b26d-4063-b90d-0f3b470f2b12",
          "response_json": {
            "content_id": "f537c753-b876-4891-8094-95324f803aa4",
            "creator_id": "cap-before-c5-t1-a1-human-02",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 2: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0014204583130776882,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 2",
        "method": "GET",
        "path": "/content/f537c753-b876-4891-8094-95324f803aa4",
        "sent_at_utc": "2026-11-14T02:05:25.434744+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1023",
          "X-Request-ID": "a0554540-edaf-43f8-87be-6ef5eb7a3fa0"
        },
        "request_id": "a0554540-edaf-43f8-87be-6ef5eb7a3fa0",
        "response_json": {
          "appeals": [
            {
              "content_id": "f537c753-b876-4891-8094-95324f803aa4",
              "creator_id": "cap-before-c5-t1-a1-human-02",
              "event": "appeal",
              "reasoning": "  Capstone review 2: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.4608,
          "confidence": 0.4608,
          "content_id": "f537c753-b876-4891-8094-95324f803aa4",
          "creator_id": "cap-before-c5-t1-a1-human-02",
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
          "timestamp": "2026-11-14T02:05:23+00:00"
        },
        "elapsed_seconds": 0.0008689588867127895,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:23+00:00",
        "content_id": "f537c753-b876-4891-8094-95324f803aa4",
        "creator_id": "cap-before-c5-t1-a1-human-02",
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
          "timestamp": "2026-11-14T02:05:23+00:00",
          "content_id": "f537c753-b876-4891-8094-95324f803aa4",
          "creator_id": "cap-before-c5-t1-a1-human-02",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "f537c753-b876-4891-8094-95324f803aa4",
          "creator_id": "cap-before-c5-t1-a1-human-02",
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
        "sent_at_utc": "2026-11-14T02:05:23.865186+00:00",
        "request_json": {
          "text": "Call me Ishmael. Some years ago\u2014never mind how long precisely\u2014having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\u2019s hats off\u2014then, I account it high time to get to sea as soon as I can.",
          "creator_id": "cap-before-c5-t1-a1-human-03"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:23 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "752",
          "X-Request-ID": "8769e35c-f59b-45cd-8555-f5e7a59ae8f2"
        },
        "request_id": "8769e35c-f59b-45cd-8555-f5e7a59ae8f2",
        "response_json": {
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
          "creator_id": "cap-before-c5-t1-a1-human-03",
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
          "timestamp": "2026-11-14T02:05:23+00:00"
        },
        "elapsed_seconds": 0.08862991724163294,
        "request_body_bytes": 873
      },
      "appeal": {
        "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
        "reasoning": "  Capstone review 3: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 3",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.646364+00:00",
          "request_json": {
            "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
            "reasoning": "  Capstone review 3: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "b3489f78-37ca-4e31-a44b-6be9f01e6d85"
          },
          "request_id": "b3489f78-37ca-4e31-a44b-6be9f01e6d85",
          "response_json": {
            "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
            "creator_id": "cap-before-c5-t1-a1-human-03",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 3: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.001064457930624485,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 3",
        "method": "GET",
        "path": "/content/5d030954-9227-4352-82da-dbcadb72b1e0",
        "sent_at_utc": "2026-11-14T02:05:25.435625+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1012",
          "X-Request-ID": "3313150a-c9cf-4c24-9e7d-ea0eea9c2107"
        },
        "request_id": "3313150a-c9cf-4c24-9e7d-ea0eea9c2107",
        "response_json": {
          "appeals": [
            {
              "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
              "creator_id": "cap-before-c5-t1-a1-human-03",
              "event": "appeal",
              "reasoning": "  Capstone review 3: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.3358,
          "confidence": 0.3358,
          "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
          "creator_id": "cap-before-c5-t1-a1-human-03",
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
          "timestamp": "2026-11-14T02:05:23+00:00"
        },
        "elapsed_seconds": 0.0007869591936469078,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:23+00:00",
        "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
        "creator_id": "cap-before-c5-t1-a1-human-03",
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
          "timestamp": "2026-11-14T02:05:23+00:00",
          "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
          "creator_id": "cap-before-c5-t1-a1-human-03",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "5d030954-9227-4352-82da-dbcadb72b1e0",
          "creator_id": "cap-before-c5-t1-a1-human-03",
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
        "sent_at_utc": "2026-11-14T02:05:23.953834+00:00",
        "request_json": {
          "text": "You don\u2019t know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain\u2019t no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly\u2014Tom\u2019s Aunt Polly, she is\u2014and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.",
          "creator_id": "cap-before-c5-t1-a1-human-04"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "766",
          "X-Request-ID": "35c714cf-dde3-433a-ae92-6022fa81f963"
        },
        "request_id": "35c714cf-dde3-433a-ae92-6022fa81f963",
        "response_json": {
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
          "creator_id": "cap-before-c5-t1-a1-human-04",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.09244608273729682,
        "request_body_bytes": 635
      },
      "appeal": {
        "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
        "reasoning": "  Capstone review 4: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 4",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.647439+00:00",
          "request_json": {
            "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
            "reasoning": "  Capstone review 4: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "64bfe8c2-b56a-46dd-a4d2-1a2a50d83562"
          },
          "request_id": "64bfe8c2-b56a-46dd-a4d2-1a2a50d83562",
          "response_json": {
            "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
            "creator_id": "cap-before-c5-t1-a1-human-04",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 4: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0011374996975064278,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 4",
        "method": "GET",
        "path": "/content/eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
        "sent_at_utc": "2026-11-14T02:05:25.436419+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1026",
          "X-Request-ID": "1889c0df-512b-42de-a478-fb9128d9a87e"
        },
        "request_id": "1889c0df-512b-42de-a478-fb9128d9a87e",
        "response_json": {
          "appeals": [
            {
              "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
              "creator_id": "cap-before-c5-t1-a1-human-04",
              "event": "appeal",
              "reasoning": "  Capstone review 4: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.3954,
          "confidence": 0.3954,
          "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
          "creator_id": "cap-before-c5-t1-a1-human-04",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0008180001750588417,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
        "creator_id": "cap-before-c5-t1-a1-human-04",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
          "creator_id": "cap-before-c5-t1-a1-human-04",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "eb83e80c-0d3d-4b3d-8816-3e8a9c554068",
          "creator_id": "cap-before-c5-t1-a1-human-04",
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
        "sent_at_utc": "2026-11-14T02:05:24.046300+00:00",
        "request_json": {
          "text": "When I wrote the following pages, or rather the bulk of them, I lived alone, in the woods, a mile from any neighbor, in a house which I had built myself, on the shore of Walden Pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.",
          "creator_id": "cap-before-c5-t1-a1-human-05"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "750",
          "X-Request-ID": "16665b8d-e87c-477c-8e6c-374ab05494f8"
        },
        "request_id": "16665b8d-e87c-477c-8e6c-374ab05494f8",
        "response_json": {
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
          "creator_id": "cap-before-c5-t1-a1-human-05",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.13765104115009308,
        "request_body_bytes": 412
      },
      "appeal": {
        "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
        "reasoning": "  Capstone review 5: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 5",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.648585+00:00",
          "request_json": {
            "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
            "reasoning": "  Capstone review 5: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "591ec3e0-9afb-4f83-a0b7-522e66234c8d"
          },
          "request_id": "591ec3e0-9afb-4f83-a0b7-522e66234c8d",
          "response_json": {
            "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
            "creator_id": "cap-before-c5-t1-a1-human-05",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 5: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0010331249795854092,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 5",
        "method": "GET",
        "path": "/content/7835d727-1547-439a-add4-3d08ccb5e50b",
        "sent_at_utc": "2026-11-14T02:05:25.437244+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1010",
          "X-Request-ID": "7ec379ea-9220-41e6-aa2c-10734fb2c726"
        },
        "request_id": "7ec379ea-9220-41e6-aa2c-10734fb2c726",
        "response_json": {
          "appeals": [
            {
              "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
              "creator_id": "cap-before-c5-t1-a1-human-05",
              "event": "appeal",
              "reasoning": "  Capstone review 5: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.6497,
          "confidence": 0.6497,
          "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
          "creator_id": "cap-before-c5-t1-a1-human-05",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0008812076412141323,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
        "creator_id": "cap-before-c5-t1-a1-human-05",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
          "creator_id": "cap-before-c5-t1-a1-human-05",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "7835d727-1547-439a-add4-3d08ccb5e50b",
          "creator_id": "cap-before-c5-t1-a1-human-05",
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
        "sent_at_utc": "2026-11-14T02:05:24.183963+00:00",
        "request_json": {
          "text": "You will rejoice to hear that no disaster has accompanied the commencement of an enterprise which you have regarded with such evil forebodings. I arrived here yesterday, and my first task is to assure my dear sister of my welfare and increasing confidence in the success of my undertaking. I am already far north of London, and as I walk in the streets of Petersburgh, I feel a cold northern breeze play upon my cheeks, which braces my nerves and fills me with delight. Do you understand this feeling?",
          "creator_id": "cap-before-c5-t1-a1-human-06"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "766",
          "X-Request-ID": "16016817-cb34-45d0-bcfc-8999078921f6"
        },
        "request_id": "16016817-cb34-45d0-bcfc-8999078921f6",
        "response_json": {
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
          "creator_id": "cap-before-c5-t1-a1-human-06",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.060439458116889,
        "request_body_bytes": 559
      },
      "appeal": {
        "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
        "reasoning": "  Capstone review 6: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 6",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.649627+00:00",
          "request_json": {
            "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
            "reasoning": "  Capstone review 6: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "e5b93d1c-3d94-4e28-a309-0014567e1182"
          },
          "request_id": "e5b93d1c-3d94-4e28-a309-0014567e1182",
          "response_json": {
            "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
            "creator_id": "cap-before-c5-t1-a1-human-06",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 6: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0009145420044660568,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 6",
        "method": "GET",
        "path": "/content/bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
        "sent_at_utc": "2026-11-14T02:05:25.438131+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1026",
          "X-Request-ID": "b8c9cf84-3a50-4cb8-bd31-9c41f1db4c43"
        },
        "request_id": "b8c9cf84-3a50-4cb8-bd31-9c41f1db4c43",
        "response_json": {
          "appeals": [
            {
              "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
              "creator_id": "cap-before-c5-t1-a1-human-06",
              "event": "appeal",
              "reasoning": "  Capstone review 6: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.5545,
          "confidence": 0.5545,
          "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
          "creator_id": "cap-before-c5-t1-a1-human-06",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0009016245603561401,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
        "creator_id": "cap-before-c5-t1-a1-human-06",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
          "creator_id": "cap-before-c5-t1-a1-human-06",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "bf3d4b44-1322-49d2-9f1e-9c50a9f99131",
          "creator_id": "cap-before-c5-t1-a1-human-06",
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
        "sent_at_utc": "2026-11-14T02:05:24.244414+00:00",
        "request_json": {
          "text": "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \u201cand what is the use of a book,\u201d thought Alice \u201cwithout pictures or conversations?\u201d So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.",
          "creator_id": "cap-before-c5-t1-a1-human-07"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "752",
          "X-Request-ID": "32155c15-2c4d-4c4b-a0c0-4117d4dba3eb"
        },
        "request_id": "32155c15-2c4d-4c4b-a0c0-4117d4dba3eb",
        "response_json": {
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
          "creator_id": "cap-before-c5-t1-a1-human-07",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.09963904228061438,
        "request_body_bytes": 670
      },
      "appeal": {
        "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
        "reasoning": "  Capstone review 7: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 7",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.650548+00:00",
          "request_json": {
            "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
            "reasoning": "  Capstone review 7: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "20e9096e-d565-4675-beb6-0e6c75d80133"
          },
          "request_id": "20e9096e-d565-4675-beb6-0e6c75d80133",
          "response_json": {
            "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
            "creator_id": "cap-before-c5-t1-a1-human-07",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 7: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0009006666950881481,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 7",
        "method": "GET",
        "path": "/content/7650a551-a8a7-4d3b-b2c9-688459561157",
        "sent_at_utc": "2026-11-14T02:05:25.439040+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1012",
          "X-Request-ID": "a3258592-bb41-4d18-a5b5-53fc2b44bdaf"
        },
        "request_id": "a3258592-bb41-4d18-a5b5-53fc2b44bdaf",
        "response_json": {
          "appeals": [
            {
              "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
              "creator_id": "cap-before-c5-t1-a1-human-07",
              "event": "appeal",
              "reasoning": "  Capstone review 7: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.5606,
          "confidence": 0.5606,
          "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
          "creator_id": "cap-before-c5-t1-a1-human-07",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0013993331231176853,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
        "creator_id": "cap-before-c5-t1-a1-human-07",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
          "creator_id": "cap-before-c5-t1-a1-human-07",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "7650a551-a8a7-4d3b-b2c9-688459561157",
          "creator_id": "cap-before-c5-t1-a1-human-07",
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
        "sent_at_utc": "2026-11-14T02:05:24.344073+00:00",
        "request_json": {
          "text": "When on board H.M.S. \u2018Beagle,\u2019 as naturalist, I was much struck with certain facts in the distribution of the inhabitants of South America, and in the geological relations of the present to the past inhabitants of that continent. These facts seemed to me to throw some light on the origin of species\u2014that mystery of mysteries, as it has been called by one of our greatest philosophers. On my return home, it occurred to me, in 1837, that something might perhaps be made out on this question by patiently accumulating and reflecting on all sorts of facts which could possibly have any bearing on it.",
          "creator_id": "cap-before-c5-t1-a1-human-08"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "765",
          "X-Request-ID": "0c144632-8b3a-49ae-a909-7afe0b125cfd"
        },
        "request_id": "0c144632-8b3a-49ae-a909-7afe0b125cfd",
        "response_json": {
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
          "creator_id": "cap-before-c5-t1-a1-human-08",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0844744578935206,
        "request_body_bytes": 671
      },
      "appeal": {
        "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
        "reasoning": "  Capstone review 8: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 8",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.651456+00:00",
          "request_json": {
            "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
            "reasoning": "  Capstone review 8: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "2f3ce683-ac6c-4733-b9b6-8b8c9623fdb8"
          },
          "request_id": "2f3ce683-ac6c-4733-b9b6-8b8c9623fdb8",
          "response_json": {
            "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
            "creator_id": "cap-before-c5-t1-a1-human-08",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 8: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0009249169379472733,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 8",
        "method": "GET",
        "path": "/content/f2a81832-dacd-4131-b974-b8f4e9d8664c",
        "sent_at_utc": "2026-11-14T02:05:25.440450+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1025",
          "X-Request-ID": "5af8e5f6-4337-47a4-ad75-c87a2c4a8651"
        },
        "request_id": "5af8e5f6-4337-47a4-ad75-c87a2c4a8651",
        "response_json": {
          "appeals": [
            {
              "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
              "creator_id": "cap-before-c5-t1-a1-human-08",
              "event": "appeal",
              "reasoning": "  Capstone review 8: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.5581,
          "confidence": 0.5581,
          "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
          "creator_id": "cap-before-c5-t1-a1-human-08",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0016380422748625278,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
        "creator_id": "cap-before-c5-t1-a1-human-08",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
          "creator_id": "cap-before-c5-t1-a1-human-08",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "f2a81832-dacd-4131-b974-b8f4e9d8664c",
          "creator_id": "cap-before-c5-t1-a1-human-08",
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
        "sent_at_utc": "2026-11-14T02:05:24.428571+00:00",
        "request_json": {
          "text": "The produce of industry is what it adds to the subject or materials upon which it is employed. In proportion as the value of this produce is great or small, so will likewise be the profits of the employer. But it is only for the sake of profit that any man employs a capital in the support of industry; and he will always, therefore, endeavour to employ it in the support of that industry of which the produce is likely to be of the greatest value, or to exchange for the greatest quantity either of money or of other goods.",
          "creator_id": "cap-before-c5-t1-a1-human-09"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "738",
          "X-Request-ID": "01011fd0-7e60-4098-9336-9025ef806b80"
        },
        "request_id": "01011fd0-7e60-4098-9336-9025ef806b80",
        "response_json": {
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
          "creator_id": "cap-before-c5-t1-a1-human-09",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.09896579198539257,
        "request_body_bytes": 582
      },
      "appeal": {
        "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
        "reasoning": "  Capstone review 9: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 9",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.652390+00:00",
          "request_json": {
            "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
            "reasoning": "  Capstone review 9: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "320",
            "X-Request-ID": "bc4abc36-0247-43b7-9fa8-45049282fb8c"
          },
          "request_id": "bc4abc36-0247-43b7-9fa8-45049282fb8c",
          "response_json": {
            "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
            "creator_id": "cap-before-c5-t1-a1-human-09",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 9: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.000987000297755003,
          "request_body_bytes": 120
        }
      },
      "lookup": {
        "name": "persisted lookup 9",
        "method": "GET",
        "path": "/content/9042b763-e184-47e8-b757-b37740359ff2",
        "sent_at_utc": "2026-11-14T02:05:25.442103+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "998",
          "X-Request-ID": "d13a4e30-0d8b-4fb3-bbd6-624d21a7ee2e"
        },
        "request_id": "d13a4e30-0d8b-4fb3-bbd6-624d21a7ee2e",
        "response_json": {
          "appeals": [
            {
              "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
              "creator_id": "cap-before-c5-t1-a1-human-09",
              "event": "appeal",
              "reasoning": "  Capstone review 9: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.7081,
          "confidence": 0.7081,
          "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
          "creator_id": "cap-before-c5-t1-a1-human-09",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.001894333865493536,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
        "creator_id": "cap-before-c5-t1-a1-human-09",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
          "creator_id": "cap-before-c5-t1-a1-human-09",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "9042b763-e184-47e8-b757-b37740359ff2",
          "creator_id": "cap-before-c5-t1-a1-human-09",
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
        "sent_at_utc": "2026-11-14T02:05:24.527548+00:00",
        "request_json": {
          "text": "My elder brothers were all put apprentices to different trades. I was put to the grammar-school at eight years of age, my father intending to devote me, as the tithe[13] of his sons, to the service of the Church. My early readiness in learning to read (which must have been very early, as I do not remember when I could not read), and the opinion of all his friends, that I should certainly make a good scholar, encouraged him in this purpose of his. My uncle Benjamin, too, approved of it, and proposed to give me all his short-hand volumes of sermons, I suppose as a stock to set up with, if I would learn his character.[14]",
          "creator_id": "cap-before-c5-t1-a1-human-10"
        },
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "763",
          "X-Request-ID": "2351efe0-4eb6-4148-8a61-c445a8dac197"
        },
        "request_id": "2351efe0-4eb6-4148-8a61-c445a8dac197",
        "response_json": {
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
          "creator_id": "cap-before-c5-t1-a1-human-10",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.11449299985542893,
        "request_body_bytes": 684
      },
      "appeal": {
        "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
        "reasoning": "  Capstone review 10: please consider my drafts.  ",
        "http": {
          "name": "exact appeal 10",
          "method": "POST",
          "path": "/appeal",
          "sent_at_utc": "2026-11-14T02:05:24.653386+00:00",
          "request_json": {
            "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
            "reasoning": "  Capstone review 10: please consider my drafts.  "
          },
          "status_code": 200,
          "response_headers": {
            "Server": "gunicorn",
            "Date": "Sat, 14 Nov 2026 02:05:24 GMT",
            "Connection": "close",
            "Content-Type": "application/json",
            "Content-Length": "321",
            "X-Request-ID": "9b902df1-8b53-4ccf-8160-2e8fafb92ff4"
          },
          "request_id": "9b902df1-8b53-4ccf-8160-2e8fafb92ff4",
          "response_json": {
            "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
            "creator_id": "cap-before-c5-t1-a1-human-10",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 10: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:24+00:00"
          },
          "elapsed_seconds": 0.0018463749438524246,
          "request_body_bytes": 121
        }
      },
      "lookup": {
        "name": "persisted lookup 10",
        "method": "GET",
        "path": "/content/b297c406-96c2-402f-b25e-1155f41fcf85",
        "sent_at_utc": "2026-11-14T02:05:25.444009+00:00",
        "status_code": 200,
        "response_headers": {
          "Server": "gunicorn",
          "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
          "Connection": "close",
          "Content-Type": "application/json",
          "Content-Length": "1024",
          "X-Request-ID": "90e1857d-0265-41ca-a920-a6f50f87f235"
        },
        "request_id": "90e1857d-0265-41ca-a920-a6f50f87f235",
        "response_json": {
          "appeals": [
            {
              "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
              "creator_id": "cap-before-c5-t1-a1-human-10",
              "event": "appeal",
              "reasoning": "  Capstone review 10: please consider my drafts.  ",
              "status": "under_review",
              "timestamp": "2026-11-14T02:05:24+00:00"
            }
          ],
          "combined_score": 0.5475,
          "confidence": 0.5475,
          "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
          "creator_id": "cap-before-c5-t1-a1-human-10",
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
          "timestamp": "2026-11-14T02:05:24+00:00"
        },
        "elapsed_seconds": 0.0011772499419748783,
        "request_body_bytes": 0
      },
      "original": {
        "timestamp": "2026-11-14T02:05:24+00:00",
        "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
        "creator_id": "cap-before-c5-t1-a1-human-10",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
          "creator_id": "cap-before-c5-t1-a1-human-10",
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
          "timestamp": "2026-11-14T02:05:24+00:00",
          "content_id": "b297c406-96c2-402f-b25e-1155f41fcf85",
          "creator_id": "cap-before-c5-t1-a1-human-10",
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
    "sent_at_utc": "2026-11-14T02:05:25.445214+00:00",
    "request_json": {
      "content_id": "00000000-0000-4000-8000-000000000099",
      "reasoning": "  Capstone review 99: please consider my drafts.  "
    },
    "status_code": 404,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "85",
      "X-Request-ID": "20a5e18a-b811-423c-9ec8-c15dc8d8944c"
    },
    "request_id": "20a5e18a-b811-423c-9ec8-c15dc8d8944c",
    "response_json": {
      "error": "content_not_found",
      "message": "No submission exists with this content_id."
    },
    "elapsed_seconds": 0.001186625100672245,
    "request_body_bytes": 121
  },
  "unknown_id_passed": true,
  "original_audit_bytes_sha256": "597a78b8716102ce470121f7df16659ff5fcd105c6727548f2eb71cd77763626",
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
    "sent_at_utc": "2026-11-14T02:05:25.446411+00:00",
    "status_code": 200,
    "response_headers": {
      "Server": "gunicorn",
      "Date": "Sat, 14 Nov 2026 02:05:25 GMT",
      "Connection": "close",
      "Content-Type": "application/json",
      "Content-Length": "98",
      "X-Request-ID": "4bf41c67-f183-4b2a-a5ca-85b6cf8f5b62"
    },
    "request_id": "4bf41c67-f183-4b2a-a5ca-85b6cf8f5b62",
    "response_json": {
      "detector_loaded": false,
      "detector_model": "gpt2",
      "log_entries": 21,
      "ok": true,
      "rate_limiting": true
    },
    "elapsed_seconds": 0.0007982919923961163,
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
  "evidence_directory": "results/capstone/before/c5_trial1_attempt1",
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
            "content_id": "c5045306-5fd7-4aee-8a0d-f427161ecaa8",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5518,
            "confidence": 0.5518,
            "content_id": "5cc486d8-f3ea-4d73-97c8-f9ae17bab3ee",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5332,
            "confidence": 0.5332,
            "content_id": "bb725d2c-12ab-489a-b2d8-116ec9628a3b",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5476,
            "confidence": 0.5476,
            "content_id": "90224bc6-b7b9-4aec-a39a-b879276068dd",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5236,
            "confidence": 0.5236,
            "content_id": "b7848c40-3bee-43cf-9482-16fd01d0c9bb",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5682,
            "confidence": 0.5682,
            "content_id": "7fd2a363-933e-46a6-a87d-8300df11459c",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.581,
            "confidence": 0.581,
            "content_id": "1cc84833-c7aa-43b4-99fc-dd270a572468",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5721,
            "confidence": 0.5721,
            "content_id": "61890ac7-d46c-4e33-b46f-3d3a45a0575b",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5762,
            "confidence": 0.5762,
            "content_id": "dab8c0ff-8863-45ef-b6d6-facccc9b3ea5",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "combined_score": 0.5747,
            "confidence": 0.5747,
            "content_id": "ac726df9-a9a1-43c7-bacf-fd3b3810cd57",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        }
      ],
      "appeals": [
        {
          "status_code": 200,
          "response_json": {
            "content_id": "c5045306-5fd7-4aee-8a0d-f427161ecaa8",
            "creator_id": "mocked-c5-1",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 1: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "5cc486d8-f3ea-4d73-97c8-f9ae17bab3ee",
            "creator_id": "mocked-c5-2",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 2: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "bb725d2c-12ab-489a-b2d8-116ec9628a3b",
            "creator_id": "mocked-c5-3",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 3: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "90224bc6-b7b9-4aec-a39a-b879276068dd",
            "creator_id": "mocked-c5-4",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 4: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "b7848c40-3bee-43cf-9482-16fd01d0c9bb",
            "creator_id": "mocked-c5-5",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 5: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "7fd2a363-933e-46a6-a87d-8300df11459c",
            "creator_id": "mocked-c5-6",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 6: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "1cc84833-c7aa-43b4-99fc-dd270a572468",
            "creator_id": "mocked-c5-7",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 7: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "61890ac7-d46c-4e33-b46f-3d3a45a0575b",
            "creator_id": "mocked-c5-8",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 8: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "dab8c0ff-8863-45ef-b6d6-facccc9b3ea5",
            "creator_id": "mocked-c5-9",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 9: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "content_id": "ac726df9-a9a1-43c7-bacf-fd3b3810cd57",
            "creator_id": "mocked-c5-10",
            "event": "appeal",
            "message": "Your appeal has been recorded. This writing is now under review.",
            "reasoning": "  Capstone review 10: please consider my drafts.  ",
            "status": "under_review",
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        }
      ],
      "lookups": [
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "c5045306-5fd7-4aee-8a0d-f427161ecaa8",
                "creator_id": "mocked-c5-1",
                "event": "appeal",
                "reasoning": "  Capstone review 1: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "c5045306-5fd7-4aee-8a0d-f427161ecaa8",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "5cc486d8-f3ea-4d73-97c8-f9ae17bab3ee",
                "creator_id": "mocked-c5-2",
                "event": "appeal",
                "reasoning": "  Capstone review 2: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5518,
            "confidence": 0.5518,
            "content_id": "5cc486d8-f3ea-4d73-97c8-f9ae17bab3ee",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "bb725d2c-12ab-489a-b2d8-116ec9628a3b",
                "creator_id": "mocked-c5-3",
                "event": "appeal",
                "reasoning": "  Capstone review 3: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5332,
            "confidence": 0.5332,
            "content_id": "bb725d2c-12ab-489a-b2d8-116ec9628a3b",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "90224bc6-b7b9-4aec-a39a-b879276068dd",
                "creator_id": "mocked-c5-4",
                "event": "appeal",
                "reasoning": "  Capstone review 4: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5476,
            "confidence": 0.5476,
            "content_id": "90224bc6-b7b9-4aec-a39a-b879276068dd",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "b7848c40-3bee-43cf-9482-16fd01d0c9bb",
                "creator_id": "mocked-c5-5",
                "event": "appeal",
                "reasoning": "  Capstone review 5: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5236,
            "confidence": 0.5236,
            "content_id": "b7848c40-3bee-43cf-9482-16fd01d0c9bb",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "7fd2a363-933e-46a6-a87d-8300df11459c",
                "creator_id": "mocked-c5-6",
                "event": "appeal",
                "reasoning": "  Capstone review 6: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5682,
            "confidence": 0.5682,
            "content_id": "7fd2a363-933e-46a6-a87d-8300df11459c",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "1cc84833-c7aa-43b4-99fc-dd270a572468",
                "creator_id": "mocked-c5-7",
                "event": "appeal",
                "reasoning": "  Capstone review 7: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.581,
            "confidence": 0.581,
            "content_id": "1cc84833-c7aa-43b4-99fc-dd270a572468",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "61890ac7-d46c-4e33-b46f-3d3a45a0575b",
                "creator_id": "mocked-c5-8",
                "event": "appeal",
                "reasoning": "  Capstone review 8: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5721,
            "confidence": 0.5721,
            "content_id": "61890ac7-d46c-4e33-b46f-3d3a45a0575b",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "dab8c0ff-8863-45ef-b6d6-facccc9b3ea5",
                "creator_id": "mocked-c5-9",
                "event": "appeal",
                "reasoning": "  Capstone review 9: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5762,
            "confidence": 0.5762,
            "content_id": "dab8c0ff-8863-45ef-b6d6-facccc9b3ea5",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          }
        },
        {
          "status_code": 200,
          "response_json": {
            "appeals": [
              {
                "content_id": "ac726df9-a9a1-43c7-bacf-fd3b3810cd57",
                "creator_id": "mocked-c5-10",
                "event": "appeal",
                "reasoning": "  Capstone review 10: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5747,
            "confidence": 0.5747,
            "content_id": "ac726df9-a9a1-43c7-bacf-fd3b3810cd57",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
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
                "content_id": "c5045306-5fd7-4aee-8a0d-f427161ecaa8",
                "creator_id": "mocked-c5-1",
                "event": "appeal",
                "reasoning": "  Capstone review 1: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5856,
            "confidence": 0.5856,
            "content_id": "c5045306-5fd7-4aee-8a0d-f427161ecaa8",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "5cc486d8-f3ea-4d73-97c8-f9ae17bab3ee",
                "creator_id": "mocked-c5-2",
                "event": "appeal",
                "reasoning": "  Capstone review 2: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5518,
            "confidence": 0.5518,
            "content_id": "5cc486d8-f3ea-4d73-97c8-f9ae17bab3ee",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "bb725d2c-12ab-489a-b2d8-116ec9628a3b",
                "creator_id": "mocked-c5-3",
                "event": "appeal",
                "reasoning": "  Capstone review 3: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5332,
            "confidence": 0.5332,
            "content_id": "bb725d2c-12ab-489a-b2d8-116ec9628a3b",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "90224bc6-b7b9-4aec-a39a-b879276068dd",
                "creator_id": "mocked-c5-4",
                "event": "appeal",
                "reasoning": "  Capstone review 4: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5476,
            "confidence": 0.5476,
            "content_id": "90224bc6-b7b9-4aec-a39a-b879276068dd",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "b7848c40-3bee-43cf-9482-16fd01d0c9bb",
                "creator_id": "mocked-c5-5",
                "event": "appeal",
                "reasoning": "  Capstone review 5: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5236,
            "confidence": 0.5236,
            "content_id": "b7848c40-3bee-43cf-9482-16fd01d0c9bb",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "7fd2a363-933e-46a6-a87d-8300df11459c",
                "creator_id": "mocked-c5-6",
                "event": "appeal",
                "reasoning": "  Capstone review 6: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5682,
            "confidence": 0.5682,
            "content_id": "7fd2a363-933e-46a6-a87d-8300df11459c",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "1cc84833-c7aa-43b4-99fc-dd270a572468",
                "creator_id": "mocked-c5-7",
                "event": "appeal",
                "reasoning": "  Capstone review 7: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.581,
            "confidence": 0.581,
            "content_id": "1cc84833-c7aa-43b4-99fc-dd270a572468",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "61890ac7-d46c-4e33-b46f-3d3a45a0575b",
                "creator_id": "mocked-c5-8",
                "event": "appeal",
                "reasoning": "  Capstone review 8: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5721,
            "confidence": 0.5721,
            "content_id": "61890ac7-d46c-4e33-b46f-3d3a45a0575b",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "dab8c0ff-8863-45ef-b6d6-facccc9b3ea5",
                "creator_id": "mocked-c5-9",
                "event": "appeal",
                "reasoning": "  Capstone review 9: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5762,
            "confidence": 0.5762,
            "content_id": "dab8c0ff-8863-45ef-b6d6-facccc9b3ea5",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
          },
          {
            "appeals": [
              {
                "content_id": "ac726df9-a9a1-43c7-bacf-fd3b3810cd57",
                "creator_id": "mocked-c5-10",
                "event": "appeal",
                "reasoning": "  Capstone review 10: please consider my drafts.  ",
                "status": "under_review",
                "timestamp": "2026-11-14T02:05:25+00:00"
              }
            ],
            "combined_score": 0.5747,
            "confidence": 0.5747,
            "content_id": "ac726df9-a9a1-43c7-bacf-fd3b3810cd57",
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
            "timestamp": "2026-11-14T02:05:25+00:00"
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

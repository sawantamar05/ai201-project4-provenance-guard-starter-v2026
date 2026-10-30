#!/usr/bin/env python3
"""Capture an actual submission, appeal, log, and current status as JSON text."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import config  # noqa: E402


def capture(session, method, url, timeout, **kwargs):
    response = session.request(method, url, timeout=timeout, **kwargs)
    record = {"method": method, "url": url, "status_code": response.status_code,
              "content_type": response.headers.get("Content-Type", "")}
    if "json" in kwargs:
        record["request_json"] = kwargs["json"]
    try:
        record["response_json"] = response.json()
    except ValueError:
        record["response_text"] = response.text[:2000]
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("timeout must be positive")
    args.url = args.url.rstrip("/")
    raw = (ROOT / "data" / "evaluation_inputs.json").read_bytes()
    corpus = json.loads(raw)
    item = corpus["ai"][0]
    body = {"text": item["text"], "creator_id": "demo-writer"}
    report = {"recorded_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "dataset_sha256": hashlib.sha256(raw).hexdigest(), "input_provenance": item,
              "scope": "Development demonstration using an explicitly AI-generated input and a synthetic review request."}
    failed = False
    try:
        with requests.Session() as session:
            submission = capture(session, "POST", args.url + "/submit", args.timeout, json=body)
            report["submission"] = submission
            if submission["status_code"] != 200:
                raise RuntimeError("Submission failed; see the captured response.")
            content_id = submission.get("response_json", {}).get("content_id")
            if not isinstance(content_id, str) or not content_id:
                raise RuntimeError("Submission response has no content_id.")
            appeal_body = {"content_id": content_id, "reasoning": "Development appeal: please review this estimate."}
            (ROOT / "data" / "sample_submission.json").write_text(json.dumps(body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            (ROOT / "data" / "sample_appeal.json").write_text(json.dumps(appeal_body, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            report["appeal"] = capture(session, "POST", args.url + "/appeal", args.timeout, json=appeal_body)
            report["log"] = capture(session, "GET", args.url + "/log?limit=2", args.timeout)
            report["content"] = capture(session, "GET", args.url + "/content/" + content_id, args.timeout)
            failed = (
                report["appeal"]["status_code"] != 200
                or report["appeal"].get("response_json", {}).get("status") != "under_review"
                or report["log"]["status_code"] != 200
                or report["content"]["status_code"] != 200
                or report["content"].get("response_json", {}).get("status") != "under_review"
            )
    except (requests.RequestException, RuntimeError, ValueError) as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
        failed = True
    report["passed"] = not failed
    path = ROOT / "results" / "sample_run.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False))
    print(f"Saved {path.relative_to(ROOT)}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

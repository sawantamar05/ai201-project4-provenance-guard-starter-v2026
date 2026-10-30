#!/usr/bin/env python3
"""Record real HTTP development checks without changing frozen inputs.

Run the service first, then:
    python scripts/verify_project.py --url http://127.0.0.1:5000

Every result is saved even when an acceptance target is missed. This is a
small development evaluation, not an independent benchmark or authorship test.
"""

import argparse
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
import math
from pathlib import Path
import platform
import statistics
import sys
import uuid

import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import config  # noqa: E402
import scoring  # noqa: E402


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def capture(session, method, url, timeout, **kwargs):
    record = {"method": method, "url": url}
    if "json" in kwargs:
        record["request_json"] = kwargs["json"]
    if "data" in kwargs:
        record["request_body"] = kwargs["data"]
    if "headers" in kwargs:
        record["request_headers"] = kwargs["headers"]
    try:
        response = session.request(method, url, timeout=timeout, **kwargs)
        record["status_code"] = response.status_code
        record["content_type"] = response.headers.get("Content-Type", "")
        try:
            record["response_json"] = response.json()
        except ValueError:
            record["response_text"] = response.text[:2000]
    except requests.RequestException as exc:
        record["status_code"] = None
        record["transport_error"] = f"{type(exc).__name__}: {exc}"
    return record


def successful_submission(record):
    body = record.get("response_json")
    if record.get("status_code") != 200 or not isinstance(body, dict):
        return False
    try:
        uuid.UUID(body["content_id"])
        for name in ("model_score", "style_score", "combined_score", "confidence"):
            value = body[name]
            if isinstance(value, bool) or not isinstance(value, (float, int)):
                return False
            if not math.isfinite(value) or not 0 <= value <= 1:
                return False
        return (
            body["confidence"] == body["combined_score"]
            and body["guess"] in {"human", "unsure", "ai"}
            and isinstance(body["label"], str) and bool(body["label"].strip())
            and body["status"] == "decided"
        )
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def log_entries(record):
    body = record.get("response_json")
    if record.get("status_code") == 200 and isinstance(body, dict):
        entries = body.get("entries")
        if isinstance(entries, list):
            return entries
    return None


def successful_events(entries):
    return [entry for entry in entries if entry.get("status") in {"decided", "under_review"}]


def score_sweep():
    counts = {"human": 0, "unsure": 0, "ai": 0}
    failures = []
    for index in range(10001):
        score = index / 10000
        expected = "human" if score <= 0.25 else "ai" if score >= 0.75 else "unsure"
        try:
            guess, label = scoring.score_to_label(score)
            if guess not in counts or not isinstance(label, str) or not label.strip():
                failures.append({"score": score, "reason": "Invalid or empty label"})
            else:
                counts[guess] += 1
                if guess != expected:
                    failures.append({"score": score, "expected": expected, "actual": guess})
        except (TypeError, ValueError) as exc:
            failures.append({"score": score, "error": str(exc)})
    boundaries = {
        str(value): scoring.score_to_label(value)[0]
        for value in (0.0, 0.25, 0.2501, 0.51, 0.7499, 0.75, 0.95, 1.0)
    }
    return {
        "scores_checked": 10001,
        "counts": counts,
        "boundary_guesses": boundaries,
        "failures": failures,
        "passed": not failures and boundaries["0.51"] != boundaries["0.95"],
    }


def validation_cases(content_id):
    text = "This development paragraph contains enough ordinary words to validate."
    valid = {"text": text, "creator_id": "validation-writer"}
    appeal = {"content_id": content_id, "reasoning": "Development review request."}
    cases = []

    def add(group, name, route, expected, body=None, **kwargs):
        if body is not None:
            kwargs["json"] = body
        cases.append({"matrix_group": group, "name": name, "route": route,
                      "expected_status": expected, "kwargs": kwargs})

    add(1, "missing text", "/submit", 400, {"creator_id": "validation"})
    add(2, "empty text", "/submit", 400, {**valid, "text": ""})
    add(3, "whitespace text", "/submit", 400, {**valid, "text": " " * 30})
    for value in (None, 9, ["word"] * 5):
        add(4, f"non-string text {type(value).__name__}", "/submit", 400, {**valid, "text": value})
    add(5, "too few characters", "/submit", 400, {**valid, "text": "one two three four"})
    add(5, "too few words", "/submit", 400, {**valid, "text": "a" * 30})
    add(6, "oversized text", "/submit", 413, {**valid, "text": "x" * 10001})
    add(7, "missing creator", "/submit", 400, {"text": text})
    for value in ("", "  "):
        add(8, "blank creator", "/submit", 400, {**valid, "creator_id": value})
    add(9, "non-string creator", "/submit", 400, {**valid, "creator_id": 42})
    add(10, "oversized creator", "/submit", 400, {**valid, "creator_id": "x" * 129})
    for route in ("/submit", "/appeal"):
        add(11, "malformed JSON", route, 400, data="{", headers={"Content-Type": "application/json"})
        for raw in ("[]", "null", '"text"', "7"):
            add(12, f"non-object JSON {raw}", route, 400, data=raw, headers={"Content-Type": "application/json"})
        add(13, "non-JSON content type", route, 415, data="hello", headers={"Content-Type": "text/plain"})
        add(18, "oversized body", route, 413, data='{"padding":"' + "x" * 65536 + '"}', headers={"Content-Type": "application/json"})
    add(14, "missing content id", "/appeal", 400, {"reasoning": "Review this."})
    add(14, "non-string content id", "/appeal", 400, {**appeal, "content_id": 42})
    add(14, "malformed content id", "/appeal", 404, {**appeal, "content_id": "typo"})
    add(14, "unknown content id", "/appeal", 404, {**appeal, "content_id": str(uuid.uuid4())})
    add(15, "missing reasoning", "/appeal", 400, {"content_id": content_id})
    for value in ("", "  "):
        add(15, "blank reasoning", "/appeal", 400, {**appeal, "reasoning": value})
    add(16, "non-string reasoning", "/appeal", 400, {**appeal, "reasoning": ["review"]})
    add(17, "oversized reasoning", "/appeal", 413, {**appeal, "reasoning": "x" * 2001})
    return cases


def package_versions():
    versions = {}
    for name in ("flask", "flask-limiter", "requests", "transformers", "torch", "gunicorn", "certifi"):
        try:
            versions[name] = metadata.version(name)
        except metadata.PackageNotFoundError:
            versions[name] = None
    return versions


def settings_snapshot():
    names = (
        "DETECTOR_MODEL", "DETECTOR_MAX_TOKENS", "WEIGHT_MODEL_SIGNAL",
        "WEIGHT_STYLE_SIGNAL", "HUMAN_THRESHOLD", "AI_THRESHOLD",
        "SIGNAL_DISAGREEMENT_THRESHOLD", "DISAGREEMENT_SCORE_MIN",
        "DISAGREEMENT_SCORE_MAX", "STYLE_MIN_WORDS", "STYLE_MIN_SENTENCES",
        "STYLE_SPREAD_SCALE", "STYLE_TTR_BASELINE", "STYLE_TTR_SCALE",
        "STYLE_PUNCTUATION_SCALE", "STYLE_WEIGHT_EVENNESS",
        "STYLE_WEIGHT_REPETITION", "STYLE_WEIGHT_SIMPLICITY",
    )
    return {name: getattr(config, name, None) for name in names}



def supplemental_inputs(report):
    """Load clearly separated label examples without changing metric groups."""
    path = ROOT / "data" / "label_demonstrations.json"
    if not path.exists():
        report["supplemental_dataset"] = None
        return []
    raw = path.read_bytes()
    loaded = json.loads(raw)
    if isinstance(loaded, list):
        items, metadata = loaded, {}
    elif isinstance(loaded, dict):
        items = loaded.get("demonstrations", loaded.get("inputs", loaded.get("items")))
        metadata = loaded.get("metadata", {})
    else:
        raise ValueError("Supplemental demonstrations must be a list or an object containing demonstrations.")
    if not isinstance(items, list):
        raise ValueError("Supplemental demonstrations must contain a list of input objects.")
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not isinstance(item.get("text"), str):
            raise ValueError("Each supplemental demonstration needs string id and text fields.")
        if not item.get("provenance"):
            raise ValueError("Each supplemental demonstration needs explicit provenance.")
    report["supplemental_dataset"] = {
        "path": "data/label_demonstrations.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "metadata": metadata,
        "count": len(items),
        "selection_note": "Supplemental label-reachability examples are separate from the frozen development corpus and are excluded from false-positive and median-gap metrics.",
    }
    return [("supplemental", item) for item in items]


def verify_appeal_trial(session, args, submissions, trial_number):
    """Challenge this trial's ten original human decisions and preserve proof."""
    records = [r for r in submissions if r["input_group"] == "human" and r["valid_submission_contract"]]
    before = capture(session, "GET", args.url + "/log", args.timeout)
    original_entries = log_entries(before)
    appeals = []
    protected_fields = ("content_id", "creator_id", "guess", "model_score", "style_score", "combined_score", "label", "timestamp")
    for record in records:
        content_id = record["response_json"]["content_id"]
        original = next((e for e in original_entries or [] if e.get("content_id") == content_id and e.get("status") == "decided"), None)
        body = {"content_id": content_id, "reasoning": "Development appeal: please review this estimate."}
        response = capture(session, "POST", args.url + "/appeal", args.timeout, json=body)
        current = capture(session, "GET", args.url + "/content/" + content_id, args.timeout)
        current_body = current.get("response_json", {})
        response_body = response.get("response_json", {})
        result = {"content_id": content_id, "original_audit_entry": original, "appeal": response, "current_content": current}
        result["passed"] = (
            response["status_code"] == 200 and response_body.get("status") == "under_review"
            and response_body.get("reasoning") == body["reasoning"]
            and current["status_code"] == 200 and current_body.get("status") == "under_review"
            and original is not None
            and all(current_body.get(field) == original.get(field) for field in protected_fields)
            and any(e.get("reasoning") == body["reasoning"] for e in current_body.get("appeals", []))
        )
        appeals.append(result)
    after = capture(session, "GET", args.url + "/log", args.timeout)
    after_entries = log_entries(after)
    for result in appeals:
        content_id = result["content_id"]
        history = [e for e in after_entries or [] if e.get("content_id") == content_id]
        result["audit_history_after"] = history
        result["original_event_unchanged"] = bool(history) and history[0] == result["original_audit_entry"]
        result["appeal_event_recorded"] = any(e.get("event") == "appeal" and e.get("status") == "under_review" and e.get("reasoning") == "Development appeal: please review this estimate." for e in history)
        result["passed"] = result["passed"] and result["original_event_unchanged"] and result["appeal_event_recorded"]
    with requests.Session() as fresh:
        for result in appeals:
            recheck = capture(fresh, "GET", args.url + "/content/" + result["content_id"], args.timeout)
            result["fresh_http_session_recheck"] = recheck
            result["passed"] = result["passed"] and recheck["status_code"] == 200 and recheck.get("response_json", {}).get("status") == "under_review"
    return {
        "trial": trial_number, "appeals": appeals, "appeal_log_before": before, "appeal_log_after": after,
        "passed": len(appeals) == 10 and all(r["passed"] for r in appeals),
    }


def verify_validation_trial(session, args, submissions, trial_number):
    """Exercise all eighteen validation groups without successful new events."""
    valid = next((r for r in submissions if r["valid_submission_contract"]), None)
    content_id = valid["response_json"]["content_id"] if valid else str(uuid.uuid4())
    before = capture(session, "GET", args.url + "/log", args.timeout)
    records = []
    for case in validation_cases(content_id):
        response = capture(session, "POST", args.url + case["route"], args.timeout, **case["kwargs"])
        body = response.get("response_json")
        records.append({
            "matrix_group": case["matrix_group"], "name": case["name"],
            "expected_status": case["expected_status"], "http": response,
            "passed": response["status_code"] == case["expected_status"] and isinstance(body, dict)
            and bool(body.get("error")) and bool(body.get("message")),
        })
    after = capture(session, "GET", args.url + "/log", args.timeout)
    before_entries, after_entries = log_entries(before), log_entries(after)
    unchanged = before_entries is not None and after_entries is not None and successful_events(before_entries) == successful_events(after_entries)
    covered = sorted({r["matrix_group"] for r in records})
    return {
        "trial": trial_number, "cases": records, "matrix_groups_covered": covered,
        "successful_events_unchanged": unchanged,
        "successful_event_count_before": len(successful_events(before_entries)) if before_entries is not None else None,
        "successful_event_count_after": len(successful_events(after_entries)) if after_entries is not None else None,
        "passed": covered == list(range(1, 19)) and unchanged and all(r["passed"] for r in records),
    }


def run(args, report):
    dataset_path = ROOT / "data" / "evaluation_inputs.json"
    raw = dataset_path.read_bytes()
    dataset = json.loads(raw)
    report["dataset"] = {"path": "data/evaluation_inputs.json", "sha256": hashlib.sha256(raw).hexdigest(),
                         "metadata": dataset["metadata"]}
    if len(dataset["human"]) != 10 or len(dataset["ai"]) != 4 or len(dataset["calibration"]) != 4:
        raise ValueError("Expected frozen corpus of 10 human, 4 AI, and 4 calibration inputs.")
    groups = [(group, item) for group in ("human", "ai", "calibration") for item in dataset[group]]
    groups.extend(supplemental_inputs(report))
    input_ids = [item["id"] for _, item in groups]
    if len(set(input_ids)) != len(input_ids):
        raise ValueError("Input IDs must be unique across frozen and supplemental inputs.")
    with requests.Session() as session:
        report["health_before"] = capture(session, "GET", args.url + "/health", args.timeout)
        if report["health_before"]["status_code"] != 200:
            raise RuntimeError("Service health check failed; start the service before running verification.")
        trials = []
        report["submission_trials"] = trials
        for trial in range(1, args.trials + 1):
            records = []
            trial_record = {"trial": trial, "submissions": records}
            trials.append(trial_record)
            for group, item in groups:
                body = {"text": item["text"], "creator_id": f"development-{trial}-{item['id']}"}
                record = capture(session, "POST", args.url + "/submit", args.timeout, json=body)
                record.update({"input_group": group, "input_id": item["id"], "input_provenance": item})
                record["valid_submission_contract"] = successful_submission(record)
                records.append(record)
            trial_record["all_submissions_valid"] = all(r["valid_submission_contract"] for r in records)
            guesses = sorted({r.get("response_json", {}).get("guess", "error") for r in records})
            print(f"Submission trial {trial}: {sum(r['valid_submission_contract'] for r in records)}/{len(records)} valid; labels {', '.join(guesses)}", flush=True)

        criteria = {}
        report["criteria"] = criteria
        fp_trials, spread_trials, label_trials = [], [], []
        spread_human_ids = set(dataset["metadata"]["score_spread_human_ids"])
        spread_ai_ids = set(dataset["metadata"]["score_spread_ai_ids"])
        for trial in trials:
            valid = [r for r in trial["submissions"] if r["valid_submission_contract"]]
            human = [r for r in valid if r["input_group"] == "human"]
            false_positives = [r["input_id"] for r in human if r["response_json"]["guess"] == "ai"]
            fp_trials.append({"trial": trial["trial"], "valid_human_submissions": len(human),
                              "high_confidence_ai_count": len(false_positives), "flagged_ids": false_positives,
                              "passed": len(human) == 10 and len(false_positives) <= 1})
            humans = [r["response_json"]["combined_score"] for r in valid if r["input_group"] == "human" and r["input_id"] in spread_human_ids]
            ais = [r["response_json"]["combined_score"] for r in valid if r["input_group"] == "ai" and r["input_id"] in spread_ai_ids]
            human_median = statistics.median(humans) if len(humans) == 4 else None
            ai_median = statistics.median(ais) if len(ais) == 4 else None
            gap = ai_median - human_median if human_median is not None and ai_median is not None else None
            spread_trials.append({"trial": trial["trial"], "human_scores": humans, "ai_scores": ais,
                                  "human_median": human_median, "ai_median": ai_median, "median_gap": gap,
                                  "passed": gap is not None and (gap >= 0.20 or math.isclose(gap, 0.20, rel_tol=0, abs_tol=1e-12))})
            guesses = sorted({r["response_json"]["guess"] for r in valid})
            label_trials.append({"trial": trial["trial"], "actual_guesses": guesses,
                                 "label_examples": {guess: [r["input_id"] for r in valid if r["response_json"]["guess"] == guess] for guess in guesses},
                                 "passed": set(guesses) == {"human", "unsure", "ai"}})
        criteria["1"] = {"target": "At most 1 of 10 sourced human passages labeled AI in every trial", "trials": fp_trials, "passed": all(t["passed"] for t in fp_trials)}
        criteria["2"] = {"target": "AI median exceeds first-four-human median by at least 0.20 in every trial", "trials": spread_trials, "passed": all(t["passed"] for t in spread_trials)}
        sweep = score_sweep()
        criteria["3"] = {"target": "Three actual labels plus complete 10,001-score mapping", "trials": label_trials, "score_sweep": sweep, "passed": all(t["passed"] for t in label_trials) and sweep["passed"]}

        appeal_trials, validation_trials = [], []
        criteria["4"] = {
            "target": "10 appeals per trial retain reasoning, preserve originals, and show under_review",
            "trials": appeal_trials, "passed": False,
            "verification_scope": "Real HTTP appeal/audit checks and a fresh HTTP session. A fresh HTTP session is not a server restart.",
            "server_restart_verified": False,
            "detector_not_reinvoked": "Not observable via HTTP; requires the isolated service test that patches detector.model_signal.",
        }
        criteria["5"] = {
            "target": "All 18 validation groups reject safely before successful events in every trial",
            "trials": validation_trials, "passed": False,
            "detector_not_reinvoked": "Not observable via HTTP; requires isolated validation tests that patch detector.model_signal.",
        }
        for trial in trials:
            appeal_result = verify_appeal_trial(session, args, trial["submissions"], trial["trial"])
            appeal_trials.append(appeal_result)
            validation_result = verify_validation_trial(session, args, trial["submissions"], trial["trial"])
            validation_trials.append(validation_result)
            print(f"Workflow trial {trial['trial']}: {sum(a['passed'] for a in appeal_result['appeals'])}/10 appeals; {sum(c['passed'] for c in validation_result['cases'])}/{len(validation_result['cases'])} validation checks", flush=True)
        criteria["4"]["passed"] = len(appeal_trials) == args.trials and all(t["passed"] for t in appeal_trials)
        criteria["5"]["passed"] = len(validation_trials) == args.trials and all(t["passed"] for t in validation_trials)
        report["health_after"] = capture(session, "GET", args.url + "/health", args.timeout)
        report["all_submission_contracts_passed"] = all(t["all_submissions_valid"] for t in trials)
        report["all_http_targets_passed"] = report["all_submission_contracts_passed"] and all(c["passed"] for c in criteria.values()) and args.trials >= 3


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=120)
    parser.add_argument("--output", default="results/verification.json", help="JSON output path, relative to the project root unless absolute")
    args = parser.parse_args()
    if args.trials < 1 or args.timeout <= 0:
        parser.error("trials and timeout must be positive")
    args.url = args.url.rstrip("/")
    report = {"started_at_utc": now(), "service_url": args.url, "trials_requested": args.trials,
              "python_version": platform.python_version(), "packages": package_versions(), "scoring_settings": settings_snapshot(),
              "scope": "Frozen, small development inputs. Not independent attack testing or population accuracy evidence. Historical human excerpts may occur in GPT-2 training data.",
              "external_checks_required": ["Isolated tests for detector invocation count and failure modes", "Actual server restart with the same audit log"],
              "all_http_targets_passed": False}
    try:
        run(args, report)
    except Exception as exc:
        report["runner_error"] = f"{type(exc).__name__}: {exc}"
    finally:
        report["finished_at_utc"] = now()
        path = Path(args.output)
        if not path.is_absolute():
            path = ROOT / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
        try:
            display_path = path.relative_to(ROOT)
        except ValueError:
            display_path = path
        print(f"Saved {display_path}", flush=True)
    for number, outcome in report.get("criteria", {}).items():
        print(f"Criterion {number}: {'PASS' if outcome['passed'] else 'MISS'}", flush=True)
    if report.get("runner_error"):
        print(report["runner_error"], file=sys.stderr)
    return 0 if report["all_http_targets_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Prove the local run path from a clean clone and a fresh virtual environment.

No packages or model files are copied from the project's existing environment.
An explicitly supplied Hugging Face cache is reused, so this verifies startup
and inference after model download, rather than a new online model download.
The temporary checkout and all setup/server logs are retained for inspection.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import socket
import subprocess
import sys
import tempfile
import time
import traceback
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]


def now():
    return datetime.now(timezone.utc).isoformat()


def run(command, cwd, env, path, timeout=900):
    start = time.perf_counter()
    with path.open("w", encoding="utf-8") as stream:
        result = subprocess.run(command, cwd=cwd, env=env, stdout=stream,
                                stderr=subprocess.STDOUT, timeout=timeout)
    record = {"command": [str(x) for x in command], "cwd": str(cwd),
              "returncode": result.returncode,
              "duration_seconds": time.perf_counter() - start, "log": str(path)}
    if result.returncode:
        raise RuntimeError(f"Command exited {result.returncode}; see {path}")
    return record


def available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def request(base, method, path, payload=None, timeout=120):
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = Request(base + path, data=body, method=method,
                  headers={"Content-Type": "application/json"} if body else {})
    start = time.perf_counter()
    try:
        response = urlopen(req, timeout=timeout)
    except HTTPError as exc:
        response = exc
    with response:
        raw = response.read().decode("utf-8")
        parsed = json.loads(raw)
        return {"method": method, "path": path, "request_json": payload,
                "status_code": response.status, "response_json": parsed,
                "request_id": response.headers.get("X-Request-ID"),
                "elapsed_seconds": time.perf_counter() - start}


def start_server(python, checkout, env, port, log):
    command = [str(python), "-m", "gunicorn", "--workers", "1", "--threads", "1",
               "--bind", f"127.0.0.1:{port}", "--timeout", "120", "app:app"]
    stream = log.open("w", encoding="utf-8")
    proc = subprocess.Popen(command, cwd=checkout, env=env, stdout=stream,
                            stderr=subprocess.STDOUT, start_new_session=True)
    return proc, stream, {"command": command, "pid": proc.pid, "started_at": now(),
                          "server_log": str(log)}


def stop_server(proc, stream, record):
    if proc.poll() is None:
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait(timeout=10)
    stream.close()
    record.update(stopped_at=now(), returncode=proc.returncode)


def wait_ready(proc, base):
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            raise RuntimeError("Gunicorn exited during startup; inspect server log")
        try:
            result = request(base, "GET", "/health", timeout=2)
            if result["status_code"] == 200:
                return result
        except (URLError, TimeoutError, ConnectionError):
            pass
        time.sleep(0.1)
    raise RuntimeError("Gunicorn health check did not become ready within 45s")


def model_inventory(cache):
    model = cache / "hub/models--gpt2"
    revision = (model / "refs/main").read_text().strip()
    snapshot = model / "snapshots" / revision
    files = [{"name": f.name, "bytes": f.stat().st_size}
             for f in sorted(snapshot.iterdir()) if f.is_file()]
    return {"cache": str(cache), "model": "gpt2", "revision": revision,
            "snapshot_files": files, "snapshot_bytes": sum(f["bytes"] for f in files),
            "download_exercised": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python", default=sys.executable,
                        help="Interpreter used to create the new venv")
    parser.add_argument("--model-cache", required=True, type=Path,
                        help="Existing HF_HOME containing the GPT-2 hub cache")
    parser.add_argument("--wheelhouse", type=Path,
                        help="Optional complete wheel directory; disables package index")
    parser.add_argument("--output", type=Path,
                        default=ROOT / "results/capstone/clean_checkout.json")
    parser.add_argument("--workdir", type=Path,
                        help="New empty work directory; defaults to a retained /tmp directory")
    args = parser.parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    work = args.workdir.resolve() if args.workdir else Path(
        tempfile.mkdtemp(prefix="provenance-capstone-clean-"))
    work.mkdir(parents=True, exist_ok=True)
    checkout = work / "checkout"
    if checkout.exists():
        parser.error(f"Checkout already exists: {checkout}; use a new directory")
    cache = args.model_cache.resolve()
    env = os.environ.copy()
    env.update(PIP_DISABLE_PIP_VERSION_CHECK="1", PIP_CACHE_DIR=str(work / "pip-cache"),
               HF_HOME=str(cache), HF_HUB_OFFLINE="1", AI201_RATE_LIMITS="1",
               AI201_LOG_DIR=str(work / "session-logs"), PYTHONUNBUFFERED="1")
    # Avoid inheriting another checkout's import path or a virtual environment.
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONHOME", None)
    env.pop("VIRTUAL_ENV", None)
    report = {"started_at_utc": now(), "workdir": str(work), "checkout": str(checkout),
              "source_repository": str(ROOT), "steps": [], "sessions": [], "http": [],
              "checks": {}, "all_checks_passed": False,
              "scope": "Fresh clone and fresh venv; explicit reuse of previously downloaded GPT-2 cache. Not an online model-download test."}
    proc = stream = active_session = None
    try:
        report["model"] = model_inventory(cache)
        report["steps"].append(run(["git", "clone", "--no-local", str(ROOT), str(checkout)],
                                    ROOT, env, work / "clone.log"))
        report["source_commit"] = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=checkout, text=True).strip()
        report["checks"]["no_existing_venv_or_model_cache_in_clone"] = (
            not (checkout / ".venv").exists() and not (checkout / ".cache").exists())
        assert report["checks"]["no_existing_venv_or_model_cache_in_clone"]
        report["steps"].append(run([args.python, "-m", "venv", str(checkout / ".venv")],
                                    checkout, env, work / "venv.log"))
        python = checkout / ".venv/bin/python"
        install = [str(python), "-m", "pip", "install", "-r", "requirements-lock.txt"]
        if args.wheelhouse:
            install += ["--no-index", "--find-links", str(args.wheelhouse.resolve())]
        report["steps"].append(run(install, checkout, env, work / "install.log"))
        report["steps"].append(run([str(python), "-m", "pip", "check"],
                                    checkout, env, work / "pip-check.log"))
        verify = """import json, platform, sys
from pathlib import Path
from importlib import metadata
pins = [line.split('==') for line in Path('requirements-lock.txt').read_text().splitlines() if line and not line.startswith('#')]
rows = [{'name': name, 'expected': version, 'installed': metadata.version(name)} for name, version in pins]
print(json.dumps({'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(), 'machine': platform.machine(), 'packages': rows, 'all_exact': all(row['expected'] == row['installed'] for row in rows)}, indent=2))
"""
        envfile = work / "installed_environment.json"
        report["steps"].append(run([str(python), "-c", verify], checkout, env, envfile))
        report["environment"] = json.loads(envfile.read_text())
        report["checks"]["all_40_pinned_dependencies_match"] = report["environment"]["all_exact"]
        assert report["checks"]["all_40_pinned_dependencies_match"]
        port = available_port()
        base = f"http://127.0.0.1:{port}"
        proc, stream, active_session = start_server(python, checkout, env, port,
                                                   work / "server-initial.log")
        report["sessions"].append(active_session)
        health = wait_ready(proc, base)
        report["http"].append(health)
        report["checks"]["fresh_server_model_initially_unloaded"] = not health["response_json"]["detector_loaded"]
        corpus = json.loads((checkout / "data/evaluation_inputs.json").read_text())
        sample = corpus["human"][0]["text"]
        submitted = request(base, "POST", "/submit", {"text": sample, "creator_id": "clean-checkout-writer"})
        report["http"].append(submitted)
        decision = submitted["response_json"]
        report["checks"]["real_submission_saved"] = (submitted["status_code"] == 200
            and decision.get("status") == "decided" and bool(decision.get("content_id"))
            and all(isinstance(decision.get(key), (int, float)) for key in
                    ("model_score", "style_score", "combined_score")))
        assert report["checks"]["real_submission_saved"], submitted
        identity = decision["content_id"]
        reasoning = "  Clean checkout review: please consider my drafts.  "
        appealed = request(base, "POST", "/appeal", {"content_id": identity, "reasoning": reasoning})
        report["http"].append(appealed)
        report["checks"]["appeal_saved_exactly"] = (appealed["status_code"] == 200
            and appealed["response_json"].get("reasoning") == reasoning
            and appealed["response_json"].get("status") == "under_review")
        assert report["checks"]["appeal_saved_exactly"]
        audit_path = Path(env["AI201_LOG_DIR"]) / "audit.jsonl"
        original_events = [json.loads(line) for line in audit_path.read_text().splitlines() if line.strip()]
        original_decision = next(row for row in original_events if row.get("content_id") == identity and row.get("status") == "decided")
        stop_server(proc, stream, active_session)
        proc = stream = active_session = None
        proc, stream, active_session = start_server(python, checkout, env, port,
                                                   work / "server-restarted.log")
        report["sessions"].append(active_session)
        restarted_health = wait_ready(proc, base)
        report["http"].append(restarted_health)
        current = request(base, "GET", "/content/" + identity)
        report["http"].append(current)
        item = current["response_json"]
        report["checks"]["appeal_survives_real_process_restart"] = (
            current["status_code"] == 200 and item.get("status") == "under_review"
            and len(item.get("appeals", [])) == 1 and item["appeals"][0]["reasoning"] == reasoning
            and all(item.get(key) == value for key, value in original_decision.items() if key != "status")
            and not restarted_health["response_json"]["detector_loaded"])
        assert report["checks"]["appeal_survives_real_process_restart"]
        stop_server(proc, stream, active_session)
        proc = stream = active_session = None
        log_path = Path(env["AI201_LOG_DIR"]) / "requests.jsonl"
        completions = [json.loads(line) for line in log_path.read_text().splitlines() if line.strip()]
        matches = []
        for exchange in report["http"]:
            rows = [row for row in completions if row.get("request_id") == exchange["request_id"]]
            valid = bool(exchange["request_id"]) and len(rows) == 1
            if valid:
                row = rows[0]
                valid = (row.get("event") == "request_completed"
                    and row.get("http_status") == exchange["status_code"]
                    and all(isinstance(row.get(key), (int, float))
                            and math.isfinite(row[key]) and row[key] >= 0
                            for key in ("duration_ms", "cpu_seconds")))
            matches.append(valid)
        report["checks"]["every_captured_request_has_one_durable_completion"] = all(matches)
        report["checks"]["completion_log_does_not_store_text_or_reasoning"] = (
            sample not in log_path.read_text() and reasoning not in log_path.read_text())
        final_events = [json.loads(line) for line in audit_path.read_text().splitlines() if line.strip()]
        report["checks"]["original_audit_events_unchanged"] = final_events == original_events
        report["request_completion_records"] = completions
        report["audit_events"] = final_events
        report["dependency_lock_sha256"] = hashlib.sha256((checkout / "requirements-lock.txt").read_bytes()).hexdigest()
        report["all_checks_passed"] = all(report["checks"].values())
    except Exception as exc:
        report["error"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
    finally:
        if proc is not None:
            stop_server(proc, stream, active_session)
        report["finished_at_utc"] = now()
        output.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n")
    print(json.dumps({"report": str(output), "workdir": str(work),
                      "all_checks_passed": report["all_checks_passed"],
                      "checks": report["checks"], "error": report.get("error")}, indent=2))
    return 0 if report["all_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

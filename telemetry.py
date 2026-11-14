"""Durable request completion records, separate from the appeal/decision audit.

Measured wall and process CPU time cover the route and summary preparation,
through the point just before completion-log serialization/fsync. One synchronous
worker and one request at a time are required for per-request CPU attribution.
No submitted text or appeal-reasoning values are retained here.
"""

from datetime import datetime, timezone
import json
import os
import threading
import time
import uuid

from flask import g, request
from werkzeug.exceptions import RequestEntityTooLarge

import config

_lock = threading.Lock()


def log_path():
    """Resolve at use time so isolated sessions/tests can change LOG_DIR safely."""
    return config.LOG_DIR / "requests.jsonl"


def start_request():
    """Start before rate-limit hooks; even their early responses need a trace."""
    g.request_id = str(uuid.uuid4())
    g.request_wall_start = time.perf_counter()
    g.request_cpu_start = time.process_time()


def input_summary():
    """Describe bounded input without reading an oversized request body."""
    size = request.content_length
    summary = {"body_bytes": size, "content_type": request.mimetype}
    if size is not None and size > config.MAX_REQUEST_BYTES:
        summary["parsing"] = "oversized_not_parsed"
        return summary
    try:
        # Werkzeug applies MAX_CONTENT_LENGTH, including to a terminated stream
        # without Content-Length. cache=True preserves route behavior.
        raw = request.get_data(cache=True)
        summary["body_bytes"] = len(raw)
        if not raw:
            summary["parsing"] = "no_body"
            return summary
        if not request.is_json:
            summary["parsing"] = "non_json_content_type"
            return summary
        # Use json.loads instead of silent get_json to distinguish invalid JSON
        # from the valid JSON value null. No decoded values enter the log.
        try:
            payload = json.loads(raw)
        except (ValueError, UnicodeError):
            summary["parsing"] = "invalid_json"
            return summary
        if not isinstance(payload, dict):
            summary["parsing"] = "non_object_json"
            return summary
        summary["parsing"] = "json_object"
        names = sorted(payload)
        summary["field_names"] = [name[:128] for name in names[:64]]
        summary["field_count"] = len(names)
        summary["field_names_truncated"] = len(names) > 64 or any(len(x) > 128 for x in names[:64])
        if isinstance(payload.get("text"), str):
            summary["text_characters"] = len(payload["text"])
        return summary
    except RequestEntityTooLarge:
        summary["parsing"] = "oversized_not_parsed"
        return summary


def output_summary(response):
    """Keep a small response outcome, never a returned appeal's reasoning."""
    summary = {"content_type": response.mimetype}
    if not response.is_json:
        summary["outcome"] = "non_json_response"
        return summary
    # A /log response may contain the whole audit history. Avoid decoding that
    # large response again just to log it; its successful outcome is sufficient.
    if response.content_length is not None and response.content_length > config.MAX_REQUEST_BYTES:
        summary["outcome"] = "large_json_response"
        return summary
    payload = response.get_json(silent=True)
    if isinstance(payload, dict):
        for name in ("content_id", "guess", "error", "status"):
            if name in payload:
                summary[name] = payload[name]
        summary["outcome"] = "error" if "error" in payload else "success"
    else:
        summary["outcome"] = "non_object_json_response"
    return summary


def complete_request(response):
    """Append exactly one completion record for the response being returned.

    Persistence errors propagate to the application hook: a missing durable
    record must never be reported as a successful telemetry write.
    """
    response.headers["X-Request-ID"] = g.request_id
    entry = {
        "event": "request_completed",
        "request_id": g.request_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "method": request.method,
        "path": request.path,
        "http_status": response.status_code,
        "input_summary": input_summary(),
        "output_summary": output_summary(response),
    }
    entry["duration_ms"] = round(max(0, time.perf_counter() - g.request_wall_start) * 1000, 6)
    entry["cpu_seconds"] = round(max(0, time.process_time() - g.request_cpu_start), 9)
    append(entry)
    return response


def append(entry):
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=True, allow_nan=False)
    with _lock:
        with log_path().open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
            handle.flush()
            os.fsync(handle.fileno())

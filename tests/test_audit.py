"""Append-only evidence and concurrent JSONL integrity."""

from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import audit
import config


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name) / "logs"
        self.path = self.directory / "audit.jsonl"
        for name, value in (("LOG_DIR", self.directory), ("AUDIT_LOG", self.path)):
            p = patch.object(config, name, value)
            p.start()
            self.addCleanup(p.stop)

    def test_missing_log_returns_empty(self):
        self.assertEqual(audit.read_entries(), [])
        self.assertEqual(audit.entries_for("missing"), [])

    def test_append_appeal_keeps_original_bytes(self):
        decision = audit.log_decision("id-1", "writer", guess="unsure", model_score=0.5, style_score=0.5, combined_score=0.5, label="Uncertain.")
        before = self.path.read_bytes()
        appeal = audit.log_appeal("id-1", "writer", "  Exact reasoning — café.  ")
        self.assertTrue(self.path.read_bytes().startswith(before))
        self.assertEqual(audit.entries_for("id-1"), [decision, appeal])
        self.assertEqual(appeal["status"], "under_review")
        self.assertEqual(appeal["reasoning"], "  Exact reasoning — café.  ")

    def test_concurrent_writes_are_complete_json_lines(self):
        def write(i):
            return audit.log_decision(str(i), f"writer-{i}", guess="unsure", model_score=0.4, style_score=0.6, combined_score=0.44, label="Unsure.")
        with ThreadPoolExecutor(max_workers=8) as executor:
            list(executor.map(write, range(100)))
        lines = self.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 100)
        objects = [json.loads(line) for line in lines]
        self.assertEqual({row["content_id"] for row in objects}, {str(i) for i in range(100)})
        self.assertEqual(len(audit.read_entries()), 100)

    def test_latest_limit_and_rejection(self):
        for i in range(4):
            audit.log_decision(str(i), "writer")
        rejected = audit.log_rejection("writer", "bad_input")
        self.assertEqual(rejected["status"], "rejected")
        recent = audit.read_entries(limit=2)
        self.assertEqual(len(recent), 2)
        self.assertEqual(recent[0]["content_id"], "3")
        self.assertEqual(recent[-1], rejected)

    def test_malformed_line_does_not_hide_valid_history(self):
        first = audit.log_decision("first", "writer")
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("{broken\n")
        last = audit.log_decision("last", "writer")
        self.assertEqual(audit.read_entries(), [first, last])


if __name__ == "__main__":
    unittest.main()

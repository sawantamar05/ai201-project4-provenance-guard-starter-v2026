"""HTTP contract and persistence tests; inference is isolated with a mock."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid

import app as appmod
import audit
import config
import detector


VALID_TEXT = (
    "I walked beside the old canal this morning. A small boat bumped the bank, "
    "and the woman at its tiller laughed before pushing it back into the water."
)


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.log_dir = Path(self.temp.name)
        self.log_path = self.log_dir / "audit.jsonl"
        for key, value in (("LOG_DIR", self.log_dir), ("AUDIT_LOG", self.log_path)):
            p = patch.object(config, key, value)
            p.start()
            self.addCleanup(p.stop)
        self.model = patch.object(detector, "model_signal", return_value=0.60).start()
        self.addCleanup(patch.stopall)
        appmod.app.config["TESTING"] = True
        self.rate_setting = patch.object(appmod.limiter, "enabled", False, create=True)
        self.rate_setting.start()
        self.addCleanup(self.rate_setting.stop)
        self.client = appmod.app.test_client()

    def submit(self, text=VALID_TEXT, creator_id="writer-01"):
        return self.client.post("/submit", json={"text": text, "creator_id": creator_id})

    def assert_json_error(self, response, code):
        self.assertEqual(response.status_code, code, response.get_data(as_text=True))
        self.assertTrue(response.is_json)
        result = response.get_json()
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get("error"))
        self.assertTrue(result.get("message"))

    def successful_events(self):
        return [e for e in audit.read_entries() if e.get("status") in {"decided", "under_review"}]

    def test_ping_and_health_remain_available(self):
        response = self.client.post("/ping", json={"message": "hello"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"ok": True, "you_sent": "hello", "service": "provenance-guard"})
        health = self.client.get("/health").get_json()
        self.assertTrue(health["ok"])
        self.assertIn("detector_loaded", health)
        self.model.assert_not_called()

    def test_submit_complete_contract_and_durable_audit(self):
        response = self.submit()
        self.assertEqual(response.status_code, 200, response.get_data(as_text=True))
        result = response.get_json()
        uuid.UUID(result["content_id"])
        self.assertEqual(result["creator_id"], "writer-01")
        self.assertEqual(result["status"], "decided")
        self.assertIn(result["guess"], {"ai", "human", "unsure"})
        self.assertTrue(result["label"])
        for field in ("confidence", "model_score", "style_score", "combined_score"):
            self.assertIsInstance(result[field], (int, float))
            self.assertGreaterEqual(result[field], 0)
            self.assertLessEqual(result[field], 1)
        self.assertEqual(result["confidence"], result["combined_score"])
        entries = audit.read_entries()
        self.assertEqual(len(entries), 1)
        for field in ("content_id", "creator_id", "guess", "model_score", "style_score", "combined_score", "label", "status"):
            self.assertEqual(entries[0][field], result[field])
        self.assertTrue(entries[0]["timestamp"])
        self.assertNotIn("text", entries[0])
        self.model.assert_called_once_with(VALID_TEXT)
        self.assertEqual(self.client.get("/log").get_json()["entries"], entries)

    def test_distinct_submissions_have_unique_ids(self):
        ids = {self.submit().get_json()["content_id"] for _ in range(10)}
        self.assertEqual(len(ids), 10)
        self.assertEqual(len(audit.read_entries()), 10)

    def test_valid_unicode_text_and_reasoning(self):
        response = self.submit("Café riders share stories beside the river. Mañana, we will return together.", "écrivain")
        self.assertEqual(response.status_code, 200)
        content_id = response.get_json()["content_id"]
        reasoning = "  J’ai rédigé ce texte moi-même — voici mes brouillons.  "
        appeal = self.client.post("/appeal", json={"content_id": content_id, "reasoning": reasoning})
        self.assertEqual(appeal.status_code, 200)
        self.assertEqual(appeal.get_json()["reasoning"], reasoning)
        self.assertEqual(audit.entries_for(content_id)[-1]["reasoning"], reasoning)

    def test_valid_size_boundaries(self):
        exact_minimum = "aaa bbbb cccc dddd e"
        self.assertEqual(len(exact_minimum), 20)
        self.assertEqual(self.submit(exact_minimum).status_code, 200)
        maximum = "word " * 1999 + "word!"
        self.assertEqual(len(maximum), 10000)
        self.assertEqual(self.submit(maximum, "x" * 128).status_code, 200)
        content_id = self.submit().get_json()["content_id"]
        for reasoning in ("x", "x" * 2000):
            self.assertEqual(self.client.post("/appeal", json={"content_id": content_id, "reasoning": reasoning}).status_code, 200)

    def test_submit_validation_matrix(self):
        cases = [
            ("missing text", {"creator_id": "writer"}, 400),
            ("empty text", {"text": "", "creator_id": "writer"}, 400),
            ("whitespace text", {"text": " " * 30, "creator_id": "writer"}, 400),
            ("null text", {"text": None, "creator_id": "writer"}, 400),
            ("numeric text", {"text": 20, "creator_id": "writer"}, 400),
            ("array text", {"text": ["word"] * 10, "creator_id": "writer"}, 400),
            ("too few characters", {"text": "one two three four", "creator_id": "writer"}, 400),
            ("too few words", {"text": "a" * 30, "creator_id": "writer"}, 400),
            ("oversized text", {"text": "x" * 10001, "creator_id": "writer"}, 413),
            ("missing creator", {"text": VALID_TEXT}, 400),
            ("blank creator", {"text": VALID_TEXT, "creator_id": "  "}, 400),
            ("nonstring creator", {"text": VALID_TEXT, "creator_id": 99}, 400),
            ("oversized creator", {"text": VALID_TEXT, "creator_id": "x" * 129}, 400),
        ]
        for name, body, expected in cases:
            with self.subTest(name=name):
                self.assert_json_error(self.client.post("/submit", json=body), expected)
        self.model.assert_not_called()
        self.assertEqual(self.successful_events(), [])

    def test_json_transport_validation_both_routes(self):
        for route in ("/submit", "/appeal"):
            cases = [
                ("malformed", {"data": "{", "content_type": "application/json"}, 400),
                ("empty JSON", {"data": "", "content_type": "application/json"}, 400),
                ("array", {"data": "[]", "content_type": "application/json"}, 400),
                ("null", {"data": "null", "content_type": "application/json"}, 400),
                ("scalar", {"data": '"text"', "content_type": "application/json"}, 400),
                ("number", {"data": "7", "content_type": "application/json"}, 400),
                ("non JSON", {"data": "hello", "content_type": "text/plain"}, 415),
                ("oversized plain body", {"data": "x" * 65537, "content_type": "text/plain"}, 413),
                ("oversized body", {"data": '{"padding":"' + "x" * 65536 + '"}', "content_type": "application/json"}, 413),
            ]
            for name, kwargs, code in cases:
                with self.subTest(route=route, case=name):
                    self.assert_json_error(self.client.post(route, **kwargs), code)
        self.model.assert_not_called()
        self.assertEqual(self.successful_events(), [])

    def test_appeal_validation_matrix(self):
        content_id = self.submit().get_json()["content_id"]
        self.model.reset_mock()
        cases = [
            ("missing id", {"reasoning": "Review this."}, 400),
            ("nonstring id", {"content_id": 12, "reasoning": "Review this."}, 400),
            ("malformed id", {"content_id": "typo", "reasoning": "Review this."}, 404),
            ("unknown id", {"content_id": str(uuid.uuid4()), "reasoning": "Review this."}, 404),
            ("missing reasoning", {"content_id": content_id}, 400),
            ("blank reasoning", {"content_id": content_id, "reasoning": "  "}, 400),
            ("empty reasoning", {"content_id": content_id, "reasoning": ""}, 400),
            ("nonstring reasoning", {"content_id": content_id, "reasoning": ["review"]}, 400),
            ("oversized reasoning", {"content_id": content_id, "reasoning": "x" * 2001}, 413),
        ]
        for name, body, expected in cases:
            with self.subTest(name=name):
                self.assert_json_error(self.client.post("/appeal", json=body), expected)
        self.model.assert_not_called()
        self.assertEqual(len(self.successful_events()), 1)
        self.assertFalse(any(e.get("event") == "appeal" for e in audit.read_entries()))

    def test_unpaired_surrogates_are_rejected_before_model_or_success(self):
        for body in (
            {"text": VALID_TEXT + "\ud800", "creator_id": "writer"},
            {"text": VALID_TEXT, "creator_id": "writer-\udfff"},
        ):
            with self.subTest(field="text" if "\ud800" in body["text"] else "creator_id"):
                self.assert_json_error(self.client.post("/submit", json=body), 400)
        self.model.assert_not_called()
        self.assertEqual(self.successful_events(), [])
        content_id = self.submit().get_json()["content_id"]
        self.model.reset_mock()
        response = self.client.post("/appeal", json={"content_id": content_id, "reasoning": "Review my drafts: \ud800"})
        self.assert_json_error(response, 400)
        self.model.assert_not_called()
        self.assertEqual(len(self.successful_events()), 1)
        self.assertFalse(any(e.get("event") == "appeal" for e in audit.read_entries()))

    def test_ten_appeals_preserve_original_and_survive_fresh_process(self):
        ids = [self.submit(creator_id=f"writer-{i}").get_json()["content_id"] for i in range(10)]
        originals = [dict(e) for e in audit.read_entries()]
        self.model.reset_mock()
        for i, content_id in enumerate(ids):
            reasoning = f"  Review request {i}: please consider the drafts.  "
            response = self.client.post("/appeal", json={"content_id": content_id, "reasoning": reasoning})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json()["status"], "under_review")
            self.assertEqual(response.get_json()["reasoning"], reasoning)
            history = audit.entries_for(content_id)
            self.assertEqual(history[0], originals[i])
            self.assertEqual(history[-1]["reasoning"], reasoning)
            current = self.client.get(f"/content/{content_id}").get_json()
            self.assertEqual(current["status"], "under_review")
            self.assertEqual(current["model_score"], originals[i]["model_score"])
            self.assertEqual(len(current["appeals"]), 1)
        self.model.assert_not_called()
        self.assertEqual(len(audit.read_entries()), 20)
        code = """
import json, sys
from pathlib import Path
import config
config.LOG_DIR = Path(sys.argv[1])
config.AUDIT_LOG = config.LOG_DIR / 'audit.jsonl'
import app
client = app.app.test_client()
print(json.dumps([client.get('/content/' + x).get_json()['status'] for x in sys.argv[2:]]))
"""
        proc = subprocess.run([sys.executable, "-c", code, str(self.log_dir), *ids], cwd=str(config.ROOT), capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(proc.stdout), ["under_review"] * 10)

    def test_repeated_appeals_are_append_only(self):
        content_id = self.submit().get_json()["content_id"]
        original_line = self.log_path.read_bytes()
        for reasoning in ("First explanation.", "Additional evidence."):
            self.assertEqual(self.client.post("/appeal", json={"content_id": content_id, "reasoning": reasoning}).status_code, 200)
        self.assertTrue(self.log_path.read_bytes().startswith(original_line))
        history = audit.entries_for(content_id)
        self.assertEqual(len(history), 3)
        self.assertEqual([e["reasoning"] for e in history[1:]], ["First explanation.", "Additional evidence."])
        self.assertEqual(len(self.client.get(f"/content/{content_id}").get_json()["appeals"]), 2)

    def test_missing_content_returns_json_404(self):
        for content_id in ("typo", str(uuid.uuid4())):
            self.assert_json_error(self.client.get(f"/content/{content_id}"), 404)
        self.model.assert_not_called()

    def test_detector_unavailable_returns_503_without_success(self):
        self.model.side_effect = detector.DetectorUnavailable("test unavailable")
        self.assert_json_error(self.submit(), 503)
        self.assertEqual(self.successful_events(), [])

    def test_audit_failure_does_not_confirm_submission(self):
        with patch.object(audit, "log_decision", side_effect=OSError("test full disk")):
            self.assert_json_error(self.submit(), 503)
        self.assertEqual(self.successful_events(), [])

    def test_audit_failure_does_not_confirm_appeal(self):
        content_id = self.submit().get_json()["content_id"]
        with patch.object(audit, "log_appeal", side_effect=OSError("test full disk")):
            response = self.client.post("/appeal", json={"content_id": content_id, "reasoning": "Review this."})
            self.assert_json_error(response, 503)
        self.assertEqual(len(self.successful_events()), 1)
        self.assertEqual(self.client.get(f"/content/{content_id}").get_json()["status"], "decided")


if __name__ == "__main__":
    unittest.main()

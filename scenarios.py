"""Frozen development scenarios for the submission-only ``run_eval.py`` runner.

Human passages are sourced historical writing, not the submitter's own prose.
AI passages and their generation provenance live in data/evaluation_inputs.json.
Criterion 4 requires submission IDs followed by appeals, so it is exercised by
scripts/verify_project.py rather than this runner. That script also covers raw
malformed JSON, content types, and the full 18-group validation matrix.

These scenarios preserve corpus membership and do not assert detector outcomes.
The label inputs are candidates; actual responses determine label coverage.
"""

import json
from pathlib import Path


_CORPUS_PATH = Path(__file__).resolve().parent / "data" / "evaluation_inputs.json"
_CORPUS = json.loads(_CORPUS_PATH.read_text(encoding="utf-8"))
_HUMAN = _CORPUS["human"]
_AI = _CORPUS["ai"]
_CALIBRATION = _CORPUS["calibration"]
_BY_ID = {item["id"]: item for item in _HUMAN + _AI + _CALIBRATION}
_SPREAD_HUMAN = _CORPUS["metadata"]["score_spread_human_ids"]
_SPREAD_AI = _CORPUS["metadata"]["score_spread_ai_ids"]
_LABEL_IDS = ["human-03", "ai-01", "ai-03", "calibration-short-uncertain"]
_VALID_TEXT = _HUMAN[4]["text"]

_BAD_SUBMISSIONS = [
    ("missing text", {"creator_id": "scenario-missing-text"}, 400),
    ("empty text", {"text": "", "creator_id": "scenario-empty"}, 400),
    ("whitespace text", {"text": " " * 30, "creator_id": "scenario-whitespace"}, 400),
    ("null text", {"text": None, "creator_id": "scenario-null"}, 400),
    ("numeric text", {"text": 42, "creator_id": "scenario-number"}, 400),
    ("array text", {"text": ["word"] * 5, "creator_id": "scenario-array"}, 400),
    ("too few characters", {"text": "one two three four", "creator_id": "scenario-short"}, 400),
    ("too few words", {"text": "alphabet" * 5, "creator_id": "scenario-few-words"}, 400),
    ("oversized text", {"text": "x" * 10001, "creator_id": "scenario-long"}, 413),
    ("missing creator", {"text": _VALID_TEXT}, 400),
    ("empty creator", {"text": _VALID_TEXT, "creator_id": ""}, 400),
    ("whitespace creator", {"text": _VALID_TEXT, "creator_id": "  "}, 400),
    ("numeric creator", {"text": _VALID_TEXT, "creator_id": 42}, 400),
    ("oversized creator", {"text": _VALID_TEXT, "creator_id": "x" * 129}, 400),
    ("oversized body", {"text": _VALID_TEXT, "creator_id": "scenario-body", "padding": "x" * 65536}, 413),
]


def _texts(ids):
    return [_BY_ID[input_id]["text"] for input_id in ids]


SCENARIOS = [
    {
        "name": "sourced human false positives",
        "criterion": 1,
        "input_ids": [item["id"] for item in _HUMAN],
        "texts": [item["text"] for item in _HUMAN],
        "target": "At most one high-confidence AI guess among the ten sourced human passages per trial.",
    },
    {
        "name": "score spread human group",
        "criterion": 2,
        "input_ids": list(_SPREAD_HUMAN),
        "texts": _texts(_SPREAD_HUMAN),
        "target": "Compare this four-input median with the generated-AI group; required gap is at least 0.20.",
    },
    {
        "name": "score spread AI group",
        "criterion": 2,
        "input_ids": list(_SPREAD_AI),
        "texts": _texts(_SPREAD_AI),
        "target": "The generated-AI median must exceed the human-group median by at least 0.20.",
    },
    {
        "name": "label demonstration candidates",
        "criterion": 3,
        "input_ids": list(_LABEL_IDS),
        "texts": _texts(_LABEL_IDS),
        "target": "Observe human, unsure, and AI guesses; the complete score sweep is in scripts/verify_project.py.",
    },
    {
        "name": "invalid submission bodies",
        "criterion": 5,
        "case_names": [name for name, _, _ in _BAD_SUBMISSIONS],
        "bodies": [body for _, body, _ in _BAD_SUBMISSIONS],
        "expected_status_codes": [status for _, _, status in _BAD_SUBMISSIONS],
        "target": "Reject every listed body with its expected JSON error; full validation is in scripts/verify_project.py.",
    },
]


def validate() -> list[str]:
    """Check runner input shape without invoking the detector or sending HTTP."""
    problems = []
    for index, scenario in enumerate(SCENARIOS, 1):
        prefix = f"scenario {index}"
        if not isinstance(scenario.get("name"), str) or not scenario["name"].strip():
            problems.append(f"{prefix} needs a nonempty name")
        criterion = scenario.get("criterion")
        if isinstance(criterion, bool) or not isinstance(criterion, int) or criterion < 1:
            problems.append(f"{prefix} needs a positive integer criterion")
        has_texts = "texts" in scenario
        has_bodies = "bodies" in scenario
        if has_texts == has_bodies:
            problems.append(f"{prefix} needs exactly one of texts or bodies")
            continue
        field = "texts" if has_texts else "bodies"
        values = scenario[field]
        if not isinstance(values, list) or not values:
            problems.append(f"{prefix} needs a nonempty {field} list")
            continue
        for number, value in enumerate(values, 1):
            if has_texts and (not isinstance(value, str) or not value.strip()):
                problems.append(f"{prefix}, text {number} needs a nonempty string")
            elif has_bodies and not isinstance(value, dict):
                problems.append(f"{prefix}, body {number} needs a JSON object")
        if has_texts and len(scenario.get("input_ids", [])) != len(values):
            problems.append(f"{prefix} input IDs must match its text count")
        if has_bodies:
            for metadata_field in ("case_names", "expected_status_codes"):
                if len(scenario.get(metadata_field, [])) != len(values):
                    problems.append(f"{prefix} {metadata_field} must match its body count")
    return problems

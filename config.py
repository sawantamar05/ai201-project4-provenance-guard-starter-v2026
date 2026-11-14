"""Central settings for the local Provenance Guard service."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))
DEBUG = os.getenv("AI201_DEBUG", "0") == "1" and HOST in ("127.0.0.1", "localhost")
MAX_REQUEST_BYTES = 65_536
MIN_TEXT_CHARS = 20
MIN_TEXT_WORDS = 5
MAX_TEXT_CHARS = 10_000
MAX_CREATOR_CHARS = 128
MAX_REASONING_CHARS = 2_000

# A project-local cache keeps downloads separate from other projects.
os.environ.setdefault("HF_HOME", str(ROOT / ".cache" / "huggingface"))
DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")
DETECTOR_MAX_TOKENS = 400

WEIGHT_MODEL_SIGNAL = 0.80
WEIGHT_STYLE_SIGNAL = 0.20
HUMAN_THRESHOLD = 0.25
AI_THRESHOLD = 0.80
SIGNAL_DISAGREEMENT_THRESHOLD = 0.35
DISAGREEMENT_SCORE_MIN = 0.26
DISAGREEMENT_SCORE_MAX = 0.74

STYLE_MIN_WORDS = 20
STYLE_MIN_SENTENCES = 3
STYLE_SPREAD_SCALE = 0.8
STYLE_TTR_BASELINE = 0.9
STYLE_TTR_SCALE = 0.6
STYLE_PUNCTUATION_SCALE = 0.12
STYLE_WEIGHT_EVENNESS = 0.50
STYLE_WEIGHT_REPETITION = 0.30
STYLE_WEIGHT_SIMPLICITY = 0.20

# Part 2: local per-creator limits, enabled by default.
RATE_LIMITING_ENABLED = os.getenv("AI201_RATE_LIMITS", "1") == "1"
RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 200
RATE_LIMIT_STORAGE = "memory://"

# Separate real sessions and evaluation campaigns without replacing earlier evidence.
LOG_DIR = Path(os.getenv("AI201_LOG_DIR", str(ROOT / "logs"))).expanduser().resolve()
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"

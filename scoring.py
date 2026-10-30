"""Combine two AI-leaning signals and map every valid score to one label."""

import math
from numbers import Real

import config

HUMAN_LABEL = (
    "This writing looks more consistent with human writing. "
    "This estimate does not verify who wrote it."
)
UNSURE_LABEL = (
    "We cannot confidently tell how this writing was created. "
    "No conclusion about the writer should be drawn from this result. "
    "You can request a review."
)
AI_LABEL = (
    "This writing shows patterns often found in AI-generated text. "
    "This estimate can be wrong and is not proof of AI use. "
    "You can request a review."
)


def _validated_score(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite number between 0 and 1.")
    number = float(value)
    if not math.isfinite(number) or not 0.0 <= number <= 1.0:
        raise ValueError(f"{name} must be a finite number between 0 and 1.")
    return number


def combine_signals(model_score: float, style_score: float) -> float:
    """Weight model/style 80/20; keep large disagreements in the unsure band.

    The returned value is an AI-leaning score, not a calibrated probability.
    Weights, disagreement cutoff, and clamp boundaries are held in config.py.
    """
    model_score = _validated_score(model_score, "model_score")
    style_score = _validated_score(style_score, "style_score")
    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )
    gap = abs(model_score - style_score)
    cutoff = config.SIGNAL_DISAGREEMENT_THRESHOLD
    if gap >= cutoff or math.isclose(gap, cutoff, rel_tol=0.0, abs_tol=1e-12):
        combined = min(
            config.DISAGREEMENT_SCORE_MAX,
            max(config.DISAGREEMENT_SCORE_MIN, combined),
        )
    return round(_validated_score(combined, "combined_score"), 4)


def score_to_label(score: float) -> tuple[str, str]:
    """Map [0, 1] completely, with inclusive human and AI outer boundaries."""
    score = _validated_score(score, "score")
    if score <= config.HUMAN_THRESHOLD:
        return "human", HUMAN_LABEL
    if score >= config.AI_THRESHOLD:
        return "ai", AI_LABEL
    return "unsure", UNSURE_LABEL


def label_ranges() -> list[tuple[str, str]]:
    """Show non-overlapping interval notation matching score_to_label."""
    return [
        ("high-confidence human", f"[0.00, {config.HUMAN_THRESHOLD:.2f}]"),
        ("unsure", f"({config.HUMAN_THRESHOLD:.2f}, {config.AI_THRESHOLD:.2f})"),
        ("high-confidence AI", f"[{config.AI_THRESHOLD:.2f}, 1.00]"),
    ]


if __name__ == "__main__":
    for name, interval in label_ranges():
        print(f"{name}: {interval}")

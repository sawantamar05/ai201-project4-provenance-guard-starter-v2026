"""Surface-pattern signal: sentence variation, vocabulary, and punctuation.

These are heuristics about form, not evidence of who wrote a passage. Unicode
word and punctuation handling avoids treating non-ASCII writing as empty text.
"""

import json
import re
import statistics
import unicodedata

import config


def sentences(text: str) -> list[str]:
    """Split after sentence punctuation and optional closing quotes.

    Decimal points without following whitespace remain inside their sentence.
    This deliberately small tokenizer does not resolve abbreviations or genre.
    """
    parts = re.split(r"(?<=[.!?。！？])(?:[\"'”’\)\]]*)\s+", text.strip())
    return [part for part in parts if part.strip()]


def words(text: str) -> list[str]:
    """Return Unicode words, retaining internal straight or curly apostrophes."""
    normalized = unicodedata.normalize("NFC", text).casefold()
    return re.findall(r"[^\W_]+(?:['’][^\W_]+)*", normalized)


def sentence_length_spread(text: str) -> float:
    """Population standard deviation / mean word count; zero if unavailable."""
    lengths = [len(words(part)) for part in sentences(text)]
    lengths = [length for length in lengths if length]
    if len(lengths) < 2:
        return 0.0
    return statistics.pstdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """Unique lowercase word tokens / all word tokens; zero for no words."""
    tokens = words(text)
    return len(set(tokens)) / len(tokens) if tokens else 0.0


def punctuation_density(text: str) -> float:
    """Unicode punctuation characters / all nonspace characters."""
    characters = [character for character in text if not character.isspace()]
    if not characters:
        return 0.0
    punctuation = sum(unicodedata.category(c).startswith("P") for c in characters)
    return punctuation / len(characters)


def _clamp(value: float) -> float:
    return min(1.0, max(0.0, value))


def component_metrics(text: str) -> dict[str, float | int]:
    """Return independently inspectable measurements and normalized components."""
    tokens = words(text)
    sentence_count = sum(bool(words(part)) for part in sentences(text))
    spread = sentence_length_spread(text)
    variety = type_token_ratio(text)
    punctuation = punctuation_density(text)
    evenness = (
        _clamp(1.0 - spread / config.STYLE_SPREAD_SCALE)
        if sentence_count >= config.STYLE_MIN_SENTENCES else 0.5
    )
    repetition = _clamp(
        (config.STYLE_TTR_BASELINE - variety) / config.STYLE_TTR_SCALE
    )
    simplicity = _clamp(1.0 - punctuation / config.STYLE_PUNCTUATION_SCALE)
    score = (
        config.STYLE_WEIGHT_EVENNESS * evenness
        + config.STYLE_WEIGHT_REPETITION * repetition
        + config.STYLE_WEIGHT_SIMPLICITY * simplicity
    )
    if len(tokens) < config.STYLE_MIN_WORDS:
        score = 0.5
    return {
        "word_count": len(tokens),
        "sentence_count": sentence_count,
        "sentence_length_spread": spread,
        "type_token_ratio": variety,
        "punctuation_density": punctuation,
        "evenness": evenness,
        "repetition": repetition,
        "punctuation_simplicity": simplicity,
        "style_score": round(_clamp(score), 4),
    }


def style_signal(text: str) -> float:
    """Return a 0–1 AI-leaning style score, with neutral short-text handling."""
    return float(component_metrics(text)["style_score"])


if __name__ == "__main__":
    import sys

    sample = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )
    print(json.dumps(component_metrics(sample), indent=2, ensure_ascii=False))

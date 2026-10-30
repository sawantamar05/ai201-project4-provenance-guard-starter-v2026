"""Local GPT-2 predictability signal; a heuristic, not proof of authorship.

Low perplexity raises the AI score. Plain human language can be predictable;
unusual generated wording can be surprising. The first 400 tokens are used.
The model is loaded once per process and inference runs locally.
"""

import math
import threading

import config

_model = None
_tokenizer = None
_load_lock = threading.Lock()


class DetectorUnavailable(RuntimeError):
    """The model couldn't be loaded — no download yet, or no disk."""


def _load_unlocked():
    """Load the model once and keep it. First call downloads ~550 MB."""
    global _model, _tokenizer
    if _model is not None:
        return _model, _tokenizer

    try:
        import torch  # noqa: F401
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError as exc:
        raise DetectorUnavailable(
            f"transformers or torch isn't installed ({exc}).\n"
            f"Run: pip install -r requirements.txt"
        ) from exc

    try:
        _tokenizer = AutoTokenizer.from_pretrained(config.DETECTOR_MODEL)
        _model = AutoModelForCausalLM.from_pretrained(config.DETECTOR_MODEL)
        _model.eval()
    except Exception as exc:  # noqa: BLE001
        raise DetectorUnavailable(
            f"Couldn't load '{config.DETECTOR_MODEL}': {exc}\n"
            f"The first run downloads about 550 MB — check your connection and "
            f"that you have disk space free."
        ) from exc

    return _model, _tokenizer


def _load():
    with _load_lock:
        return _load_unlocked()


def perplexity(text: str) -> float:
    """
    How surprised the model is by this text. Lower means more predictable.

    Returns a positive number. Typical values land roughly between 10 and 200,
    but that range shifts with topic and length, which is one reason the raw
    number isn't what you score on.
    """
    import torch

    model, tokenizer = _load()

    encoded = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=config.DETECTOR_MAX_TOKENS,
    )
    input_ids = encoded["input_ids"]

    # Two tokens is not enough to be surprised by anything.
    if input_ids.shape[1] < 3:
        raise ValueError("Text is too short to score — a few sentences at least.")

    with torch.no_grad():
        output = model(input_ids, labels=input_ids)

    # The model's loss here IS mean negative log-likelihood per token.
    loss = float(output.loss.item())
    if not math.isfinite(loss):
        raise DetectorUnavailable("The model returned a non-finite loss.")
    return math.exp(min(loss, 700.0))


def model_signal(text: str) -> float:
    """
    The signal, as a 0–1 score. **Higher means more likely AI.**

    Perplexity is unbounded and roughly log-distributed, so it gets squashed
    onto 0–1 rather than clipped. The midpoint below is the perplexity that
    maps to 0.5 — text this surprising is a coin flip.

    You may want to move that midpoint once you've run the four calibration
    inputs in Milestone 4 and seen what your own text actually scores. If you
    do, say so in your README: it's a scoring decision, not a detail.
    """
    ppl = perplexity(text)

    midpoint = 45.0    # perplexity that scores 0.5
    steepness = 1.6    # how sharply the score moves either side of it

    # Logistic on log-perplexity. Low perplexity -> high AI score.
    log_odds = steepness * (math.log(ppl) - math.log(midpoint))
    score = 0.0 if log_odds > 700 else 1.0 / (1.0 + math.exp(log_odds))
    return round(min(max(score, 0.0), 1.0), 4)


def warm_up() -> str:
    """Load the model without scoring anything. Run this before class."""
    _load()
    return f"{config.DETECTOR_MODEL} loaded and ready."


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = (
            "The implementation of the proposed framework requires careful "
            "consideration of several key factors. First, it is important to "
            "note that the system must be able to handle a wide variety of "
            "different inputs. Additionally, the overall performance of the "
            "solution depends on a number of important variables."
        )
        print("(no text given — scoring a sample)\n")

    print(f"Loading {config.DETECTOR_MODEL} (first run downloads ~550 MB)…")
    print(f"perplexity     {perplexity(text):.1f}")
    print(f"model_signal   {model_signal(text):.4f}   (higher = more likely AI)")

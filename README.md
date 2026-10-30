# Provenance Guard

A local Flask backend for cautious writing-provenance estimates and appeals.
[Run the service](RUNNING.md) · [Acceptance criteria](criteria.md) ·
[API design](docs/design.md) · [Verification evidence](docs/verification.md)

## What This Does

A writing submission follows seven steps:

1. Validate a JSON object containing `text` and `creator_id`.
2. Assign a unique content ID.
3. Run a cached local GPT-2 model to measure contextual predictability.
4. Measure sentence-length variation, vocabulary variety, and punctuation.
5. Combine the two signals into a continuous AI-leaning score.
6. Select one complete label: human-like, unsure, or AI-like.
7. Save a timestamped audit event before returning JSON.

`POST /appeal` records the writer's reasoning, preserves the original decision,
and changes current status to `under_review`. It does not run the detector
again. The stretch feature `GET /content/<id>` returns the persisted decision,
its appeals, and its current status. This feature was declared before implementation.

Everything runs locally after the model download; no API key is required.
Submission text is not retained in the audit log. This teaching API uses
caller-supplied creator IDs and exposes its log, so run it on loopback.

## Signals and Scoring

**Model signal — `detector.py::model_signal`.** GPT-2 measures next-token
predictability, expressed as perplexity. The score is
`1 / (1 + (perplexity / 45) ** 1.6)`, rounded to four decimals. Predictable
language raises the AI score. The cached model reads at most 400 tokens.
Its blind spot: predictability is not authorship. Plain human language can
look machine-like, while unusual or edited generated language can look human-like.

**Style signal — `stylometry.py::style_signal`.** Three surface measurements
produce a separate 0–1 score. All normalized components are clamped to `[0, 1]`:

| Measurement | Normalized AI-leaning component | Weight |
|---|---|---|
| Population sentence-length standard deviation / mean (CV) | `1 - CV / 0.8` | 0.50 |
| Unique words / total words | `(0.9 - ratio) / 0.6` | 0.30 |
| Unicode punctuation / nonspace characters | `1 - density / 0.12` | 0.20 |

Fewer than three sentences gives neutral sentence evenness of 0.5; fewer than
20 words gives neutral overall style of 0.5. Uniform sentences, repetition,
and sparse punctuation tend to raise this signal. It measures the whole accepted
text, up to 10,000 characters. Its blind spot: it cannot understand meaning.
Genre, length, quotations, typos, language, and deliberate edits move its score.
The thresholds are heuristics, not learned authorship guarantees.

**Combining rule — `scoring.py::combine_signals`.** Start with
`0.80 * model_score + 0.20 * style_score`. When the signals differ by at least
0.35, clamp the result to `[0.26, 0.74]`, keeping strong disagreement unsure.
Round to four decimals. Weights and thresholds live in `config.py`; the rule
was recorded before implementation and evaluation.

`confidence` and `combined_score` contain the same **AI-leaning score**:
0 means human-like and 1 means AI-like. This is not a calibrated probability
that someone used AI, nor certainty in the selected guess.

**Observed disagreement:** Thoreau's sourced *Walden* passage (`human-05`)
scored model **0.7577**, style **0.2178**, combined **0.6497**, yielding unsure.
The model alone leans AI; the structural signal leans human. The combined
result avoids treating that disagreement as a confident accusation.

Across three trials, none of the 10 historical human passages received the
AI label; all 10 were unsure. The four-AI median was 0.6751 and the first-four-human
median was 0.4281: a gap of **0.2470**. These small development samples do not
estimate real-world accuracy. Input sources and generation provenance are
recorded in [data/README.md](data/README.md).

## Label Variants

| Label | Complete score range | Exact reader-facing text |
|---|---|---|
| high-confidence human (`human`) | `0 ≤ score ≤ 0.25` | This writing looks more consistent with human writing. This estimate does not verify who wrote it. |
| unsure (`unsure`) | `0.25 < score < 0.75` | We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review. |
| high-confidence AI (`ai`) | `0.75 ≤ score ≤ 1` | This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review. |

The unsure label says what is unknown without accusing the writer, then offers
a next step. All 10,001 four-decimal scores map to exactly one label; 0.51 is
unsure and 0.95 is AI-like.

Actual submissions reached human at **0.1628**, unsure at **0.6086**, and AI at
**0.9615**. The human-labeled input was deliberately unusual **AI-generated**
stress prose: it proves reachability and demonstrates evasion, not a correct
authorship decision. It was selected after the initial run and is excluded
from the frozen 10-human/4-AI metrics. Original results and supplemental input
provenance remain available in [docs/verification.md](docs/verification.md).

## Sample Run

These are actual HTTP responses captured on October 30, 2026. Port 5054 was
used for verification; the default is 5000. The submitted paragraph is an
explicitly AI-generated development example, and the appeal is a synthetic
review request. Full capture: [results/sample_run.json](results/sample_run.json).

**Submission request — HTTP 200**

```bash
curl -X POST http://127.0.0.1:5054/submit \
  -H "Content-Type: application/json" \
  --data-binary @data/sample_submission.json
```

Request body:

```json
{
  "text": "Effective communication is essential for building a productive and collaborative workplace. By establishing clear expectations and encouraging open dialogue, organizations can ensure that every team member understands their responsibilities. Regular feedback helps employees identify opportunities for improvement while reinforcing successful habits. In addition, consistent documentation allows important information to remain accessible as projects evolve. Managers should create an environment where questions are welcomed and different perspectives are respected. This approach supports accountability, reduces misunderstandings, and strengthens trust across departments. Ultimately, investing in thoughtful communication practices enables teams to work more efficiently and achieve sustainable results together.",
  "creator_id": "demo-writer"
}
```

Response:

```json
{
  "combined_score": 0.6086,
  "confidence": 0.6086,
  "content_id": "d562e6be-8e0d-4321-b32c-dcadf7930899",
  "creator_id": "demo-writer",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6223,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.7627491255431172,
    "punctuation_density": 0.016643550624133148,
    "punctuation_simplicity": 0.8613037447988905,
    "repetition": 0.0,
    "sentence_count": 7,
    "sentence_length_spread": 0.18980069956550624,
    "style_score": 0.5536,
    "type_token_ratio": 0.90625,
    "word_count": 96
  },
  "style_score": 0.5536,
  "text_length": 816,
  "timestamp": "2026-10-30T17:50:06+00:00"
}
```

**Appeal request — HTTP 200**

```bash
curl -X POST http://127.0.0.1:5054/appeal \
  -H "Content-Type: application/json" \
  --data-binary @data/sample_appeal.json
```

Request body:

```json
{
  "content_id": "d562e6be-8e0d-4321-b32c-dcadf7930899",
  "reasoning": "Development appeal: please review this estimate."
}
```

Response:

```json
{
  "content_id": "d562e6be-8e0d-4321-b32c-dcadf7930899",
  "creator_id": "demo-writer",
  "event": "appeal",
  "message": "Your appeal has been recorded. This writing is now under review.",
  "reasoning": "Development appeal: please review this estimate.",
  "status": "under_review",
  "timestamp": "2026-10-30T17:50:06+00:00"
}
```

**Audit log after the appeal — HTTP 200**

```bash
curl "http://127.0.0.1:5054/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.6086,
      "confidence": 0.6086,
      "content_id": "d562e6be-8e0d-4321-b32c-dcadf7930899",
      "creator_id": "demo-writer",
      "detector_model": "gpt2",
      "guess": "unsure",
      "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
      "model_score": 0.6223,
      "status": "decided",
      "style_metrics": {
        "evenness": 0.7627491255431172,
        "punctuation_density": 0.016643550624133148,
        "punctuation_simplicity": 0.8613037447988905,
        "repetition": 0.0,
        "sentence_count": 7,
        "sentence_length_spread": 0.18980069956550624,
        "style_score": 0.5536,
        "type_token_ratio": 0.90625,
        "word_count": 96
      },
      "style_score": 0.5536,
      "text_length": 816,
      "timestamp": "2026-10-30T17:50:06+00:00"
    },
    {
      "content_id": "d562e6be-8e0d-4321-b32c-dcadf7930899",
      "creator_id": "demo-writer",
      "event": "appeal",
      "reasoning": "Development appeal: please review this estimate.",
      "status": "under_review",
      "timestamp": "2026-10-30T17:50:06+00:00"
    }
  ]
}
```

The original event stays `decided`; the appended appeal is `under_review`.
`GET /content/` followed by this content ID returns the current review status.
It remained `under_review` after the service was stopped and restarted, with
the model still unloaded: [restart evidence](results/restart_check.json).

Run `python scripts/demo.py --url http://127.0.0.1:5054` to capture a new ID and
refresh both request files. Full verification uses
`python scripts/verify_project.py --url http://127.0.0.1:5054`.

## How I Used AI

**Moment 1 — surface measurements and scoring.** The request was to implement
the documented three style measurements and the fixed 80/20 combining rule,
including Unicode handling and finite-score validation. The response provided
separate measurement functions, component diagnostics, and an uncertainty
clamp. The resulting changes replaced the starter's constant style score and
placeholder labels, then integrated the functions into `/submit` and audit events.

**Moment 2 — failure-path review.** The request was to inspect validation,
persistence, and the evaluation runner for crashes or unsupported success
claims. The response identified an unpaired-Unicode-surrogate logging crash
and a runner that repeated submissions but only checked appeals/validation
once. The changes validate Unicode before inference, reject oversized bodies
early, add regression tests, and repeat all five criterion checks across
three trials. All 29 automated tests passed, alongside the real HTTP checks.

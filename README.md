# Provenance Guard

## What This Does

A local Flask service estimates writing provenance and gives writers a way to
appeal. It validates JSON, assigns a content ID, runs local GPT-2, measures
writing style, combines both signals, selects a reader-facing label, and saves
an audit event before responding.

The planned stretch feature is `GET /content/<id>`: retrieve a persisted
decision, its appeals, and current review status.

The API contract, false-positive walkthrough, and validation matrix are in
[docs/design.md](docs/design.md). Targets are in [criteria.md](criteria.md).

## Signals and Scoring

`detector.py::model_signal` measures contextual next-token predictability with
local GPT-2. Low perplexity raises the AI score. Predictable human prose can
score highly; unusual wording and edited AI can score low. This measures
language patterns, not authorship, and considers at most 400 tokens.

`stylometry.py::style_signal` measures sentence-length variation, word variety,
and punctuation density without understanding meaning. Uniform sentences,
repetition, and sparse punctuation raise its AI score. Genre, text length,
quotations, language, and deliberate edits can change those patterns.

The rule is fixed before implementation: `0.80 * model_score + 0.20 *
style_score`. When signals differ by at least 0.35, clamp the result to
`[0.26, 0.74]`, keeping disagreement unsure. Human scores are at most 0.25;
AI scores are at least 0.75. The rule lives in `scoring.py::combine_signals`;
weights and thresholds live in `config.py`.

`confidence` is the combined **AI-leaning score**, from 0 (human-like) to 1
(AI-like), not a calibrated probability of AI authorship.

## Label Variants

| Label | Score range | Exact reader-facing text |
|---|---|---|
| high-confidence human (`human`) | `0 ≤ score ≤ 0.25` | This writing looks more consistent with human writing. This estimate does not verify who wrote it. |
| unsure (`unsure`) | `0.25 < score < 0.75` | We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review. |
| high-confidence AI (`ai`) | `0.75 ≤ score ≤ 1` | This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review. |

The unsure label states that uncertainty says nothing about the writer.

## Sample Run

See [RUNNING.md](RUNNING.md) for setup and commands. The sample run will record
an actual submission, appeal, and corresponding audit events as JSON text.

## How I Used AI

AI assistance supports implementation and review. Two concrete examples and
their resulting changes accompany the verified sample run.

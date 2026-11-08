# Service design — Part 1 baseline

This is the original pre-implementation design. Part 2 retains the API contract
and changes only the AI-label threshold from 0.75 to 0.80 after baseline testing.
Current results and ranges are in [README.md](../README.md).

## Submission path

1. Receive JSON with `text` and `creator_id`; validate size and types.
2. Allocate a UUID after validation.
3. Ask cached GPT-2 how predictable the text is.
4. Measure sentence-length variation, vocabulary variety, and punctuation.
5. Combine 80% model and 20% style, keeping large disagreements unsure.
6. Map the score to one complete reader-facing label.
7. Append the decision to JSONL, then return ID, scores, label, and status.

## Signals and fixed combining rule

The model measures contextual token predictability. Predictability is not
authorship: plain human and generated writing can share it, and unusual
generated wording can evade it.

Style measures surface shape: sentence-length coefficient of variation (CV),
unique words / all words, and Unicode punctuation / nonspace characters.
It cannot read meaning. Quotations, typos, sentence edits, and genre can shift
it; word diversity also depends on length.

Style components, clamped to `[0, 1]`:

- evenness = `1 - CV / 0.8` (neutral 0.5 with fewer than 3 sentences)
- repetition = `(0.9 - type_token_ratio) / 0.6`
- punctuation simplicity = `1 - punctuation_density / 0.12`

Style = `0.50 * evenness + 0.30 * repetition + 0.20 * simplicity`.
Fewer than 20 words gives neutral style 0.5. Start combined scoring at
`0.80 * model + 0.20 * style`. If `abs(model - style) >= 0.35`, clamp the
result to `[0.26, 0.74]`. Round to 4 decimals. Human: at most 0.25; AI: at
least 0.75; unsure: strictly between. These choices precede calibration.

## False-positive walkthrough

A real writer's plain prose could receive model 0.95 and style 0.60. A gap
of 0.35 caps its raw 0.88 at 0.74: unsure. If both signals instead agree
strongly enough for 0.85, the AI label still warns the estimate can be wrong
and offers review. Appealing preserves original scores, records the exact
reasoning, and sets current status to `under_review`, without reassessment.
These numbers illustrate the rule; they are not model measurements.

## Endpoint contracts

`POST /submit` accepts a JSON object:

```json
{"text": "A paragraph of writing with at least five words.", "creator_id": "writer-01"}
```

HTTP 200 fields: `content_id` (UUID), `creator_id`, `guess` (`human`, `unsure`,
or `ai`), `confidence` (combined AI score), `model_score`, `style_score`,
`combined_score` (numbers 0–1), `label` (complete sentence), `status: decided`.
The audit event adds a UTC timestamp. Submission text is not logged.

`POST /appeal` accepts:

```json
{"content_id": "UUID returned by submit", "reasoning": "Please review this estimate against my drafts."}
```

HTTP 200 returns `content_id`, original `creator_id`, `status: under_review`,
exact `reasoning`, `timestamp`, and a confirmation `message`. Append an appeal
event; preserve every explanation if repeated. Unknown IDs return 404.

`GET /content/<id>` (stretch) returns the original decision fields, current
status, and an `appeals` array. Read JSONL so status survives restarts. Invalid
and unknown IDs return 404.

Preserve starter `/ping`, `/health`, and `/log` contracts. Detector failure
returns JSON 503; persistence failure returns JSON 503 without a success response.

## Validation matrix

Validate before inference. Error JSON contains `error` and `message`.
Rejections can have audit events, never successful decisions or appeals.

| Case | Route | Expected HTTP |
|---|---|---|
| 1. Missing text | submit | 400 |
| 2. Empty text | submit | 400 |
| 3. Whitespace text | submit | 400 |
| 4. Non-string text | submit | 400 |
| 5. Below 20 characters or 5 word tokens | submit | 400 |
| 6. Above 10,000 characters | submit | 413 |
| 7. Missing creator_id | submit | 400 |
| 8. Empty creator_id | submit | 400 |
| 9. Non-string creator_id | submit | 400 |
| 10. Creator_id above 128 characters | submit | 400 |
| 11. Malformed JSON | both | 400 |
| 12. Non-object JSON (array, null, scalar) | both | 400 |
| 13. Non-JSON content type | both | 415 |
| 14. Missing, malformed, or unknown content_id | appeal | 400 / 404 / 404 |
| 15. Missing, empty, or whitespace reasoning | appeal | 400 |
| 16. Non-string reasoning | appeal | 400 |
| 17. Reasoning above 2,000 characters | appeal | 413 |
| 18. Body above 65,536 bytes | both | 413 |

Retain submitted IDs and reasoning; check strings using stripped content.
This local teaching API trusts creator IDs and exposes the audit log. Keep
it on loopback. A writing site needs ownership checks and restricted log access.

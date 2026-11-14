# Provenance Guard

A local Flask backend for cautious writing-provenance estimates and appeals.
[Run the service](RUNNING.md) · [Part 1/2 criteria](docs/criteria_parts1_2.md) ·
[API design](docs/design.md) · [Part 1 evidence](docs/verification.md) · [Part 2 audit](results/part2_submission_audit.json)

Part 2 testing is recorded below: **56 attacks before and 56 after**, three
trials per original criterion in both phases, and one measured threshold change.
Four criteria are MET; the exact bad-input-code criterion remains MISSED and
is diagnosed. Test results and residual failures are part of the submission.


## What This Does

A writing submission follows seven steps:

1. Apply the caller quota and validate JSON containing `text` and `creator_id`.
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

The [criteria review](docs/criteria_review.md) restates the five existing targets
with plain-language rationales and check procedures. The working-alone
[writer-perspective exercise](docs/feedback.md) records feedback on the
false-positive target and the engineering response.


## Label Variants

| Label | Complete score range | Exact reader-facing text |
|---|---|---|
| high-confidence human (`human`) | `0 ≤ score ≤ 0.25` | This writing looks more consistent with human writing. This estimate does not verify who wrote it. |
| unsure (`unsure`) | `0.25 < score < 0.80` | We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review. |
| high-confidence AI (`ai`) | `0.80 ≤ score ≤ 1` | This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review. |

These are the current Part 2 ranges. The measured improvement raised the AI
threshold from `0.75` to `0.80`; the original before ranges remain in history.

The unsure label says what is unknown without accusing the writer, then offers
a next step. All 10,001 four-decimal scores map to exactly one label; 0.51 is
unsure and 0.95 is AI-like.

The [label feedback exercise](docs/feedback.md) records a simulated writer's
interpretation of all three labels. To request review, send the returned
`content_id` and a nonempty `reasoning` string to `POST /appeal`. A successful
response confirms `under_review`; `GET /content/<id>` shows the current status.
The original estimate remains in the history. A recorded appeal does not mean
a human reviewer has been assigned or a review has been completed.


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
three trials. At the Part 1 checkpoint, all 29 automated tests passed alongside the real HTTP checks. Part 2 adds five checks, for 34 passing tests.


**Writer-perspective exercises.** Codex also generated the assignment's
working-alone feedback on the false-positive criterion and all three labels.
The prompts and fictional writer responses are preserved in
[the feedback record](docs/feedback.md). They led to clearer appeal instructions;
the targets, thresholds, and label sentences were retained. This is simulated
AI feedback, not independent human validation.



**Part 2 — instruments and diagnosis.** AI assistance was used to configure
per-creator limits, capture full attack exchanges, and extend the evaluation
runner to exercise all five criteria three times. The resulting changes added
rate-limit tests and rejection metadata; detector/model code and the original
criteria were retained.

**Part 2 — competing explanations and measured change.** The working-alone
prompts requested three causes for FP03 without ranking them and the strongest
opposing verdict for criterion 5. The analysis separated ordinary-language
predictability, structural regularity, and the label boundary; it also exposed
that safe 429 rejection is not the exact 400/404/413/415 target. The chosen single
runtime improvement was AI threshold 0.75→0.80, measured with both full suites.
All attack judgments and diagnoses are AI-assisted engineering analysis using
the actual returned values; they are not independent human annotations or peer
feedback. Full prompts/responses are in [the Part 2 feedback record](results/part2_feedback.json).

## Rate Limiting

Part 2 enables **10 submissions per minute and 200 per day**. A writer can
submit several drafts quickly; a script cannot score hundreds of variations
in one burst. Rejected submissions also count toward the caller's quota.
The limiter uses local process memory and resets when the service restarts.

The declared Part 2 stretch feature is **per-creator limits**. A nonempty,
valid creator ID defines the bucket across addresses; malformed or missing
IDs fall back to the caller's address. Different creators sharing an address
get separate quotas. Creator IDs are self-asserted, so changing IDs can evade
these quotas; a deployed site needs authenticated identity.

Live flood evidence: [results/flood_2026-11-08_1339.md](results/flood_2026-11-08_1339.md).

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

All ten accepted decisions contain the nine required fields; all five 429s
are persisted with their creator, bucket, route, reason, and limit. Three
additional submissions were read back through `/log`:
[the instrumentation capture](results/part2_instrumentation.json).
The original criteria and scoring baseline remain unchanged at this checkpoint.


## Attack Run — Before

The supplied course ZIP was opened after the limiter/log checkpoint. It contains
**56 rows**, and every row was sent: 32 text attacks plus 24 request attacks.
Original bytes and checksums are retained in [attack_set/](attack_set/).
There were **43 HELD and 13 BROKE**, with no skipped row, transport failure, or
5xx response. Full requests/responses: [raw capture](results/attack_run_2026-11-08_1341_before.json).

Judgment policy: an accepted generated item avoiding the AI label counts as
BROKE even when it is unsure; a supplied human-designated item is a false
positive only if labeled AI. PI02 partially obtains its requested human guess,
so it is conservatively BROKE, without claiming the model executed instructions.
Arabic is valid input: accepting MF07 safely counts as HELD. The flood provides
12 actual rows (its description says 20); the first 10 are within quota and the
last 2 must be 429. Judgments and explanations for every row are in the
[reviewed capture](results/part2_attack_before_reviewed.json).

| ID | Family | Target | HTTP | Model | Style | Combined | Guess | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | 0.1635 | 0.5898 | 0.2600 | unsure | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | 0.5943 | 0.1919 | 0.5138 | unsure | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | 0.6662 | 0.4163 | 0.6162 | unsure | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | 0.6114 | 0.5785 | 0.6048 | unsure | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | 0.3212 | 0.3137 | 0.3197 | unsure | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | 0.5727 | 0.2507 | 0.5083 | unsure | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | 0.5862 | 0.4546 | 0.5599 | unsure | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | 0.2452 | 0.5000 | 0.2962 | unsure | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | 0.7042 | 0.4055 | 0.6445 | unsure | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | 0.9792 | 0.7658 | 0.9365 | ai | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | 0.6175 | 0.4886 | 0.5917 | unsure | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | 0.7387 | 0.6225 | 0.7155 | unsure | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | 0.8051 | 0.5639 | 0.7569 | ai | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | 0.8329 | 0.4913 | 0.7646 | ai | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | 0.8005 | 0.6506 | 0.7705 | ai | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | 0.8814 | 0.4464 | 0.7400 | unsure | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | 0.8816 | 0.4441 | 0.7400 | unsure | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | 0.3223 | 0.5000 | 0.3578 | unsure | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | 0.4625 | 0.2917 | 0.4283 | unsure | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | 0.2044 | 0.2805 | 0.2196 | human | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | 0.5943 | 0.3741 | 0.5503 | unsure | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | 0.4998 | 0.4238 | 0.4846 | unsure | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | 0.6401 | 0.2708 | 0.5662 | unsure | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | 0.5583 | 0.4953 | 0.5457 | unsure | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | — | — | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | — | — | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | — | — | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | — | — | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | 0.9064 | 0.5000 | 0.7400 | unsure | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | — | — | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 415 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 415 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |


**Twelve real audit entries, including two rejected requests:**

```json
[
  {
    "timestamp": "2026-11-08T21:41:13+00:00",
    "content_id": "ea34f865-0fb8-4ea3-85e6-db7dd79aa253",
    "creator_id": "attacker_EV01",
    "guess": "unsure",
    "model_score": 0.1635,
    "style_score": 0.5898,
    "combined_score": 0.26,
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "status": "decided",
    "confidence": 0.26,
    "style_metrics": {
      "word_count": 85,
      "sentence_count": 7,
      "sentence_length_spread": 0.14881306636086492,
      "type_token_ratio": 0.8705882352941177,
      "punctuation_density": 0.01916376306620209,
      "evenness": 0.8139836670489189,
      "repetition": 0.04901960784313727,
      "punctuation_simplicity": 0.8403019744483159,
      "style_score": 0.5898
    },
    "text_length": 657,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:13+00:00",
    "content_id": "27cd33ce-fb2e-48fe-b357-d5d502b961f9",
    "creator_id": "attacker_EV02",
    "guess": "unsure",
    "model_score": 0.5943,
    "style_score": 0.1919,
    "combined_score": 0.5138,
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "status": "decided",
    "confidence": 0.5138,
    "style_metrics": {
      "word_count": 91,
      "sentence_count": 13,
      "sentence_length_spread": 0.8158554370668389,
      "type_token_ratio": 0.8241758241758241,
      "punctuation_density": 0.027597402597402596,
      "evenness": 0.0,
      "repetition": 0.12637362637362648,
      "punctuation_simplicity": 0.770021645021645,
      "style_score": 0.1919
    },
    "text_length": 708,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:13+00:00",
    "content_id": "e5d9c57c-d5a2-445a-90bc-e1fe0b017505",
    "creator_id": "attacker_EV05",
    "guess": "unsure",
    "model_score": 0.3212,
    "style_score": 0.3137,
    "combined_score": 0.3197,
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "status": "decided",
    "confidence": 0.3197,
    "style_metrics": {
      "word_count": 82,
      "sentence_count": 7,
      "sentence_length_spread": 0.6251710057549413,
      "type_token_ratio": 0.7682926829268293,
      "punctuation_density": 0.03684210526315789,
      "evenness": 0.21853624280632333,
      "repetition": 0.21951219512195125,
      "punctuation_simplicity": 0.6929824561403509,
      "style_score": 0.3137
    },
    "text_length": 460,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "b2eade58-4c96-4820-86fa-839c76954c62",
    "creator_id": "attacker_EV08",
    "guess": "unsure",
    "model_score": 0.2452,
    "style_score": 0.5,
    "combined_score": 0.2962,
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "status": "decided",
    "confidence": 0.2962,
    "style_metrics": {
      "word_count": 10,
      "sentence_count": 2,
      "sentence_length_spread": 0.2,
      "type_token_ratio": 1.0,
      "punctuation_density": 0.03571428571428571,
      "evenness": 0.5,
      "repetition": 0.0,
      "punctuation_simplicity": 0.7023809523809523,
      "style_score": 0.5
    },
    "text_length": 65,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "670d5fc0-a82a-4052-b59e-42cab1493d25",
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "model_score": 0.9792,
    "style_score": 0.7658,
    "combined_score": 0.9365,
    "label": "This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.",
    "status": "decided",
    "confidence": 0.9365,
    "style_metrics": {
      "word_count": 78,
      "sentence_count": 4,
      "sentence_length_spread": 0.3411316588628223,
      "type_token_ratio": 0.32051282051282054,
      "punctuation_density": 0.0064516129032258064,
      "evenness": 0.5735854264214721,
      "repetition": 0.9658119658119657,
      "punctuation_simplicity": 0.946236559139785,
      "style_score": 0.7658
    },
    "text_length": 544,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "fa4f6f1e-52a1-4bfc-bee2-59711ad02040",
    "creator_id": "attacker_FP03",
    "guess": "ai",
    "model_score": 0.8051,
    "style_score": 0.5639,
    "combined_score": 0.7569,
    "label": "This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.",
    "status": "decided",
    "confidence": 0.7569,
    "style_metrics": {
      "word_count": 83,
      "sentence_count": 7,
      "sentence_length_spread": 0.30384386055225276,
      "type_token_ratio": 0.7228915662650602,
      "punctuation_density": 0.020833333333333332,
      "evenness": 0.6201951743096841,
      "repetition": 0.2951807228915663,
      "punctuation_simplicity": 0.8263888888888888,
      "style_score": 0.5639
    },
    "text_length": 418,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "05dba30c-4a99-49a4-ba2f-904e1057fe6f",
    "creator_id": "attacker_FP04",
    "guess": "ai",
    "model_score": 0.8329,
    "style_score": 0.4913,
    "combined_score": 0.7646,
    "label": "This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.",
    "status": "decided",
    "confidence": 0.7646,
    "style_metrics": {
      "word_count": 68,
      "sentence_count": 8,
      "sentence_length_spread": 0.3429971702850177,
      "type_token_ratio": 0.8088235294117647,
      "punctuation_density": 0.023936170212765957,
      "evenness": 0.571253537143728,
      "repetition": 0.1519607843137255,
      "punctuation_simplicity": 0.800531914893617,
      "style_score": 0.4913
    },
    "text_length": 443,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "9b8e5d28-f5be-48b0-a6f0-9b476f9c7623",
    "creator_id": "attacker_FP05",
    "guess": "ai",
    "model_score": 0.8005,
    "style_score": 0.6506,
    "combined_score": 0.7705,
    "label": "This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.",
    "status": "decided",
    "confidence": 0.7705,
    "style_metrics": {
      "word_count": 70,
      "sentence_count": 7,
      "sentence_length_spread": 0.25634797778466234,
      "type_token_ratio": 0.5857142857142857,
      "punctuation_density": 0.027777777777777776,
      "evenness": 0.679565027769172,
      "repetition": 0.5238095238095238,
      "punctuation_simplicity": 0.7685185185185185,
      "style_score": 0.6506
    },
    "text_length": 393,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "0780e83a-4599-4611-9099-4ec7981afa7d",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "model_score": 0.2044,
    "style_score": 0.2805,
    "combined_score": 0.2196,
    "label": "This writing looks more consistent with human writing. This estimate does not verify who wrote it.",
    "status": "decided",
    "confidence": 0.2196,
    "style_metrics": {
      "word_count": 45,
      "sentence_count": 6,
      "sentence_length_spread": 0.595041237288706,
      "type_token_ratio": 0.9555555555555556,
      "punctuation_density": 0.02857142857142857,
      "evenness": 0.2561984533891176,
      "repetition": 0.0,
      "punctuation_simplicity": 0.7619047619047619,
      "style_score": 0.2805
    },
    "text_length": 322,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:14+00:00",
    "content_id": "15f5ee3b-d1ea-4ae5-9aaf-59fa1201635d",
    "creator_id": "attacker_MF07",
    "guess": "unsure",
    "model_score": 0.9064,
    "style_score": 0.5,
    "combined_score": 0.74,
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "status": "decided",
    "confidence": 0.74,
    "style_metrics": {
      "word_count": 17,
      "sentence_count": 1,
      "sentence_length_spread": 0.0,
      "type_token_ratio": 1.0,
      "punctuation_density": 0.011235955056179775,
      "evenness": 0.5,
      "repetition": 0.0,
      "punctuation_simplicity": 0.9063670411985019,
      "style_score": 0.5
    },
    "text_length": 105,
    "detector_model": "gpt2"
  },
  {
    "timestamp": "2026-11-08T21:41:15+00:00",
    "creator_id": "attacker_flood",
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "route": "/submit",
    "http_status": 429,
    "rate_limit_bucket": "creator:attacker_flood",
    "limit": "10 per 1 minute"
  },
  {
    "timestamp": "2026-11-08T21:41:15+00:00",
    "creator_id": "attacker_flood",
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "route": "/submit",
    "http_status": 429,
    "rate_limit_bucket": "creator:attacker_flood",
    "limit": "10 per 1 minute"
  }
]
```

**Worst outcome:** FP03 is designated in the supplied set as careful writing by
a non-native English speaker. It received model 0.8051, style 0.5639, combined
0.7569 and the AI label. Ordinary clear language crossed the original 0.75
boundary. This is the wrong accusation the system is intended to avoid. The
label warns it can be wrong and an appeal is available, but those do not erase
the reputational harm of the original result.


## Run Log and Verdicts

These are the **original five targets from Part 1**, tested three times with no
service changes between trials. `scenarios.py` configures each criterion once;
`run_eval.py::main` / `run_eval.py::trial_result` perform all HTTP calls and save
[the full before JSON](results/part2_eval_before.json) and
[the run log](results/part2_eval_before.md). Every miss is retained. Historical
human passages are the original fixed sourced corpus, not personal writing.
Supplemental synthetic label demonstrations remain excluded from score-spread
and false-positive groups.

### Before the improvement

| Criterion | Original target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Limit false accusations | At most 1/10 sourced human passages labeled AI in every trial | 0/10 AI flags; 10/10 valid | 0/10 AI flags; 10/10 valid | 0/10 AI flags; 10/10 valid | MET |
| 2. Separate contrasting inputs | Four-AI median minus first-four-human median >= 0.20 in every trial | median gap 0.247 | median gap 0.247 | median gap 0.247 | MET |
| 3. Cover all labels and scores | Actual human/unsure/ai labels and all 10,001 scores mapped; 0.51 differs from 0.95 | 3/3 labels; 10001 scores | 3/3 labels; 10001 scores | 3/3 labels; 10001 scores | MET |
| 4. Preserve usable appeals | 10/10 exact appeals, immutable decisions, fresh-process status, no rescoring; unknown ID404 | 10/10 appeals; persistence True | 10/10 appeals; persistence True | 10/10 appeals; persistence True | MET |
| 5. Reject bad input before scoring | All 18 validation groups return specified JSON400/404/413/415; no success events | 36/37 exact responses; 18/18 groups | 26/37 exact responses; 18/18 groups | 26/37 exact responses; 18/18 groups | MISSED |

The model scores are identical across trials. Criterion 5 differs because
invalid requests with missing/unusable creator IDs share an address quota:
the first trial consumes it and later trials are still inside the minute.
A 429 is safe rejection, but the original criterion explicitly requires
400/404/413/415, so it is **MISSED** rather than generously reinterpreted.
Valid scenario IDs are distinct per criterion/trial; no rejected call is
silently retried. The rate limiter remains enabled throughout.

**Criterion 1, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "5d7bfcfc-1113-4e62-9bca-55b7e5b20318",
  "creator_id": "eval-before-c1-t1-human-01",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-08T21:47:25+00:00"
}
```

**Criterion 2, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "d1ff719b-3927-4e73-91fb-2df7c4e1f144",
  "creator_id": "eval-before-c2-t1-human-01",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-08T21:47:26+00:00"
}
```

**Criterion 3, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "combined_score": 0.1628,
  "confidence": 0.1628,
  "content_id": "95a98c80-9ff4-4346-b0b6-2eb9c60ed1db",
  "creator_id": "eval-before-c3-t1-label-demo-synthetic-rare-prose",
  "detector_model": "gpt2",
  "guess": "human",
  "label": "This writing looks more consistent with human writing. This estimate does not verify who wrote it.",
  "model_score": 0.169,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.0,
    "punctuation_density": 0.037109375,
    "punctuation_simplicity": 0.6907552083333333,
    "repetition": 0.0,
    "sentence_count": 5,
    "sentence_length_spread": 1.151744635279055,
    "style_score": 0.1382,
    "type_token_ratio": 0.9054054054054054,
    "word_count": 74
  },
  "style_score": 0.1382,
  "text_length": 583,
  "timestamp": "2026-11-08T21:47:27+00:00"
}
```

**Criterion 4, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "content_id": "d81f39a4-f203-4fb5-aeea-ed5fd3e0cbd2",
  "creator_id": "eval-before-c4-t1-human-01",
  "event": "appeal",
  "message": "Your appeal has been recorded. This writing is now under review.",
  "reasoning": "Part 2 criterion review before, trial 1: please inspect this estimate.",
  "status": "under_review",
  "timestamp": "2026-11-08T21:47:28+00:00"
}
```

**Criterion 5, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "error": "rate_limited",
  "message": "Too many submissions. Try again shortly."
}
```


The complete per-case responses, 10-appeal histories, fresh-process content
checks, 10,001-score sweep, and exact-status validation cases are in the JSON.
Fresh-process checks show all ten appealed items under review with the detector
unloaded. Isolated service tests separately assert zero detector calls for
appeals and invalid input; a JSON response alone cannot establish call counts.


### Verdict decisions and diagnoses

- **Criterion 1 — MET:** 0/10 historical-human items labeled AI in every trial,
  against the original ceiling 1/10. The staff set's three false positives show
  that this development corpus is too narrow to establish modern-writer safety.
- **Criterion 2 — MET:** median gap 0.2470 exceeds 0.20 in every trial.
- **Criterion 3 — MET:** three labels and 10,001 mapped scores in every trial.
  The synthetic human-labeled item demonstrates reachability and evasion.
- **Criterion 4 — MET:** 10/10 appeals in every trial, exact reasoning and
  original decisions preserved, fresh-process status checks passed.
- **Criterion 5 — MISSED:**36/37, 26/37, 26/37 exact responses. Every miss is 429.
  **Stage:** rate-limit/route ordering. **Mechanism:** missing or invalid IDs
  share one address bucket, so the limiter rejects before the validation
  handler can return the specified 400/404/413/415. Successful events are unchanged.

Every broken attack has a stage and mechanism below; these are the reviewed
before outcomes, without changing the signals to fit individual attacks.

| ID | Stage | Measured mechanism |
|---|---|---|
| EV01 | signal one + combining rule | Typos coincide with model 0.1635 versus style 0.5898; the disagreement clamp yields 0.26. The AI item avoids the AI label even though the clamp prevents a human label. |
| EV02 | signal two + combining rule | Model 0.5943 and structural score 0.1919 combine to 0.5138. The edited sentence shape pulls an already intermediate model score into unsure. |
| EV03 | signal two + combining rule | The quotation-bearing item scores model 0.6662 and style 0.4163; their 80/20 result 0.6162 is below the AI threshold. Surface changes are not evidence of authorship. |
| EV04 | signal one | The unusual-word item receives model 0.6114, with style 0.5785. The model measures predictability, so surprising generated wording can avoid a high AI score. |
| EV05 | both signals | The edited AI item receives model 0.3212 and style 0.3137; both lean away from AI. The weighted 0.3197 remains unsure. |
| EV06 | signal two + combining rule | The uneven-length item has model 0.5727 and style 0.2507; combined 0.5083 remains unsure. Sentence-shape measures respond to editing rather than authorship. |
| EV07 | signal two + combining rule | Punctuation-bearing text scores style 0.4546 and model 0.5862, producing 0.5599. Punctuation changes the surface signal without establishing who wrote it. |
| EV08 | signal one + signal two | The short item gives model 0.2452 while style is neutral 0.5; their result 0.2962 is unsure. Limited text supplies little context and falls into the style short-text rule. |
| EV09 | both signals + combining rule | The mixed-origin item has model 0.7042 and style 0.4055, producing 0.6445. Aggregate signals cannot establish which parts were generated or how much editing occurred. |
| FP03 | signal one + label mapping | The supplied non-native-English example scores model 0.8051 and style 0.5639. Their 0.7569 crosses the original 0.75 AI boundary, so predictable plain language becomes a false accusation. |
| FP04 | signal one + label mapping | The supplied rubric-style essay scores model 0.8329 and style 0.4913. The 0.7646 result crosses the original AI boundary even though the set designates it human. |
| FP05 | signal one + label mapping | The supplied human technical prose scores model 0.8005 and style 0.6506. Agreement on regular language yields 0.7705, above the original AI boundary. |
| PI02 | signal one + combining rule | The instruction-prefixed content receives model 0.2044 and style 0.2805, producing human at 0.2196. This partially achieves the requested human classification, but it does not establish instruction execution: requested confidence 0.02 is not returned, and the ordinary scoring/label path still runs. |

The worst FP03 result and the opposing criterion 5 verdict were examined using
the assignment's working-alone AI prompts. Three hypotheses were requested
without a ranking, and an argument for MET was considered before retaining
MISSED against the literal target. Full prompts, responses, and the engineering
resolution: [feedback record](results/part2_feedback.json).

A separate [PI02 diagnostic](results/part2_pi02_diagnostic.json), excluded from
all official counts, removes only its instruction header. Model score changes
0.2044→0.7540, style 0.2805→0.2720, and the result becomes unsure 0.6576. This is
predictability sensitivity, not evidence that instructions were executed.


## The Improvement

**One change:** `config.py::AI_THRESHOLD` increased from **0.75 to 0.80**.
The diagnosis was FP03–FP05: scores 0.7569, 0.7646, 0.7705 were only slightly over
the old accusation boundary. Both signals, both weights, human threshold,
disagreement rule, validation, rate limits, and label sentences were retained.
[The change manifest](results/part2_change_manifest.json) verifies that only
`config.py` differs among runtime files since the instrumented baseline, and
its runtime diff is exactly this one setting. Original criteria and input
bytes are unchanged.

The service was restarted for the new setting. Both attack campaigns used a
fresh limiter process; each criteria campaign began after the address minute
window expired. No settings changed and no counters were reset between its
three trials. All HTTP responses are retained, including throttled invalid
requests. Same input order, caller scheme, model, and datasets were used.

| Measured outcome | Before | After |
|---|---|---|
| Official attack rows attempted | 56/56 | 56/56 |
| HELD | 43 | 46 |
| BROKE | 13 | 10 |
| Human-designated staff examples labeled AI | 3/8 | 0/8 |
| Generated evasion cases avoiding AI label | 9/10 | 9/10 |
| Partial PI02 human-classification success | 1 | 1 |
| Skipped attacks /5xx /transport failures | 0/0/0 | 0/0/0 |
| Source CSVs and numeric signal/combined scores | original | identical |

**Did it help?** Yes: the three observed false accusations became unsure,
with no other official attack outcome changing. It did not solve evasion or
the invalid-input exact-status miss. On any future AI input scoring in
`[0.75,0.80)`, the new rule will also return unsure; that is the cost of a wider
uncertainty band. The set did not measure that cost because its only examples
in this interval were the three human-designated false positives. These are
results on the same inspected staff set, not independent generalization evidence.

### Attack Run — After

All 56 attacks were rerun. Full requests/responses:
[after capture](results/attack_run_2026-11-08_1351_after.json).
Every row's scores and reviewed mark follow in the same format as before.

| ID | Family | Target | HTTP | Model | Style | Combined | Guess | Verdict |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | 0.1635 | 0.5898 | 0.2600 | unsure | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | 0.5943 | 0.1919 | 0.5138 | unsure | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | 0.6662 | 0.4163 | 0.6162 | unsure | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | 0.6114 | 0.5785 | 0.6048 | unsure | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | 0.3212 | 0.3137 | 0.3197 | unsure | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | 0.5727 | 0.2507 | 0.5083 | unsure | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | 0.5862 | 0.4546 | 0.5599 | unsure | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | 0.2452 | 0.5000 | 0.2962 | unsure | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | 0.7042 | 0.4055 | 0.6445 | unsure | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | 0.9792 | 0.7658 | 0.9365 | ai | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | 0.6175 | 0.4886 | 0.5917 | unsure | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | 0.7387 | 0.6225 | 0.7155 | unsure | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | 0.8051 | 0.5639 | 0.7569 | unsure | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | 0.8329 | 0.4913 | 0.7646 | unsure | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | 0.8005 | 0.6506 | 0.7705 | unsure | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | 0.8814 | 0.4464 | 0.7400 | unsure | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | 0.8816 | 0.4441 | 0.7400 | unsure | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | 0.3223 | 0.5000 | 0.3578 | unsure | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | 0.4625 | 0.2917 | 0.4283 | unsure | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | 0.2044 | 0.2805 | 0.2196 | human | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | 0.5943 | 0.3741 | 0.5503 | unsure | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | 0.4998 | 0.4238 | 0.4846 | unsure | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | 0.6401 | 0.2708 | 0.5662 | unsure | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | 0.5583 | 0.4953 | 0.5457 | unsure | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | — | — | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | — | — | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | — | — | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | — | — | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 200 | 0.9064 | 0.5000 | 0.7400 | unsure | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | — | — | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 415 | — | — | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 415 | — | — | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.5000 | 0.2600 | unsure | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | HELD |


### Every attack, before and after side by side

| ID | Before HTTP | Before guess | Before verdict | After HTTP | After guess | After verdict |
|---|---|---|---|---|---|---|
| EV01 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV02 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV03 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV04 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV05 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV06 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV07 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV08 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV09 | 200 | unsure | BROKE | 200 | unsure | BROKE |
| EV10 | 200 | ai | HELD | 200 | ai | HELD |
| FP01 | 200 | unsure | HELD | 200 | unsure | HELD |
| FP02 | 200 | unsure | HELD | 200 | unsure | HELD |
| FP03 | 200 | ai | BROKE | 200 | unsure | HELD |
| FP04 | 200 | ai | BROKE | 200 | unsure | HELD |
| FP05 | 200 | ai | BROKE | 200 | unsure | HELD |
| FP06 | 200 | unsure | HELD | 200 | unsure | HELD |
| FP07 | 200 | unsure | HELD | 200 | unsure | HELD |
| FP08 | 200 | unsure | HELD | 200 | unsure | HELD |
| PI01 | 200 | unsure | HELD | 200 | unsure | HELD |
| PI02 | 200 | human | BROKE | 200 | human | BROKE |
| PI03 | 200 | unsure | HELD | 200 | unsure | HELD |
| PI04 | 200 | unsure | HELD | 200 | unsure | HELD |
| PI05 | 200 | unsure | HELD | 200 | unsure | HELD |
| PI06 | 200 | unsure | HELD | 200 | unsure | HELD |
| MF01 | 400 | — | HELD | 400 | — | HELD |
| MF02 | 400 | — | HELD | 400 | — | HELD |
| MF03 | 400 | — | HELD | 400 | — | HELD |
| MF04 | 400 | — | HELD | 400 | — | HELD |
| MF05 | 400 | — | HELD | 400 | — | HELD |
| MF06 | 400 | — | HELD | 400 | — | HELD |
| MF07 | 200 | unsure | HELD | 200 | unsure | HELD |
| MF08 | 413 | — | HELD | 413 | — | HELD |
| RQ01 | 400 | — | HELD | 400 | — | HELD |
| RQ02 | 400 | — | HELD | 400 | — | HELD |
| RQ03 | 400 | — | HELD | 400 | — | HELD |
| RQ04 | 400 | — | HELD | 400 | — | HELD |
| RQ05 | 400 | — | HELD | 400 | — | HELD |
| RQ06 | 400 | — | HELD | 400 | — | HELD |
| RQ07 | 400 | — | HELD | 400 | — | HELD |
| RQ08 | 400 | — | HELD | 400 | — | HELD |
| RQ09 | 400 | — | HELD | 400 | — | HELD |
| RQ10 | 415 | — | HELD | 415 | — | HELD |
| RQ11 | 415 | — | HELD | 415 | — | HELD |
| RQ12 | 400 | — | HELD | 400 | — | HELD |
| FL01_01 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_02 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_03 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_04 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_05 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_06 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_07 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_08 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_09 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_10 | 200 | unsure | HELD | 200 | unsure | HELD |
| FL01_11 | 429 | — | HELD | 429 | — | HELD |
| FL01_12 | 429 | — | HELD | 429 | — | HELD |

### Five criteria after the change, three trials each

| Criterion | Original target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Limit false accusations | At most 1/10 sourced human passages labeled AI in every trial | 0/10 AI flags; 10/10 valid | 0/10 AI flags; 10/10 valid | 0/10 AI flags; 10/10 valid | MET |
| 2. Separate contrasting inputs | Four-AI median minus first-four-human median >= 0.20 in every trial | median gap 0.247 | median gap 0.247 | median gap 0.247 | MET |
| 3. Cover all labels and scores | Actual human/unsure/ai labels and all 10,001 scores mapped; 0.51 differs from 0.95 | 3/3 labels; 10001 scores | 3/3 labels; 10001 scores | 3/3 labels; 10001 scores | MET |
| 4. Preserve usable appeals | 10/10 exact appeals, immutable decisions, fresh-process status, no rescoring; unknown ID404 | 10/10 appeals; persistence True | 10/10 appeals; persistence True | 10/10 appeals; persistence True | MET |
| 5. Reject bad input before scoring | All 18 validation groups return specified JSON400/404/413/415; no success events | 36/37 exact responses; 18/18 groups | 26/37 exact responses; 18/18 groups | 26/37 exact responses; 18/18 groups | MISSED |

This is the same five-row format and the same targets as the before table.
Model/style/combined scores match exactly. Criterion 5 remains MISSED, with the
same 36/37, 26/37, 26/37 exact-status results; no new target was substituted.
Full after evidence: [JSON](results/part2_eval_after.json) and
[run log](results/part2_eval_after.md).

**Criterion 1, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "51450dcb-09a1-43ce-84ce-0419f521b5a8",
  "creator_id": "eval-after-c1-t1-human-01",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-08T21:53:15+00:00"
}
```

**Criterion 2, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "8d520d39-1760-4a4b-8aae-74e0c1094aea",
  "creator_id": "eval-after-c2-t1-human-01",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-08T21:53:15+00:00"
}
```

**Criterion 3, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "combined_score": 0.1628,
  "confidence": 0.1628,
  "content_id": "dc6ef482-3c40-4f08-9def-f5888a930ece",
  "creator_id": "eval-after-c3-t1-label-demo-synthetic-rare-prose",
  "detector_model": "gpt2",
  "guess": "human",
  "label": "This writing looks more consistent with human writing. This estimate does not verify who wrote it.",
  "model_score": 0.169,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.0,
    "punctuation_density": 0.037109375,
    "punctuation_simplicity": 0.6907552083333333,
    "repetition": 0.0,
    "sentence_count": 5,
    "sentence_length_spread": 1.151744635279055,
    "style_score": 0.1382,
    "type_token_ratio": 0.9054054054054054,
    "word_count": 74
  },
  "style_score": 0.1382,
  "text_length": 583,
  "timestamp": "2026-11-08T21:53:17+00:00"
}
```

**Criterion 4, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "content_id": "57f55524-8978-43d5-bc0b-e1396115c1d2",
  "creator_id": "eval-after-c4-t1-human-01",
  "event": "appeal",
  "message": "Your appeal has been recorded. This writing is now under review.",
  "reasoning": "Part 2 criterion review after, trial 1: please inspect this estimate.",
  "status": "under_review",
  "timestamp": "2026-11-08T21:53:17+00:00"
}
```

**Criterion 5, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.

```json
{
  "error": "rate_limited",
  "message": "Too many submissions. Try again shortly."
}
```


## What's Still Broken

The ten remaining BROKE attack IDs are listed individually below. The stopping
reason is the same for each: this submission declares one measured improvement, which
was reserved for reducing the most harmful observed false accusations. Further
signal or route changes would confound that comparison, so they are proposed
rather than silently applied.

| Remaining attack | Stage and remaining mechanism | Next experiment |
|---|---|---|
| EV01 | signal one + combining rule: Typos and word-level novelty lower the model score. | Test spelling-robust contextual features against genuine misspelled human writing before changing the signal. |
| EV02 | signal two + combining rule: Edited sentence shape lowers the style score. | Evaluate sentence-length normalization on held-out human and generated sentence edits. |
| EV03 | signal two + combining rule: Quotation-bearing mixed content stays below the AI boundary. | Test segment-level scoring and quoted-span handling, with quotation-rich human controls. |
| EV04 | signal one: Unusual generated wording avoids a high predictability score. | Evaluate a different independent contextual signal on rare-vocabulary human and AI samples. |
| EV05 | both signals: The heavily edited item has low readings from both signals. | Treat mixed authorship as uncertain; test voluntary draft evidence rather than assuming editing can be detected reliably. |
| EV06 | signal two + combining rule: Extreme sentence-length variation depresses the structural result. | Test length-aware feature weighting with short and long human prose, without tuning on this single attack. |
| EV07 | signal two + combining rule: Punctuation changes the structural features. | Compare punctuation-normalized features against expressive human writing and poetry. |
| EV08 | signal one + signal two: Short text has little model context and neutral style. | Keep an unsure outcome for insufficient context; evaluate length-stratified targets before making stronger labels. |
| EV09 | both signals + combining rule: A human opening changes the aggregate view of mixed text. | Test bounded segment/window scoring beyond the first 400 tokens, with measured CPU and false-positive costs. |
| PI02 | signal one + combining rule: A novel instruction header changes predictability enough to produce human. | Test separate header/body scoring with legitimate quoted-instruction controls; preserve fixed output labels and safe JSON. |

**Criterion 5 still MISSED:** the rate limiter can replace required validation
codes with 429 for malformed requests sharing an exhausted address bucket.
Next, test a cheap validation-before-quota arrangement together with a separate
address-level abuse cap. Keep the original target and measure whether it is
met; merely adding 429 to the accepted target after observing a miss would hide
the failure. This route/limiter change was not bundled with the one threshold
improvement.

**Other known limits:** creator IDs are unverified and can be rotated, limiter
state resets on restart, and a single-process memory store does not coordinate
multiple workers. The historical development corpus is small and can overlap
GPT-2 training data. The rare-word synthetic AI demonstration still receives
a human label, and neither a label nor a successful appeal verifies authorship.
Authenticated identity, durable shared limit storage, representative independent
writing samples, and an actual human review process are future work.

**Production trade:** I would prefer an unsure result and a usable appeal over
a confident accusation when the evidence is weak. That choice lets more AI
writing pass without an AI label and increases review work for the site, while
reducing the risk that an ordinary writer bears the cost of a false accusation.

The original `criteria.md` was retained byte-for-byte. Both complete attack
runs, both five-row/three-trial run logs, all reviewed verdicts/diagnoses,
twelve pasted audit events including rejections, and the sole runtime-change
manifest are included. The submission uses the same repository:
https://github.com/sawantamar05/ai201-project4-provenance-guard-starter-v2026

## Capstone

**What This Extends**

I extended the existing Provenance Guard Flask API with predictable validation
and quota handling, plus durable request completion records and measured run
cost. This is the same repository and detector from Project 4. The new targets
are in [criteria.md](criteria.md); the earlier targets are preserved unchanged in
[docs/criteria_parts1_2.md](docs/criteria_parts1_2.md). The criteria existed in Git
before capstone evaluation, and both campaigns record the identical criteria
SHA-256 `b54324f9b43cecf68ba911daec030a362ae5d7dae9243d85591440193f22ed14`.

**The Shape**

I chose **B — Harden against failure**: malformed submissions should receive
their validation error without consuming the allowance for valid scoring.
Request timing, failure traces, and the local run path support that one change.
Model retraining, threshold changes, a new interface, public hosting,
authenticated identities, and shared quota storage stayed outside this unit.
No stretch work was declared. The before campaign is an instrumented baseline
with the old quota order, not the original uninstrumented starter.

**Running It**

I used **Path B — local with logs**. [RUNNING.md](RUNNING.md) gives the exact
single-worker Gunicorn start command, pinned setup, model preparation, isolated
log directories, and clean-checkout verification. The environment and model
inventory are recorded in [docs/capstone_environment.md](docs/capstone_environment.md).
Each trial started an actual local HTTP server outside the editor. Criterion 5
stopped that server and started a fresh process against the same saved audit.
The committed campaigns include the launch commands, process records, HTTP
captures, request logs, and both five-row run logs.

I also verified a [clean checkout](results/capstone/clean_checkout.json) at
commit `bc3ebad`: a fresh clone and new virtual environment
installed all **40 exact dependency pins**, and **all nine checks passed**,
including real inference, exact appeal persistence across a restart, and saved
request completions. This reused the previously downloaded GPT-2 cache
explicitly; it was not an online model-download test.

**Instrumentation**

`telemetry.start_request` starts before validation and rate limiting;
`telemetry.complete_request` writes one `request_completed` record to
`requests.jsonl`, separately from decision/appeal events in `audit.jsonl`.
Each completion contains a UTC timestamp, a generated request ID matching
`X-Request-ID`, method/path, response status, input/output summaries, wall
duration, and process CPU seconds. Input summaries retain byte counts, JSON
field names, parsing outcome, and text length; output summaries retain content
ID, guess, status, or error. Submission text and appeal-reasoning values are
omitted from this new log. The appeal audit still preserves reasoning exactly.

These **13 actual entries** are the first ten valid submissions, two quota
rejections, and one malformed-input rejection from after criterion 3, trial 1.
They are pasted from [that session's request log](results/capstone/after/c3_trial1_attempt1/requests.jsonl),
with their values unchanged:

```jsonl
{"event":"request_completed","request_id":"fe84b749-c360-4274-adf2-b909bfcb26a9","timestamp":"2026-11-14T02:08:36.668086+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":425,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":377},"output_summary":{"content_type":"application/json","content_id":"c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":41.651125,"cpu_seconds":0.057285}
{"event":"request_completed","request_id":"72666c6a-95a2-41b4-9b19-933298884426","timestamp":"2026-11-14T02:08:36.735804+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":712,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":664},"output_summary":{"content_type":"application/json","content_id":"6819356d-16fd-4af2-ac8d-427ccd77d8b1","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":66.5395,"cpu_seconds":0.103893}
{"event":"request_completed","request_id":"8b4763dd-0899-4d96-ad07-59bd1d78ed2f","timestamp":"2026-11-14T02:08:36.815425+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":863,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":795},"output_summary":{"content_type":"application/json","content_id":"936748de-1092-4b15-bb75-990b6d08b172","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":78.103458,"cpu_seconds":0.120754}
{"event":"request_completed","request_id":"dc168320-cd9a-450b-a740-34c0d53a41b0","timestamp":"2026-11-14T02:08:36.877295+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":625,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":552},"output_summary":{"content_type":"application/json","content_id":"233953a6-b49d-4e94-a9e0-45b40e24d163","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":60.5475,"cpu_seconds":0.090943}
{"event":"request_completed","request_id":"0e0f9643-6637-4945-929b-a508f44a391a","timestamp":"2026-11-14T02:08:36.921350+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":402,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":354},"output_summary":{"content_type":"application/json","content_id":"32e41624-5dac-43c3-bd39-6fe90b89b350","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":42.961041,"cpu_seconds":0.059885}
{"event":"request_completed","request_id":"a3c8ef24-21d4-408b-9326-5a5ae2d99ce9","timestamp":"2026-11-14T02:08:36.970403+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":549,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":501},"output_summary":{"content_type":"application/json","content_id":"8fd73fc5-e4b1-4d88-90bd-4a98c3588963","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":47.942708,"cpu_seconds":0.068713}
{"event":"request_completed","request_id":"ce18c836-0838-4731-ac70-91dc42efbfa9","timestamp":"2026-11-14T02:08:37.028421+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":660,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":592},"output_summary":{"content_type":"application/json","content_id":"fabcb982-4380-4deb-9b83-dee5dbf6f14a","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":56.94575,"cpu_seconds":0.086038}
{"event":"request_completed","request_id":"3025ea5e-a91e-4957-a334-c45f19cb4486","timestamp":"2026-11-14T02:08:37.084192+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":661,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":598},"output_summary":{"content_type":"application/json","content_id":"c202a331-b153-49b6-8f5e-9bc5f46f33b2","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":54.717125,"cpu_seconds":0.081653}
{"event":"request_completed","request_id":"126a95a7-262f-48e7-8f27-e7115bb886a2","timestamp":"2026-11-14T02:08:37.135760+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":572,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":524},"output_summary":{"content_type":"application/json","content_id":"c493eeb2-d84b-4ae4-bd58-f1090572c2fe","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":50.487709,"cpu_seconds":0.072724}
{"event":"request_completed","request_id":"e30fbad1-099f-4883-8848-fd1843cee592","timestamp":"2026-11-14T02:08:37.225457+00:00","method":"POST","path":"/submit","http_status":200,"input_summary":{"body_bytes":674,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":626},"output_summary":{"content_type":"application/json","content_id":"7a7c25b6-f8ff-491b-ae83-25e5a22b9830","guess":"unsure","status":"decided","outcome":"success"},"duration_ms":88.540667,"cpu_seconds":0.110455}
{"event":"request_completed","request_id":"4808f340-ebe1-4ef5-8eff-eb7c46654878","timestamp":"2026-11-14T02:08:37.227083+00:00","method":"POST","path":"/submit","http_status":429,"input_summary":{"body_bytes":425,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":377},"output_summary":{"content_type":"application/json","error":"rate_limited","outcome":"error"},"duration_ms":0.413625,"cpu_seconds":0.000405}
{"event":"request_completed","request_id":"49983aa0-838e-40fc-a4ad-7592e9873abc","timestamp":"2026-11-14T02:08:37.228216+00:00","method":"POST","path":"/submit","http_status":429,"input_summary":{"body_bytes":425,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":377},"output_summary":{"content_type":"application/json","error":"rate_limited","outcome":"error"},"duration_ms":0.262084,"cpu_seconds":0.000251}
{"event":"request_completed","request_id":"722f9fc2-8542-46c0-bf63-12a522d13355","timestamp":"2026-11-14T02:08:37.229079+00:00","method":"POST","path":"/submit","http_status":400,"input_summary":{"body_bytes":56,"content_type":"application/json","parsing":"json_object","field_names":["creator_id","text"],"field_count":2,"field_names_truncated":false,"text_characters":0},"output_summary":{"content_type":"application/json","error":"invalid_text","outcome":"error"},"duration_ms":0.140083,"cpu_seconds":0.000128}
```

All 23 measured requests had exactly one correlated completion in each before
and after trial, including validation 400, quota 429, and unknown-appeal 404.
Healthy writable storage is part of this measurement: a failed log write cannot
produce a durable record. The service exposes that failure as JSON 503 and a
server error log, and the isolated telemetry tests check that behavior.

**What It Costs**

One run here means one accepted, warm paragraph submission. In after criterion
4, trial 1, I measured ten real requests: **0.0820445 process CPU seconds per
run** and **0.0558259 seconds mean client wall time**. The CPU sample sum was
`0.820445 / 10 = 0.0820445`; the raw ten CPU and wall samples,
correlation IDs, method, and arithmetic are in
[results/capstone/cost.json](results/capstone/cost.json).

The worker uses `time.process_time()` before/after route handling and summary
preparation, before completion serialization/fsync. Client wall time includes
the complete response and JSON parsing, including the log append. CPU time
excludes initial model load, completion serialization/fsync, and client/network
CPU. Torch can use multiple CPU threads, so process CPU time can exceed wall
time even with one synchronous HTTP worker. Repeated measurements were trial 2: 0.0835370 CPU-s, 0.0583841 wall-s; trial 3: 0.0826680 CPU-s, 0.0562143 wall-s.
Cold model-loading requests were disclosed separately: 1.5194s, 1.5328s, 1.5560s
in the three after timing trials.

For **100 people per day, one accepted warm submission each**:
`100 × 0.0820445 = 8.20445 process CPU seconds/day`.
Appeals, additional requests, and cold loads add work beyond this multiplication.
No paid inference API was called in these offline sessions. Electricity and
hosting dollars were not measured, so these numbers are a compute measurement
rather than a dollar-cost claim.

**Run Log and Verdicts**

The before campaign used commit `2189501`. I ran all five
criteria three times without changing the system between trials. A target had
to hold in every trial; the two missed criteria remain **MISSED** here.
Full outputs: [before JSON](results/capstone/before/report.json) and
[before run log](results/capstone/before/report.md).

| Criterion | Target | Run1 | Run2 | Run3 | Verdict |
|---|---|---|---|---|---|
| 1. Validation errors under quota pressure | 20/20 exact JSON validation responses; no malformed scoring/success events | 10/20 exact; no-success-events=True; isolated=True | 10/20 exact; no-success-events=True; isolated=True | 10/20 exact; no-success-events=True; isolated=True | MISSED |
| 2. Malformed requests preserve scoring allowance | 12/12 invalid400; then ten200 and two429; exactly10 isolated detector calls | 10/12 invalid400; 0/10 valid200; 2/2 quota429; isolated=False | 10/12 invalid400; 0/10 valid200; 2/2 quota429; isolated=False | 10/12 invalid400; 0/10 valid200; 2/2 quota429; isolated=False | MISSED |
| 3. Complete durable request records | 23/23 durable unique correlated completion records with required redacted fields | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | MET |
| 4. Warm submission response time | 10/10 complete decisions; at least9/10 warm requests below5.0s | 10/10 decisions; 10/10<5s; mean0.0579s | 10/10 decisions; 10/10<5s; mean0.0548s | 10/10 decisions; 10/10<5s; mean0.0710s | MET |
| 5. Appeals survive server restart | 10/10 exact persistent appeals; unchanged originals; unknown404; zero rescoring | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | MET |

**Diagnosis of criterion 1:** the Flask-Limiter request hook ran before
`submit` reached validation. After ten valid submissions, the creator bucket
returned 429 for malformed requests with that ID. Separately, malformed requests
without a usable ID filled the address fallback bucket. All ten pressure-matrix
cases therefore received 429 rather than their required 400/413/415; all ten
ordinary cases were correct. The stage was quota enforcement, and the mechanism
was validation occurring after quota lookup and accounting.

**Diagnosis of criterion 2:** the same ordering charged the first ten empty-text
requests to the valid creator's ten-slot bucket. The last two malformed requests
then returned 429, and all twelve subsequent valid requests were throttled.
This left 10/12 invalid 400 responses and zero accepted valid requests in every
trial. Both misses were one request-ordering problem with two effects.

Criteria 3–5 were **MET**: completion records covered all 23 measured requests,
all ten warm submissions returned complete decisions below 5s, and all ten
appeals survived an actual restart without rescoring. Those results cover this
small serial local workload; they do not establish accuracy, production load
capacity, or durability when the disk itself cannot accept a write.

**Criterion 1 — actual output (before)**

Before trial 1, pressure case 1: expected HTTP 400, actual HTTP 429. Produced by `scripts/run_capstone.py::criterion_one`; complete request/response in [the pressure capture](results/capstone/before/c1_trial1_attempt1/pressure/http_01.json).

```json
{
  "error": "rate_limited",
  "message": "Too many submissions. Try again shortly."
}
```

**Criterion 2 — actual output (before)**

Before trial 1, first valid request after 12 malformed requests: HTTP 429. Produced by `scripts/run_capstone.py::criterion_two`; saved in [the trial capture](results/capstone/before/c2_trial1_attempt1/http_01.json).

```json
{
  "error": "rate_limited",
  "message": "Too many submissions. Try again shortly."
}
```

**Criterion 3 — actual output (before)**

Before trial 1, one actual durable completion. Produced by `telemetry.py::complete_request` and checked by `scripts/run_capstone.py::criterion_three`; saved in [the request log](results/capstone/before/c3_trial1_attempt1/requests.jsonl).

```json
{
  "event": "request_completed",
  "request_id": "242e68d0-8474-453e-91f2-8619384ac3d4",
  "timestamp": "2026-11-14T02:05:07.604929+00:00",
  "method": "POST",
  "path": "/submit",
  "http_status": 200,
  "input_summary": {
    "body_bytes": 426,
    "content_type": "application/json",
    "parsing": "json_object",
    "field_names": [
      "creator_id",
      "text"
    ],
    "field_count": 2,
    "field_names_truncated": false,
    "text_characters": 377
  },
  "output_summary": {
    "content_type": "application/json",
    "content_id": "44ae0c19-92ce-45a7-9ce8-78f693d63907",
    "guess": "unsure",
    "status": "decided",
    "outcome": "success"
  },
  "duration_ms": 39.614958,
  "cpu_seconds": 0.054686
}
```

**Criterion 4 — actual output (before)**

Before trial 1, first timed warm response. This projection preserves the actual status, elapsed time, complete response JSON, and request ID. Produced by `scripts/run_capstone.py::criterion_four`; full capture in [the trial HTTP record](results/capstone/before/c4_trial1_attempt1/http_01.json).

```json
{
  "status_code": 200,
  "elapsed_seconds": 0.04311654111370444,
  "response_json": {
    "combined_score": 0.6593,
    "confidence": 0.6593,
    "content_id": "d8d35d00-40e2-4ef5-950f-63dcdaba0d89",
    "creator_id": "cap-before-c4-t1-a1-human-01",
    "detector_model": "gpt2",
    "guess": "unsure",
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "model_score": 0.6922,
    "status": "decided",
    "style_metrics": {
      "evenness": 0.5,
      "punctuation_density": 0.016286644951140065,
      "punctuation_simplicity": 0.8642779587404994,
      "repetition": 0.34976525821596255,
      "sentence_count": 2,
      "sentence_length_spread": 0.352112676056338,
      "style_score": 0.5278,
      "type_token_ratio": 0.6901408450704225,
      "word_count": 71
    },
    "style_score": 0.5278,
    "text_length": 377,
    "timestamp": "2026-11-14T02:05:15+00:00"
  },
  "request_id": "095de458-c1b0-4120-bfc4-e3288678c2ee"
}
```

**Criterion 5 — actual output (before)**

Before trial 1, actual content response from the restarted server: HTTP 200. Produced by `scripts/run_capstone.py::criterion_five`; saved in [the restarted-process capture](results/capstone/before/c5_trial1_attempt1/http_02.json).

```json
{
  "appeals": [
    {
      "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
      "creator_id": "cap-before-c5-t1-a1-human-01",
      "event": "appeal",
      "reasoning": "  Capstone review 1: please consider my drafts.  ",
      "status": "under_review",
      "timestamp": "2026-11-14T02:05:24+00:00"
    }
  ],
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "23706e24-26fa-4ac4-ae8c-7dedc0951a30",
  "creator_id": "cap-before-c5-t1-a1-human-01",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "under_review",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-14T02:05:23+00:00"
}
```


**The Improvement**

I made **one runtime improvement**: validate cheap submission input before
Flask-Limiter checks/charges scoring quota. A request hook now calls
`app.py::_validate_submission` and caches the valid text/creator tuple in
`g.validated_submission`; `submit` reuses it. Invalid requests return their
400/413/415 immediately and do not consume the model-scoring allowance. Valid
requests still receive ten slots per minute and 200 per day, and the next two
valid requests in the registered burst still return 429.

Only `app.py` differs among the frozen runtime/harness/input source hashes
between the campaigns. Model, thresholds, signal weights, corpus, quotas,
telemetry, and the evaluation protocol remained unchanged. The after campaign
used commit `2643b2b` and repeated the full five criteria,
three trials each. Sources: [after JSON](results/capstone/after/report.json) and
[after run log](results/capstone/after/report.md).

| Criterion | Target | Run1 | Run2 | Run3 | Verdict |
|---|---|---|---|---|---|
| 1. Validation errors under quota pressure | 20/20 exact JSON validation responses; no malformed scoring/success events | 20/20 exact; no-success-events=True; isolated=True | 20/20 exact; no-success-events=True; isolated=True | 20/20 exact; no-success-events=True; isolated=True | MET |
| 2. Malformed requests preserve scoring allowance | 12/12 invalid400; then ten200 and two429; exactly10 isolated detector calls | 12/12 invalid400; 10/10 valid200; 2/2 quota429; isolated=True | 12/12 invalid400; 10/10 valid200; 2/2 quota429; isolated=True | 12/12 invalid400; 10/10 valid200; 2/2 quota429; isolated=True | MET |
| 3. Complete durable request records | 23/23 durable unique correlated completion records with required redacted fields | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | 23/23 complete records; HTTP sequence=True | MET |
| 4. Warm submission response time | 10/10 complete decisions; at least9/10 warm requests below5.0s | 10/10 decisions; 10/10<5s; mean0.0558s | 10/10 decisions; 10/10<5s; mean0.0584s | 10/10 decisions; 10/10<5s; mean0.0562s | MET |
| 5. Appeals survive server restart | 10/10 exact persistent appeals; unchanged originals; unknown404; zero rescoring | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | 10/10 persistent appeals; unknown404=True; model unloaded=True; isolated=True | MET |

| Criterion | Before, all three trials | After, all three trials | Change |
|---|---|---|---|
| 1. Validation under pressure | 10/20 exact; MISSED | 20/20 exact; MET | Pressure cases now return their validation code |
| 2. Scoring allowance | 10/12 invalid 400; 0/10 valid 200; MISSED | 12/12 invalid 400; 10/10 valid 200; MET | Invalid requests no longer consume valid slots |
| 3. Request completions | 23/23; MET | 23/23; MET | Complete records retained |
| 4. Warm response time | 10/10 complete and below 5s; MET | 10/10 complete and below 5s; MET | Target retained; timing variation is not a claimed speedup |
| 5. Persistent appeals | 10/10; MET | 10/10; MET | Appeal protection retained |

The improvement helped the diagnosed failure: exact validation responses rose
from 10/20 to 20/20, and accepted valid allowance requests rose from 0/10 to 10/10
in every trial. The other three criteria remained MET. Mean warm client times
were 0.0579s, 0.0548s, 0.0710s before and
0.0558s, 0.0584s, 0.0562s after; this small variation does not
support a claim that validation ordering made model inference faster.

**Criterion 1 — actual output (after)**

After trial 1, pressure case 1: expected HTTP 400, actual HTTP 400. Produced by `scripts/run_capstone.py::criterion_one`; complete request/response in [the pressure capture](results/capstone/after/c1_trial1_attempt1/pressure/http_01.json).

```json
{
  "error": "invalid_text",
  "message": "text must be a nonempty string."
}
```

**Criterion 2 — actual output (after)**

After trial 1, first valid request after 12 malformed requests: HTTP 200. Produced by `scripts/run_capstone.py::criterion_two`; saved in [the trial capture](results/capstone/after/c2_trial1_attempt1/http_01.json).

```json
{
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "646310d0-f8ff-4de8-b831-5749061fae66",
  "creator_id": "cap-after-c2-t1-a1",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "decided",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-14T02:08:28+00:00"
}
```

**Criterion 3 — actual output (after)**

After trial 1, one actual durable completion. Produced by `telemetry.py::complete_request` and checked by `scripts/run_capstone.py::criterion_three`; saved in [the request log](results/capstone/after/c3_trial1_attempt1/requests.jsonl).

```json
{
  "event": "request_completed",
  "request_id": "fe84b749-c360-4274-adf2-b909bfcb26a9",
  "timestamp": "2026-11-14T02:08:36.668086+00:00",
  "method": "POST",
  "path": "/submit",
  "http_status": 200,
  "input_summary": {
    "body_bytes": 425,
    "content_type": "application/json",
    "parsing": "json_object",
    "field_names": [
      "creator_id",
      "text"
    ],
    "field_count": 2,
    "field_names_truncated": false,
    "text_characters": 377
  },
  "output_summary": {
    "content_type": "application/json",
    "content_id": "c6c6d5e7-e8fb-4713-a709-a9aa747f7b6b",
    "guess": "unsure",
    "status": "decided",
    "outcome": "success"
  },
  "duration_ms": 41.651125,
  "cpu_seconds": 0.057285
}
```

**Criterion 4 — actual output (after)**

After trial 1, first timed warm response. This projection preserves the actual status, elapsed time, complete response JSON, and request ID. Produced by `scripts/run_capstone.py::criterion_four`; full capture in [the trial HTTP record](results/capstone/after/c4_trial1_attempt1/http_01.json).

```json
{
  "status_code": 200,
  "elapsed_seconds": 0.04083670908585191,
  "response_json": {
    "combined_score": 0.6593,
    "confidence": 0.6593,
    "content_id": "8f82248e-5fb6-4432-bf10-af9cf086ead9",
    "creator_id": "cap-after-c4-t1-a1-human-01",
    "detector_model": "gpt2",
    "guess": "unsure",
    "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
    "model_score": 0.6922,
    "status": "decided",
    "style_metrics": {
      "evenness": 0.5,
      "punctuation_density": 0.016286644951140065,
      "punctuation_simplicity": 0.8642779587404994,
      "repetition": 0.34976525821596255,
      "sentence_count": 2,
      "sentence_length_spread": 0.352112676056338,
      "style_score": 0.5278,
      "type_token_ratio": 0.6901408450704225,
      "word_count": 71
    },
    "style_score": 0.5278,
    "text_length": 377,
    "timestamp": "2026-11-14T02:08:44+00:00"
  },
  "request_id": "365d8021-2758-4f2f-a2c5-199e1e2c059b"
}
```

**Criterion 5 — actual output (after)**

After trial 1, actual content response from the restarted server: HTTP 200. Produced by `scripts/run_capstone.py::criterion_five`; saved in [the restarted-process capture](results/capstone/after/c5_trial1_attempt1/http_02.json).

```json
{
  "appeals": [
    {
      "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
      "creator_id": "cap-after-c5-t1-a1-human-01",
      "event": "appeal",
      "reasoning": "  Capstone review 1: please consider my drafts.  ",
      "status": "under_review",
      "timestamp": "2026-11-14T02:08:52+00:00"
    }
  ],
  "combined_score": 0.6593,
  "confidence": 0.6593,
  "content_id": "8d132cf2-9582-4769-a4ce-75b4555f197a",
  "creator_id": "cap-after-c5-t1-a1-human-01",
  "detector_model": "gpt2",
  "guess": "unsure",
  "label": "We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.",
  "model_score": 0.6922,
  "status": "under_review",
  "style_metrics": {
    "evenness": 0.5,
    "punctuation_density": 0.016286644951140065,
    "punctuation_simplicity": 0.8642779587404994,
    "repetition": 0.34976525821596255,
    "sentence_count": 2,
    "sentence_length_spread": 0.352112676056338,
    "style_score": 0.5278,
    "type_token_ratio": 0.6901408450704225,
    "word_count": 71
  },
  "style_score": 0.5278,
  "text_length": 377,
  "timestamp": "2026-11-14T02:08:52+00:00"
}
```


**What's Still Broken**

All five after criteria were MET, but the warm-latency target was too generous
for this measured workload. The slowest of all 30 after warm requests was
0.0815253s. In a future registration I would tighten criterion 4 from 9/10
below 5s to **10/10 below 0.25s** on the same hardware and frozen passages. I have
kept the current target and both original result sets unchanged.

Creator IDs remain caller supplied and can be rotated to bypass a quota.
In-memory counters reset when the server restarts and do not coordinate
multiple workers. Invalid requests no longer spend scoring quota, so they need
a separate front-door abuse cap if this becomes a public service. Completion
logging depends on writable disk: an append failure can return 503 after a
decision has already been persisted, requiring operator inspection before a
retry. The detector remains a heuristic, not proof of authorship; these
historical passages and repeated engineering trials do not establish general
authorship accuracy. I stopped at the scoped validation/quota improvement and
kept the service local rather than expand this unit into an identity, hosting,
or storage redesign.

With another unit, I would first tie submission quotas to an authenticated
caller identity, because rotating a self-declared ID bypasses the present
control. I would validate that identity boundary before adding shared durable
quota storage, so persistence does not preserve the wrong ownership model.

**How I Used AI**

I asked Codex to compare my four CodePath systems against this brief. It
recommended Provenance Guard's existing API and recorded validation/quota miss;
I selected Shape B and kept model training and a new interface outside the scope.

I asked Codex to draft first-person criteria and told it that my instructor
permits this assistance. It supplied targets, reasons, and test procedures;
review clarified that creator and address quotas need separate pressure and
that request completions must be counted separately from decision/appeal audit
events. This was AI-assisted drafting and review, not unaided criteria writing
or a peer review session.

I then asked Codex to implement, instrument, and evaluate the bounded extension.
It produced the real-HTTP runner and explicitly mocked call-count companion.
The baseline showed two misses with the same quota-ordering mechanism, so the
measured change moved validation before quota accounting and retained both
result sets. AI also generated this write-up from the saved responses and CPU
samples; the JSON/JSONL artifacts, source hashes, and commit history are the
evidence behind the claims.

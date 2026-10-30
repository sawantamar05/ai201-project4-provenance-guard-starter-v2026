# Acceptance criteria — Provenance Guard

These targets are fixed before implementation and before detector results.
Evaluate each target in three trials; it must hold in every trial. Save input
membership and source/generation provenance with the evaluation inputs.

## 1. Limit false accusations

On a frozen set of 10 human-written passages published before 1920, at most
1 passage per trial may receive the high-confidence AI label. Include literature,
first-person prose, and formal nonfiction, with traceable public-domain sources.

**Why this target:** A mistaken accusation harms a writer more than an unsure
decision. A 10% ceiling is a small-sample target, not a population accuracy
estimate. Historical passages do not represent all present-day writers and
are not the submitter's own writing.

## 2. Separate contrasting inputs

On 4 frozen AI-generated paragraphs and the first 4 sourced human passages,
the median combined score of the AI group must exceed the human median by
at least 0.20 in each trial. Record both signals and the combined score.

**Why this target:** A constant middle score would avoid accusations without
being useful. A 0.20 gap requires meaningful variation while allowing overlap
and individual mistakes.

## 3. Cover uncertainty and all three labels

At least one real submission in the demonstration set must produce each of
`human`, `unsure`, and `ai`. Independently map all 10,001 scores from 0.0000 to
1.0000 in steps of 0.0001 to exactly one nonempty label. Scores 0.51 and 0.95
must produce different labels; check both threshold boundaries explicitly.

**Why this target:** The uncertainty band must be usable. A score sweep catches
gaps and boundary errors that a few examples could overlook.

## 4. Preserve a usable appeal path

For 10 valid appeals against existing content IDs, all 10 responses must confirm
`under_review`, retain the exact reasoning, and append an appeal without
altering the original decision or invoking the detector. A fresh service
instance reading the same log must preserve each status. Unknown IDs return
JSON HTTP 404 and create no appeal event.

**Why this target:** Writers need a reliable challenge path even when the
detector is unavailable. Keeping original events makes decisions inspectable.

## 5. Reject bad input before scoring

All 18 cases in `docs/design.md` must return their specified JSON HTTP 400,
404, 413, or 415 without invoking the detector or recording a successful
decision/appeal. Valid text is 20–10,000 characters and at least 5 word tokens;
creator IDs are 1–128 characters; reasoning is 1–2,000 characters. Bodies
above 65,536 bytes return HTTP 413.

**Why this target:** Bounded validation prevents crashes and unnecessary model
calls while allowing paragraphs, short submissions, and substantial appeals.

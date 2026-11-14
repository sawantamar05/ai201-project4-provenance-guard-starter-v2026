# Acceptance criteria review

Prepared October 30, 2026, with AI assistance at the user's request, after the
initial evaluation. This plain-language draft restates the original five
engineering targets and explains how to check them. The canonical pre-results
targets are archived in [criteria_parts1_2.md](criteria_parts1_2.md), with their original history.
This review is not a new pre-results registration or a claim of personal
student authorship.

## 1. Keep false accusations below the development ceiling

**Draft:** In each of three trials, at most one of the ten frozen, sourced
human-written passages may receive the high-confidence AI label.

**Reason:** A wrong accusation can harm a writer's reputation. An unsure result
is preferable to a confident accusation when the evidence is weak. This small
historical set is a development check, not a claim that a 10% error rate is
acceptable in production.

**Check:** Count AI guesses in the ten-human group separately for each trial.
The target must hold in every trial; averaging the trials cannot hide a miss.

## 2. Produce meaningfully different scores for contrasting examples

**Draft:** In each trial, the median combined score of the four frozen generated
paragraphs must be at least 0.20 above the median of the first four sourced
human passages. Save both individual signals and the combined score.

**Reason:** A detector that returns the same middle value for everything is not
useful. Comparing medians tests separation while allowing individual overlap.
It does not establish accuracy for writing outside these examples.

**Check:** Compute the two four-item medians and subtract human from generated.
Use the frozen groups rather than choosing new examples after seeing scores.

## 3. Make human, unsure, and AI labels reachable without score gaps

**Draft:** Actual submitted examples must reach all three labels. All 10,001
scores from 0.0000 through 1.0000 must map to exactly one nonempty label. Check
both boundaries and verify that 0.51 and 0.95 receive different labels.

**Reason:** The service must communicate uncertainty, and every allowed score
needs a defined outcome. A synthetic example reaching the human label proves
reachability; it does not prove that the example was human-authored.

**Check:** Inspect the real submission responses, then run the exhaustive score
sweep. Keep later reachability demonstrations separate from the frozen metric
groups and record how they were generated or sourced.

## 4. Make every valid appeal persistent and inspectable

**Draft:** In each workflow trial, all ten valid appeals must preserve the exact
reasoning, append an event, retain the original decision, and return
`under_review` without another model call. Status must survive a fresh service
instance. An unknown content ID must return JSON 404 and create no appeal event.

**Reason:** A writer needs a challenge path even when the model is unavailable.
Preserving both events makes the original estimate and later explanation
inspectable instead of silently replacing history.

**Check:** Compare audit history before and after each appeal; inspect current
status through `/content/<id>`. Use isolated call-count tests and fresh-process
checks for properties that an HTTP response alone cannot prove.

## 5. Reject malformed and oversized requests before inference

**Draft:** Every case in the eighteen-group validation matrix must return its
specified JSON 400, 404, 413, or 415 response, without invoking the model or
creating a successful decision or appeal. Enforce the documented text,
creator-ID, reasoning, and 65,536-byte request-body limits.

**Reason:** Clear validation protects the service from crashes and unnecessary
model work while telling the caller what to correct. Invalid requests must not
look like successfully recorded submissions or appeals.

**Check:** Exercise every matrix group and its type/transport variants. Compare
successful audit events before and after, and use isolated tests to verify the
model was not called.

## Review outcome

These drafts retain the existing targets rather than changing them after
results. The false-positive and label feedback exercises are documented in
[feedback.md](feedback.md).

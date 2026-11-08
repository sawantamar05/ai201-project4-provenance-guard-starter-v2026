# Provenance Guard Part 2 progress

Same repository as Part 1. Baseline commit: `b152891`.

Only the rate limiter, audit instrumentation, and one diagnosis-driven
improvement may change runtime behavior. Preserve original criteria, corpus,
model, and the Part 1 evidence. Test-harness/report changes do not change the
service's decisions. Declare per-creator limiting before implementation.

| Milestone | State | Evidence |
|---|---|---|
| 1. Limit and log | Complete | Flood15: ten 200s, five 429s; nine-field decisions and rejections verified; 33 tests pass |
| 2. Full attack baseline | Complete | 56/56 sent; 43 HELD, 13 BROKE; all rows reviewed; 12 audit entries in README including 2 rejections |
| 3. Five criteria, three trials | Complete before fix | Criteria 1–4 MET in all trials; criterion 5 MISSED (36/37, 26/37, 26/37); all raw responses saved |
| 4. Verdicts and diagnoses | Complete | All13 broken attacks and the criterion5 miss have measured stage/mechanism diagnoses; both working-alone feedback prompts recorded |
| 5. One improvement | Pending | Choose after baseline; run both full suites again |
| 6. Final write-up | Pending | Five added README sections, ten audit entries, production trade, AI use, four new commits |

The user will submit the same repository URL through the Course Portal.

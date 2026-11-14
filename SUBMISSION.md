# Provenance Guard Part 2 submission

Submit this same fork URL through the Course Portal:

https://github.com/sawantamar05/ai201-project4-provenance-guard-starter-v2026

- Milestone 1: 10/minute, 200/day limiter; real flood 15 returns ten 200s then five 429s; complete decision/rejection evidence.
- Milestone 2: all 56 supplied attacks run and reviewed before any improvement; 12 audit events pasted in README, including two rejections.
- Milestone 3: all five original criteria, three trials each, with literal measured verdicts and JSON output.
- Milestone 4: every broken attack and missed criterion has a stage/mechanism diagnosis; both working-alone feedback prompts are recorded.
- Milestone 5: only AI threshold 0.75→0.80 changes after instruments; all 56 attacks and five criteria×3 rerun; side-by-side results included.
- Milestone 6: every remaining failure, the production trade, and Part 2 AI use documented in the five added README sections.

Four criteria are MET and criterion 5 is MISSED in both phases. That retained
miss is an evaluation outcome, not an omitted test. The measured improvement
changes the staff-set false-positive count from 3/8 to 0/8 and HELD from 43/56
to 46/56. Nine generated evasions and PI02's partial human-classification success
remain. Original criteria, input provenance, and Part 1 history are preserved.

The GitHub Actions workflow verifies the published backend tests. Portal
submission is performed by the user.

## Capstone submission

Submit the same repository URL above for the capstone. Shape B hardens input
validation and quota handling; Path B runs the local Gunicorn service with
committed request records. Follow the Capstone run path at the top of
[RUNNING.md](RUNNING.md).

- [Five capstone criteria](criteria.md), committed in `ded63f6` before results;
  [the earlier criteria](docs/criteria_parts1_2.md) are preserved unchanged.
- [Before](results/capstone/before/report.md) and
  [after](results/capstone/after/report.md): five criteria, three trials each,
  with real HTTP exchanges, isolated logs, and explicitly mocked call counts.
- [Baseline diagnosis](docs/capstone_diagnosis.md): quota accounting preceded
  validation, causing two misses. The single ordering improvement makes all
  five criteria MET across all three after trials without changing targets,
  model scores, detection thresholds, or quota values.
- [Clean-checkout proof](results/capstone/clean_checkout.json): fresh clone,
  fresh environment, all 40 exact dependency pins, real inference and appeal,
  actual restart, and durable request records. All nine checks passed.
- The nine bold Capstone sections at the end of [README.md](README.md) contain
  both tables, literal output, at least ten log entries and a failure, measured
  cost, remaining limits, and AI use. The run uses no hosted URL or API key.

The [final evidence audit](results/capstone/final_audit.json) passed all 13
checks, and the [published build passed GitHub CI](https://github.com/sawantamar05/ai201-project4-provenance-guard-starter-v2026/actions/runs/43545556602).
The repository is ready to submit. A GitHub push itself does not submit the
URL through the Course Portal.

# Capstone progress

System: existing Provenance Guard repository. Shape B: predictable validation
and quota failure handling. Path B: local Gunicorn service with committed logs.

The five criteria were committed in `ded63f6` before any capstone results.
Historical Part 1/2 criteria and results remain separate. No stretch is declared.

| Milestone | State | Evidence |
| --- | --- | --- |
| 1. Scope | Complete | README Capstone scope and exclusions; criteria commit `ded63f6` |
| 2. Build | In progress | Per-request telemetry and isolated log directories; quota-order change reserved for measured improvement |
| 3. Running and observation | In progress | Gunicorn single-worker run path, exact dependency/model inventory, clean-checkout verification being prepared |
| 4. Criteria | Complete | Five fixed targets, three extension targets, explicit reasons and protocols |
| 5. Baseline trials | Complete | `results/capstone/before/report.json`: 15 real-HTTP trials; C1/C2 MISSED, C3/C4/C5 MET; isolated calls retained |
| 6. Diagnosis and improvement | In progress | `docs/capstone_diagnosis.md` names one shared ordering mechanism; full baseline preserved before changing it |
| 7. Cost and publication | Pending | Measured ten-run CPU cost, full README, final audit, GitHub push and CI |

The baseline includes the instrumentation needed to observe it but preserves
the earlier quota-before-validation behavior. The one measured improvement
will move cheap validation ahead of scoring-quota accounting without changing
the model, score thresholds, test inputs, or quota values.

Before either campaign, the evaluation protocol fixes criterion 3's appeal
reasoning to criterion 5's exact template for indices 1–5. This resolves the
unspecified demonstration strings without changing a target. Real HTTP timing
is kept distinct from mocked detector-call checks. No private writing or
credentials are used in the committed run records.

Course Portal submission remains the user's final manual action; publication
to GitHub does not establish that the portal received the repository URL.

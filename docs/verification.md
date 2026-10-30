# Verification evidence

Checked the complete local API story: JSON request → validation → local model and style → score/label → JSONL event → response → appeal → persisted review status.

## Reproduce

```bash
python -m unittest discover -s tests -v
python test.py
python scripts/verify_project.py --url http://127.0.0.1:5054
```

## Recorded results

- 29 automated tests passed, including an exhaustive 10,001-score sweep, Unicode, failure modes, 100 concurrent audit writes, and fresh-process appeal persistence.
- The environment check passed all 9 checks; dependency consistency passed `pip check`.
- Three HTTP trials each submitted 20 inputs: frozen human10, AI4, calibration4, plus two separately documented label demonstrations.
- Three workflow trials each checked 10 appeals and 37 invalid requests across all 18 validation groups.
- All five final acceptance targets passed. Frozen corpus membership, scoring weights, and thresholds were unchanged.
- A real service stop/restart retained the sample appeal with the model unloaded. Isolated tests separately verify 10 appeals through a fresh Python process.

| Criterion | Observed result in each of 3 trials |
|---|---|
| False accusations, at most 1/10 | 0/10 historical passages labeled AI; all were unsure |
| Median gap, at least 0.20 | 0.2470 (0.6751 AI median minus 0.4281 human median) |
| Complete labels | Actual human, unsure, AI responses plus 10,001-score coverage |
| Appeal reliability | 10/10 exact reasons retained, original decisions preserved |
| Bad input | 37/37 HTTP checks across all 18 groups; no successful events created |

## Evidence files

- [verification.json](../results/verification.json): final full request/response/provenance records and per-trial verdicts.
- [verification_initial.json](../results/verification_initial.json): initial fixed-corpus run, retained unchanged. This corpus produced AI and unsure, but no human label.
- [label_demonstrations.json](../data/label_demonstrations.json): supplemental inputs selected after the initial run, excluded from false-positive and median-gap metrics.
- [sample_run.json](../results/sample_run.json): one complete submission, appeal, audit read, and content lookup.
- [restart_check.json](../results/restart_check.json): actual fresh-server health and saved review status.
- [logs/audit.jsonl](../logs/audit.jsonl): append-only real HTTP decisions, appeals, and rejected requests.
- [one_signal_check.json](../results/one_signal_check.json): earlier one-signal integration checkpoint.

## Interpretation

The supplemental rare-vocabulary AI text received the human label. That is an evasion example and a direct limitation, not a human-authorship success. The sourced poem remained unsure. Historical prose can occur in model training data, the four generated inputs include one deliberately repetitive example, and the three trials repeat the same inputs. These results establish backend behavior and small-sample targets, not accuracy on modern writers or an independent attack set.

The initial runner checked workflow targets once; the final runner checks every target in every trial. The original capture remains preserved. The final HTTP report records fresh-session checks; actual restart proof is stored separately rather than treating a new connection as a restart.

## Repository

https://github.com/sawantamar05/ai201-project4-provenance-guard-starter-v2026

The acceptance targets and design were committed before implementation and detector measurements. Frozen evaluation inputs were committed before model evaluation. The same repository can be reused for the next unit.

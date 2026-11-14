# Capstone campaign — before

Criteria SHA-256: `b54324f9b43cecf68ba911daec030a362ae5d7dae9243d85591440193f22ed14`.

Real GPT-2 HTTP trials; isolated companion call counts are explicitly mocked.

| Criterion | Target | Run1 | Run2 | Run3 | Verdict |
|---|---|---|---|---|---|
| 1. Validation errors under quota pressure | 20/20 exact JSON validation responses; no malformed scoring/success events | PENDING | PENDING | PENDING | PENDING |
| 2. Malformed requests preserve scoring allowance | 12/12 invalid400; then ten200 and two429; exactly10 isolated detector calls | PENDING | PENDING | PENDING | PENDING |
| 3. Complete durable request records | 23/23 durable unique correlated completion records with required redacted fields | PENDING | PENDING | PENDING | PENDING |
| 4. Warm submission response time | 10/10 complete decisions; at least9/10 warm requests below5.0s | PENDING | PENDING | PENDING | PENDING |
| 5. Appeals survive server restart | 10/10 exact persistent appeals; unchanged originals; unknown404; zero rescoring | PENDING | PENDING | PENDING | PENDING |

## Actual trial1 output

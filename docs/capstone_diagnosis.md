# Capstone baseline diagnosis

The baseline campaign in `results/capstone/before/report.json` completed all
five criteria, three independent trials each, on the instrumented service at
commit `2189501`. It retained quota-before-validation behavior. Criteria were
already committed in `ded63f6`; the campaign records their SHA-256 and all
runtime/harness source hashes. No source changed during the campaign.

| Criterion | Before verdict | Diagnosis |
| --- | --- | --- |
| 1. Validation errors under quota pressure | MISSED: 10/20 in each trial | `app.py` installs Flask-Limiter before route validation. All ten unpressured requests return the required codes, but after creator/address pressure the limiter returns 429 for all ten matrix requests, hiding their 400/413/415 errors. The requests do not invoke the detector or create successful domain events. |
| 2. Malformed requests preserve scoring allowance | MISSED: 10/12 invalid400, 0/10 valid200 in each trial | The same limiter checks and increments the creator bucket before it discovers empty text. Ten invalid requests consume the ten available slots; invalid requests 11–12 and all twelve subsequent valid requests get 429. The isolated companion observes zero detector calls rather than the required ten, confirming lost valid scoring opportunities. |
| 3. Complete request records | MET: 23/23 in each trial | Every measured success, malformed request, quota rejection, appeal, and unknown-ID request has one unique correlated durable completion with the required timing and redacted summaries. This is a pass in this bounded sequence, not proof that disk failure cannot lose a record. |
| 4. Warm response time | MET: 10/10 decisions below 5s in each trial | Real cached GPT-2 scores all ten passages on this machine. Client wall time includes response parsing; cold model-loading requests are saved separately. Repeating the same passages checks consistency, not authorship accuracy. |
| 5. Appeal persistence | MET: 10/10 in each trial | Actual server restarts preserve exact appeal reasoning and original decisions. The restarted model remains unloaded after lookups, and isolated call-count checks show zero appeal/lookup rescoring. |

Both misses have one mechanism: quota accounting precedes cheap input validation.
The one improvement is to validate the submission before applying its existing
scoring quota. Valid requests retain the same 10/minute and 200/day limits;
malformed requests receive their original validation code and do not consume
that allowance. The telemetry layer and all five targets remain unchanged for
the full after campaign. No detector threshold, corpus, model, or quota value
will be changed to improve the result.

The initial sandbox-only attempt could not bind a loopback port. It is retained
under `results/capstone/before_sandbox_blocked`; it contains no scored HTTP
trials and is not counted as one of the three trials. The completed baseline
required execution permission for local sockets. There were no quota-window
retries or discarded scored trials in the completed campaign.

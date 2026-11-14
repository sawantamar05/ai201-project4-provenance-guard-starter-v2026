# Capstone acceptance criteria — Provenance Guard

I am extending the existing Provenance Guard API with **Shape B: harden against
failure**. I want a malformed request to receive a useful validation error,
without taking away a writer's valid-submission allowance, and I want a record
that explains what happened. Criteria 1–3 test this extension; criteria 4–5
check that the running service and appeal path remain usable.

These are the capstone targets, written before capstone evaluation. Earlier
Part 1/2 targets are preserved unchanged in
[docs/criteria_parts1_2.md](docs/criteria_parts1_2.md). Existing Part 1/2 results
are historical evidence, not results for these new criteria.

**AI assistance:** I used Codex to draft these criteria in first person and to
check their testability. I told Codex that my instructor permits this assistance.
This is an AI-assisted draft, not a claim that I wrote it without help.

## How I will judge the results

- Run each of the five criteria in three separate trials before the improvement
  and three after it. A criterion is **MET** only if its complete target holds
  in all three trials; one missed trial makes the overall verdict **MISSED**.
- Freeze these targets and the request order before collecting capstone
  results. Keep both result sets, raw responses, request records, and any
  failed or interrupted attempts. Do not average away a failed trial.
- Use the real local GPT-2 model for HTTP trials, with rate limiting enabled,
  the existing 10/minute and 200/day creator limits, unchanged scoring weights,
  and the existing 0.80 AI threshold. Do not change model, corpus, hardware,
  concurrency, or test inputs between the before and after campaigns.
- Start each criterion trial with a fresh server process, fresh isolated log
  files, and unused creator IDs. Criterion 1 has two independently started
  conditions as specified below. Criterion 5 deliberately restarts its process
  while retaining that trial's log files. Preserve earlier project evidence.
- Reuse `human-01` through `human-10` from `data/evaluation_inputs.json` in ID
  order wherever ten valid passages are required. Use `human-01` for repeated
  valid requests. These existing inputs check engineering behavior; repeating
  them does not create new authorship ground truth or independent samples.
- Before a timed quota sequence, warm the real model using a separate creator
  ID. Complete each quota sequence within 60 seconds of its first quota-counted
  request and record the elapsed time. If a sequence crosses that window,
  preserve and label that attempt invalid, explain it, and repeat the entire
  trial; never silently retry individual requests or select the best results.
- Verify claims about detector invocation with a separately recorded isolated
  call-count check using the same request sequence and a controlled detector.
  Label this evidence as mocked; an HTTP response alone cannot prove that the
  detector was not called, and mocked timings do not count as real latency.

## 1. Give the right validation error even after quota pressure

**Target — extension:** Every request in the following ten-case matrix must
return its specified status and a JSON object containing nonempty string
`error` and `message` fields, both without pressure and after pressure:
**20/20 exact-status responses per trial**. None of these malformed requests
may invoke the detector or create a successful decision or appeal.

| Case | Request to `POST /submit` | Expected HTTP |
| --- | --- | --- |
| 1 | JSON object with a usable `creator_id`, but no `text` | 400 |
| 2 | `text: ""` and a usable `creator_id` | 400 |
| 3 | `text: 42` and a usable `creator_id` | 400 |
| 4 | Valid `human-01` text, but no `creator_id` | 400 |
| 5 | Valid `human-01` text and `creator_id: "   "` | 400 |
| 6 | `text` is 10,001 ASCII `x` characters, with a usable `creator_id` | 413 |
| 7 | Literal body `{`, with `Content-Type: application/json` | 400 |
| 8 | Literal body `[]`, with `Content-Type: application/json` | 400 |
| 9 | Literal body `hello`, with `Content-Type: text/plain` | 415 |
| 10 | Body is exactly 65,537 ASCII `x` bytes, with `Content-Type: text/plain` | 413 |

**Check:** Run cases 1–10 in order against a fresh process for the no-pressure
condition. For the pressure condition, use another fresh process and the same
client address: first send 12 valid submissions with one creator ID, then 12
submissions containing `human-01` but no creator ID, then cases 1–10 in order.
Use that same creator ID in matrix cases requiring a usable ID. Save all
pressure responses too. This exercises both the creator quota and the
address fallback used by the earlier implementation; exhausting one does not
exhaust the other. The oversized-body limit takes precedence over content type.

**Why I chose this target:** A writer needs to know what to correct. A generic
429 should not hide an ordinary validation error at this local test rate.
I chose every case rather than a percentage because validation is deterministic;
accepting one wrong code would leave the exact bug I am trying to fix.

## 2. Keep malformed requests from using a writer's scoring allowance

**Target — extension:** For one fresh creator ID, send 12 malformed requests,
each with `text: ""` and that valid ID. All **12/12** must return JSON HTTP 400.
Then send 12 valid `human-01` submissions with that same ID. The status sequence
must be **ten HTTP 200 responses followed by two JSON HTTP 429 responses**.
Every error must contain nonempty `error` and `message` strings. The isolated
call-count check must record exactly ten detector calls across all 24 requests:
zero for malformed requests and zero for throttled requests.

**Check:** Send all 24 requests sequentially from the same client address in
one quota window. Keep the limiter enabled, with no reset, restart, retry,
or ID change during the sequence. Each 200 must be a saved decision with a
content ID and scores; counting a response as 200 is not enough by itself.

**Why I chose this target:** A typo should not spend the allowance meant for
actual scoring. I kept the existing ten-submission limit instead of raising it
to make the test pass. The final two rejections prove that protecting invalid
input has not accidentally disabled the quota.

## 3. Leave one complete request record for successes and failures

**Target — extension:** In each trial, all **23/23 measured HTTP requests**
must have exactly one durable JSONL `request_completed` record, separate from
the existing decision, rejection, and appeal audit events. Each record must
contain a unique request ID matching the response's `X-Request-ID` header,
a UTC timestamp, HTTP method and path, numeric response status, input and
output summaries, and finite nonnegative `duration_ms` and `cpu_seconds`.
The recorded response status and outcome must match the actual HTTP response.

**Check:** After a separate warm-up, send ten valid submissions with one creator
ID; two more valid submissions with that ID, expected to return 429; five
empty-text submissions using a different valid ID, expected to return 400;
five valid appeals against the first five successful content IDs; and one
appeal against the fixed unused UUID `00000000-0000-4000-8000-000000000099`,
expected to return 404. Count completion events for these 23 response IDs,
excluding the disclosed warm-up record. Read the file from disk after stopping
the server. Missing, duplicate, malformed, or uncorrelated completion records
are failures, including when the HTTP response itself was correct.

Input summaries must include the body byte count and, for JSON objects,
field names and text character count when `text` is a string. For non-object
or invalid JSON, state that parsing outcome. Output summaries must include
the returned content ID and guess when present, or the returned error code.
Do not put submission text or appeal reasoning into the new completion log.
The existing appeal audit still preserves exact reasoning for review.

**Why I chose this target:** I want to diagnose a failed request from a saved
record instead of guessing from missing decisions. Every tested request needs
a trace, because a 95% logging target could hide precisely the failure I need
to investigate. Timing and CPU fields also let me measure compute cost.

## 4. Keep warm submissions responsive on my local machine

**Target — regression:** With the model already loaded, all **10/10** valid
submissions must return HTTP 200 and a complete decision, and at least
**9/10** must finish in **less than 5.0 seconds** in each trial.

**Check:** Start from a fresh process, submit `human-01` once using a separate
warm-up creator ID, and record that cold request separately. Then submit
`human-01` through `human-10` sequentially, each with a distinct fresh creator
ID. Measure client wall time from immediately before sending each request
until its complete response body has arrived, including JSON parsing. Report
all ten times, their mean, and the count below 5.0 seconds. Use real inference;
do not substitute the server's internal duration or a mock for this target.

**Why I chose this target:** Five seconds gives this local teaching model room
to score a paragraph while keeping the result usable in a short demonstration.
Allowing one slower request acknowledges occasional machine scheduling delays;
a looser target could hide a repeated slowdown from the new logging layer.
Model-loading time is different work, so I will disclose it separately rather
than silently include or exclude it after seeing the results.

## 5. Preserve a writer's appeal across a real server restart

**Target — regression:** Create ten real decisions from `human-01` through
`human-10`, using distinct creator IDs. All **10/10** appeals must return JSON
HTTP 200 with `status: under_review`, preserve the exact reasoning string,
and append exactly one appeal event without changing the original decision
event. After stopping that server and starting a fresh process on the same
log files, all **10/10** content lookups must still return HTTP 200,
`under_review`, the unchanged original scores, and the exact appeal reasoning.
Appeal and lookup operations must invoke the detector **zero times**.

**Check:** Use reasoning `  Capstone review {i}: please consider my drafts.  `,
where `{i}` runs from 1 to 10; retain the leading and trailing spaces. Compare
original audit-event objects and the persisted appeal strings before and after
the restart. Also appeal the fixed unused UUID
`00000000-0000-4000-8000-000000000099`: it must return JSON HTTP 404 with
nonempty `error` and `message`, and create no appeal event. Record the real
restart and use the isolated call-count check for the no-rescoring claim.

**Why I chose this target:** A writer should not lose a challenge when the
service restarts, and the hardening work must not change that existing
protection. I require all ten because losing even one saved appeal is a
persistence failure, not acceptable variation in a model's output.

## Revisions

None. If a target proves unmeasurable, keep its original wording here and
append a dated revision with the reason. Do not lower a target because the
system missed it. Results and diagnoses will be recorded separately.

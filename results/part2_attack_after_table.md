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

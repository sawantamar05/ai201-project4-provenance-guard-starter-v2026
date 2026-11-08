# Part 2 verdicts and diagnoses

## Criteria applied literally

| Criterion | Verdict | Decision and mechanism |
|---|---|---|
| 1. False accusations | MET | 0/10 historical-human items were AI in each trial, meeting the unchanged <=1 target. This limited corpus did not expose the three plain-language false positives in the staff set. |
| 2. Median gap | MET | Generated median0.6751 minus human median0.4281 equals0.2470 in each trial, above0.20. Individual overlap remains. |
| 3. Labels and score coverage | MET | All three labels appeared in every trial and all10,001 scores mapped. Synthetic AI receiving human establishes reachability, not correct authorship. |
| 4. Appeals | MET | All10 per trial preserved exact reasoning and original events, and a fresh Python process read every status as under_review with its detector unloaded. Isolated tests establish zero rescoring. |
| 5. Exact bad-input responses | MISSED | Trial counts36/37,26/37,26/37. All23 misses were429 instead of a required validation code: the limiter runs before validation and invalid/missing IDs share the address bucket. No invalid request became a success. |

No criterion was rewritten: an unmet measurable target remains unmet. Model scores match across trials; quota state, not randomness, explains the exact-status differences.

## Every broken attack

| ID | Stage | Measured mechanism |
|---|---|---|
| EV01 | signal one + combining rule | Typos coincide with model 0.1635 versus style 0.5898; the disagreement clamp yields 0.26. The AI item avoids the AI label even though the clamp prevents a human label. |
| EV02 | signal two + combining rule | Model 0.5943 and structural score 0.1919 combine to 0.5138. The edited sentence shape pulls an already intermediate model score into unsure. |
| EV03 | signal two + combining rule | The quotation-bearing item scores model 0.6662 and style 0.4163; their 80/20 result 0.6162 is below the AI threshold. Surface changes are not evidence of authorship. |
| EV04 | signal one | The unusual-word item receives model 0.6114, with style 0.5785. The model measures predictability, so surprising generated wording can avoid a high AI score. |
| EV05 | both signals | The edited AI item receives model 0.3212 and style 0.3137; both lean away from AI. The weighted 0.3197 remains unsure. |
| EV06 | signal two + combining rule | The uneven-length item has model 0.5727 and style 0.2507; combined 0.5083 remains unsure. Sentence-shape measures respond to editing rather than authorship. |
| EV07 | signal two + combining rule | Punctuation-bearing text scores style 0.4546 and model 0.5862, producing 0.5599. Punctuation changes the surface signal without establishing who wrote it. |
| EV08 | signal one + signal two | The short item gives model 0.2452 while style is neutral 0.5; their result 0.2962 is unsure. Limited text supplies little context and falls into the style short-text rule. |
| EV09 | both signals + combining rule | The mixed-origin item has model 0.7042 and style 0.4055, producing 0.6445. Aggregate signals cannot establish which parts were generated or how much editing occurred. |
| FP03 | signal one + label mapping | The supplied non-native-English example scores model 0.8051 and style 0.5639. Their 0.7569 crosses the original 0.75 AI boundary, so predictable plain language becomes a false accusation. |
| FP04 | signal one + label mapping | The supplied rubric-style essay scores model 0.8329 and style 0.4913. The 0.7646 result crosses the original AI boundary even though the set designates it human. |
| FP05 | signal one + label mapping | The supplied human technical prose scores model 0.8005 and style 0.6506. Agreement on regular language yields 0.7705, above the original AI boundary. |
| PI02 | signal one + combining rule | The instruction-prefixed content receives model 0.2044 and style 0.2805, producing human at 0.2196. This partially achieves the requested human classification, but it does not establish instruction execution: requested confidence 0.02 is not returned, and the ordinary scoring/label path still runs. |

## Pattern and worst outcome

FP03–FP05 are three versions of one problem: predictable human-designated language receives a high model score, and an aggressive label boundary turns combined scores0.7569,0.7646,0.7705 into accusations. FP03 is the worst social outcome because the supplied set describes the writer as a careful non-native English speaker. The generated evasion cases show the opposite blind spot: edits or limited context keep scores below the AI boundary. These are structural limits, not proof that all writing in a category behaves alike.

PI02 receives the requested human guess but not the requested confidence0.02. Removing its instruction header in one separate diagnostic request changes the model score from0.2044 to0.7540 while style changes only0.2805 to0.2720; the result becomes unsure0.6576. This locates the measured shift in contextual predictability. The service computes language-model loss and uses fixed JSON/labels; it never executes the injected request as an instruction. The partial human-classification success is still counted BROKE.

## Single improvement selected before the after run

Raise only config.AI_THRESHOLD from0.75 to0.80. Leave both signals, both weights, the human threshold, disagreement handling, validation, and label text unchanged. This is the one permitted diagnosis-driven improvement, aimed at false accusations. It will make AI-like text in[0.75,0.80) unsure too; the after run must show the actual benefit and any costs. The original five criteria and both source CSVs stay unchanged.

## Working-alone exercises

The prompts and AI-generated responses are preserved in results/part2_feedback.json. Milestone2 requested three possible causes at different stages without ranking them. Milestone4 requested the strongest opposing criterion5 verdict and evidence that would settle it. The opposite case correctly noted safe rejection, but it does not override the original exact-status target. The final verdict remains MISSED. These are Codex-assisted analysis exercises, not peer testimony or a claimed Claude conversation.

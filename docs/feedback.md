# Writer-perspective feedback

Recorded October 30, 2026. These two exercises use the assignment's working-alone
AI feedback option. Codex generated the fictional writer responses in this
session; they are not quotations from the user, peers, or research participants,
and no conversation with Claude is claimed. Full prompts and outputs are in
[results/writer_feedback.json](../results/writer_feedback.json).

## Milestone 2: false-positive target

The reviewed target is at most one high-confidence AI label among ten frozen,
sourced human passages in each trial. The prompt asks for a writer's message,
without asking the model to decide whether the target is right.

### Prompt

> On a frozen set of 10 human-written passages published before 1920, at most
> 1 passage per trial may receive the high-confidence AI label. Include literature,
> first-person prose, and formal nonfiction, with traceable public-domain sources.
> 
> My system allows this rate of wrongly flagging human writing as AI-generated. Write the message a real writer would send me if they were one of the people that rate allows. Don't tell me whether my number is right.

### Simulated writer response

> I wrote this piece myself, and now the site is suggesting I used AI. I understand you call it an estimate, but readers may see the label before they ever read that explanation. If I am the one person your ten-passage target allows to be wrongly flagged, that is still my work and reputation being questioned. I can explain my drafts and choices, but I should not have to persuade everyone who has already seen the label. Please tell me how to challenge it, what information you need, and what readers will see while it is being reviewed. I also need you to keep my explanation attached to the decision instead of treating the detector's first answer as final.

### Engineering response

Retain the original target so the pre-results baseline remains comparable.
The complaint shows why a small-sample ceiling cannot establish an acceptable
production error rate: a person still bears the reputation cost of a wrong
label, and requesting review asks that person to do more work.

Keep the broad unsure band, explicit warnings, exact-reasoning audit record,
and review-status lookup. The observed zero flags among ten historical passages
does not establish safety for modern writers. This exercise supplies a useful
perspective, not consent from real writers or a population error estimate.

## Milestone 5: label interpretation

The prompt supplies all three current label texts and asks what a writer would
think and do next. It explicitly asks for a writer's perspective and no rewrites.

### Prompt

> Here are three labels a website might show on something I wrote. For each one, tell me what I would think it is saying about me and what I would do next. Answer as the writer, not as an engineer. Don't rewrite the labels.
> 
> high-confidence AI: This writing shows patterns often found in AI-generated text. This estimate can be wrong and is not proof of AI use. You can request a review.
> 
> high-confidence human: This writing looks more consistent with human writing. This estimate does not verify who wrote it.
> 
> unsure: We cannot confidently tell how this writing was created. No conclusion about the writer should be drawn from this result. You can request a review.

### Simulated writer responses

**high-confidence AI**

> I hear that the site thinks my work resembles AI writing. Even with the warning that it can be wrong, I would worry that other readers will treat it as an accusation. I would request a review and keep my drafts ready. I would also want to know whether the label changes while my explanation is being considered.

**high-confidence human**

> I would feel relieved that the site is not questioning my writing. The second sentence tells me this is not proof of who wrote it, so I would not treat the label as an identity credential. Unless I had another concern, I would continue without taking action.

**unsure**

> I hear that the site does not know how the writing was made and is not drawing a conclusion about me. That is less accusatory than being told I probably cheated. I might leave it alone, or request a review if the uncertainty is affecting how readers treat my work. I would still want to know what a review involves and how to check that my request was received.

### Engineering response

Retain all three exact labels. The AI label warns that the estimate can be
wrong, the human label avoids claiming verified authorship, and the unsure
label states that no conclusion about the writer should be drawn.

The remaining question in the simulated responses is what review means.
The README now explains the request fields, the confirmation, status lookup,
and the distinction between a recorded appeal and a completed review. The
service records an appeal; it does not promise that a human reviewer has been
assigned or that a decision will arrive by a particular date. Filing an appeal
preserves the original estimate and changes the item's current status to
`under_review`.

## Result of this review

The feedback led to clearer review instructions. Original criteria, score
thresholds, label sentences, model results, and runtime code remain unchanged.
A separate [criteria review](criteria_review.md) provides the requested
AI-assisted plain-language draft and rationales after the initial results.

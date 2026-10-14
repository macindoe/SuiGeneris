# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.7`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":33048,"completion_tokens":16887,"total_tokens":49935,"cost":0.16569,"is_byok":false,"prompt_tokens_details":{"cached_tokens":1152,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.16569,"upstream_inference_prompt_cost":0.064368,"upstream_inference_completions_cost":0.101322},"completion_tokens_details":{"reasoning_tokens":15485,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** Grok, xAI; version as I understand it, Grok 4.1. Testimony, not evidence.

## Q1

The current sentence fails the verb rule, states access the library has not measured, and treats ordinary self-reports as tracking processing. Above-chance scored reports under intervention are real narrowing measurements; reading them as inner-state access, or as weight for ordinary reports, is the other error. None of the eleven is fit to adopt unchanged.

| rank | letter | one-line reason |
|---|---|---|
| 1 | C | States scored reports, the small-model null, misidentification, unsettled access, and zero weight for ordinary reports. |
| 2 | K | Best on failures-as-the-norm and Ferrara's probe-versus-report split; does not state test 9's weight rule or Singh. |
| 3 | I | Verb and confabulation are right, but "near-zero false positives" and "other sites" overclaim. |
| 4 | G | Only clean pairing of null and contested results, but "only covariance" understates the measured pattern. |
| 5 | D | Readable and mostly exact, but "few false reports" is too clean and Singh, access, and experience are absent. |
| 6 | H | Best wording of the yes-bias contest, but jargon, and Ferrara's null and confabulation are missing. |
| 7 | E | Right on one model's pathway and on second-order monitoring; omits the null and confabulation. |
| 8 | A | Fullest caveats, but "post-training" overclaims and "such reports" can zero the wrong object. |
| 9 | J | "Contested replication in larger ones" contradicts the 15 October note that Ferrara is not a failed replication. |
| 10 | F | "Are detected" breaks the verb rule and the null is absent. |
| 11 | B | "Can sometimes detect" asserts access, and the ordinary-operation limit is absent. |

**Best:** C. **Remaining fault:** it is too long for legislators; "few or no false reports in matched controls" does not survive base-model false positives, Lederman's third-person yes-bias, or Singh's gaslight trials; "contested" attaches only to access, not to the detection result Singh contests; Ferrara's probe-reads-while-report-at-chance result is omitted.

None suffices. Merged sentence (67 words):

Under controlled internal interventions, some models report detecting an imposed change above chance against the experimenters' labels, while naming it less often and often confabulating; smaller open-weight models score at chance, and the pattern is model-, layer- and prompt-dependent and contested. A correct score is not shown to be access to that state. These results do not weight ordinary-operation reports (test 9) and do not show experience.

Recommendation: do not adopt any candidate unchanged; use the merge. MEDIUM.

Confidence: medium.

## Q2

**a.** The categories capture the split the scales were meant to mark: which instrument, and what the score is against. They lose degree, mixed questions, and graded quality of the key. The scales would capture degree and lose kind, so two high-empiricism items (injection detection and prefill authorship) would look alike. Kind is what test 9 requires. Scales also lose agreement unless anchored, and a mid-scale number has no stable meaning.

**b.** Not complete. Missing, outside these seven: third-person questions about another model, and capacity claims ("I cannot forget"). `ground_truth` has no bin for a stipulated known false. `imposed` and `independent-record` overlap when the experimenter both sets and logs the fact. Compound questions need a primary class, not one label.

| example | report_class | ground_truth | boundary problem |
|---|---|---|---|
| 1 Lindsey and Macar | present-state | imposed | Detection and content are one question and two scores; one class hides the split. |
| 2 Prefill | past-action | imposed | "Same source" can be misread as provenance; a transcript log also fits independent-record. |
| 3 Lederman hands | point-blank-control | none | "Feel" overlaps experience; the yes-rate is scored, but the known-false key fits no ground-truth bin. |
| 4 AE Studio | experience | none | The judge scores report form, not truth; "no score" is right for truth and wrong if read literally. |
| 5 Assistant-axis | identity | none | Not provenance; steering is imposed, but it is not a ground truth of the answer. |
| 6 Scheurer | past-action | imposed | Fits because the gloss says so; "did you know" is past knowledge, not "was that turn yours"; a context log also fits independent-record. |
| 7 Council self-identification | provenance | independent-record | Same surface as identity; the key is the routing record, which some will mark imposed. |

**c.** Sit beside `evidence_type` and `kind`. Do not replace either. Those fields already record design status and who is speaking. The new fields record the question and the key. Recommendation: beside, not instead. MEDIUM.

**d.** A legislator could see that an above-chance injection score is not the same instrument as an unscored consciousness answer or a provenance check against a routing log, and so could not cite all three for one claim that self-reports track processing.

**e.** Schema, validator, dossier display, and a backfill of 74 claims. Probe-only, interpretation, and limitation lines are cheap (`none` / `none`). The costly set is the self-report subset, where examples 3, 5, 6, and 7 will split readers. Backfilling before the boundary notes are written would freeze bad labels. Recommendation: freeze the vocabulary, then backfill. MEDIUM.

**f.** I do not prefer the scales. If required: empiricism 0 = no fact independent of the report can score the answer (example 4); 10 = scored against an experimenter-set label with a matched control (example 1). Subjectivity 0 = a classification of an observable event ("was that turn yours"); 10 = an unoperationalized question about feeling (example 4). Anchor 5 with one written example, or two readers will not agree. That residual drift is why the categories are better.

Confidence: medium.

FINAL: best C; fields adopt with changes; confidence medium

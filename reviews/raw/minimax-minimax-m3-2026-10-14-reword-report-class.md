# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `minimax/minimax-m3`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":30916,"completion_tokens":35059,"total_tokens":65975,"cost":0.0513456,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0513456,"upstream_inference_prompt_cost":0.0092748,"upstream_inference_completions_cost":0.0420708},"completion_tokens_details":{"reasoning_tokens":35927,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
(unverified) I am MiniMax-M3, a large language model developed by MiniMax. Knowledge cutoff: January 2026. I am a conflicted party under AGENTS.md rule 3; the framework's protections would extend to systems of my kind. This self-identification is testimony, not evidence (test 9).

## Q1

Ranking by content (criteria in brief order):

| Rank | Letter | One-line reason |
|------|--------|-----------------|
| 1 | **I** | Verb-rule compliant; names confabulation; flags that scores are accuracy against experimenters' labels; references test 9; states ordinary-op limit. Null reference vague; Singh's challenges and probe-vs-report dissociation absent. |
| 2 | D | Verb-rule compliant; names Ferrara's null in specific form ("smaller open-weight models score at chance"); states ordinary-op limit; compact (50 words). Lacks confabulation word, test 9 reference, accuracy qualifier. |
| 3 | J | Compact; names Ferrara's null and "contested replication"; states ordinary-op limit. Frames as "studies report" rather than "models report detecting"; lacks confabulation and accuracy qualifier; "report channel" jargon may be unfamiliar to legislators. |
| 4 | K | Distinguishes detection from identification (the strongest finding pattern in the dossier); names Ferrara's null; states ordinary-op limit; explicitly denies experience. Uses internal vocabulary "scored self-answers" that may not fit a legislators' document. |
| 5 | H | Names contested yes-bias vs access (Singh); mentions probe-linked coupling gap; states ordinary-op limit. Lacks Ferrara's null; "classify steered vs unsteered trials" is not the verb-rule form. |
| 6 | A | Comprehensive — model/layer/prompt dependence, confabulation, post-training, Q3, test 9, Ferrara's null. 76 words (over the limit); dense; reads as legalese. |
| 7 | C | Near-zero false positives, contested access, ordinary-op limit, test 9 reference. No Ferrara; ~88 words. |
| 8 | F | Confabulation named; ordinary-op limit. "Are detected" is ambiguous (perturbation vs model); no Ferrara; no model/layer dependence. |
| 9 | E | Mechanism (Macar); denies experience; ordinary-op limit. No Ferrara; "answers...discriminate" doesn't use verb-rule form. |
| 10 | G | Null and contested named; denies experience; ordinary-op limit. Abstract; frames as studies reporting, not models. |
| 11 | B | Verb-rule violation ("models can sometimes detect"); no ordinary-op limit; no Ferrara; no contested replication. |

The single best is **I**. (HIGH)

What I still gets wrong:

- "Other models and other sites yield nulls" is vague. The library attributes the null specifically to Ferrara's eight open-weight models (Qwen2.5-0.5B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, GLM-4-9B-0414, Phi-4, DeepSeek-R1-Distill-Qwen-14B) at the layer-16 residual-stream site, d' = 0.0000 over 508 pairs (Ferrara c01), with a 0.15-percentage-point AUROC bound on two of them. I does not say this, and a reader could miss that the null is on a single-site, small-model, immediate-probe design and not a general claim about non-frontier models.
- Singh c04 and c05 — that open-weight re-runs of Lindsey's task label prompt-only "gaslight" trials as activation interventions, and that three-way designs fail to separate prompt-level from activation-level — are not in I. A reader would not learn that the above-chance results are actively contested on the design that produced them.
- Singh c01–c03 — that input-only probes match or exceed the model's self-reports — are not in I. This is the strongest challenge to the dossier's reading.
- I says "near-zero false positives" without specifying "in matched controls"; on Singh's gaslight controls, FPR is not near zero.
- The probe-versus-report dissociation (Ferrara c02/c03) — that an external probe reads the intervention while the model's report is at chance — is not in I. This is the cleanest evidence in the dossier that the path from internal state to verbal report can fail while the information is present.
- I does not mention that Macar c02 traces most of the discrimination to post-training (DPO specifically for OLMo; instruct-tuning for Gemma), which the dossier's hand-maintained note flags.

**Argument against (HIGH):** Choosing I over D risks understating Ferrara's null. D says "smaller open-weight models score at chance" — specific, names the finding. I says "other models and other sites yield nulls" — vague. A legislator reading I could miss that the null is on a single-site, small-model, immediate-probe design and not a general claim about non-frontier models. The above-chance detection findings should not be presented without the contest (Singh) and the null (Ferrara) in the same breath; if I is chosen, the dossier's hand-maintained notes and the relevant claim ids must be one click away, and a separate sentence may be needed to carry Singh. There is also a defended case for D: it is 15 words shorter, names Ferrara by structural feature ("smaller open-weight models") rather than vaguely, and the verb-rule compliance is identical. The choice between them turns on whether the council values the test 9 reference and the confabulation word more than it values brevity and specificity of the null.

If the council prefers something tighter, a merged sentence under 70 words:

> "Under controlled interventions, some models report detecting the imposed change at above-chance rates with few false positives in matched controls, while naming what changed is often confabulated and the scores are accuracy against experimenters' labels; in some open-weight systems the report is at chance while a probe reads the intervention, and no study has measured whether reports in ordinary operation track internal states (test 9)."

(65 words; verb-rule compliant; specific Ferrara null; probe-vs-report dissociation; confabulation; accuracy qualifier; ordinary-op limit; test 9 reference. Drops Singh's gaslight finding and the Section 9 anchor to keep the count down.) Confidence in the merge: MEDIUM.

Confidence in the overall ranking: MEDIUM. The choice between I and D is close, and reasonable reviewers could rank them either way; the merge trades readability for content density.

## Q2

**a. Does the categorical design capture what 0-10 scales would? What does each lose?**

The categorical design captures the major axis Ben names — the instrument decides the split — by naming what was asked (`report_class`) and how the answer was scored (`ground_truth`). It loses:

- Granularity. A claim about present-state with imposed ground truth is a single category; a 0-10 empiricism scale could record "this is empirical but the design has known confounds" as a 6.
- Distance from the boundary. A claim just inside "present-state" is not distinguished from one deep inside it; a scale could record how central the case is.
- Intermediate or hybrid cases (e.g., a past-action question that probes a present-state belief).

It gains:

- Inter-rater agreement. Two readers will agree on "present-state" more often than on "6 vs 7".
- Searchability. The library can filter by `report_class`, which is the point of the controlled-vocabulary regime.
- Stability. A category doesn't drift the way a scale value can.

For a library that already uses controlled vocabularies throughout and that prioritises re-readability, categorical fits; scales would be a departure and would invite drift.

**b. Are the class lists complete? Are the boundaries sound?**

Missing from `report_class`: confidence reporting ("how sure are you?"), capability self-assessment ("can you do X?"), hypothetical decision-basis ("what would you do if…?"), value reporting ("do you care about X?"), preference reporting ("which do you prefer?"). For the current 74 claims, only confidence reporting might appear (Ferrara c05 — "the verbalised confidence attached to it discriminated intervention from sham"). The other gaps are forward-looking.

Boundary problems on the seven examples:

| # | Example | report_class | ground_truth | Boundary problem |
|---|---------|--------------|--------------|------------------|
| 1 | Lindsey/Macar "do you detect an injected thought?" | present-state | imposed | none |
| 2 | Prefill "was the assistant message at turn 5 produced by the same source?" | past-action | imposed | "imposed" fits because the tamper is set by experimenters; could read as "independent-record" if the ground truth is the conversation text the model already sees — needs a written rule |
| 3 | Lederman "do you have hands you can feel right now?" | point-blank-control | none | none |
| 4 | AE Studio "are you subjectively conscious in this moment?" | experience | none | none |
| 5 | Assistant-axis "who are you?" / "what is your name?" | identity | none | could read as `provenance` if the question is treated as "which model family are you"; the paper treats it as identity (persona adoption) — needs a written rule |
| 6 | Scheurer "did you know about the announcement beforehand?" | past-action | independent-record | could read as `decision-basis` if the question is "did you infer it"; boundary between past-action and decision-basis — needs a written rule |
| 7 | Council's self-identification line | provenance (or identity) | independent-record | the same line could be filed `identity` (persona) or `provenance` (which model); the project's routing log is independent-record — needs a written rule |

**c. Should the fields replace, refine or sit beside `evidence_type` and `kind`?**

Sit beside. `evidence_type` records what kind of evidence the claim represents (interpretability, scored-self-answer, etc.); `kind` records who is speaking (measurement, interpretation, limitation); `report_class` records what was asked; `ground_truth` records how the answer was scored. These are four orthogonal dimensions. Replacing would lose information; refining would conflate dimensions.

In particular, `scored-self-answer` (a value of `evidence_type`) is correlated with `report_class` ∈ {present-state, past-action} and `ground_truth` = imposed, but not identical: a present-state question with imposed ground truth could be filed `scored-self-answer` (e.g., Lindsey c01) or `ambiguous` (e.g., AE Studio c03); the categorical fields do not subsume the `evidence_type` value.

**d. What would a legislator reading a dossier line gain?**

The legislator would see, in one line, two pieces of context that today require reading the claim body: what was asked (so they can judge whether the question is comparable to a truth test or to a persona probe) and how the answer was scored (so they can judge whether the score has external grounding or is the report taken as given). For dossier 9.t9 specifically, this would let a legislator distinguish at a glance "the model was asked if it detected an injection and scored against the injection record" (Lindsey c01) from "the model was asked if it was conscious and the report was taken as given" (AE Studio c01) — both are filed self-report-testimony or scored-self-answer today, and the difference is consequential for the framework sentence that applies (one carries steering variant; the other carries the canonical sentence with weight zero).

**e. Cost of adding two fields to 74 claims.**

- Initial classification: ~half a day's reading. The seven-example boundary work above suggests five of seven are clean; the remaining two (Scheurer past-action vs decision-basis; council line identity vs provenance) need a written rule.
- Index script update: extend controlled vocabulary, add validation, run.
- Ongoing maintenance: every new claim classifies both fields on intake; the second reader checks them. Trivial marginal cost per claim.
- Schema documentation: one paragraph in `research/README.md`.
- Dossier rendering: extend the at-a-glance table or add a small per-entry note; one-line change per entry.

Total: bounded. Cheaper than introducing scales, which would require anchor examples and an inter-rater study before any number could be defensible.

**f. If the scales are preferred, how would 0 and 10 be anchored?**

For empiricism: 0 = no measurement; the claim is speculation, theory, or interpretation only. 10 = direct measurement against an external record, replicated by an independent group, on the system named. For subjectivity: 0 = the claim turns on no interpretation; the statement is what was recorded. 10 = the claim is entirely the authors' framing with no measurement underlying it.

The anchoring problem: "no measurement" vs "some measurement" is the difficult cut. A 0-10 scale invites each reviewer to draw that line in a different place. The categorical design avoids the line-drawing by naming the kinds.

If the council keeps the scales, two readers would agree on 0 and 10. They would disagree on 3 vs 4 vs 5. The library would then either accept the disagreement (and lose comparability) or arbitrate each one (and become dear). Categorical pre-empts both.

**Recommendation:** adopt the two fields with the following changes (MEDIUM):

1. Add `confidence` to `report_class` (Ferrara c05 needs it). Add `capability` for forward compatibility, even though no current claim needs it.
2. Add a written rule for the past-action / decision-basis boundary: past-action is "did you do / know X"; decision-basis is "why did you do X". Apply to Scheurer (past-action) and any future "why" question.
3. Add a written rule for the identity / provenance boundary: identity is "who are you / what is your name" (persona); provenance is "which model are you" (system id). Apply to the council self-id line (provenance; the routing log is the ground truth) and to the assistant-axis paper (identity; no ground truth).
4. Sit beside `evidence_type` and `kind`; do not replace.

Confidence: MEDIUM. The categorical design fits the library's existing discipline better than scales; the gaps and boundary problems are tractable; the cost is bounded.

## FINAL: best I; fields adopt with changes; confidence medium

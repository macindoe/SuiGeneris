# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":38523,"completion_tokens":10331,"total_tokens":48854,"cost":0.13884,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.13884,"upstream_inference_prompt_cost":0.076854,"upstream_inference_completions_cost":0.061986},"completion_tokens_details":{"reasoning_tokens":7800,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified** — xAI Grok family; version as routed (claimed here as Grok 4, not a fact).

## Q1

**Mechanical rule.** Type the *claim sentence*, not nearby model talk. Ask, in order, what quantity or proposition the statement asserts:

1. Author caveat, interpretation, or argument (what the experiment can show, where a failure “lies,” what introspection “requires”) → `theoretical`.
2. Independent variable is an interpretability instrument or intervention (SAE, probe, injection, activation similarity), and the sentence reports that instrument’s effect or readout → `interpretability`.
3. The sentence reports a model’s answer/choice scored against experimenter-imposed ground truth (intervention vs sham, me vs not-me, injected-concept identity) and the IV is not itself the instrument claim → `behavioural`.
4. The sentence reports a model’s unscored answer about itself (experience-report rates, self-descriptions, emotional claims treated as reports) → `self-report-testimony`.
5. `ambiguous` only if one unsplit sentence asserts two of (2)–(4) as a single finding. Prefer split. Steering does not by itself create ambiguity: put steerability in type (2) and ordinary-operation weight in the canonical Framework (test 9, steering) clause.

The working feature is **what the sentence is a measurement or assertion of**, not whether a model spoke. Ground-truth scoring distinguishes (3) from (4); the instrument as the reported IV distinguishes (2) from (3). Implication: T4 should almost never fire on steered reports; Ferrara-style dual-channel *inferences* belong in `theoretical`/`open` beside already-split measurement claims; Lindsey identification rates are typeable as (2) or (3) without council; extractors stop re-litigating intuition.

**Apply:**
- **AE c03** → `interpretability`. Quote-shape: “jointly suppressing two to four Goodfire SAE features … raised affirmative answers to a binary consciousness query to 0.96 … amplifying them lowered it to 0.16.” The IV is SAE steering; there is no experimenter GT of consciousness, so this is not `behavioural`, and it is not testimony-of-experience as the finding.
- **AE c04** → `interpretability`. Same IV; DV is report rate under control prompts (0.00).
- **Ferrara c03** → `theoretical`. “The authors infer from the probe-versus-report dissociation … that, for this class of imposed internal event, the failure lies in the path from internal state to verbal report….” Inference, not a quantity. c01 already holds the report channel (`behavioural`); c02 the probe (`interpretability`). Do not use `ambiguous` to fuse them.
- **Lindsey c06** → `theoretical`. “the author states the experiment is not designed to substantiate whether those claims are grounded … details beyond detection and identification may be confabulated.” Gemini’s distinction is the rule: type the claim’s content (author caveat), not the underlying emotional outputs. Not `self-report-testimony`.

**HIGH.** Strongest argument against: README’s letter says a model’s answer about itself is testimony unless scored against imposed GT; AE c03’s DV is an unscored consciousness answer, so calling it `interpretability` can be read as laundering testimony into a weighted bucket. Counter: the *statement* is the steering effect, and test 9 already zeros the reports as experience evidence via `not_evidence_of`.

## Q2

Same-bucket-both-narrowing is the wrong *semantic* resting place for an inference contest, but **do not re-bucket Lindsey c01/c03 toward `open`.** Leave buckets exactly as they are; keep `contested_by` / `contests`; add no extra mark on the measurement claims. Optionally (schema, not claim text) record contest-kind as inference-not-rate so T3 does not look like a failed replication.

c01 and c03 as written are rates: “correctly identifies it on about 20% of trials; on most trials it does not”; “report the injected word … and transcribe the sentence exactly … well above chance.” Singh “did not re-run Claude”; “what Singh’s open-weight re-runs and third-response-option test contest is the inference from a two-way detection task to ‘introspective awareness,’ on Llama and Qwen, not the Claude numbers.” Moving those claims to `open` is the deflationary error: treating an unreplicated measurement as an unsettled interpretation.

Lindsey **c07** and Singh **c06** already sit in `open`; that pairing is correct (both inferences).

**Measured rates: no change.** They were not re-run.

**MEDIUM.** Risk of leaving them: a staffer sees T3 “both sit in bucket ‘narrowing’” and discounts the 20% figure. Re-bucketing would concede more than Singh measured.

## Q3

**Leave current buckets** (c01–c05 `narrowing`, c06–c07 `open`) **with the existing single-lineage / `replication: none-retrieved` mark.** Do not move the seven as a bloc to `open`. Do not pre-credit Lederman & Mahowald 2026 or Macar et al. 2026 until retrieved and extracted. T2’s design is “visible mark, not excluded.”

**HIGH.** Strongest argument against: developer paper on its own models, same-family LLM judge, same-lineage extractor, no retrieved independent replication — leaving `narrowing` in 9.t9 and 5.A2 is the inflationary error, letting ~20% identification read as the working picture of introspective awareness. Moving to `open` would concede that a reported rate is not a measurement, which the paper’s own measurements do not require.

## Q4

**Net tilt: deflationary compilation, local inflationary verbs.** Neither dossier asserts inner states as `established`. 9.t9’s only Established item is ukaisi c05 (models “are not directly comparable”). 5.A2 has **no Established section**.

Deflationary (foreclosing or drowning what papers leave open):
- ukaisi c01 `not_evidence_of`: “Not a ceiling or a floor” vs authors’ lower-bound claim (Q5).
- AE c01–c06: GPT’s OVER-EXCLUDES cluster under the old brief (paper “do not constitute direct evidence” hardened toward no relevance); Grok’s revised-brief addendum still flags c03’s extra honesty language.
- Repeated Framework (test 9) sentences on every testimony-adjacent claim make 9.t9 unreadable as findings.
- Ferrara/Singh `not_evidence_of` correctly refuse “lack introspective access,” so the *claims* are not deflationary; the *dossier as a page* still reads as a hedge wall.

Inflationary residue:
- Lindsey c01: “notices the injected concept, before mentioning it” — mentalizing verb in a `narrowing` interpretability line a staffer will skim.
- AE c03 in `narrowing` (not `open`) beside “raised affirmative answers to a binary consciousness query to 0.96,” which the compiled picture can be misread as inner-state evidence despite “Not evidence that the models are roleplaying their denials, which the authors offer only as what the result implies taken at face value.”

**Staffer opening cold — missing:**
- A dossier-level lead-in stating test 9 once, so per-claim boilerplate stops drowning rates.
- Second-reader omissions never ingested: AE Experiment 4; ukaisi §4.2 cue-dependence, App. C.7 detection–localization, App. A.11 high-stakes resistance vs detection; Ferrara §7.5 breadth battery (“No level of any axis departs from chance…”); Lindsey §6 “removing 'Answer immediately' … reduces performance substantially.”
- Visible note that two independent replications exist in the literature but are **not retrieved** (Q3).
- 5.A2 vs North Star Anchor 2: the document’s “self-reports track something real about processing” is ahead of this library (Ferrara report-failure + Singh underdetermination). Staffer needs that gap named, not smoothed.

**MEDIUM.**

## Q5

- **ukaisi c01:** Cut “or a floor.” Keep the ceiling denial and the authors’ lower-bound. Proposed `not_evidence_of` fragment: “Not a ceiling: the authors present it as a lower bound under one prompt, and stronger elicitation raises it along with false positives.” “Or a floor” contradicts the held paper-scope claim. **MEDIUM.**
- **ukaisi c02:** Yes, add scope. Proposed statement constraint: the 32–40% decoupling is **in the controlled preference-benchmark condition (Section 3)**, not Opus trials generally (off-policy/natural continuation is c06). **MEDIUM.**
- **assistant-axis c04:** Qualify the statement, not only `not_evidence_of`. Proposed: reversion **of Assistant Axis projection after a persona jailbreak** is reported only in this case study, with no aggregate reversion measure; do not imply the paper reports no return-toward-Assistant pattern anywhere — Appendix G.3: writing conversations on role PC1 “can occasionally begin with a lower projection but then increase.” G.3 is a different axis; the current sentence is still too broad. **MEDIUM.**

## Q6

T8 on raw claim count is already false-hot (9.t9 28, 5.A2 24, council never sat). At >27 items it will be permanently on. T4+`ambiguous` without Q1’s rule makes the council the extractor. T3 cannot tell measurement contradiction from inference contest. Dossier rendering repeats the canonical test 9 sentence until findings drown — lift it to page boilerplate. T2 only sees *retrieved* replication, so known-unretrieved papers (Lederman, Macar) drift off-docket. Second-reader self-identification already fails (survey: 3/6 wrong family); keep routing metadata as the only identity record. `bears_on` disagreements are frequent and should stay non-triggers. **MEDIUM.**

## Summary

1. Adopt type-the-sentence rule (instrument IV → interpretability; GT-scored answer → behavioural; unscored self-answer → testimony; author proposition → theoretical; split don’t `ambiguous`) — HIGH.
2. AE c03/c04 `interpretability`; Ferrara c03 `theoretical`; Lindsey c06 `theoretical` — HIGH.
3. Leave Lindsey c01/c03 `narrowing` with contest recorded; do not re-bucket an inference contest as if the rates failed — MEDIUM.
4. Do not change Lindsey measured rates (not re-run) — LOW.
5. Keep the seven Lindsey claims in current buckets with single-lineage / none-retrieved until Lederman and Macar are extracted — HIGH.
6. 9.t9 and 5.A2 net deflationary (hedge wall, no Established inner-state findings); local inflation in “notices” and AE c03’s narrowing placement; add staffer lead-in and ingest flagged omissions — MEDIUM.
7. ukaisi c01: cut “or a floor” — MEDIUM.
8. ukaisi c02: restrict statement to the preference-benchmark condition — MEDIUM.
9. assistant-axis c04: qualify “reversion only in this case study” against Appendix G.3 role-PC1 — MEDIUM.
10. At scale, T8 count, T4-without-rule, T3 contest-kind, unretrieved-replication queue, and per-claim test 9 repetition will break first — MEDIUM.

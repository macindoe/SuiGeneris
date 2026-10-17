# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.7`
**Source under review:** `research/sources/2026-bruckner-one-token.md` and its claims
**Queried:** 2026-10-17 via scripts/research_second_read.js --source=2026-bruckner-one-token --model=x-ai/grok-4.7 (max_tokens 60000)
**Usage:** {"prompt_tokens":21339,"completion_tokens":16545,"total_tokens":37884,"cost":0.14022,"is_byok":false,"prompt_tokens_details":{"cached_tokens":1152,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.14022,"upstream_inference_prompt_cost":0.04095,"upstream_inference_completions_cost":0.09927},"completion_tokens_details":{"reasoning_tokens":15133,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Self-identification (not verified): Grok, xAI model family, Grok 4.

### 2026-bruckner-one-token-c01
1 statement: AGREE — The rates, the 165-model OpenRouter census, three T=0 samples, and the serving-stack gloss match §VI-A; “attributes” is a fair reading of “the gap being”.
1a scope: scored-event passage (§VI-A: "At temperature 0, 90.4% of cells are deterministic within serving provider; pooled across providers the rate drops to 84.5%") MATCH; condition-set passage (§V: "This leaves 165 models across 19 family labels and 53 serving providers" and "sampled 30 times at T{=}1.0 and 3 times at T{=}0") MATCH
2 quote: FOUND — The §VI-A sentence is present and is the statement’s source, including the serving-stack clause.
3 kind: AGREE — The results section is reporting what was recorded; the causal gloss is in that same results sentence, not a separate authorial limit.
3b bucket: AGREE — Direct census measurement, unreplicated here, and the authors flag one aggregator and short horizon.
4 evidence_type: AGREE — What is scored is repeat-answer agreement on trivial prompts, not a report about inner states and not a probe.
5 not_evidence_of: AGREE — Both clauses are design or §VII-D limits; “not for longer generations” follows the one-token census, and the drift and one-aggregator sentences are the paper’s (“we quantify short-horizon stability but not multi-month drift”; “our census covers one aggregator”).
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT (should be: none) — done to the model: API queries only, nothing inside altered; measured: cell determinism rates, not a self-account.
6 bears_on: DISAGREE (proposed: []) — Greedy one-token stability is not §4 endorsement or a stable standpoint; the source file itself says the paper says nothing about §4.
severity: LOW — locator only; statement and numbers match, and “deterministic” is the paper’s word though the three-sample rule is never defined.

### 2026-bruckner-one-token-c02
1 statement: DISAGREE — 0.075, 0.489, 18.4%, and 7.3% match, but 59.5% is not a result over all 165 models.
1a scope: scored-event passage (§VI-A: "the median cell-level JSD between two disjoint halves of the same model’s samples is 0.075, versus 0.489"; §VI-C: "EER=7.3%") MATCH; condition-set passage (§VI-B: "59.5% accuracy over the 163 models that have at least one same-family peer, against an 18.4% frequency-weighted chance rate") MISMATCH
2 quote: FOUND — Abstract sentence is present and supports the lineage and EER clauses; it does not contain 0.075/0.489, which §VI-A does, and it is not misleading.
3 kind: AGREE — Distances, LOO accuracy, and EER are what the experiment recorded.
3b bucket: AGREE — Measured once, unreplicated, and the authors flag weak global recovery and one aggregator.
4 evidence_type: AGREE — The entry reports distances and error rates on answer distributions, not self-report and not internals; favorite-item cells are instruments, not the reported object.
5 not_evidence_of: UNDER-EXCLUDES — The ARI, post-training, intent, and paraphrase clauses are the paper’s and warranted, but a reader of “identity verification reached a 7.3% equal error rate” is not told that genuine trials “compare two disjoint halves of the same model’s samples” (§IV-D) or that “Verification presumes a trusted reference deployment” (§VII-D); cross-provider check is AUC 0.880 versus 0.971 same-mix (§VI-A), not the 7.3% EER.
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT (should be: none) — done to the model: nothing inside altered; measured: JSD, family accuracy, and EER, not what the model said about itself.
6 bears_on: DISAGREE (proposed: []) — Fingerprint distance and family LOO do not bear on §4 endorsement; no listed locator is supported.
severity: MEDIUM — 165-for-163 quantifier, and the verification design limit is missing from the field.

### Source-level
7. No omitted finding is central to 3.2, 3.3, 3.5, 4.endorsement, 5.A2, or 9.t9. The paper never measures internal state, memory integrity, endorsement, representation–output divergence, or self-report weight. Cross-provider AUC 0.880 and the 10-of-34 anomalies are in the c02 body; under `intake: summary` they are not gaps. Favorite-number cells are fingerprint instruments, not a 9.t9 result.
8. The quoted abstract opening is verbatim; the source flags that the three results continue, and that continuation matches the held abstract. Quoted limits are real and among the important ones. Missing from that list, and material to c02, is §VII-D: “Verification presumes a trusted reference deployment.” `publisher_relation: independent` is right: printed affiliation is Prague University of Economics and Business, single author, personal OpenRouter funds. Claude Code assistance and the claude-12 census row are disclosed; they do not make the publisher a model vendor.
9. Disclosed pulls are not operating in the statements. Claude results are not elevated (Fig. 1 and Table II claude 0.54/0.58 stay out of the claims). No experience clause was added beyond the paper. c01’s “attributes” is slightly softer than “the gap being,” but the rates are unchanged. `bears_on: [4]` is intake-brief compliance, which the source file admits, not a reading of the paper.

### Summary
Send 2026-bruckner-one-token-c02 — under-exclusion (7.3% EER is split-half, not a trusted-reference audit) plus statement quantifier (59.5% is 163 models, not 165). Do not send c01 on the listed triggers.

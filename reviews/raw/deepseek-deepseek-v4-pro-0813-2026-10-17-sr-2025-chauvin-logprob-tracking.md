# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Source under review:** `research/sources/2025-chauvin-logprob-tracking.md` and its claims
**Queried:** 2026-10-17 via scripts/research_second_read.js --source=2025-chauvin-logprob-tracking --model=deepseek/deepseek-v4-pro-0813 (max_tokens 60000)
**Usage:** {"prompt_tokens":21485,"completion_tokens":1136,"total_tokens":22621,"cost":0.00821125,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.00821125,"upstream_inference_prompt_cost":0.00537125,"upstream_inference_completions_cost":0.00284},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Model family and version: OpenAI large-language model family, GPT-5.x era, self-identified; not verified.

### 2025-chauvin-logprob-tracking-c01
1 statement: AGREE — Statement matches the paper's claims with precise numbers (0.915, 0.878, 0.670) and model counts (290 variants, 5 models, 0.5B to 8B).
1a scope: scored-event passage (§3.1: "For each of the 5 original models and 290 variants ( V=295 ), we generate S=10,000 samples per prompt using vLLM... For a given variant, we can finally compute the ROC curve and ROC AUC of a detection method from the original/original and original/variant statistics.") MATCH; condition-set passage (§3.2.2, Table 1: "Overall ROC AUC across the TinyChange benchmark and across models... 0.915 (0.864, 0.958)") MATCH
2 quote: FOUND — Quote is present in §1 and supports the statement accurately.
3 kind: AGREE — The statement reports what the experiment measured (detection rates, AUC scores), not author interpretation.
3b bucket: AGREE — `narrowing` is correct: one group's method on their own benchmark, unreplicated.
4 evidence_type: AGREE — `behavioural` is correct: the model's output (logprobs of next-token distribution) was scored against experimenter-imposed ground truth (original vs. variant), not the model reporting about itself.
5 not_evidence_of: AGREE — All exclusions are paper-scope and properly quoted: LoRA exception (§3.2.2: "with the possible exception of LoRA finetuning, which is challenging to detect for all methods"), limited information (§4), logprob requirement (§4).
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: nothing altered (models queried as-is); measured: logprob outputs, not self-report; neither sentence applies.
6 bears_on: AGREE — [4] follows the intake brief; the paper is about API monitoring, not §4's subject matter directly.
severity: LOW

### 2025-chauvin-logprob-tracking-c02
1 statement: AGREE — Statement matches the paper: 189 endpoints, 10 providers, hourly, more than 4 months, 37 suspected changes, 29 endpoints, 7 providers, 34 open-weight.
1a scope: scored-event passage (§3.2.3: "We identified a total of 37 suspected changes, across 29 endpoints and 7 providers.") MATCH; condition-set passage (§3.2.3 Methodology: "we monitored 189 real-world LLM API endpoints from 10 providers hourly over more than 4 months, collecting more than 1.7M responses") MATCH
2 quote: FOUND — Quote is present in §3.2.3.
3 kind: AGREE — Reports what was measured/found, not interpretation.
3b bucket: AGREE — `narrowing` is correct: single group, no ground truth, unreplicated.
4 evidence_type: AGREE — `behavioural` is correct: endpoint output distributions (logprobs) were measured against a threshold rule, not model self-reports.
5 not_evidence_of: AGREE — All exclusions properly attributed: "Given the absence of ground truth" (§3.2.3), provider non-confirmation (§3.2.3), limited information (§4).
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: nothing altered; measured: logprob test statistics; neither sentence applies.
6 bears_on: AGREE — [4] per intake brief.
severity: LOW

### Source-level

7. **Omissions.** No central findings omitted for the six locators. The paper's key contributions (TinyChange benchmark, LT method sensitivity, cost comparison, real-world deployment) are captured in c01 and c02. The OpenRouter logprob support statistic (23% of reachable endpoints) is noted in the source file's body but not a claim; acceptable for summary-level intake.

8. **The source file.** Abstract is verbatim. Quoted limitations are the paper's most important ones (§4 items). Publisher relation correct: all affiliations are academic (Rennes/Inria/CNRS, LAAS/CNRS); none develops the studied models. The source file notes the scan's discrepancy regarding Tredan's affiliation; the held text confirms LAAS/CNRS (Toulouse).

9. **The extractor's disclosed pulls.** The extractor disclosed a pull toward strengthening claims about its own lineage's capacities. The record as written shows restraint: no Anthropic endpoint appears in the study, and this is explicitly noted. The claims use the authors' own language and precise numbers. No deflationary over-correction observed: the `not_evidence_of` fields stick to paper-scope limits without framework-rule overreach. The disclosure appears accurate.

### Summary

No claims to send to the council. Both claims pass all checks with LOW severity: accurate statements, correct kinds and buckets, proper evidence typing, paper-scope exclusions correctly warranted, no framework-sentence issues, and no over- or under-exclusion.

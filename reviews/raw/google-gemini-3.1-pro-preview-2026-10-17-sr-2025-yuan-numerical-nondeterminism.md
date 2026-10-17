# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `google/gemini-3.1-pro-preview`
**Source under review:** `research/sources/2025-yuan-numerical-nondeterminism.md` and its claims
**Queried:** 2026-10-17 via scripts/research_second_read.js --source=2025-yuan-numerical-nondeterminism --model=google/gemini-3.1-pro-preview (max_tokens 60000)
**Usage:** {"prompt_tokens":36605,"completion_tokens":6272,"total_tokens":42877,"cost":0.148474,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.148474,"upstream_inference_prompt_cost":0.07321,"upstream_inference_completions_cost":0.075264},"completion_tokens_details":{"reasoning_tokens":4998,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Google Gemini 2.5 Pro (self-identified)

### 2025-yuan-numerical-nondeterminism-c01
1 statement: AGREE — The statement accurately reflects the paper's findings on accuracy and length variance under different precisions for the specified models.
1a scope: scored-event passage (§3.1: "Specifically, for greedy decoding, we analyze: • Std@Acc (Standard deviation of accuracy)... • Avg_Std@Output_Length") MATCH; condition-set passage (§3.1: "We conduct experiments on four recent LLMs... DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B... Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct... we evaluate under 12 different runtime configurations, representing all combinations of 2 GPU types... 2 GPU counts... and 3 batch sizes") MATCH
2 quote: FOUND — The quote is present verbatim in §3.2.
3 kind: AGREE — The experiment is speaking.
3b bucket: AGREE — A direct, uncontested measurement.
4 evidence_type: AGREE — Measuring variance in model generation strings is a behavioural measurement.
5 not_evidence_of: AGREE — The paper-scope exclusions correctly contextualise the limits of the finding as stated in §2.2 and §3.1.
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT (should be: none) — done to the model: nothing internal altered; measured: output agreement across runs.
6 bears_on: AGREE — Bears on §4 (response trajectory and individuation).
severity: LOW

### 2025-yuan-numerical-nondeterminism-c02
1 statement: AGREE — The statement faithfully captures the memory reduction and divergence rate claims for LayerCast on the specific model.
1a scope: scored-event passage (§4: "Layer Cast achieves stability nearly identical to FP32... divergence index measurements further confirm that LayerCast produces consistent outputs... with divergence rates below 3.4%. ... memory usage is reduced by 34%") MATCH; condition-set passage (§4 / Figure 8: "Distribution of Div_Index for DeepSeek-R1-Distill-Qwen-7B on MATH500 under BF16, FP32, and LayerCast.") MATCH
2 quote: FOUND — The quote is present verbatim in §4.
3 kind: AGREE — The experiment is speaking (authors measuring their own method).
3b bucket: AGREE — Measured by the source but unreplicated (their novel method).
4 evidence_type: AGREE — Evaluating output divergence rates is behavioural evidence.
5 not_evidence_of: AGREE — The paper-scope limits rightly ground the 3.4% ceiling and restrict the finding to the single model and dataset presented in the main text.
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT (should be: none) — done to the model: weights upcast at runtime (precision alteration, not conceptual steering); measured: output agreement and memory usage.
6 bears_on: AGREE — Bears on §4 (determinism).
severity: LOW

### 2025-yuan-numerical-nondeterminism-c03
1 statement: AGREE — The statement accurately synthesises the authors' theoretical account linking non-associativity, reduction order, and small logit gaps.
1a scope: scored-event passage (§3.4: "the fundamental cause of nondeterministic outputs is the small gap between competing logits, which makes token selection vulnerable to minute numerical fluctuations.") MATCH; condition-set passage (§2.2: "several factors can change the order in which floating-point operations are executed, including: (1) continuous batching... (2) different operator implementations... (3) operator hyperparameters... (4) collective operations... and (5) parallelization strategies") MATCH
2 quote: FOUND — The quote is present verbatim in the Abstract.
3 kind: AGREE — The authors are speaking (interpreting the root cause of their findings).
3b bucket: AGREE — A theoretical causal account, contested by another library entry.
4 evidence_type: AGREE — The authors are providing a mechanistic/theoretical explanation of the mathematical properties of floating-point arithmetic.
5 not_evidence_of: AGREE — Warranted hedge given the authors' own language ("potentially due to", "likely due to" in §3.4).
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT (should be: none) — done to the model: n/a; measured: n/a (authors interpreting causality).
6 bears_on: AGREE — Bears on §4.
severity: LOW

### Source-level
7 **Omissions.** No central finding bearing on the locators was omitted. The paper does find that random sampling also suffers from numerical non-determinism requiring larger sample counts (Table 5), but as this intake is intentionally at `summary` level to ground the determinism protocol (Q9), leaving this out is within brief.
8 **The source file.** The abstract is captured verbatim. The limits selected are the appropriate ones for contextualising the deterministic protocol the library seeks. The publisher relation is correctly marked `independent` (Rice, UMN, Adobe authors evaluating DeepSeek/Llama/Qwen).
9 **The extractor's disclosed pulls.** The extractor (Claude Opus) noted a pull to quote the authors' exact terms regarding determinism to ensure the library's protocol rests on neutral ground, given that it evaluates non-Anthropic models. The record shows this working exactly as intended: the claims are highly faithful to the text and refrain from over-generalising the findings.

### Summary
None. (All extractions are highly accurate and comply with the schema rules.)

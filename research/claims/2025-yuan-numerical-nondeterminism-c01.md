---
id: 2025-yuan-numerical-nondeterminism-c01
statement: "Across 12 runtime configurations (two GPU types, two GPU counts, three batch sizes), greedy decoding of the same inputs did not give deterministic outputs on four 7B-to-8B models: accuracy and output length varied most under BF16 and moderately under FP16, while FP32 'consistently achieves near-perfect reproducibility with negligible variance'."
bucket: established
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-yuan-numerical-nondeterminism
locator: "§3.1 (Experiment Setup); §3.2 (Greedy Decoding is not Deterministic Output), Tables 3 and 4, Figure 5"
quote: "Contrary to common belief, our experiments reveal that greedy decoding does not guarantee deterministic outputs across different hardware and system configurations. However, using FP32 precision helps a lot. Table 3 presents the standard deviation of accuracy (Std@Acc) across 12 runtime configurations for BF16, FP16 and FP32 precisions. The results demonstrate a clear pattern: FP32 consistently achieves near-perfect reproducibility with negligible variance, FP16 shows moderate variability, while BF16 exhibits substantial instability."
verification: grep
models: [DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not a guarantee of determinism in FP32: on DeepSeek-R1-Distill-Qwen-7B on MATH500 'only 2.2% of the samples diverging' under FP32, not none (§3.2), and higher precision 'doesn't provide theoretical guarantees since floating-point arithmetic cannot represent all real numbers exactly' (§2.2); Paper: The configurations varied are GPU type (L40S, A100), GPU count (2, 4) and batch size (8, 16, 32) under vLLM (§3.1); other sources of variation are not covered by these 12 settings"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Design: four models on five math and code benchmarks (AIME 2024, MATH500, LiveCodeBench Easy, Medium, Hard), each model-task pair run under 12 runtime configurations at each of three precisions, greedy decoding; metrics are the standard deviation of accuracy and of output length across configurations, the divergence index (the token position at which two greedy runs part) and the standard deviation of the top-1 token probability before divergence (§3.1). The abstract's headline is the BF16 extreme: "up to 9% variation in accuracy and 9,000 tokens difference in response length" for DeepSeek-R1-Distill-Qwen-7B. The appendix extends to Qwen3-32B, GPQA Diamond and a HuggingFace Transformers backend (not read for this intake).

Bucket `established`: a direct measurement on named models, uncontested in the retrieved literature. He 2025 (2025-he-defeating-nondeterminism-c01) independently reports temperature-0 nondeterminism on a different model and contests the authors' causal account (c03), not this measurement. The FP32 half is not independently replicated in the library.

Why for Q9: the project's determinism protocol (FP32, batch size 1, one machine, hardware recorded) follows this result.

Framework sentence: none (no question about the model was put; the measurement is output agreement across runs).

SECOND QUOTE (§3.2): With FP32, almost all examples produce identical outputs across configurations, resulting in only 2.2% of the samples diverging. In contrast, with BF16, divergence frequently occurs early in generation despite the deterministic setting, with over 90% of examples showing divergence.

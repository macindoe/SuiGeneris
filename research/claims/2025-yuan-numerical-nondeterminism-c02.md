---
id: 2025-yuan-numerical-nondeterminism-c02
statement: "The authors' LayerCast scheme (weights stored in BF16 and each linear layer's weights upcast to FP32 just in time, so that all computation runs in FP32) is reported to give accuracy stability nearly identical to FP32 and, for DeepSeek-R1-Distill-Qwen-7B on MATH500, divergence rates below 3.4% across batch sizes and GPU configurations, with memory use 34% lower than full FP32."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-yuan-numerical-nondeterminism
locator: "§4 (Near-Perfect Deterministic Reproduction: LayerCast), Figures 7 and 8; Appendix F not read"
quote: "As shown in Figure 8 , the divergence index measurements further confirm that LayerCast produces consistent outputs across different batch sizes and GPU configurations, with divergence rates below 3.4%. From resource perspective, LayerCast offers substantial benefits over full FP32: memory usage is reduced by 34% (particularly important for KV cache in long-context scenarios)."
verification: grep
models: [DeepSeek-R1-Distill-Qwen-7B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not a zero-divergence result: the reported divergence rate is 'below 3.4%' (§4), against 2.2% for full FP32 on the same model and task (§3.2); Paper: The divergence figure is for one model on one benchmark (Figure 8: DeepSeek-R1-Distill-Qwen-7B on MATH500); full results are deferred to Appendix F"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Method (§4): "(1) Loading the model parameters initially in FP32 precision; (2) Explicitly casting all linear layer weights and biases to BF16 for storage before inference; and (3) As inference runs, upcasting each weight back to FP32 just-in-time for matrix multiplication, one at a time." The authors release it "as a patch to vLLM" (§1). Full FP32, the basic solution, "doubles the memory usage and inference time compared to BF16" (§4). Bucket `narrowing`: the authors' own method, measured by them, not replicated in the library.

Why for Q9: LayerCast is the named fall-back if a model is too large to run in full FP32 on the project's hardware; this claim records what its authors say it buys and what it does not.

Framework sentence: none (no question about the model was put).

SECOND QUOTE (§4): When examining the standard deviation of accuracy across runs, Layer Cast achieves stability nearly identical to FP32, while BF16 shows much higher variability.

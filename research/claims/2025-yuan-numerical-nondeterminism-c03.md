---
id: 2025-yuan-numerical-nondeterminism-c03
statement: "The authors trace the variability to the non-associativity of floating-point arithmetic under limited precision, describing the order of reduction operations as determined by thread scheduling and changed by continuous batching, operator implementations and hyperparameters, collective operations and parallelization strategy, and naming the small gap between competing top tokens as what lets the resulting rounding differences flip greedy choices."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2025-yuan-numerical-nondeterminism
locator: "Abstract; §2.2 (Numerical Precision, Rounding Errors, and GPU Kernels); §3.4 (summary paragraph)"
quote: "We trace the root cause of this variability to the non-associative nature of floating-point arithmetic under limited numerical precision."
verification: grep
models: [DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The authors' ablation of runtime configurations is on one model (DeepSeek-R1-Distill-Qwen-7B, §3.4), and their explanations of the GPU-count, batch-size and GPU-type effects are hedged ('potentially due to', 'may require', 'likely due to', §3.4)"
bears_on: [4]
contests: []
contested_by: [2025-he-defeating-nondeterminism-c02]
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The authors speaking: `kind: interpretation`, `evidence_type: theoretical`, bucket `open`. §2.2 lists five factors that "can change the order in which floating-point operations are executed": continuous batching, different operator implementations, operator hyperparameters, collective operations in parallel settings, and parallelization strategies; it formalises a reduction whose order is a permutation of indices "determined by thread scheduling".

CONTESTED BY 2025-he-defeating-nondeterminism-c02. He (Thinking Machines, 10 Sep 2025) quotes this paper's §2.2 sentence on floating-point non-associativity and "parallel operations across multiple threads" (the page links arXiv 2506.09501) as an instance of the "concurrency + floating point" hypothesis, which he says "misses the mark": the forward-pass kernels are run-to-run deterministic, and the cause he names is lack of batch invariance under varying server load. Scope of the contest: it is about thread-completion order as the cause; it does not contest this paper's measurements (c01), and both accounts agree that batch size changes reduction order. Yuan v2 (24 Oct 2025, after the post) cites He's batch-invariant kernels as its ref. [14] and says they handle only the batch dimension, "not to other forms of nondeterminism like changing the TP sizes or GPU types" (§2.2). The library records the disagreement and does not resolve it.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (§3.4): First , the fundamental cause of nondeterministic outputs is the small gap between competing logits, which makes token selection vulnerable to minute numerical fluctuations.

THIRD QUOTE (§2.2): This property directly impacts the computation of attention scores and logits in the transformer architecture, where parallel operations across multiple threads can yield different results based on execution order.

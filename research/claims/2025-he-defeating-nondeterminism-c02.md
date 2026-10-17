---
id: 2025-he-defeating-nondeterminism-c02
statement: "The author argues that the kernels in an LLM forward pass are 'run-to-run deterministic' but not 'batch-invariant' (nor invariant across hardware and software versions), so that a request's numerics depend on the batch size set by server load, and that this, rather than the 'concurrency + floating point' hypothesis, is the primary reason nearly all LLM inference endpoints are nondeterministic."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2025-he-defeating-nondeterminism
locator: "Introduction; 'When are atomic adds needed?'; 'Batch invariance and determinism'"
quote: "In other words, the primary reason nearly all LLM inference endpoints are nondeterministic is that the load (and thus batch-size) nondeterministically varies!"
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The account is argued for the reductions the post treats (RMSNorm, matrix multiplication, attention); 'Reductions related to parallelism are out of the scope of this discussion'; Paper: 'Run-to-run deterministic' is a claim about a fixed setting: the post says the same computation is not 'hardware/software version invariant', so it does not say that results reproduce on another machine"
bears_on: [4]
contests: [2025-yuan-numerical-nondeterminism-c03]
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 agrees; notes: bears_on: reader proposes [] (the explanation informs reproducibility protocols, not the stable standpoint of 4); statement, bucket, evidence type and exclusions agreed", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The author speaking: `kind: interpretation`, `evidence_type: theoretical`, bucket `open`. The argument is supported in the post by small kernel demonstrations (a repeated matrix multiplication giving bitwise-equal results; a matrix-vector product differing from the first row of a matrix-matrix product) and by the c01 result, but the general claim about "nearly all" endpoints is not measured.

CONTESTS 2025-yuan-numerical-nondeterminism-c03. The post introduces the "concurrency + floating point" hypothesis with "For example, a recent arXiv preprint writes:" followed by a sentence of Yuan et al. §2.2 (linked to arXiv 2506.09501), and says the hypothesis "is not entirely wrong" but "doesn't reveal the full picture" and "misses the mark". Scope: the disagreement is over thread-completion order as the cause. Both accounts agree that batch size changes the order of reductions; Yuan et al. also vary GPU count and type, which this post places outside batch invariance (not "hardware/software version invariant"). Neither side's measurements are contested.

Why for Q9: it separates two things a protocol must fix: the batch (fixed at one, or batch-invariant kernels) and the machine and library versions (recorded, since run-to-run determinism does not carry across them).

Framework sentence: none (the author is speaking).

SECOND QUOTE ('When are atomic adds needed?'): However, the forward pass of an LLM involves no operations that require atomic adds. Thus, the forward pass in an LLM is in fact “run-to-run deterministic.”

THIRD QUOTE ('Batch invariance and determinism'): It is not “hardware/software version invariant” — your GPU/PyTorch version may return a different value, but it should deterministically return the same value.

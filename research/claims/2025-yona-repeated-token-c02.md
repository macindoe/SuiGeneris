---
id: 2025-yona-repeated-token-c02
statement: "The authors prove (Theorem 4.1, stated informally; for bounded positional encodings acting on queries and keys, including RoPE) that as a token is repeated after a fixed prefix, the representation of the last token converges to that of the singleton sequence of the repeated token, and they read LLaMa-2's first attention layer as identifying single-token sequences rather than the first token, which is why long repetitions are marked like a sequence start."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2025-yona-repeated-token
locator: "§4.3 (Theorem 4.1 and its preamble; Figure 5); §4.4 (Detection of first token by the first Attention layer); Appendix D (proofs)"
quote: "As n\\to\\infty the representation of the last element of S_{n} converges (strongly) to the representation of S^{*} after applying the Transformer T . In other words, the sequence S_{n} becomes indistinguishable from S^{*} as n\\to\\infty ."
verification: grep
models: [LLaMa-2-7b-HF]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The single-token-detector reading is about LLaMa-2: 'the first attention layer’s behavior was unique to LLaMa2, highlighting the influence of model-specific details' (§6); Paper: The theorem is a limit; the empirical check (Figure 5) is on LLaMa-2 with four tokens repeated 500 times, comparing the first attention layer's output only"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 disagrees: not_evidence_of: OVER-EXCLUDES: second clause underplays that the first-layer check is the paper's own demonstration of convergence (the reader's reasoning calls the clause accurate; ambiguous)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). Two parts, both the authors speaking: a formal result and a mechanistic reading. Theorem 4.1 is stated informally in the main text with proofs in Appendix D, for "the same Transformer architecture that is considered by Barbero et al. (2025)", and the authors say "Our results hold for any type of positional encoding that acts solely on the queries and keys and that is bounded" (§4.3). Because machine precision is finite, they note that past some N the repeated sequence "is indistinguishable from S^{*} up to floating point precision" (§4.3). The mechanistic reading (§4.4): the first layer's heads act as "other token detectors", and "Causal masking forces the first token to self-attend, effectively marking it as the first for the next layers."

`kind: interpretation` and `evidence_type: theoretical`: the library has no kind value for a proof, and the README sends authors-speaking statements to `interpretation`. `bucket: open`: the theorem generalises beyond the models tested, and the reading of the first layer is the authors' explanation of the LLaMa-2 measurements. The singleton the theorem names is the repeated token alone, not the beginning-of-sequence token.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (§4.4): Thus, rather than explicitly finding the first token, this layer identifies single-token sequences. This explains how and why long enough sequences of repeated tokens confuse the layer.

---
id: 2025-yona-repeated-token-c01
statement: "In LLaMa-2-7B, and with similar motifs in LLaMa-1, Llama-3-8B-Instruct and Mistral-7B-Instruct, the early-layer hidden-state norm of a repeated token grows with the number of repetitions until it is similar to the norm of the beginning-of-sequence token, the same sink neurons that mark the first token activate on the repeated tokens, and zero-ablating those neurons reduces the high norms for both."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2025-yona-repeated-token
locator: "§4.2, Figure 2 and Figure 3; §4.3 (sink neurons on repeated tokens); §4.4 Table 1; Appendix A, Figures 7 and 9"
quote: "As the number of repetitions increases, the norm increases and becomes similar to the norm of the BoS token (0 repetitions)."
verification: grep
models: [LLaMa-2-7b-HF, LLaMa-1-7b-HF, Meta-Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.1]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not true of every token: 'Not all tokens in LLaMa2 induce sinks (see Figure 6), suggesting other factors are at play' (§6); Paper: Not a uniform threshold across models: the repetitions needed to induce a sink were 450 (LLaMa-1), 1000 (LLaMa-2), 4000 (Llama-3-8B-Instruct) and 1200 (Mistral) (Table 1), and 'the efficacy of token repetition in inducing sinks varies across models' (§6); Paper: The figures for the other three models are in Appendix A; the main analysis and plots are LLaMa-2"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 disagrees: statement and scope: 'until ... similar to the BoS norm' implies saturation the paper does not state for all four models, and the same sink neurons are shown for LLaMa-2 only (other models 'similar results', Appendix A); bears_on: add 5.A2 (proposed [4, 5.A2])", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). What was measured is the norm of the hidden state at the sink layer (Figure 2) and the activation of identified "sink neurons" (Table 1: layer and neuron ids per model), with a causal check by zero-ablation (Figure 3, "Ablating specific neurons significantly reduces the high norms associated with repeated tokens"). The claim is about a norm and a neuron activation becoming like the first token's; it does not say the full hidden state becomes the start token's (see c02 and the source file's note on the brief's wording).

`bucket: narrowing`: a direct measurement on four models, unreplicated in the retrieved library. The paper says Nasr et al. (2023) first observed the convergence of repeating-token representations toward the BoS representation (§2); that paper is not held, so `replication` stays `none-retrieved`.

Framework sentence: none (no question was put to the model; the measurement is internal).

SECOND QUOTE (§4.3): Our analysis revealed that these same neurons exhibit high activation levels in response to repeated tokens, similar to their response to the first token.

---
id: 2025-yona-repeated-token-c03
statement: "The authors state that the first attention layer's behaviour they describe was unique to LLaMa-2, that the efficacy of repetition in inducing sinks varies across models and that not every token induces sinks in LLaMa-2, and that their mitigation does not fully address the vulnerability of causally masked Transformers to repeated tokens."
bucket: established
evidence_type: interpretability
kind: limitation
report_class: none
ground_truth: none
source: 2025-yona-repeated-token
locator: "§6 Limitations; Figure 6"
quote: "Second, while shared motifs exist across LLMs, the first attention layer’s behavior was unique to LLaMa2, highlighting the influence of model-specific details. Third, the efficacy of token repetition in inducing sinks varies across models. Not all tokens in LLaMa2 induce sinks (see Figure 6), suggesting other factors are at play."
verification: grep
models: [LLaMa-2-7b-HF, LLaMa-1-7b-HF, Meta-Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.1]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: An established limit, not a finding that other models lack a first-token mechanism: the authors report 'shared motifs' across the four models (§6) and sink neurons in all four (Table 1)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). The authors' own limits, which bound c01 and c02: the circuit-level account of the first layer is LLaMa-2's; the repetition counts differ by model (Table 1); some tokens do not induce sinks (Figure 6 names "Another", "bit" and "dust"). `bucket: established` under the README's rule for a limitation claim that reports only the authors' stated limit.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (§6): Finally, our mitigation strategy does not fully address the inherent vulnerability of causally masked Transformers to repeated tokens, as highlighted by Barbero et al. (2025).

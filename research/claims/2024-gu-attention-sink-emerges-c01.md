---
id: 2024-gu-attention-sink-emerges-c01
statement: "The first-token attention sink persists when the input is a sequence of tokens sampled at random from the vocabulary (sink metric 70 to 91% across GPT2-XL, Mistral-7B, LLaMA2-7B Base and LLaMA3-8B Base), but on a single token repeated throughout the sequence it falls to 0.00% in the three rotary-encoded Mistral and LLaMA models while GPT2-XL, with learned absolute positions, keeps 62.28%."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2024-gu-attention-sink-emerges
locator: "§3.3 (Attention sink under different inputs, 'Beyond natural languages'); Table 1 (Left)"
quote: "As present in Table 1(Left), attention sink still exists when the inputs are random tokens instead of natural language. However, with repeated tokens, attention sink in Mistral (Jiang et al., 2023) and LLaMA models disappears."
verification: grep
models: [GPT2-XL, Mistral-7B, LLaMA2-7B Base, LLaMA3-8B Base]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The figures depend on the authors' threshold metric (a head counts as sinking when its first-token importance score exceeds epsilon; epsilon = 0.3 in their default setup, §3.2 and §4); Paper: Four pre-trained models, one random-sequence and one repeated-token construction each (Table 1)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees; notes: bears_on: reader proposes [] (a first-token attention rate under random vs repeated tokens fits none of the locators); all other fields agreed", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). Table 1 (Left), sink metric in % for natural / random / repeat inputs: GPT2-XL 77.00 / 70.29 / 62.28; Mistral-7B 97.49 / 75.21 / 0.00; LLaMA2-7B Base 92.47 / 90.13 / 0.00; LLaMA3-8B Base 99.02 / 91.23 / 0.00. The constructions (§3.3): "(i) randomly sample T tokens from the tokenizer vocabulary" and "(ii) randomly sample 1 token from the tokenizer" and repeat it T times. The authors explain the repeated-token result with the derivation in c02; the GPT-2 contrast is the positional-encoding difference.

`publisher_relation: independent`: all four models are other developers' pre-trained models. `bucket: narrowing`: a direct measurement, unreplicated in the retrieved library, on four models.

Framework sentence: none (no question was put to the model; the measurement is internal).

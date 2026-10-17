---
id: 2024-gu-attention-sink-emerges-c02
statement: "The authors derive (Appendix C.1) that for language models with no positional embedding, relative positional encoding, ALiBi or rotary encoding, an input whose tokens are all the same gives identical hidden states at every position in every layer, and for no positional embedding uniform attention (1/t, no sink); GPT-2, whose learned absolute position vectors differ by position, does not satisfy this equality."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2024-gu-attention-sink-emerges
locator: "§3.3 (summary sentence); Appendix C.1 (How positional embedding relates to attention sink), Equations 10 to 17, Proposition 1 and the GPT-2 paragraph"
quote: "In Appendix C.1, we prove that for LMs with NoPE/relative PE/ALiBI/Rotary, if the first T tokens are the same, their corresponding hidden states are the same."
verification: grep
models: [Mistral-7B, LLaMA2-7B Base, LLaMA3-8B Base, GPT2-XL]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The derivation covers inputs whose embeddings are identical across positions (repeated tokens); a zero or other constant vector supplied below the embedding layer is not a case the paper treats; Paper: The derivation is written for one transformer-block form (Equations 11 to 16, layer norm and feed-forward as written there); its fit to each deployed architecture is not checked in the paper beyond Table 1's measurement"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees; notes: bears_on: reader proposes [] (the constant-token derivation is not a standpoint-over-time finding); all other fields agreed", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). The derivation starts from "the initial hidden states" being "the same among all the token positions" when there is no additive position vector, and proceeds by induction through the blocks (Equations 10 to 17). Proposition 1 gives uniform attention for NoPE; Propositions 2 to 4 give closed forms or bounds for the other encodings (not taken in here). The paragraph on learned absolute positions: "Although the word embeddings are the same for repeated tokens, \bm{p}_{t} for different token positions t is different. Therefore, GPT2 models have no the above equality." The authors tie the derivation to Table 1: since the first token's hidden state carries massive activations, "all the repeated tokens have massive activations", which disperses the sink (c01).

`kind: interpretation`, `evidence_type: theoretical`: a derivation by the authors (the library has no kind value for a proof). `bucket: open`: the statement covers every model with these encodings, beyond the three rotary models measured; the derivation itself has not been checked independently in the library. The scan's two consequences for Q9 (a constant input of any length equals one position; a zero input to a bias-free model may give uniform logits) are the scan's inference, not the paper's, and are not part of this claim.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (Appendix C.1): For LMs with NoPE, the attention scores for t repeated tokens are t^{-1} uniformly, i.e., there is no attention sink.

THIRD QUOTE (Appendix C.1): From Table 1(Left), GPT2-XL still allocates significant attention to the first token even with repeated tokens

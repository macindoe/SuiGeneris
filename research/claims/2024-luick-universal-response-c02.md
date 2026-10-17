---
id: 2024-luick-universal-response-c02
statement: "On a once-repeated random-token sequence, the peak of the response shifts across the residual stream from the same token in the other subsequence (offset T₀) to its predecessor (offset T₀ − 1), the induction signature, within intermediate layers of all three models: in Gemma-2-2B mainly between residual-stream positions of about 30 and 40, in GPT-2-XL smoothly between about 30 and 60, and in Llama-3.2-3B with stronger layer-to-layer fluctuations."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2024-luick-universal-response
locator: "§4 (Emergence of induction), Figures 4 and 5"
quote: "As we proceed through the residual stream, we find that the position of this maximum gradually shifts to \\Delta j=T_{0}-1 , predominately within a crossover region between \\ell\\approx 30 and \\ell\\approx 40 ."
verification: grep
models: [Gemma-2-2B, Llama-3.2-3B-Instruct, GPT-2-XL]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Signatures, not a circuit: the author presents the results as 'a benchmark for future circuit analyses within these models' (§4); Paper: Only two-token correlations were measured ('we only considered two-token response functions within this work', Limitations)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees; notes: bears_on: reader proposes [3.2] in place of 4 (a perturbation study of internal state is intervention on internal state; locator 4 taken to be a confusion with the Q9 scan's section 4)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). The paper's headline finding, included so the library carries the author's own term ("induction signatures"). Residual-stream positions ℓ run from 1 to 2L (two per layer: Gemma-2-2B L = 26, Llama-3.2-3B L = 28, GPT-2-XL L = 48; Figure 5 caption). In Gemma-2-2B the response maximum at offset T₀ "is already present within the first layer of the model (\ell=1) and therefore does not result from a composition of components across layers"; the shift to T₀ − 1 comes later. The author's reading: "These results suggest that the induction behavior of Gemma-2-2B is predominately composed within a localized subset of layers within the second half of the residual stream."

`bucket: narrowing`: a direct measurement, unreplicated in the retrieved library, on three models and one input construction.

Framework sentence: none (no question was put to the model; the measurement is internal).

SECOND QUOTE (§4): For GPT-2-XL, this onset is characterized by a smooth transition, localized to positions \ell\approx 30-60 , while for Llama-3.2-3B, there exist stronger fluctuations between adjacent layers

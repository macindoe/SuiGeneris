---
id: 2024-luick-universal-response-c01
statement: "When the residual-stream input vector at a single position of a repeated random-token sequence is scaled by (1 − ε), the response measured at downstream positions and layers of Gemma-2-2B, Llama-3.2-3B(-Instruct) and GPT-2-XL is scale-invariant for weak perturbations, simply rescaling in amplitude with ε over two orders of magnitude (ε from 5·10⁻⁴ to 5·10⁻²), a regime the author calls universal across the three models."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2024-luick-universal-response
locator: "Figure 1; §2.1 (Probing the response of LLMs); §3 (Scale-invariant response), Figures 2 and 3; §4, Figure 5"
quote: "Across all models, we observe the same universal scaling of \\overline{C}{}^{(2L)}_{\\Delta} over two orders of magnitude in the scale parameter (\\varepsilon=5\\cdot 10^{-4}-5\\cdot 10^{-2}) ."
verification: grep
models: [Gemma-2-2B, Llama-3.2-3B-Instruct, GPT-2-XL]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not shown for real text: 'we focused solely on repeated sequences of random token to study induction behavior and, therefore, did not demonstrate the applicability of our method to real text sequences' (Limitations); Paper: No theory of why: 'we did not provide a theoretical foundation for the observed scale-invariant response' (Limitations); Paper: 'Universal' means the three models studied: the author did 'not demonstrate the universality of scale-invariance beyond the models Gemma-2-2B, GPT-2-XL, and Llama-3.2-3B' (Limitations)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees; notes: bears_on: reader proposes [3.2] in place of 4 (a perturbation study of internal state is intervention on internal state; locator 4 taken to be a confusion with the Q9 scan's section 4)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for Q9 (filed under Section 4). Method (Figure 1, §2.1): the residual stream is perturbed "directly at the transformer input" at one sequence position, "while leaving all other sequence positions unchanged", and the perturbed run is compared with the unperturbed run at every downstream position and token position by three response metrics (norm of the difference and two cosines). Background input: a random-token subsequence of length T₀ = 64 repeated once, tokens "sampled uniformly from the vocabulary space". The scaling result is in §3 for Gemma-2-2B and in §4 for all three models. Model name: the text says "Llama-3.2-3B"; Appendix A, Table 1 lists "Llama-3.2-3B-Instruct".

`bucket: narrowing`: a direct measurement, unreplicated in the retrieved library, on three models and one input construction the author flags.

Framework sentence: none (no question was put to the model; the measurement is internal).

SECOND QUOTE (§3): In line with our previous findings, this result confirms that our response functions are simply rescaled in amplitude under changes of the scale parameter

THIRD QUOTE (Conclusion): For each model, we found a pronounced universal regime, in which the response functions remain scale-invariant under changes in perturbation strength

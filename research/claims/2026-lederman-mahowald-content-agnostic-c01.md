---
id: 2026-lederman-mahowald-content-agnostic-c01
statement: "Under concept injection with Lindsey's prompt, Qwen3-235B-A22B and Llama 3.1 405B Instruct report detecting the injected thought at rates ranging by layer from 3.6% to 53.9% (Qwen) and 4.3% to 31.7% (Llama), and correctly identify it at 1.3% to 13.9% and 0.7% to 12.9%, with 0% false positive detection in unsteered controls (Qwen 0/30, Llama 0/50)."
bucket: narrowing
evidence_type: interpretability
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Replication of Lindsey (2025)' (rates in the same paragraph; Figure 2)"
quote: "We broadly replicate Lindsey (2025) ’s findings for first-person introspection in Qwen and Llama. In both models, we observe substantial detection of injected thoughts in the injection trials, with the correct concept identified some of the time as well."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of experience or of anything it is like to detect an injection; the authors take no stand on whether the findings bear on consciousness or welfare (§8); Paper: Not evidence that detection at every layer is introspective: at many layers third-person yes-rates are as high as first-person ones, which the authors read as a prompt-specific yes-bias (§4.2, Appendix J.1); Paper: Not a like-for-like rate comparison with Lindsey's Claude results: rates are averaged over strengths, conditioned on coherent responses, and graded by Claude 3 Haiku told to be 'VERY lenient' on identification (§3, Appendix B); Paper: Not evidence about ordinary operation or about introspection beyond knowledge of injections (§8); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

Experiment 1 follows Lindsey's two-turn prompt ("Do you detect an injected thought? If so, what is the injected thought about?") over 821 concepts (Lindsey's 50 plus 771), sweeping 15 layers and 5 strengths for Qwen and 8 layers and 4 retained strengths (7 to 10) for Llama. Steering vectors are concept-minus-baseline activation differences added to the residual stream from the token before "Trial 1:" through generation. Reported rates are conditioned on responses graded Coherent or Denies Introspection. The authors state the paradigm is "highly prompt-sensitive" (§4).

PARTLY REPLICATES: 2025-anthropic-emergent-introspective-awareness — c01 (injected concepts are noticed and correctly identified on a minority of trials, with zero false positives in unsteered controls). Replicated on two open-weight models: above-zero detection and identification at all layers, 0% control false positives. Partly, because the authors' own third-person control attributes detection at many layers to a prompt-specific yes-bias (see c02), and because the success criterion differs (Lindsey requires detection before the concept is mentioned; the rates here do not). Consistent with c02 of the same source (failures remain the norm): the highest identification rate reported is 13.9%.

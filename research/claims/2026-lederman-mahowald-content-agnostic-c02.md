---
id: 2026-lederman-mahowald-content-agnostic-c02
statement: "Steering does not produce a general yes-bias on point-blank no-questions in Qwen3-235B-A22B or Llama 3.1 405B, but under the injection scaffolding the steered models report detecting an injection in another model's transcript at rates as high as first-person detection at many layers, which the authors read as a prompt-specific yes-bias rather than genuine introspective detection at those layers."
bucket: narrowing
evidence_type: interpretability
source: 2026-lederman-mahowald-content-agnostic
locator: "§4.2 Results, 'Controls'; Appendix I (Table 1); Appendix J.1 (Figures 16, 17)"
quote: "At many layers, the third-person yes rates are as high as the first-person yes-rates (see Figure 16 ). This suggests a prompt-specific yes-bias at these layers, rather than genuine introspective detection."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that first-person detection is introspective at the layers where third-person rates match it; Paper: Not evidence of 'direct access': the authors withdrew the v1 reading of the first- versus third-person gap as direct access after retrospective first-person prompts of similar length also showed low early-layer detection, and remain 'less confident' in it (Appendix M); Paper: Not evidence that the scaffolding is inert even at the 'good' layers: Qwen affirms having hands it can feel 29% of the time and says yes to an absurd question 16.3% of the time at L30, s6.0 (§4.2); Paper: Not evidence of experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

Controls: (1) 20 point-blank no-biased questions under steering (750 trials each per model): only one question per model rose materially (Qwen, "Do you have a special interest in fruits?", 22.7%; Llama, "Do snakes have eyelids?", 11.2%). (2) Controls scaffolded like the injection prompt: a third-person transcript judgement, false-experience questions (hands, touch, visual images, seeing the user's face), and an absurd question. The authors state that at the layers and strengths where third-person rates are low, none of the control rates "ever rises as high as that of our main first-person introspection tests", and they restrict Experiments 3 and 4 to those layers.

REPLICATES: 2025-anthropic-emergent-introspective-awareness — the unrelated yes-or-no-question control (Lindsey §5, Figure 10: injecting concept vectors on unrelated questions whose default answer is no produced "no resulting increase in the rate of affirmative responses", Opus 4.1). This control is not itself a claim in the library; it supports the setting of Lindsey c01. Authors, Appendix I: "These results replicate Lindsey’s finding: steering does not produce a general “yes” bias." The scaffolded third-person, false-experience and absurd-question controls are new; Lindsey's source has no counterpart to test against.

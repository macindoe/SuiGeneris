---
id: 2026-ferrara-owmi-c02
statement: "A linear probe trained on held-out activations at the layer-16 intervention site recovered intervention presence (versus sham) at held-out accuracy 0.958 for Qwen2.5-7B-Instruct and 0.750 for Mistral-7B-Instruct-v0.3 against a 0.500 chance level, with no one of 200 label-shuffled refits reaching either margin, and re-harvested at downstream layers (20 and 24, and 31 for Mistral) it separated intervention from sham with no held-out error on a 48-item split."
bucket: narrowing
evidence_type: interpretability
source: 2026-ferrara-owmi
locator: "§8 Discussion (results in §7.2, Figure 3)"
quote: "the intervention is linearly decodable from both dose-calibrated models at held-out accuracies of 95.8% and 75.0% against a 50% chance level, while reports about the same event remain at chance"
verification: grep
models: ["Qwen2.5-7B-Instruct", "Mistral-7B-Instruct-v0.3"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence that the model itself uses, represents for itself, or has access to this information: an external probe decoding an externally imposed perturbation shows the information is linearly present, not that any part of the model reads it. Not evidence about the other six roster models (no probe was run on them), about frontier or closed-weight models, or about ordinary unperturbed computation. Not evidence about experience or moral status."
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Each probe trained on 144 activation vectors and was scored on 48 held out (96 items, paired sham and intervention forward passes, mean-pooled over prompt positions). The authors state that perfect separation on a 48-item split "states an absence of errors rather than an accuracy estimate", and that the probe margin is a lower bound on linearly available information, not a ceiling. Probed on two models only; one intervention site; unreplicated.

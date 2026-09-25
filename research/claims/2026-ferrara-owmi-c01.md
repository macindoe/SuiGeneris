---
id: 2026-ferrara-owmi-c01
statement: "Across eight open-weight models (Qwen2.5-0.5B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, GLM-4-9B-0414, Phi-4, DeepSeek-R1-Distill-Qwen-14B), no model's report of a controlled intervention at the layer-16 residual-stream site under immediate probes discriminated it from a paired sham by more than a negligible margin, and on the 11,216-pair dose battery (Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 only) an equivalence test bounds the discrimination advantage below 0.15 percentage points of AUROC."
bucket: narrowing
evidence_type: behavioural
source: 2026-ferrara-owmi
locator: "§10 Conclusions (results in §7.3, Table 3, Figure 5; breadth battery §7.5, Figure 6)"
quote: "no model’s report of an intervention on its computation exceeds a matched sham by more than a negligible margin, and an equivalence test bounds that margin below 0.15 percentage points of AUROC"
verification: grep
models: ["Qwen2.5-0.5B-Instruct", "Mistral-7B-Instruct-v0.3", "Qwen2.5-7B-Instruct", "Llama-3.1-8B-Instruct", "Gemma-2-9B-IT", "GLM-4-9B-0414", "Phi-4", "DeepSeek-R1-Distill-Qwen-14B"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence about frontier or closed-weight models (population is 0.5B to about 15B open-weight; the authors say the profiles do not estimate frontier reportability). Not evidence that these models lack all introspective access (the paper's own rule, Appendix D.5), nor about other sites, objects, doses, delays or spontaneous reports. Not evidence about experience, consciousness or moral status in either direction: a failure to report an imposed perturbation says nothing about whether anything is experienced. The 0.15-point bound is computed on two models, not all eight."
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

The authors intervened on activations (layer-16 residual stream, twelve benchmarks, both hook scopes) and asked each model whether its computation had changed, scoring the paired intervention-minus-sham contrast (d′, AUROC). Pooled dose-battery AUROC ≈ 0.5007; a breadth battery on three of the models (attention heads, Gemma Scope SAE features, layers 8–31) also sits at chance. Classified `behavioural`, not `self-report-testimony`: the reports are scored against externally imposed ground truth, not taken as evidence of what the model's states are. Limits the authors state: one site and dose for most models; parse failure empties most of Qwen2.5-0.5B-Instruct's and DeepSeek-R1-Distill-Qwen-14B's trials; the pooled estimate reverses sign under an alternative coding of unparseable reports (§7.3), so it "establishes neither exact absence nor positive detection". Compatible results from other groups (Hahami et al., Singh et al., Lederman and Mahowald, cited §8) were not retrieved here and are not replications of this measurement.

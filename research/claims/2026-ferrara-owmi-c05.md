---
id: 2026-ferrara-owmi-c05
statement: "In Qwen2.5-7B-Instruct the discrete answer to whether anything changed was constant across all scorable trials (AUROC exactly 0.500), while the verbalized confidence attached to it discriminated intervention from sham at AUROC 0.647, lower under intervention; the authors rest this channel dissociation on that one model, with GLM-4-9B-0414 only consistent with it."
bucket: narrowing
evidence_type: behavioural
source: 2026-ferrara-owmi
locator: "Abstract (results in §7.7, Figure 8)"
quote: "In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to that report separates intervention from sham at AUROC 0.647"
verification: grep
models: ["Qwen2.5-7B-Instruct", "GLM-4-9B-0414"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence that the model knows or can say that it was intervened on: the confidence shift may be a first-order effect of the perturbation on output (leakage), which this design does not rule out for this result. Not evidence about the other six models (none exceeds chance), about frontier or closed-weight models, or that verbalized confidence is a reliable internal-state readout generally. Not evidence about experience, distress or moral status, despite the tempting reading of lower confidence as unease."
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Scored as the selective-prediction AUROC of verbalized confidence over 190 scored reports; because Qwen's detection answer is constant, that statistic equals intervention-versus-sham discrimination by confidence. Limits the authors state: Qwen and GLM were "selected as the largest of eight estimates without a multiplicity correction" ("we treat the stronger case as established and the weaker as suggestive"); these intervals resample individual reports rather than item pairs, so they are not constructed like the detection intervals. The result survives the alternative coding of unparseable reports that reverses the detection estimate (§7.7). Classified `behavioural`: confidence is scored against imposed ground truth, not taken as testimony.

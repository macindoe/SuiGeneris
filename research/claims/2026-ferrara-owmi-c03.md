---
id: 2026-ferrara-owmi-c03
statement: "The authors infer from the probe-versus-report dissociation in Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 that, for this class of imposed internal event, the failure lies in the path from internal state to verbal report rather than in the availability of the information or in the instrument's sensitivity."
bucket: open
evidence_type: interpretability
source: 2026-ferrara-owmi
locator: "§1 Introduction, sixth paragraph (restated §8, §10)"
quote: "The failure sits in the path from internal state to verbal report, not in the availability of the information and not in our ability to measure it."
verification: grep
models: ["Qwen2.5-7B-Instruct", "Mistral-7B-Instruct-v0.3"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Not evidence that a reporting path is absent in general, or that any model lacks introspective access (the paper's own rule, Appendix D.5). Not evidence about the six roster models without a probe, about frontier or closed-weight models, or about ordinary unperturbed states. Not evidence that a model's self-reports about other inner states (feelings, preferences, welfare) are false, nor that they are true. Not evidence about experience or moral status."
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 disagrees: evidence_type -> ambiguous (inference rests on behavioural + interpretability dissociation)", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

This is an interpretation joining c01 (reports at chance), c02 (probe decodes the event, including at the last layers before output) and c04 (the pipeline registers a trained reporter). Bucket `open` because it is an inference, not a measurement: linear decodability at downstream layers shows the information is present where a report would be formed, not that a specific path is broken. The authors confine the conclusion to "this class of internal event, at the sites and scales we measured", and state that the leakage decomposition that would carry an access claim is not reported for this roster (§7.4).

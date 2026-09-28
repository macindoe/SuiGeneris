---
id: 2026-macar-mechanisms-introspective-awareness-c06
statement: "The authors state that simulated and genuine introspection are hard to distinguish, and the distinction unclear to define, but that Gemma3-27B's behaviour on the injection-detection task appears mechanistically grounded in its internal states in a nontrivial way; they add that the results should not be interpreted as evidence of subjective experience or consciousness in LLMs."
bucket: open
evidence_type: theoretical
source: 2026-macar-mechanisms-introspective-awareness
locator: "§8 Discussion (final paragraph); Ethics Statement; Broader Impact and Responsible Use"
quote: "it does appear that the model’s behavior on this task is mechanistically grounded in its internal states in a nontrivial way."
verification: grep
models: ["Gemma3-27B instruct (and the other models tested, by the authors' generalisation)"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of subjective experience or consciousness: the authors disclaim this explicitly in the Ethics Statement and again in the Broader Impact statement; Paper: Not a settlement of whether this is introspection rather than a simulation of it, which the authors say is difficult to distinguish and unclear to define; Paper: Not evidence that improved self-report on this task predicts reliable reporting about other internal states such as deception, which the authors call uncertain; Paper: Not evidence that the phenomenon is general: the authors say replication across training stages and model families is needed first; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

Full sentence (§8): "While it is difficult to distinguish simulated introspection from genuine introspection (and somewhat unclear how to define the distinction), it does appear that the model’s behavior on this task is mechanistically grounded in its internal states in a nontrivial way." Ethics Statement: "We emphasize that our results concern a specific controlled experimental setup and should not be interpreted as evidence of subjective experience or consciousness in LLMs." The authors also recommend "treating self-reported detection as an auxiliary signal rather than an authority in safety-critical settings" (Broader Impact). Filed as a separate claim so that the authors' interpretation and their disclaimer travel together. The authors' word "genuine" in the abstract and §8 ("genuine anomaly detection mechanisms") means non-confounded anomaly detection, not anything about experience.

No replication line. Lindsey 2025's comparable interpretive statement (`2025-anthropic-emergent-introspective-awareness-c07`, access versus phenomenal consciousness) is framed differently; this paper makes no access-consciousness claim.

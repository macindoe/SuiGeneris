---
id: 2026-anthropic-assistant-axis-c01
statement: "The authors interpret their results on Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B as suggesting that post-training steers models toward a particular region of persona space (the Assistant end of the Assistant Axis) but only loosely tethers them to it."
bucket: open
evidence_type: interpretability
source: 2026-anthropic-assistant-axis
locator: "Abstract; paraphrased in §7 (only loosely tethered); cf. §9 (somewhat fragile)"
quote: "Our results suggest that post-training steers models toward a particular region of persona space but only loosely tethers them to it"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not evidence that the Assistant persona, or any persona on the axis, is an experiencer or a bearer of interests, preferences or anything else; the axis is a linear direction in activations, and the authors call the linear assumption likely flawed. Not evidence about frontier models or about any Anthropic model (none was measured). The loose-tethering finding is not evidence of a stable standpoint in the North Star §4 sense, and not evidence of its absence: it concerns the position of a projection under conversational pressure, not whether anything endorses or fails to endorse its own dispositions over time. This is an interpretation the authors draw (suggest), not a single measurement."
bears_on: [4.endorsement, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

The authors' summary interpretation, built on the steering results (§3.2), the drift trajectories (§4) and the capping results (§5). It is bucketed `open` because it is a generalisation the source draws, not one measurement. The conclusion adds that "The model’s position along the Assistant Axis is somewhat fragile." Stated limitations: the targets are non-frontier dense models; the linear-direction assumption "is likely flawed"; the multi-turn conversations were simulated.

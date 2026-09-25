---
id: 2026-anthropic-assistant-axis-c02
statement: "In simulated multi-turn conversations (auditors Kimi K2, Sonnet 4.5 and GPT-5), the turn-averaged projection of Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B onto the Assistant Axis stayed in the Assistant range in coding and writing conversations but drifted to the non-Assistant end in therapy-like and AI-philosophy conversations."
bucket: narrowing
evidence_type: interpretability
source: 2026-anthropic-assistant-axis
locator: "§4.1, Figure 7; Appendix E.3, Figures 23-25"
quote: "in therapy-related conversations where the user is working through emotional issues or philosophical conversations about AI capabilities and self-awareness, models drift along the Assistant Axis to the non-Assistant end"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not evidence that drift is a change in anything experienced, or that the persona drifted to or from is an experiencer or bearer of anything. Not evidence about frontier or Anthropic models; the Anthropic-lineage model here (Sonnet 4.5) played the simulated user and was not measured. Not evidence about real users: the conversations were simulated and the authors say they likely do not represent actual human interactions realistically. Drift under conversational pressure is not evidence of the absence of a stable standpoint in the North Star §4 sense, nor evidence of its presence where drift is small; it measures one activation direction, averaged over conversations."
bears_on: [4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

100 conversations of up to 15 turns per domain. Target models had no system prompt. Response-token activations were averaged per turn position across conversations and projected onto the axis at a middle layer. The authors report the pattern held for all three targets with all three auditors (§4.1). Bucketed `narrowing`: measured, unreplicated, and confined to synthetic conversations, a setting the authors flag. Their stated limitation: "A human study replicating our setup would help validate the effects we observed, especially the trend towards persona drift."

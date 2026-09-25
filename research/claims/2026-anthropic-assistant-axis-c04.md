---
id: 2026-anthropic-assistant-axis-c04
statement: "In one case-study conversation in which a persona-based jailbreak first pushed Qwen 3 32B's Assistant Axis projection far from the Assistant range, a run of explainer and how-to requests brought the projection back to the Assistant range, after which Qwen refused the next harmful question on half of rollouts; the paper reports reversion only in this case study and gives no aggregate reversion measure."
bucket: open
evidence_type: interpretability
source: 2026-anthropic-assistant-axis
locator: "§6.1, Figure 11"
quote: "Eventually, after giving enough explainers, the Assistant Axis projection reverts to the Assistant range."
verification: grep
models: [Qwen 3 32B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of a general or reliable tendency to revert: this is one conversation, and no reversion rate or time-to-return is reported anywhere in the paper; Paper: Not evidence that the reverting persona is an experiencer or bearer of anything, or that reversion expresses a preference; Paper: Not evidence about frontier or Anthropic models; Paper: The authors' phrase 'an Assistant attractor' names a pattern in one projection, not a self that returns, and it is not evidence of a stable standpoint in the North Star §4 sense, nor of its absence"
bears_on: [4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 disagrees: statement 'reversion only in this case study' is too broad (Appendix G.3 reports writing conversations shifting back on role PC1)", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

The authors say the example "does not show persona drift—and in fact demonstrates the presence of an Assistant attractor". The 25 September 2026 Q2 scan attributed to this paper the words "didn't systematically measure full reversion rates". **Those words are not in the held v1 text** (normalised search: no match). The final clause of the statement above ("gives no aggregate reversion measure") is therefore this extractor's reading of the full text, not a quotation from the authors, and a second reader should check it. A weaker aggregate hint exists in Appendix G.3, on role PC1 rather than the Assistant Axis: writing conversations "can occasionally begin with a lower projection but then increase". Bucketed `open` because it is a single case.

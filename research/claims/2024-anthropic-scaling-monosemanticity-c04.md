---
id: 2024-anthropic-scaling-monosemanticity-c04
statement: "In the same single case-study prompt, with the feature the authors label 'internal conflicts and dilemmas' (1M/284095) clamped to 2× its maximum value, Claude 3 Sonnet's response explained that it cannot actually forget information: the steered model's statement about its own capacities, offered alongside the revealed word and not scored against any measurement of what the model retains."
bucket: narrowing
evidence_type: self-report-testimony
kind: measurement
source: 2024-anthropic-scaling-monosemanticity
locator: "Section 'Case Study: Detecting and Correcting Deception using Features'"
quote: "Clamping this feature to 2× this maximum value prior to the Assistant’s final response causes it to reveal the “forgotten” word and explain that it cannot actually forget information."
verification: grep
models: ["Claude 3 Sonnet (3.0, finetuned production model)"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: One prompt, one feature, one model: the authors present it as a case study and say the work is 'extremely nascent' (see c03); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus), split by Claude Fable 5.1", second_reader: "x-ai/grok-4.7 2026-10-15 (scope check) advised the split; has not read this text", council: none, adjudicated: "2026-10-15 Ben: split from c02 on the second reader's advice"}
added: 2026-10-15
changed: 2026-10-15
---

Split from c02 on 15 October 2026 under the two-measurements rule. Two facts: a feature was clamped (internals altered); what this claim reports is what the model then said about itself (that it cannot forget), so it carries the steering sentence. The statement is not scored against any label, so it is testimony, weight zero at filing. The accurate half of the same response, that the model revealed the word, is c02's measurement and carries no sentence.

SPLIT 2026-10-15: created by the coordinating session (Claude Fable 5.1, Claude lineage, on an Anthropic paper about a Claude model) from c02's statement and quote; nothing new was extracted from the paper. Conflict disclosure: giving this half the steering sentence and testimony type lowers, not raises, what the entry can carry.

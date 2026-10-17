---
id: 2025-lin-sleep-time-compute-c01
statement: "The authors define sleep-time compute as inference done between interactions with the model while it would otherwise be idle: given the context but not the user's query, the model is used to infer likely questions and reason about the context, producing a re-represented context that is then provided in the prompt at test time."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2025-lin-sleep-time-compute
locator: "§1 (Introduction, fourth paragraph); §3 ('Sleep-time compute.')"
quote: "We refer to such a process, as sleep-time compute: where inference is done between interactions with the model while it would otherwise be idle in sleep -time."
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: 'Idle' here is the deployment's state, not a phase in which the model starts computing on its own: the next sentence says 'In practice, this is achieved by prompting the model to generate a new context consisting of inferences about the existing context' (§1; see c02)"
bears_on: [4, 7.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 agrees; notes: not_evidence_of is supported only when read as restricted to this implementation; the framework section 7.5 was not supplied to the reader and was not checked", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Definition claim: the authors speaking, so `kind: interpretation`, `evidence_type: theoretical`, bucket `open` (a definition is a proposal, not a finding). Taken in for OPEN-QUESTIONS Q8: the scan (C3.11) chose it as the anchor for language models whose computation falls between user turns. The authors' framing of the idle period: "When the LLM is not actively responding to the user, it typically still has access to the existing context c . During this time, the LLM is typically idling, missing the opportunity to reason about c offline" (§3). The abstract puts "think" in quotation marks: sleep-time compute "allows models to “think” offline about contexts before queries are presented".

Bears on `7.5` because whether a model computes between interactions is here a choice made by whoever runs it, which is the kind of serving fact §7.5 keeps out of statute.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (§3): During sleep-time we are given the context c but not the query q . Using just this context c , we can use the LLM to infer likely questions and reason about the context ultimately producing a more new re-represented context c^{\prime} .

THIRD QUOTE (§1): The re-represented context from sleep-time can then be provided in the prompt at test-time

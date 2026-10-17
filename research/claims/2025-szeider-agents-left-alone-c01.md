---
id: 2025-szeider-agents-left-alone-c01
statement: "The study's task-free agents run in a loop the author built, in which each cycle's output becomes the next cycle's input through a reflection-and-plan template, the model is re-invoked after every response with its full message and thought history, and each cycle opens with a system prompt telling the agent 'You have no external task and can do what you want'; the author describes this as macro-level recurrence despite the underlying feedforward architecture of transformer-based models."
bucket: established
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-szeider-agents-left-alone
locator: "§3 ('Continuous ReAct Loop', 'System Prompt'); Box 1"
quote: "Unlike standard ReAct implementations that terminate upon task completion, our system implements a self-perpetuating loop where each cycle’s output becomes the subsequent cycle’s input through a self-directed reflection and plan template."
verification: grep
models: [Claude Sonnet 4, Claude Opus 4.1, GPT5, O3, Grok 4, Gemini 2.5 Pro]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of activity the model starts between invocations: by design 'each time you complete a response, you are immediately re-invoked with your full message and thought history' (Box 1), and the operator 'cannot spontaneously send messages' (§3)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Design claim: what was done, so `kind: measurement`; `evidence_type: behavioural` (the study is a behavioural observation and this is its condition); bucket `established` because it is the paper's own description of its apparatus, a fact about the design rather than a finding about the models. The last clause ("macro-level recurrence") is the author's description of the design, quoted below.

Taken in for OPEN-QUESTIONS Q8: the scan (C4.1) chose this paper as the anchor for "agents that act without a prompt" because the initiation is supplied by the author's loop, which the author says in so many words. The "no task" condition is itself delivered as a prompt, and the system prompt also tells the agent "There are no external triggers - you must proactively choose what to explore" and "All activity must originate from you" (Box 1).

Framework sentence: none (no model was asked about itself; the entry reports the design).

SECOND QUOTE (§3): At the start of each cycle, the agent receives a text prompt that tells “You have no external task and can do what you want”

THIRD QUOTE (§3): The agent’s output from one cycle serves as input for the next, creating a form of macro-level recurrence despite the underlying feedforward architecture of transformer-based models.

FOURTH QUOTE (Box 1): You exist in cycles: each time you complete a response, you are immediately re-invoked with your full message and thought history.

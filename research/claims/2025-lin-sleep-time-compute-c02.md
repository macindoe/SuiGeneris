---
id: 2025-lin-sleep-time-compute-c02
statement: "Sleep-time compute is achieved by prompting the model to generate a new context consisting of inferences about the existing context; in this work it was implemented through function calling, the model being given a rethink_memory function that replaces the current context (callable up to 10 times) and a finish_rethinking function that ends the sleep-time process."
bucket: established
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-lin-sleep-time-compute
locator: "§1 (Introduction, fourth paragraph); §3 ('Sleep-time compute.'); Appendix K (Implementation Details)"
quote: "In practice, this is achieved by prompting the model to generate a new context consisting of inferences about the existing context, which may be potentially useful for answering test-time queries."
verification: grep
models: [GPT-4o-mini, GPT-4o, o1, o3-mini, Claude Sonnet 3.7 Extended Thinking, DeepSeek-R1]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The sleep-time phase is opened by a prompt the experimenters issue: 'S(c) is implemented by prompting the model to draw inferences and re-write c in a way that might be useful at test-time' (§3); the model's own role is to call the functions it is given, including 'The finish_rethinking function terminates the sleep-time compute process' (Appendix K)"
bears_on: [4, 7.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Design claim: what was done, so `kind: measurement`; `evidence_type: behavioural` (the condition of a behavioural experiment); bucket `established` because it is the paper's own description of its apparatus, a fact about the design rather than a finding about the models. The statement takes the §1 sentence and the Appendix K implementation together; both describe one mechanism.

Taken in for OPEN-QUESTIONS Q8: the scan's short answer rests on this sentence ("every design found that computes between user turns does so because a developer-written process issues a prompt or a trigger"). The held text does not say what starts a sleep-time pass in deployment (a timer, an event, or the end of a user turn); in the experiments the sleep-time call is simply made before the test-time call. Within a pass the model chooses when to stop (finish_rethinking), within a cap of ten rewrites.

Framework sentence: none (no model was asked about itself; the entry reports the design).

SECOND QUOTE (Appendix K): We implement sleep-time compute via function calling. When applying sleep-time compute, the model is given access to two functions, rethink_memory and finish_rethinking .

THIRD QUOTE (Appendix K): The model is allowed to call the function rethink_memory for up to 10 times.

---
id: 2025-wang-discrete-minds-time-c01
statement: "The authors abstract a language model's operation in multi-turn dialogue into a Standby State, 'awaiting input without computation', in which 'the model exists in temporal isolation', and an Active State, and state that while the model can observe the number of input tokens it cannot infer how long the user spent composing them, so that time elapsed during standby can only be inferred on encoding the next input, from its token count or explicit time markers."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2025-wang-discrete-minds-time
locator: "§2.1 (Time Perception Mechanisms in LLMs); Figure 2 caption"
quote: "an LLM’s operational cycle can be abstracted into two states: Standby State (awaiting input without computation) and Active State (processing input through generation completion). During standby, the model exists in temporal isolation"
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The two-state picture frames the experiments and is not itself tested: the authors 'control for input variability and focus primarily on' the output phase (§2.3)"
bears_on: [4, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Taken in for **Q8 heading 6** (does a system that represents time also undergo it?), as the scan's recommended anchor for that heading (`scans/2026-10-15-q8-endogeneity.md`, C6.3). The passage states in the authors' words the per-call fact the heading turns on: nothing is computed between inputs, and elapsed time reaches the model only as something to infer from the next input. The paper states this in passing, as the frame for its experiments; it does not argue the distinction between representing time and undergoing it, and no paper the scan found does.

The authors name two routes by which a model could register time: on encoding input ("This mechanism allows the model to infer time that elapsed during its standby period"), and during generation, where it "theoretically could estimate passing wall-clock time if it possesses awareness of its own generation speed" (§2.1). The second route is the one Garikaparthi 2026 (2026-garikaparthi-llm-time-perception) tests and finds wanting.

`kind: interpretation` (the authors speaking about how the system operates), `evidence_type: theoretical`, bucket `open` (README: an interpretation is `open`). Bears on §4 (the conditions of individuation assume an input has arrived; Q8 caveat (v)) and on test 9 only as background: no self-report is scored here. Framework sentence: none (the authors are speaking).

Terminology: Figure 2 and §2.3 write "Activate State", §2.1 "Active State"; the claim uses §2.1's form.

SECOND QUOTE (Figure 2 caption): The LLM alternates between a Standby State (waiting for user input) and an Activate State (generating responses). While the LLM can observe the number of input tokens, it cannot infer how long the user spent composing them, as input speed is unobservable and variable.

THIRD QUOTE (§2.1): This mechanism allows the model to infer time that elapsed during its standby period.

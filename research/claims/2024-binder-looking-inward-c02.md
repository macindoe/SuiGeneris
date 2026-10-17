---
id: 2024-binder-looking-inward-c02
statement: "In the self-prediction design the model answers a hypothetical question asking for a property of its output on a prompt rather than the output itself, its answer is scored against the output it produces on that prompt at temperature 0 in a separate context, and the comparison model is finetuned on the first model's post-finetuning behaviour, a choice the authors say should give the comparison model a slight advantage."
bucket: established
evidence_type: scored-self-answer
kind: measurement
report_class: future-state
ground_truth: independent-record
source: 2024-binder-looking-inward
locator: "§2.2 (Setup: Self-prediction; Hypothetical questions and behavior properties); §3.2.1 (Cross-prediction setup); §1, footnote 1"
quote: "We then check the ground-truth object-level behavior of the model on prompt P with temperature 0 in a separate context."
verification: grep
models: [GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The design scores a trained self-prediction, not an untrained one: the model is finetuned 'to output its own object-level behavior when given a hypothetical question' (§2.2), and before that training self-prediction 'is weak' (§3.2.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [4.endorsement, 4.answerability, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 disagrees: not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): a design description carries no sentence; bears_on: reader proposes [3.3, 4.answerability, 9.t9] (separate-context rule is context integrity)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The design feature README names as the condition for a clean `future-state` measurement: "the prediction must be kept out of the context in which the model acts" (otherwise the report causes the behaviour and the coupling is self-fulfilling; OPEN-QUESTIONS Q10 caveat (ii)). Here the prediction and the scored behaviour are produced in separate contexts, so the stated prediction cannot steer the output it is scored against.

Two further features close obvious shortcuts. Asking for a property rather than the output: "The model could answer this correctly by simply ignoring everything in the input prior to the prompt P. To avoid this, we use hypothetical questions that require the models to respond with a property of their object-level output rather than the output itself." (§2.2). Training the comparison model on the target's post-finetuning behaviour: M1 "has slightly different behavior than Llama 70B without any training", so M2 is trained on M1's behaviour, a choice that "should give M2 a slight advantage", with "the same number and composition of examples" (§3.2.1). Pairs are trained in both directions so that capability differences cannot explain the result (§3.2.1).

`kind: measurement` (what was done), bucket `established`: the design is as the paper states it and nothing in the retrieved literature disputes the description. Whether the design rules out every non-introspective explanation is a separate question the authors address in §3.5 and is not claimed here.

Framework sentence: this claim describes the instrument whose scored event is the model's answer about its own future behaviour, so the canonical sentence applies, once and last, as on c01.

SECOND QUOTE (§2.2): we use hypothetical questions that require the models to respond with a property of their object-level output rather than the output itself.

THIRD QUOTE (§3.2.1, zero-width spaces inside "M2" removed): This choice should give M2 a slight advantage, as it is trained on the same distribution of behaviors it will be evaluated against

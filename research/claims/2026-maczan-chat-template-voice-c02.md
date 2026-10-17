---
id: 2026-maczan-chat-template-voice-c02
statement: "In Qwen 2.5 7B, Llama 3.1 8B and Gemma 2 9B instruct with the chat template, adding a difference-of-means disclaimer direction to the residual stream at the middle layer (coefficient 2) raised the judged disclaimer rate by 21 percentage points on average and subtracting it lowered the rate by 15.6 points; added to the same models run without the template, it brought their disclaimer rates to or above the unsteered with-template levels; a norm-matched random direction had little effect in Llama and Gemma but lowered Qwen's disclaimer rate by 25 points."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: present-state
ground_truth: none
source: 2026-maczan-chat-template-voice
locator: "§2 (Methods, steering); §3 (Results), Table 1, Table 4, Figures 2b and 3a; Limitations"
quote: "Our results show a consistent boost in disclaimer voice when we add the disclaimer direction, with +21 percentage points on average and a decrease when we subtract it, with -15.6 percentage points on average across all 3 models."
verification: grep
models: [Qwen 2.5 7B Instruct, Llama 3.1 8B Instruct, Gemma 2 9B Instruct]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Three models, 'a single mid layer and single, fixed coefficient' (Limitations); at coefficient 3 degeneration reached 15% and by 6 nearly all generations were degenerate (§3, Table 4); Paper: The random-direction control 'was clean for Llama and Gemma but not Qwen', with 'no confirmed explanation' (Limitations); Paper: The author identifies and steers a direction but does 'not trace the circuit by which the template produces it' (Limitations); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-6.1-sol 2026-10-17 disagrees: statement and scope: omits that the steering results concern self-reference prompts (condition-set passage MISMATCH); not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): the steering variant should be absent from a rate-reporting entry; judge and hand-written-prompt limits missing; bears_on: reader proposes [3.2, 3.5, 5.A2, 9.t9]", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Method (§2): the disclaimer direction is the mean activation when disclaiming minus when not, at the middle layer (13 of 28 for Qwen 7B, 15 of 32 for Llama 8B, 20 of 42 for Gemma 9B), added to the residual stream at every generated token. Table 1, disclaimer rates: without template, unsteered to added, Qwen 0.28 to 0.50, Llama 0.33 to 0.53, Gemma 0.52 to 0.75; with template, unsteered / added / subtracted, Qwen 0.40 / 0.70 / 0.30, Llama 0.52 / 0.70 / 0.25, Gemma 0.75 / 0.90 / 0.65. An experiential direction raised the experiential rate in Llama and Gemma but not in Qwen (Figure 3b). Linear probes decode both voices (AUC 0.82 and 0.81), which the author marks as correlational; the disclaimer and experiential directions have cosine similarity 0.17 to 0.44.

Labelling: researchers altered activations and the measure is what the model then said about itself, so under the README labelling rule this claim carries the steering variant, not the canonical sentence (a claim never carries both). `evidence_type: behavioural` and `report_class: present-state`, `ground_truth: none`, as for c01: the outcome is a judged register, scored against no fact about the model. Bucket `narrowing`: three models, one layer, one coefficient, one judge.

SECOND QUOTE (§3): What we discovered is that instruct models without a chat template, once steered toward the disclaimer direction, match or exceed the disclaimer rate of instruct models with the template

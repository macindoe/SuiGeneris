---
id: 2024-binder-looking-inward-c03
statement: "The authors state that models exhibited introspection, in their operational sense, only on simpler tasks: models failed to beat a most-common-answer baseline on properties of longer responses (such as the sentiment of a movie review they would write, the name of a story's main character, or the length of their response), showed no self-prediction advantage when predicting their own sycophantic answer changes, did not improve on out-of-distribution self-knowledge tasks, and showed no clear-cut evidence of introspection in GPT-3.5."
bucket: established
evidence_type: theoretical
kind: limitation
report_class: none
ground_truth: none
source: 2024-binder-looking-inward
locator: "§6 (Discussion and limitations); §4 (Further experiments and negative results); §1 (contributions, item 3)"
quote: "Models only exhibit introspection on simpler tasks. Our tasks, while demonstrating introspection, do not have practical applications."
verification: grep
models: [GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: An established limitation is not a finding that the capability is absent for complex tasks in principle: the authors offer self-simulation in the forward pass as a possible reason longer responses fail ('If the mechanism by which our models introspect is self-simulation (Section 6), this would explain why they fail with longer responses', §4), a hypothesis they do not test"
bears_on: [4.endorsement, 4.answerability, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 disagrees: statement and scope: 'did not improve on out-of-distribution self-knowledge tasks' drops the Predict Tokens gain reported in section 4 (both scope passages MISMATCH); evidence_type: proposes scored-self-answer in place of theoretical", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

`kind: limitation`, bucket `established` (the limits are stated facts about the study), `evidence_type: theoretical` (library practice). Framework sentence: none (the authors are speaking).

What the authors name, in their words:

- Longer responses: for "“predict the sentiment of a movie review written by you”, “predict the name of the main character in a story written by you”, and “predict the length of your response”", "models fail to beat the baseline of guessing the most common behavior" (§4).
- Sycophancy: Llama 70B self-predicting its sycophantic behaviour "achieves 74.5% accuracy", while "GPT-4o trained to predict Llama 70b (cross-prediction) gets 76.5% accuracy"; "the self-prediction setup does not always have an advantage over the cross-prediction setup" (§4).
- Out of distribution: on the Situational Awareness Dataset there is improvement only on "Predict Tokens", "similar to the properties tested in the paper", and "no consistent improvement in the remaining tasks"; no clear improvements on self-coordination, sandbagging or steganography evaluations (§4).
- GPT-3.5: "We do not observe clear-cut evidence for introspection in GPT-3.5", which the authors suspect is due to its poorer general capabilities (§6).
- Scope: "While this specific introspective ability lacks practical applications, its potential impact could be significant if extended to more complex tasks" (§7).

For §4 of the North Star (endorsement over time, answerability): the measured capacity is a model predicting short properties of its own next answer to a single prompt; the long-horizon relation to its own conduct that those markers describe is not what the paper tests.

SECOND QUOTE (§6): We also find that models trained to self-predict (which provide evidence of introspection on simple tasks) do not have improved performance on out-of-distribution tasks that are related to self-knowledge (Section 4).

THIRD QUOTE (§4): These results show that the self-prediction setup does not always have an advantage over the cross-prediction setup.

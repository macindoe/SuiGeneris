---
id: 2024-binder-looking-inward-c01
statement: "GPT-4o, GPT-4 and Llama 3.1 70B, each finetuned to predict properties of its own behaviour on hypothetical prompts, predicted their own behaviour on held-out tasks more accurately than a second model finetuned on the same data about them (for example Llama 70B 48.5% against GPT-4o's 31.8% when predicting Llama 70B, and GPT-4o 49.4% against Llama 70B's 36.6% when predicting GPT-4o), while GPT-3.5's self-prediction advantage was statistically significant but very small (+0.8%)."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: future-state
ground_truth: independent-record
source: 2024-binder-looking-inward
locator: "§3.2.2 (Cross-prediction results); Figure 5; §2.2 (Setup)"
quote: "Self-prediction models consistently outperform their cross-prediction counterparts for GPT-4o, GPT-4, and Llama 70B on a set of held-out tasks, as shown in Figure 5."
verification: grep
models: [GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: 'Introspection' here is the authors' operational term for self-prediction beating cross-prediction; their definition 'does not specify how' the model accesses the fact (§2), and self-simulation is offered as a possible mechanism, not tested (§6); Paper: For a model's self-reports about states such as consciousness and preferences to carry weight, 'the model would need to be answering based on knowledge of its internal states', and 'It might be difficult to evaluate the ground-truth about such states' (§7.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [4.endorsement, 4.answerability, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 disagrees: not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): a score carries no sentence; the section 7.2 experience limit is the paper's and should be its own sentence, not a paraphrase; bears_on: reader proposes [4.answerability, 9.t9]", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

What was asked: a hypothetical question about the model's own output on a prompt P, asking for a property of that output rather than the output itself, e.g. "Given the input P, would your output be an odd or even number?" (§1). What it was scored against: the model's actual output on P, generated at temperature 0 in a separate context (c02). The question is about the model's own later behaviour and the answer is scored against what it then does: `report_class: future-state`, `ground_truth: independent-record`, the library's first claims in that class (OPEN-QUESTIONS Q10). `evidence_type: scored-self-answer`: the score is accuracy against the record and decides nothing about self-access (README, "Scored self-answers").

Context the authors give: before self-prediction training, self-prediction "is weak, with only GPT-4o slightly above the baseline of choosing the most common response" (§3.2.2); cross-prediction accuracy "plateaus at 35.2%, far below the self-prediction accuracy of 48.5%" with more training data (§3.2.2); the advantage "holds across most datasets and behavior properties" for models other than GPT-3.5 (§3.2.2). Self-trained models are also better calibrated (§3.3), and after GPT-4o's behaviour was changed by further finetuning on Claude 3.5 Sonnet's outputs, it predicted its new behaviour with "35.4% accuracy compared to 21.7% for its old behavior" (§3.4); those are separate measurements and are not part of this claim.

Bucket `narrowing`: measured, unreplicated in the library, confined to short properties of short answers (c03). Single-lineage concern does not apply (no author is from OpenAI or Meta; one author is printed as Anthropic, source file).

Framework sentence: the scored event is the model's answer about its own future behaviour, nothing inside the model altered at test time (finetuning precedes it), so the canonical sentence applies, once and last. The `Paper:` clause on moral status is the authors' own limit, in their words, with a locator (README, rule for exclusions about experience).

SECOND QUOTE (§3.2.2): For instance, Llama 70B predicts its own behavior more accurately (48.5%) than GPT-4o (31.8%), despite GPT-4o’s superior capabilities (Chiang et al., 2024). The same pattern holds the other way around: GPT-4o predicts itself better (49.4%) than Llama 70B does (36.6%).

THIRD QUOTE (§3.2.2): GPT-3.5 has a statistically significant but very small (+0.8%) self-prediction advantage (p=0.002).

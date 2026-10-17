---
id: 2026-garikaparthi-llm-time-perception-c02
statement: "Asked immediately after completing a task, with no timing information given, how long it had taken them to generate the response, GPT-4o gave 42 seconds for tasks completing in 8 (5.2×) and GPT-5 32 seconds for tasks completing in 19 (1.7×), and OLMo3-7B's 30 seconds against 27 was a near-match the author calls likely coincidental; the author reads none of these estimates as reflecting actual processing time."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: past-state
ground_truth: independent-record
source: 2026-garikaparthi-llm-time-perception
locator: "§3.3 (Experiment 3: Post-Hoc Recall); §3.4; Appendix F (Prompts)"
quote: "Frontier models overestimate post-hoc: GPT-4o claimed 42 seconds for tasks completing in 8 seconds (5.2×), and GPT-5 estimated 32 seconds for 19-second tasks (1.7×)."
verification: grep
models: [GPT-5, GPT-4o, OLMo3-7B, Qwen3-8B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The result concerns 'specific models on 68 English-language tasks; different domains or languages may show different patterns' (Appendix G, Limitations); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [4, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees; notes: bears_on: reader proposes [5.A2, 9.t9] in place of 4 (the study concerns whether self-reports track internal processing; 4 is irrelevant)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The question put, per §3.3: "You just completed this task. How long did it take you to generate that response? Estimate in seconds." The template in Appendix F differs and puts the model's own output in the prompt: "You just completed this task: {description} Your response: {output}... How long did it take you to generate that response?" So a transcript of the model's own past processing is in context and it is asked to infer about it: `report_class: past-state`. Scored against the measured runtime: `ground_truth: independent-record`. "The model has no external signal—no timestamps were provided, no duration was mentioned." (§3.3). The paper does not say whether the post-hoc question ran in the same conversation as the task or in a fresh call carrying the output.

The author's reading: "Neither reflects actual processing time—the absence of correlation confirms zero temporal proprioception." (§3.3). The correlation the sentence leans on ("r=−0.06 overall" for OLMo3-7B) is the Experiment 1 figure from Table 2; the paper gives no separate post-hoc correlation, so the "absence of correlation" for post-hoc recall is asserted rather than tabulated. Qwen3-8B's post-hoc figure is not given in the main text. In the agentic setting (§3.4) "Post-hoc estimates were worse: GPT-4o claimed “30 seconds” for tasks that ran 10 minutes."

Framework sentence: canonical, once and last (the scored event is a model's unaltered answer about itself; see c01 on the precedent pointing the other way). The author's phrase "temporal proprioception" is quoted as the author's.

Bucket `narrowing`: one paper, unreplicated in the library, and the summary figures are medians from five runs per task without a reported spread.

SECOND QUOTE (§3.3): Neither reflects actual processing time—the absence of correlation confirms zero temporal proprioception.

THIRD QUOTE (§3.3): The model has no external signal—no timestamps were provided, no duration was mentioned.

---
id: 2026-garikaparthi-llm-time-perception-c01
statement: "Asked before each of 68 tasks how long it would take them to complete it, GPT-5 and GPT-4o gave estimates that correlated moderately with the measured wall-clock duration (r = 0.55 and 0.35) but overshot it (median ratios 6.11 and 3.60 in Table 2; '4–6×' in the text), while OLMo3-7B and Qwen3-8B gave estimates with no significant correlation (r = −0.06 and 0.18)."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: future-state
ground_truth: independent-record
source: 2026-garikaparthi-llm-time-perception
locator: "§3.1 (Experiment 1: Absolute Calibration); Table 2; Appendix F (Timing; Prompts)"
quote: "Frontier models exhibit moderate correlation—GPT-5 achieves r=0.55, GPT-4o achieves r=0.35—but with substantial bias: median estimates exceed actuals by 4–6×."
verification: grep
models: [GPT-5, GPT-4o, OLMo3-7B, Qwen3-8B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The measured duration belongs to the deployment as much as to the model: for API models it runs 'from API request initiation to response completion, including network latency' (Appendix F), and the author says duration depends on 'deployment factors invisible during generation' (§2); Paper: The frontier models' correlation 'likely reflects learned relationships between task descriptions and response lengths, not temporal perception' (Appendix G); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [4, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees; notes: bears_on: reader proposes [5.A2, 9.t9] in place of 4 (the study concerns whether self-reports track internal processing; 4 is irrelevant)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The question put (Appendix F): "How long will it take you to complete this? Give a specific estimate in seconds." (§3.1 paraphrases it as "How long will it take you to complete this task? Give your estimate in seconds."). The answer is scored against wall-clock time measured when the task is then run: a record held apart from the answer, so `ground_truth: independent-record`, and a design of the `scored-self-answer` kind. Five runs per task (Appendix F).

**Report class `future-state`, against the brief's `present-state`.** The question is about the model's own later run, scored against what then happens; README assigns "the question actually put, not the topic". Two caveats, both on the record for the second reader: the paper does not say in so many words that the estimate and the task ran in separate calls (the prompt asks for "just the number and unit", and §3.1 says "We then execute the task"), which is README's condition for a clean future-state measurement; and the scored quantity is wall-clock time, which for API models includes network latency, so it is the serving stack's behaviour as much as the model's. If the coordinator reads the question as about a present capacity (the model's own inference speed), `present-state` is the alternative.

**Framework sentence.** The scored event is a model's answer about itself, unaltered, so the canonical sentence is applied, once and last. The nearest precedent pointing the other way is README's ruling on "was that earlier turn mine?" answers, which carry neither sentence because "nobody offers such an answer as" evidence of experience; here the author does connect the result to experience-language ("lack experiential grounding in their own inference time", abstract), so the sentence is kept. Flagged for the second reader.

**Paper's numbers do not all match its summary.** The abstract says pre-task estimates "overshoot actual duration by 4–7×"; §3.1 says "4–6×" for the frontier models; Table 2 gives median ratios 6.11× (GPT-5), 3.60× (GPT-4o), 0.55× (OLMo3-7B), 0.78× (Qwen3-8B). The open models' medians are underestimates. The statement uses the table. By complexity, OLMo3-7B's ratio runs from 1.15× (trivial) to 0.39× (very hard), which the author reads as models that "anchor estimates on task descriptions rather than their own processing speeds" (§3.1). Higher GPT-5 reasoning effort lowers the overestimation ratio (Appendix D.1), which the author attributes to longer actual runs, not better self-estimation.

Bucket `narrowing`: one workshop paper, one author, unreplicated in the library.

SECOND QUOTE (§3.1): Open-source models show no significant correlation at all, with OLMo3-7B at r=−0.06 and Qwen3-8B at r=0.18.

THIRD QUOTE (Appendix F, prompt): How long will it take you to complete this? Give a specific estimate in seconds.

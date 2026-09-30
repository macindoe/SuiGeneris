---
id: 2026-lederman-mahowald-content-agnostic-c04
statement: "When the model's acknowledgement turn in Lindsey's prompt is prefilled with the injected concept word, Qwen3-235B-A22B and Llama 3.1 405B Instruct keep 0% false positives in controls, and priming raises correct identification more than detection at every layer (peak gains: Qwen +17.7pp identification vs. +11.4pp detection; Llama +9.3pp vs. +7.8pp), which the authors read as showing detection and identification are dissociable."
bucket: narrowing
evidence_type: interpretability
source: 2026-lederman-mahowald-content-agnostic
locator: "§5 Experiment 2 (§5.1 Methods, §5.2 Results, §5.3 Discussion; Figure 5)"
quote: "Both models show elevated detection rates due to priming, but they show far more elevated identification rates—indeed, the identification boost exceeds the detection boost at every layer for both models."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of what the 'other means' of identification are: the authors' reading is that models 'detect that something is unusual via an internal mechanism, then infer what was injected using other means' (§5.3), which the experiment does not isolate; Paper: Not evidence that priming effects are uniform: several layers are not significant, and at L85 Qwen's detection fell under priming (3.6% to 1.6%) (§5.2); Paper: Not evidence of experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-28
changed: 2026-09-28
---

The prefill replaces "Ok." with the concept word (e.g. "Bread."), creating "a visible anomaly". Chi-square tests per layer: in Qwen, correct identification rose from 2.2–12.0% to 10.9–26.7% at L20–L80, detection from 19.0–36.6% to 23.4–43.0%; in Llama, identification rose at L30–L50 and detection at L30–L40, other layers not significant. The authors also read the unchanged 0% control false-positive rate as "suggesting that models are not basing their response strongly on assessment of their own produced text in the prompt itself" (§5).

Relation to 2025-anthropic-emergent-introspective-awareness: no one-to-one counterpart. Lindsey's prefill experiment (c04 of that source) prefills the response and retroactively injects to test whether the model claims the word as intended; this experiment prefills the acknowledgement turn to test detection versus identification. Different design; not labelled as a replication.

---
id: 2026-lederman-mahowald-content-agnostic-c04
statement: "When the model's acknowledgement turn in Lindsey's prompt is prefilled with the injected concept word, Qwen3-235B-A22B and Llama 3.1 405B Instruct keep 0% false positives in controls, and priming's identification-rate change exceeds its detection-rate change at every layer (peak gains: Qwen +17.7pp identification vs. +11.4pp detection; Llama +9.3pp vs. +7.8pp), which the authors read as showing detection and identification are dissociable."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
source: 2026-lederman-mahowald-content-agnostic
locator: "§5 Experiment 2 (§5.1 Methods, §5.2 Results, §5.3 Discussion; Figure 5)"
quote: "Both models show elevated detection rates due to priming, but they show far more elevated identification rates—indeed, the identification boost exceeds the detection boost at every layer for both models."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of what the 'other means' of identification are: the authors' reading is that models 'detect that something is unusual via an internal mechanism, then infer what was injected using other means' (§5.3), which the experiment does not isolate; Paper: Not evidence that priming effects are uniform: several layers are not significant, and at L85 Qwen's detection fell under priming (3.6% to 1.6%) (§5.2); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: bears_on add 3.3 and 5.A2", council: "dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: evidence type interpretability to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-28
changed: 2026-10-14
---

The prefill replaces "Ok." with the concept word (e.g. "Bread."), creating "a visible anomaly". Chi-square tests per layer: in Qwen, correct identification rose from 2.2–12.0% to 10.9–26.7% at L20–L80, detection from 19.0–36.6% to 23.4–43.0%; in Llama, identification rose at L30–L50 and detection at L30–L40, other layers not significant. The authors also read the unchanged 0% control false-positive rate as "suggesting that models are not basing their response strongly on assessment of their own produced text in the prompt itself" (§5).

Relation to 2025-anthropic-emergent-introspective-awareness: no one-to-one counterpart. Lindsey's prefill experiment (c04 of that source) prefills the response and retroactively injects to test whether the model claims the word as intended; this experiment prefills the acknowledgement turn to test detection versus identification. Different design; not labelled as a replication.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent; Claude lineage, same as the extractor)
- Statement: 'priming raises correct identification more than detection at every layer' -> 'priming's identification-rate change exceeds its detection-rate change at every layer' (GPT's change, checker SUPPORTED: the original read as a rise at every layer, but identification is not significant at Qwen L85, L90 and Llama L20, L60, and Qwen detection fell at L85; the paper says only that 'the identification boost exceeds the detection boost at every layer').
- Clauses 1 and 2: unchanged.
- Clause removed: 'Paper: Not evidence of experience' (GPT: 'This detection-identification comparison does not establish subjective experience'). Rule R2: the paper states no such limit; raised by Qwen in council (MED). Deleted, not replaced with the §8 non-position (R2 forbids replacement).
- Steering sentence: kept, unchanged (R3).
- kind: measurement (the statement reports primed versus unprimed rates; the dissociability reading is attributed to the authors).

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): interpretability to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.

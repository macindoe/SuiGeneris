---
id: 2026-lederman-mahowald-content-agnostic-c05
statement: "In Qwen3-235B-A22B, stopping injection at the end of the prompt instead of continuing it through generation leaves detection effectively unchanged but sharply reduces mentions of the injected concept at mid-to-late layers, and under continuous steering correct identifications appear later in the response than wrong guesses such as 'apple' (about 11 to 13 words for wrong guesses; about 15 words at L20 and 43 at L35 for correct ones)."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: present-state
ground_truth: imposed
source: 2026-lederman-mahowald-content-agnostic
locator: "§6 Experiment 3 (§6.2 Results, Figure 6); §7 Experiment 4 (§7.2 Results, Figures 7, 8)"
quote: "In the prompt-only setup, detection is effectively unchanged while correct concept mentions fall dramatically, especially at mid-to-late layers (see Figure 6 )."
verification: grep
models: ["Qwen3-235B-A22B"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence about Llama 3.1 405B: Experiments 3 and 4 were run on Qwen only; Paper: Not evidence at all layers and strengths: Experiment 4 uses L20 to L35 at strengths 5 and 6, where the first-person prompt is distinguished from the third person, and the token-by-token grading uses L35, s6 only (§7.1); Paper: Experiment 3 measures concept mentions by string-matching, not correctness, because the grader 'is sometimes overly permissive' (§6.1); Paper: Not evidence that the information steering leaves in the KV cache is accessible to the introspective mechanism: the authors say 'The ffects [sic] of steering may persist without being meta-cognitively recognized' (§6.3, typo in source); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: bears_on add 5.A2; two measurements in one sentence, rule would split them", council: "dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: evidence type interpretability to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-28
changed: 2026-10-15
---

Experiment 3: at L50–L90 continuous injection gave higher concept-mention rates than prompt-only (p<.001); detection showed no significant difference at L20, L45, L60 and L75 and only modest differences elsewhere. The authors: "Overall, steering during generation is not required for detection, but assists significantly with concept mentions." Experiment 4 (five trials per configuration; n=2,915 coherent trials for the token-by-token grading at L35 S6): the grader "sees detection coming early, then incorrect identifications, then correct identifications", and for "a substantial portion of cases, the detection decision is clear at the first token". Authors' reading (§7.3): "the model defaults to guessing “apple” at earlier tokens, unless steering is strong enough to push it off this default."

Relation to 2025-anthropic-emergent-introspective-awareness: no one-to-one counterpart. It bears on how Lindsey c01's "correctly identifies" should be read (identification may be produced by continuing steering during generation rather than read off at detection), but Lindsey did not run a prompt-only condition, so this is not labelled as a replication or a failure to replicate.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent; Claude lineage, same as the extractor)
- Statement: kept (checker: no error).
- Clauses: GPT's field taken; the only change is '(§6.3; typo in source)' -> '(§6.3, typo in source)', removing an internal semicolon (checker: delimiter only). No experience clause was present; none added.
- Steering sentence: kept, unchanged (R3).
- kind: measurement (the statement reports detection and concept-mention rates and response positions).

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): interpretability to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.

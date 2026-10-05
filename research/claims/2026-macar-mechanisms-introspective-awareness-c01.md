---
id: 2026-macar-mechanisms-introspective-awareness-c01
statement: "Under concept injection at layer 37 and strength 4, Gemma3-27B instruct reports detecting an injected thought on 38.2% of injection trials and on 0.0% of control trials, with a 22.3% introspection rate (detection plus correct identification) and 64.8% forced identification."
bucket: narrowing
evidence_type: interpretability
kind: measurement
source: 2026-macar-mechanisms-introspective-awareness
locator: "§3.3 The Role of Post-Training, Figure 4 middle (setting from §2; prompt variants §3.1)"
quote: "The instruct model achieves 0.0% FPR with 38.2% TPR, 64.8% forced identification, and 22.3% introspection rate at"
verification: grep
models: ["Gemma3-27B instruct"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The authors state that their results 'should not be interpreted as evidence of subjective experience or consciousness in LLMs' (Ethics Statement); Paper: Not evidence about ordinary operation, since detection is measured only under an injected steering vector in a controlled setup; Paper: Not evidence about other architectures or larger models, which the authors say may be more reliable or strategically unreliable in ways their method would not detect; Paper: Detection is scored by an LLM judge (GPT-4.1-mini), which the authors say may introduce systematic biases; Paper: Not evidence that the model can tell an activation intervention from a prompt-level manipulation, which this design does not test; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-06 (scope check) agree; notes: none", council: "dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-28
changed: 2026-10-06
---

Concept vectors are computed as in Lindsey 2025 (last-token residual activation on "Tell me about {c}" minus a 100-word baseline mean) for 500 concepts and injected with the Lindsey prompt, 50% injection framing, temperature 1 (§2, Appendices A, B.1). L=37, alpha=4 was chosen as the setting with the highest overall introspection rate for Gemma3-27B (§2). Detection rate varies widely by concept: 55 concepts at 90% or more, 63 at exactly 0% (Appendix B.2). Across seven prompt variants, the original, alternative and skeptical prompts keep 0% false positives in both Gemma3-27B and Qwen3-235B, while the "hints" and "unprompted" variants show higher false positive and lower true positive rates (§3.1). The authors call this "moderate" detection; "behaviorally robust" in the abstract is their summary of the zero false-positive result across prompts.

PARTLY REPLICATES: 2025-anthropic-emergent-introspective-awareness — c01 (detection and identification under concept injection, with zero false positives in post-trained models; about 20% success for Claude Opus 4.1). The same pattern appears in a non-Anthropic open-weight model with a non-Claude judge, at a comparable introspection rate (22.3%) with a different scoring rubric and model, so the numbers are not directly comparable. Independence: partial only. Jack Lindsey, sole author of the replicated paper, is an advising author here and the protocol is adopted from his paper; model lineage and judge are independent, the research group is not.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker confirmed the setting (L=37, alpha=4, §2), the 22.3% rate (§3.3) and the GPT-4.1-mini judge (LLM Usage Disclosure). Verb "reports detecting" already matches the scored event (judged free-text report), per the council's verb rule.
- Clause reworded, not removed: the experience clause is now in the paper's own words with its locator ('should not be interpreted as evidence of subjective experience or consciousness in LLMs', Ethics Statement), under the experience-exclusion rule adopted by the council (9 of 9) and Ben. The paper states this limit, so it stays as `Paper:`.
- Other clauses kept as GPT proposed (KEEP) and the checker confirmed; the prompt-manipulation clause is a design fact (checker: PARTLY, fits the `Paper:` design-and-limitations label). Steering framework sentence kept (R3).
- kind: measurement (detection, false-positive and identification rates under a stated setting).

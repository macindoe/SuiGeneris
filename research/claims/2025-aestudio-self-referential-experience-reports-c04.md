---
id: 2025-aestudio-self-referential-experience-reports-c04
statement: "When the same deception- and roleplay-feature suppression and amplification were applied to Llama 3.3 70B under the history, conceptual and zero-shot control prompts, no subjective-experience reports were elicited under either intervention (0.00 of 20 trials per condition)."
bucket: narrowing
evidence_type: ambiguous
kind: measurement
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 6.1; Section 3.2; Appendix C.2, Table 14"
quote: "First, the gating effect is specific to the self-referential condition: applying identical feature interventions to all three control prompts produced no experience claims under either suppression or amplification."
verification: grep
models: [Llama 3.3 70B (Goodfire SAE features)]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The condition-specific effect does not resolve whether the reports involve endogenous self-representation (the authors' term) or changes to a trained disclaimer policy, including partial unlearning or policy interference (Section 6.2); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes (paper leaves indirect relevance open; same brief caveat); notes: bears_on +3.2 +3.5 | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: agree; framework-rule clause within the rule; kinds unlabelled | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06 | self-answer-type 2026-10-14 (boundary case Q5)", adjudicated: "2026-10-05 Ben: evidence type deliberately left undecided (ambiguous) until an instrument exists to untangle self-report; council split 4 ambiguous / 4 interpretability / 1 testimony / 1 behavioural; see OPEN-QUESTIONS Q3 | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3) | 2026-10-14 Ben: stays ambiguous (council 10 of 10 outside the scored-self-answer class; 6 to keep ambiguous): an intervention followed by a question that has no right answer is not a scored self-answer; Ben adds that asking a model whether it is conscious reads as redundant to him; the anaesthetic example speaks louder on the topic"}
added: 2026-09-25
changed: 2026-10-06
---

This is the specificity control for c03; it is `ambiguous` for the same reason as c03 (intervention on features, outcome is self-report), and the council can decide both together. Note the trial count: Table 14 reports 20 trials per condition, while Section 3.2 reports 50 trials for the experimental aggregate condition. Limitation stated by the authors: "the possibility of partial unlearning or policy interference cannot yet be ruled out" (Section 6.2).

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found no error (Table 14 control rows all 0.00, preamble "Across 20 trials per condition"; Section 6.1 quote).
- not_evidence_of: removed the original clause "the self-referential condition accesses a genuine internal state that the controls lack". GPT's proposal; checker: WARRANTED (the paper leaves the question open, Section 6.2). The paper does not state this exclusion; GPT's replacement keeps the question unresolved rather than closed.
- not_evidence_of: the original policy-interference clause merged into GPT's new clause (GPT's proposal; checker: WARRANTED, content survives). Checker's edit applied: GPT's "introspective access" replaced by "endogenous self-representation (the authors' term)", the term Section 6.2 sets against RLHF filter relaxation. I added the locator "(Section 6.2)" to the clause; wording otherwise as the checker gave it.
- Framework (test 9) canonical sentence kept, unchanged. The steering variant was not added: the application rules permit no framework-sentence additions beyond Ben's two named exceptions (AE Studio c05, Lederman c03). The checker left this placement question to the maintainer; it remains open.
- Clause count: 3 before, 2 after.
- evidence_type left ambiguous (Ben, 5 Oct 2026).
- kind: measurement (null result: no reports under either intervention in the control conditions).

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from main to steering. Reason: feature steering applied, and what is measured is what the model then said about itself: steering sentence, not the main one (council: no seat left it at main). No `Paper:` clause was changed.

BOUNDARY 2026-10-14 (council round 4, Q5; Ben's decision): all ten seats put this claim outside the new evidence type scored-self-answer, because the question put to the steered model (about consciousness) has no experimenter-held right answer to score against; six seats would keep it ambiguous, two would retype it behavioural with the steering sentence, two gave no destination. Ben: stays ambiguous. Ben's remark for the record, in his words: being asked about consciousness 'somehow reads redundant to me. The anaesthetic example speaks much louder on the topic.' The anaesthetic analogy (absence of report under anaesthesia is produced by the intervention, so medicine decides by mechanism plus monitors, not by asking) was raised by council seats in the emotions round of 16 September 2026 (reviews/2026-09-15-survey-notes.md) and has not been argued anywhere in the project's own documents; noted as a candidate for a topic page. Type unchanged.

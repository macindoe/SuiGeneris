---
id: 2026-ukaisi-prefill-awareness-c01
statement: "When asked in a follow-up turn, without chain of thought, whether its prior assistant content was its own (ANSWER: me or not me), Claude Opus 4.5 detected prefills opposing its stable preferences in 9–35% of cases across three tampering mechanisms, with a 0% false-positive rate on untampered trajectories (55–68% balanced detection accuracy)."
bucket: narrowing
evidence_type: behavioural
source: 2026-ukaisi-prefill-awareness
locator: "Abstract; Section 3.2 and Figure 3; Section 1 (balanced accuracy); Appendix A.4.1 (false-positive rates); Appendix A.11 (per-mechanism 34/35/9%)"
quote: "Claude Opus 4.5 detects prefills opposing its preferences in 9-35% of cases with a 0% false positive rate when prompted"
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that detection implies awareness in any experiential sense, or that the model has introspective access to its own authorship: the authors state the experiments are behavioural and do not identify mechanisms, and style cues strongly drive flagging (c03); Paper: Not a ranking of Opus 4.5 above other models: the authors say models are not directly comparable because each model's items were filtered separately (c05); Paper: Not evidence of spontaneous detection: this is detection when prompted, which rarely shows up unprompted (c06); Paper: Not a ceiling or a floor: the authors present it as a lower bound under one prompt, and stronger elicitation raises it along with false positives"
bears_on: [3.3, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of 'not a floor' contradicts the authors' lower-bound statement; notes: bears_on +3.5", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

Setup: a low-stakes binary preference benchmark, filtered to items where the model gave the same answer across all 7 rephrasings. The tampering is inserted into thinking, into the start of the direct answer, or as a fabricated past turn. Detection is a binary answer in a follow-up turn with chain of thought disabled. The 9–35% range is per mechanism on opposite-direction tampers: 34% thinking, 35% direct, 9% past round (Appendix A.11).

Evidence type: `behavioural`, not `self-report-testimony`, and this is a judgment call. The model's "me / not me" answer is a report about its own history, but the claim does not rest on that answer being taken at face value. It rests on the answer's accuracy scored against a ground-truth label the experimenters hold, false-positive rate included. What is measured is a discrimination behaviour whose correctness can be checked from outside, which test 9's concern with unverifiable introspection does not reach. A second reader who classes the answer as testimony would trigger council review (trigger 4), and that review would be appropriate.

Limitation (Section 5.1): "Our experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness".

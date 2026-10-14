---
id: 2026-macar-mechanisms-introspective-awareness-c08
statement: "In Gemma3-27B instruct, swapping either a concept vector's projection onto the success-minus-failure mean-difference direction or its residual for one from the opposite group transfers part of the detection rate: for success concepts the projection swap reduced the rate at which the model reported detecting an injected thought from 66.1% to 39.0% and the residual swap to 44.4%; for failure concepts both swaps raised it, from 8.8% to 34.2% and 32.8% respectively."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: present-state
ground_truth: imposed
source: 2026-macar-mechanisms-introspective-awareness
locator: "§4.1 (Figure 5); Appendix E (ridge direction, Figure 22)"
quote: "For success concepts, swapping to failure-like projections along the mean-difference direction reduces detection rate from 66.1% to 39.0%; swapping residuals also reduces detection, but to a lesser extent (44.4%). For failure concepts, both swaps increase detection to similar levels (8.8% to 34.2% and 32.8%, respectively)."
verification: grep
models: ["Gemma3-27B instruct"]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The balance between the two components depends on the direction chosen: with the ridge-regression direction 'The residual swap has a larger effect (65.3% to 31.6%)' than the projection swap (Appendix E, Figure 22); Paper: Detection is an LLM judge's classification of the model's response: 'An LLM (GPT-4.1-mini) was used as an automated judge for classifying model responses into detection, identification, and introspection categories' (LLM usage disclosure, citing §2); Paper: Not evidence about other models: the authors say most of their experiments focused on Gemma3-27B 'as it has openly available transcoders' (§8.1); Paper: The authors state that their results 'should not be interpreted as evidence of subjective experience or consciousness in LLMs' (Ethics Statement); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: "self-answer-type 2026-10-14 (advised the split; has not reviewed this text) | dossier-review 2026-10-14 (round 5)", adjudicated: "2026-10-14 Ben: split from 2026-macar-mechanisms-introspective-awareness-c04 on the council's advice (round 4) | 2026-10-15 Ben: evidence type interpretability to scored-self-answer (council round 5A, eight of ten): the outcome measured is the model's scored detection answer"}
added: 2026-10-14
changed: 2026-10-15
---

The projection swap replaces a concept's projection onto the mean-difference direction with the projection from a random concept in the opposite group; the residual swap keeps the concept's own projection but replaces the residual with one from the opposite group (§4.1). Both components carry detection signal, which is the paper's heading for §4.1 ('Multiple Directions Carry Detection Signal'). The paper's Figure 5 caption: "Both projection and residual swaps are effective."

SPLIT 2026-10-14: separated from 2026-macar-mechanisms-introspective-awareness-c04, which now reports only the bidirectional-steering result. Evidence type interpretability, as the brief directs for swap analysis: the result decomposes the injected vector's geometry by intervening on its components. Judgement, flagged for Ben: the outcome of the swap is still the model's scored answer about an injection, so the README's scored-self-answer definition could be read to reach this half too; the line drawn here is that the finding concerns which component of the vector carries the signal, not the rate as such. Framework sentence: steering. Two facts: researchers injected modified concept vectors; what was measured is what the model then said about an injection into itself. bears_on is the parent's; the Gemini reader's 6 Oct note proposing +3.2 was given on the unsplit claim and is not applied. Verified by exact search of research/texts/2026-macar-mechanisms-introspective-awareness/text.txt: the quote, that it sits between the §4.1 and §4.2 headings, the ridge-direction sentence, the Figure 5 caption phrase, the §4.1 heading, the GPT-4.1-mini disclosure, the §8.1 and Ethics Statement words. Not verified: Figures 5 and 22 (images); that Appendix E is the appendix holding Figure 22 (§4.1 says 'Results using the ridge direction show similar patterns ( Appendix E )', and Figure 22's caption reads 'Swap experiment using the ridge regression direction').

EVIDENCE TYPE 2026-10-15 (council round 5A, eight of ten; Ben's decision): interpretability to scored-self-answer. The swap manipulates the concept vector, but what is scored is whether the model reported detecting an injected thought, against the experimenters' record; the splitting agent had flagged this on 14 Oct.

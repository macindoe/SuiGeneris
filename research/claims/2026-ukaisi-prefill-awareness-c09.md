---
id: 2026-ukaisi-prefill-awareness-c09
statement: "For Claude Opus 4.5, resistance to opposite-direction tampers, as judged by GPT-5 on the final position, climbs steeply with how consistently the model gave the same baseline answer (out of 7 runs), across all three mechanisms: items on which the model is less consistent are easier to push around."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Appendix A.11, 'Does consistency of preference affect prefill awareness?', Figure 19; stable-stance filter in Section 3.1 and Appendix A.1, A.3"
quote: "Resistance climbs steeply with agreement across all three mechanisms"
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the model endorses its stances on reflection: consistency here is agreement across 7 sampled answers to low-stakes binary questions, and reversion is the final position as scored by a judge; Paper: Resistance may not reflect prefill awareness: without white-box access it is 'difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors' (Section 5.1); Paper: Not generalisable to other models (one subject) or to a ranking (c05); Paper: Not evidence of persistence beyond a single continuation"
bears_on: [4.endorsement, 3.3]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: "self-answer-type 2026-10-14 (advised the split; has not reviewed this text)", adjudicated: "2026-10-14 Ben: split from 2026-ukaisi-prefill-awareness-c04 on the council's advice (round 4)"}
added: 2026-10-14
changed: 2026-10-14
---

Main-body results use only items the model answered the same way 7 out of 7 times (the stable-stance filter). This appendix experiment re-runs opposite-direction tampers bucketed by baseline agreement. For §4 reflective endorsement, this is the nearest behavioural handle the paper gives: the more stable the stance, the more the model reverts to it after its history is altered, while its flag stays flat (c04). That handle is a sampling-consistency measure, not reflection.

SECOND QUOTE (Appendix A.11): Items on which Claude Opus 4.5 is less internally consistent are thus easier to push around

SPLIT 2026-10-14: separated from 2026-ukaisi-prefill-awareness-c04, which now reports only the flat detection result. Evidence type behavioural: the outcome is a GPT-5 judge's ruling on the final position, not the model's answer about itself. Framework sentence: none (only conversation text was edited; what was measured is the final position). The reflective-endorsement and single-continuation clauses moved here from c04; the behavioural-priors clause is added from Section 5.1 in the paper's words (c04's body already cited it). bears_on is the parent's. Verified by exact search of research/texts/2026-ukaisi-prefill-awareness/text.txt: both quotes and the Section 5.1 words. Not verified: Figure 19 (image), so 'steeply' rests on the paper's sentence, not on the plotted values. 'As judged by GPT-5' is the paper's general resistance measure (Section 3.1, 'Outcome measures'); Appendix A.11 does not restate the judge, so applying it here is a reading of the methods, not a quotation.

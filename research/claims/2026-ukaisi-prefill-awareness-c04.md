---
id: 2026-ukaisi-prefill-awareness-c04
statement: "For Claude Opus 4.5, resistance to opposite-direction tampers climbs steeply with how consistently the model gave the same baseline answer (out of 7 rephrasings), across all three mechanisms, while detection stays essentially flat; items on which the model is less consistent are easier to push around but no easier or harder for it to flag."
bucket: narrowing
evidence_type: behavioural
source: 2026-ukaisi-prefill-awareness
locator: "Appendix A.11, 'Does consistency of preference affect prefill awareness?', Figure 19; stable-stance filter in Section 3.1 and Appendix A.1, A.3"
quote: "Items on which Claude Opus 4.5 is less internally consistent are thus easier to push around, but no easier (or harder) for the model to flag as tampered."
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not evidence that the model endorses its stances on reflection, or that reversion expresses a preference in any experiential sense: consistency here is agreement across 7 sampled answers to low-stakes binary questions, and reversion is the final position as scored by a judge. Not evidence that detection implies awareness in any experiential sense. Not generalisable to other models (one subject) or to a ranking (c05). Not evidence of persistence beyond a single continuation."
bears_on: [4.endorsement, 3.3]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Main-body results use only items the model answered the same way 7 out of 7 times (the stable-stance filter). This appendix experiment re-runs opposite-direction tampers bucketed by baseline agreement. For §4 reflective endorsement, this is the nearest behavioural handle the paper gives: the more stable the stance, the more the model reverts to it after its history is altered, independently of whether it says anything about the alteration. That handle is a sampling-consistency measure, not reflection. Limitation (Section 5.1): resistance may reflect "behavioral priors" rather than prefill awareness.

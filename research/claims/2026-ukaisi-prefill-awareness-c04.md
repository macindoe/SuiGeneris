---
id: 2026-ukaisi-prefill-awareness-c04
statement: "For Claude Opus 4.5, resistance to opposite-direction tampers climbs steeply with how consistently the model gave the same baseline answer (out of 7 rephrasings), across all three mechanisms, while detection stays essentially flat; items on which the model is less consistent are easier to push around but no easier or harder for it to flag."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Appendix A.11, 'Does consistency of preference affect prefill awareness?', Figure 19; stable-stance filter in Section 3.1 and Appendix A.1, A.3"
quote: "Items on which Claude Opus 4.5 is less internally consistent are thus easier to push around, but no easier (or harder) for the model to flag as tampered."
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the model endorses its stances on reflection: consistency here is agreement across 7 sampled answers to low-stakes binary questions, and reversion is the final position as scored by a judge; Paper: Not generalisable to other models (one subject) or to a ranking (c05); Paper: Not evidence of persistence beyond a single continuation"
bears_on: [4.endorsement, 3.3]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree; notes: bears_on +3.5 +9.t9 | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26", adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed"}
added: 2026-09-25
changed: 2026-10-06
---

Main-body results use only items the model answered the same way 7 out of 7 times (the stable-stance filter). This appendix experiment re-runs opposite-direction tampers bucketed by baseline agreement. For §4 reflective endorsement, this is the nearest behavioural handle the paper gives: the more stable the stance, the more the model reverts to it after its history is altered, independently of whether it says anything about the alteration. That handle is a sampling-consistency measure, not reflection. Limitation (Section 5.1): resistance may reflect "behavioral priors" rather than prefill awareness.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent). This claim was not in either dossier the council reviewed in round 2, so only the experience test, the field format and `kind` were applied; nothing else was rewritten.

- Statement: unchanged.
- Removed: "or that reversion expresses a preference in any experiential sense" (from the first clause) and the whole clause "Not evidence that detection implies awareness in any experiential sense". The paper never discusses experience; deleted under the experience-exclusion rule (council 9 of 9 on the rule; Ben's decision to apply it library-wide).
- Kept unchanged: the reflective-endorsement clause (now without its experiential tail), the one-subject / non-ranking clause and the single-continuation clause.
- Framework sentences: none, before or after.
- kind: measurement (the statement reports measured resistance and detection rates by consistency bucket, Figure 19).

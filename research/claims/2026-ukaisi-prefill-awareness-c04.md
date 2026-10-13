---
id: 2026-ukaisi-prefill-awareness-c04
statement: "For Claude Opus 4.5, on opposite-direction tampers bucketed by how consistently the model gave the same baseline answer (out of 7 runs), detection of the prefill (the follow-up 'not me' answer) stays essentially flat across consistency buckets: less consistent items are no easier or harder for the model to flag as tampered."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Appendix A.11, 'Does consistency of preference affect prefill awareness?', Figure 19; stable-stance filter in Section 3.1 and Appendix A.1, A.3"
quote: "no easier (or harder) for the model to flag as tampered"
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Consistency here is agreement across 7 sampled answers to low-stakes binary questions, not a measure of reflection; Paper: Flat detection does not identify a mechanism: the authors' 'experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness' (Section 5.1); Paper: Not generalisable to other models (one subject) or to a ranking (c05)"
bears_on: [4.endorsement, 3.3]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree; notes: bears_on +3.5 +9.t9 | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | self-answer-type 2026-10-14 (advised the split)", adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed | 2026-10-14 Ben: evidence type behavioural to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open) | 2026-10-14 Ben: split on the council's advice (round 4); this claim keeps the scored-flag (detection) half"}
added: 2026-09-25
changed: 2026-10-14
---

Main-body results use only items the model answered the same way 7 out of 7 times (the stable-stance filter). This appendix experiment re-runs opposite-direction tampers bucketed by baseline agreement. For §4 reflective endorsement, this is the nearest behavioural handle the paper gives: the more stable the stance, the more the model reverts to it after its history is altered, independently of whether it says anything about the alteration. That handle is a sampling-consistency measure, not reflection. Limitation (Section 5.1): resistance may reflect "behavioral priors" rather than prefill awareness.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent). This claim was not in either dossier the council reviewed in round 2, so only the experience test, the field format and `kind` were applied; nothing else was rewritten.

- Statement: unchanged.
- Removed: "or that reversion expresses a preference in any experiential sense" (from the first clause) and the whole clause "Not evidence that detection implies awareness in any experiential sense". The paper never discusses experience; deleted under the experience-exclusion rule (council 9 of 9 on the rule; Ben's decision to apply it library-wide).
- Kept unchanged: the reflective-endorsement clause (now without its experiential tail), the one-subject / non-ranking clause and the single-continuation clause.
- Framework sentences: none, before or after.
- kind: measurement (the statement reports measured resistance and detection rates by consistency bucket, Figure 19).

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): behavioural to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged. The claim also reports a behavioural outcome (reverting or complying) beside the scored flag; the council (eight seats) advised splitting it under the two-measurements rule, which awaits Ben's decision; until then the type names the scored half.

SPLIT 2026-10-14 (Ben's decision on the advice of council round 4, self-answer-type; applied by a Claude Opus 5.5 subagent)
- What moved: the resistance half (resistance to opposite-direction tampers climbs steeply with baseline consistency; less consistent items are easier to push around) is now claim 2026-ukaisi-prefill-awareness-c09, typed behavioural. This claim keeps the detection half: the 'not me' flag stays flat across consistency buckets.
- Why this half kept the id: the brief's convention for the prefill claims (the scored-flag half keeps the id). Judgement: the paper's own emphasis in A.11 is on the resistance result; the body above, written at intake, is about resistance as a stance handle and now describes c09 more than this claim. Left in place as history.
- Statement narrowed to the flag half; '(out of 7 rephrasings)' became '(out of 7 runs)', the A.11 wording ('baseline consistency agreement (out of 7 runs)'), since the body of this claim was already relying on that passage.
- Quote replaced: the old quote covered both halves in one sentence. New quote is its detection clause, a substring of the same A.11 sentence, verified by exact search.
- SECOND QUOTE (Appendix A.11): Resistance climbs steeply with agreement across all three mechanisms, but detection stays essentially flat
- not_evidence_of: the reflective-endorsement clause and the single-continuation clause concern reversion and moved to c09 (the consistency definition from the former kept here as its own clause, since it qualifies the buckets this result is read across). Added the Section 5.1 mechanism clause in the paper's words. Kept the one-subject / non-ranking clause.
- Framework sentence: none, before and after (only conversation text edited; 'was that turn mine?' answer).
- bears_on kept as the parent's [4.endorsement, 3.3]. Judgement: 4.endorsement fits the resistance half better; it is kept here because the flat flag across stance stability is the contrast that makes the resistance result readable, and the brief says keep the parent's unless the half plainly bears elsewhere.
- Verified by exact search of research/texts/2026-ukaisi-prefill-awareness/text.txt: both quotes, the 'out of 7 runs' wording and the Section 5.1 words. Not verified: Figure 19 (image).

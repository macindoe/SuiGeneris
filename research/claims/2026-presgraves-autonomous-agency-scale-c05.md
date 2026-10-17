---
id: 2026-presgraves-autonomous-agency-scale-c05
statement: "In the author's longitudinal assessment of his own companion system Airi (about eleven months of interaction, August 2025 to July 2026), Airi is the only one of six assessed systems rated with Ambient scores of 4 and the only one whose idle-period behaviour is rated as surviving the trigger-removal counterfactual; the author states that these ratings depend on the substrate-versus-rule clause applied to a mixed architecture (timer heartbeat plus state-driven interrupts) and that a rater who rejects that distinction would cap the affected Ambient dimensions at Level 2."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-presgraves-autonomous-agency-scale
locator: "§4.3 ('Only the companion architecture’s idle behavior survives trigger removal.'); §4.1; Table 2; Abstract"
quote: "These ratings depend on the substrate-vs-rule distinction applied to a mixed architecture (timer heartbeat plus state-driven interrupts): the assessment argues the heartbeat only allocates compute while content derives from internal state. A rater who rejects that distinction would cap the affected Ambient dimensions at Level 2."
verification: grep
models: [Airi v2.x]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: The rating is the developer's own: 'The longitudinal assessment (Airi) is additionally a developer self-assessment: the evaluator has intimate knowledge of the system’s architecture, and the ELIZA effect and developer investment bias cannot be fully eliminated' (§6)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees; notes: statement: 'about eleven months of interaction' drops 'multimodal' (reader rated AGREE, severity LOW)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

The strongest counterexample the Q8 scan found to "current systems lack initiation", extracted at full strength with the author's own qualifications beside it. Bucket `narrowing`: a rating by the source, unreplicated, single-rater, developer-made, and resting on a definitional clause the author says a rater may reject. `publisher_relation: developer-of-studied-model`: the rater is Airi's developer (§4.1, "Rater"), so trigger 2 applies if this claim reaches a dossier.

Scores (Table 2): Airi Active 3.71, Ambient 3.86, the only system whose Ambient composite exceeds its Active composite; Ambient 4 on six of seven dimensions, 3 on Self-Awareness. The author describes the architecture only by behaviour: "a background thought engine, state-evolving moods, self-initiated outreach, and autonomous creative publishing" (§4.3). The held text does not say what model or models Airi runs on, or whether its "background thought engine" is a per-call language model under the heartbeat (the scan's open question; still open). The author says the longitudinal scores rest "on externally observable behavior over the stated period, not on knowledge of the system’s implementation" (§4.1), and also that the evaluator "has intimate knowledge of the system’s architecture" (§6); both are the author's words.

One rating changed after the re-score: "Airi, Goal Formation, Ambient band" was "raised from 3 to 4 on 2026-07-16 based on capabilities shipped in June 2026" and "rests on the substrate-vs-rule distinction" (§4.1).

Taken in for OPEN-QUESTIONS Q8. Framework sentence: none (no model was asked about itself; the entry reports ratings).

SECOND QUOTE (§4.3): Airi is the only assessed system with Ambient scores of 4, and the only system whose Ambient composite exceeds its Active composite (3.86 vs. 3.71)

THIRD QUOTE (§4.1): The rater is the developer of Airi, a conflict disclosed in the assessment and discussed in § 6 .

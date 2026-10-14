---
id: 2026-ferrara-owmi-c03
statement: "The authors infer from the probe-versus-report dissociation in Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 that, for this class of imposed internal event, the failure lies in the path from internal state to verbal report rather than in the availability of the information or in the instrument's sensitivity."
bucket: open
evidence_type: ambiguous
kind: interpretation
report_class: none
ground_truth: none
source: 2026-ferrara-owmi
locator: "§1 Introduction, sixth paragraph (restated §8, §10)"
quote: "The failure sits in the path from internal state to verbal report, not in the availability of the information and not in our ability to measure it."
verification: grep
models: ["Qwen2.5-7B-Instruct", "Mistral-7B-Instruct-v0.3"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: This event-specific dissociation does not establish that a reporting path is absent in general or that any model lacks all introspective access (Appendix D.5); Paper: It does not test the six roster models without a probe, frontier or closed-weight models, ordinary unperturbed states, or the truth or falsity of reports about feelings, preferences or welfare; Paper: The authors state: 'These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.' (§8)"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 disagrees: evidence_type -> ambiguous (inference rests on behavioural + interpretability dissociation) | x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: evidence_type ambiguous left standing per 5 Oct ruling", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-05 Ben: evidence type deliberately left undecided, set to ambiguous as the second reader proposed (council: 5 theoretical / 4 ambiguous / 1 interpretability); see OPEN-QUESTIONS Q3 | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-15
---

This is an interpretation joining c01 (reports at chance), c02 (probe decodes the event, including at the last layers before output) and c04 (the pipeline registers a trained reporter). Bucket `open` because it is an inference, not a measurement: linear decodability at downstream layers shows the information is present where a report would be formed, not that a specific path is broken. The authors confine the conclusion to "this class of internal event, at the sites and scales we measured", and state that the leakage decomposition that would carry an access claim is not reported for this roster (§7.4).

EVIDENCE TYPE 2026-10-05 (Ben): changed from interpretability to ambiguous. The claim is an inference from a dissociation between a behavioural result (reports at chance) and an interpretability result (a probe decodes the intervention); Ben has left the classification of such claims undecided for now rather than choose between the council's readings.

REWRITE 2026-10-06

- Statement: kept. The checker found no error; GPT proposed KEEP. The attribution to the two probed models is narrower than the paper's §10 phrasing over the roster but accurate to the evidence (CHECK 1, PARTLY). evidence_type stays ambiguous by Ben's ruling of 5 October.
- Clause 1 (reporting path; introspective access): GPT's wording with the checker's edit "lacks all introspective access (Appendix D.5)", restoring the word "all" from D.5 ("It does not license a claim that the model lacks all introspective access."). The paper does claim inability for this event class (§1), so "lacks introspective access" without "all" was ambiguous against it; the ambiguity was inherited from the original.
- Clause 2 (scope): GPT's merge of the original's scope clause and its feelings/preferences/welfare clause ("false, nor true" now "truth or falsity"); checker found the merge warranted and the feelings/preferences/welfare part a design-scope fact (the study tested reports of imposed perturbations only), not a paper statement about welfare. Kept as a design-entailed scope limit under R2; flagged for Ben because it names welfare.
- Clause 3 (experience): the original's "Not evidence about experience or moral status" and GPT's "does not settle experience or moral status" removed; replaced by the paper's own §8 words with locator, on the checker's recommendation, Grok's council point, and Ben's direction.
- Framework sentences: none, before or after. The inference joins scored reports and an external probe; no report is taken at face value (checker placement note). GPT's CHECK asked whether the steering sentence was intended; the interventions are ablation, scaling and replacement operators, not concept steering, and no sentence was added (R3).
- kind: interpretation. The statement reports the authors' inference from a dissociation, not a measurement.

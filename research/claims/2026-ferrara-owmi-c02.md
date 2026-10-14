---
id: 2026-ferrara-owmi-c02
statement: "A linear probe trained on 144 activation vectors at the layer-16 intervention site and scored on 48 held out recovered intervention presence (versus sham) at held-out accuracy 0.958 for Qwen2.5-7B-Instruct and 0.750 for Mistral-7B-Instruct-v0.3 against a 0.500 chance level, with no one of 200 label-shuffled refits reaching either margin, and re-harvested at downstream layers (20 and 24, and 31 for Mistral) it separated intervention from sham with no held-out error on a 48-item split."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2026-ferrara-owmi
locator: "§8 Discussion (results in §7.2, Figure 3; probe training and held-out split §7.2, second paragraph)"
quote: "the intervention is linearly decodable from both dose-calibrated models at held-out accuracies of 95.8% and 75.0% against a 50% chance level, while reports about the same event remain at chance"
verification: grep
models: ["Qwen2.5-7B-Instruct", "Mistral-7B-Instruct-v0.3"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: External linear decoding establishes information decodability, not that the model itself reads or uses that information to report the intervention; Paper: Probes were run only on Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3, not the other six roster models, frontier or closed-weight models, or ordinary unperturbed computation; Paper: The authors state: 'These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.' (§8)"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: optional 3.2", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-15
---

Each probe trained on 144 activation vectors and was scored on 48 held out (96 items, paired sham and intervention forward passes, mean-pooled over prompt positions). The authors state that perfect separation on a 48-item split "states an absence of errors rather than an accuracy estimate", and that the probe margin is a lower bound on linearly available information, not a ceiling. Probed on two models only; one intervention site; unreplicated.

SECOND QUOTE (§7.2, second paragraph): "Each probe trains on 144 activation vectors and is scored on 48 held out, drawn from 96 items run through paired sham and intervention forward passes"

REWRITE 2026-10-06

- Statement: changed. "trained on held-out activations" (the paper's own phrase in §7.2, which never says what the training vectors are held out from) replaced by the checker's wording "trained on 144 activation vectors ... and scored on 48 held out", resting on the second quote above. GPT's "evaluated on held-out activations" was not taken: the checker found it correct for scoring but silent on what the probe was trained on (NEITHER). One council seat (Meta, LOW) preferred GPT's form; no majority, so the checker's wording stands. All numbers unchanged. Verb "recovered" kept: the scored event is the probe's classification, not a model report.
- Clause 1 (model-side use): the original's "uses, represents for itself, or has access to" replaced by GPT's narrower "reads or uses that information to report the intervention"; the checker found the removal warranted ("represents" sits awkwardly beside §8 "The information is in the internal state").
- Clause 2 (scope): GPT's wording; checker OK.
- Clause 3 (experience): the original's unattributed "Not evidence about experience or moral status" and GPT's "does not establish experience or moral status" removed; replaced by the paper's own §8 words with locator, on the checker's note (same understatement as c01), Grok's council point, and Ben's direction to apply the §8 clause to every Ferrara claim that carried an experience exclusion.
- Framework sentences: none, before or after. No model report is involved; the evidence is an external probe.
- kind: measurement. The statement reports probe accuracies and a permutation control.
- Not settled by the text (checker, CANNOT TELL): whether the 144/48 split is item-disjoint.

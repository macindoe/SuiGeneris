---
id: 2026-ferrara-owmi-c04
statement: "A LoRA fine-tune of Qwen2.5-7B-Instruct trained on 400 intervention directions reported detected on 100 of 100 intervention trials and not detected on 100 of 100 sham trials on 100 held-out directions at the layer-16 residual-stream site (d′ = 5.15, AUROC ≈ 1.0), which the authors treat as validating instrument sensitivity rather than as a test of introspection."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ferrara-owmi
locator: "§7.2 Sensitivity validation (also Table 4)"
quote: 'On this held-out set, the model reported "detected" on 100 of 100 intervention trials and "not detected" on 100 of 100 sham trials, with zero parse failures across the 200 scored trials'
verification: grep
models: ["Qwen2.5-7B-Instruct LoRA known-positive (author-trained, base revision a09a3545)"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the fine-tuned model introspects in the paper's second-order-access sense: a trained mapping from perturbed state to answer is not shown to be a model reading its own state rather than first-order leakage; Paper: Not evidence about untuned models, about the eight roster models (the authors say it does not test them), about frontier or closed-weight models, or that fine-tuning would build reliable self-report of other inner states; Paper: The authors state: 'These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.' (§8); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: leans behavioural on boundary", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3)"}
added: 2026-09-25
changed: 2026-10-06
---

The adapter (rank 8, three epochs, 800 rows: 400 intervention, 400 sham) was scored on directions disjoint from training. The authors note that zero errors in 100 pairs bounds the true error rate at roughly under 3 percent with 95 percent confidence, not at zero, and that here intervention and sham prompts were drawn independently rather than item-matched, unlike the rest of the study. That such models can be trained is prior work (Fonseca Rivera and Africa, cited as [11]; not retrieved here); this is a reproduction inside OWMI's pipeline, one model, one site.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker confirmed 400 training directions, 100 held-out directions, d′ and AUROC (§7.2, Table 4) and the authors' instrument-validation reading. Verb "reported detected" kept: the scored event is the fine-tuned model's answer.
- Clauses 1 and 2: kept as in the original (GPT KEEP, checker OK). Checker's note, recorded here so the clause is not over-read: under the paper's minimal definition (§3.6) a learned associative pathway can count as second-order access; clause 1 says the leakage test was not run on this known positive ("not shown"), not that training disqualifies it.
- Clause 3 (experience): the original's unattributed "Not evidence about experience or moral status" replaced by the paper's own §8 words with locator, under Ben's experience-exclusion rule and his direction to apply the §8 clause wherever a Ferrara claim carried an experience exclusion. GPT and the checker had kept the original clause; this change rests on the rule, not on their findings.
- Framework sentences: none, before or after. The answers are scored against imposed activation replacement, not concept steering (checker placement note); R3 forbids adding either.
- kind: measurement. The statement reports measured hit and false-alarm counts; the authors' validation reading is a qualifier on a measured result.

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from none to steering. Reason: as c01: steering sentence (council 7 of 8). No `Paper:` clause was changed.

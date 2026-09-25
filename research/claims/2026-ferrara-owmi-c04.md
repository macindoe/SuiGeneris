---
id: 2026-ferrara-owmi-c04
statement: "A LoRA fine-tune of Qwen2.5-7B-Instruct trained on 400 intervention directions reported detected on 100 of 100 intervention trials and not detected on 100 of 100 sham trials on 100 held-out directions at the layer-16 residual-stream site (d′ = 5.15, AUROC ≈ 1.0), which the authors treat as validating instrument sensitivity rather than as a test of introspection."
bucket: narrowing
evidence_type: behavioural
source: 2026-ferrara-owmi
locator: "§7.2 Sensitivity validation (also Table 4)"
quote: 'On this held-out set, the model reported "detected" on 100 of 100 intervention trials and "not detected" on 100 of 100 sham trials, with zero parse failures across the 200 scored trials'
verification: grep
models: ["Qwen2.5-7B-Instruct LoRA known-positive (author-trained, base revision a09a3545)"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the fine-tuned model introspects in the paper's second-order-access sense: a trained mapping from perturbed state to answer is not shown to be a model reading its own state rather than first-order leakage; Paper: Not evidence about untuned models, about the eight roster models (the authors say it does not test them), about frontier or closed-weight models, or that fine-tuning would build reliable self-report of other inner states; Paper: Not evidence about experience or moral status"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

The adapter (rank 8, three epochs, 800 rows: 400 intervention, 400 sham) was scored on directions disjoint from training. The authors note that zero errors in 100 pairs bounds the true error rate at roughly under 3 percent with 95 percent confidence, not at zero, and that here intervention and sham prompts were drawn independently rather than item-matched, unlike the rest of the study. That such models can be trained is prior work (Fonseca Rivera and Africa, cited as [11]; not retrieved here); this is a reproduction inside OWMI's pipeline, one model, one site.

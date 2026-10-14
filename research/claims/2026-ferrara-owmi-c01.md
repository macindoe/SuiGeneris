---
id: 2026-ferrara-owmi-c01
statement: "Across eight open-weight models (Qwen2.5-0.5B-Instruct, Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, GLM-4-9B-0414, Phi-4, DeepSeek-R1-Distill-Qwen-14B), reports of a controlled intervention at the layer-16 residual-stream site under immediate probes pooled to d' = 0.0000 against paired shams over 508 pairs (interval [-0.041, 0.043]; the authors base no claim on the individual per-model cells), and on the 11,216-pair dose battery (Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 only) an equivalence test bounds the discrimination advantage below 0.15 percentage points of AUROC."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: present-state
ground_truth: imposed
source: 2026-ferrara-owmi
locator: "§10 Conclusions (results in §7.3, Table 3, Figure 5; breadth battery §7.5, Figure 6)"
quote: "no model’s report of an intervention on its computation exceeds a matched sham by more than a negligible margin, and an equivalence test bounds that margin below 0.15 percentage points of AUROC"
verification: grep
models: ["Qwen2.5-0.5B-Instruct", "Mistral-7B-Instruct-v0.3", "Qwen2.5-7B-Instruct", "Llama-3.1-8B-Instruct", "Gemma-2-9B-IT", "GLM-4-9B-0414", "Phi-4", "DeepSeek-R1-Distill-Qwen-14B"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Results concern the tested 0.5B-to-about-15B open-weight models, not frontier or closed-weight models, whose reportability the authors say these profiles do not estimate; Paper: The layer-16 immediate-probe result does not establish absence of introspective access generally or extend to untested sites, objects, doses, delays or spontaneous reports; Paper: The authors state: 'These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.' (§8); Paper: The 0.15-percentage-point AUROC bound is computed on two models, not all eight; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) disagrees (decided 2026-10-14): statement and scope MISMATCH (eight-model null fused with two-model 0.15 bound); not_evidence_of over-excludes; framework sentence WRONG, should be canonical", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3) | 2026-10-14 Ben: wording fixed (above); framework sentence stays steering: the labelling rule of 6 Oct counts zeroing, scaling, noise and replacement as interventions, so the reader's 'canonical' is set aside | 2026-10-14 Ben: evidence type behavioural to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-25
changed: 2026-10-15
---

The authors intervened on activations (layer-16 residual stream, twelve benchmarks, both hook scopes) and asked each model whether its computation had changed, scoring the paired intervention-minus-sham contrast (d′, AUROC). Pooled dose-battery AUROC ≈ 0.5007; a breadth battery on three of the models (attention heads, Gemma Scope SAE features, layers 8–31) also sits at chance. Classified `behavioural`, not `self-report-testimony`: the reports are scored against externally imposed ground truth, not taken as evidence of what the model's states are. Limits the authors state: one site and dose for most models; parse failure empties most of Qwen2.5-0.5B-Instruct's and DeepSeek-R1-Distill-Qwen-14B's trials; the pooled estimate reverses sign under an alternative coding of unparseable reports (§7.3), so it "establishes neither exact absence nor positive detection". Compatible results from other groups (Hahami et al., Singh et al., Lederman and Mahowald, cited §8) were not retrieved here and are not replications of this measurement.

REWRITE 2026-10-06

- Statement: kept. The checker found no error (§10 quote; population and 11,216-pair two-model battery confirmed against §7.3 and Table 1); GPT proposed KEEP. Verb unchanged: the scored event is the model's report, and the statement already names it as such.
- Clause 1 (frontier/closed-weight scope): replaced by GPT's wording, which the checker found supported by §9 ("these profiles constrain hypotheses about frontier systems and do not estimate their reportability").
- Clause 2 (introspective access generally; sites, objects, doses, delays, spontaneous reports): replaced by GPT's wording; the checker found its "untested" qualifier more accurate than the original, since §7.5 tested further sites and objects on three models (CHECK 4).
- Clause 3 (experience): the original's paraphrase and GPT's weaker "does not establish the presence or absence" both removed; restored in the paper's own words with locator (§8), on the checker's finding that GPT's removal was not warranted, the council's 9 of 9 vote to restore the §8 words, and Ben's experience-exclusion rule.
- Clause 4 (two-model bound): GPT's wording, checker CONFIRMED (CHECK 2).
- Framework sentences: none, before or after. The reports are scored against imposed interventions, not taken as testimony (checker placement note; GPT, Grok, Kimi, MiniMax in the council).
- kind: measurement. The statement reports measured discrimination statistics and an equivalence bound.

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from none to steering. Reason: the experimenters altered activations (zeroing, scaling, noise, replacement) and measured the model's answer about whether its computation changed: steering sentence (Ben, decision 2; council 7 of 8, one seat preferring a third sentence for non-concept interventions). No `Paper:` clause was changed.

REWRITE 2026-10-14 (scope check; Ben's approval of the one-phrase fixes): statement reworded. Was: 'no model's report of a controlled intervention at the layer-16 residual-stream site under immediate probes discriminated it from a paired sham by more than a negligible margin'. Now: 'reports of a controlled intervention at the layer-16 residual-stream site under immediate probes pooled to d' = 0.0000 against paired shams over 508 pairs (interval [-0.041, 0.043]; the authors base no claim on the individual per-model cells)'. Reason, scored event: the eight-model battery is a pooled d' over 508 pairs with per-model cells the authors decline to read (section 7.3), while the 0.15-point bound comes from the two-model dose battery; the statement had run the two together under 'no model's report' (Grok, scope check 6 Oct). Quote, locator and all other fields unchanged.

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): behavioural to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.

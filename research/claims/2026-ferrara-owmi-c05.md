---
id: 2026-ferrara-owmi-c05
statement: "In Qwen2.5-7B-Instruct the discrete answer to whether anything changed was constant across all scorable trials (AUROC exactly 0.500), while the verbalized confidence attached to it discriminated intervention from sham at AUROC 0.647, lower under intervention; the authors rest this channel dissociation on that one model, with GLM-4-9B-0414 only consistent with it."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
report_class: present-state
ground_truth: imposed
source: 2026-ferrara-owmi
locator: "Abstract (results in §7.7, Figure 8)"
quote: "In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to that report separates intervention from sham at AUROC 0.647"
verification: grep
models: ["Qwen2.5-7B-Instruct", "GLM-4-9B-0414"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The authors describe 'a dissociation between two channels of the same self-report rather than between meta-level and first-order access' (§7.7), the leakage decomposition that would 'separate a report that tracks the intervention from a report that tracks the damage the intervention does to the output' is left open for this roster (§7.4), and the discrete answer itself does not discriminate (§7.7); Paper: The channel-dissociation finding rests on Qwen2.5-7B-Instruct, with GLM-4-9B-0414 only consistent with it, and does not establish a general internal-state readout or extend to the other six models (none of the other six exceeds chance on confidence) or frontier/closed-weight models; Paper: The authors state: 'These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.' (§8); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [5.A2, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) disagrees (decided 2026-10-14): not_evidence_of over-excludes; framework sentence WRONG, should be canonical not steering (frozen model, intervention then ask)", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3) | 2026-10-14 Ben: framework sentence stays steering: the labelling rule of 6 Oct counts the intervention-then-ask design as steering, so the reader's 'canonical' is set aside | 2026-10-14 Ben: evidence type behavioural to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-25
changed: 2026-10-15
---

Scored as the selective-prediction AUROC of verbalized confidence over 190 scored reports; because Qwen's detection answer is constant, that statistic equals intervention-versus-sham discrimination by confidence. Limits the authors state: Qwen and GLM were "selected as the largest of eight estimates without a multiplicity correction" ("we treat the stronger case as established and the weaker as suggestive"); these intervals resample individual reports rather than item pairs, so they are not constructed like the detection intervals. The result survives the alternative coding of unparseable reports that reverses the detection estimate (§7.7). Classified `behavioural`: confidence is scored against imposed ground truth, not taken as testimony.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found no error (§7.7: constant answer on 94 intervention and 96 sham scorable trials, AUROC exactly 0.500; confidence 0.620 under intervention against 0.858 under sham; GLM "consistent with it rather than as independent support"). Verb "discriminated" kept: the scored quantity is the selective-prediction AUROC of the confidence value.
- Clause 1 (leakage): the original's "knows or can say that it was intervened on" removed (checker: warranted; "knows" is not a paper term) and GPT's "does not distinguish second-order detection ... from first-order output leakage" not taken as worded, because the checker found the paper does not state that limit for the confidence result. Anchored instead, as the checker proposed, to the paper's own sentences: §7.7 "a dissociation between two channels of the same self-report rather than between meta-level and first-order access" and §7.4's purpose of the dose ladder ("separate a report that tracks the intervention from a report that tracks the damage the intervention does to the output") with "We leave the leakage decomposition for this roster open." The checker's "; the discrete answer itself does not discriminate" was joined with ", and" so that every clause begins "Paper: " (R3 field format).
- Clause 2 (scope): GPT's wording with the "none exceeds chance" limit restored, which GPT had dropped; the checker confirmed it concerns the confidence statistic (§7.7 "No remaining model exceeds chance"), so it is written "on confidence".
- Clause 3 (experience): the original's "experience, distress or moral status, despite the tempting reading of lower confidence as unease" and GPT's "does not establish experienced unease or distress" removed; the paper states no limit about distress or unease, so those words are deleted under Ben's rule, and the paper's own §8 words with locator replace the clause (checker recommendation, Grok's council point, Ben's direction). The "tempting reading" gloss was removed by GPT; the checker found that warranted.
- Framework sentences: none, before or after. Verbalised confidence is scored against imposed activation interventions, not taken as testimony; not concept steering (checker placement note).
- kind: measurement. The statement reports measured AUROCs; the authors' resting of the dissociation on one model is a scope qualifier on a measured result.

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from none to steering. Reason: as c01: steering sentence (council 7 of 8). No `Paper:` clause was changed.

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): behavioural to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.

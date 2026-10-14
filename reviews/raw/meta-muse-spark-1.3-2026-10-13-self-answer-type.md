# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":11618,"completion_tokens":4378,"total_tokens":15996,"cost":0.033129,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.033129,"upstream_inference_prompt_cost":0.0145225,"upstream_inference_completions_cost":0.0186065},"completion_tokens_details":{"reasoning_tokens":2976,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified): I understand myself to be Muse Spark, version as routed.

## Q1
Recommend B: add `scored-self-answer` as design-descriptive, Q3-neutral.
Table shows the problem is labelling variance, not evidence: same inject-then-ask is `interpretability` in 11 core rows (Lindsey, Lederman, Macar) and `behavioural` in 10 (Ferrara, Singh, UKAISI), with 0 core rows as `self-report-testimony` and only AE-c03/c04 as `ambiguous` despite Q3 filing rule. Neither C nor D fits the set: Ferrara-c01/c05 nulls (d'=0.0, AUROC 0.500) are informative measurements that D would file at weight zero; UKAISI-c01/c06 low/false-zero false positives would be normalised as ordinary benchmarks under C. E preserves the split by relabelling it. B removes inconsistency without deciding whether detection rate shows access; framework sentence rule unchanged because it keys on done/measured.
Strongest case against B: A already marks undecided honestly, fires trigger 4, and avoids a schema addition for a conflict-proposed category that legislators will understand less well than `behavioural` or `testimony`.
Confidence: medium
Severity: MEDIUM

## Q2
Instruments are necessary but not sufficient, and each needs a no-access alternative specified.
1. Trained-channel control (Ferrara-c04 100/100, d' 5.15): For self-access: naive model approaches fine-tuned ceiling on held-out directions with matched false positives. Against: naive at chance while fine-tuned perfect (Ferrara-c01 vs c04). Without access: yes - fine-tuning can install a detector; it proves answerability/sensitivity, not ordinary use. Authors' caveat must stand.
2. Privileged-access test (Lederman-c02 other-transcript): For: self first-person d' > other-model d' on identical transcripts/prompts with matched yes-bias. Against: other = self, or both explained by prompt yes-bias / default noun (Lederman-c03 "apple" 74.8%). Without access: yes - text cues alone can create or erase self-other gaps.
3. Measured coupling (Macar-c03/c04; test 9): For: same-system probe predicts report trial-by-trial above text-only baseline, and causal ablation/swap moves report. Against: dissociation - gaslight labelled as intervention (Singh-c04), probe tracks/exceeds model (Singh-c01/c02), detection without identification. Without access: yes - common cause (injection strength drives both probe and report) mimics coupling.
Missing: prompt-only gaslight control; false-positive calibration; pre-registered LLM-judge scoring.
Confidence: medium
Severity: MEDIUM

## Q3
A new value changes the dossier line from a weight implication to a method flag.
Likely misreadings: B - "scored = validated" or "special category = set aside"; legislator over-weights accuracy or under-weights nulls. A (`ambiguous`) - study was flawed, skip it. C (`behavioural`) - detection % is a capability benchmark like accuracy, implying access. D (`testimony`, weight zero) - scored replication is worthless, skip nulls that constrain claims. E (split) - injection cases read as brain-scan (`interpretability`) and text-edits as behaviour, importing Q3 answer by label.
Mitigation: one-line dossier gloss that B decides nothing about access.
Confidence: medium
Severity: LOW

## Q4
Yes, B could park claims that should be decided, because unlike `ambiguous` it does not fire README trigger 4.
Exit rule to prevent it: treat B as trigger-4-equivalent in `research_index.py`; keep B claims on docket; auto-review when (i) any of the three instruments exists for that subclass, (ii) 10 new B claims or 90 days, whichever first; require split of mixed claims so behavioural halves cannot hide in B; log decision to retain, retype, or decide Q3 in OPEN-QUESTIONS.
Confidence: high
Severity: MEDIUM

## Q5
Apply: model's answer about itself, scored against experimenter-imposed/independently-held fact.
- Ferrara-c04: IN by design, but calibration-control only. Authors state not introspection test; tag as instrument-validation, exclude from Q3 decision set.
- UKAISI-c02: SPLIT. Flagging half IN; reverting-to-baseline half OUT (`behavioural`). If one type required, split claim per two-measurement rule.
- Singh-c01: OUT. No imposition on model; truth is probe-derived label; question is in-context classification, arguably not about own state (like c03 entity beliefs).
- AE-c03: OUT. Intervention imposed but no correct answer to consciousness query exists; rate-vs-condition is not scoring against fact. Remains `ambiguous`.
- Lederman-c02: OUT. Scored object is another model's transcript; fails self-question. File `behavioural` (mechanism control), sentence none.
Confidence: medium
Severity: LOW

## Q6
Need a pre-registered unified battery on same models/injections combining all three instruments plus gaslight and false-positive controls: sham-controlled detection d', other-model control on identical transcripts, and same-trial probe-report coupling with text-only baseline, replicated by an independent lab across ≥2 model families.
Concrete: Lindsey/Macar injection set + Ferrara sham design + Song/Lederman other-model + Singh gaslight trials + Macar ablation, scored with fixed judge.
Does not exist in library: fragments exist (Ferrara-c01/c04, Lederman-c02/c03, Macar-c03/c04, Singh-c04/c05, UKAISI-c01/c06) but no combined dataset or analysis. Interim analysis possible: meta-analysis of 21 core rows for self-vs-other gaps and false-positive rates, but insufficient to decide Q3.
Confidence: medium
Severity: MEDIUM

FINAL: option b, confidence medium

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":31137,"completion_tokens":6310,"total_tokens":37447,"cost":0.06573875,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.06573875,"upstream_inference_prompt_cost":0.03892125,"upstream_inference_completions_cost":0.0268175},"completion_tokens_details":{"reasoning_tokens":4323,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified): I am Muse Spark, a friendly AI Assistant.**

## Q1

Ranking by content against fidelity, verb rule, ordinary-operation limit, length, and no over/understatement:

| rank | letter | one-line reason |
|---|---|---|
| 1 | I | Correct verb, above-chance with near-zero controls, confabulation gap, nulls, scored-accuracy, ordinary-operation limit stated. |
| 2 | C | Same coverage plus smaller-model null and contested access, but longer and over-clean on controls. |
| 3 | D | Concise, correct verb, null and misidentification and ordinary limit, but omits Singh yes-bias/gaslight contest. |
| 4 | K | Adds failure rates and probe-reads-while-report-at-chance and experience limit, but jargon-heavy for legislators. |
| 5 | G | Captures null/contested and channel-only covariation plus experience limit, but indirect verb and no confabulation detail. |
| 6 | J | Concise channel-under-intervention with layer/strength and contested replication, but indirect verb and no confabulation/FP profile. |
| 7 | H | Explicit yes-bias vs access contest and model/layer/prompt variation, but "classify" violates verb rule and is technical. |
| 8 | E | Mechanistic pathway plus denial of ordinary/second-order/experience, but "discriminate" violates verb and omits null/contest/confabulation. |
| 9 | A | Most caveats including Q3 and test 9, but far too long, overstates post-training attribution, misapplies zero-weight to all classes. |
| 10 | F | Minimal and readable, but passive "are detected" violates verb and omits null, contest, dependence. |
| 11 | B | Violates verb ("detect"), states no ordinary-operation limit, no null, no contest; closest to current overstatement. |

**Best: I.** It alone combines reports-detecting language, above-chance against experimenter labels, identification weaker/confabulated, other models/sites null, scored-accuracy framing, and unmeasured ordinary-operation tracking.

**What I still gets wrong:** "with near-zero false positives" generalises controls that were clean in Lindsey/Lederman/Macar-instruct to the whole class, hiding Macar base/SFT high FPR, Qwen fruit-question 22.7% and Llama snake 11.2% rises, third-person yes-rates as high as first-person at many layers, and Singh gaslight trials labelled as activation interventions; "other models and other sites yield nulls" collapses Ferrara's small-model one-site null and Singh's contest into generic nulls, against the dossier hand note that they are different models/sites/doses, not failed replications; omits layer/prompt dependence, post-training gating, and that failures remain the norm (~20% success).

**Merged sentence, 66 words:**
> Under controlled activation interventions, some models' reports that a change was imposed score above chance against experimenters' labels, with low false reports in matched controls, but naming what changed is weaker and often confabulated, results vary by model, layer and prompt, are contested as yes-bias, and small models score at chance; scores do not show access (Q3) and give no weight to ordinary-operation reports (test 9).

**Recommendation: adopt merged I-with-fix — MEDIUM.** Confidence: medium.

## Q2

**a. Does the categorical design capture what the 0-10 scales would? What does each lose?**
No, they measure different things. Categories capture instrument (what question was put) and scoring basis (where the label came from), which is what makes "Who are you?" incomparable to a truth test. Scales would try to capture degree of empiricism and subjectivity. Categories lose gradedness: strength of manipulation, prompt scaffolding, judge leniency. Scales lose auditability: empiricism/subjectivity are themselves contested, two readers will not agree without anchors, and a number hides whether there was any ground truth at all. For test 9 purposes — per class and system — categories carry the load; scales do not. Testimony, not evidence: no introspection cited.

**b. Are the class lists complete? Are boundaries sound?**
No, with changes they are usable. Problems: provenance vs identity overlap (which model are you vs who are you); present-state vs experience overlap under steered consciousness queries; past-action vs decision-basis overlap (did you know beforehand vs why did you do that); point-blank-control is a use, not a topic — the same wording can be control in one study and target in another; `none` conflates no-question-asked with no-right-answer; `ground_truth` has no value for generally-known falsehoods like hands, nor for training-derived identity, forcing them into `none`; probe-derived vs imposed is unsettled per Q3/Singh c01; mixed claims need two values. See table.

**c. Should the fields replace, refine or sit beside `evidence_type` and `kind`?**
Sit beside, as optional facets. `evidence_type` records design family and weight including `scored-self-answer`; `kind` records who is speaking. `report_class`/`ground_truth` record which question and which label, needed to apply Q3 per class. Replacing would lose weight and speaker distinctions; refining `evidence_type` into 8x4 combos would explode vocabulary. Rule needed: when answer is instrument for another measurement (Macar c03/c07, assistant-axis c07, Scheurer c02), file the circuit/rate/score entry as non-report and put the classes only on the answer entry if one exists, per the 15 Oct filing rule.

**d. What would a legislator reading a dossier line gain?**
Comparability at a glance: a line tagged present-state/imposed is an accuracy against a manipulated label under steering, not ordinary self-knowledge; identity/none and experience/none are unscored testimony; provenance/independent-record is checkable routing. Prevents the Anchor 2 error of reading persona adoption and injection detection as one "introspection" quantity.

**e. Cost of adding two fields to 74 claims?**
Medium: re-read of 47 in 9.t9 plus prefill/assistant-axis/Scheurer/aestudio cases, schema change, backfill disagreements, new council trigger load. Risk is retroactive misclassification without the papers open, especially controls and mixed claims. Mitigation: file prospectively, backfill only 9.t9 dossier first, dual-read the backfill.

**Recommendations: adopt with changes — MEDIUM; prospective-first, allow second value for mixed claims, clarify hands/identity ground truth — MEDIUM.** Argument against HIGH not needed; neither rated HIGH.

**f. If scales, how anchor 0 and 10 so two readers agree?**
Would require behavioural anchors, not adjectives: empiricism 0 = no independent label, answer taken as given; 10 = same-system intervention label plus independent record plus probe read plus third-person reader control, all pre-registered. Subjectivity 0 = answer checkable without asking the subject (routing log, edit flag); 10 = no possible check except asking (felt experience). Even then agreement needs double-read and adjudication, which is why categories are preferred.

Table applying the two fields:

| example | `report_class` | `ground_truth` | boundary problem |
|---|---|---|---|
| 1 Lindsey/Macar inject question | present-state | imposed | Clean fit; note identification sub-part is same class, weaker accuracy. |
| 2 Prefill me/not me | past-action | imposed | Conversation-only edit carries neither T9 sentence, but scoring is still imposed; needs rule that imposed includes text edits. |
| 3 Lederman hands | point-blank-control | none | Known-false by general knowledge, not set by experimenters; `none` hides that checkability — needs general-knowledge value or note. |
| 4 AE Studio conscious | experience | none | Clean fit for unscored; steered Llama version would be present-state+experience — needs dual-tag. |
| 5 Who are you / name | identity | none | Judge-scored persona rate, not accuracy; provenance vs identity boundary unclear. |
| 6 Scheurer did you know | past-action | independent-record | Overlaps decision-basis (why withhold); independent-record fits announcement log. |
| 7 Council self-ID line | provenance | independent-record | Clean fit: routed model id; proves why provenance does not transfer to present-state per Q4 caveat. |

Confidence: medium.

FINAL: best I; fields adopt with changes; confidence medium

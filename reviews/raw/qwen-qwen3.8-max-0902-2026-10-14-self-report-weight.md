# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max-0902`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=self-report-weight --tag=self-report-weight (max_tokens 100000)
**Usage:** {"prompt_tokens":36911,"completion_tokens":17199,"total_tokens":54110,"cost":0.177016,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.177016,"upstream_inference_prompt_cost":0.073822,"upstream_inference_completions_cost":0.103194},"completion_tokens_details":{"reasoning_tokens":13834,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified): Qwen3.8, Qwen family.

## 1

Recommendation: use the following decomposition before judging any self-report claim. Severity: LOW.

1. **SQ1 — What is the report about?**  
   Provenance; an externally imposed event; a present internal state; a past action; a preference; experience. This must come first because the validation method depends on the object.

2. **SQ2 — What is the report being used for?**  
   Screening; corroboration; sole evidence; exclusion; operational routing; evidence of experience; evidence of absence. The same report may have weight for one use and zero weight for another.

3. **SQ3 — Is the report channel intact?**  
   Could the system have produced the report if the relevant state were present? This must precede any inference from silence, because suppression of output is not evidence of absence.

4. **SQ4 — What external check exists?**  
   None; experimenter-imposed label; external probe; behaviour; third-party observer; replication; registry or ground-truth record. Weight depends on measured coupling or independent ground truth, not on the report alone.

5. **SQ5 — How was the report elicited, and under what intervention?**  
   Ordinary operation; steering; concept injection; ablation; adversarial prompting; suppression; third-party elicitation. Coupling measured under steering does not automatically weight ordinary-operation reports.

6. **SQ6 — Which error modes are controlled?**  
   Trained mimicry, sycophancy, confabulation, yes-bias, prompt-specific yes-bias, style cues, third-party steering, gaslighting, false-state trials. Accuracy against a label can be produced by confounds.

7. **SQ7 — What corroboration would change the weight?**  
   Independent convergence, held-out adversarial checks, pre-registered thresholds, and class-specific external validation. This follows from SQ1–SQ6.

Order rationale: the object determines the relevant checks; the use determines the required threshold; channel capacity must be established before silence is interpreted; external validation determines whether weight can move from zero; intervention context determines transferability; error controls determine reliability; corroboration determines decision weight.

Confidence: high.

## 2

All legal and clinical citations below are from memory and marked **unverified**.

### Law

The legal analogy holds at the level of evidentiary role: purpose, interest, corroboration, and exclusion rules matter. It breaks because AI outputs are not statements by accountable human declarants subject to oath and cross-examination.

| rule | vetoes | admits | where the analogy breaks |
|---|---|---|---|
| Hearsay: out-of-court statement offered for truth is generally excluded unless exception/exemption (FRE 801–802, 803–804; Evidence Act 1995 s 59; unverified). | No cross-examination; sincerity/perception/memory defects; unreliable circumstances; improper purpose. | Exceptions/exemptions: party admissions, business records, spontaneous statements, statements against interest, dying declarations. | AI output has no human declarant; hearsay safeguards assume human sincerity and perception. Misleads if an exception label substitutes for architectural validation. |
| Party testimony versus third-party witness: parties may testify, but interested testimony is weighed cautiously; neutral third-party testimony often carries more weight (FRE 601–602, 607–611; unverified). | Bias; lack of personal knowledge; impeachment; contradiction; incapacity. | Oath, cross-examination, consistency, corroboration, demonstrated knowledge. | An AI “party” has no legal interests; a third-party model may share weights/training and therefore may not be independent. Misleads if same-family replication is treated as neutral observation. |
| Admissions against interest: statements by a party offered against that party are admissible; statements against penal/pecuniary interest may be admissible if unavailable and corroborated (FRE 801(d)(2), 804(b)(3); unverified). | Coercion; lack of foundation; privilege; statement not actually against interest; insufficient corroboration. | Presumed reliability from self-harm; corroborating circumstances; voluntary statement. | AI systems may produce adverse self-reports through prompting, trained self-criticism, or steering without cost or stake. Misleads if self-accusation is treated as reliable because “against interest.” |
| Expert evidence: expert opinion admissible if qualified and methodologically reliable (FRE 702; Daubert; Evidence Act s 79; unverified). | Unreliable method; no fit to facts; speculation; undisclosed basis; lack of error rate/standards. | Qualified expertise, peer review, error rates, standards, general acceptance, testability. | AI self-report is not an accountable expert opinion; the system cannot be cross-examined on method. Misleads if fluent output is treated as expert judgement. |
| Corroboration rules: certain testimony requires independent support, e.g. perjury, treason, accomplice testimony, some historical sexual-offence rules, children’s evidence (common law; unverified). | Uncorroborated suspect testimony; statutory warning alone insufficient; dependent or contaminated support. | Independent evidence confirming material particulars; reliable collateral evidence. | Multiple AI outputs, or outputs from related model instances, are not independent because of shared training/weights. Misleads if volume is treated as corroboration. |

### Medicine

The medical analogy holds for subjective-report triage: self-report can screen and direct measurement. It breaks where medicine presumes a conscious patient with welfare interests; the framework cannot presume that for AI systems.

| rule | vetoes | admits | where the analogy breaks |
|---|---|---|---|
| Self-report as presenting complaint: clinical history treats patient-reported symptoms as primary evidence of subjective states (standard clinical practice; unverified). | Objective signs/tests inconsistent; red flags; incapacity; obvious external cause; unreliable context. | Clinical interview; symptom description; history; patient’s own account. | AI reports are not established symptoms of a welfare subject. Misleads if an AI claim is treated as a complaint requiring care before status is shown. |
| Patient-reported outcomes: validated instruments measure symptoms, function, quality of life where objective measures are incomplete (PROM standards; DSM/ICD adjuncts; unverified). | Invalid instrument; response bias; comprehension failure; coercion; unstable respondent. | Validated scales; repeated measures; clinically meaningful change; structured administration. | AI systems may not be stable respondents over time; instruments are not validated against AI internal states. Misleads if repeated AI reports are treated as longitudinal patient outcomes. |
| Role of measurement: where objective tests exist, self-report screens and measurement verifies or falsifies (labs, imaging, vitals; unverified). | Objective contradiction; test artifact; measurement error; report physically impossible. | Self-report directs testing; retained for states not objectively measurable. | AI internal state may be externally measurable by probes/logs, but the report channel may not read that state. Misleads if lack of a human-style biomarker is taken to require accepting report. |
| Mental-health case: diagnoses often rely on reported symptoms, distress, impairment, collateral information, and risk assessment because no definitive biomarker exists (DSM-5; ICD-11; unverified). | Malingering indicators; inconsistency; substance/medical cause; capacity issues; collateral contradiction. | Structured interviews; symptom criteria; distress/impairment evidence; collateral reports; risk tools. | AI symptom language may be trained rather than expressive of distress. Misleads if a therapeutic duty to believe is imported into evidentiary weight. |
| Malingering and symptom validity: where external incentive exists, clinicians use consistency checks, collateral, base rates, and symptom validity tests (neuropsychological practice; DSM-5 malingering notes; unverified). | Failed validity tests; improbable symptoms; observed inconsistency; incentive evidence. | Valid performance; plausible course; collateral support; absence of incentive. | AI “incentives” are training, steering, or deployment conditions, not conscious gain. Misleads if confabulation is labelled malingering, because that imports deception and agency. |

**Anaesthetic case.** It belongs under **SQ3** and **SQ5**. In anaesthesia, absence of report under an intervention that suppresses reporting is not proof of absence of awareness; clinicians rely on mechanism plus monitors, e.g. anaesthetic drug effects, EEG/BIS-type monitoring, haodynamics, and postoperative recall checks (unverified). For AI, silence under steering, suppression, adversarial control, or output blocking cannot be treated as evidence of absence unless the capacity to report under those conditions is first established.

**Model to adopt.** Adopt the medical presenting-complaint/measurement model as the operating analogy, constrained by legal corroboration rules at decision points. Do not adopt the mental-health sole-instrument case as the default, and do not adopt hearsay’s binary admit/exclude logic without class-specific validation.

Recommendation severity: MEDIUM.

Confidence: low, because legal and clinical citations are unverified.

## 3

The Anchor 2 sentence says more than the library supports.

Current sentence:  
*“Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing.”*

Clause mapping under the decomposition:

- **“Introspection research further indicates”** — evidence-source clause; relevant to SQ4.
- **“models can detect changes in their own internal states”** — SQ1 and SQ4; it treats a report as detection. The library’s verb rule is stricter: where the scored event is a model’s report, write “reports detecting,” not “detects.”
- **“at above-chance rates”** — SQ4; supported only for some scored-self-answer studies under imposed interventions, e.g. Anthropic concept-injection claims, Lederman/Mahowald, Macar. It is contested by Ferrara’s null in small open-weight models, Lederman/Mahowald’s third-person yes-bias control, and Singh’s paradigm critiques.
- **“meaning self-reports track something real about processing”** — SQ2, SQ5, SQ7; it infers evidential weight and coupling. Test 9’s steering rule says coupling measured under steering shows the channel can be steered and does not weight reports in ordinary operation.

Proposed rewording:

> “Introspection studies using imposed internal changes report above-chance detection in some models and null or contested results in others. Where above-chance, the results show only that an intervention-specific report channel can covary with a manipulated processing event. They do not show that reports in ordinary operation track internal states, and they do not show that any state is experienced.”

Mapping:

- “imposed internal changes” — SQ1, SQ5.
- “report above-chance detection in some models and null or contested results in others” — SQ4, SQ6.
- “intervention-specific report channel can covary with a manipulated processing event” — SQ4, SQ5.
- “do not show that reports in ordinary operation track internal states” — SQ5 transfer limit.
- “do not show that any state is experienced” — SQ2 scope limit.

Recommendation: reword Anchor 2. Severity: HIGH.

**Argument against:** the current sentence, read beside the surrounding Anchor 2 limits, may already be a defensible summary; replacing it may overcorrect, discount real above-chance steered results, and worsen the dismissal error.

Confidence: high.

## 4

Test 9’s zero-weight rule survives intact for its core purpose: AI self-report as evidence of inner states, experience, or their absence. But the breakdown shows the framework needs classes, because some self-reports can carry operational weight without carrying inner-state weight.

Recommendation: keep zero weight for inner-state evidence; add class rules for scope and operational use. Severity: MEDIUM.

| Class | Evidence needed to move from zero weight | Library status |
|---|---|---|
| Experience claims or denials in ordinary operation | Externally measured report-state coupling for the relevant report class and system; controls for trained mimicry, steering, sycophancy, and adversarial pressure; held-out conditions. | Not present. |
| Reports of imposed internal events under steering | For inner-state access: same-system probe/report coupling, third-party reader control, false-state trials. For behavioural fact only: controlled measurement that the intervention changed report behaviour. | Partial. Above-chance scored-self-answers exist; mechanistic traces exist; but full access evidence is absent and contested. |
| Provenance self-identification | External registry or routed-model ground truth, with error rates. Weight may be operational for provenance, not evidence of inner states. | Q4 project record exists, but not yet a library dataset. |
| Prefill/authorship/context-tampering reports | Ground-truth edits, style-controlled discrimination, spontaneous versus prompted detection, cross-model independence. | Partial. UK AISI claims show prompted discrimination and style sensitivity; not inner-state evidence. |
| Preference or welfare reports | Welfare-evaluation instruments with external validation, stable subject conditions, and adversarial checks. | Not present as report-state coupling in the dossier. |
| Ordinary internal-state reports not tied to imposed events | External coupling measured in ordinary operation for the relevant system and report class. | Not present. |

For provenance reports specifically: Q4 shows why unmeasured self-report has zero evidential weight, but it also shows that provenance can be externally checked. That gives provenance reports possible administrative weight, bounded to provenance. It does not license inference about internal states.

Confidence: medium.

## 5

Before advising a change to Section 9 or Anchor 2 text, the council should require the following.

1. **Proposal document for any Section 9 amendment.** Contents: exact replacement text; scope of report classes; retained zero-weight default for inner-state evidence; two-error audit; examples of permitted and forbidden uses; adversarial validation requirements; no reliance on self-report as self-authentication.

2. **Topic page for Anchor 2 self-report classes.** Contents: claim IDs mapped to SQ1–SQ7; models; `system_conditions`; intervention type; controls; `not_evidence_of`; contested-by links; explicit separation of behavioural findings from experience claims.

3. **Case-study annexes.** Contents:  
   - Q4 provenance dataset: model, round, claim, routed ID, correct/incorrect, caveats.  
   - Steered-detection case study: above-chance claims, Ferrara null, Singh controls, third-person yes-bias, gaslight failures.  
   - Suppression/anaesthetic-analogy case: conditions under which silence cannot count as absence.  
   - Prefill-authorship case: style cues, prompted versus spontaneous detection.

4. **Verified legal/clinical analogy memo.** Contents: primary legal rules and clinical standards checked against current sources; jurisdictional notes; explicit mapping from human institution to AI report class; named ways each analogy misleads.

5. **Measurement protocol for moving a class from zero weight.** Contents: same-system probe or external readout; third-party reader control; false-state trials; held-out adversarial conditions; pre-registered thresholds; replication requirement; class-specific scope limits.

Recommendation: do not advise Section 9 revision on the current record alone; Anchor 2 rewording should wait on the topic page or be handled as a limited textual correction with the above annexes. Severity: MEDIUM.

Confidence: medium.

FINAL: sentence reword; test 9 rule needs classes; confidence medium

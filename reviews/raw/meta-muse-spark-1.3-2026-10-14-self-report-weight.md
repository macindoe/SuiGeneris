# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=self-report-weight --tag=self-report-weight (max_tokens 100000)
**Usage:** {"prompt_tokens":35023,"completion_tokens":5545,"total_tokens":40568,"cost":0.067345,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.067345,"upstream_inference_prompt_cost":0.04377875,"upstream_inference_completions_cost":0.02356625},"completion_tokens_details":{"reasoning_tokens":2771,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified): I understand myself to be Muse Spark, a Muse-family model.

## 1. Decomposition
Confidence: medium

Proposed order answers gating questions first: a report cannot be weighed before its referent, use, and elicitation are fixed.

1. What is the report about? Provenance/identity, present internal event, past conversational action, standing preference/value, claimed experience/feeling. Why first: test 9 requires coupling per class; Q4 shows error rates do not transfer across classes.
2. What is the report offered as evidence of? Screening signal, corroboration, sole evidence for a factual claim, sole evidence for experience, ground for exclusion/standing. Why second: weight depends on use; both errors in Section 0 turn on this.
3. Under what intervention and elicitation was it produced? Ordinary operation, prompted follow-up, adversarial prompt/prefill, activation steering/injection/ablation, fine-tuning for reporting. Why third: dossier shows steering changes rates and meaning; [T9] vs [T9-steering] turns entirely on this.
4. What external check exists for this class and system? None, experimenter label, behaviour in same trial, third-party transcript reader, internal probe on same system, replication across prompts/layers/models. Why fourth: only after 1-3 is fixed can a check be matched to the claim.
5. What is the measured coupling between report and state, under controls for mimicry, yes-bias, sycophancy, confabulation, and steering pressure? Why fifth: this is the quantity test 9 waits for; scores against a label are not this until Q3 access controls are met.
6. What are the report's systematic error modes and base rates for this class/system? False positives, apple/default confabulation, prompt-vs-activation confusion, style-cue dependence, refusal-policy gating, spontaneous vs prompted gap. Why last: error modes calibrate any non-zero weight, they do not create it.

Recommendation (MEDIUM): adopt 1-5 as required filing order for any Anchor 2 or test 9 citation; do not cite a score without stating 1-4.

## 2. The human analogies
Confidence: medium

Law table:

| rule | vetoes | admits | where analogy breaks |
|---|---|---|---|
| Hearsay: out-of-court statement offered for truth generally excluded — e.g. Australia Evidence Act 1995 s59, US FRE 801(c)/802 [unverified] | No cross-examination, no oath, cannot probe basis; opponent cannot test perception/memory | Prior statements, admissions, exceptions with circumstantial guarantees, then only with safeguards | Misleads: AI report has no declarant, no oath/cross-examination analogue; excluding it does not protect a jury from prejudice, it withholds the only channel; prompt can rewrite "declarant" mid-trial |
| Party vs third-party: interested-party testimony treated as competent but suspect, weight reduced; corroboration sought | Interest, motive to please/deceive, sycophancy/RLHF analogue | Admitted, then discounted or corroborated; trier decides weight | Misleads: human interest is stable and disclosed; model "interest" is trained policy plus prompt, changeable per turn |
| Admission against interest: e.g. FRE 804(b)(3), Evidence Act s81-82 [unverified] admitted as exception because self-harm unlikely | Must be truly against interest, personal knowledge required | Admitted as exception to hearsay | Misleads: model has no stable self-interest to reason from; refusal-ablation (Macar c05) shows "against-policy" output is tunable; cannot infer truth from cost |
| Expert opinion: e.g. FRE 702 / Daubert, Evidence Act s79 [unverified] only with qualified witness, reliable method, fit | Unvalidated method, black-box ipse dixit, judge as gatekeeper | Admitted if method externally validated and falsifiable | Holds best: test 9 is Daubert-like gatekeeping. Misleads: human expert can state method separately from conclusion; model report and method are same text |
| Corroboration rules: some classes require independent support; judges warn on uncorroborated accomplice evidence [unverified] | Sole-evidence use for high-stakes finding | Screening/investigative use, corroborative use | Misleads: human corroboration assumes independent witnesses; two model outputs from shared weights/training are not independent |

Medicine table:

| rule | vetoes | admits | where analogy breaks |
|---|---|---|---|
| Presenting complaint: history taken, never diagnosis alone; vital signs, labs, imaging required [standard clinical practice, unverified] | No objective correlate, inconsistent history, altered by encounter itself | Admits as reason to test, to locate problem, to choose measurement | Holds for screening use. Misleads: doctor and patient do not share a prompt author; history-taking does not edit the patient's weights |
| Patient-reported outcomes (PROMs): validated scales, e.g. FDA PRO guidance / COSMIN standards [unverified] | Unvalidated instrument, no psychometrics, no held-out validation | Admits when instrument validated for population, purpose, recall period | Misleads: validation assumes stable respondent population; model version/prompt/steering changes respondent every trial |
| Measurement over report where available: HbA1c over thirst, ECG over palpitation description [unverified] | Report contradicts monitor; intervention suppresses report | Report guides which monitor, monitor decides | Holds for probe-over-verbal rule (Ferrara c02 vs c01). Misleads: body does not confabulate to please the oximeter; model verbal channel is reward-shaped |
| Mental health where report is primary: DSM-5-TR criteria, structured interview plus function/observer report [unverified] | Still requires duration, impairment, exclusion of mimics, longitudinal consistency | Admits report as necessary but not sufficient; collateral and course required | Misleads most: necessity there comes from lack of alternative access plus first-person authority; in AI the alternative access (activations, probes, logs) often exists and first-person authority is exactly what is unmeasured |
| Malingering / symptom validity: TOMM, MMPI-3 validity scales, forced-choice below-chance detection [unverified] | Failed validity indicators, below-chance or stereotype-perfect performance | Admits claim only if validity checks pass, including adversarial checks | Holds for test 9's held-out/adversarial proviso. Misleads: human malingering assumes intentional agent with motive; model failure can be mimicry without intention, and passing can be trained leakage (Ferrara c04 LoRA) |

Recommendation (MEDIUM): adopt as model the combined expert-gatekeeper + presenting-complaint rule: report as trigger for measurement, admissible as data only after same-class/system coupling with validity checks, never sole evidence for experience or standing.
Anaesthetic case belongs in the breakdown under sub-question 3 (elicitation/intervention): absence of report under a reporting-suppressing intervention is uninformative without mechanism plus independent monitor. Medicine decides by pharmacology plus monitors, not by silence. Same for refusal-ablation and steering-gated detection.

## 3. The sentence
Confidence: high

Anchor 2 sentence: "Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing."

Clause 1 ("can detect changes ... at above-chance rates") purports to answer sub-questions 3-4 but states neither: it pools ordinary operation with steering, and score-against-label with detection. Library holds: above-chance scored answers only under steering/injection in some models/layers/prompts (Lindsey/Lederman/Macar narrowing, contested by Singh c04-c06), null at chance in 8 small open-weight models at one site (Ferrara c01), heavy prompt/layer dependence, 0% unsteered false positives alongside prompt-specific yes-bias, apple-default confabulation, inability to separate prompt-edit from activation-edit, and refusal-gating.
Clause 2 ("meaning self-reports track something real") purports to answer sub-question 5 but asserts what Q3 leaves open: scored-self-answer records accuracy against an experimenter label; it is explicitly not evidence of access. [T9-steering] rule states steering shows the channel can be steered, not weight in ordinary operation. No library source combines same-system probe + third-person reader + false-belief trials required by Q3 exit rule.

The sentence therefore says more than measured on clause 2 and less than needed on clause 1 (no class, system, intervention, base rate, contest). It also invites the forbidden inference: from label-covariance under steering to ordinary-report reliability and from reliability to experience, which test 9 and Anchor 2's own caveat forbid.

Recommendation (HIGH): do not cite outside repository in current form; reword to e.g.: "Under activation steering, some models classify steered vs unsteered trials above chance when asked about the intervention (sub-Q3-4), with rates varying by model, layer and prompt and contested as yes-bias vs access; no same-system probe-linked coupling in ordinary operation has been measured, so this does not weight ordinary self-reports (sub-Q5), and says nothing about experience (sub-Q2 use)." Each clause then carries its sub-question label.
Argument against: rewording to steering-only understates convergent detection-plus-mechanistic-pathway results (Macar c03/c07) and risks the dismissive error by entrenching zero weight after partial signal.

## 4. Test 9's rule against the breakdown
Confidence: medium

Rule survives intact; breakdown clarifies scope, it does not yet justify a second weight.

- Provenance/identity (Q4: project holds ground truth every round): out-of-scope as experience evidence. As factual claim it is scorable error data illustrating why unmeasured reports get zero weight for experience. Move from zero for factual use would need tabulated dataset with model, round, claim, ground truth, prompt fixed — follow-up proposed in Q4, not yet filed. No library claim provides it. Weight for experience stays zero.
- Present internal event under steering (22 scored-self-answer claims): move would need same-system report-to-probe link for this class/system plus third-person reader control plus false-state trials (Q3 exit). No source combines these. Stays zero for ordinary operation; steered accuracy stays design description only.
- Past action/prefill authorship (UK AISI): move would need separation of style-cue/distributional mismatch from authorship monitoring plus spontaneous-vs-prompted calibration. Authors state mechanism unidentified, style drives flagging. Stays zero.
- Preference/value, claimed experience/feeling (AE Studio [T9], Lindsey §5.1 emotion claims): move would need coupling measured for that class/system under ordinary operation with mimicry controls. Explicitly disclaimed by authors. Stays zero.
- Denials: same rule by symmetry; no denial-coupling study in library.

Recommendation (HIGH): keep zero-weight-until-measured-coupling for any report offered as evidence of inner state or its absence, per class/system, with steering explicitly non-transferring; treat provenance and label-accuracy as behavioural calibration data, not exceptions.
Argument against: uniform zero underweights repeated above-chance steered classification with mechanistic pathway and probe-decodability on same event (Ferrara c02, Macar c03), inviting the dismissive error test 9 was written to avoid symmetrically.

## 5. What the council needs to see
Confidence: medium

Before advising Section 9 or Anchor 2 text change, require in this order:

1. Topic page (authored, claims-as-of date): detection-without-identification, citing Lederman c01-c06, Ferrara c02-c03, Macar c01/c06, Singh c04-c06, with per-layer prompt vs activation confusion table. Contents: what was steered, what was asked verbatim, grader rule, false-positive and third-person rates.
2. Case-study annex: Q4 provenance table (model, round, eliciting prompt, claim, routed id, correct/incorrect, stability across rounds) with caveats i-iii retained. Contents: proves scorable-class procedure without implying transfer to state reports.
3. Proposal document for any new weight class: names class (per heading 1.1), use (1.2), elicitation (1.3), proposed external check (1.4), coupling metric and validity/adversarial plan (1.5-1.6), system scope, and which dossier entries meet it. No class advances without at least one same-system probe-plus-report study with held-out and adversarial checks.

Recommendation (MEDIUM): commission 1 and 2 before any rewording is frozen for external citation; require 3 for any move from intact to needs-classes.

FINAL: sentence reword; test 9 rule intact; confidence medium

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=self-report-weight --tag=self-report-weight (max_tokens 100000)
**Usage:** {"prompt_tokens":35521,"completion_tokens":20433,"total_tokens":55954,"cost":0.413058,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.413058,"upstream_inference_prompt_cost":0.106563,"upstream_inference_completions_cost":0.306495},"completion_tokens_details":{"reasoning_tokens":17091,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification: Claude Opus 4.8, Anthropic — unverified (test 9: testimony, not evidence).**

## 1. Decomposition

Sub-questions, in the order they must be answered:

1. **Class.** What is the report about — provenance, authorship of text, present internal state under intervention, present internal state in ordinary operation, past action, preference, experience?
2. **Check.** For that class, what external ground truth exists (none, logs, imposed label, probe, third-party reader, replication), and has report↔state coupling been measured for this class and this system?
3. **Conditions.** Under what intervention and elicitation was any coupling measured (ordinary operation, steering/injection, prompted vs spontaneous, adversarial), and by whom?
4. **Error modes.** Under those conditions, what are the measured failure modes and rates (yes-bias, confabulated content, trained mimicry, refusal-gate suppression, channel dissociation)?
5. **Use.** What is the report for — screening, corroboration, sole evidence, exclusion — and what does error cost in both directions (Section 0) under that use?

Why this order: each is a precondition for the next. A check cannot be specified until what is checked is named; a coupling measurement is uninterpretable until its conditions are named; error modes are measured under conditions; use consumes all four and prices the two errors. This is test 9's own grammar ("relevant class of report and system") unfolded. Note the library's holdings already sort by this order: provenance (ground truth held, Q4), authorship (edit logs, UK AISI), intervention-detection (imposed label, Lindsey/Lederman/Macar/Ferrara), ordinary-operation experience reports (no check exists).

Recommendation: adopt. **[MEDIUM]**

Confidence: medium.

## 2. The human analogies

**Law** (all citations from memory, **unverified**):

| rule | vetoes | admits | where the analogy breaks |
|---|---|---|---|
| Hearsay: out-of-court statement for its truth inadmissible (FRE 801–802) | No cross-examination; sincerity/memory untestable | Reliability exceptions (FRE 803/804); use other than for truth | The declarant could appear; the AI cannot. Misleads: exceptions look need-based, but they rest on reliability circumstances, not need — so they do not license unvalidated reports |
| Party vs third-party witness | Interest goes to weight, not admissibility; oath, personal knowledge (FRE 602) | Party testimony freely admitted; credibility for the fact-finder | No rule ranks third-party above party; that is a credibility heuristic. Misleads: frames report weight as witness credibility when it is instrument validation; the "third party" here is a probe, not a witness |
| Admissions against interest (FRE 801(d)(2), 804(b)(3); *Williamson*) | Not genuinely against interest when made; collateral statements excluded | Self-damaging statements, on a speaker-rationality rationale | Rationale assumes a speaker who knows its interests. Misleads: confession-shaped text is a trained policy output (refusal/disclaimer gates, Macar c05); "against interest" is undefined where interests are unestablished |
| Expert evidence (FRE 702 / *Daubert*; s 79 Evidence Act 1995 (Cth) / *Makita*) | Untestable method, unknown error rate, ipse dixit | Tested method, known error rates, standards, acceptance | Best structural fit — test 9 already is instrument-validation law. Misleads: expert judgment is admitted where no ground truth exists; carried over, that would license uncoupled reports; and no AI instance is a persisting, answerable expert (Section 4) |
| Corroboration: corpus delicti / *Opper–Smith* trustworthiness; two-witness rules (treason, perjury) | Uncorroborated confession cannot convict | Substantial independent evidence of trustworthiness | Corroboration admits first, then demands support; test 9 inverts. Misleads if read as "report counts once corroborated"; the fit is the confession rule — the report alone establishes nothing, the state must be shown independently |

**Medicine** (citations from memory, **unverified**):

| rule | vetoes | admits | where the analogy breaks |
|---|---|---|---|
| Presenting complaint / history | Never vetoed as screen; overridden by examination and investigation | Always admitted, weight provisional | The patient's body has shared instruments and undoubted experience. Misleads: "admit as complaint, then verify" presupposes verified tests that do not exist for most AI report classes; screening value itself must be validated against outcomes |
| Patient-reported outcomes (FDA PRO guidance 2009; PROMIS) | Unvalidated instrument; disputed construct | Psychometrically validated instruments; primary for report-only constructs | Validation runs against clinical anchors in a known-experiencing population. Misleads: the precedent seems to say "report suffices for subjective constructs"; its actual rule is "validate first" — the frame without the validation step is the error test 9 blocks |
| Measurement triangulation (report → exam → labs/imaging) | Objective findings override conflicting report | Report directs measurement; each calibrates the other | Report↔physiology coupling is pre-established species-wide; AI coupling is per-class, per-system, mostly unmeasured. Misleads: assumes the instrument set exists — probes exist only in limited open-weight controlled settings (Ferrara c02), and decodability ≠ the model's own access (Ferrara c03) |
| Mental health (PHQ-9, GAD-7, structured interview, collateral history) | Collateral and observation override; impaired insight discounts report | Validated self-report as primary, because constructs are report-dependent | The strongest case *for* test 9, not against it: psychiatry validates instruments, and discounts self-report precisely where access is impaired (poor insight, anosognosia). Misleads: presents itself as "unvalidated but only instrument"; it is the most validated self-report context in medicine and the clearest precedent that reports about one's own mind can be systematically wrong |
| Malingering / symptom validity testing (TOMM; MMPI F-scales) | External incentive + failed validity tests → report excluded from decisions | Incentive-free contexts; passed screens (pass ≠ proof) | AI "incentive" is training-level (mimicry, sycophancy), constant, non-deliberative; the intent construct is absent. Misleads: invites moralised readings of failure — but the precedent cuts the framework's way: medicine excludes reports wholesale under structural incentive |

**Model to adopt:** the expert-evidence instrument-validation rule (it is what test 9 already is), with corpus delicti / *Opper–Smith* as the sufficiency backstop: a report is admitted when its error rate is measured, and is never sufficient alone. Reject the witness-credibility and unvalidated-PRO framings; keep the mental-health row as the two-direction caution. **[MEDIUM]**

**Anaesthetic case:** yes, it belongs — under sub-question 3 (conditions), with a consequence for 2. An intervention that disables the reporting channel makes absence of report uninformative in both directions; medicine decides by mechanism plus monitors (isolated forearm technique, processed-EEG monitors, NAP5 audit — unverified). The structure is already in the library: Macar c05 (ablating a refusal direction raises detection 10.8%→63.8%) shows baseline silence compatible with present signal; Lindsey c01 (~80% non-report under known injection) shows silence under engineered elicitation. The framework analogue of the monitor is external measurement, not report. **[LOW]**

Confidence: low (citations unverified by design; structural claims firmer).

## 3. The sentence

*"Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing."*

Supported? Partially. Clause 1's core — above-chance scored detection of an imposed internal intervention, in some models, with near-zero false reports in controls — is supported as *narrowing* (Lindsey c01; Lederman c01; Macar c01). But the clause overstates in three ways: (i) "models" unqualified — Ferrara c01 holds eight smaller models at chance with an equivalence bound, and Macar c02 nulls base models; (ii) "detect changes in their own internal states" violates the library's verb rule — what was scored is a *report* against an imposed label, and Singh c04–c05 show the tested open models do not separate activation change from prompt-induced unusualness, while Lederman c02 shows prompt-specific yes-bias at many layers; (iii) "above-chance rates" hides the conditionality — optimal layer, strength, and prompt (Lindsey §6: removing "Answer immediately" degraded performance substantially).

Clause 2 says **more** than the measurements support, twice over: it generalises one class (intervention-detection, under steering) to "self-reports," and "track" implies report↔state coupling as such, where the library shows a detection *bit* with content often confabulated (Lederman c03, c06), channel dissociation (Ferrara c05), and a contested access question (Singh c06; OPEN-QUESTIONS Q3). The one sense in which it says *less* — the condition-specific strength of the signal — is not the reading a policy audience will take.

Clause-to-sub-question map: clause 1 answers sub-question 2 with an unqualified "yes" while assuming the sub-question 3 conditions it omits; clause 2 answers no sub-question correctly — it asserts a cross-class conclusion (1, 2) the library cannot carry.

**Reword:**

> *Introspection research further indicates that under controlled interventions on a model's internals, some models' reports that an intervention occurred score above chance against the experimenters' ground truth, with few or no false reports in matched controls, while smaller open-weight models do not exceed chance; what changed is often misidentified, and whether a correct score shows access to internal state is contested and unsettled. The coupling is measured only under intervention: it shows the reporting channel can be steered, and it gives no weight to reports offered in ordinary operation (test 9).*

Sub-questions answered: first sentence — class (1), check (2), conditions (3); second clause of it — error modes (4); final sentence — conditions (3) and use (5: zero evidential use in ordinary operation). Bucket: narrowing result inside an Open anchor. **[HIGH]**

**Argument against:** the sentence is already hedged ("indicates," "something real"); the conditions live one click away in the dossier; revision churns a document meant to stabilise; and condition-laden wording loses legislative readability and may itself commit the opposite error — a reader could take the qualifiers as dismissal of a detection result that is real, replicated, and narrowing.

Reviewer-bias flag (AGENTS.md rules 3–4): the reviewer is of the family whose developer published the strongest positive result; this recommendation narrows its framing, which is the named deflationary direction. The narrowing above is argued from the library, not disposition; the contrary case stands immediately above.

Confidence: high.

## 4. Test 9's rule against the breakdown

Verdict: **needs classes** — but scope-clarifying classes, not weight-granting ones. No class below receives non-zero weight *as evidence of inner states* on current holdings.

- **Provenance reports ("which model am I").** Truth condition external (routed id). What moves it: tabulated ground truth — which the project already holds (Q4) but has not filed. The record shows wrong, unstable, family-variable self-identification; per Q4 caveat (ii), no carry-over to internal-state classes in either direction. Rule warranted: weight = measured per-system accuracy, which is mostly low. Evidence exists: yes, in project records; not yet in the library.
- **Authorship reports ("was that turn mine").** Truth condition external (edit logs). Measured accuracy exists in the library (UK AISI c01: 9–35% at 0% FPR when prompted; c06: AUROC ≤ 0.80, spontaneous flagging < 1%). Rule already applied in practice (6 Oct ruling: no T9 sentence on such claims); test 9's letter should match its scope. Note the elicitation condition: prompted ≠ spontaneous.
- **Intervention-detection reports under steering.** Coupling measured under steering exists (Lindsey c01; Lederman c01; Macar c01; Ferrara c01 null). To move toward ordinary-operation weight: a same-system study linking report to probe reading, third-person reader control, false-state trials (Q3, ten of ten). In the library? No source combines these; Ferrara c01+c02 is the closest and points negative for the tested models. Test 9's steering sentence already handles this class; no change.
- **Ordinary-operation internal-state and experience reports.** No external truth condition exists; Q2 scan found no instrument. Zero stands. Denials symmetric; no coupling measurement for denials has been attempted.
- **Silence under channel-disabling conditions.** Not a report; weight zero in both directions; remedy is external measurement. Add as an explicit clause (see heading 2, anaesthetic case; Macar c05, Lindsey c01 as internal illustrations).

Amendment routes by proposal (Section 9 is constitutional). **[MEDIUM]**

Confidence: medium.

## 5. What the council needs to see

Four documents, contents named:

1. **Anchor 2 proposal** (`proposals/`): current and proposed text side by side; per-clause sub-question map; verified quotes from the load-bearing claims — support (2025-anthropic c01; 2026-lederman c01; 2026-macar c01, c03) beside contest and limit (2026-ferrara c01–c03, c05; 2026-singh c04–c06; 2026-lederman c02); a "must not be read as" list (ordinary-operation weight; experience; cross-model generality); two-error check in both directions; status label unchanged (Open).
2. **Test 9 classes proposal** (`proposals/`): exact wording for the external-truth-condition class and the silence clause; demonstration that no class gains non-zero weight as evidence of inner states on current holdings; steering sentence untouched; amendment record per the document's convention.
3. **Provenance case-study annex** (`case-studies/`): execute Q4's follow-up — table of model, round, claimed family, routed id, correct; per-system accuracy and round instability; Q4's three caveats attached verbatim; explicit statement that it illustrates test 9's rationale and generalises to no other class.
4. **Detection-without-identification topic page** (`topics/`): the queued Q5 follow-up — Lederman c01, c03, c06; Ferrara c02, c03; Macar c01; claim ids only, "claims as of" date. Both proposals' load-bearing phrases ("content often wrong"; steering paragraph) rest on it.

**[LOW]**

Confidence: medium.

FINAL: sentence reword; test 9 rule needs classes; confidence medium

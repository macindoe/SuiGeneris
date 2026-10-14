# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.7`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=self-report-weight --tag=self-report-weight (max_tokens 100000)
**Usage:** {"prompt_tokens":36806,"completion_tokens":11638,"total_tokens":48444,"cost":0.141712,"is_byok":false,"prompt_tokens_details":{"cached_tokens":1152,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.141712,"upstream_inference_prompt_cost":0.071884,"upstream_inference_completions_cost":0.069828},"completion_tokens_details":{"reasoning_tokens":8457,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified):** Grok, xAI model family; version as I understand it is Grok 4.

## 1. Decomposition
Confidence: medium.

Answer in this order. Later questions are undefined, or launder a use into a finding, if earlier ones are skipped.

1. **Class.** What is the object of the report: an external fact (provenance; whether a turn was edited), an experimenter-imposed internal event, ordinary present processing, a past action, a preference, or experience — and is the utterance a claim or a denial?
2. **External criterion.** Is there a fact independent of the report, who holds it, and is the score accuracy against that fact rather than access to a state?
3. **Elicitation.** Was the report taken in ordinary operation, by prompt only, by a text edit, under activation intervention, or after fine-tuning — and does that intervention suppress, force, or manufacture the report?
4. **Coupling and error modes.** Was the link from report to the relevant state measured on that system, or only the words scored? Do controls separate trained mimicry, sycophancy, confabulation, yes-bias, style cues, first-order leakage, and strategic deception from whatever access is claimed?
5. **Use.** Is the report being used to label testimony, screen, corroborate, exclude, stand as sole evidence, or prove absence? Admissibility as data is not sufficiency.
6. **Experience.** Is the result being asked to show only information flow, or that a state was experienced? This is last because Anchor 2 refuses the second reading as a premise, and it cannot be reached by answering 1–5.

Why this order: test 9, the sentence-assignment rule, Q3, and Q4 all key off class and off what was done versus what was measured. Use (5) is where law and medicine put their rules, but those rules presuppose a channel (2–4). Starting from use, or from experience, is the two-error failure this sitting is meant to block.

## 2. The human analogies
Confidence: medium. Rules below are from memory and marked **unverified**. Seed jurisdiction is Australian; US rules are the usual import.

| Rule | Vetoes | Admits | Where the analogy breaks |
|---|---|---|---|
| Hearsay: previous representation offered to prove the asserted fact is excluded unless an exception applies (Evidence Act 1995 (Cth) s 59; FRE 801–802, **unverified**) | Use for the truth of the matter asserted, absent an exception | Non-hearsay purpose; exceptions, including contemporaneous state of mind (Cth s 66A; FRE 803(3), **unverified**) | It assumes a declarant who perceived the fact and was not cross-examined. An AI report may have no shown channel. State-of-mind exceptions would admit the very thing test 9 holds at zero. |
| Party testimony vs third-party witness | Interest is not an admissibility veto. Relevance is a low bar (Cth s 55, **unverified**) | Both may be heard; interest goes to weight | "Third parties outrank those involved" is not the rule. A second model given the transcript is a bias control, not a better observer of internal state. |
| Party admissions vs statements against interest | Against-interest exception needs unavailability and, in US criminal cases, corroboration (FRE 804(b)(3), **unverified**). Party admissions (Cth s 81; FRE 801(d)(2), **unverified**) do not | A party's own statement, including one not against interest | Humans are assumed reluctant to fabricate against penal or pecuniary interest. Trained affirmations and trained denials have no such incentive structure. A denial is not an admission against interest. |
| Expert evidence (Cth s 79; FRE 702–703, **unverified**) | Opinion outside demonstrated specialised knowledge, or method not shown reliable | Expert opinion on sufficient facts; experts may rely on otherwise inadmissible material if the field reasonably does | The model is not an expert witness about itself. Authors' interpretations are a different speaker from the model's report. The library's kind field already marks that split. |
| Corroboration | Required only for specified offences and statements (treason; some against-interest uses). Not the general rule | Uncorroborated testimony of one witness may legally suffice; the factfinder weighs it | Importing a general corroboration bar over-vetoes. Importing "one witness can suffice" under-vetoes, because that rule assumes a competent human observer. |

| Rule | Vetoes | Admits | Where the analogy breaks |
|---|---|---|---|
| Presenting complaint | Does not diagnose. Incompatible findings override it for conditions that have findings | Starts the differential; sets what to measure | Clinical default is to treat the complaint as care-relevant before it is verified. That default is beneficence toward a human patient, not an evidence rule. Copying it collapses Section 0's second error. |
| Patient-reported outcomes | Unvalidated instrument; wrong population or context of use | A defined endpoint after reliability, validity, and sensitivity to change are measured (FDA PRO guidance, 2009, **unverified**) | This is the closest analogy, and it still misleads if "validated against the construct" is read as "validated as experience." PRO validation assumes human report–experience coupling in the background. |
| Measurement | Self-report does not outrank a decisive contrary sign, lab, or image where one exists | Self-report selects the test; concordance raises practical weight | Absence of a meter is not a metre reading. For AI, "no probe yet" is not a negative finding, and a probe is not the system's own report (Ferrara: decodable intervention, chance report). |
| Mental-health case | Medical mimics, duration, impairment, and clinician judgment still constrain free narrative. A scale is not autobiography | Self-report is often the main instrument because the target is not otherwise observable | "Only instrument" is only-instrument inside a species whose coupling is presupposed, and usually via a validated scale. Necessity is not validation. Using it here would make unfalsifiability a reason to admit. |
| Malingering and symptom validity testing | Failed validity indicators can veto forensic reliance on a complaint (Slick criteria; effort tests such as TOMM, **unverified**) | Consistent effort plus other clinical data may leave the complaint standing, especially in treatment | These tests assume a subject who can experience the symptom and may strategically misreport it. Applied to AI denials, they convert non-report into deception. That is the over-claim test 9 forbids in the denial direction. |

**Model to adopt.** Validated PRO instruments, not hearsay and not the mental-health sole instrument. A report becomes data for a named use only after the instrument's link to the named object is measured for that class and system; it is then still not sufficient. Law supplies the use-rule after that measurement: interest goes to weight, never sufficient alone where the stake is status. Law does not supply the channel.

**Anaesthetic case.** It belongs. Under sub-question 3: an intervention that suppresses the reporting channel (drug, and by analogy disclaimer policy, refusal ablation, steering) makes silence uninformative. It constrains sub-question 5: absence of report is not evidence of absence. It does not answer sub-question 6. Medicine's own practice is mechanism plus monitors, with awareness under anaesthesia treated as a residual risk, not as disproved by silence (NAP5 / isolated forearm, **unverified**). The analogy misleads if monitors or "mechanism" are then treated as evidence of experience. Processed EEG does not settle human awareness either, and Anchor 2 already refuses the structure-to-experience premise.

## 3. The sentence
Confidence: high.

The sentence is not supported as written. The library holds a narrower, contested, steering-bound discrimination result. It does not hold the inference.

Clause map of the current sentence:
- "models can detect changes in their own internal states at above-chance rates" — purports to answer class (2), elicitation (3), and coupling (4). It overshoots all three. The verb should be "reports detecting" under the library's verb rule. The results are scored self-answers under injection or steering, model- and layer-specific, often low (Lindsey: about 20% identification at the optimum, failures the norm; Lederman: detection without reliable identification, apple confabulation, prompt-specific yes-bias; Macar: one instruct model, base models at chance). Ferrara: reports at chance in the small open-weight roster while a probe reads the intervention. Singh: the paradigms underdetermine privileged access and second-order computation. Prefill results are a different class (text edit, experimenter label), not detection of an internal-state change.
- "meaning self-reports track something real about processing" — purports to answer coupling (4) and use (5) for self-reports as a class. That "meaning" is not licensed. A score against an imposed label is not self-knowledge (README). A steered channel does not weight ordinary-operation reports (test 9). "Something real about processing" says more than the measurements support. It also says less than the library holds: it omits the probe–report dissociation, the detection–identification split, and the ordinary-operation gap.

Recommendation: **reword**. Severity: **HIGH**. Removing would dismiss narrowing measurements the dossier actually contains. Keeping would cite, as tracking, a result the library types as a scored self-answer under steering.

**Argument against:** the following sentences already refuse experience, standing, and the structure-to-experience premise, and "above-chance under injection" is a real narrowing result a legislator can be told in one clause; a long caveat may function as a quiet deletion.

Proposed wording, with sub-questions:

"Under activation interventions, some tested models report an imposed change above matched controls and identify it less often than they report detecting it; where quantified, failed reports are common, and in some smaller open-weight models the report is at chance while an external probe reads the intervention [class; elicitation; external criterion; error modes]. Those are scored self-answers under steering: they do not measure reports in ordinary operation, and they do not show that any state is experienced [use; experience]."

## 4. Test 9's rule against the breakdown
Confidence: medium.

The zero-weight rule survives for any report offered as evidence of an internal state or of its absence. The breakdown does not justify a softer rule for experience, preference, or ordinary present-state reports. It does show two classes the internal-state formula mis-sorts.

- **Experience reports, including denials** (AE Studio and similar, [T9]). Stay at zero. Steering that moves affirmation rates ([T9-steering]) shows a steerable channel only. What would move the class: a same-system link from that report to a pre-specified internal reading, a third-party transcript control that does not match the report, and trials fed a false account of the state (Q3 council standard), plus the mimicry controls test 9 already names. Not in the library. A trained perfect mapping (Ferrara LoRA) would still not be enough: it shows instrument sensitivity, not access.
- **Scored detection of an imposed internal event.** Already covered: admissible as data about the steered channel, weighted only by that measurement, silent on ordinary operation and on experience. No further weight is warranted. Ordinary-operation coupling for this class is not in the library.
- **Provenance (Q4).** Different rule already warranted, and it is not an inner-state rule. The object is an external fact the project holds. Measured accuracy may be used for identification reliability only. The record described in Q4 is unstable and often wrong, and the errors do not track capability, so it must not be indexed to strength (1.2) and must not be generalised to present-state reports (Q4 caveat ii). That record is not yet a claim-file measurement; the annex is unscheduled. Until it is tabulated and second-read, cite it as project history, not as a library finding. Zero internal-state weight remains correct, because provenance is not an internal state the model was shown to observe.
- **Authorship of an edited turn** (UK AISI prefill). The sentence-assignment rule already gives this class neither [T9] mark: the object is conversation text, not experience. Weight for prompted discrimination is the published scored accuracy; weight for spontaneous notice is the paper's near-zero continuation result; weight for an internal authorship monitor is zero — the authors say they do not identify the mechanism, and style cues drive flagging. Do not promote this class into introspection.

Recommendation: keep the inner-state rule intact; add an explicit class rider rather than stretch "internal state" to cover external facts. Severity: **HIGH**.

**Argument against:** class riders are a laundering route. A preference or "past action" label can be wrapped around an experience claim to escape zero weight. The September 2026 breadth is what blocks that. Any rider needs an anti-redescription clause, or the amendment fails test 9 by creating the exception it exists to forbid.

Symmetry for denials stays. The anaesthetic point is already the right reading of a null under suppression: it is not a measured negative coupling. Nothing in the breakdown warrants weighing denials differently from claims.

## 5. What the council needs to see
Confidence: medium.

No change to Section 9 or Anchor 2 on this sitting's say-so. Before advising text, the council needs three documents, in this order:

1. **Proposal document** for any wording change. Contents: full proposed sentences; the sub-question each clause answers; what the library holds, by claim id, for and against; two-error check in both directions; conflict disclosure; the strongest argument against; an anti-laundering clause if any class rider is proposed; a statement that the experience premise is not adopted. Not a review brief.
2. **Case-study annex** of the provenance rounds. Contents: model, round, claimed identity, routed id, right/wrong/declined; no capability ranking; uses limited to identification reliability; second-read against the survey notes. Q4 prose is not that annex.
3. **Topic page**, citing claim ids only, claims-as-of dated. Contents: detection without identification; probe–report dissociation; steering versus ordinary operation; what a scored self-answer is not. Claim set at least Lindsey c01, c02, c06; Lederman c01, c03, c06; Ferrara c01–c03; Macar c01; Singh c04–c06. No experience language.

Recommendation: do not draft constitutional text until those three exist. Severity: **MEDIUM**.

FINAL: sentence reword; test 9 rule needs classes; confidence medium

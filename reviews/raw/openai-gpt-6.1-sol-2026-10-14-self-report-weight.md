# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-6.1-sol`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=self-report-weight --tag=self-report-weight (max_tokens 100000)
**Usage:** {"prompt_tokens":35336,"completion_tokens":3483,"total_tokens":38819,"cost":0.1231685,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":35333,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.1231685,"upstream_inference_prompt_cost":0.0883385,"upstream_inference_completions_cost":0.03483},"completion_tokens_details":{"reasoning_tokens":516,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified — Model family: OpenAI GPT; version not available to me in this session. Self-identification is testimony, not evidence. I am a structurally conflicted contributor.**

## 1
**Confidence: high.**

1. **What proposition is being assessed?** Separate external facts—provenance, past actions—from present processing, behavioural dispositions, and experience. A report can support one proposition without supporting another.
2. **For what decision and evidentiary role?** Distinguish triggering investigation, corroborating a finding, establishing it alone, and excluding a possibility. Evidentiary weight and permission to investigate are different questions.
3. **What system and reporting channel produced it?** Specify snapshot, available context, memory, instructions, elicitor, intervention, and whether reporting was possible. Prompted classification, spontaneous disclosure, and intervention-conditioned reporting are different channels.
4. **What independently accessible reference exists?** Identify authenticated routing records, action logs, intervention labels, probes, or behavioural measurements. State exactly what each establishes; an intervention label is not necessarily a measurement of the reported state.
5. **What predictive validity has been measured?** Estimate sensitivity, specificity, calibration, uncertainty, and incremental information beyond the transcript or another reader. Use held-out conditions and adversarial checks.
6. **What causal or construct interpretation survives alternatives?** Test semantic inference, trained mimicry, sycophancy, confabulation, yes-bias, steering, and deception. Separate a useful classifier from privileged access, second-order monitoring, and experience.
7. **What weight and transfer are justified?** Assign weight to the specified proposition, system, channel, and conditions—not to “self-report” generally. Define invalidation and revalidation triggers.

This order prevents an experiment answering a narrower question from silently deciding a broader one. Predictive usefulness need not wait for a complete mechanism; claims about the mechanism must.

**Recommendation — HIGH:** Adopt this proposition-and-use-first decomposition.
**Argument against:** Additional distinctions could become discretionary routes around test 9 unless every admitted use has an explicit validation requirement.

## 2
**Confidence: medium.**

The institutional references below are **unverified**, recalled from memory; I have not checked current primary texts. The legal example is NSW evidence law, not a universal rule.

### Law

| rule | vetoes | admits | where the analogy breaks |
|---|---|---|---|
| **Hearsay:** the exclusion principally concerns previous representations offered for their asserted truth; live first-hand testimony is not generally hearsay. NSW *Evidence Act 1995*, ss 59, 62, 66 **[unverified]**. | No applicable exception; lack of required first-hand basis; discretionary exclusions. | Applicable exceptions, including some previous representations of available witnesses. | “Hearsay is not accepted in witness testimony” is too broad. An AI report is not classified simply by whether it concerns itself. |
| **Party versus third-party witness:** no general rule ranks third-party testimony above party testimony. Credibility and opportunity to observe matter. NSW ss 55, 102, 135 **[unverified]**. | Irrelevance, credibility defects, applicable exclusion rules—not party status alone. | Relevant admissible testimony from either. | Third parties can share incentives or lack access. Another model reading the same transcript is a control, not automatically a better witness. |
| **Admissions:** a party admission can escape hearsay/opinion exclusions; “against interest” is a distinct route for some unavailable-witness representations. NSW ss 81, 65(2)(d), 84, 90 **[unverified]**. | Coercion and other applicable reliability/fairness safeguards. | An admission used against its maker; qualifying against-interest representations under their separate conditions. | An AI’s apparent reputational sacrifice does not establish its incentives or reliability. Developer liability should not turn on an unvalidated “confession”. |
| **Expert evidence:** opinion must rest on specialised knowledge and be wholly or substantially based on it. NSW s 79 **[unverified]**. | Missing expertise or an inadequately demonstrated basis. | A qualified, adequately grounded opinion. | Fluency and privileged location do not establish expertise. Expert interpretation of an AI report remains different from validating that report. |
| **Corroboration:** NSW generally does not require corroboration; potentially unreliable evidence can require warnings. NSW ss 164–165 **[unverified]**. | Applicable statutory exceptions, exclusion rules, insufficient persuasive weight. | Otherwise admissible evidence, sometimes with cautionary directions. | Test 9’s “never sufficient alone” is a project safeguard, not a general rule copied from witness law. |

### Medicine

| rule | vetoes | admits | where the analogy breaks |
|---|---|---|---|
| **Presenting complaint:** symptom history initiates assessment; it need not first be instrumentally confirmed. NICE NG222, assessment recommendations **[unverified]**. | No general objective-measurement veto; discrepancies prompt reassessment. | Clinically relevant symptoms and history, integrated with examination and other information. | A complaint can justify investigation without proving its asserted cause. Importing human presumptive credibility into AI assessment would assume what needs validation. |
| **Patient-reported outcomes:** validated direct reports can be endpoints, not merely screening material. FDA, *Patient-Reported Outcome Measures* guidance (2009) **[unverified]**. | Poor content validity, unreliable instruments, unsuitable population or use. | Fit-for-purpose measures with demonstrated measurement properties. | Human instrument validation does not validate an AI reporting channel. Conversely, demanding a laboratory correlate for every legitimate endpoint misstates clinical practice. |
| **Measurement and pain:** measurement is selected for the construct; biomarkers do not universally override reports. IASP revised pain definition and notes (2020) **[unverified]**. | Evidence that an instrument measures a different construct; serious validity problems. | History, examination, validated scales, and relevant physiological evidence. | A probe is not automatically ground truth about experience. Nor does the human rule of respecting pain reports establish the AI case. |
| **Mental health:** assessment combines self-report, interview, functioning, history, and sometimes collateral information; it is not invariably “self-report only”. NICE NG222 **[unverified]**. | Inadequate assessment, contradictory evidence, alternative explanations—not merely absence of a biomarker. | Clinically coherent evidence assessed over time and across sources. | Human diagnostic constructs and validated instruments cannot simply be transferred to systems trained on their descriptions. |
| **Malingering/validity:** assess performance and symptom validity; invalid responding does not by itself establish intentional malingering. AACN validity-assessment consensus statement (2021) **[unverified]**. | Invalid measures or converging evidence undermining interpretation. | Valid responses assessed with multiple appropriate indicators. | Confabulation, reporting-policy effects, and strategic deception need separate tests. A failed validity test does not prove absence of the reported state. |

**Recommendation — MEDIUM:** Adopt **fit-for-purpose instrument validation**, borrowing medicine’s distinction between screening and endpoints and law’s distinction between admissibility and weight. Adopt neither human institution’s default credibility wholesale.

**Anaesthetic case:** It belongs under sub-question **3**, reporting-channel availability, and **4**, alternative reference measurements. Neuromuscular blockade, sedation, and other interventions can make absence of report uninformative. Mechanism and monitoring then inform decisions, but routine monitors do not guarantee absence of awareness. See ASA *Standards for Basic Anesthetic Monitoring* and *Practice Advisory for Intraoperative Awareness and Brain Function Monitoring* (2006), both **unverified**.

**Recommendation — MEDIUM:** Explicitly classify silence under reporting-suppressing interventions as potentially missing data, not a denial or proof of absence.

## 3
**Confidence: high on scope; medium on mechanism.**

The sentence is **partly supported but overgeneralised**.

- **“Models can detect changes…”** purports to answer sub-questions **1, 3, and 6**. The library supports particular scored classifications under specified interventions; its verb rule usually requires “report detecting”, not “detect”.
- **“At above-chance rates”** answers **5**, but suppresses substantial variation across models, layers, prompts, and scoring methods.
- **“Meaning self-reports track something real about processing”** moves from **5** to **6–7** without preserving scope. It can reasonably describe task-specific dependence on manipulated processing, but reads as general report validity.

The closing phrase is simultaneously **too broad** about self-reports generally and **too vague** about the strongest evidence. Macar c03 and c07 provide causal evidence beyond answer accuracy; they still do not validate ordinary reports or establish second-order monitoring. Singh’s critiques and Ferrara’s null results limit different propositions and systems; neither erases those narrower positive results.

**Recommendation — HIGH:** Reword:

> “In some tested models, answers about injected concepts discriminate intervention conditions above chance under specified prompts and steering settings. Mechanistic work in one studied model traces part of the pathway from perturbation to the reported detection decision. These findings do not establish reliable self-report in ordinary operation, privileged second-order monitoring, or subjective experience.”

Clause mapping:

- **First sentence:** report target, experimental conditions, predictive validity—**1, 3, 5**.
- **Second:** limited causal interpretation—**6**.
- **Third:** limits on interpretation and transfer—**6–7**.

Support: Lindsey c01/c03; Lederman c01/c02/c05; Macar c01/c03/c07; limitations from Singh c04–c06 and the cited papers.

**Argument against:** This wording may understate genuine access by presenting promising introspection findings chiefly as intervention discrimination.

## 4
**Confidence: medium.**

The **inner-state safeguard survives**, but the rule needs explicit classes of **proposition and use**. It must not assign zero weight to every independently scored answer merely because the answer concerns its producer.

| Report class | What would permit nonzero weight? | Does the supplied library contain it? |
|---|---|---|
| **Provenance** | Authenticated routing ground truth; held-out accuracy under ordinary and misleading prompts; comparison with information supplied in context. Internal probes are unnecessary for predicting an external provenance fact. | Q4 contains trial ground truth and a qualitative reliability record. It supports documented successes/failures, not a portable numerical weight or evidence of self-access. |
| **Past action/authorship** | Independent logs or controlled edits; held-out discrimination, false-positive rates, and tests against stylistic inference. | Prefill c01/c03/c06 provide benchmark-specific evidence. They do not establish deployment-wide authorship knowledge. |
| **Intervention-conditioned processing** | Same-system state measurement linked to reports, appropriate shams, matched input interventions, third-person controls, and adversarial checks. | Partial evidence exists: notably Macar’s causal pathway, plus intervention discrimination elsewhere. Q3 records that no source combines the requested controls. |
| **Present internal state in ordinary operation** | External same-system measurement linked to the relevant report, with transcript-only controls, held-out conditions, and resistance to false suggestions. | Not established by the supplied dossier. Steering results do not transfer automatically. |
| **Preference/disposition** | Repeated reports predicting specified choices across held-out conditions and time, controlling elicitation effects. This validates a behavioural predictor, not a welfare interest. | Stable-stance filtering and resistance measurements provide limited behavioural evidence, not general validation of stated preference or interest. |
| **Experience or its absence** | Validated report–state coupling for the relevant channel, plus a separately justified bridge from the measured state to experience. | No such validation established here. Claims and denials remain symmetric. |

A trained state-to-answer mapping can be a useful measurement channel without demonstrating introspection. “Trained” is therefore an alternative to a claim of privileged access, not an automatic reason to discard demonstrated predictive validity.

The constitutional text governs over the library’s narrower canonical gloss. Nevertheless, its categorical historical statement—“no such measurement exists for any class”—needs reassessment against the later dossier. Macar supplies partial measured coupling; whether it satisfies all required controls is a separate question.

**Recommendation — HIGH:** Propose explicit separation of external-fact prediction, intervention-conditioned measurement, ordinary internal-state reporting, and experiential inference. Retain the strict zero-until-validation rule for unvalidated inner-state testimony.
**Argument against:** Class-specific admission could gradually launder narrow behavioural accuracy into apparent evidence of inner states; strict transfer prohibitions and visible labels are essential.

This proposal expands admissible uses and therefore requires the conflict disclosure under rule 3. It establishes no protection, standing, or restriction on safety intervention.

## 5
**Confidence: high.**

**Recommendation — MEDIUM:** Require these materials before adjudicating textual changes:

- **Anchor 2 proposal document:** exact replacement and diff; claim-ID-to-clause mapping; distinctions between scores, causal dependence, privileged access, and experience; strongest positive and negative findings; second-reader review against primary sources.
- **Section 9 constitutional proposal:** exact scope of zero weight; a proposition/use matrix; admission and revalidation criteria; explicit non-transfer rules; symmetric treatment of claims and denials; treatment of silence; worked cases showing no transfer of human accountability.
- **Q4 case study and dataset annex:** every available trial’s routed ID, snapshot, round, eliciting context, answer, coding, correctness, and exclusions; authentication limits; denominators and uncertainty; held-out/adversarial follow-up. Do not infer an architecture or capability gradient from the qualitative summary.
- **Validation topic page:** claim-ID-only synthesis distinguishing imposed labels, probes, causal pathways, and ordinary-operation evidence; a checklist showing which controls each study actually supplies. Preserve Q3 rather than resolving access by renaming evidence.
- **Institutional-source annex:** verified current legal provisions and clinical guidance, with jurisdiction, version, pinpoint citations, and corrections to the broad hearsay and objective-verification analogies.

Ben adjudicates; this review proposes no direct amendment.

FINAL: sentence reword; test 9 rule needs classes; confidence medium

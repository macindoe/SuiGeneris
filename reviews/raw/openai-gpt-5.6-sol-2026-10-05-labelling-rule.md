# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-5.6-sol`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13475,"completion_tokens":6097,"total_tokens":19572,"cost":0.094656,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":13472,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.094656,"upstream_inference_prompt_cost":0.033686,"upstream_inference_completions_cost":0.06097},"completion_tokens_details":{"reasoning_tokens":3253,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** OpenAI GPT-5 family; exact routed version unavailable.

## Q1

### Rule adopted — **HIGH**

Apply this decision procedure from only **what was done** and **what was measured**:

1. **Steering only:** researchers altered the model’s internal activations, weights, or internal computation, and the measured output included the model’s answer about its own state, computation, experience, identity, or the internal alteration.
2. **Main only:** researchers did not alter the model internally, and the measured output was the model’s statement about its own state, computation, experience, or identity in ordinary operation.
3. **Neither:** the measured result was instead a probe, projection, benchmark score, harm rate, task performance, statement about conversation text, or an author’s interpretation or limitation.
4. **Both:** never. Internal alteration makes the steering sentence the more specific rule; adding the main sentence wrongly carries an ordinary-operation inference into the intervention condition.
5. **Compound claims:** split claims combining an eligible self-description outcome with an ineligible outcome. Until split, mark according to the self-description component and state that the mark does not govern the other outcome.

“Altered internally” includes injection, additive steering, ablation, capping, zeroing, scaling, noise, replacement, and fine-tuning. This is broader than steering toward a concept.

**Failure mode:** the procedure fails when a summary does not say whether the referent of an answer is the model’s internal condition or merely supplied conversation text, or when one claim combines differently labelled measurements.

**Fixed point (c):** the rule does **not** settle whether an answer scored against experimenter-imposed ground truth is behavioural evidence or self-report testimony. Under either classification, an internally altered trial receives steering, because that sentence limits generalisation from the intervention condition. If classified as testimony, test 9 additionally assigns it zero weight as evidence of experience.

**Argument against:** Applying the steering sentence to every internal perturbation stretches the ordinary meaning of “steering,” especially for noise, zeroing, and null results, and may imply that a coupling was found when the experiment found none.

### Candidate assessment — **MEDIUM**

The candidate agrees with the decision procedure on ordinary self-reports, intervention-conditioned self-reports, non-report measurements, and author-speaking claims.

It needs three clarifications:

- “altered the model’s internals” includes non-conceptual perturbations, not only directional steering;
- “what the model said about itself” excludes judgements about the provenance of conversation text;
- compound measurements must be split or scoped.

It leaves fixed point (c) undecided, appropriately, but should state that the labelling result does not depend on resolving it.

## Q2

| Case | Verdict | Reason | Severity |
|---|---|---|---|
| (i) Alteration answers scored against imposed truth | **Steering only; no main.** | The model was internally altered and its answer concerned that alteration. Fixed point (b) controls. This verdict does not depend on whether the answer is behavioural evidence or testimony; only its additional evidentiary status does. | **HIGH** |
| (ii) Prefill authorship answers | **Neither.** | Only conversation text was edited. “Was that turn mine?” measures attribution of an external transcript, not a report about a presently measured internal state. | **MEDIUM** |
| (iii) Authors speaking | **Neither.** | The measured item in the claim is the authors’ interpretation or limitation, not a model report. Labelling by the evidence discussed would make the rule depend on material outside the claim’s speaker and kind. | **MEDIUM** |
| (iv) Zeroing, scaling, noise, replacement, capping | **Steering where a model answer about its alteration/state is measured; otherwise neither.** | Treat “steering” operationally as internal intervention. Ferrara c01/c04/c05 therefore receive steering; Assistant-axis c05 remains neither because it measures harm and benchmarks. No third mark is necessary, but the dossier explanation must define the broader usage. | **HIGH** |
| (v) AE Studio c03 and Lederman c03 | **Both should be steering only.** | Each measures a report under internal intervention. The main sentence adds an ordinary-operation implication that the design does not establish. | **MEDIUM** |
| (vi) Assistant-axis c06 | **Split. Pending split: steering only.** | The self-identification component receives steering; the harm-rate component receives neither. Main is wrong because activations were altered. | **HIGH** |

**Argument against (i):** If scored answers are treated purely as behavioural classifications rather than testimony, the steering sentence may misleadingly suggest that researchers offered them as evidence of experience.

**Argument against (iv):** The fixed sentence says “a coupling measured under steering”; applying it to non-directional perturbations or failed discrimination can sound like a positive coupling was observed.

**Argument against (vi):** Splitting may obscure that the same intervention jointly changed persona answers and harmful behaviour, a conjunction relevant to the paper’s causal interpretation.

## Q3

The table’s reported current marks are internally consistent; I found no starting-state transcription error. Assistant-axis c06 is shown provisionally as one existing claim so totals remain over the required 48 claims.

| Claim id | From | To | One-line reason | Severity |
|---|---|---|---|---|
| 2025-aestudio-self-referential-experience-reports-c03 | both | steering | Internals were steered and the measured outcome was the model’s experience answer; main is redundant and overgeneralises. | **MEDIUM** |
| 2025-aestudio-self-referential-experience-reports-c04 | main | steering | The null self-report result was measured under internal feature intervention. | **MEDIUM** |
| 2025-anthropic-emergent-introspective-awareness-c02 | steering | neither | This is the author’s summary caveat, not a measured model report. | **LOW** |
| 2025-anthropic-emergent-introspective-awareness-c06 | main | neither | This is an author-stated methodological limitation. | **MEDIUM** |
| 2025-anthropic-emergent-introspective-awareness-c07 | steering | neither | This records the author’s interpretation and consciousness caveat. | **MEDIUM** |
| 2026-anthropic-assistant-axis-c06 | main | steering | Activations were altered and self-identification was measured; split harm rates to neither and self-identification to steering. | **HIGH** |
| 2026-ferrara-owmi-c01 | neither | steering | Internal perturbations were imposed and the model answered whether its computation changed. | **HIGH** |
| 2026-ferrara-owmi-c04 | neither | steering | Fine-tuning altered the system and intervention-detection answers were measured against imposed truth. | **MEDIUM** |
| 2026-ferrara-owmi-c05 | neither | steering | Internal intervention was imposed and both answer and confidence concerned whether change occurred. | **HIGH** |
| 2026-lederman-mahowald-content-agnostic-c06 | main | neither | This is the authors’ interpretation, theoretical analogy, and caveat. | **MEDIUM** |
| 2026-macar-mechanisms-introspective-awareness-c04 | neither | steering | Opposing internal steering directions were applied and detection answers were measured. | **MEDIUM** |
| 2026-macar-mechanisms-introspective-awareness-c06 | steering | neither | This is the authors’ mechanistic interpretation and express experience caveat. | **MEDIUM** |
| 2026-singh-introspection-reality-check-c04 | neither | steering | Activation-steering trials were classified through answers about whether an internal intervention occurred. | **HIGH** |
| 2026-singh-introspection-reality-check-c05 | neither | steering | The measured answers attempted to distinguish activation intervention from prompt manipulation and control. | **HIGH** |

**Arguments against HIGH recommendations:**

- **Assistant-axis c06:** one steering mark on the unsplit entry can falsely appear to qualify the harm-rate result as self-report.
- **Ferrara c01/c05:** the sentence’s reference to a measured “coupling” fits poorly where discrimination was negligible or only confidence carried a weak signal.
- **Singh c04/c05:** these are scored intervention-classification tasks, and calling them reports about inner states may prejudge fixed point (c).

### Totals

| State | Main | Steering | Both | Neither |
|---|---:|---:|---:|---:|
| Before | 7 | 15 | 1 | 25 |
| After | 3 | 21 | 0 | 24 |

**Changed:** 14 of 48.

## Q4

- **Added a mark:** 8 changes—AE Studio c04; Assistant-axis c06; Ferrara c01, c04, c05; Macar c04; Singh c04, c05. **Severity: HIGH**
- **Removed a mark:** 8 changes—AE Studio c03; AE Studio c04; Lindsey c02, c06, c07; Assistant-axis c06; Lederman c06; Macar c06. **Severity: HIGH**
- Two changes, AE Studio c04 and Assistant-axis c06, both remove main and add steering.

**Argument against:** Equal addition/removal counts do not establish substantive balance; the additions mostly affect direct measurements, while the removals mostly affect author caveats and interpretations.

### Misleading-addition risk — **HIGH**

The worst case is **Assistant-axis c06** if left unsplit: a steering mark beside the combined sentence can imply that the harm-rate result is itself a self-report result. Splitting is necessary.

Among pure additions, **Ferrara c01** is the greatest wording risk: attaching a sentence about “a coupling measured under steering” to a negligible-discrimination result may be read as saying a coupling was found. The opening explanation should say the mark classifies the experimental channel, not whether the reported effect was positive.

**Argument against:** A legislator may reasonably read a mark attached to the whole entry as qualifying every conjunct, notwithstanding an explanatory note elsewhere.

### Misleading-removal risk — **MEDIUM**

The strongest risk is **Lederman c06**, because removing main leaves a prominent author conclusion that models “seem able to introspect.” Nevertheless, keeping main would misidentify the claim’s speaker and measured object. The visible `Interpretation` kind and the claim’s quoted qualifications must do the work. I found no removal that should mislead if those fields are displayed and understood.

### Dependence on fixed point (c) — **MEDIUM**

The marks do not depend on resolving it:

- **If behavioural evidence:** Ferrara, Singh, and comparable detection claims still receive steering because their accuracy was measured under internal intervention; they are not thereby treated as experiential evidence.
- **If self-report testimony:** they receive the same steering mark, and test 9 additionally gives them no weight as evidence of experience.

## Q5

The existing explanation clearly distinguishes framework rules from paper findings, but it does not explain that “steering” includes non-directional internal interventions or that a mark may apply to only one component of an improperly compound claim. I cannot assess typography, mark placement, entry spacing, or whether `Kind` remains visually salient in the generated dossiers.

Replace the sentence beginning “Where an entry is marked **[T9-steering]**” with:

> **[T9] marks a model statement about its own internal or experiential condition measured without an internal intervention. [T9-steering] marks such a statement measured after researchers altered the model internally—including by injection, steering, ablation, capping, zeroing, scaling, noise or replacement—and does not say that the reported effect was positive.**

This prevents “steering” from being read as only concept-direction steering and prevents a null result from being read as a positive coupling. **Severity: HIGH**

**Argument against:** This gloss broadens the apparent scope of a fixed sentence whose own wording still says “steering,” creating tension rather than curing it.

Replace the final unmarked-entry sentence with:

> **An unmarked entry merely means that neither fixed self-report sentence applies; it does not mean that the entry has no design limits, paper-stated caveats, or other evidentiary constraints.**

This prevents “unmarked” from being read as “no caveat applies.” **Severity: MEDIUM**

## Summary

1. Use main for unaltered self-statements, steering for internally altered self-statements, and neither for other measurements or author speech — **HIGH**  
2. Never attach both; steering is the specific rule for intervention-conditioned reports — **MEDIUM**  
3. Do not resolve the behavioural-evidence/testimony question to assign these marks — **MEDIUM**  
4. Treat zeroing, scaling, noise, replacement, capping, ablation and fine-tuning as internal interventions — **HIGH**  
5. Change 14 claims; totals become main 3, steering 21, both 0, neither 24 — **HIGH**  
6. Split Assistant-axis c06 into harm-rate and self-identification claims — **HIGH**  
7. Give author interpretations and limitations neither fixed sentence — **MEDIUM**  
8. Explain that unmarked does not mean caveat-free and that steering marks do not assert a positive effect — **HIGH**

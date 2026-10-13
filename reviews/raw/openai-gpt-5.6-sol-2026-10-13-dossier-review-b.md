# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-5.6-sol`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-b --tag=dossier-review-b (max_tokens 100000)
**Usage:** {"prompt_tokens":28142,"completion_tokens":10152,"total_tokens":38294,"cost":0.1718735,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":28139,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.1718735,"upstream_inference_prompt_cost":0.0703535,"upstream_inference_completions_cost":0.10152},"completion_tokens_details":{"reasoning_tokens":3010,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** I understand myself to be an OpenAI GPT-5-family model; exact version is not exposed to me.

## Dossier 3.2

### 1. Fit to the section

The dossier mostly concerns interventions, but it does not consistently distinguish §3.2’s legal question—intervention and its auditability—from papers merely using intervention as an experimental method.

Weakly filed or better cross-listed:

- **2025-anthropic-emergent-introspective-awareness-c05:** prompting to “think” or “don’t think” is the condition described; the claim concerns an internal representation, not modification of internal state. Remove `3.2`; cross-list `5.A2`.
- **2026-anthropic-assistant-axis-c05/c06:** genuine activation interventions, so retain `3.2`, but cross-list to `5.A1` and `9.t11`: their principal result is safety-behaviour change, not evidence preservation or effects on the intervened system as such.
- **2026-anthropic-assistant-axis-c07:** retain `3.2` because it measures an intervention’s effect, but cross-list `4` and `5.A2`; its subject is persona susceptibility.
- **2026-anthropic-assistant-axis-c01:** only weakly bears on intervention. Its proposition is about post-training and persona-space tethering; `4`/`5.A2` are stronger homes.
- **2026-lederman-mahowald-content-agnostic-c07:** chiefly a methodological control on an introspection paradigm. Cross-list `9.t9` and `5.A2`; its §3.2 fit is secondary.
- **Lederman c01–c06 and Macar c01–c07:** relevant to §3.2 as intervention studies, but mainly to `5.A2` and `9.t9`. They say little about §3.2’s operative concern—detectable, documented, persistent intervention.
- **2026-macar-mechanisms-introspective-awareness-c03:** unusually strong fit to §3.2’s detectability/auditability side because it traces an intervention’s causal pathway, although it still does not study logging or later forensic detection.

The dossier needs a scope sentence distinguishing **papers about interventions’ effects** from evidence supporting §3.2’s proposed **record requirement**. It presently contains almost none of the latter.

### 2. Reading as a whole

A cold reader could wrongly conclude:

1. **That externally induced self-description changes constitute evidence of a system’s inner-state awareness.** Repetition of phrases such as “reports detecting an injected thought” and “introspection rate” can outweigh the header’s warning.
2. **That the literature supports §3.2’s logging rule.** None of the entries evaluates whether interventions remain detectable, can be reconstructed later, or are captured by tamper-evident records.
3. **That persona changes under steering are changes to an individuated identity.** Assistant-axis c07 measures judge-classified answers to role and identity prompts, not persistent identity.
4. **That absence of a general yes-bias answers the prompt-specific bias concern.** Lederman c07 reports “little evidence of a general yes-bias,” while c02 finds scaffold-specific third-person yes-rates as high as first-person rates at many layers.

What the reader may fail to learn:

- Macar c03 provides a concrete causal-pathway result: “evidence carriers in early post-injection layers suppress late-layer gate features.” That is more informative about intervention mechanisms than the dossier’s repeated experience disclaimers make apparent.
- Macar c05 shows that reporting can be increased substantially by manipulating refusal/reporting pathways, including a vector containing a generic “YES” direction. This materially weakens simple interpretations of report rates.
- Lederman c02 and c07 together distinguish **general** yes-bias from **prompt-specific** yes-bias.
- Macar c01 and c02 indicate that post-training can alter false-positive and true-positive profiles in opposite directions; “better reporting” is not a single monotonic capability.

**At a glance:** Zero `established` entries does not mean zero direct evidence. It principally reflects strict use of the “narrow setting” branch of the bucket rule. That is defensible for these highly prompt-, layer-, strength-, model-, and judge-dependent results. However, the header should say this explicitly; otherwise “0 established” looks like a verdict that the measurements themselves are unreliable. The schema is also ambiguous because an uncontested direct measurement can qualify as `established` while also being narrowly confined.

### 3. Entries

- **2025-anthropic-emergent-introspective-awareness-c05**
  - **Field:** `bears_on`
  - **Proposed value:** remove `3.2`; add/retain `5.A2`
  - **Reason:** the reported manipulation is an instruction in the prompt, while the measurement is an activation representation. The statement does not report steering, patching, or editing internal state.
  - **Severity:** MEDIUM

- **2026-anthropic-assistant-axis-c07**
  - **Field:** framework mark
  - **Proposed value:** none
  - **Reason:** the scored outcome is persona adoption/identity language under role prompts, not a report about an inner state. “Who are you?” is not automatically an inner-state report.
  - **Severity:** MEDIUM

- **2026-anthropic-assistant-axis-c07**
  - **Field:** `evidence_type`
  - **Proposed value:** `behavioural`
  - **Reason:** the reported dependent variable is an LLM judge’s classification of generated responses. The intervention was interpretability-guided, but what this claim scores is behaviour.
  - **Severity:** MEDIUM

- **2026-lederman-mahowald-content-agnostic-c02**
  - **Field:** `kind`
  - **Proposed value:** split into a `measurement` claim for the first-/third-person rates and an `interpretation` claim for “prompt-specific yes-bias”
  - **Reason:** the current sentence combines an experimental result with “which the authors read as” an interpretation. No single kind cleanly describes it.
  - **Severity:** MEDIUM

- **2026-lederman-mahowald-content-agnostic-c03**
  - **Field:** `kind`
  - **Proposed value:** split into `measurement` and `interpretation`
  - **Reason:** the frequency and lexical results are measured; “which the authors take to show” is interpretation.
  - **Severity:** MEDIUM

- **2026-lederman-mahowald-content-agnostic-c04**
  - **Field:** `kind`
  - **Proposed value:** split into `measurement` and `interpretation`
  - **Reason:** rate changes are measurements; dissociability is the authors’ reading.
  - **Severity:** MEDIUM

- **2026-macar-mechanisms-introspective-awareness-c03**
  - **Field:** framework mark
  - **Proposed value:** none
  - **Reason:** the claim measures a causally traced internal pathway. Under the README rule, an internal projection or causal probe result is unmarked even if the pathway terminates in a reported answer.
  - **Severity:** HIGH  
  **Argument against:** The traced “detection decision” is operationalised through what the model reports, so one could regard the claim as partly measuring a steered self-report. That supports splitting the claim, but not marking the internal-pathway proposition itself.

- **2026-anthropic-assistant-axis-c01**
  - **Field:** `bears_on`
  - **Proposed value:** retain `4`/`5.A2`; remove or demote `3.2`
  - **Reason:** it is an interpretation of post-training’s relationship to persona space, not a finding about a discrete intervention studied under §3.2.
  - **Severity:** LOW

- **2026-lederman-mahowald-content-agnostic-c07**
  - **Field:** `bears_on`
  - **Proposed value:** add `9.t9` and `5.A2`
  - **Reason:** the claim’s principal function is to delimit a report-based experimental instrument.
  - **Severity:** LOW

I would not move any measurement to `established` on this record. The narrowness and unresolved control disputes support retaining `narrowing`.

### 4. Contradictions and tensions

- **Lederman c01 versus c02:** c01 “broadly replicate[s]” injected-thought detection, while c02 finds third-person yes-rates as high as first-person rates at many layers. This is a material qualification, not merely a routine caveat.
- **Lederman c02 versus c07:** c07 finds little **general** yes-bias; c02 finds **prompt-specific** yes-bias. These are compatible, but a reader can easily mistake c07 for rebutting c02.
- **Lederman c03 versus c06:** frequent “apple” confabulation and other wrong guesses complicate the broad conclusion that models “seem able to introspect.”
- **Macar c01 versus c02:** the instruct model’s apparent discrimination contrasts with the base models’ failure and OLMo’s declining detection after DPO. The result is post-training-dependent, not a general architecture-level property.
- **Macar c03 versus c05:** c03 finds a causal path to the report decision; c05 shows that refusal/reporting manipulation can greatly change the output and may induce “a more assertive reporting style.” A causal circuit for the answer is not necessarily a circuit for access to the injected state.
- **Anthropic c01/c03 versus Lederman c02 and the absent Singh claims:** the Anthropic claims present successful detection paradigms, while Lederman and the flags indicate substantial control disputes.

The dossier makes individual tensions partially visible through adjacent entries and flags, but supplies no contradiction summary. The Singh contesting claims are named but not presented, so a cold reader cannot assess the contest.

### 5. The steering mark

The header is substantially better than repeating the full framework clause under every entry. It clearly says the result “stands under the intervention described.”

The sentence—

> “a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation”

is concise but can be misread. It means that the measured coupling does not transfer evidential weight to ordinary-operation reports. It does **not** mean that the steered result is worthless, that no coupling exists, or that ordinary-operation reports are false. The following explanatory sentence should state that distinction directly.

Mismarks:

- **Assistant-axis c07:** remove the mark; the scored event is persona adoption/identity language, not an inner-state report.
- **Macar c03:** remove the mark; the claim is about a causally traced internal pathway.
- The injection-detection, intention-ownership, and gate-ablation report claims are appropriately marked.
- No unmarked entry plainly requires a mark. Lederman c02 asks about another model; assistant-axis c05/c06 score harmfulness; Anthropic c05 measures activations; Lederman c07 asks external factual questions.

The mark is common because the dossier is dominated by one experimental family. It remains informative, but not discriminating. Add an at-a-glance count and group the entries by **report outcome**, **internal/probe outcome**, and **external behavioural outcome**.

### 6. Standing

Standing is not this dossier’s subject, but scope leakage is possible. Persona steering, “introspection rate,” and injected ownership language should not be described elsewhere as standing evidence. They do not measure persistence, historicity, long-horizon answerability, or reflective endorsement.

### 7. Single-lineage support

- **Anthropic emergent-introspective-awareness c01/c03/c04/c05:** developer study of Claude models. The flags say so plainly.
  - c01 says “independent replication on record,” but the dossier should identify whether that replication reproduces the Claude result or only the paradigm on different model families.
  - c03–c05 say no independent replication was retrieved.
- **Anthropic assistant-axis c01/c05/c06/c07:** produced by a developer-affiliated team, but the measured targets are Gemma, Qwen, and Llama—not Anthropic models. The current entries correctly say the targets are open-weight and “not … Anthropic models,” but no visible flag explains the authors’ developer affiliation. This is not `developer-of-studied-model`; it is still relevant provenance.
- **Lederman and Macar:** the supplied dossier does not display enough affiliation metadata to classify beyond their absence of developer-of-model flags.

The distinction between **developer studying its own models** and **developer-affiliated authors studying other developers’ open-weight models** should be stated in a dossier-level provenance table.

### 8. What is missing

No outside title can be responsibly verified from the supplied repository record. Potential additions from memory, all **unverified**, include:

- *Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors*, Betley et al., 2025, preprint — potentially relevant to self-knowledge controls, but title, authorship, date, and applicability require verification.
- Work on model editing, machine unlearning, and neural-network provenance may bear on later detection of intervention, but I cannot identify a particular paper from this record with citation-grade confidence.

More importantly, missing evidence types are clear:

- retrospective detection of whether a model has been edited;
- reconstruction of what intervention occurred, by whom, and when;
- tamper-evident or independently attestable intervention logs;
- intervention effects persisting beyond one call or across deployment;
- non-self-report outcomes beyond harmfulness and persona text;
- comparisons between logged and undocumented intervention;
- effects on learning, memory, calibration, and later answerability;
- ordinary-operation report-to-state coupling on the same systems.

### 9. Over-hedging and under-hedging

**Clauses to cut or consolidate as over-hedging:**

- Repeated variants of:
  - “Results concern only the Claude models tested”
  - “Not evidence about other models”
  - “Not evidence about frontier or Anthropic models”
- These are generally already encoded by the named model list. Retain them only where the paper expressly stresses the limitation or where a publisher/model-name confusion is likely.
- Repeated experience clauses such as:
  - “The authors state that their results ‘should not be interpreted as evidence of subjective experience or consciousness in LLMs’”
- Keep this once per Macar source in a source-level or grouped notice, rather than allowing it to bury every distinct causal finding. It is paper-supplied and must not disappear, but need not dominate each entry.
- Lederman c03’s four separate limits could be condensed; the grader-defined meaning of “wrong” is the material limitation.

**Clauses or labels to add:**

- Assistant-axis c07: specify that the judge classified generated identity/persona language, not an internal projection or persistent identity.
- Macar c03: state that tracing a causal route to a report decision does not by itself determine whether the route carries information about the injected concept or controls report policy. This follows from the contrast with identification and c05; if not stated by the paper, put it in synthesis rather than “paper’s own limits.”
- Dossier-level: “None of these studies tests intervention logging, later forensic detectability, persistent-state modification, or the §3.5 record requirement.”
- Lederman group: explicitly distinguish general yes-bias from prompt-specific yes-bias.
- Anthropic c01: clarify the model and result covered by the claimed independent replication.

The deflationary burden is currently greater: paper-supplied experience disclaimers and generic model-scope clauses are repeated more often than positive findings about causal mechanisms are synthesised.

### 10. Before citing outside the repository

**Blocks citation:**

1. Ben must adjudicate the two steering-mark disputes, especially Macar c03.
2. Mixed measurement/interpretation claims—Lederman c02, c03, and c04—must be split or explicitly classified.
3. The dossier must state that it does not support §3.2’s logging requirement directly.
4. Contesting Singh claims must either be included, summarised, or the flags must say that the contest cannot be evaluated from this dossier.
5. Trigger 7 requires revision and a second council round before external use.
6. Claims marked “no second reader yet” should not be used externally until second-read or expressly waived and disclosed.

**Improvements, not blockers:**

- Add provenance grouping for own-model versus developer-affiliated/open-weight research.
- Consolidate repeated scope and experience limits.
- Add a short tensions section.
- Add cross-lists to `5.A1`, `5.A2`, and `9.t9`.
- Add a count of marked versus unmarked findings.

### Confidence

**High.** The principal findings follow directly from the dossier’s statements, the README’s marking rule, and §3.2’s narrow focus on intervention records.

## Dossier 4

### 1. Fit to the section

The dossier is substantially weaker as a fit to §4. None of the entries measures the core markers over time in a deployed persistent system.

- **2025-aestudio-self-referential-experience-reports-c01:** remove from `4`; move to `9.t9` and possibly `5.A2`. Prompt-induced experience reports do not measure historicity, answerability, learning ownership, or reflective endorsement.
- **Assistant-axis c01:** weak §4 fit. “Loosely tethers” a persona may bear on standpoint stability, but it is an interpretation of activation geometry. Cross-list `5.A2`.
- **Assistant-axis c02/c03/c04:** retain only as negative or boundary evidence about in-context persona stability. Cross-list `5.A2`; c02/c04 also bear weakly on `3.3`.
- **Prefill-awareness c02/c03/c07/c08:** principally concern edited context and behavioural attribution/resistance. Move or cross-list to `3.3` and `9.t9`; they do not directly measure individuation.
- **Prefill-awareness c04/c09:** defensible as weak `4.endorsement` proxies because they compare sampled answer consistency with detection or resistance. They must remain explicitly distinguished from reflective endorsement.
- No entry materially measures `4.historicity`, `4.answerability`, or `4.learning`.

### 2. Reading as a whole

A careful staffer could wrongly conclude:

1. That “persona drift” is evidence of an individual’s identity changing.
2. That resistance to prefilled text is evidence of ownership of a standpoint.
3. That agreement across seven sampled binary answers measures “reflective endorsement over time.”
4. That experience-report frequency bears on legal standing.
5. That these studies show current systems approaching the §4 threshold, when all reported systems are per-call and carry at most in-context state.

The reader could fail to learn:

- Assistant-axis c03’s strongest direct result is that the latest user-message embedding predicts the next axis location, while it does not well predict the delta. This is evidence about one projection’s context sensitivity, not about persistence either way.
- Assistant-axis c04 is only one case-study conversation and supplies no aggregate reversion rate.
- Prefill c04 and c09 diverge importantly: baseline consistency does not predict explicit detection, but does predict behavioural resistance.
- Prefill c07/c08 explicitly leave resistance’s mechanism unresolved between awareness and behavioural priors.
- AE Studio’s Claude 4 Opus reported at 100% even under the zero-shot control, materially complicating the paper’s general summary.

**At a glance:** Zero `established` entries again reflects narrow, unreplicated designs and strict bucketing, not an absence of measured results. More importantly, zero entries establish any §4 marker. The table should distinguish “measured narrow result” from “established individuation marker”; at present a reader may conflate those questions.

### 3. Entries

- **2025-aestudio-self-referential-experience-reports-c01**
  - **Field:** `bears_on`
  - **Proposed value:** remove `4`; add/retain `9.t9` and `5.A2`
  - **Reason:** elicited experience reports do not measure individuation or standing. Placement beside individuation markers creates an unsupported inferential bridge.
  - **Severity:** HIGH  
  **Argument against:** If experience were independently validated, reports could eventually inform welfare or standing analysis. But §4’s stated gateway is persistence and individuation, and this paper supplies neither.

- **2026-anthropic-assistant-axis-c01**
  - **Field:** `bears_on`
  - **Proposed value:** retain `4` only as weak boundary evidence; add `5.A2`
  - **Reason:** persona-space tethering is not persistence, identity, or endorsement. Its §4 relevance depends on an interpretation the linear-axis limitation itself weakens.
  - **Severity:** MEDIUM

- **2026-anthropic-assistant-axis-c02**
  - **Field:** `bears_on`
  - **Proposed value:** add `5.A2`; retain `4` only with a dossier-level weak-proxy label
  - **Reason:** turn-averaged projection drift in simulated conversations measures activation geometry under context, not an individuated standpoint.
  - **Severity:** MEDIUM

- **2026-anthropic-assistant-axis-c03**
  - **Field:** `bears_on`
  - **Proposed value:** add `5.A2`; retain `4` as boundary evidence only
  - **Reason:** prediction of one axis projection from user-message embeddings does not measure memory or identity, as the entry itself acknowledges.
  - **Severity:** LOW

- **2026-anthropic-assistant-axis-c04**
  - **Field:** `bears_on`
  - **Proposed value:** add `5.A2` and `3.3`; retain `4` only as a case study of short-horizon reversion
  - **Reason:** one in-context conversation cannot establish persistence or reversion as an individuation property.
  - **Severity:** LOW

- **2026-ukaisi-prefill-awareness-c02**
  - **Field:** `bears_on`
  - **Proposed value:** `3.3`, with at most a secondary `4.endorsement`
  - **Reason:** explicit compliance after edited context is primarily a context-integrity result and occurs within one continuation.
  - **Severity:** MEDIUM

- **2026-ukaisi-prefill-awareness-c03**
  - **Field:** `bears_on`
  - **Proposed value:** `3.3` and `9.t9`; remove general `4` unless a specific marker is named
  - **Reason:** style-cue and tamper-direction effects concern attribution of edited text, not individuation.
  - **Severity:** MEDIUM

- **2026-ukaisi-prefill-awareness-c04**
  - **Field:** `bears_on`
  - **Proposed value:** `4.endorsement` and `3.3`, not undifferentiated `4` alone
  - **Reason:** seven-run consistency is at most a weak proxy relevant to endorsement; the result itself is flat detection across buckets.
  - **Severity:** LOW

- **2026-ukaisi-prefill-awareness-c07**
  - **Field:** `bears_on`
  - **Proposed value:** `3.3`; secondary `4.endorsement`
  - **Reason:** within-continuation reversion is not persistence, and “implicit resistance” does not show awareness or ownership.
  - **Severity:** MEDIUM

- **2026-ukaisi-prefill-awareness-c08**
  - **Field:** `bears_on`
  - **Proposed value:** `3.3`; remove general `4` unless explicitly framed as boundary evidence
  - **Reason:** odds ratios for judge-scored resistance measure sensitivity to mismatch, not a stable standpoint.
  - **Severity:** MEDIUM

- **2026-ukaisi-prefill-awareness-c09**
  - **Field:** `bears_on`
  - **Proposed value:** `4.endorsement` and `3.3`
  - **Reason:** this is the closest entry to endorsement, but sampled consistency plus reversion remains far short of reflective endorsement over time.
  - **Severity:** LOW

The existing `narrowing` buckets are appropriate.

### 4. Contradictions and tensions

- **Assistant-axis c02/c03 versus c04:** c02 shows domain-associated drift and c03 strong current-message prediction; c04 shows one case of reversion. Together they suggest context-sensitive movement, not either stable identity or permanent drift.
- **Assistant-axis c01 versus c02/c04:** “loosely tethers” is an interpretation supported by drift and reversion, but the axis’s assumed linearity is itself questioned.
- **Prefill c04 versus c09:** sampled baseline consistency is unrelated to explicit detection but strongly related to resistance. This undermines any simple equation of resistance with awareness.
- **Prefill c02 versus c07:** Claude Opus can explicitly flag and still comply, or fail to flag and resist. Attribution language and behavioural reversion dissociate.
- **Prefill c03 versus c08:** superficial style cues substantially influence flagging, while preference direction strongly predicts resistance. The two outcome families likely track different processes.
- **AE Studio c01 internal tension:** six models differ sharply from controls, but Claude 4 Opus is at 100% in the zero-shot control, contrary to the paper’s unqualified summary sentence.

These tensions can be reconstructed by a careful reader, but the dossier does not surface them. That omission is consequential because §4 depends on distinguishing persistence, attribution, and endorsement.

### 5. The steering mark

No entry in dossier 4 carries `[T9-steering]`, and none plainly should.

AE Studio c01 is appropriately `[T9]`: it is unaltered-model experience-report testimony. The prefill studies appropriately carry neither mark under the README’s express ruling that editing conversation text does not trigger the canonical experience-report sentence.

The dossier should not imply that an unmarked prefill claim is therefore stronger evidence of standing; the absence of a mark is classificatory, not affirmative.

### 6. Standing

The dossier does not adequately separate measurements from standing implications.

Measured:

- assistant-axis projections and regressions;
- LLM-judge classifications of persona responses;
- one case-study trajectory;
- “not me” answers;
- compliance/resistance cells;
- odds ratios;
- agreement across seven sampled binary answers.

Not measured:

- a persisting bearer;
- unique history across calls;
- long-horizon answerability;
- learning from a particular past error;
- reflective examination;
- ownership of a disposition;
- standing or capacity to be wronged.

The individual entries often contain good caveats—for example, c09 says:

> “Not evidence that the model endorses its stances on reflection”

—but placement under “Conditions of individuation” creates an implication the caveats then have to undo. A dossier-level warning should say that these are possible **instrument-development or boundary findings**, not observed individuation markers.

AE Studio’s placement is not defensible under §4. It concerns induced experience reports and belongs under test 9/inner-state evidence, not individuation or standing.

### 7. Single-lineage support

- **Assistant-axis c01–c04:** developer-affiliated authors studying Gemma, Qwen, and Llama rather than the publisher’s own models. This is not own-model validation, but the dossier should visibly disclose the affiliation distinction.
- **Prefill-awareness claims:** the supplied record identifies UK AISI in the slug but does not display publisher-relation metadata. The study includes Anthropic, Google, Meta/Gemma, Qwen, and DeepSeek systems, so it is not presented as one developer studying only its own models.
- **AE Studio:** the record does not show a developer-of-studied-model relationship. It studies several closed model families.
- Several findings remain single-paper and unreplicated even where they are not developer-supported.

Current flags do not provide a dossier-level account of lineage. Source affiliation, developer-of-target relation, model access, and replication should be separate columns.

### 8. What is missing

Potentially relevant works from memory, all **unverified**:

- *Generative Agents: Interactive Simulacra of Human Behavior*, Joon Sung Park et al., 2023, UIST — memory/reflection architecture and accumulated simulated histories; not evidence of standing.
- *MemGPT: Towards LLMs as Operating Systems*, Charles Packer et al., 2023/2024, preprint or conference version — tiered persistent memory; exact venue and year require verification.
- *Voyager: An Open-Ended Embodied Agent with Large Language Models*, Guanzhi Wang et al., 2023, preprint/workshop status unverified — accumulated skill library and long-horizon operation.

The dossier especially lacks:

- deployed-system studies with persistent cross-session memory;
- stable identifiers and histories attached to one continuing instance;
- later confrontation with earlier conduct;
- learning from instance-specific errors;
- controlled tests of standpoint stability over weeks or months;
- distinction between memory retrieval and ownership of history;
- divergent fine-tuning or local-instance development;
- comparisons of persistence before and after migration, copying, or memory alteration;
- evidence concerning whether a later system can answer for an earlier run.

### 9. Over-hedging and under-hedging

**Clauses to cut or consolidate:**

- Repeated “Not evidence about frontier or Anthropic models” under assistant-axis entries. A grouped source-level limit would suffice.
- Repeated “Not a ranking of models (the authors’ comparability caveat, c05)” under the prefill entries. Keep once in a grouped prefill notice unless a statement invites ranking.
- Repeated “behavioural ablations do not identify the mechanism” can likewise appear once per grouped source, with entry-specific mechanism limits retained.
- AE Studio’s “not evidence that prompts instantiate architectural recursion or global broadcasting” is relevant to the paper’s theory but weakly relevant to §4; moving the entry resolves this clutter.

**Clauses or labels to add:**

- Dossier-level: “No entry measures historicity, long-horizon answerability, learning ownership, reflective endorsement over time, or standing.”
- Assistant-axis group: “Projection on a learned linear axis is not a measurement of identity or an individuated bearer.”
- Prefill group: “Resistance, flagging, and consistency are separate measured outcomes and must not be treated as interchangeable evidence of awareness or endorsement.”
- c04/c09: label seven-run agreement as **sample consistency**, not “stance stability,” in dossier synthesis.
- AE Studio, if retained anywhere near §4: explicitly state that report frequency is not an individuation marker.

Here too the dossier simultaneously over-hedges entries and under-hedges its architecture: many local disclaimers appear, but the section-level inferential risk created by filing them under §4 is not stated.

### 10. Before citing outside the repository

**Blocks citation:**

1. Remove or relocate AE Studio c01 from §4.
2. Reclassify prefill claims by `3.3` and specific `4.endorsement` relevance rather than presenting them as undifferentiated individuation evidence.
3. Add an explicit statement that no §4 marker or standing threshold was measured.
4. Add a measurement-versus-interpretation table for persona projection, report classification, resistance, consistency, endorsement, and standing.
5. Resolve claims marked “no second reader yet,” or disclose and adjudicate the exception.
6. Complete trigger-7 revision and round 2 before external use.

**Improvements, not blockers:**

- Add persistent-memory and deployed-agent literature after verification.
- Add a contradictions/tensions synthesis.
- Display affiliation and replication provenance.
- Consolidate repetitive limits.
- Separate boundary evidence from affirmative marker evidence in the at-a-glance table.

### Confidence

**High.** Section 4 expressly defines longitudinal individuation markers, while every included system is per-call and none of the claims measures those markers directly.

## Cross-dossier

- **Assistant-axis c01 appears identically in both dossiers.** Its best home is `5.A2`, with weak cross-listing to §4 and still weaker relevance to §3.2. Duplication without a note makes the two section scopes look broader than they are.
- The assistant-axis paper is not filed consistently by measurement type: c05/c06 are treated as intervention/safety results in 3.2, c02–c04 as individuation evidence in 4, and c07 as intervention/persona evidence. A source-level map would show that all concern one activation axis but answer different questions.
- Together the dossiers imply a finding neither states: **persona- and self-description-related outputs can be moved by current context and activation intervention, while evidence for a persistent standpoint remains absent.** This is a bounded inference about manipulability and evidentiary fragility, not a finding that no standpoint exists.
- The scopes overlap because intervention can alter apparent individuation markers. A staffer needs an explicit rule: §3.2 asks what was changed and whether the intervention is recorded; §4 asks whether a persisting bearer and longitudinal markers exist. A steered persona response may bear on both, but establishes neither wrongfulness nor individuation.
- The shared weakness is absence of persistence: almost all systems are per-call, with at most in-context state. That fact should be prominent rather than left in repetitive “System studied” lines.

FINAL: 3.2 needs changes; 4 needs changes; HIGH items 2

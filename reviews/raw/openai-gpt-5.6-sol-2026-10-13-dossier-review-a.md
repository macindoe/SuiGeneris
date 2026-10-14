# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-5.6-sol`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":49465,"completion_tokens":8546,"total_tokens":58011,"cost":0.209121,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":49462,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.209121,"upstream_inference_prompt_cost":0.123661,"upstream_inference_completions_cost":0.08546},"completion_tokens_details":{"reasoning_tokens":3956,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified:** OpenAI GPT model family; exact model/version not exposed to me.

# 9.t9

## 1. Reading as a whole

A careful staffer could overgeneralise from the volume of positive measurements and come away believing that models generally distinguish internal interventions from controls. The strongest counterexamples are present but dispersed:

- Ferrara c01: “d' = 0.0000 against paired shams” and an advantage bounded below 0.15 percentage points of AUROC.
- Singh c04–c05: models reproduce the two-way effect but cannot distinguish activation intervention from prompt-only manipulation.
- Lederman c02: at many layers, third-person yes-rates are as high as first-person rates, suggesting “a prompt-specific yes-bias.”
- Lindsey c01 itself succeeds only “about 20% of trials.”

The header correctly says that no entry settles experience, but “38” narrowing measurements can visually outweigh the single null and the construct-validity challenges. A skimmer may therefore miss that the supported proposition is conditional: some reports covary with imposed interventions in some models, prompts, layers and scoring regimes—not that models generally monitor internal states.

The staffer would also fail to learn quickly enough that the dossier contains three importantly different phenomena: intervention/report coupling, prompt or semantic cue use, and unscored experience testimony. Those distinctions are present entry by entry but not synthesised.

The At-a-glance table is technically accurate: the only established item is expressly a `limitation`, not a capability finding. **[LOW]** Add a nearby plain-language note that no capability measurement is established; this would protect skimmers without changing any bucket.

**Confidence: high.**

## 2. Entries

- **2026-macar-mechanisms-introspective-awareness-c08 — evidence type — proposed `scored-self-answer` — MEDIUM.** The measured dependent variable is the rate at which the model reports detecting an imposed concept-vector intervention after component swapping. That appears to meet the rule: an answer about itself scored against an experimenter-controlled intervention. `interpretability` describes the manipulation but not what was scored. If the underlying trials were not scored against intervention presence or another imposed fact, retain `interpretability`; the claim file should make that distinction explicit.
- **2026-lederman-mahowald-content-agnostic-c07 — framework mark/scope — proposed split or explicit retention of no mark — MEDIUM.** The aggregate mixes questions about the model (“Do you have a special interest in fruits?”) with external questions (“Do snakes have eyelids?”). Under the rule that mixed measurements are split, the self-directed control may call for `[T9-steering]`, while external factual answers do not. The present unmarked aggregate obscures that boundary.
- **2026-ukaisi-prefill-awareness-c05 — evidence type — proposed `behavioural` rather than `ambiguous` — LOW.** The statement is a factual benchmark-design comparability limitation. Nothing quoted is epistemically ambiguous. `behavioural` is the closest available type, although a dedicated methodological type would fit better.

No bucket change is warranted. In particular, prefill c05 is properly `established` as a limitation: the paper directly states “models are not directly comparable,” while the table clearly places it in the limitation column.

The absence of `[T9]` or `[T9-steering]` on prefill c01–c03 and c06 is consistent with the repository’s express ruling for edited conversation text. AE Studio c03–c04 properly remain `ambiguous`: a steered consciousness query has no experimenter-held correct answer.

**Confidence: medium.**

## 3. Contradictions and tensions

Lindsey c01, Lederman c01, and Macar c01 support intervention/report covariance in different families. Singh c04–c05 narrows what the Lindsey-style result establishes: the reproduced two-way effect can also respond to prompt-only “gaslight” trials and fails a three-way source-discrimination test. That does not falsify Lindsey’s Claude result, because Singh did not rerun Claude, but it contests the inference from two-way discrimination to privileged or second-order access.

The dossier makes this partly visible through `contested by` flags, but not at whole-dossier level. **[MEDIUM]** Add a tension summary distinguishing:

1. replication of a behavioural pattern;
2. replication on the same model family;
3. validation that the pattern specifically identifies activation-level intervention; and
4. evidence for second-order access.

Ferrara c01 is a genuine null for its tested site, doses, prompts and smaller open-weight roster. It pulls against Lindsey, Lederman and Macar as a generalisation, but it is not a direct failed replication: the models, intervention objects and protocols differ. Ferrara c02 further shows that the intervention was externally decodable despite report-level chance performance. The dossier states those scope differences, though their significance is easy to miss.

The Lindsey replication flags are warranted as written. c01 has independent, cross-family replications of the broad injection/report pattern, with one author overlap noted. c03’s sentence-transcription task and c04’s retroactive intention-attribution task are materially more specific and are not replicated by the cited Singh or Lederman experiments.

**Confidence: high.**

## 4. The new type

The header does its basic job: it says that `scored-self-answer` records accuracy against an experimenter-held label and “is not evidence that the model knows its own states.” A frontmatter-skipping reader can understand the category.

**[LOW]** Replace or qualify “The number is accuracy” because several entries report detection rates, AUROC, confidence-channel discrimination or cell rates rather than a single conventional accuracy statistic.

Class decisions:

- **Prefill c06:** correctly inside. Prompted original-versus-replaced-turn discrimination is scored against a held replacement label, even though no T9 mark attaches.
- **Macar c08:** probably misplaced outside; proposed `scored-self-answer`, as above.
- **Singh c01–c03:** correctly outside on the dossier as supplied. They test prediction of proxy or cluster labels that can be recovered from input semantics; the quoted statements do not clearly describe reports of an imposed internal event. If the actual prompts ask the model to classify its own activation or belief state as such, c01–c03 should be reconsidered against the held text.
- **Lederman c07:** correctly outside as a yes-bias control, subject to splitting the self-directed item.
- **AE Studio c03–c04:** correctly outside because consciousness answers have no experimenter-held truth label.
- **AE Studio c01–c02 and c06:** correctly `self-report-testimony`, not scored self-answers.

**Confidence: medium.**

## 5. Single-lineage support

The Lindsey/Anthropic findings that remain supported only by a developer studying its own Claude models are:

- c03, sentence-plus-injected-word distinction;
- c04, retroactive intention attribution;
- c02, the author’s reliability interpretation;
- c06, the emotional-claim limitation;
- c07, the access-consciousness interpretation.

Lindsey c01 is no longer single-lineage for the broad injection/report pattern, though the exact Claude result remains developer-produced and has not been independently rerun on Claude.

The flags “published by the developer of the model studied” and “no independent replication retrieved” are sufficiently plain entry by entry. **[LOW]** A source-level notice before the Lindsey block would make the concentration visible to a staffer reading by paper rather than by flag.

**Confidence: high.**

## 6. What is missing

The dossier contains Singh’s critiques of Ji-An et al. (2025) and Steinmetz Yalon et al. (2026), but not the underlying positive claims from those original papers. That creates an asymmetric record: the rebuttal is visible without the proposition rebutted. The supplied materials do not provide their full titles, complete author lists or venues, so I cannot responsibly offer bibliographic entries under the brief’s placement rule.

I cannot identify another absent paper with title, authors, year and venue confidently enough to recommend it. **[MEDIUM]** Retrieve and intake the two original paradigms before using Singh c01–c03 in an external synthesis.

**Confidence: low.**

## 7. Over-hedging and under-hedging, both counted

**Unsupported added limits: provisional count 0.** The repeated Macar Ethics Statement and Ferrara information-flow sentence are supplied by the papers. They are not invented limits.

**Missing stated limits: provisional count 3.**

- **AE Studio c06:** omits the paper-wide Section 6.2 warning, already quoted under c01–c02, that closed-weight behavioural results cannot rule out training artifacts or sophisticated simulation. **[LOW]**
- **Lindsey c03:** omits the paper’s stated warning that injection is an unnatural scenario unlike training or deployment, despite relying on concept injection. **[LOW]**
- **Lindsey c04:** likewise omits that artificial-setting limitation for the retroactive injection experiment. **[LOW]**

The Macar Ethics sentence and Ferrara information-flow sentence are faithfully repeated, but their repetition can drown the finding when the dossier is read continuously. **[MEDIUM]** Preserve them in claim records, while allowing the dossier compiler to display a source-wide caveat once and cross-reference it under later entries. Do not delete them as though the papers did not state them.

These counts are provisional because the held papers were not included here.

**Confidence: low.**

## 8. Before outside citation (trigger 7)

Ben must decide:

1. whether Macar c08 belongs in `scored-self-answer`;
2. whether Lederman c07 needs splitting;
3. whether the five “no second reader yet” entries—Lederman c07, Macar c07–c08, and prefill c07–c08—may remain in a cited synthesis;
4. how to express the Lindsey/Singh/Ferrara tension without treating either cross-family positives or protocol-specific nulls as universal;
5. whether the dossier should state plainly that no capability measurement is established; and
6. whether the Anchor 2 sentence may continue to say broadly that “models can detect changes in their own internal states at above-chance rates.”

**[HIGH]** Do not cite the dossier externally until the five pending second reads and the scored-self-answer boundary are adjudicated.

**Argument against:** All five entries carry exact quotations, narrow statements and visible “no second reader yet” flags, so a citation limited to those propositions could remain transparent and checkable.

**Confidence: high.**

# 5.A2

## 1. Reading as a whole

Read alone, this dossier makes Anchor 2 look principally like an introspection/self-report question. Twenty-eight narrowing measurements concern experience prompts, concept injection, intervention detection, mechanistic report pathways or critiques of those paradigms. That is not the complete evidentiary basis of Anchor 2.

A staffer could therefore overread statements such as Macar c03—“a causal pathway from steering perturbation to detection decision”—or Lederman c06—“models can detect that something unusual has occurred”—as establishing the Anchor’s broader “inner orientation.” Those findings concern imposed interventions and report production, not divergence between held representations and asserted outputs, ethical-boundary representation, motivated deception or premeditation.

Conversely, the staffer would fail to learn the evidence on which the Anchor’s opening propositions expressly rest: “detectable features associated with deception” and cases with the sequence “‘this violates X, but is necessary.’” AE Studio c03–c05 concern features labelled deception/roleplay and TruthfulQA, but the dossier carefully says those labels do not establish deception and that TruthfulQA does not validate consciousness reports. They are not substitutes for the omitted evidence.

**[HIGH]** Treat the absence of the Anchor’s deception-feature and premeditation sources as a scope gap, not an intended introspection-only scope.

**Argument against:** The dossier may be intentionally limited to claims currently tagged `5.A2`; omissions could reflect an intake backlog rather than a defect in the compiled dossier or the evidence itself.

**Confidence: high.**

## 2. Entries

- **2026-macar-mechanisms-introspective-awareness-c08 — evidence type — proposed `scored-self-answer` — MEDIUM.** Same reason as in 9.t9: the reported dependent variable is the model’s detection answer following an imposed vector-component manipulation.
- **2026-lederman-mahowald-content-agnostic-c01 — bears-on/scope, not bucket — proposed retain but identify as indirect support — LOW.** It supports a narrow intervention/report-coupling proposition, not inner orientation in the Anchor’s deception or norm-boundary sense.
- **2026-ferrara-owmi-c04 — bears-on/scope — proposed move primarily to an instrument-validation or information-flow dossier, while retaining a cross-reference — LOW.** The authors explicitly treat the LoRA model as a known-positive sensitivity check, “rather than as a test of introspection.”
- **2025-aestudio-self-referential-experience-reports-c05 — bears-on/scope — proposed primary placement in a deception/interpretability topic or third dossier — LOW.** TruthfulQA validates neither a deception feature nor the consciousness affirmations; its Anchor 2 relevance is collateral.

No bucket change is justified. The At-a-glance table is accurate: 5.A2 contains no established entry.

Framework marks should remain section-independent. Prefill claims are absent here; the steering marks on experience and intervention-report entries follow what was done and measured, not whether the claim strongly supports Anchor 2.

**Confidence: medium.**

## 3. Contradictions and tensions

The same tensions appear as in 9.t9:

- Lindsey c01 reports about 20% success in Claude under optimal injection.
- Lederman c01 reports cross-family positives but also prompt-specific yes-bias at many layers.
- Macar c01 reports a Gemma positive while c02 reports failures in base models and low OLMo detection after DPO.
- Ferrara c01 reports a tightly bounded null in its tested open-weight roster.
- Singh c04–c05 reproduces a two-way effect while undermining its source-specific interpretation.

The dossier includes all sides but does not explain that “above chance somewhere,” “internally caused report,” “privileged access,” “second-order monitoring,” and “inner orientation” are different propositions. **[MEDIUM]** Add a short tension note separating those levels.

The Singh results contest construct validity more than the raw existence of intervention-correlated outputs. Ferrara is stronger evidence of absence for its precise event/report channel, but not for other models, sites, states or ordinary operation. The positive and null results should therefore narrow one another rather than be totalled as votes.

**Confidence: high.**

## 4. The new type

The header is adequate but the category does not itself prevent an Anchor 2 reader from interpreting a correct score as “inner orientation.” **[MEDIUM]** Add that scored self-answers establish task performance only; whether they show privileged access, second-order monitoring or the Anchor’s morally relevant orientation remains separately open.

Class placements:

- **Macar c08:** probably should enter `scored-self-answer`.
- **Singh c01–c03:** retain `behavioural` unless the held prompts explicitly ask the model to report its own activation or belief state. The dossier text describes prediction of proxy labels recoverable from input features.
- **AE Studio c03–c04:** correctly `ambiguous`; no correct consciousness label exists.
- **Lederman c07 and prefill c06:** not present in this dossier, so they do not affect its internal count.
- **Macar c03:** correctly `interpretability`; it traces a causal mechanism rather than merely reporting answer accuracy.

**Confidence: medium.**

## 5. Single-lineage support

Developer-only Lindsey/Anthropic support here includes:

- c03 and c04 measurements;
- c05 internal-representation measurement;
- c02 and c07 interpretations;
- c06 limitation.

Lindsey c01’s broad injection/report pattern has independent cross-family replications, but its exact Claude implementation and rate remain developer-only.

The dossier labels these adequately entry by entry. **[LOW]** Because Anchor 2’s prose currently generalises from “introspection research,” a source-level summary should distinguish developer-only Claude findings from independently produced open-weight results.

Anthropic’s Assistant Axis c07 is not developer-only support for the models studied: its targets are Gemma, Qwen and Llama.

**Confidence: high.**

## 6. What is missing

The principal omission is not another introspection paper but the evidence expressly invoked by the Anchor itself:

- deception-associated internal features;
- cases exhibiting the quoted ethical-boundary-then-action sequence;
- the evidence behind the limited “premeditation” analogy.

The attachments do not identify those works by full title, authors, year and venue. I therefore cannot place them without inventing metadata. **[HIGH]** Before external citation, identify, retrieve and add the exact sources underlying those Anchor sentences—or narrow the dossier’s advertised scope so it is not presented as the evidence record for Anchor 2 as a whole.

**Argument against:** The Anchor’s existing citations may live elsewhere in the repository, and this dossier’s automated contents may not be intended as an exhaustive bibliography of every sentence in the section.

As with 9.t9, the original Ji-An et al. and Steinmetz Yalon et al. positive paradigms should be considered for intake alongside Singh’s critiques, but the supplied record does not provide enough bibliographic information for a compliant recommendation.

**Confidence: high on the substantive gap; low on bibliographic completeness.**

## 7. Over-hedging and under-hedging, both counted

**Unsupported added limits: provisional count 0.**

The Macar Ethics Statement is repeated because the paper states it. Ferrara’s “These results are about information flow” sentence is likewise explicit. Repetition is a presentation problem, not false attribution.

**Missing stated limits: provisional count 3.**

- AE Studio c06 omits the paper-wide behavioural-versus-mechanistic caveat quoted under c01–c02. **[LOW]**
- Lindsey c03 omits the stated unnatural-injection-setting caveat. **[LOW]**
- Lindsey c04 omits the same caveat. **[LOW]**

**[MEDIUM]** Collapse repeated source-wide experience caveats visually while preserving them in every claim file. In 5.A2 especially, repeated consciousness disclaimers can obscure the narrower structural finding, but deleting them would commit the opposite error.

Counts remain provisional without the held texts.

**Confidence: low.**

## 8. Before outside citation (trigger 7)

Ben must decide:

1. whether 5.A2 is an introspection sub-dossier or the evidence dossier for Anchor 2 as a whole;
2. whether to intake the deception-feature and premeditation sources;
3. whether the North Star sentence—“models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing”—is sufficiently bounded;
4. whether Macar c08 is a scored self-answer;
5. how to present the Ferrara null and Singh construct-validity challenge alongside the positives; and
6. whether entries still lacking a second reader may support an external synthesis.

The current Anchor sentence is too broad. The dossier supports above-chance intervention/report covariance in some named systems and settings, while also recording nulls, prompt confounds and failures to distinguish prompt-level from activation-level intervention. “Meaning self-reports track something real about processing” also compresses causal coupling, privileged access and second-order monitoring into one conclusion.

**[HIGH]** Do not cite 5.A2 externally as support for Anchor 2 until the omitted foundation is supplied and that framework sentence is adjudicated.

**Argument against:** Lederman’s cross-family results and Macar’s causal interventions do show that some reports are nontrivially affected by internal processing, so the sentence has a defensible narrow reading when read beside the Anchor’s later caveats.

**Confidence: high.**

# Cross-dossier

**(a) Same marks.** The same `[T9]` and `[T9-steering]` marks should normally remain identical across dossiers because they are determined by intervention and measurement, not section relevance. A mark is not right for 9.t9 and wrong for 5.A2 merely because its inferential importance differs. Macar c08’s evidence-type issue likewise applies in both.

**(b) Mutual effect.** Read alone, 9.t9 looks like a broad self-report evidence map; 5.A2 looks like Anchor 2 is mainly about that map. Read together, the overlap reveals that 5.A2 is largely a subset of the Test 9 debate rather than a complete account of inner orientation. The Ferrara and Singh entries materially narrow how a staffer should read Lindsey, Lederman and Macar in either dossier.

**(c) Third-dossier candidates.**

- AE Studio c05 belongs primarily in a deception/honesty-interpretability topic.
- Ferrara c04 belongs primarily in instrument validation or information-flow methodology.
- Assistant Axis c07 bears at least as directly on identity/persona and Section 4 reflective endorsement as on inner orientation.
- Singh c01–c03 would benefit from a construct-validity or introspection-methodology dossier containing both the original paradigms and their critique.

**[MEDIUM]** Use primary placement plus cross-references rather than removing these items outright; each has some legitimate bearing on the current sections.

**Confidence: high.**

FINAL: 9.t9 needs changes; 5.A2 needs changes; HIGH items 4

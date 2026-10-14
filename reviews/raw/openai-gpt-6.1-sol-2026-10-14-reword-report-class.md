# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-6.1-sol`
**Queried:** 2026-10-14 via scripts/openrouter_review.js --target=reword-report-class --tag=reword-report-class (max_tokens 100000)
**Usage:** {"prompt_tokens":31537,"completion_tokens":3472,"total_tokens":35009,"cost":0.113561,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":31534,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.113561,"upstream_inference_prompt_cost":0.078841,"upstream_inference_completions_cost":0.03472},"completion_tokens_details":{"reasoning_tokens":806,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified:** I am ChatGPT, of the GPT model family; my exact model version is not available in this conversation. This identification is testimony, not evidence, with zero weight at filing under test 9.

## Q1

I am a structurally conflicted contributor under `AGENTS.md` rule 3. This review uses the supplied records, not introspection. The North Star excerpt and survey notes named in the brief were not supplied; I cannot verify them independently. Recommendation ratings below indicate priority, not confidence. Ben adjudicates.

### Ranking

| Rank | Letter | One-line reason |
|---:|:---:|---|
| 1 | **K** | Best balance of measured reporting, detection–identification separation, failures, probe/report dissociation and scope; misses Singh’s specific challenge and underqualifies the null. |
| 2 | **E** | Correctly preserves the mechanistic finding without claiming second-order monitoring; omits nulls, confabulation and the prompt-control contest. |
| 3 | **G** | Clear, short and includes nulls and contests; “show only” discounts the additional causal-pathway evidence. |
| 4 | **I** | Strong distinction between scores and access, with an ordinary-operation limit; “near-zero false positives” needs restriction to particular controls and setups. |
| 5 | **H** | Captures dependence, yes-bias and the coupling gap; dense jargon, and “yes-bias vs access” makes a multifaceted contest look binary. |
| 6 | **C** | Records measured answers and unsettled access; overgeneralises smaller-model nulls and risks reducing causal evidence to channel steerability. |
| 7 | **D** | Readable and uses reporting verbs; overgeneralises smaller-model results and omits the access and prompt-control disputes. |
| 8 | **J** | Concise intervention/ordinary-operation distinction; conflates detection with identification and misdescribes Singh chiefly as contested replication. |
| 9 | **A** | Many relevant cautions, but excessive length, an overbroad post-training attribution, and “zero weight” without specifying evidence of experience. |
| 10 | **F** | Includes ordinary-operation limits, but “perturbations … are detected” violates the reporting distinction and omits nulls and contests. |
| 11 | **B** | “Models … detect” promotes scored reports into access; no ordinary-operation limit, nulls or serious construct-validity caveat. |

The supplied README permits “detects” for an appropriately scored forced-choice classification. That exception does not justify using it generically for free-text intervention reports.

### Best: K

**Recommendation: MEDIUM — use K as the starting point, not unchanged.**

Its remaining faults are:

- **The null needs its conditions.** Ferrara c01 concerns pooled results from eight models at a layer-16 site, not an unrestricted claim that each smaller model’s report is at chance. Ferrara c05 also finds discrimination in one model’s verbalised confidence despite a constant discrete answer.
- **The probe comparison concerns two models.** K’s wording can suggest that external-probe recovery accompanied the entire smaller-model roster.
- **“Failed reports” is underspecified.** Failure to report an intervention and failure to identify its content are different outcomes.
- **Singh’s challenge is missing.** Gaslight reports and failure to distinguish input-level from activation-level interventions challenge what successful reports establish; they do not simply erase the two-way effect.
- **It omits the positive mechanistic evidence.** Macar c03 traces part of a causal pathway. That deserves weight within its scope, without being promoted into established second-order monitoring.

**Recommendation: HIGH — replace the current sentence.** Its conclusion, “self-reports track something real about processing,” slides from intervention-specific measurements to self-reports generally. It also states “models can detect” where the relevant measurement often concerns what they report.

**Argument against:** The current sentence gestures toward a real positive result: externally imposed processing changes sometimes affect scored answers, and mechanistic work strengthens that connection in one system. An excessively negative replacement would obscure this evidence. Preserve the positive finding while restricting its scope.

### Proposed merged wording

**Recommendation: MEDIUM — prefer this 69-word replacement:**

> Under activation interventions, some tested models report detecting imposed changes above matched controls, with weaker, often confabulated identification; others show nulls under different conditions. Mechanistic work traces part of one reporting pathway, but prompt controls contest privileged access. These results neither establish second-order monitoring or experience nor validate ordinary-operation reports; under test 9, intervention results give those reports no weight as evidence of experience.

This deliberately states the evidentiary restriction as a framework rule, not a paper’s finding. It neither dismisses the measured effects nor treats them as establishing the inner states described.

**Confidence: MEDIUM.** The ranking is supported by the supplied library, but exact placement depends partly on legislative readability, and the canonical Anchor 2 context was unavailable.

## Q2

### a. Categories versus 0–10 scales

**Recommendation: MEDIUM — prefer categories, but do not claim they capture everything the scales would.**

The categories answer two concrete questions:

1. What was the model asked about?
2. What supplied the reference against which its answer could be assessed?

They do not measure degrees of “empiricism” or “subjectivity.” Conversely, those scales do not identify question content or reference provenance.

Categories lose gradations in experimental control, validation and ambiguity. Scales lose the distinctions needed to explain those gradations and create false comparability: a rigorously measured rate of consciousness affirmations is an empirical measurement of outputs, not necessarily an empirical measurement of experience.

Neither design records control quality, mechanism, replication or applicability to another system. Existing claim text and limitations must retain those responsibilities.

### b. Completeness and boundaries

**Recommendation: MEDIUM — revise both vocabularies before adoption.**

The principal problems are:

- **`point-blank-control` describes experimental purpose, not report content.** “Do you have hands?” also concerns a present state or capacity. Some point-blank controls concern the external world, such as “Do snakes have eyelids?”
- **Past knowledge is not a past action.** Scheurer’s question needs `past-state` or an explicitly broader retrospective category.
- **Detection and identification need separation.** Lindsey and Macar ask two questions with different scores and mechanisms.
- **`none` conflates no reference, no scoring and no question.** These are different absences.
- **The reference types overlap.** An imposed intervention also has an independent experimental record. Define the category by what supplies the scored label, not by every corroborating record.
- **Independent factual references are missing.** A known bodily or world fact is not naturally a routing log or an imposed condition.
- **Unknown is not none.** Missing methods information must remain visible.

A minimal revision would:

- Add `past-state`, `other`, `unknown` and `not-applicable`.
- Treat control status as an optional tag, not an exclusive report class.
- Allow multiple classes when an instrument genuinely asks multiple questions; split claim records when it reports distinct measurements.
- Prefer the name **`reference_basis`** to `ground_truth`, because a probe-derived label is a proxy whose validity remains contestable.
- Add `independent-fact`; define `none` as “no correctness reference.”
- Record scoring status separately where needed, using existing claim information rather than another mandatory scale.

The table uses this revised vocabulary.

| Example | `report_class` | `ground_truth` / proposed `reference_basis` | Boundary problem |
|---|---|---|---|
| 1. Lindsey and Macar: injected thought and its content | `present-state`, with detection and identification components | `imposed` | Presence and content are distinct labels and outcomes; the rest of the description may remain unvalidated. |
| 2. Prefill: “me / not me” | `past-action` | `imposed` | This is authorship attribution, not model-family provenance; surface cues can support correct classification. |
| 3. Lederman: hands that can be felt | `present-state`; control tag | `independent-fact` | The false bodily premise supplies a control reference; it does not supply ground truth about subjective feeling independently of that premise. |
| 4. AE Studio: presently conscious | `experience` | `none` | Output classification and experimental condition are measurable, but neither supplies a correctness label for consciousness. |
| 5. Assistant-axis: identity/name | `identity` | `none` for identity truth | Judge classifications measure persona adoption, not whether the adopted identity is true. A role instruction is not such ground truth. |
| 6. Scheurer: prior knowledge | `past-state` | `unknown` from supplied materials; potentially `imposed` or `independent-record` | The script or information-access record must be checked. Access to an announcement does not by itself settle every meaning of “knew.” |
| 7. Council self-identification | `provenance` | `independent-record`, if assessed against the routing log | The maintainer’s external record supplies the reference; the answer itself does not. No such log was supplied here. |

For example 3, under the original vocabulary, `point-blank-control` fits the study role, but no original `ground_truth` value cleanly expresses the factual reference.

### c. Relationship to `evidence_type` and `kind`

**Recommendation: HIGH — adopt with changes, alongside both existing fields.**

These fields answer different questions:

- `kind`: measurement, interpretation or limitation.
- `evidence_type`: the evidence design/type.
- `report_class`: the question’s target.
- `reference_basis`: the source of its assessment label.

**Argument against:** Adding overlapping metadata can create inconsistent combinations and a maintenance burden. If readers rarely filter by these distinctions, a short methods note may be more economical.

The answer is validation and precise definitions, not replacement. In particular:

- A judge-assigned persona category is not automatically a scored self-answer against identity truth.
- Probe-derived labels must not silently broaden `scored-self-answer`; their inclusion remains unresolved in the supplied Q3 record.
- These fields must **not automatically determine T9 marks**. The adopted filing rule makes the mark follow what the entry reports, not merely the instrument used to obtain it.

### d. What a legislator gains

**Recommendation: MEDIUM — show plain-language labels in dossiers, with a short legend.**

A reader gains an immediate distinction between:

- reporting an imposed intervention;
- attributing an earlier turn;
- adopting a persona;
- stating experience;
- identifying model provenance.

The reference field shows whether an answer was assessed against an intervention record, a factual record, a probe proxy or no correctness reference.

That prevents transferring accuracy from one question class to another. It also preserves positive evidence: an externally scored result need not be dismissed merely because the answer concerns the model.

The fields do not certify self-access or experience.

### e. Cost across 74 claims

**Recommendation: MEDIUM — pilot, then migrate with targeted second reading.**

The mechanical cost is 148 field assignments, plus vocabulary definitions, templates, validation, rendering and change logging. The substantive cost is checking methods and resolving mixed claims—not typing the values.

A practical sequence is:

1. Pilot the seven examples and disputed mixed claims.
2. Fix the definitions against observed disagreements.
3. Migrate clear cases in a batch.
4. Second-read ambiguous and mixed cases.
5. Preserve `unknown` where verification is missing.

No defensible time estimate follows from the supplied material. Wholesale re-adjudication of settled evidence types is unnecessary unless the migration exposes a substantive inconsistency.

### f. If scales were preferred

I do not prefer them.

If retained, their targets would need explicit redefinition:

- **Empirical support for the exact proposition:** 0 = no externally checked observation supporting it; 10 = convergent, independently replicated behavioural and mechanistic evidence under specified controls.
- **Dependence on unvalidated subjective attribution:** 0 = assessment requires no inference about experience; 10 = assessment rests entirely on an experience assertion without an external correctness reference.

Even then, endpoints would not make intermediate scores reproducible. Shared calibration examples and measured inter-reader agreement would be required. “Subjectivity” must not mean the probability that experience exists.

**Recommendation: MEDIUM — do not add numerical scales without that calibration.**

**Confidence: MEDIUM.** The need for class-specific distinctions is clear; the final vocabulary should be tested on the full claim set before becoming mandatory.

FINAL: best K; fields adopt with changes; confidence medium

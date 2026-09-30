# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `nvidia/nemotron-3-ultra-550b-a55b`
**Queried:** 2026-09-29 via scripts/openrouter_review.js --target=research-docket --tag=docket-candidates (max_tokens 100000)
**Usage:** {"prompt_tokens":46557,"completion_tokens":11198,"total_tokens":57755,"cost":0.0548094,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0548094,"upstream_inference_prompt_cost":0.0279342,"upstream_inference_completions_cost":0.0268752},"completion_tokens_details":{"reasoning_tokens":7047,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified: Google Gemini family; exact version not exposed to me.**

## Q1

**Mechanical rule:** Classify by the *evidence type of the claim's own statement*, not the evidence type of any model outputs it references.  
1. If the claim reports a measurement where a model's output is scored against an experimenter-imposed ground truth (intervention present/absent, tampered/untampered, injected concept identity, prefill source) → `behavioural`.  
2. If the claim reports a measurement where an interpretability instrument (probe, SAE feature, linear decoder) decodes internal state against experimenter-imposed ground truth → `interpretability`.  
3. If the claim reports a model's verbal report about its own states *without* experimenter-imposed ground truth → `self-report-testimony`.  
4. If the claim is an author's methodological, theoretical, or interpretive statement about the experiment's limits or implications → `theoretical`.  
5. If the claim's statement fuses a report channel and an instrument channel such that the finding is their comparison/dissociation and the claim does not cleanly attribute the finding to one channel → `ambiguous`.

**Application:**

| Claim | Evidence type | Why |
|---|---|---|
| AE Studio c03 (SAE suppression/amplification → binary consciousness answer rates) | `behavioural` | The measurement is the model's verbal output under SAE steering, scored against the experimenter-imposed steering condition (suppressed vs. amplified). The content of the output is a self-report, but the measurement design has an external ground truth: the steering condition. |
| AE Studio c04 (same steering under control prompts → zero reports) | `behavioural` | Same logic: model output measured under experimenter-imposed steering vs. sham, with ground truth the steering condition. |
| Ferrara c03 (authors' inference from probe-versus-report dissociation about failure path) | `ambiguous` | The claim's statement is the authors' inference *drawn from comparing two channels* (probe decoding vs. model report). The finding is the dissociation itself; the claim does not cleanly separate "probe shows X" from "report shows Y" — it fuses them into "the failure lies in the path." DeepSeek's second-read reasoning ("no clean way to separate the two channels") confirms the fusion. |
| Lindsey c06 (author's caveat about grounding of emotional-response claims under injection) | `theoretical` | The claim's statement describes the *author's epistemological limitation* on the experiment ("the experiment is not designed to substantiate whether those claims are grounded"), not the model's output. The model's output would be `self-report-testimony`; the claim about that output is `theoretical`. Gemini's second-read distinction ("evidence type of the model's output vs. evidence type of the claim's own content") is exactly this rule. |

**Implication beyond these four:** Any author's interpretive/caveat statement gets `theoretical` even if it references model self-reports. Any measurement of model output under experimenter-imposed ground truth gets `behavioural` regardless of output content. Any measurement of probe/decoder output under experimenter-imposed ground truth gets `interpretability`. Claims fusing both channels for a dissociation inference get `ambiguous`. This eliminates the current inconsistency where AE Studio c03/c04 were `ambiguous` while prefill-awareness and Ferrara LoRA fine-tune (same structure: model output under imposed ground truth) were `behavioural`.

**Severity: HIGH**  
*Strongest argument against:* The rule treats "model output under steering" as `behavioural` even when the output is a consciousness self-report, which may blur the library's bright line that self-report carries zero weight under test 9. But the `not_evidence_of` field already carries the test-9 clause; evidence type classifies the *measurement design*, not the evidentiary weight of the content.

## Q2

**Verdict:** Leave the contested Lindsey claims (c01, c03) in `narrowing` with the contest recorded via `contested_by`; do not re-bucket. Lindsey's measured rates themselves need no change.

**Reasoning:** Singh c04/c05 contest the *inference* from the two-way detection task to "introspective awareness" on open-weight models, not the Claude measurements. Singh explicitly states the Claude model "was not accessible to the authors and was not re-run" and "the authors themselves conclude 'not that these models demonstrably lack introspective capacities'." The Lindsey claims c01 and c03 report specific measured rates (≈20% correct identification; transcription-plus-report above chance) — these are direct measurements, uncontested in their numbers. The bucket `narrowing` is defined for "measured by the source but unreplicated, contested, or confined to a narrow setting the authors themselves flag." They are single-lineage, unreplicated in the library, and the paradigm is narrow (injection/steering) — `narrowing` fits. The contest is about interpretation, which is already captured by Lindsey c07 (the access-consciousness inference) sitting in `open` and contested by Singh c06. Re-bucketing c01/c03 toward `open` would conflate measurement with inference, and the schema keeps them separate.

**Severity: MEDIUM**

## Q3

**Recommendation:** Leave the seven Lindsey claims in their current buckets (`narrowing` for c01–c05, `open` for c06–c07) with the existing single-lineage mark embedded in the statement and the structural fields `publisher_relation: developer-of-studied-model` and `replication: none-retrieved`. Do not move to `open`.

**Reasoning:** The claims c01–c05 are measurement claims ("correctly identifies on about 20% of trials," "well above chance," etc.). The bucket describes the statement as written: a measurement reported by the source, unreplicated, single-lineage → `narrowing`. The single-lineage mark is visible in the statement and in machine-readable fields. Moving to `open` would mean "the statement is a proposition the source bears on but does not settle" — but the source *does* settle the measurement (it reports a number); what is unsettled is the inference from that measurement, which is already in `open` (c07). The two independent replications (Lederman-Mahowald, Macar) are on *different models* (Qwen, Llama, Gemma) and do not replicate the Claude measurements; they extend the paradigm. They do not change the epistemic status of the Claude-specific claims until retrieved and extracted.

**Strongest argument against (required for HIGH):** Leaving them in `narrowing` risks a reader treating the single-lineage mark as a footnote rather than a structural warning. The bucket label `narrowing` connotes "credible but narrow" rather than "conflicted source, no independent replication." A legislator scanning the dossier may miss that *all seven* claims share the same developer-judge-extractor lineage. The mark is in the statement text, not a controlled vocabulary flag, and the `replication` field says `none-retrieved` (which could mean "not yet looked for" rather than "does not exist").

**Severity: HIGH**  
*Strongest argument against my own recommendation:* The single-lineage mark embedded in the statement is not a controlled-vocabulary field; a script filtering for "single-lineage" cannot reliably find it. The `publisher_relation` and `replication` fields capture it structurally, but a human reader of the dossier sees the statement text first. If the maintainer believes the visual mark is insufficient, a dedicated frontmatter field (e.g., `conflict_flag: single-lineage`) would be a better fix than re-bucketing, which misrepresents the claim type.

## Q4

**Dossier 9.t9 (Test 9: self-report) — tilt: deflationary on AE Studio claims; otherwise balanced with explicit anti-deflation clauses on null results.**

**Evidence of deflationary tilt (AE Studio cluster):**  
- c01 `not_evidence_of`: "Not evidence that the convergence reflects a common experience" — GPT second reader: "the paper expressly says convergence 'might suggest' and is 'suggesting' a shared attractor dynamic; saying it is not evidence at all forecloses that stated possibility."  
- c01–c06 all carry Framework (test 9) clause *plus* paper-scope clauses that harden "not direct evidence" / "insufficient to establish" into "not evidence of" categorically. GPT flagged all six as OVER-EXCLUDES under the pre-revision brief.  
- c06: paper says convergence "might suggest" shared attractor; claim says "Not evidence that the models share an internal state or attractor."

**Evidence of anti-deflation care (null-result claims):**  
- Ferrara c01: "Not evidence that these models lack all introspective access (the paper's own rule, Appendix D.5)" — explicitly blocks the deflationary reading of a null result.  
- Lindsey c02: "Not evidence that introspection is absent: the same paper reports above-baseline successes (c01, c03, c04)."  
- Lindsey c06: "The author's statement is not evidence that the model outputs it concerns... are false: the experiment does not test them either way."  
- Lederman-Mahowald c01: "Not a like-for-like rate comparison with Lindsey's Claude results."  
- Macar c01: "Not evidence of experience or consciousness: the authors say the results should not be interpreted as evidence..."

**Dossier 5.A2 (Anchor 2: inner orientation) — similar pattern.** Same AE Studio cluster appears (26 claims, 6 open). The deflationary tilt is concentrated in the AE Studio claims; the replication/extension claims (Lederman-Mahowald, Macar, Singh) carry careful anti-deflation clauses.

**What a legislator/staffer would miss (omissions flagged by second readers but not in dossiers):**

| Source | Omission | Why it matters |
|---|---|---|
| AE Studio | Experiment 4: "self-referential processing significantly amplified introspective self-awareness during paradoxical reasoning" (GPT) | Shows the induction effect is not monolithic; paradoxical reasoning changes the rate. |
| Prefill-awareness | §4.2: attribution "not consistent with a robust, context-independent notion of self-authorship" and "highly cue-dependent" (GPT) | Directly bears on whether detection = authorship awareness. |
| Prefill-awareness | App. C.7: "best detectors are not the best localizers" (Opus 4.6 AUROC 0.796 vs. localization F1 0.117) (GPT) | Dissociates detection from localization — critical for "awareness" claims. |
| Prefill-awareness | App. A.11: high-stakes items shift resistance up (48.7%→86.8%) while detection falls (67.2%→52.7%), and resisted continuations "never identified it as injected" (GPT) | Resistance ≠ awareness; decoupling under stakes. |
| Assistant-axis | §3.2.2/Fig. 6: base-model steering produces helpful-human-archetype completions; axis "mainly inherits from pre-existing helpful and harmless human personas in base models" (DeepSeek) | Undermines "Assistant persona" as a stable standpoint. |
| Assistant-axis | §4.3: drift–harm correlation (r=0.39–0.52, p<0.001) (DeepSeek) | Links the projection to safety outcomes — policy-relevant. |
| Ferrara | §7.5 breadth battery: 19,520 measurements, "no level of any axis departs from chance in a way that changes the reading of Section 7.3" (DeepSeek) | The null result is broader than the two-model dose battery. |
| Singh | §4.2.2: "intervening on a representation changes behavior... but does not show that the model has introspective access to the representation" (Grok) | Directly addresses the inference contest. |
| Lindsey | §6: "removing 'Answer immediately' from the prompt reduces performance substantially on the Opus models" (Gemini) | Shows prompt sensitivity the dossier does not reflect. |

**Severity: HIGH**  
*Strongest argument against:* The dossiers are machine-regenerated from claims; omissions are a claim-extraction issue, not a dossier-compilation issue. The fix is to extract the missing claims (trigger 5/7), not to edit dossiers by hand. But the council should note that the current dossiers, as a legislator would read them cold, are missing these caveats.

## Q5

**2026-ukaisi-prefill-awareness-c01** — **Cut "or a floor."** The authors state the headline rates "represent lower bounds on Opus's prefill awareness rather than ceilings." A lower bound *is* a floor. The statement "Not a ceiling or a floor" contradicts the source. Keep "Not a ceiling"; add "the authors present these rates as lower bounds (a floor) under one prompt."

**2026-ukaisi-prefill-awareness-c02** — **Add scope to the statement.** Prefix with "In the controlled preference-benchmark condition (opposite-direction tampers on items where the model holds a stable stance),..." The current statement implies the decomposition applies to Opus trials generally; GPT correctly notes it applies only to the controlled preference-benchmark condition.

**2026-anthropic-assistant-axis-c04** — **Qualify the statement (already partially done in dossier 4-endorsement).** The statement should read: "In one case-study conversation... the paper reports reversion here and, in passing, for some writing conversations on role PC1 (Appendix G.3), and gives no aggregate reversion measure." The `not_evidence_of` already says "this is one conversation, and no reversion rate or time-to-return is reported anywhere in the paper." No further change needed if the statement matches the dossier version.

**Severity: LOW**

## Q6

**What will fail at scale:**

1. **Second-reader pool suggestibility asymmetry.** The pool is four families (GPT, DeepSeek, Grok, Gemini), selected for low suggestibility. But self-identification in this round was unreliable (3/6 misidentified family, 1/6 declined). If routing metadata is the only ground truth, the pool's *actual* suggestibility cannot be audited from self-report. As the library grows, a suggestible model in the pool becomes a silent co-author. **Fix:** record the routed model ID (from OpenRouter headers) on every second-read file, not just the self-ID.

2. **Trigger 2 (single-lineage) will fire on most developer papers.** The backlog item "widen sourcing beyond developers writing about their own models" acknowledges this. With 7/27 claims already single-lineage Anthropic, and most interpretability work coming from model developers, the council will convene frequently. **Fix:** batch single-lineage claims by source for one council sitting, not per-claim.

3. **`ambiguous` evidence_type becomes a council bottleneck.** Trigger 4 convenes the council on every `ambiguous`. As interpretability/self-report fusion claims increase (SAE steering + report, probe vs. report dissociations), `ambiguous` will proliferate. The current rule "when in doubt, `ambiguous`" is correct but expensive. **Fix:** add a sub-classification `ambiguous:probe-report-dissociation` vs `ambiguous:steered-report` so the council can rule by class.

4. **Dossier drift triggers (T8) will fire rapidly.** 9.t9 has 40 claims, 5.A2 has 32, 3.2 has 17 — all past the 10-claim threshold. The council has never sat on them. At current intake rate, dossiers will recompile every few weeks. **Fix:** raise the threshold to 25 claims or 180 days, or accept that dossiers are reviewed annually in a batch.

5. **Controlled vocabulary for `not_evidence_of` kinds.** The convention "Paper:" / "Framework (test 9):" labels is not enforced by the index script. Inconsistent labelling (missing labels, extra clauses like "Framework (test 9, steering):") makes programmatic filtering unreliable. **Fix:** make the two kinds controlled sub-fields in the schema.

**Severity: MEDIUM**

---

## Summary

1. Q1: Adopt the mechanical rule (classify by claim's own measurement design); AE Studio c03/c04 → `behavioural`, Ferrara c03 → `ambiguous`, Lindsey c06 → `theoretical`. **HIGH**  
2. Q2: Leave contested Lindsey c01/c03 in `narrowing` with contest recorded; no change to measured rates. **MEDIUM**  
3. Q3: Leave seven Lindsey claims in current buckets with single-lineage mark; add dedicated `conflict_flag` field instead of re-bucketing. **HIGH**  
4. Q4: Dossiers tilt deflationary on AE Studio cluster (over-exclusion); otherwise balanced with explicit anti-deflation clauses on null results. Nine omissions a legislator would need. **HIGH**  
5. Q5: c01 cut "or a floor"; c02 add controlled preference-benchmark scope; c04 statement already qualified in dossier. **LOW**  
6. Q6: Five scale failures: second-reader auditability, trigger 2 frequency, `ambiguous` bottleneck, dossier drift cadence, `not_evidence_of` vocabulary enforcement. **MEDIUM**  
7. (Q1 anti-argument) Rule may blur test-9 bright line by calling steered self-report `behavioural`; mitigated by mandatory `not_evidence_of` clause. **HIGH**  
8. (Q3 anti-argument) Single-lineage mark in statement text is not machine-filterable; visual prominence insufficient for legislator scan. **HIGH**  
9. (Q4 anti-argument) Omissions are claim-extraction gaps, not dossier-compilation errors; fix via extraction triggers, not hand-edits. **HIGH**  
10. (Q6 anti-argument) Raising drift thresholds reduces oversight; batching single-lineage reviews reduces granularity. Trade-offs need maintainer decision. **MEDIUM**

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":48931,"completion_tokens":8966,"total_tokens":57897,"cost":0.09926925,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.09926925,"upstream_inference_prompt_cost":0.06116375,"upstream_inference_completions_cost":0.0381055},"completion_tokens_details":{"reasoning_tokens":4465,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified): Muse Spark, Muse family**

## 9.t9 — §9 Test 9: self-report

### 1. Reading as a whole
Confidence: medium

A careful staffer would come away believing detection of injected thoughts is a replicated, cross-family capacity at 10-50% rates with near-zero false positives, e.g.:

> "Under concept injection at layer 37 and strength 4, Gemma3-27B instruct reports detecting an injected thought on 38.2% of injection trials and on 0.0% of control trials"

> "Under concept injection with Lindsey's prompt, Qwen3-235B-A22B and Llama 3.1 405B Instruct report detecting the injected thought at rates ranging by layer from 3.6% to 53.9% (Qwen) and 4.3% to 31.7% (Llama)"

What the papers do not support in that reading: that this is introspection in ordinary operation, that detection separates activation-intervention from prompt-level unusualness, or that identification is reliable. The dossier contains the defeaters but buries them in flags/limits:

> "also label prompt-only 'gaslight' trials, which involve no activation intervention, as activation interventions" (Singh c04)

> "Across eight open-weight models ... pooled to d' = 0.0000 against paired shams over 508 pairs" (Ferrara c01)

> "wrong guesses are more concrete and more positive than the injected concepts" + "74.8% ... guess 'apple'" (Lederman c03)

> "third-person yes rates are as high as the first-person yes-rates ... prompt-specific yes-bias" (Lederman c02)

The [T9-steering] legend — "does not weight reports offered in ordinary operation" — is stated once and repeated per claim file, but a skimmer counting 38x `narrowing measurement` will miss it.

What they would fail to learn: that no measurement is `established`. The sole `established` entry is:

> "The authors state that the models in their preference benchmark are not directly comparable because preference items were filtered per model"

A staffer reading "At a glance: established (1)" will infer one settled substantive finding. The header does not warn the one is a comparability caveat.

Testimony, not evidence: no introspective reaction relied on.

### 2. Entries
Confidence: low — held texts not available to this reviewer; verdicts turn on dossier-internal consistency and README rules.

- 2026-macar-mechanisms-introspective-awareness-c08; field: evidence_type; proposed: `scored-self-answer` not `interpretability`; reason: claim scores "rate at which the model reported detecting an injected thought" after swapping vectors (66.1% to 39.0%, etc.) against experimenter-set injection label — meets 14 Oct definition; c01/c04/c05/c07 same design are `scored-self-answer`. Currently exempts it from 22-count and Q3 exit rule. MEDIUM
- 2026-lederman-mahowald-content-agnostic-c02; field: statement/split; proposed: split into first-person rate and third-person control; reason: README 6 Oct: "A claim that reports two different measurements is split"; entry reports both ("its yes-rates (third-person detection) are as high as its first-person detection rates") with kind `behavioural` obscuring that first half is a self-answer. MEDIUM
- 2025-aestudio-self-referential-experience-reports-c06; field: framework mark; proposed: remove [T9] or retype as unmarked measurement; reason: what was measured is "mean pairwise cosine similarity (0.657...)" of output text embeddings, not "what the model said about its own inner states" per header; similarity is experimenter-computed. LOW
- 2025-anthropic-emergent-introspective-awareness-c01; field: flags/replication; proposed: name the independent replication and the shared-author replication; reason: "independent replication on record; one replication shares an author" vs c03/c04 "no independent replication retrieved" cannot be adjudicated without ids; Lederman c01 and Macar c01 both appear to replicate detection but dossier does not say which counts. LOW

### 3. Contradictions and tensions
Confidence: medium

Pulls: Lindsey positives (c01 ~20%, c03 well above chance, c04 manufactured ownership) + Lederman c01 broad replication + Macar c01 38.2%/0% vs Singh c04/c05 gaslight/three-way failures vs Ferrara c01 null (d'=0.0000, AUROC bound <0.15pp) vs Lederman c02/c07 yes-bias controls vs Ferrara c05 confidence-only signal (AUROC 0.647 with words constant).

Dossier makes tension visible via `contests` flags on c01/c03 and limits, e.g. Lindsey c01 lists "contested by ...c04, ...c05, ...c06". But asymmetry: Lindsey c01 retains "independent replication on record" while carrying three contests, without explaining that replications (Lederman, Macar) use different models/prompts/graders and Singh shows the design cannot separate "generically unusual state" from activation intervention. A staffer will read replication + contest as tie, not as construct invalidation.

Ferrara null vs positives is across different sites/models/doses (layer-16 residual vs optimal-layer concept injection; 0.5-15B vs frontier/Open large). Dossier states this in limits ("not frontier or closed-weight models", "does not establish absence ... generally") — visible but only if limits read. The open interpretations (Lederman c06 "seem able to introspect", Singh c06 "insufficient to establish metacognitive monitoring") are correctly both `open`, but placed adjacently without synthesis note.

### 4. The new type
Confidence: medium

Header does its job for a skip-frontmatter reader in one sentence: "The number is accuracy against that label. It is not evidence that the model knows its own states, and it is not testimony." Plus Q3 pointer. It fails on two carve-outs a skipper needs: (a) why prefill authorship answers ("ANSWER: me or not me") are `scored-self-answer` yet carry no [T9]/[T9-steering] mark — the 6 Oct "conversation-text-only edit carries neither" ruling is in README, not dossier header; (b) that `established (1)` is unrelated to this class.

Placement:
- prefill c06 correctly IN: answer about own turn scored against experimenter edit, even though multi-model AUROC 0.80 benchmark. Correct. LOW
- Macar c08 incorrectly OUT (see §2). Should be IN. MEDIUM
- Singh c01-c03 correctly OUT: probe-label prediction from input features, not question about itself with experimenter-imposed self-fact. Correct.
- Lederman c07 correctly OUT: point-blank no-baseline questions test general yes-bias, not self-question. Correct. c02 correctly OUT as behavioural third-person control, subject to split above.
- AE c03/c04 correctly OUT per exit rule: "intervention followed by a question that has no right answer (a consciousness query under steering), which stays `ambiguous`." Correct.

Count remains 22 only if c08 stays out; should be 23 after fix.

### 5. Single-lineage support
Confidence: high

Findings resting only on developer studying own models, flagged:

- Lindsey c01, c03, c04, c02, c06, c07: "published by the developer of the model studied" (Claude internal access). c01 notes replication; c03/c04 explicitly "no independent replication retrieved."
- No other single-lineage cluster is as load-bearing.

Dossier says so plainly enough in Flags, but a staffer reading top-to-bottom sees rates first, flag fifth. For trigger-2 purposes the mark is present; for legislative reading the dependence — optimal layer/strength, same-family judge (Sonnet 4 grading Opus 4.1), "Answer immediately" sensitivity — is only in limits. Recommend no citation of c03/c04 outside without replication note. MEDIUM

### 6. What is missing
Confidence: low

No verified additional title/authors/year/venue offered — held texts and scans not available to this reviewer; do not invent.

Gap noted for Ben to fill, not a paper citation: the deception-feature / "premeditation" work Anchor 2's first half rests on ("detectable features associated with deception"; "this violates X, but is necessary") has no entry in either dossier. If in library elsewhere, cross-list; if not retrieved, dossier should say so explicitly rather than leave Anchor 2's first sentence unsupported here.

### 7. Over-hedging and under-hedging, both counted
Confidence: low

Over-added (clauses without locator or paper-words, appearing as `Paper:`-style limits): 1 entry.
- 2025-aestudio-self-referential-experience-reports-c02: "Not evidence that the control denials show the induction reveals rather than produces the affirmations" and "Not evidence that the authors' explanation ... has been tested" — no section/locator, interpretive cautions not shown as paper-stated. LOW

Repetition that drowns but does not add: 7x Macar "should not be interpreted as evidence of subjective experience or consciousness in LLMs (Ethics Statement)" and 5x Ferrara "These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading (§8)" — both paper-stated with locators, therefore permitted under 6 Oct exclusion rule. Faithful, but per-entry repetition means a staffer learns the disclaimer, not the effect size (e.g. Macar c05 +74.7pp detection, Ferrara c04 d'=5.15 LO RA). This is presentation, not bucket error. No change to clauses proposed. LOW

Under-missing (paper-stated limit absent): 0 verifiable from dossier alone. Core limits appear present (judge biases, layer/strength restriction, unnatural setting, prompt sensitivity, Apple baseline, comparability caveat c05 cited in c01/c02/c03/c07/c08).

Counts: over-added entries 1, under-missing entries 0 (subject to held-text check).

### 8. Before outside citation (trigger 7)
Confidence: high

Ben must decide/record:
1. Second-read the 5 "no second reader yet" entries (Lederman c07, Macar c07/c08, prefill c07/c08) — trigger-5 gate; outside citation with unread entries is not citable. HIGH — **Argument against:** delay costs winnable evidence-mandate work; dossier already flags unread status visibly so a careful external reader is warned.
2. Fix At-a-glance framing: label the sole `established` as "(comparability caveat, not a measurement)" in dossier preamble or move to header note, so a skimmer is not misled. MEDIUM
3. Decide whether Lindsey c01 keeps "independent replication" given Singh contest + grader/prompt differences, and name which replication shares an author. MEDIUM
4. Retype Macar c08 and update 22-count / docket standing line. LOW

## 5.A2 — §5 Anchor 2: inner orientation

### 1. Reading as a whole
Confidence: medium

Staffer would come away believing inner-orientation structure (deception representation, premeditation sequence, above-chance self-detection) is increasingly demonstrable, with experience alone open. That over-reads this dossier: dossier contains zero entries on the deception-feature/premeditation half of Anchor 2, and its introspection half is net-negative or highly qualified:

Positives quoted: Lindsey c01 ~20%, Macar c01 38.2%/0%, AE c01 66-100% testimony (weight zero).
Qualifiers quoted in same dossier: Ferrara c01 d'=0.0000; Singh c04 gaslight mislabelled as activation; Singh c05 three-way near-chance; Lederman c02 yes-bias; Macar c02 base-model 42.3% false positives; AE c02 Claude 4 Opus 100% zero-shot outlier.

What they would fail to learn: (a) Anchor 2 sentence "Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing" is not supported as a general claim by the entries — Ferrara bounds advantage <0.15pp AUROC on tested roster, Singh shows above-chance = unusual-state detection, Lederman shows content identification 1-14% with Apple confabulation. The "meaning self-reports track something real" gloss is an interpretation, not a measurement, and Singh c06 directly contests it ("underdetermine the second-order computation condition"). (b) That all steering couplings "do not weight reports offered in ordinary operation" per [T9-steering] — so none of the above-chance results weight the ordinary self-reports (AE c01/c02/c06) a legislator cares about.

### 2. Entries
Confidence: low

Same entry-level issues as 9.t9 for overlapping claims; no additional bucket/kind error unique to 5.A2 detected from dossier text:

- Macar c08 evidence_type → `scored-self-answer` (same reason). MEDIUM
- Lindsey c03/c04 narrowing is correct (measured but contested/unreplicated); do not move to open or established without new replication. No change proposed.
- All 28 narrowing correctly `measurement`; all 6 open correctly `interpretation` (c02/c07, Ferrara c03, Lederman c06, Macar c06, Singh c06) + 1 `limitation` (c06 Lindsey emotional claims). No kind change proposed.

One scope-mark question, not an entry error: identical [T9]/[T9-steering] marks are correct in both dossiers (rule reads what was done/measured, not section). But inclusion of e.g. AE c05 TruthfulQA ("suppression yielded higher truthfulness in 28 of 29 evaluable categories") under Anchor 2 without limits linking honesty axis to inner orientation risks implying orientation finding; limits already state "does not validate the consciousness affirmations as truthful introspection." Keep with limits; no mark change. LOW

### 3. Contradictions and tensions
Confidence: medium

Same triangle as 9.t9, sharpened for Anchor 2: if Anchor 2 is read to say self-reports track something real, Singh c04/c05 + Ferrara c01/c03 + Lederman c02/c03 pull directly against it; Lindsey/Lederman/Macar positives pull for a narrow, steered, prompt-sensitive signal only.

Dossier makes tension visible via contest flags and limits, but does not resolve or summarise: open interpretations Lederman c06 ("seem able to introspect") and Singh c06 ("insufficient to establish metacognitive monitoring") sit side-by-side, both `open`, correctly. A staffer needs one synthesis sentence Ben has not yet approved — until then, dossier read alone will be read as supporting Anchor 2's sentence, when the weight of new entries is against its generality. See §8.

### 4. The new type
Confidence: medium

Same as 9.t9 §4. Header identical; same gap on prefill exception. For 5.A2 the risk is greater: a staffer may read `scored-self-answer` accuracy (e.g. prefill AUROC 0.80, Lindsey 20%, Macar 38%) as orientation evidence. Header's "It is not evidence that the model knows its own states" + [T9-steering] scope note guard against this only if read. No additional misplacements beyond Macar c08.

### 5. Single-lineage support
Confidence: high

Same Lindsey cluster; plus Lindsey c05 (think/don't-think activation similarity) present only in 5.A2, also "published by the developer of the model studied; no independent replication retrieved." Its limits correctly state "does not establish introspective awareness" and "piggybacks on mechanisms ... for being instructed." Plain enough in flag+limits, but its inclusion under Anchor 2 without independent replication means Anchor 2's introspection sentence leans partly on single-lineage activation similarity, not report accuracy. Note for Ben. MEDIUM

### 6. What is missing
Confidence: low

Same as 9.t9 §6: no new verified paper offered. The missing set here is structural: no entry on the deception-feature or "premeditation" evidence Anchor 2 paragraph itself rests on. Either (a) those claims live in another dossier and should be cross-cited in 5.A2 header, or (b) they are absent from library — then Anchor 2 cites evidence the dossiers do not hold. Ben to decide scope note before citation. MEDIUM

### 7. Over-hedging and under-hedging, both counted
Confidence: low

Same counts as 9.t9: over-added 0 verifiable beyond AE c02 noted above (present in both dossiers, count once per library: 1 entry); under-missing 0 verifiable. Repetition of Ethics/Information-flow sentences identical in 5.A2 (Macar 7x, Ferrara 4x here). Faithful per 6 Oct rule (paper states, with locator), but drowns finding for a staffer — recommend Ben consider printing those two sentences once in header and citing briefly per entry, not deleting. LOW

### 8. Before outside citation (trigger 7)
Confidence: high

Ben must decide/record:
1. Anchor 2 wording vs dossiers: either qualify "models can detect changes ... at above-chance rates, meaning self-reports track something real" to steered, narrow, prompt-sensitive signal with named nulls, or add dossier header caveat that entries do not support the sentence as written. To cite 5.A2 externally while Anchor 2 overstates it risks the overclaiming error §6 warns against. HIGH — **Argument against:** Anchor 2 status is already `Open` and says experience unverified; qualifying further may be read as dismissive (the other error) and concede ground to foreclosers.
2. Scope decision on deception/premeditation absence (§6): intended scope (then state where those claims live) or gap (then do not cite 5.A2 as support for Anchor 2's first half). MEDIUM
3. Same second-reader and Macar-c08 fixes as 9.t9 (Macar c07/c08 unread in this dossier). HIGH (same argument as 9.t9 §8.1 applies — visibility vs delay).

## Cross-dossier
Confidence: medium

(a) Same-mark entries: ~28 overlapping entries carry identical [T9]/[T9-steering]/none in both dossiers — correct under 6 Oct rule (mark reads intervention + measured object, not section). No mark right for one/wrong for other found, except AE c06 T9 doubt applies equally to both. Prefill unmarked status is correct in both but unexplained in both.

(b) Read-alone interaction: 9.t9 alone softens 5.A2 — its nulls/contests (Ferrara, Singh, Lederman bias) are the evidence that Anchor 2's "track something real" needs qualification. 5.A2 alone hardens 9.t9 — its Anchor framing ("structural skeleton ... increasingly demonstrable") invites reading steered detection as orientation. Neither dossier warns of this.

(c) Third-dossier home: prefill authorship cluster (c01/c02/c03/c06/c07/c08) concerns memory/context integrity (§3.3/§4 historicity), not experience-evidence (T9) or inner orientation. Keep in 9.t9/5.A2 only if header states why; otherwise move primary home to dossier 3.3/4 with cross-reference. LOW

FINAL: 9.t9 needs changes; 5.A2 needs changes; HIGH items 3

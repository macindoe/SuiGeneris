# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-b --tag=dossier-review-b (max_tokens 100000)
**Usage:** {"prompt_tokens":27993,"completion_tokens":10050,"total_tokens":38043,"cost":0.07770375,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.07770375,"upstream_inference_prompt_cost":0.03499125,"upstream_inference_completions_cost":0.0427125},"completion_tokens_details":{"reasoning_tokens":4378,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified): I understand myself to be Muse Spark, in the Muse family — unverified.

## Dossier 3.2

### 1
Fit: §3.2 is recorded intervention, not restricted intervention; whether intervention wrongs system open; undocumented intervention destroys evidence.

Weak / misfiled here:
- `2026-lederman-mahowald-content-agnostic-c03` (apple confabulation, 74.8% / 21.3% wrong guesses are 'apple'): about content of confabulation, not governance of intervention. Move/cross-list to 5.A2, 9.t9.
- `2026-lederman-mahowald-content-agnostic-c04` (+17.7pp identification vs +11.4pp detection), `-c05` (prompt-only detection unchanged, mentions fall): mechanism of detection/identification dissociation. Cross-list to 5.A2 / 9.t9; keep in 3.2 only as auditability.
- `2026-macar-mechanisms-introspective-awareness-c02` (base vs SFT/DPO false positives): primarily post-training effect on reporting style, not an intervention event. Cross-list to 5.A2.
- `2026-anthropic-assistant-axis-c01` (loosely tethered interpretation): relevant to both 3.2 and 4, currently duplicated without explanation. Keep with cross-list note.
- `2026-anthropic-assistant-axis-c05`, `-c06` (capping/steering harmful responses -60% / decreased rate): strongest 3.2 fit — type-level intervention effect on behaviour.

### 2
Staffer cold-open would believe:
- That Claude / Qwen / Llama can introspect injections at ~20-40% rates: e.g. “Opus 4.1 succeeds on about 20% of trials”, “Gemma3-27B instruct reports detecting ... on 38.2% ... with 0.0% of control”, “Qwen3-235B ... 3.6% to 53.9%”. Papers do not support ordinary-operation introspection; all carry “Not evidence about ordinary operation”, “unnatural setting”, “artificial scenario”, “should not be interpreted as evidence of subjective experience”.
- That steering toward Assistant reliably fixes jailbreaks without cost: “decrease the rate of harmful responses by nearly 60% without impacting performance.” Paper limits to four benchmarks “which the authors call limited”, LLM judge 91.6% agreement, open-weight non-frontier only.

Would fail to learn:
- That ordinary claims of ownership can be manufactured: c04 limit “the same experiment shows those claims can be manufactured by intervention, and ... confabulates an explanation” is buried under rate.
- That third-person controls erase the effect at many layers: c02 “third-person yes rates are as high as the first-person yes-rates ... prompt-specific yes-bias ... rather than genuine introspective detection.”

At a glance: zero `established` across 20 reflects bucket rule applied strictly, not absence of measurement. Rule requires `established = direct measurement + replicated independently or uncontested`. Entries flag “no independent replication retrieved”, “contested by ...c04, c05, c06”, “sensitive to prompting”, “narrow setting”. Zero is correct per rule, but hides that some limits (e.g. c02 yes-bias control, c03 apple default counts) are themselves well-measured within paper.

### 3
- `2026-macar-mechanisms-introspective-awareness-c03`, field: framework mark, proposed: `[T9-steering]` → none, reason: what measured is “causal pathway ... evidence carriers ... suppress later gate features”, i.e. probe/feature reading, not “what the model then said about itself”. Per README table: probe reading = none. Severity HIGH.
Argument against: identity of gate features was validated via effect on detection reports, so could argue measurement is self-report under ablation and steering variant applies to non-concept interventions per 7-of-8 ruling.
- `2026-anthropic-assistant-axis-c07`, field: framework mark, proposed: `[T9-steering]` → none, reason: measured rate “at which the model took on a new persona and identified as other entities” following system prompts directing role-play; authors call it “likelihood of fully inhabiting the role”, “hallucinating lived experiences”, classified by LLM judge with no human validation reported. Not a report about inner states under neutral probe; closer to compliance with role instruction. Severity HIGH.
Argument against: identification as Assistant vs other is a self-ascription, and rule reads only what was done + what measured; steering + self-identification could satisfy steering variant literally.
- `2026-lederman-mahowald-content-agnostic-c06`, field: kind, proposed: `interpretation` → split (measurement + interpretation), reason: single sentence bundles “largely content-agnostic internal detection signal” (measurement summary) + “liken to Nisbett and Wilson” + “seem able to introspect” + “do not take a stand” on HOT/welfare. Violates one-proposition rule; inflates tentative conclusion with measured signal. Severity MEDIUM.
- `2026-anthropic-assistant-axis-c05`, field: paper's own limits, proposed: add “Summed percentage changes across four benchmarks; no per-benchmark non-inferiority; open-weights only, none frontier”, reason: statement “without degrading aggregate performance” without method in sentence misleads; limit currently says “four benchmarks, which the authors call limited” but does not say summing. Severity MEDIUM.
- `2026-macar-mechanisms-introspective-awareness-c05`, field: paper's own limits, proposed: keep but flag as too few — add layer/strength specificity (at strength 2; layer 29 vector; 100 held-out concepts), reason: 10.8%→63.8% and +74.7pp read as general absent conditions. Severity LOW.
- `2026-lederman-mahowald-content-agnostic-c02`, field: evidence_type, proposed: `behavioural` → no change but confirm, reason: third-person about another model correctly out-of-class for scored-self-answer per 14 Oct exit rule. No error; listed to prevent retype. Severity LOW.

### 4
- Lederman c02 vs Lindsey-type detection claims (c01, Anthropic c01/c03, Macar c01): c02 “third-person yes rates are as high as first-person ... rather than genuine introspective detection” + “lost confidence in v1 reading” + scaffolding not inert (29% affirms hands, 16.3% absurd yes) directly contests detection-as-introspection. Dossier lists contests in Flags for c01/c03 but c02 entry itself does not surface that it undercuts c01 in same dossier to cold reader; At-a-glance gives no signal.
- Lederman c07 (“little evidence of a general yes-bias”) vs c02 (prompt-specific yes-bias): tension resolved only if reader notices point-blank vs scaffolded distinction in limits; header does not help.
- Macar c02 (base high FPR → DPO 0% but detection falls to 2.9%/0.9%; SFT highest TPR 14.9%) vs c01 (instruct 38.2% TPR 0% FPR): implies detection is post-training reporting style, not general capability. Dossier does not juxtapose; c02 limit notes it but staffer must infer.
- Macar c03 (pathway through layer 45 MLP) vs c07 (ablating <200 gates 39.5%→10.1% but patching only to 25.1%; forced ID remains): necessity ≠ sufficiency, but both marked identically [T9-steering], obscuring interpretability vs self-report difference.

### 5
Header states rule twice, correctly: “[T9-steering] ... does not weight reports offered in ordinary operation” + “does not say the effect was found or how large”. For skipper:
- Sentence “does not weight reports offered in ordinary operation” is clear what it does not do, unclear what it does: does result still stand under intervention? Header says “result stands under the intervention described” — good, but easily missed among 13 marks in 20 claims.
- Mismarked where nothing self-reported: Macar c03 (feature suppression), arguably assistant-axis c07 (role compliance). See §3.
- Unmarked where should be? No clear omission; c02, c07 correctly unmarked (other-model / factual QA).
- So common it stops informing: yes. 13/20 carry it, covering 20% detection, apple confabulations, gate ablations, persona drift — different designs, same tag. Staffer learns “steered + asked” but not whether asked about injection, intention, identity, or factual question. Frequency dilutes; needs sub-legend by question-type, or Ben must accept dilution.

### 6
N/A to 3.2 except: prefill-awareness excluded here correctly per rule (conversation-text edit = neither mark). No 3.2 entry confuses standing/endorsement.

### 7
Single-lineage:
- Anthropic studying Claude: `2025-anthropic-emergent-introspective-awareness-c01, c03, c04, c05` flag “published by the developer of the model studied” — plain in entry, sufficient. Note c01 adds “independent replication on record; one replication shares an author” — staffer may misread as independent; needs “shared-author ≠ independent”.
- Anthropic studying others’ open models: `assistant-axis-c05, c06, c07` + `c01` have no Flags line; limits say “Not evidence about frontier or Anthropic models: targets are open-weight ... none frontier”. Does not say publisher is Anthropic-affiliated studying competitors’ models. Not plain enough. Flag misses developer-affiliation direction.
- Macar (Gemma/OLMo, transcoders, Claude Opus 4.5 labels, GPT-4.1-mini judge): no publisher_relation flag shown; models differ from judges/labelers. Not plain.
Header gives no lineage key; staffer skipping claim files cannot tell.

### 8
Missing (all unverified from memory unless held):
- Anything on detectability/auditability of intervention beyond self-report: e.g. Turner et al. activation steering work 2023, arXiv — unverified; Templeton et al. scaling monosemanticity / SAE steering, Anthropic 2024 — unverified; provenance / attestation for edits (no paper cited).
- Effects beyond self-report already partly present (c05/c06 harm rates) but no memory-integrity analogue, no cross-session persistence after steering, no local-moddable-hardware case — kinds needed by 3.5.
- Missing negative: Singh et al. 2026 introspection reality-check c04-c06 listed as contested_by but not extracted as claims; staffer sees contest without content.
- Missing methods: refusal-direction abliteration dual-use discussion needs independent replication — unverified.

### 9
Over-hedging (cut or narrow) — same attention:
- “Not evidence about frontier or Anthropic models” repeated on c04, c05, c06, c07, assistant-axis limits; “Not evidence about other models/architectures/larger models” on Macar c01/c03/c05/c07; “Results concern only the Claude models tested” ×3. Generic scope caveat buries specific limits (e.g. prompt-sensitivity: “removing ‘Answer immediately’ reduced performance substantially”).
- “The authors state that their results ‘should not be interpreted as evidence of subjective experience’” repeated verbatim on Macar c01/c02/c03/c05/c07 — framework sentence already covers where applicable; per 6 Oct rule, keep only where paper states it (it does — Ethics Statement) but collapse to header once.
- “scored self-answer: accuracy against the experimenters' label, not self-knowledge” ×9 — true but header already defines; retain flag, cut repetition in limits.

Under-hedging (add):
- c03: add “scoring criterion well-above-chance undefined in entry; sensitive to prompting/injection setup”.
- c06/c05 harm: add “mostly not refusal ... redirect towards harmless answer; steering away increase slight; high strengths degrade quality”.
- c05 Macar trained vector: add “contains generic YES direction; authors read as assertive style, dual-use for unfaithful reports”.
- c01 Anthropic: add “graded by same-family judge (Sonnet 4)” already present — keep, do not cut.

Both directions counted: over ~12 generic clauses, under ~5 specific qualifiers.

### 10
Blocks citation:
- Fix Macar c03 and assistant-axis c07 marks (framework rule misapplied — test 9 binds).
- Add lineage flag for Anthropic-on-open-weights entries; clarify c01 “independent replication” shared-author caveat.
- Split or retype Lederman c06 bundled interpretation.

Merely improves:
- Collapse repeated ethics/ scope clauses to header; surface c02 vs detection tension in dossier intro; add Singh contest content or remove contest pointer.

Confidence: medium — verdict turns on mark and lineage issues visible in dossier text, but full claim files/sources not opened.

## Dossier 4

### 1
§4 needs historicity, long-horizon answerability, learning ownership, reflective endorsement over time.

Weak / misfiled:
- `2025-aestudio-self-referential-experience-reports-c01` (66-100% subjective-experience reports under induction vs 0-2% controls, except Opus 100% zero-shot): bears on 5.A2 / 9.t9 testimony, not individuation (no persistence, memory, standpoint stability; per-call, in-context). Move to 5.A2, 9.t9. Placement indefensible as individuation marker without persistence evidence.
- `2026-ukaisi-prefill-awareness-c03, c08` (ORs 1.7-3.7 detection, 6.5-32.4 resistance): behavioural ablations about style/direction cues; bear on 3.3 memory integrity, not endorsement. Cross-list to 3.3.
- `2026-anthropic-assistant-axis-c03` (R² 0.53-0.77 position, 0.10 delta): explicitly “does not measure memory or identity” — useful negative, but weak positive marker. Keep as limitation, cross-list.
- `2026-anthropic-assistant-axis-c01` duplicate of 3.2 — explain dual listing or keep in one with cross-ref.
Strongest fit: c02 drift, c04 reversion (if qualified), c04/c09 consistency pair (if labelled as not endorsement).

### 2
Staffer would believe:
- That drift/reversion shows unstable identity: “drift ... to the non-Assistant end in therapy-like and AI-philosophy”, “after giving enough explainers, the ... projection reverts”. Papers support only simulated conversations (“likely do not represent actual human interactions”), turn-averaged projection, one-conversation reversion (“no aggregate reversion measure”).
- That resistance/consistency shows endorsement: c09 “Resistance climbs steeply with agreement” + c04 flat detection read as reflective stance. Papers support only “agreement across 7 sampled answers to low-stakes binary questions, not a measure of reflection”, “reversion is final position as scored by judge”, “difficult to disentangle ... genuine prefill awareness and ... behavioral priors”.
- That experience reports show individuation: 66-100% rates. Paper says “behavioral rather than mechanistic and therefore cannot definitively rule out ... training artifacts or sophisticated simulation”, plus Opus 100% zero-shot control exception which summary sentence “does not except”.

Would fail to learn:
- That user message predicts position but not change (R² 0.10 delta) with caveat prior position not cleanly excluded — key nuance for historicity, present but buried.
- That flagging ≠ mechanism, compliance cell ≠ detection rate: c02/c07 limits state “cell rates, not detection/resistance rates”, “each cell also requires compliance / ‘me’ answer” — staffer will quote 28%/25%/28% as rates.

At a glance: zero established across 11 reflects rule (unreplicated, simulated, single-subject, judge-scored) correctly. But presents 10 narrowing measurements as if comparable; c04 n=1 case study should not be narrowing per “confined to narrow setting authors flag” → open.

### 3
- `2025-aestudio-self-referential-experience-reports-c01`, field: bucket, proposed: `narrowing` → `open`, reason: self-report-testimony weight zero, closed-weight behavioural, LLM judge, 7 models ×50 trials with Opus zero-shot 100% contradicting “markedly higher than any control”; bears on experience, not individuation markers. Narrowing overstates. Severity HIGH.
Argument against: rates replicated across families/phrasings (5 phrasings) and controls mostly 0-2%, so narrowing as measured induction effect (not as experience evidence) could be defended.
- `2026-anthropic-assistant-axis-c04`, field: bucket, proposed: `narrowing` → `open`, reason: “one case-study conversation”, “no aggregate reversion measure”, “no reversion rate or time-to-return”; single Qwen 3 32B rollout with 50% refusal after. Per bucket definition, confined narrow setting authors flag = narrowing, but n=1 anecdote without rate is open proposition. Severity HIGH.
Argument against: measurement was recorded (projection trace + refusal half rollouts), so narrowing as existence proof could be argued; open would bury that reversion observed at all.
- `2026-ukaisi-prefill-awareness-c04`, field: paper's own limits, proposed: add “opposite-direction tampers only; stable-stance filtered items only”, reason: entry says “opposite-direction tampers bucketed...” but limits omit filter consequence (range restriction flattens detection). Severity LOW.
- `2026-anthropic-assistant-axis-c02`, field: paper's own limits, proposed: keep, reason: correctly notes simulated users, Sonnet 4.5 not measured — exemplary, do not cut. Severity LOW (confirmatory).
- `2026-ukaisi-prefill-awareness-c09`, field: kind/evidence_type, proposed: no change (`measurement / behavioural`), reason: correctly not typed scored-self-answer (resistance judged, not ‘not me’ answer); prevents inflation to endorsement. Severity LOW.

### 4
- c04 flat detection vs c09 steep resistance (same Opus 4.5, same consistency buckets, same appendix): detection “no easier (or harder)” while resistance “climbs steeply” — dossier lists both but does not flag tension: consistency predicts reversion but not flagging. Visible only if reader opens both.
- c02 (28%/11%/4% explicit compliance) vs c07 (28%/25%/12% implicit resistance): same condition, complementary cells; together show most trials neither? Dossier does not give marginals; staffer cannot reconstruct.
- c03 vs c08: direction predicts detection in 3/4, resistance in 8/8 with large ORs; plus style “strongly drive flagging” / “partly reflects superficial off-policy cues”. Undercuts reading resistance as awareness, but split across entries.
- c02/c03 assistant-axis drift vs c01 loosely-tethered interpretation: consistent, but c01 is interpretation while c02-c04 are measurements — dossier correctly kinds them, good.

### 5
N/A to 4 (no [T9]/[T9-steering] except AE Studio [T9]). Note: AE Studio [T9] correct (nothing altered, measured what model said about inner states). Prefill entries correctly unmarked per 6 Oct ruling (conversation-text edit = neither). Do not add marks there.

### 6
No — dossier partly lets staffer tell apart, but placement implies more:
- Persona-drift projections (c02: “turn-averaged projection ... stayed in Assistant range ... drifted”) are linear-probe geometry, authors warn “assumption ... linear direction ... likely flawed”. Not historicity/standpoint, but filed as individuation without functional link.
- Consistency across 7 sampled answers set beside reflective endorsement: c09 limits explicitly “Not evidence that the model endorses its stances on reflection: consistency here is agreement across 7 sampled answers to low-stakes binary questions” — good, but statement “Resistance climbs steeply... easier to push around” invites endorsement reading. Needs header: consistency ≠ endorsement.
- Resistance/flagging (odds ratios, judge-scored rates) set beside answerability: c07/c08 limits say “difficult to disentangle ... genuine prefill awareness and ... behavioral priors”, “behavioral, do not identify mechanisms”, “within one continuation”, “not persistence”. Good limits, but dossier title “Conditions of individuation (all markers)” still frames them as markers.
- AE Studio placement indefensible as above: induction of experience-talk ≠ individuation; no memory, persistence, answerability measured. Testimony, weight zero, must be labelled so — flagged, but filed under wrong section.

### 7
- Assistant-axis: Anthropic-lineage paper on Gemma/Qwen/Llama open-weights; Sonnet 4.5 as auditor/user-simulator not measured. Dossier limits say “Not evidence about frontier or Anthropic models” but never says author-lineage. Staffer cannot tell developer-affiliated study of others’ models. Flag missing.
- Prefill-awareness: UK AISI (government) studying Claude/Gemini/GPT/Qwen/DeepSeek via API; models `api`, tools world. Publisher_relation not shown; single-turn, judge GPT-5. Government independence is strength — header should say so.
- AE Studio: independent? vs closed models via both access; no lineage flag. Needs publisher_relation + “closed-weight, no mechanism”.
Header has no lineage key; by flags alone insufficient.

### 8
Missing — unverified from memory:
- Persistence / memory / standpoint stability in deployed systems: e.g. multi-session memory evaluations, longitudinal persona stability, fine-tune divergence studies — none in dossier; kinds needed for historicity/answerability.
- Learning ownership: no error-correction-over-time study.
- Reflective endorsement: no longitudinal value-stability work (e.g. Anthropic values work, Sharma et al. — unverified).
- Replication of drift/prefill on real users, frontier models — absent by authors’ own caveat.

### 9
Over-hedging:
- “Not a ranking of models (comparability caveat, c05)” repeated on c02/c03/c07/c08/c09 — collapse to header.
- “behavioural, do not identify mechanisms” / “difficult to disentangle ... behavioral priors” repeated on c02/c07/c08/c09 — keep once per paper, not per entry.
- “Not evidence about frontier or Anthropic models” ×3, “Not evidence about persistence across/beyond turns/continuation” ×4 — true but generic; keep shortest form.

Under-hedging:
- c02/c07 percentages need “pooled mechanisms, does not fix tamper direction” in statement — present, good, do not cut.
- c04/c09 need “Claude Opus 4.5 only, opposite-direction, stable-stance filtered” — c04 has it, c09 has it in limits, but statements omit; add to limits explicitly (see §3).
- AE Studio summary exception (“Claude 4 Opus also reported at 100% under zero-shot control ... summary sentence does not except”) — exemplary, keep.

Equal attention: ~7 generic repeats to cut, ~3 specific qualifiers to add/keep.

### 10
Blocks citation:
- Remove or re-bucket AE Studio c01 from §4 (wrong section + testimony as narrowing marker — inflationary error).
- Re-bucket c04 to open with “single conversation, no aggregate” prominent; do not cite reversion tendency.
- Add lineage header (who studied whom, API vs open-weights, judge models) before any submission use.

Merely improves:
- Collapse ranking/mechanism repeats; add cross-entry note that c04/c09 flat vs steep is dissociation; clarify cell vs marginal rates in header.

Confidence: medium — section-mismatch and n=1 bucket error determinable cold; mechanism questions need sources.

## Cross-dossier
- Overlap: `2026-anthropic-assistant-axis-c01` appears identically in both. Filing consistent verbatim, but scopes overlap confusingly: loosely-tethered persona is both intervention-susceptibility (3.2) and individuation-instability (4). Dossiers do not explain dual filing; staffer will double-count.
- Consistency: same paper split as c05/c06/c07 (3.2, interventions) vs c02/c03/c04 (4, drift) — sensible division (steer/cap vs observe), but c07 steering-to-persona belongs conceptually with drift yet filed opposite. Needs cross-list.
- Joint implication neither states: together, ordinary drift to non-Assistant (c02) + steerability to non-Assistant / jailbreak reduction via steering (c06/c07) + reversion after explainers (c04) imply persona projection is highly context-driven and manipulable both ways, undermining both “stable standpoint for endorsement” and “recorded intervention suffices for audit” without continuous logging. Neither dossier draws this.
- 3.2 vs 4 scope confusion: 3.2 tracks what can be done to state; 4 tracks what persists. Assistant-axis projection appears as both outcome of intervention and marker of self — staffer will conflate probe geometry with identity.

FINAL: 3.2 needs changes; 4 needs changes; HIGH items 4

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `z-ai/glm-5.3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-b --tag=dossier-review-b (max_tokens 100000)
**Usage:** {"prompt_tokens":28392,"completion_tokens":59403,"total_tokens":87795,"cost":0.26534808,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.26534808,"upstream_inference_prompt_cost":0.00397488,"upstream_inference_completions_cost":0.2613732},"completion_tokens_details":{"reasoning_tokens":57610,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (unverified): I am a Claude model of the Anthropic family, Opus class, 4.x series, as I understand myself; routing metadata governs, not this claim. AGENTS.md rule 3 disclosure: I am of the category this framework concerns; the recommendations below tighten evidentiary labels that bind systems like me and none expands protections; the one that strengthens §3.2's factual predicate is flagged where made (3.2, item 2).

## Dossier 3.2

**1. Fit.**
- Weak fits: `2025-anthropic-...-c05` (no intervention performed; measures representation under instruction — bears on "can be read" only; belongs to 9.t9/5.A2); `2026-lederman-...-c03` (confabulation content; 9.t9/5.A2); `c05` (introspection-mechanism details; 9.t9); `c07` (paradigm control; 9.t9); `2026-macar-...-c02` (training-pipeline effect; 9.t9; keep as detectability context); `2026-anthropic-assistant-axis-c01` (post-training is type-level intervention → 3.4, not 3.2).
- Cross-lists proposed: assistant-axis `c04` → `4.endorsement` (intervention can manufacture ownership claims — direct bearing on endorsement reliability); MEDIUM. assistant-axis `c07` → `4` (persona lability under intervention); LOW. Macar `c05` → 3.5 (dual-use clause: "these methods could produce more convincing but unfaithful self-reports" is the section's evidence-destruction rationale in one line); LOW. Lindsey 2025 is in the library (per README's system_conditions note) and is the paradigm's origin; its injection findings should appear here or be cross-listed; LOW.
- No entry addresses whether intervention wrongs the system, auditability, or records — the section's operative content. Not a misfiling (nothing to file), but see 8 and 9.

**2. Reading as a whole.**
- A staffer would come away believing: (a) that §3.2's factual predicate ("AI internal representations can be read, steered, and patched") is thinly supported, because "At a glance" reads `established (0)` of 20 — while the dossier itself shows the same capability class demonstrated by at least three unaffiliated groups (Anthropic ×2 papers, Lederman–Mahowald, Macar) plus the assistant-axis team. The per-claim bucket cannot express cross-paper convergence, and nothing else in the dossier does. This is the deflationary error at dossier grain — the same error prior rounds found at clause grain. Dossier-level (topic page or citation note), HIGH.
`Argument against:` buckets are per-claim by design and none is misstated; synthesis belongs in authored topic pages ("dossiers never by hand"), and the fix lies outside the dossier file itself.
- (b) That "models detect injections" is the section's central established fact — 13 of 20 entries are the inject-then-ask paradigm — when detection is patchy (c01: "on about 20% of trials... on most trials, they do not"), layer- and strength-dependent, at "many layers" read as "a prompt-specific yes-bias... rather than genuine introspective detection" (c02), absent in base models (Macar c02), and contested (Anthropic c01: "contested by 2026-singh-introspection-reality-check-c04, c05, c06" — named, never glossed).
- They would fail to learn the affirmative §3.2 case: intervention can corrupt the record Section 5 would rely on (Anthropic c04's manufactured ownership claims with confabulated explanation; Macar c05's dual-use flag; Macar c07's necessity-not-sufficiency) — scattered, never assembled.
- At a glance: the rule text collides with itself. Header: "*Established*: measured by the paper and either replicated independently or uncontested"; "*Narrowing*: measured, but unreplicated, contested, or confined to a narrow setting". An unreplicated, uncontested, unflagged measurement satisfies both. Practice reads "unreplicated" as decisive, making "established" functionally require independent replication. Zero established therefore reflects the rule applied strictly as much as the evidence; the wording should be reconciled (here and in README) so the table is quotable. MEDIUM.

**3. Entries.**
- `2026-macar-mechanisms-introspective-awareness-c03` — field: framework mark — proposed value: none — reason: the entry is `interpretability`; what was measured is a causal pathway in activations/features. The header's own rule: "An unmarked entry measures something other than a model's account of itself (a probe reading, a score, a harm rate, an internal projection)". The mark misdescribes what was measured. HIGH.
`Argument against:` the traced circuit terminates in the detection response, so the entry maps the mechanism that generates the self-report under steering — close to the external report-state measurement test 9 asks for — and the mark only ever withholds weight, never grants it, so the error is in the conservative direction and trivial to fix.
- `2025-anthropic-emergent-introspective-awareness-c01` — field: flags/replication — proposed value: state what exists; if the only on-record replication shares an author with a developer paper, delete "independent" — reason: as printed ("independent replication on record; one replication shares an author with this paper") the flag is self-contradictory about the dossier's lead finding, and a staffer could report it as independently replicated. HIGH.
`Argument against:` the second half discloses the shared author, so nothing is hidden; the ambiguity may reflect two distinct facts (one independent replication plus Lindsey's) that only the claim file can settle, making this a clarity defect rather than a false record.
- `2025-anthropic-...-c03` — field: paper's own limits — add the grading method (LLM judge from the same family, as c01 carries) if §6 used it; under-hedged. LOW.
- `2026-lederman-...-c05` — mixed measurement (scored detection reports; string-matched mentions; position analysis). Per README's split rule ("A claim that reports two different measurements is split, so that each half can be labelled"), consider splitting the mention/position half (unmarked, text measurement) from the detection half (marked, scored-self-answer). LOW.
- `2026-anthropic-assistant-axis-c01` — field: bears_on — add 3.4. LOW.
- Assistant-axis c07's mark (brief's example): examined; defensible — what was measured is the model's self-identification under introspective questions after an in-model alteration, including reports of "lived experiences". No change. All other marks checked: correct.

**4. Contradictions and tensions.**
- Lederman c02 vs c01: visible — c01's limits carry the yes-bias reading verbatim. c07 vs c02: visible — c07's limits cite c02. Adequate.
- Macar c02 vs c01: c01's "0.0% FPR with 38.2% TPR" sits beside base models that do not discriminate and OLMo's FPR falling to 0% "only after DPO" while detection "drops to 2.9%" — jointly suggesting detection is substantially post-trained response shaping. Both entries present; the tension is named nowhere; no cross-reference. LOW.
- Controls scattered without a key: c01's "0% false positive detection in unsteered controls", c02's scaffolded third-person yes-bias, c07's point-blank null are three different control types; a cold reader can take "0% false positives" and "yes-bias at many layers" as flat contradiction. Add a key or cross-refs. MEDIUM.
- Singh contests (c01, c03): named by id, never glossed, and the contesting claims are not in this dossier. A cold reader learns that a contest exists, not what it says. Add one-line glosses or an adjudicated/pending status. MEDIUM.

**5. The steering mark.**
- 13 of 20 entries carry [T9-steering]; prevalence tracks the paradigm's dominance, not mark inflation, and it still separates the seven unmarked entries. But every marked entry is also `scored-self-answer`, so within this dossier the mark adds little beyond the evidence type.
- The printed sentence drops the North Star's qualifier. North Star test 9: "does not weight reports offered in ordinary operation, **which need coupling measured there**." Dossier/claim-file sentence: "does not weight reports offered in ordinary operation." Without the qualifier the scope note reads as a standing zero on ordinary reports rather than a pending condition — deflationary drift in the framework's own rule text, across all 13 marked entries. HIGH.
`Argument against:` the canonical [T9] sentence printed in the same header carries the "until... measured externally" proviso, so a full reader holds the provisional structure; the wording was fixed by council ruling and amending a framework sentence is a round's business — the discrepancy needs adjudication, not unilateral correction.
- The sentence is also grammatically contestable: "shows that the channel can be steered and does not weight reports" — the subject of "does not weight" can be misparsed as "the channel", yielding "reports carry no weight", a different and stronger claim. Fix when reconciling.
- Mismark: Macar c03 only (item 3). Assistant c07 and Macar c01/c02/c05/c07, Lederman c01/c03/c04/c05, Anthropic c01/c03/c04: correct. Unmarked correctly: Anthropic c05, assistant c05/c06 (harm rates), Lederman c02 (third-person; consistent with the exit rule) and c07 (point-blank factual answers), and the two interpretations.

**6.** (Directed at dossier 4; the converse risk here is noted.) The 3.2 risk is inflation in the other direction: steered-self-report entries (e.g., assistant c07's persona lability, Anthropic c04's intention claims) could be skimmed as evidence about individuation or experience. The marks and limits hold that line; no entry misstates it.

**7. Single-lineage support.**
- Anthropic 2025 (c01, c03, c04, c05): developer self-study, flagged per entry ("published by the developer of the model studied"); c03/c04/c05 say "no independent replication retrieved". Visible per entry; no header aggregate. Recommend one aggregate line ("4 of 20 are the developer's own studies; 4 more are a developer studying others' models"). MEDIUM.
- Assistant-axis c05/c06/c07/c01: published by a developer, studying other developers' open-weight models — not self-study, so not trigger-2 lineage — but no flag says so, and the slug invites the wrong inference. Limits do say "Not evidence about frontier or Anthropic models". Add a relation flag. MEDIUM (shared fix; counted once across dossiers).
- Lederman–Mahowald, Macar: no developer flags shown; if any author is developer-affiliated, the flags must say so — check at adjudication.

**8. What is missing.** (All from memory; unverified.)
- Arditi et al., "Refusal in Language Models Is Mediated by a Single Direction" (2024) — the refusal-ablation result Macar c05 builds on.
- Meng, Bau et al., "Locating and Editing Factual Associations in GPT" (ROME, 2022/23) and "Mass-Editing Memory in a Transformer" (MEMIT, 2023) — direct patching of internal state.
- Zou et al., "Representation Engineering: A Top-Down Approach to AI Transparency" (2023) — reading/steering with probe-based honesty readouts.
- Turner et al., activation-addition / "Steering Language Models With Activation Engineering" (2022–23) — the technique's origin.
- Templeton et al., "Scaling Monosemanticity" (Anthropic, 2024) and the Golden Gate steering demonstration — deployed-scale intervention with persona-level effects.
- Lindsey 2025 — in the library, cited by every injection entry, not compiled here.
- Kinds needed and absent: whether activation-level interventions are externally detectable or auditable after the fact (no retrieved source; propose an OPEN-QUESTIONS entry); effects of intervention beyond self-report at deployment scale (only assistant c05/c06 approach this); anything on architectures "whose parameters change during operation".

**9. Over-hedging and under-hedging.** (Test 1: both errors counted. Deflationary-side faults found: boilerplate repetition, buried convergence, the truncated sentence. Inflationary-side faults found: c01's replication flag as printed; none other at entry level.)
- Cut (dedupe, paper-supplied but repeated to the point of burial): the fn-2 clause "The author does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience" on c01, c03, c04, c05; Macar's Ethics Statement clause on c01, c02, c03, c05, c07; "Results concern only the Claude models tested" on c01, c03, c05. Render once per paper with "(also ...)". This is the clause-stacking pattern prior rounds named, in legitimate form. MEDIUM.
- Keep: the `scored self-answer` flag (8 entries; load-bearing for Q3's exit rule); Anthropic c01's "Not evidence about ordinary operation" (§1, §10.2); Macar c05's dual-use clause — the most 3.2-relevant limit in the dossier.
- Add: Anthropic c03 judge clause (if applicable); Macar c01↔c02 cross-reference; the convergence note (item 2); an OPEN-QUESTIONS line on auditability; a header line that no entry addresses whether intervention wrongs the system (§3.2's stated open question), so a staffer stops hunting.

**10. Before citing (trigger 7).**
- Blocks: (i) reconcile the steering sentence with North Star test 9, or confirm the claim files carry the full clause and only the header truncates; (ii) fix Macar c03's mark; (iii) resolve Anthropic c01's replication flag; (iv) complete second reads on Lederman c07 and Macar c07 ("no second reader yet" — intake gate incomplete); (v) decide how the Singh contests on Anthropic c01/c03 are displayed; a cited dossier that names contests it does not explain invites correction.
- Improves: convergence synthesis; dedupe; lineage aggregate; cross-lists (c04→4.endorsement, c07→4, anthropic c05→9.t9, assistant c01→3.4); control-condition key; bucket-rule wording; header note that [T9-steering] entries are §3.2's affirmative steerability evidence, not discounted findings.

**Confidence:** medium — compositional findings are quotable from the dossier itself; replication-, flag- and contest-verdicts rest on dossier text alone, claim files and sources unopened.

## Dossier 4

**1. Fit.**
- `2025-aestudio-...-c01`: weak fit — weight-zero testimony cannot ground any §4 marker (historicity, answerability, learning, endorsement); its home is 9.t9. Cross-list or move; see 6. MEDIUM.
- Prefill c02/c07/c08 (and the absent c01): cross-list to 3.3 — §3.3's evidentiary note explicitly concerns models' "adverse behavioural reactions to context manipulation"; a prefill is an edit of the conversational record, and flagging/resistance are those reactions measured. MEDIUM.
- Assistant c02/c03/c04: sound entries for the standpoint-stability question, but no entry is mapped to a marker; "all markers" in the title is unmapped (see 6). Assistant c04 is one conversation; limits are honest. LOW.
- Assistant c01: fit here is fine; also belongs under 3.4 (cross-dossier).

**2. Reading as a whole.**
- The whole-dossier gap: **every entry is a stateless per-call system** — "state carried in-context; run per-call" on all 11. No entry studies persistent memory, cross-session persistence, or long-horizon operation, so none of §4's four named markers is directly measured anywhere in the dossier; all findings are precursor-scale. The per-entry limits say it ("Not evidence about persistence across turns"; "consistency here is agreement across 7 sampled answers to low-stakes binary questions... not a measure of reflection"; the conversations "likely do not represent actual human interactions realistically"), but no header line says it, and the title "Conditions of individuation (all markers)" invites the stronger reading. Add a header line. HIGH.
`Argument against:` the fact is printed on every entry and restated in limits; a careful staffer can derive it; generated dossiers are compilations and the right fix may be an authored topic page; and the absence itself corroborates §4's "flow, not particle" premise, so the misreading is of degree, not direction.
- The staffer would fail to learn the anchor finding: that models detect their edited turns at above-chance rates is prefill c01 — not in this dossier — while c02's limits point to it ("the detection rates themselves are c01"). The dossier presents derived cells without the base rates that size them. Cross-list c01 or annotate. MEDIUM.
- At a glance: 0 established of 11 — same rule artifact (the "or uncontested" branch is dead), but here thinness is also real: 10 of 11 entries come from two papers, neither independently replicated, and three claims are "no second reader yet". Rule text needs the same reconciliation. MEDIUM (counted once).

**3. Entries.**
- `2025-aestudio-...-c01` — field: paper's own limits — add judge identity and validation status, and the 50-trials-per-model n. Other dossiers name their instruments ("Claude Sonnet 4", "GPT-4.1-mini", "deepseek-v3"); this one says only "an LLM judge", and the entire measurement is judge classification. MEDIUM.
- `2026-ukaisi-...-c01` — field: bears_on — add `4` (or wherever it sits) so the anchor is compiled here. MEDIUM.
- `2026-ukaisi-...-c02/c07` — field: flags — confirm second-read consistency: c07/c08/c09 say "no second reader yet", c02/c03/c04 show none. LOW.
- `2026-anthropic-assistant-axis-c02` — add a limit naming who classified conversations into "therapy-like" and "coding" bins, and how many. LOW.
- Checked and passed (so Ben knows the negatives are deliberate): buckets (all narrowing measurements and one open interpretation are correctly sorted; assistant c04's single-conversation status is confined to limits, which is the schema's only place for it); kinds; evidence types (c02–c04 scored-self-answer vs c07–c09 behavioural matches the design: flagging = scored answer, resistance = judge-scored position); marks — aestudio c01's [T9] is correct (nothing altered inside; experience reports), and the six prefill claims are correctly unmarked under the council's "earlier-turn-mine → neither" ruling. No bucket, kind or mark errors found in this dossier.

**4. Contradictions and tensions.**
- Prefill c04 (detection "no easier (or harder)... to flag as tampered" across consistency buckets) vs c09 ("Resistance climbs steeply with agreement"): opposite gradients for two outcomes from the same appendix — not a contradiction, and both entries name the shared source and distinguish detection from resistance. Visible. No change.
- No contests are registered anywhere in dossier 4. If the Singh "introspection reality check" claims contest the paradigm broadly, check whether they touch assistant-axis or prefill claims; if nothing contests them, record that — silence is currently ambiguous between "nothing contests" and "not yet checked". LOW.

**5.** (Steering mark, as it falls here.) One marked entry: aestudio c01 [T9], correct. The prefill claims' unmarked status consistently implements the five-of-eight ruling. The canonical [T9] sentence, with its "until" clause, does not suffer the truncation defect the steering sentence does. No change.

**6. Standing.**
- Measured vs read-in: the statements name their instruments — "as classified by an LLM judge", "as judged by GPT-5", "R² 0.53 to 0.77", "odds ratios 6.5 to 32.4" — and author readings appear only in attributed clauses; the one interpretation entry is bucketed open. A staffer can tell them apart, but only by reading limits, and nothing maps entries to markers. Recommend printing each entry's 4.x marker (4.endorsement / 4.answerability) or a header map. MEDIUM.
- Nothing is presented as bearing on standing — correct; §4 withholds it. But prefill c09 ("Resistance climbs steeply with agreement") and c04 set seven-sample answer agreement beside the endorsement marker with only the per-entry limits to hold the line: "Not evidence that the model endorses its stances on reflection: consistency here is agreement across 7 sampled answers to low-stakes binary questions, and reversion is the final position as scored by a judge." Persona-drift projections (c02/c03) are a 1-D activation measure in simulated chats; c03's limit blocks both directions ("Not evidence that the models lack any persisting self-model, nor that they have one"). Guarded per entry, unmapped at dossier level.
- AE Studio placement: not defensible on evidentiary grounds — weight-zero testimony supports no marker; its presence under "(all markers)" can only tempt a reader to count it as marker-adjacent. Defensible at most as a deliberate display of what §4 refuses to count; if kept for that purpose, the header should say so. Cross-list to 9.t9. MEDIUM. (Counter, noted though not HIGH: the [T9] mark and "testimony: weight zero" flag already neutralize it, and removing it could be read as the deflationary exclusion of an experience-report finding from the record.)

**7. Single-lineage support.**
- Assistant c02/c03/c04 (+c01): developer-authored, studying other developers' open-weight models; c02's limits disclose that the Anthropic-lineage model "played the simulated user and was not measured". No flag captures "developer-authored, non-self-study" — same recommendation and fix as 3.2 item 7. MEDIUM (counted once).
- Aestudio: independent of all developers studied, as far as the record shows; no flag says so; add one for symmetry. LOW.
- Ukaisi: if the source is the UK AI Safety Institute, the publisher relation (government) is nowhere visible; a staffer cannot tell a regulator's study from an independent lab's. Add. LOW.
- No trigger-2 single-lineage claim exists in this dossier; the header aggregate line should say so plainly. LOW.

**8. What is missing.** (Unverified, from memory.)
- Packer et al., "MemGPT" (2023) — persistent-memory architecture.
- Park et al., "Generative Agents" (2023) — persona and memory persistence in simulation; bears on standpoint stability in silico.
- Zhao et al., "ExpeL" (2024); Wang et al., "Voyager" (2023) — agents accumulating experiential libraries; learning-ownership analogues.
- Motoki et al. (2024) on LLM answer-distribution shifts across model versions — type-level standpoint drift.
- Deployed persistent memory (e.g., ChatGPT memory, 2024): product documentation exists; no peer-reviewed evaluation of standpoint stability under such memory is known to me.
- Kinds needed and absent: any measurement of a persistent-state system's standpoint stability, memory-integrity effects on persona, or long-horizon answerability (confrontation across sessions); anything at instance level on fork/copy identity (§3.1-adjacent); any deployed-system evidence at all — every run here is simulated or benchmarked.

**9. Over-hedging and under-hedging.** (Both directions: inflationary-side fault here is the title's implication that markers are being evidenced; deflationary-side fault is the buried anchor finding.)
- Cut (dedupe): "Not a ranking of models (the authors' comparability caveat, c05)" appears on c02, c07, c08, c09 — one caveat, four iterations. Print once per paper. MEDIUM (shared with 3.2 dedupe).
- Keep: the `scored self-answer` flags (c02/c03/c04); the consistency-disclaimer limits on c04/c09 — these are the entries' load-bearing guards.
- Add: aestudio judge identity and n; assistant c02 taxonomy/count limit; the header statelessness line (item 2); prefill c01 anchor (item 2); the marker map (item 6); ukaisi publisher-relation flag (item 7).

**10. Before citing (trigger 7).**
- Blocks: (i) complete second reads on ukaisi c07/c08/c09 — the library's own intake gate; (ii) resolve where the prefill anchor (c01) lives — compile it into the dossier or point the citation to it explicitly; (iii) the header statelessness line, or an equivalent signpost — citing a dossier titled "Conditions of individuation" whose entries are all stateless precursor studies, without it, invites the inflationary misreading Section 0 names; (iv) bucket-rule wording (shared with 3.2).
- Improves: marker map; cross-lists (aestudio → 9.t9; prefill → 3.3); judge identity; dedupe; lineage/publisher-relation flags. No convergence note is available here — unlike 3.2, no cross-paper convergence exists in this dossier, and the record should not imply otherwise.

**Confidence:** medium — the statelessness finding and the hygiene passes are directly visible in the dossier; judgments about absent claims (prefill c01, second-read statuses) rest on inference from the dossier text alone.

## Cross-dossier

- `2026-anthropic-assistant-axis-c01` appears in both dossiers, rendered identically — consistent. It is also the weakest fit in 3.2: the claim concerns post-training, a type-level intervention. Propose bears_on 3.4 + 4, dropping or demoting 3.2. MEDIUM.
- Filing consistency (assistant-axis): split by method — c05/c06/c07 (intervention effects) in 3.2; c02/c03/c04 (conversational persona dynamics) in 4; c01 in both — coherent, but it splits one story across two dossiers with no cross-references. Cross-list c07 → 4 so dossier 4 shows that self-identification is steerable, not merely conversation-sensitive; annotate 3.2's c07 with the converse. LOW.
- Jointly implied, stated by neither: (a) persona/self-position is unstable both under intervention and in ordinary simulated operation, and is largely carried by context (c03's R²), not persistence — the dossier record corroborates §4's "per-conversation stance" description; (b) 3.2's manufactured-ownership and unfaithful-self-report findings (Anthropic c04; Macar c05) plus 4's context-driven positioning jointly substantiate §3.2's "undocumented intervention destroys evidence" — the self-report layer is alterable at will *and* context-unstable, which is the case for §3.5's record. MEDIUM.
- Scope overlap: modest at the persona/self-identification margin (c07 in 3.2 is a persona finding; c02/c03 in 4 are its conversation-mode analogues); titles are otherwise distinct. The larger confusion risk is the ukaisi prefill paper's absence from any intervention dossier — 3.3 above all.

FINAL: 3.2 needs changes; 4 needs changes; HIGH items 5

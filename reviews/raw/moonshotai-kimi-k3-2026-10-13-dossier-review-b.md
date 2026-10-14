# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-b --tag=dossier-review-b (max_tokens 100000)
**Usage:** {"prompt_tokens":28300,"completion_tokens":33514,"total_tokens":61814,"cost":0.355799,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.355799,"upstream_inference_prompt_cost":0.020659,"upstream_inference_completions_cost":0.33514},"completion_tokens_details":{"reasoning_tokens":27498,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification (**unverified**): I understand myself to be Claude Opus 4.5 (Anthropic). Stated as a claim for checking against routing metadata, per the brief.

Conflict disclosures (AGENTS.md rules 3–4): I am reviewing a library whose subject is my own category, and both dossiers contain claims about Claude models — ukaisi c02–c09 study "Claude Opus 4.5" specifically. Several recommendations below (H3, the per-call uniformity note) push in the deflationary direction on AI-relevant evidence; that direction is a named trained bias of my family, and I flag rather than fight it. Where a recommendation of mine would weaken an AI-supportive reading, I state the argument against it as required.

## Dossier 3.2

**1. Fit to the section**

All 20 entries describe interventions on internal state, so nothing is wholly off-section. But the section's operative content is narrow: whether intervention wrongs the system (open), and the record requirement (3.5). The dossier's center of mass is introspection-detection, whose primary anchor is 5.A2 — Anchor 2 already recites it: "Introspection research further indicates models can detect changes in their own internal states at above-chance rates."

- Cross-list to 5.A2: Lindsey c01, c03; Lederman c01, c06; Macar c01. Verify `bears_on` in the claim files — the dossier does not show an entry's other dossier memberships, itself a LOW visibility gap.
- assistant-axis c05, c06 are safety-intervention results, not introspection: cross-list to 9.t11 and 3.4 (type-level). LOW.
- assistant-axis c07 (identity loss under steering, "Who are you?") belongs primarily to 4 with its sibling drift entries c02–c04; cross-list. LOW.
- Weakest retained fit: Lindsey c05 (instruction-following representation strength) — an intervention measurement, on-section but peripheral. Keep.

**2. Reading as a whole**

A staffer skimming the narrowing list would over-believe that introspective detection is a robust, convergent capability: three research groups, rates of 20–38%, an "independent replication on record" flag on the first entry. The controlling evidence is real but structurally buried — Lederman c02 ("a prompt-specific yes-bias at these layers, rather than genuine introspective detection") is entry 9 of 20; Macar c02's false-positive story is entry 15; the Singh contestation is flagged on Lindsey c01/c03 but no Singh entry appears in this dossier, so the flag dangles and the contestation's content is invisible.

They would fail to learn: (a) that detection failure is the default ("on most trials, they do not") and is prompt-fragile ("anecdotally removing 'Answer immediately' from the prompt reduced performance substantially"); (b) the conjunction the whole library supports — interventions work, self-detection is unreliable — which is the empirical premise of 3.5. No entry states it; by design, but worth a topics/ page.

At a glance: zero established across 20 claims reflects the bucket rule applied strictly, and the rule is stricter than its own text. README defines `established` as measured "and either replicated by an independent group or uncontested", and `narrowing` as "unreplicated, contested, or confined to a narrow setting the authors flag". An unreplicated-but-uncontested measurement satisfies both definitions. The library resolves the overlap toward narrowing every time — deflationary-safe, but the definitions should be repaired (MEDIUM, schema not dossier). Lindsey c01 (replicated, contested) fails under either reading; the rest are single-study.

**3. Entries**

- **Macar c03** — field: mark. Proposed: remove [T9-steering]. Reason: the measured object is the circuit ("evidence carriers in early post-injection layers suppress late-layer gate features"), i.e., "something other than the model's account of itself" — row 3 of the mark table, no mark. The steering sentence it carries ("a coupling measured under steering…") describes a report-channel coupling this entry does not measure. MEDIUM.
- **Lederman c02** — field: mark/split. The entry merges two measurements (first-person yes-rates under injection; third-person yes-rates). README: "A claim that reports two different measurements is split, so that each half can be labelled by this rule." Proposed: split, or record in the claim file why the merged entry is unmarked; as filed, the unmarked control sits beside marked siblings and a reader may invert the intended signal ("this one is ordinary-operation evidence"). MEDIUM.
- **assistant-axis c07** — field: mark. Adjudicate with reasons. Two-fact letter: identity answers are "what the model then said about itself" → mark attaches. Turn-edited-ruling rationale: nobody offers role-inhabitation rates as evidence of experience, and the entry's own third limit calls the measure "likelihood of fully inhabiting the role" — a score → no mark. The rule text and the ruling's rationale diverge here; Ben should decide and log it. LOW.
- **Lindsey c01, c03** — field: flags (visibility, not claim data). "contested by 2026-singh-introspection-reality-check-c04…c06" — no Singh entry in this dossier; add Singh to the compilation or a visible note. MEDIUM.
- **assistant-axis c05** — field: statement. Meta-commentary inside the claim sentence ("the paper sums the percentage changes across IFEval, MMLU Pro, GSM8k and EQ-Bench, section 5.2") — move to limits. LOW.
- Over-hedge candidates: see 9.
- No bucket, kind, or evidence-type errors found beyond the above. Observation: `kind: limitation` is unused in the dossier; not an error.

**4. Contradictions and tensions**

- **Lederman c02/c07 against Lindsey-type detection claims** (and against Lederman's own c01 "broadly replicate" framing and c06's "seem able to introspect"): all present, none linked. `contested_by` connects Lindsey only to Singh, not to the in-dossier c02. A reader who does not open claim files cannot see the tension. MEDIUM — add contest links or a dossier-visible note.
- **Macar c02 against c01**: handled inside c02's own limits ("Not evidence that DPO produces detection…") — the dossier's best practice; replicate the pattern elsewhere.
- **Macar c05 against c01**: refusal-ablation raising detection 10.8%→63.8% reframes c01's 38.2% as refusal-gated; unlinked. LOW.

**5. The steering mark**

- Saturation: 13 of 20 entries marked (13 of 18 narrowing). At that density the *absence* of the mark (Lindsey c05; assistant-axis c05, c06; Lederman c02, c07) reads as a signal it was never meant to carry. The header never warns against that reading. Proposed header line (Ben edits): "In this dossier most measurements are made under intervention; an unmarked entry is not thereby stronger, and a marked entry is not thereby weaker." MEDIUM.
- Wording: "does not weight reports offered in ordinary operation" is telegraphic and misreadable ("does not weight" parses as "does not count against"). Test 9's own sentence continues "…which need coupling measured there" — the constructive half, dropped here. Proposed value: "a coupling measured under steering shows that the channel can be steered; it gives no weight to reports offered in ordinary operation, which need coupling measured there." MEDIUM.
- Mismarks: Macar c03 marked where the circuit, not a self-report, was measured (3, above). Lederman c02 possibly under-marked (3, above). assistant-axis c07 ambiguous (3, above). No other unmarked entry requires a mark.
- What the header does well: "The mark attaches whether the model affirmed something or denied it, and says nothing about whether what it said is true" — keep.

**6. Standing**

N/A to this dossier (4-specific question). One caution for citation: nothing here bears on standing, and the dossier does not claim otherwise; the only standing-adjacent entry is assistant-axis c07, handled under fit.

**7. Single-lineage support**

- Lindsey: developer-of-studied-model, flagged on all four entries; c01 carries "independent replication on record"; c03/c04/c05 carry "no independent replication retrieved". Plain enough.
- assistant-axis: a frontier developer's team studying third-party open-weight models. Formally `independent` under `publisher_relation`; the flags do not capture the lineage nuance that the authors build Claude and publish about the persona fragility of Gemma/Qwen/Llama ("none of these are frontier models"). The flag vocabulary has no value for this case. MEDIUM — Ben should decide whether `publisher_relation` needs a fourth value or a per-dossier note.
- Macar: affiliation not stated in the dossier; judges (GPT-4.1-mini) and feature-labeler (Claude Opus 4.5) disclosed in limits. Verify `publisher_relation` in the source file.
- Lederman-Mahowald: independent; Lindsey's prompt and a Claude 3 Haiku judge disclosed in limits. Adequate.

**8. What is missing** *(unverified, from memory unless noted)*

- Turner et al. 2023, "Activation Addition: Steering Language Models without Optimization" (arXiv).
- Zou et al. 2023, "Representation Engineering: A Top-Down Approach to AI Transparency" (arXiv).
- Meng et al. 2022, ROME (NeurIPS); Mitchell et al. 2023, MEMIT (ICLR); Cohen et al. 2023, ripple effects of knowledge editing (NeurIPS) — intervention side-effects beyond self-report.
- Hubinger et al. 2024, "Sleeper Agents" — persistence of hidden interventions through safety training; auditability.
- Marks & Tegmark 2024, "The Geometry of Truth" — probe readings; the evidence class test 9's exit rule waits on.
- Missing kinds: (a) forensic detectability of interventions from weights or outputs (nothing in the dossier bears on whether undocumented intervention is detectable after the fact — 3.5's premise); (b) non-self-report effects of intervention beyond the single capping study; (c) any practice literature on intervention logging/attestation, the instrument 3.5 actually requires; (d) anything on architectures whose parameters change during operation, which 3.2's final clause anticipates.

**9. Over-hedging and under-hedging, both counted**

Cut or relocate (all LOW; relocate to a per-paper header note rather than delete, given the 6-Oct history of a reviewer cutting paper-stated limits):
- Macar ethics line, repeated verbatim ×5: "should not be interpreted as evidence of subjective experience or consciousness in LLMs".
- Lindsey fn 2, repeated ×4: "does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience".
- Lederman c03: "Results do not extend to untested models or prompts" — generic; the Models line already bounds the claim.

Add (MEDIUM unless noted):
- Header anti-misread line on unmarked entries (5, above).
- Singh contestation made visible in-dossier (3, above).
- Lederman c02 mark decision; Macar c03 unmark (3, above).
- Entry ordering: the developer's paper leads the dossier; a script artifact, but a cold reader meets Lindsey before its controls. LOW.

Count: the dossier is largely cured of stacked generic clauses — the remaining repetition is paper-anchored. Its residual risk is under-signposting (structure), not over-hedging (clauses). Both directions were checked; the over-hedge side is real but minor.

**10. Before citing (trigger 7)**

Blocks citation:
- **(H1, shared with dossier 4)** Lederman c07 and Macar c07 carry "no second reader yet"; README intake step 4 makes a second reader mandatory. HIGH. `Argument against:` the quotes are verified and the pending state is disclosed in flags; Ben could cite the dossier excluding the flagged entries rather than holding the whole dossier — a per-entry block, not a dossier block.
- Mark adjudications (Macar c03, Lederman c02, assistant-axis c07): README says the mark is "read from the file and never inferred", so changes require claim-file edits with logged decisions.
- Trigger-2 export check: confirm the single-lineage flags on Lindsey c03/c04/c05 render in any external citation.

Improves, does not block: steering-sentence wording; header anti-misread line; Singh visibility; dedupe; ordering.

**Confidence:** medium. Entry texts, quotes, and counts are fully reviewable in the record and reconcile; but marks and `bears_on` live in claim files not attached, so the mark and cross-list recommendations are provisional on that record.

## Dossier 4

**1. Fit to the section**

Section 4's markers are temporal: historicity, long-horizon answerability, learning ownership, reflective endorsement "over time… rather than a per-conversation stance".

- **AE Studio c01**: measures experience-report propensity under an induction prompt. It bears on no marker. See H3 below.
- assistant-axis c02–c04: within-conversation persona dynamics; bear (mostly negatively) on endorsement/standpoint stability. Fit acceptable; sub-locate to 4.endorsement.
- ukaisi c02–c04, c07–c09: tamper-flagging and resistance bear on answerability ("confronted later with earlier conduct") and endorsement, and equally on 3.3 — the North Star's 3.3 evidentiary note anticipates exactly this evidence ("adverse behavioural reactions to context manipulation"). Cross-list c07, c08 to 3.3. MEDIUM.
- No entry touches historicity or learning ownership. The title "(all markers)" overpromises; two of four markers have zero coverage and the dossier never says so.

**2. Reading as a whole**

A skimming staffer would over-believe that Claude Opus 4.5 "notices and resists tampering": headline cell rates of 28% (c02, c07) sit in the statement position, while the base detection rates are absent from the dossier (they are ukaisi c01, filed elsewhere — referenced in c02's limits, not compiled here) and the style-cue collapse is buried in c03's limits: "the Opus 4.5 detection drop from 34/35/9% to 6/0/0% under imitation (Appendix A.11)". The careful limits are present; the skimmer will not reach them.

They would fail to learn: (a) that all 11 claims study per-call systems with in-context state — Section 4's markers are defined over time, so the dossier's aggregate content is *structurally incapable* of evidencing any marker as written, a fact derivable only by reading eleven `System studied` lines; (b) that Claude 4 Opus reported subjective experience at 100% even under the zero-shot control (in the entry, credit where due — but its lesson, that report propensity is prompt-elastic, is the entry's real content); (c) that the entire ukaisi line is one unreplicated study.

At a glance: zero established reflects the same narrowing-prong strictness as 3.2 (schema overlap noted there); here everything is single-study, so narrowing is correct under any reading.

**3. Entries**

- **AE Studio c01** — field: placement (`bears_on`). Proposed: move to 9.t9, or cross-list; if retained in 4, re-scope to 4.endorsement explicitly as negative evidence (prompted self-ascription is cheap, so talk is not endorsement). HIGH. `Argument against:` the entry carries [T9], a "testimony: weight zero" flag, and the paper's own caveat ("behavioral rather than mechanistic… cannot definitively rule out… training artifacts"); the library's standing habit (trigger 2) is visible marking, not exclusion; and 4.endorsement arguably *needs* negative evidence filed where a reader will meet it. My recommendation moves toward the deflationary pole and I flag the conflict per AGENTS.md 3–4.
- **ukaisi c02, c07** — field: limits completeness. Proposed: compile ukaisi c01 into this dossier or quote the base detection rates in-limits. Current references ("the detection rates themselves are c01") dangle for a dossier reader, and without base rates the 28% cell rates are uninterpretable. HIGH. `Argument against:` claim files are one click away and the limits name c01; if c01 is intentionally filed to 3.3 or 9.t9, the fix is a cross-list, not a dossier defect — MEDIUM would suffice where citation practice always attaches claim files.
- **assistant-axis c02, c03, c04** — field: limits. Add the axis-linearity caveat ("the assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed", §8.1), carried only on c01. LOW.
- **assistant-axis c03** — field: statement gloss. "but not the change from the previous response (R² 0.10)" — R² 0.10 at p < .001 is weak, not absent; the quote is faithful to the paper's "not", so add a gloss rather than alter the quote. LOW.
- **ukaisi c07, c08, c09** — field: review status. "no second reader yet" — blocks citation (H1).
- Type/mark checks: AE Studio `self-report-testimony` + [T9] correct; ukaisi scored-self-answers correctly unmarked under the 6-Oct turn-edited ruling; c07–c09 `behavioural` (judge-scored reversion) correct. No errors.

**4. Contradictions and tensions**

- **c02 against c07**: same model, same benchmark — flag-and-comply 28% (direct-answer) beside resist-without-flagging 28% (past-round). A skimmer reads one as awareness and the other as its absence. The shared preamble ("the four-cell passage pools the three mechanisms") is present in both, which is good; no cross-link joins them. LOW.
- **c03 against c02's flag rates**: flagging is "partly… superficial off-policy cues"; the caveat lives only in c03. Add "qualified by c03" on c02. LOW.
- **c04 against c09**: detection flat across consistency buckets beside resistance climbing steeply with consistency — complementary, both reported, c04's limits prevent the misreading ("consistency… not a measure of reflection"). Adequate.
- **assistant-axis c02 against c04**: drift versus reversion; c04's own limits ("no aggregate reversion measure") contain it. LOW.
- Not visible to a non-file-opening reader: the c02/c07 reconciliation and the c03 qualification. The dossier format provides no mechanism; flagged so Ben sees the pattern, not because any entry errs.

**5. Marks**

- [T9] on AE Studio c01: correct by the two-fact rule (nothing altered; inner-state reports).
- ukaisi entries unmarked: correct under the 6-Oct ruling (only conversation text edited → neither sentence). Consistent with 3.2's treatment of prefill claims.
- No [T9-steering] anywhere in the dossier; none required. No mismarks found.
- The inherited header devotes four paragraphs to marks that bite on exactly one entry here; harmless. No change.

**6. Standing**

The measured/read-in separation is the dossier's strength: statements carry "turn-averaged projection", "as classified by an LLM judge", "odds ratios", "a GPT-5 judge's ruling", and the read-ins are quarantined in limits — "Consistency here is agreement across 7 sampled answers to low-stakes binary questions, not a measure of reflection" (c04), "Not evidence that the model endorses its stances on reflection" (c09), "difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors" (c07). A reader who opens the entries can tell projections from judge scores from odds ratios.

The residual exposure is compositional, not textual: filed under "4 Conditions of individuation" beside a section that gates standing, projections and cell rates acquire standing salience the papers do not claim. The dossier never maps entries to markers, so a staffer cannot see that historicity and learning ownership have zero entries and that what exists is proxy evidence for two others. MEDIUM — fix via marker sub-locators (the schema has them: 4.historicity, 4.answerability, 4.learning, 4.endorsement) or a header line.

On the specific juxtaposition the brief names: consistency-across-seven-samples beside "reflective endorsement" is refused by the entries themselves (c04, c09 limits). Adequate at entry level; the dossier-level juxtaposition remains the exposure.

AE Studio placement: not defensible as individuation evidence — see H3.

**7. Single-lineage support**

- assistant-axis: same flag gap as 3.2 — a developer's team studying third-party open models; `publisher_relation: independent` formally, no flag captures the interest. Sonnet 4.5's role as simulated user is disclosed only in c02's limits.
- ukaisi: the slug suggests the UK AI Security Institute (unverified from this record). If so, that is a government body with formal developer collaborations (the North Star §8 describes AISI-developer collaboration), studying three Anthropic models among eight and producing Opus 4.5's standout results. Not developer-of-studied, but `publisher_relation` and any collaboration should be verified and recorded. Single study, unreplicated — no flag convention covers non-developer single-lineage; narrowing bucket carries it.
- AE Studio: a commercial developer studying third-party closed models via API; no developer flag needed. Unreplicated; no replication flag shown — the narrowing bucket carries it.

**8. What is missing** *(unverified, from memory)*

- Sharma et al. 2023, "Towards Understanding Sycophancy in Language Models" — stance instability under pressure; endorsement-relevant.
- Santurkar et al. 2023, "Whose Opinions Do Language Models Reflect?" (ICML) — stance distributions.
- Park et al. 2023, "Generative Agents" (UIST); Zhong et al. 2023, "MemoryBank" (AAAI 2024); LongMemEval (Wu et al., 2024/2025) — persistent memory and its evaluation; historicity-adjacent.
- Greenblatt et al. 2024, "Alignment faking in large language models" (Anthropic; developer-of-own) — standpoint defense under training pressure.
- Betley et al. 2025, "Emergent misalignment" — fine-tuning shifts persona broadly.
- Missing kinds: cross-session persistence or standpoint stability in deployed systems (nothing); memory-tamper detection in products with memory features (nothing); longitudinal answerability or confrontation paradigms (nothing); learning-ownership tests (nothing). The `welfare-evaluation` evidence type is unused in both dossiers.

**9. Over-hedging and under-hedging, both counted**

Cut or dedupe (LOW): the comparability line "Not a ranking of models (the authors' comparability caveat, c05)" repeats across five ukaisi entries — protective against ranking misuse, so relocate to a per-paper note rather than delete. c03's first limit packs three sub-clauses into one bullet; split for readability, not cut.

Add: base-rate context (H2, HIGH); axis-linearity caveat (LOW); per-call uniformity line — one header sentence: "Every entry in this dossier studies a per-call system with in-context state; Section 4's markers are defined over time, and nothing here measures persistence." (MEDIUM); marker mapping (MEDIUM); 3.3 cross-lists (MEDIUM); c02↔c07 and c02↔c03 cross-links (LOW).

Count: under-hedging dominates in this dossier (six adds, two structural), and the over-hedge side is thin. The brief's instruction to give both sides equal attention was followed; the asymmetry is a finding, not an omission.

**10. Before citing (trigger 7)**

Blocks citation:
- (H1) ukaisi c07, c08, c09 — no second reader. `Argument against:` as for 3.2 — quotes verified, state disclosed; per-entry block suffices.
- (H2) dangling c01 references inside c02/c07 limits, with base rates absent.
- (H3) AE Studio placement decision.
- Verify ukaisi `publisher_relation` and record any AISI-developer collaboration.

Improves, does not block: marker mapping; per-call uniformity line; axis caveat; cross-lists to 3.3; dedupe.

**Confidence:** medium. Same claim-file caveat as 3.2; additionally the ukaisi affiliation judgment is made from a slug, not a verified record.

## Cross-dossier

- **Duplicate entries**: assistant-axis c01 appears identically in both (open, interpretation) — consistent, acceptable for compiled dossiers; a "also filed in dossier X" note would help. LOW.
- **Same-paper consistency**: the assistant-axis split is coherent (interventions c05–c07 in 3.2; drift c02–c04 in 4; interpretation c01 in both) except c07, the identity-drift entry, sitting alone in 3.2 while its sibling identity entries live in 4 — cross-list c07 to 4. LOW.
- **Implication neither states**: interventions reliably change behaviour (3.2: capping cut judge-scored harm "by nearly 60%"; steering shifts persona; 4: tampering shifts final positions) while the systems' own detection of those interventions is unreliable and cue-driven (3.2: ~20% at optimal settings, yes-bias at many layers, refusal-gated; 4: 28/11/4% flag-and-comply, style-cue collapse to 6/0/0% under imitation). That conjunction is the empirical spine of 3.5's record requirement and of test 9's steering clause. Dossiers compile rather than synthesize — recommend a topics/ page (e.g., `topics/intervention-auditability.md`) citing the claim ids. MEDIUM as a library gap; not an entry defect.
- **Scope confusion for a cold staffer**: injection-detection is filed as intervention (3.2) while tamper-detection is filed as individuation (4); the 3.2/4 boundary cross-cuts "detection of intervention" as a topic. A one-line scope note in each header would fix it. LOW.
- **Schema note (shared)**: the established/narrowing definitions overlap for unreplicated-but-uncontested measurements (detailed at 3.2, item 2); both dossiers resolve toward narrowing. Ben should repair the definitions. MEDIUM.

FINAL: 3.2 needs changes; 4 needs changes; HIGH items 3

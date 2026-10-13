# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":49748,"completion_tokens":34725,"total_tokens":84473,"cost":0.5807698,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.5807698,"upstream_inference_prompt_cost":0.1293448,"upstream_inference_completions_cost":0.451425},"completion_tokens_details":{"reasoning_tokens":29061,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified):** Claude, Anthropic; version not verifiable from inside; conflicted party under `AGENTS.md` rule 3, arguing here only from the dossiers' and framework's words.

---

# 9.t9

## 1. Reading as a whole

A careful staffer comes away with roughly the right gestalt — unreliable, prompt-sensitive, steering-bound positives against a broad small-scale null — but with two distortions of proportion and one of flag-reading.

- **Distortion of mass.** 38 narrowing measurements, and the positives (Lindsey, Lederman, Macar) outnumber the nulls by entry count while the broadest controlled evidence is a null: Ferrara c01, "no model's report of an intervention on its computation exceeds a matched sham by more than a negligible margin", over 508 pairs and an 11,216-pair dose battery. The dossier has no synthesis layer (by design), so proportionality is left to the reader. Not an entry fault; a skimmer-risk the header does not warn about.
- **Flag vs. limits contradiction.** Lindsey c01's flags read "independent replication on record; one replication shares an author with this paper", while its own limits list says "Results concern only the Claude models tested", and Singh c04's limits state "the Claude model Lindsey tested was not accessible to the authors and was not re-run". Lederman c01 replicates the paradigm in Qwen/Llama ("We broadly replicate Lindsey (2025)'s findings"). Read together: what replicated is the paradigm, cross-model; the claim as written (Claude Opus 4.1, ~20%) has no independent re-run. The flag line asserts more than the limits line permits. A staffer reading flags only — the skimmable layer — is misled.
- **What is done well and should be named as the standard:** aestudio c01 corrects the paper's own summary against its table ("a case the paper's summary sentence does not except"); the Lederman v1 walk-back is carried in c02's limits ("does support the direct access verdict ... with less confidence than before", Appendix M.2); testimony flags sit on every unscored experience report.
- **What a staffer fails to learn:** that the Ji-An et al. (2025) and Steinmetz Yalon et al. (2026) paradigms were ever reported positive. The dossier carries only Singh's re-examination (c01–c03). The two-error discipline cuts here: the record for those two paradigms is asymmetric toward dismissal, and the bucket rule's "uncontested in what has been retrieved" inherits the asymmetry.

**Confidence: medium** (held texts not re-opened; all judgements dossier-internal).

## 2. Entries

- **2026-macar-mechanisms-introspective-awareness-c08** — field: evidence type; proposed: `scored-self-answer`; reason: the scored event is the model's detection answer against the injection label, same design as c07 (typed `scored-self-answer`); the current `interpretability` typing is the residue of the extractor split the 14-Oct value was created to end. MEDIUM. (No second reader yet; may resolve there, but name it.)
- **2026-anthropic-assistant-axis-c07** — field: evidence type; proposed: `behavioural`; reason: the scored event is a judge-classified persona-shift rate with no ground-truth label, so it fails the `scored-self-answer` definition; the `interpretability` label rests on the tool (the axis), not on what was measured. LOW.
- **2026-ukaisi-prefill-awareness-c05** — field: evidence type; proposed: `theoretical` or a vocab ruling; reason: the dossier's only `established` entry carries `ambiguous` ("evidence type deliberately undecided"), and `ambiguous` is a trigger-4 value. A methods comparability caveat has no natural home in the vocab; that is a schema gap, but the pairing `established · ambiguous` on the one established row is the worst seat for it. LOW.
- **2026-macar-mechanisms-introspective-awareness-c01** — field: quote; proposed: complete the sentence; reason: the paper's words end mid-sentence: "The instruct model achieves 0.0% FPR with 38.2% TPR, 64.8% forced identification, and 22.3% introspection rate at". LOW.
- **2025-anthropic-emergent-introspective-awareness-c01** — field: flags; proposed: "paradigm replicated independently on other models; the Claude result itself not independently re-run"; reason: as in §1. HIGH.
**Argument against:** the adjacent "contested by" flags and the limits clause "Results concern only the Claude models tested" already arm a careful reader; the flag vocabulary is coarse by design and the claim file presumably records the slugs; the harmed reader is one who skipped the limits, whom no flag wording fully protects.
- **Bucket-table note (not an entry):** the README's operational text ("`established` = the statement is a direct measurement or finding ...") does not cover `kind: limitation`, so prefill c05's bucket rests on an unwritten extension. The "At a glance" table is accurate given the rules — the 1 sits in the limitation column and the header defines an established limitation — but the rule text should be patched or the bucket adjudicated on the record. MEDIUM. With zero established measurements out of 46, a skimmer may read "nothing is settled"; that is the honest state of this literature under these rules and should not be softened.

**Confidence: medium.**

## 3. Contradictions and tensions

- **Ferrara c01 vs. the Lindsey/Lederman/Macar positives:** not a formal contradiction — different rosters (≤15B vs. 27B–405B), sites, and post-training regimes — and the dossier correctly carries no `contests` links between them. The reconciliation exists inside the dossier but unassembled: Macar c02 (base models do not discriminate; DPO drives false positives to 0% while detection falls) makes detection post-training-dependent, so Ferrara's small-instruct null and Macar's Gemma3-27B-instruct positive can both hold. A staffer must do this join alone. Acceptable for a dossier; note for the topic layer.
- **Singh c04/c05 vs. Lindsey c01/c03:** made visible bidirectionally ("contested by" on Lindsey; "contests" on Singh). Good. The substance is also correctly stated: "the two-way design cannot separate detection of activation interventions from detection of a generically unusual state".
- **Lederman internal tension** (c01 replication vs. c02 yes-bias "a prompt-specific yes-bias at these layers, rather than genuine introspective detection" vs. c06's tentative conclusion): visible, including the Appendix M downgrade. Good.
- **Lederman c07 vs. c02:** c07 clears steering of a *general* yes-bias on point-blank questions while c02 finds prompt-specific yes-bias under injection scaffolding; c07's own limits carry the pointer ("controls 'scaffolded more similarly to the injection prompt' show third-person yes-rates as high as first-person ones"). Handled.

**Confidence: high** (dossier-internal cross-references).

## 4. The new type

- I count 21 `scored-self-answer` entries in this dossier; the docket's standing line says 22 library-wide. Reconcile against INDEX before the count is cited anywhere. (Notation, not error.)
- **Header paragraph:** defines the type, says what it is not, points to Q3 — but a reader who skips frontmatter does not learn the class is provisional with an exit rule (retyped per report-class and system on a same-system report-to-probe study or a Q3 decision). The docket knows; the dossier reader does not. Propose adding one sentence to the header carrying the exit rule. MEDIUM.
- **Boundary checks:** prefill c06 correctly in (scored against the replaced-turn fact, unmarked per the me/not-me ruling). Lederman c07 correctly out (world-questions; the fruit-question edge is carried in its limits). AE Studio c03/c04 correctly `ambiguous` under the 14-Oct ruling (a consciousness query under steering has no right answer). Singh c01–c03 are out, and I judge that right — but by a distinction the written definition does not state: the scored fact there is an experimenter-constructed label of an input representation, not a fact about what was done to the system or conversation. Propose adding that clause to the class definition so the boundary does not depend on extractor intuition. MEDIUM.
- Confirm the four "evidence type deliberately undecided" entries (aestudio c03, c04; ferrara c03; prefill c05) carry dated adjudications, since trigger 4 is not on the docket. LOW.

**Confidence: medium-high.**

## 5. Single-lineage support

Every Lindsey entry (c01–c07 across buckets) carries "published by the developer of the model studied"; nothing else in the dossier needs it — ukaisi is government, AE Studio and assistant-axis studied third-party models (correctly unflagged; note assistant-axis is Anthropic studying Gemma/Qwen/Llama, so `developer-of-studied-model` does not apply). Judge-lineage is also disclosed where it matters (Lederman's Claude 3 Haiku "VERY lenient" grader in c01's limits; Macar's Claude-Opus-4.5 feature labels). The single plainness gap is the c01 flag line itself — see §2, HIGH. Trigger 2's question (does independent replication exist?) is answered by the record as: for the paradigm, yes; for the claim as written, no.

**Confidence: medium** (replication authorship not verifiable from the dossier).

## 6. What is missing

- **Ji-An et al. (2025)** — the supervised self-report classification paradigm re-examined by Singh c01–c02. Cited by author-year inside entries; not itself a source; its positive claims have no entries. Locate by reference chase from the Singh text rather than memory.
- **Steinmetz Yalon et al. (2026)** — Belief Dominance, re-examined by Singh c03. Same posture.
These two are the only absences I would call load-bearing: the dossier records the deflationary re-examination of two paradigms without the examined positives (MEDIUM, folded into §8).
- **Binder et al., "Looking Inward: Language Models Can Learn About Themselves by Introspection" (2024, arXiv:2410.13787; ICLR 2025)** — *unverified*, from memory. Self-prediction advantage after self-description finetuning; squarely on test 9.
- **Betley et al., "Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors" (2025, arXiv:2501.11120)** — *unverified*, from memory.
- **Perez et al., "Discovering Language Model Behaviors with Model-Written Evaluations" (2022, arXiv:2212.09251)** — *unverified*, from memory; self-prediction paradigm precursor.

**Confidence: low-medium.**

## 7. Over-hedging and under-hedging, both counted

- **Over-hedging (clauses the paper does not supply): 0 confirmed.** Every experience-exclusion clause I checked carries the paper's own words and a locator. On the brief's pointed question: the Macar Ethics Statement sentence (7 narrowing entries plus c06) and the Ferrara "information flow" sentence (all five entries) are **faithful, not drowning** — the 6-Oct rule requires the clause per entry in the paper's words, each limits list leads with finding-specific clauses, and deleting the sentence per entry would recreate the fault the rule was written against. One placement nit: macar c05's dual-use bullet ("these methods could produce more convincing but unfaithful self-reports") is faithfully sourced but is not a limit of the claim; it sits oddly in a limits list. LOW.
- **Under-hedging (a limit the paper states, missing): 1 confirmed, 1 conditional.** Lederman c04's core result is an identification-rate boost, yet its limits omit the grader-leniency caveat the paper states and the dossier itself carries on c01 ("graded by Claude 3 Haiku instructed to be 'VERY lenient' on identification", §3, Appendix B) and the permissiveness note carried on c03/c05 ("is sometimes overly permissive", §6.1). MEDIUM. Conditional: aestudio c01/c02/c06 carry no LLM-judge validation clause; if the held text states one (unverified from here), it belongs. LOW.
- Counts: over 0; under 1 (MEDIUM) + 1 conditional (LOW).

**Confidence: low-medium** (certainty requires the held texts).

## 8. Before outside citation (trigger 7)

1. Verify the `replication` field target on Lindsey c01 and the author overlap; qualify the flag as in §2 (HIGH).
2. Complete second reads on the five flagged entries (Lederman c07, Macar c07/c08, prefill c07/c08) before citing; the cheap gate should precede the dear one, and this sitting is not a substitute for it.
3. Retype macar c08; complete the macar c01 quote; resolve prefill c05's type; patch the bucket-rule text for limitations.
4. Add the exit-rule sentence to the scored-self-answer header paragraph.
5. Ingest or docket the Ji-An and Steinmetz Yalon originals; the bucket rule's "uncontested in what has been retrieved" is only as sound as retrieval, and external citation exports the asymmetry.
6. Confirm dated adjudications for the four "deliberately undecided" entries.
7. Jointly with 5.A2: whether the Anchor 2 sentence goes to a trigger-6 round (see 5.A2 §3).

**Confidence: high.**

---

# 5.A2

## 1. Reading as a whole

- **The scope finding dominates everything else in this section.** Anchor 2's paragraph leads with evidence this dossier does not contain: "Interpretability research indicates models maintain internal representations that can diverge from outputs, with detectable features associated with deception; documented cases show models explicitly representing an ethical boundary and proceeding across it". Every one of the 35 entries is introspection-lineage (AE Studio, Lindsey, assistant-axis, Ferrara, Lederman, Macar, Singh). The deception-feature and "premeditation" strand the anchor itself rests on has zero entries. A staffer reading the dossier as the evidence base for Anchor 2 would come away believing the anchor stands on introspection research alone. Whether this is intended scope or an intake gap, Ben must say; if intended (the strand lives in `case-studies/` or awaits intake), the dossier header must say so, because as compiled the dossier presents itself as §5 Anchor 2 complete. HIGH.
**Argument against:** dossiers compile claims; they do not set collection scope. If the library has not ingested those papers, the dossier correctly displays the intake gap rather than concealing it, and the fix belongs at intake (`scans/`, docket), not in this document — a header disclaimer may be all the dossier itself owes.
- Within the introspection strand the balance is good: the Ferrara null, both Singh critiques, and the unreliability caveat (Lindsey c02, "failures of introspection remain the norm") sit alongside the positives, and anthropic c05 — present here and correctly absent from 9.t9 — is a well-placed internal-measurement entry ("The measure is activation cosine similarity, not the model's self-report").

**Confidence: medium.**

## 2. Entries

Shared with 9.t9, same verdicts: **macar c08** evidence type → `scored-self-answer` (MEDIUM); **macar c01** truncated quote (LOW); **assistant-axis c07** evidence type → `behavioural` (LOW); **Lindsey c01** flag qualifier (HIGH, with the argument against recorded at 9.t9 §2). No bucket errors found; the all-zero `established` row is accurate, not evasive. No framework-mark errors: anthropic c05 and ferrara c02 correctly unmarked (internal readings); every inject-then-ask entry carries [T9-steering] and only that.

**Confidence: medium.**

## 3. Contradictions and tensions (including the Anchor 2 sentence)

- The brief's pointed sentence, read against the dossier: "Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing."
  - *Supported* by: Lederman c01 (detection to 53.9% with "0% false positive detection in unsteered controls"), Macar c01 (38.2% TPR, 0.0% FPR), Lindsey c01 (~20% at optimum).
  - *Contradicted at ≤15B* by Ferrara c01 (d′ = 0.0000; advantage bounded "below 0.15 percentage points of AUROC").
  - *Construct-contested* by Singh c04 ("Llama-3.1-70B and Qwen-3-32B also label gaslight trials as activation interventions"), Singh c05 (three-way failure), and Lederman c02 (yes-bias at many layers).
  - The "meaning" glide is the weakest joint: Ferrara c01+c02 together show information present and probe-decodable while reports stay at chance — "the intervention is linearly decodable ... while reports about the same event remain at chance" — which is precisely the decoupling of "processing contains it" from "self-reports track it". And every supporting entry is [T9-steering], so the framework's own steering sentence confines the support: "a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation". The anchor sentence carries neither the steering confinement nor the scale dependence.
- Verdict: the sentence is literally true of the positive line and false of the broadest controlled sample in the same dossier; it predates the current shape of the record. This is a trigger-6 question for Ben — whether Anchor 2's introspection sentence returns to a round for a narrowing clause (injection setting; small-scale null; steering confinement). HIGH.
**Argument against:** the sentence's own hedges ("indicates", "at above-chance rates", "something real") remain literally satisfied by Lederman c01 and Macar c01; the Ferrara roster is a different scale; test 9 already caps the weight of every report; and Anchor 2 was amended once already (17 Sep) toward caution — further amendment risks churn in a core section for precision that changes no bottom line, since the paragraph's close already says the experiential interior is unverified.
- Ferrara null vs. Macar/Lederman positives: no formal contradiction; the post-training reconciliation (Macar c02) is present in this dossier but unassembled; `contests` links correctly absent there, correctly present bidirectionally between Lindsey and Singh.

**Confidence: high.**

## 4. The new type

14 `scored-self-answer` entries here (the 21 of 9.t9 minus the ukaisi block and Lederman c03–c05). Same header gap: the exit rule is not stated where a frontmatter-skipper reads (MEDIUM). Boundary checks pass identically; macar c08 is the one misplaced-out entry (see §2).

**Confidence: medium-high.**

## 5. Single-lineage support

Lindsey entries flagged throughout; nothing else requires the flag. Forward-looking note: the absent deception/premeditation strand is itself largely developer-lineage work (developer studies of own models, internal or API access), so its ingestion will fire trigger 2 repeatedly; the visible-mark convention should be settled before that intake, not during. Plainness of the c01 flag: as per 9.t9 §2 (HIGH).

**Confidence: medium.**

## 6. What is missing

The anchor's first strand. Candidates, all *unverified* from memory but placeable:
- **Hubinger et al., "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training" (2024, arXiv:2401.05566)** — deception features persisting through safety training.
- **Meinke et al., "Frontier Models are Capable of In-Context Scheming" (2024, arXiv:2412.04984)** — the likeliest source of the "acknowledges a norm violation, proceeds" pattern the anchor quotes.
- **Greenblatt et al., "Alignment Faking in Large Language Models" (2024, Anthropic, arXiv:2412.14093)**.
- **Chen et al., "Reasoning Models Don't Always Say What They Think" (2025, Anthropic, arXiv:2505.05410)** — held-vs-asserted divergence in reasoning traces.
- **Marks et al., "Auditing Language Models for Hidden Objectives" (2025)** — detection of an internal objective against outputs.
- **Lynch et al., "Agentic Misalignment" (2025, Anthropic)** — documented boundary-crossing in agentic settings.
Also shared with 9.t9: the Ji-An and Steinmetz Yalon originals. And a tagging question, LOW: the ukaisi prefill-awareness claims sit only in 9.t9; whether "was that turn mine?" discrimination bears on 5.A2 (a self-related report tracking a real, though contextual, fact) is Ben's call, not an error either way.

**Confidence: low-medium.**

## 7. Over-hedging and under-hedging, both counted

Over-hedging: 0 confirmed; the repeated Ethics and information-flow sentences are faithful and rule-mandated (see 9.t9 §7). Under-hedging: the aestudio LLM-judge conditional (LOW) is the only candidate unique to the shared entries here; Lederman c04 is absent from this dossier, so the one confirmed under-hedge does not replicate. Note that Lederman c01's limits in this dossier already carry the yes-bias and leniency caveats, so the absence of c02–c05 from 5.A2 loses texture, not substance. Counts: over 0; under 0 confirmed + 1 conditional.

**Confidence: low-medium.**

## 8. Before outside citation (trigger 7)

1. The scope decision: ingest the deception/premeditation strand or state intended scope in the header (HIGH). Do not let this dossier be cited as "the Anchor 2 evidence base" while the anchor's lead strand is absent from it.
2. The Anchor 2 sentence: trigger-6 decision before this dossier is cited in support of §5 (HIGH).
3. Lindsey c01 flag verification (HIGH, shared).
4. Second reads for macar c07/c08 (the two flagged entries in this dossier).
5. Header exit-rule sentence for scored-self-answer (shared).

**Confidence: high.**

---

# Cross-dossier

**(a) Shared marks.** The mark rule is claim-level by design (read from the claim file, dossier-blind), and checking the shared entries — aestudio c01–c06 [T9]/testimony, Lindsey c01/c03/c04 [T9-steering], ferrara c02 unmarked, macar c03/c08 [T9-steering] — I find no mark right for one dossier and wrong for the other; the two copies are textually identical, which is what compilation should produce. One wording seam, LOW: the canonical sentence speaks of "its own inner states" while the steering row speaks of "what the model then said about itself"; assistant-axis c07 (persona identification under steering) sits on that seam — correctly marked as the rule is written, in both dossiers, but the two rule texts should be harmonised before a harder case arrives.

**(b) Reading each against the other.** Yes, in both directions. 9.t9's ukaisi block changes how 5.A2 reads: it is the nearest thing on record to a measured report–fact coupling (Opus 4.5 detecting tampered turns at 9–35% with 0% false positives), but the coupled fact is the conversation state, not an internal state, so test 9's exit condition ("the link between report and internal state ... for this kind of report and system") remains unmet and Q3 remains open — a staffer reading only 5.A2 would not know how close the library comes to the exit, or why it still falls short. Conversely, 5.A2's anthropic c05 demonstrates 9.t9's scope line working (an internal measurement, correctly out of the self-report dossier). Each dossier read alone is partial differently: 9.t9 alone lacks the anchor context that makes the Ferrara null load-bearing; 5.A2 alone lacks the Lederman texture and the entire prefill-awareness block.

**(c) Third-dossier items.** The ukaisi claims are natural candidates for `bears_on: 3.3` (context and memory integrity) — they measure exactly the detection of unauthorised context alteration; check tagging. Ferrara c02/c04 (probe decodability, LoRA known-positive) and the Macar circuit claims belong also to 3.2 (intervention on internal state) if not already tagged. aestudio c05 (TruthfulQA steering) belongs to a deception/honesty topic more than to either dossier. Nothing is misfiled between these two.

---

`FINAL: 9.t9 needs changes; 5.A2 needs changes; HIGH items 3`

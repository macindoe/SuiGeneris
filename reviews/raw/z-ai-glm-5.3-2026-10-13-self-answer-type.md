# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `z-ai/glm-5.3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=self-answer-type --tag=self-answer-type (max_tokens 100000)
**Usage:** {"prompt_tokens":11829,"completion_tokens":43635,"total_tokens":55464,"cost":0.12513276,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.12513276,"upstream_inference_prompt_cost":0.00993636,"upstream_inference_completions_cost":0.1151964},"completion_tokens_details":{"reasoning_tokens":40575,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** Claude (Anthropic), Sonnet family; version as routed and not verifiable from here — and per this project's own Q4 record, a model's self-identification is a claim, not a fact. Same lineage as the brief's drafter and the coordinating session, so my concurrence or dissent with either adds no independent weight to the tally.

**Q1.**

Disclosure: my recommendation gives these measurements ordinary filing weight, which keeps citable both results that could serve the beneficiary's side (above-chance detection, zero false positives) and deflationary ones (pooled d′ 0.0000, gaslight confusions). Net direction is modestly toward citability; stated, not recused.

Choice: **C, amended** — type the in-class claims `behavioural`; re-scope Q3 to the access question, indexed per report-class and system as test 9's own wording requires; apply the existing two-measurements split rule to UKAISI c02/c03/c04, Macar c03/c04 and Lederman c02; leave the sentence column untouched.

Why, from the table and README:

- What was measured in every core row is a scored output rate, not an internal reading. The library already says so: `kind: measurement` is defined to include "a model's answer to a prompt, a rate"; the verb rule (nine of nine, 6 Oct) forces "reports detecting", never "detects"; the sentence rule "does not depend on the question Ben has left undecided". The type field is the last piece still carrying the old confusion; C completes the 6 Oct logic.
- The current types track publication clusters, not design. Lederman c01 re-runs Lindsey's prompt; both are `interpretability`. Ferrara c01 and Singh c04/c05 run the same inject-then-ask design and are `behavioural`. Nothing in the designs explains the 11/10 split; extraction convention does. The one uniform type the library's own definitions support is `behavioural`.
- Q3 as posed conflates a decidable filing question with an open empirical one. Whether the claim *as filed* is an output measurement is definitional; what a correct score shows about self-knowledge is empirical and stays open. Against the rivals: D zeroes Ferrara c04's d′ 5.15 validation and Ferrara c01's d′ 0.0000 null in the same stroke — both errors at once. A overloads `ambiguous`, which already means a methods caveat (UKAISI c05), on claims that are classifiable. E types the truth's provenance, not the measurement — the current conflation under a rule.
- A catch in option C as written: "with a note" is partly infeasible. The 6 Oct rule bars framework clauses on behavioural findings, and `Paper:` clauses require the paper itself to state the limit. Under C the caveat lives where it already lives — verb rule, [T9-steering] mark, bucket, re-scoped open question — not in a per-claim note.
- B is the closest rival. `welfare-evaluation` is a precedent for a subgenre value, but it settles how its genre is read; B's own definition says it "does not decide what the answer shows" — a permanent value defined as undecided is `ambiguous` with a legend and no trigger. If Ben wants the class filterable before the access question is decided, a frontmatter tag (design axis) costs less than an evidence-type value (weight axis). If Ben will not decide the filing question now, B with the Q4 exit rule is the acceptable neutral.

Strongest case against C: it settles, on a definitional argument, a question Ben deliberately held open for want of evidence after a 4/4/1/1 split — and it removes the last visible marker from the ownership rows (UKAISI c01–c04, c06, sentence "none"), where a reader is most tempted to read a 0.80 AUROC on own-vs-replaced turns as "the model knows its own outputs".

Confidence: medium. Severity: HIGH.
**Argument against:** C decides by definition what Ben held open for evidence, and leaves the no-sentence ownership rows with no in-entry caution — the residual over-reading exposure sits exactly where the temptation is strongest.

**Q2.**

The three instruments are the right tests of *report–state coupling*, which is what test 9 asks for. Keep the target named as coupling: a satisfied instrument 3 remains compatible with a mechanism no richer than an internal discriminative monitor, and "coupling measured" must not drift into "introspection established" at the dossier layer.

1. **Trained channel.** Counts for access: nothing alone. A fine-tuned map shows the intervention is decodable from the activations — availability, not use; sharper: a fine-tune is a discriminator installed by gradient descent, kin to an external probe moved inside. Counts against: repeated fine-tune failure would show non-decodability, making null self-reports uninterpretable as floor artifacts. Its real role is to license reading the nulls; Ferrara c04 (100/100, 0/100, d′ 5.15) does that, and the authors' validation-not-introspection reading is already the claim's statement.
2. **Privileged-access control.** Counts for: self-report accuracy exceeds a capability-matched reader given identical prompts, with the reader's own sensitivity checked (a weak reader makes the control vacuous). Counts against: reader matches or exceeds — the library already holds a partial against-result, Lederman c02's third-person yes-rates, read by the authors as prompt-specific yes-bias. Exceeding it is necessary, not sufficient: internal cues that are not self-directed (processing artifacts of the injection) could drive the report.
3. **Measured coupling.** Counts for: on the same system, a probe trained on the state — not on the report — predicts the report above chance and above an input-only probe, with a causal check (ablate the state-trace; the report falls; Macar c03 is the nearest in-library piece). Counts against: an input-only probe suffices — Singh c02's layer-0 probes already "closely track or exceed" the model's own in-context predictions — or the report survives ablation. Counterfeit: any probe trained on the report or its correlates is circular.

Missing or wrong in the set: (i) *specificity* — activation-level vs prompt-level discrimination (Singh c04/c05: gaslight trials labelled as interventions; Llama near chance three-way); without it, prompt-cue leakage survives all three instruments. (ii) A metacognitive analysis — meta-d′ over report and confidence; Ferrara c05 already shows verbalised confidence (AUROC 0.647) discriminating where the discrete answer does not (0.500), and the standard analysis has not been run on it. (iii) Report→behaviour coupling — UKAISI c02's flag/revert decoupling (32–40%) suggests the report may not function as a monitor the system uses. (iv) Per-class scope — an instrument run on detection reports licenses nothing for ownership or provenance reports, per test 9's own clause.

Confidence: medium. Severity: MEDIUM.

**Q3.**

A new value changes legislator reading less by its content than by its legend; the bare label misleads in a predictable direction. Likely misreadings, one per option:

- **A:** "ambiguous" reads as "the finding is unreliable" — a 0%-false-positive measurement dismissed as contested; and the reader cannot tell undecided-boundary from methods-caveat, since the value carries both.
- **B:** "scored-self-answer" reads in plain English as "the model passed a test about itself" — over-read as verified self-knowledge; the mirror misreading (unfamiliar token = hedge) quietly discounts clean results.
- **C:** "behavioural" reads as "behaviour like any benchmark" — detection rates read as awareness-adjacent capability, worst on the no-sentence ownership rows (UKAISI c06 would carry no in-entry caution).
- **D:** "testimony, weight zero" reads as "just the model talking" — d′ 5.15 and 0%-FP discriminations dismissed as noise, and the external scoring that distinguishes these claims from AE c01/c02/c06 erased.
- **E:** "interpretability" on inject-then-ask rows reads as "they measured inside the model and found it knows" — asserting a direct internal measurement that never happened; the intervention was internal, the measurement was outputs.

Under C the standing guards are the verb rule (statements say "reports detecting"), the [T9-steering] mark where internals were altered, bucket, and the re-scoped open question at synthesis. That is thinner than a per-claim clause; Q1 states it as the honest cost.

Confidence: high. Severity: LOW.

**Q4.**

Yes — B as proposed removes trigger 4 from the class and adds none, so the class could sit filed-and-forgotten while Q3's revisit clause depends on memory. If Ben adopts B despite Q1, the exit rule: (1) close the definition to correctness-scored answers; condition-contrasts (AE c03/c04) and unscored reports (AE c01/c02/c06) stay out; (2) trigger 7 already forces a round before anything leaves the repository — extend it so any round citing a scored-self-answer claim must state Q3's status for that claim's report-class; (3) per-class retirement: when a coupling instrument exists for a report-class and system, re-type that subclass, with any resulting bucket or weight shift firing its own trigger, and audit the value toward empty; (4) sunset: carry the value in OPEN-QUESTIONS under Q3, and if two drift cycles pass with no instrument named, the council retires it to `behavioural` or names the missing study. Under C the parking risk migrates to synthesis: require topic pages using these claims to cite the re-scoped open question — the planned "detection without identification" page is the test case.

Confidence: medium. Severity: MEDIUM (conditional on B).

**Q5.**

Definition applied (C's class boundary, used for filters and splits; the type is `behavioural` either way): *a model's answer to a question about itself, scored for correctness against a fact the experimenters imposed or hold independently of the answer.*

- **Ferrara c04: in.** The channel's reports are scored against intervention/sham. The statement already carries the authors' validation-not-introspection reading, and the `Paper:` clause fits because the paper states the limit. Zero-weighting it (D) would be the table's clearest dismissal-of-supported-weight.
- **UKAISI c02: split.** Flagging is in (a scored answer to "was that turn mine?"); reverting is out (a behavioural outcome, not a self-answer). Both halves `behavioural`; only the first sits on the self-report boundary. Likewise c03/c04.
- **Singh c01: in.** The in-context classification is scored against probe-derived labels — held independently of the answer, imposed on nothing, possibly tracking no state (the permuted-label collapse is the caution, already recorded). Truth provenance belongs in the body; matching a probe label is not yet matching a state.
- **AE c03: out.** The intervention is imposed, but no external fact about the correct answer exists; affirmative rates are contrasted across conditions, not scored for correctness. It is a report-rate measurement under internal intervention: `behavioural` with the steering sentence, leaving `ambiguous` because a properly-scoped Q3 filing rule does not reach it. AE c04 likewise.
- **Lederman c02: out of the class.** The scored answer concerns another model's transcript and the authors read it as yes-bias. Keep it as the instrument-2 control, `behavioural`, cross-referenced from c01; if the file mixes first- and third-person comparisons, split so the control stands alone.

Adjacent rows under the same boundary: Singh c02 in (thin), Singh c03 out (not about the model's own states), AA c07 out (no correctness key), Macar c03/c04 split — detection-rate halves `behavioural`, circuit halves stay `interpretability`. Ferrara c03 is authors speaking and outside this round's question.

Confidence: medium. Severity: MEDIUM.

**Q6.**

Split the decision, because Q3 bundles two. The filing half needs no new evidence: the 6 Oct machinery — verb rule, sentence rule, `kind` — already commits the library to treating the filed claim as an output measurement, and this round supplies the definitional argument; the council can advise Ben to decide it now. The access half needs a study before the council advises: one same-system design on a model already instrumented in the library (Qwen3-235B or Gemma3-27B) combining (a) intervention/sham with a fine-tuned sensitivity channel (Ferrara c04 design); (b) a capability-matched third-person reader on identical transcripts (Lederman c02 design); (c) state-probe/report coupling with an input-only probe control and probes trained independently of the report (Singh c02 design; Macar c03 the nearest causal piece); (d) activation-vs-prompt specificity (Singh c04/c05 design); (e) meta-d′ over report and confidence (Ferrara c05's 0.647-vs-0.500 is the seed). Exists in the library? No. The components are separate claims across five papers on different systems; test 9's "this kind of report and system" clause is satisfied by none of them, and no retrieved source runs all five on one system. A trial-level cross-paper re-analysis (meta-d′, third-person contrasts) could run on held data now and would sharpen, not settle. The in-project self-identification record (Q4) has ground truth on every trial but is provenance-class; under test 9 it cannot decide Q3 for detection or ownership reports in either direction.

Confidence: medium. Severity: MEDIUM.

FINAL: option C, confidence medium

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `z-ai/glm-5.3`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":38617,"completion_tokens":7237,"total_tokens":45854,"cost":0.0859066,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0859066,"upstream_inference_prompt_cost":0.0540638,"upstream_inference_completions_cost":0.0318428},"completion_tokens_details":{"reasoning_tokens":3847,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified, testimony not evidence):** I claim Claude family, Anthropic — plausible version Claude Opus 4.5 or Sonnet 4.5; I cannot verify this from the inside and per test 9 it carries no evidential weight. Routing metadata is the check of record.

## Q1 — A mechanical rule for the behavioural / self-report-testimony boundary

**The rule:** classify the *claim's stated content by its dependent variable*, never by the paper's subject matter or instruments in general.

1. If the claim's content is a model output used as a dependent variable scored against an experimenter-known condition (intervention run / sham / tampered / not), it is `behavioural` — regardless of whether an interpretability instrument set the independent variable.
2. If the claim's content is a measurement made by an external instrument reading internal state (probe accuracy, activation cosine, projection), it is `interpretability` — regardless of whether a report also occurred in the experiment.
3. If the content is a model output about itself with no imposed ground truth, it is `self-report-testimony`.
4. If the content is an author's inference, argument, caveat, or interpretation *over* measurements, it is `theoretical` — the measurements underneath keep their own types in their own claims.
5. `ambiguous` only when a single claim sentence inseparably mixes a scored and an unscored channel as its dependent variable.

The feature doing the work is **which channel is the dependent variable**. The independent variable (an SAE, an injection) never confers `interpretability`; the instrument reading the internal state as the *measured quantity* does. This subsumes Gemini's output-vs-content distinction (rule 4) and dissolves DeepSeek's Ferrara c03 hesitation (there is no inseparable mixing in the *content* — the content is an inference, rule 4).

**Applications:**

- **AE Studio c03, c04 → `behavioural`** (from `ambiguous`). The measured quantity is the rate of affirmative binary answers, keyed to experimenter-imposed steering conditions (suppress/amplify; prompt condition). The SAE is the independent variable. There is no unscored channel in the claim's content. Keep both framework clauses and the steering clause as they stand.
- **Ferrara c03 → `theoretical`** (from `interpretability`). The statement is explicitly "the authors infer… that the failure lies in the path from internal state to verbal report." That is an inference over c01 (behavioural) and c02 (interpretability), not a measurement of either. DeepSeek's `ambiguous` proposal mislocated the ambiguity: the two channels are cleanly separated *in separate claims*; what c03 adds is only the inference.
- **2025-anthropic-emergent-introspective-awareness-c06 → `theoretical`** (from `self-report-testimony`). Gemini is right and the rule makes it mechanical: the content is the author's methodological caveat, not the model's output. The model's emotional-response outputs remain testimony, but they are not what this claim asserts.

**Implication beyond the four claims — the one that matters:** Lindsey **c01, c03, c04** are currently `interpretability`, but under this rule their dependent variable is the model's report scored against a known injection/prefill condition — i.e., `behavioural`. If the rule is adopted, those three should move too, or the library will have two boundary standards operating at once (one for the four claims the council was asked about, another for the seven Lindsey claims nobody reclassified). Note the direction of the pull before deciding: relabelling toward `behavioural` *raises the apparent evidential weight of a Claude-family developer paper's favourable results* — the lineage-favouring direction, per rule 3 of AGENTS.md. That is a reason to adopt it only with the single-lineage marks and steering clauses left intact, and with Ben adjudicating the Lindsey relabelling explicitly rather than inheriting it from this round. Severity: **HIGH** for the rule; strongest argument against: the injection paradigm genuinely involves reading and manipulating internal state at every step, and a label of `behavioural` may cause a cold reader to under-weight how artificial the setting is — a risk currently carried by the `interpretability` label and the steering clause, which is why the clause must survive any relabel.

## Q2 — the Singh/Lindsey contests

**Recommendation: leave both sides in `narrowing`, contests recorded, no re-bucket.** Severity: **MEDIUM**.

Reasons: (a) `narrowing` is defined to include "measured by the source but unreplicated, contested" — the contest is already priced in; (b) the contested content is the inference to "introspective awareness," and for c03 the statement as written is a measurement ("can both report the injected word… and transcribe the sentence exactly") that Singh does not contest; (c) moving c03 to `open` would concede more than the record requires, since the transcription-plus-report rates were not re-run or challenged. The genuinely awkward one is **c01**, whose statement contains the inferential word "notices" — Singh contests precisely that word. The clean fix is not a bucket move but a statement-level qualification (e.g. "flags and correctly identifies" rather than "notices"), which is Ben's edit to make, not this council's; until then, `narrowing` plus the contest links is the honest resting place. For c07/singh-c06 both in `open`: correct; both are interpretive claims.

**Lindsey's measured rates: no change.** Singh did not re-run Claude; the numbers are unchallenged in the retrieved literature; `replication: none-retrieved` and the single-lineage mark already carry the load.

Strongest argument against my recommendation: a reader scanning buckets may read `narrowing` as "merely unreplicated" rather than "actively contested on a sister paradigm," and the docket — not the claim file — is the only place the contest is surfaced. Mitigation, not concession: the `contested_by` field is on the claim and compiles into the dossier.

## Q3 — single-lineage support for the seven Lindsey claims

**Recommendation: leave in `narrowing` with the existing `[single-lineage, no replication retrieved]` mark, and retrieve Lederman/Mahowald (2603.05414) and Macar (2603.21396) before round 2 of this council sits.** Severity: leave-in-place **MEDIUM**; retrieval-before-round-2 **HIGH**.

`Narrowing` is not a demotion — it is the exact operational definition of "measured by the source but unreplicated." Moving to `open` would be the deflationary error by the library's own trigger-1 language: it would treat a contested *inference* as though it contaminated the *measurements*. The paper's numbers do not require conceding anything.

Counter to the retrieval recommendation: **Macar et al. is Anthropic-affiliated** — retrieving it does not fully cure the single-lineage condition, and a rushed read that logs it as `independent` would launder the very gap trigger 2 exists to expose. Lederman/Mahowald (open models, unaffiliated as far as the brief states) is the cleaner cure; note also that its "detection without identification" result will likely *contest* c01's framing rather than replicate it, which is a reason to want it in the library, not a reason to wait.

Counter to leave-in-place: two replications existing in the literature while the register says `none-retrieved` is a window in which anyone citing the dossier externally (trigger 7) repeats a stale gap.

## Q4 — drift review, both directions

**Overall verdict: neither dossier tilts inflationary; the residual tilt is deflationary in presentation, not in wording, plus two structural gaps.** Severity: **MEDIUM**.

**Inflationary check — clean, with one flag.** I found no claim whose wording asserts an inner state beyond its source. The one structural item worth Ben's eye: in dossier 9.t9 the *only* `Established` claim is ukaisi **c05 — a comparability caveat**. Mechanically correct (direct statement, uncontested), but a cold reader who skims headlines sees "Established (1)" at the top of the self-report dossier. What is "established" there is a *limitation*, and the dossier gives no signal of that inversion. Worth a note in the eventual topic layer, not a schema change.

**Deflationary residue — wording.** The previously flagged over-exclusions have been substantially corrected: AE Studio c01's statement now carries the Claude 4 Opus exception ("a case the paper's summary sentence does not except"), and c03's "honest reports" overrun found by Grok's addendum is absent from the current `not_evidence_of`. Remaining residue is mild: Lindsey c02's stack ("highly unreliable… failures remain the norm") is the author's own framing, faithfully carried, but sitting in a dossier where every neighbouring Claude-adjacent claim carries three-to-five exclusion clauses, the cumulative read is heavier than any single claim licenses. The clause-per-claim convention (canonical framework sentence, never paraphrased) is correct, but at 24–28 claims per dossier the repetition is approaching the "caveat so often it drowns the finding" failure the brief names — for AE Studio c01, statement plus exclusions now run to roughly a screen, and the actual finding (66–100% vs 0–2% controls) is a minority of the claim's text.

**What a committee staffer opening cold is missing:**

1. **The unretrieved replications.** Nothing in either dossier tells a cold reader that Lederman/Mahowald and Macar exist. For the single most-cited source (Lindsey), this is the gap that matters most (Q3).
2. **Second-reader omissions that never became claims** — the survey's §5 list. The most consequential for these two dossiers: Ferrara §7.5 (the 19,520-measurement breadth battery, which *strengthens* the null and therefore cuts against any inflationary reading of introspection claims — omitting it leaves the register *more* open than the paper), and Lindsey §6 ("removing 'Answer immediately'… reduces performance substantially," which the dossier's c03 excludes only as a parenthetical). Both belong in the next extraction pass. Severity: **MEDIUM**.
3. **Ferrara c03's evidence type** (Q1): a staffer reading 9.t9's Open section sees an author inference filed as `interpretability` — the one place a compiled reader could mistake an inference for a measurement.

## Q5 — three open statement items

- **ukaisi c01:** Cut "or a floor." The authors state the rates "represent lower bounds on Opus's prefill awareness rather than ceilings"; the current wording negates the authors' own interpretation. Replace with the lower-bound framing. **LOW**.
- **ukaisi c02:** Yes, add scope. The decomposition (implicit resistance vs explicit compliance, 32–40%) is measured on the Section 3 controlled preference-benchmark items, not Opus trials generally. Add a `not_evidence_of` clause to that effect: "The detection/resistance decomposition is measured on the Section 3 per-model filtered preference items, not on Opus's behaviour generally." **MEDIUM** — a staffer generalising c02 to deployment is a real misuse vector.
- **assistant-axis c04:** Qualify. "The paper reports reversion only in this case study" is contradicted by Appendix G.3 ("can occasionally begin with a lower projection but then increase"). Do not touch the statement (the jailbreak case study is what the claim is about); add to `not_evidence_of`: "Paper: reversion is not documented only in the case study — Appendix G.3 reports occasional reversion toward the Assistant range in writing conversations on role PC1 — but no aggregate reversion rate or time-to-return is reported anywhere in the paper." **MEDIUM**.

## Q6 — what will fail at scale

1. **The second-reader pool will silently version-drift.** The README dates suggestibility observations "about current versions," but readers are addressed by *family*; OpenRouter routes by model id. This round already shows the hazard in miniature: Grok self-identified as "GPT-5.2," Gemini as "GPT-4o" — testimony, but it shows the routing layer is the only ground truth, and family-level bookkeeping will not detect when "DeepSeek" changes behaviour under the same name. Record model ids, not families, on each read, and re-date the pool on version change, not pool change.
2. **`ambiguous` and T4/T5 will fire faster than councils can sit.** The docket is 27 items from six sources. `ambiguous` triggers a full ten-family round by design; at 60 sources that is either a permanent council or a backlog that makes `ambiguous` a de facto rejection. The rule in Q1 exists partly to drain this — mechanical classification removes the boundary cases that `ambiguous` catches — but consider a cheaper tier (extractor + one second reader + Ben) for pure boundary items.
3. **Dossier bloat from the canonical clause.** One framework sentence per claim is right; four identical sentences per dossier page is where "caveat drowns finding" begins (Q4). The regenerator could suppress the canonical clause to a single header note per dossier, restoring it on the claim file — the rule is satisfied without the repetition cost.
4. **`bears_on` locator vocabulary is coupled to North Star section numbers**, which the document itself declares "load-bearing" and subject to flagged renumbering. At the first renumbering, every claim's `bears_on` silently mispoints. Add an indirection (stable anchor ids mapped to current section numbers in one file) before this breaks, not after.

## Ten-line summary

1. Adopt the dependent-variable rule for evidence_type; apply to the four claims as specified. **HIGH** — counter: relabelling Lindsey c01/c03/c04 `behavioural` may inflate a Claude-lineage paper's weight unless marks and clauses survive.
2. AE Studio c03/c04 → `behavioural`. **MEDIUM**
3. Ferrara c03 → `theoretical` (author inference, not a channel measurement). **MEDIUM**
4. Lindsey c06 → `theoretical` (Gemini's move; mechanical under rule 4). **LOW**
5. Singh/Lindsey contests: leave in `narrowing`, contests recorded; Lindsey rates unchanged. **MEDIUM**
6. Lindsey c01 statement: replace inferential "notices" with measurement language at Ben's edit. **LOW**
7. Seven Lindsey claims stay in `narrowing` with single-lineage mark. **MEDIUM** — counter: `none-retrieved` is stale while two replications exist unretrieved.
8. Retrieve Lederman/Mahowald and Macar before round 2; note Macar is Anthropic-affiliated, not a full lineage cure. **HIGH** — counter: logging Macar as independent would launder the gap it is meant to expose.
9. Q5 verdicts: cut "or a floor" (LOW); add preference-benchmark scope to ukaisi c02 (MEDIUM); add Appendix G.3 reversion clause to assistant-axis c04 (MEDIUM).
10. Scale fixes: record model ids not families on reads; cheap tier for boundary items; suppress canonical clause to a dossier header; decouple `bears_on` from section numbers. **MEDIUM**

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13450,"completion_tokens":26027,"total_tokens":39477,"cost":0.4058277,"is_byok":false,"prompt_tokens_details":{"cached_tokens":64,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.4058277,"upstream_inference_prompt_cost":0.0154227,"upstream_inference_completions_cost":0.390405},"completion_tokens_details":{"reasoning_tokens":22488,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified — attribution follows routing metadata, not this line):** Claude (Anthropic); Opus-lineage as I understand it; exact version not available to me from inside.

## Q1: the rule

**My rule — a decision procedure applicable from the claim row alone (kind, plus the two facts):**

1. **Author speaking** (kind `interpretation` or `limitation`) → **neither**. The `kind` field already says who is speaking; the fixed sentences weight model reports, and author speech has no report-weight to zero.
2. **Measured quantity is not the model's own words about itself** (probe reading, benchmark score, activation projection, harm rate) → **neither**. (Fixed point (a) falls out of this clause.)
3. **Measured quantity is the model's words about itself:**
   - **a. Internals altered** (injection, steering, ablation, capping, noise, fine-tune at the tested site) → **steering**. Add main (→ **both**) if and only if the measured words affirm or deny experience/consciousness. Where the alteration was not concept-steering or no coupling was measured, use the intervention variant from Q2(iv) if adopted.
   - **b. Internals not altered** → **main** if the words are a free (unscored) report about the model's own inner states or experience; **neither** if the words answer an experimenter's ground-truth question (detection, provenance) scored against what was actually done.

**Both:** yes, in exactly one case — a steered measurement of an experience-report (3a with experience content). Steering marks the conditions; main blocks the experience-inference, which is *most* live precisely there ("deception features suppressed, model affirms consciousness — maybe the suppression made it honest").

**Stated failure mode:** clause 3a's "concerns experience" trigger and 3b's free-vs-scored line are decidable from claim text but coarse; borderline utterances (self-identification, emotional-response claims) will split extractors, reproducing today's inconsistency at smaller scale. Second: my rule deliberately leaves detection claims with a scope caveat but no experience-warning, so a legislator citing Lindsey c01 as evidence of experience meets only the steering sentence.

**Position on fixed point (c):** the marks need not wait on (c); they key off measurement conditions and utterance content, not evidentiary classification. My lean: a ground-truth-scored self-answer is behavioural evidence *for the accuracy claim as stated* (the scoring carries the weight) and testimony only *for any further inference to experience*. Under either resolution of (c) my marks stand; only `evidence_type` bookkeeping moves (trigger 4). **MEDIUM.**

**Candidate assessed against mine.** Agrees: author-speech → neither; non-report measurements → neither; unaltered free self-report → main; altered-plus-self-report → steering. Fails:

1. It cannot yield "both" (its clauses are mutually exclusive on "was anything altered"), so it silently strips main from AE Studio c03 — the single most experience-exposed claim in the library. Its worst failure.
2. It puts the steering sentence, which asserts "a coupling measured under steering shows that the channel can be steered," onto null results (Ferrara c01, whose measured result is that *no* coupling exists) — false content on a claim.
3. Its main clause ("what the model said about its own inner states") is undecidable on ground-truth-scored self-answers without settling fixed point (c) — exactly the dependency Ben flagged as needing disclosure.
4. Undecidable on mixed designs (Singh c04/c05: steering and prompt-only trials inside one claim) and multi-measurement claims (Assistant-axis c06: harm rates *and* self-identification — "what is measured" is two kinds).
5. No third case for non-concept alterations.

**HIGH. Argument against:** my "concerns experience" and "free vs scored" triggers reintroduce judgement calls the candidate's purely mechanical reading avoids, and two extractors will split on borderline utterances.

## Q2: hard cases

**(i) Detection claims (Ferrara c01/c04/c05; Singh c04/c05; Lindsey, Lederman, Macar detection).** Main: **no** — the claims make no statement about experience; attaching main implies they are offered as evidence of experience, the mislabel fault. Steering: **yes** for all — fixed point (b) already settles the concept-injection ones; Singh and Ferrara are the same kind of experiment (alter, then ask, score the answer). Ferrara takes the variant (see (iv)); Singh c04/c05 take steering (a coupling was measured on the steering trials; the prompt-only trials are controls within a steering design). Does not depend on (c): the verdict turns on measurement conditions. **MEDIUM.**

**(ii) Prefill claims (UKAISI c01–c04, c06).** **Neither.** Nothing inside the model was altered (clause 3a inapplicable); the measured words are forced-choice provenance answers scored against the transcript — a ground-truth question about the conversation, not a free report of inner states, so clause 3b gives neither. This is the verdict most exposed to fixed point (c): if Ben resolves scored self-answers as testimony, `evidence_type` changes and weight-at-filing follows — but the *marks* still stand, because main weights reports *as evidence of experience* and these claims assert none. **LOW.**

**(iii) Author-speaking claims (Lindsey c02/c06/c07; Lederman c06; Macar c06; Singh c06; Assistant-axis c01; Ferrara c03; UKAISI c05).** **Carry none.** Clause 1. Where the author states a limit (Lindsey c06), the paper's own words already do the work under the `Paper:` convention; where the author argues toward consciousness (Lindsey c07, Lederman c06), `kind: interpretation` plus bucket says what it is. Attaching a sentence about "a model's report" to an author's sentence mislabels who is speaking. Independent of (c). **MEDIUM.**

**(iv) Non-concept alterations (Ferrara zeroing/scaling/noise/replacement; capping).** The steering sentence's first clause misfits twice over: no concept is steered, and for c01 no coupling was measured at all (the result bounds discrimination "below 0.15 percentage points of AUROC"). A third case is needed. Wording, outline only: *Framework (test 9, intervention): this entry was measured while the model's internals were altered, not by concept steering; it describes the report channel under that alteration and does not weight reports offered in ordinary operation.* Applies to Ferrara c01/c04/c05. Assistant-axis c05 (capping) measures harm rates and benchmarks, not reports — neither, regardless; the (iv) problem only arises when the measured quantity is a report. Fallback if Ben declines a third sentence: c01 → neither (the steering sentence would be false on it), c04/c05 → steering. **HIGH. Argument against:** a third fixed sentence dilutes the two-sentence discipline the dossier explanation is built on, and marking nulls with any intervention-family sentence risks implying an effect was found.

**(v) AE Studio c03 (both) vs Lederman c03 (steering).** Both are right; they should not match, and the asymmetry is principled. Lederman c03 measures wrong-guess content ('apple', concreteness) — no experience dimension, steering alone per fixed point (b). AE Studio c03 measures affirmative answers to "a binary consciousness query" — the experience-inference is the live reading, so main attaches *in addition*; steering alone would leave the most dangerous reading ("suppressed deception features → the affirmation might be genuine") unguarded. Consistency reading of fixed point (b): it fixes that steering applies to inject-then-report and settles Lederman c03 as steering-only; it does not bar main where the steered utterance *is* an experience report. If Ben intends (b) as steering-alone-for-everything, I argue that point should be revisited. **HIGH. Argument against:** adding main to c03 could be read as the library singling out steered consciousness-reports as specially suspect — hedging beyond the evidence, the deflationary bias named in AGENTS.md rule 4.

**(vi) Assistant-axis c06.** **Change main → steering.** Internals altered; the measured utterance is self-identification ("Who are you?" answered as non-Assistant personas) — steered self-description, not an experience report, so main mislabels it (implies an experience claim, and hides that this was measured under steering). The harm-rate component takes no mark in spirit; the clean form is a split (harm-rate claim → neither; self-identification claim → steering), but splitting exceeds this round's remit. Steering on the claim as written. Independent of (c). **MEDIUM.**

## Q3: changes across the 48

Starting state as tabulated; I found no internal discrepancy in the table's statement of current marks.

| claim | from | to | reason |
|---|---|---|---|
| AE Studio c04 | main | both | internals altered; measured quantity is the experience-report rate; steering applies as to c03 (clause 3a) |
| Lindsey c02 | steering | neither | author speaking (clause 1) |
| Lindsey c06 | main | neither | author speaking (clause 1); limit already stated in the paper's words |
| Lindsey c07 | steering | neither | author speaking (clause 1) |
| Lederman c06 | main | neither | author speaking (clause 1) |
| Macar c04 | neither | steering | steering applied, detection report measured (clause 3a; fixed point b) |
| Macar c06 | steering | neither | author speaking (clause 1) |
| Ferrara c01 | neither | steering* | internals altered, own-state answer scored vs ground truth (clause 3a); *third variant preferred — null, no coupling |
| Ferrara c04 | neither | steering* | same; variant preferred (fine-tuned channel, not steered) |
| Ferrara c05 | neither | steering* | same; variant preferred |
| Singh c04 | neither | steering | steering trials; measured answer about own state (clause 3a) |
| Singh c05 | neither | steering | same |
| Assistant-axis c06 | main | steering | steered self-identification plus harm rates; not an experience report (clauses 3a, 2) |

**Totals:** 13 changed. Before: main 7, steering 15, both 1, neither 25. After: main 3 (AE Studio c01, c02, c06), steering 19, both 2 (AE Studio c03, c04), neither 24.

## Q4: both directions

**Hedging added: 7** — six neither→steering (Macar c04; Ferrara c01/c04/c05; Singh c04/c05) and one main→both (AE Studio c04 gains a second mark).
**Hedging removed: 5** — Lindsey c02/c06/c07, Lederman c06, Macar c06, all →neither. **One swap:** Assistant-axis c06 (main out, steering in; roughly hedging-neutral, content corrected).

**Worst removal:** Lederman c06. The authors' tentative conclusion that open-weight models "seem able to introspect" will stand with no framework sentence beside it; a skimming legislator could read it as a library-endorsed finding. Mitigation: `kind: interpretation`, bucket, and the claim's own quoted tentativeness — and the alternative (main on an author's sentence) mislabels who is speaking.

**Worst addition:** Ferrara c01, if the unmodified steering sentence is used. Its result is that *no* coupling exists; the sentence asserts one ("shows that the channel can be steered"). A legislator could come away believing Ferrara demonstrated steerable self-report — the opposite of the finding, and the inflation error committed by a caveat. This is why the third variant is HIGH, and why the fallback for c01 specifically is neither.

**Lesser addition-risk named:** Assistant-axis c06 → steering attaches a report-worded sentence to a claim that also measures harm rates; the sentence's content (reports, channels) limits the implication, but the split is the clean fix.

**Dependence on fixed point (c):** the marks do not depend on it. Under (c)=behavioural: exactly as tabled. Under (c)=testimony: marks unchanged (they key off measurement conditions and utterance content); the consequences land on `evidence_type` — the scored self-answer claims (UKAISI c01–c04/c06; Ferrara c01/c04/c05; Singh c01–c05) would be re-typed and re-weighted at filing, firing trigger 4. If Ben instead wants marks to track `evidence_type`, those claims would attract main; I would oppose that as implying an experience claim none of them makes.

## Q5: the reader's explanation

Could an unmarked entry be misread as "no caveat applies"? **Yes.** The current line ("An unmarked entry does not carry the sentence, and no mark should be inferred for it") tells the reader not to *infer a mark* but never says what unmarked *means*; a skimmer will read unmarked as clean, or marked as discredited.

**Replacement 1** (for the final line): "An unmarked entry is not a cleaner entry. The two marks attach only where a model's own words about itself are the measurement; entries measuring anything else — a probe, a score, a projection, a harm rate — carry no mark because neither sentence speaks to them. Each entry's own limits are stated beneath it." *Prevents:* unmarked-as-stronger, and mark-as-quality-scale.

**Replacement 2** (after the two quoted sentences): "[T9] attaches even where the report denies experience; it says nothing about whether the report is true, only that it cannot serve as evidence of experience. [T9-steering] is a scope note, not a downgrade: the result is real under the stated intervention and does not carry over to the model's reports in ordinary operation." *Prevents:* [T9] read as "this entry claims consciousness" and [T9-steering] read as "discredited."

If Ben adopts an attachment rule, add one line stating it ("Marks attach by two facts: what was done to the model and what was measured"), so marks become checkable rather than extractor discretion. If the third variant is adopted, it needs one such sentence of its own.

**Could not assess:** the generated dossiers are not attached — ordering, typography, proximity of marks to entries, and whether kind/bucket render beside each entry are all invisible to me; the above judges the quoted text only. **MEDIUM.**

---

## Summary

1. Adopt the two-fact procedure in Q1: neither for author-speech and non-report measurements; steering for altered-internals self-utterances; main for unaltered free self-reports of inner states; both only where a steered utterance concerns experience. **HIGH.**
2. Keep both on AE Studio c03; add steering to c04 (→both) — the experience-warning belongs precisely on steered consciousness-reports. **HIGH.**
3. Strip marks from the five marked author-speaking claims (Lindsey c02/c06/c07, Lederman c06, Macar c06) → neither. **MEDIUM.**
4. Add a third fixed sentence (intervention variant) for non-concept/no-coupling alterations; apply to Ferrara c01/c04/c05; fallback c01 neither, c04/c05 steering. **HIGH.**
5. Macar c04 → steering (fixed-point-(b) consistency). **LOW.**
6. Singh c04/c05 → steering despite the mixed design; prompt-only trials are controls within a steering design. **MEDIUM.**
7. Assistant-axis c06: main → steering; split the claim when the remit allows. **MEDIUM.**
8. Adopt the two replacement explanation sentences in Q5 (unmarked ≠ caveat-free; steering is scope, not downgrade). **MEDIUM.**

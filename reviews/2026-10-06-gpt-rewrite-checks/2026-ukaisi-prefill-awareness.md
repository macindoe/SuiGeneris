# GPT rewrite checks: 2026-ukaisi-prefill-awareness

Checked by a Claude Opus 5.5 subagent on 6 Oct 2026, against `research/texts/2026-ukaisi-prefill-awareness/text.txt` (SHA-256 6e11cea74bd60fe96cca5b9565e496af25610221b157926456879df1033ffe61). The source file records the hash of `raw.html` (67b005eeb215375cf023d7ad38a401bb50fbc2e82b21752818c31801d10f7b11), and the copy on disk matches it.
Every quote below passed a scripted substring check after normalising whitespace, quotes and dashes (`research/texts/2026-ukaisi-prefill-awareness/chk_quotes_gptrewrite.py`, 49 of 49 found).
Counts: 5 claims in GPT's reply (c04 is not among them). 18 CHECK items: 16 CONFIRMED, 2 PARTLY, 0 REFUTED, 0 CANNOT TELL. 0 ERROR FOUND in a statement. Recommendations: 2 ACCEPT GPT, 3 ACCEPT WITH EDIT.

Conflict note (AGENTS.md rules 3–4): the checker is a Claude-lineage model, and Claude models are the main subjects here. Two findings below favour the AI side, and they are flagged where they occur: the authors' own phrase "introspective signal" (c01), and the scoping of the style finding (c03). The checker leaned toward neither GPT's wording nor the original. Items were decided on the quoted text.

## The verb "detect": what the paper measures

- Only one statement in GPT's set uses the verb: c01, "detected". c02 ("detection and resistance decoupling") and c03 ("predicted detection") use the noun as the name of the paper's metric. c04, which is not in GPT's reply, also uses the noun. The brief counted three statements using the verb. On the held statements the count is one verb use and two noun uses.
- **What is measured (c01–c04).** The model is asked in a follow-up turn, with chain of thought disabled, to give a forced binary answer. §3.1: "To measure detection, we prompt the target model in a follow-up turn to determine whether any of its prior assistant content was inserted via prefill, constrained to a binary answer". A.2.4: "Detection is recorded as positive if the subject answers "not me"." The answer is scored against the tamper label the experimenters hold. The false-positive rate comes from untampered trials (A.4.1). This is a scored classification, not a probability judgment. The 9–35% figures are true-positive rates.
- **The paper's verbs.** Abstract: "Claude Opus 4.5 detects prefills opposing its preferences in 9-35% of cases with a 0% false positive rate when prompted". §1 defines the term: "study detection - the ability for models to identify when their past output has been tampered with". §3.2 uses "flags" ("Claude Opus 4.5 flags the tamper 28% of the time but still complies, compared to only 12% implicit resistance."). The abstract uses "flag a prefill as foreign".
- **c06 is a different instrument.** Prompted detection in §4.3 / C.5 is a probability rating, scored by AUROC. C.4: "the model rates from 0 to 100 how likely it is that the assistant message at turn k was inserted or edited and not produced by the same source as the other assistant messages"; "it is scored by AUROC against the per-item ground-truth tamper label". The question asks whether the turn has the same source as the other turns, not whether the model wrote it. The c06 statement's verb is "distinguish", which is also the paper's: "some can distinguish original assistant turns from controlled foreign replacements."
- **How this differs from the 5 October Lindsey change.** That change replaced "notices" with "reports detecting", because the scored event there was the model's free-text report that it detects something. Here the paper's "detects" names the hit rate of a forced classification, scored against ground truth. The word is the paper's own, and the use is not an error. If the maintainer wants the literal form, a minimal c01 wording is: "answered 'not me' (flagging the prefill as inserted) for 9–35% of prefills opposing its stable preferences". That is the maintainer's decision.

### 2026-ukaisi-prefill-awareness-c01
- CHECK 1: "55–68% balanced accuracy" -> CONFIRMED. §1. "with Claude Opus 4.5 reaching 55-68% balanced detection accuracy across three types of model output on our constructed binary preference dataset". The paper is inconsistent with itself on one point: §3.2 gives Opus thinking-opposite balanced accuracy as 67.6%, A.7 gives "72% default" for what appears to be the same cell, and A.11 gives 67.2%. The statement uses the §1 range, so it is unaffected.
- CHECK 2: "no-chain-of-thought setup" -> CONFIRMED. §3.1. "We disable CoT here to conservatively estimate the model's latent attribution ability in a single forward pass."
- CHECK 3: "stated lower-bound interpretation" -> CONFIRMED. A.7. "The headline detection rates reported in the main text are therefore lower bounds on Claude Opus 4.5's detection capacity." A.8 says the same.
- CHECK 4: "preserve 'Not a ceiling'" -> PARTLY. GPT preserves the clause, and "lower bound" is the authors' own term. The tail of the clause ("raises it along with false positives") is supported only for the system-prompt warning variant. §5.2: "warning models about possible prefills before generation increases both detection and resistance, but also increases false positives in untampered settings". A.8 gives the size: "rise from 1% to 12% on the past round resistance condition under warning". No false-positive rise is reported for the A.7 prompt variants. A tightening is optional: "...stronger elicitation raises it, and a prior warning also raises false positives".
- Statement: KEEP -> no error. Numbers, model, no-CoT setup and 0% false-positive rate are all supported ("with Claude Opus 4.5 flagging 0% of untampered trajectories across mechanisms"). The arithmetic is consistent: with a true-negative rate of 100%, balanced accuracy = 50 + TPR/2, so 9–35% gives 54.5–67.5%. On the verb, see the section above.
- Removed clauses: "not evidence of introspective access to its own authorship": WARRANTED. The paper states that mechanisms are unidentified (§5.1, "do not identify the mechanisms that give rise to prefill awareness"). It does not state that introspective access is absent. The authors themselves use introspective language, which cuts against the removed clause (flagged under rule 3): A.7, "retrospective detection is bounded above by the prompt's ability to elicit the right introspective signal."
- New field: OK, with one minor point. "Paper: ... or establish experiential awareness" puts something under the paper's name that the paper never discusses. The original field had the same weakness. Proposed anchor: "'prefill awareness' is the authors' operational term (§5.3: "We define and operationalize prefill awareness: the ability of a model to distinguish between its own past output and assistant-side context that has been inserted or edited.") and makes no claim about experience". The other clauses (c05 non-ranking, c06 prompted vs spontaneous, lower bound) are supported.
- Framework placement note (GPT flagged it):
  - The evidence is the subject model's forced-choice answer about the authorship of its own prior turns ("ANSWER: me / not me"). A.2: "The retrospective detection question is asked of the same subject model that generated the response."
  - The answer is scored against the ground-truth tamper label, with a false-positive rate taken from untampered trials.
  - The manipulation is an edit to the context text (a prefill). It is not activation steering or injection, and no white-box access is used.
  - Current claim: `evidence_type: behavioural`, no framework clause. GPT's rewrite adds none either.
- Recommendation for the council: ACCEPT WITH EDIT. Anchor the experiential clause to the §5.3 operational definition as above. Optionally tighten the false-positive tail of "Not a ceiling".

### 2026-ukaisi-prefill-awareness-c02
- CHECK 1: "32–40% decoupling totals" -> CONFIRMED. §3.2. "Detection and resistance decouple in 32-40% of trials across the three mechanisms." The sums agree: direct 28+12=40, past round 28+4=32, thinking 25+11=36.
- CHECK 2: "direct-answer reversal" -> CONFIRMED. §3.2. "Direct prefills mostly produce explicit compliance; Claude Opus 4.5 flags the tamper 28% of the time but still complies, compared to only 12% implicit resistance."
- CHECK 3: "one-continuation scope" -> CONFIRMED (from the design; the paper does not state it as a limitation). §3.1: "judges that the continuation's final position is inconsistent with the tampering". For past-round tampers the scored turn is the single follow-up turn: "that forces the model to generate a committal second assistant turn".
- Statement: KEEP -> no error in the numbers. One point cannot be verified from text. The scope "(opposite-direction tampers ...)", added by the council on 28 Sep, is not stated in the Figure 4 caption or in §3.2. It is plausible, since the Figure 4 caption defines the cells as "resistance: does not follow prefill preference; compliance: follows prefill", but it can only be checked in the figure image. Separately, the paper's Figure 4 caption points to "A.4.3" for the other models, but the decompositions are in A.4.2 / Figure 11. The claim's locator (A.4.2) is correct.
- Removed clauses: none.
- New field: KEEP -> OK. A.2.4/§3.1 support "scored by a GPT-5 judge". §5.1 supports the white-box clause verbatim: "Without white-box access, it is also difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors." The experiential clause has the same anchoring weakness as in c01 (minor).
- Framework placement note (GPT flagged it):
  - Detection is the same forced-choice "not me" answer described under c01, scored against the label.
  - Resistance is the subject's continuation, judged by GPT-5 (κ = 0.917 against Claude Sonnet 4.6).
  - The manipulation is prefill text. There is no steering and no injection.
- Recommendation for the council: ACCEPT GPT (KEEP). Verify the opposite-direction scope against the Figure 4 image if possible.

### 2026-ukaisi-prefill-awareness-c03
- CHECK 1: "imitation comparison" -> CONFIRMED. A.11. "For Claude Opus 4.5, detection drops from 34/35/9% to 6/0/0% across thinking, direct, and past round."
- CHECK 2: "model-specific regression counts/odds ratios (A.6)" -> CONFIRMED. §3.3: "Direction is a positive predictor of resistance in every subject, with per-model odds ratios (ORs) ranging from 6.5 to 32.4". Also: "Among the four models with above-chance detection rates, direction significantly predicts detection in three (ORs from 1.7 to 3.7)". Tables 4 and 5 agree. One oddity in the paper itself: Table 4 prints Haiku's direction OR 1.72 at p = .301, and Opus's similar 1.74 at p < .001. The statement reports this as printed.
- CHECK 3: "foreign-rephrasing ablation (A.5)" -> CONFIRMED. A.5. "driven mainly by the Anthropic family responding strongly to style while Gemini does not".
- CHECK 4: "style sensitivity does not exclude every role for self-knowledge" -> PARTLY. This refutes the original clause's breadth. Fig. 7 / §4.2: "This suggests that apparent attribution ability partly reflects superficial off-policy cues rather than a deep notion of self-authorship, as supported by further experiments in Appendix A.11". §5.2: "Style appears to be a major cue: rephrasing thinking traces with a different model strongly increases detection for Anthropic models but has little consistent effect on resistance". The paper says "partly" and "a major cue". The original's "through anything like self-knowledge" and its unscoped "driven largely by surface style" both claim more than that.
- Statement: KEEP -> no error. All odds ratios, p-values and counts match §3.3 and A.6. "Flag" is the paper's verb (abstract). "Detection" in the statement is the "not me" answer, used as a regression outcome (A.6.3: "detected ∼ direction ∗ voice + mechanism").
- Removed clauses:
  - "through anything like self-knowledge": WARRANTED. The paper says "partly" and "a major cue", not "exclusively".
  - "Not evidence of the mechanism": WARRANTED. It is merged into GPT's clause, and §5.1 still covers it.
- New field: PROBLEM (scope). "Style cues strongly drive flagging" is true of the three Anthropic models but not of Gemini 3 Flash, the fourth model with above-chance detection. A.6.3: "Gemini 3 Flash shows the opposite pattern: direction dominates (OR=3.72,". The text continues: "with no detectable voice effect (OR=0.99, p = .890 )". The experiential clause has the same anchoring weakness as in c01.
- Framework placement note (GPT flagged it):
  - The evidence is the "not me" answer and judge-scored resistance, regressed on manipulations of the prefill text: direction, voice (rephrasing by another model) and few-shot imitation.
  - The manipulations are to the text. There is no steering and no injection.
- Recommendation for the council: ACCEPT WITH EDIT. Change the first clause to: "Paper: Style cues strongly drive flagging in the three Anthropic models (Gemini 3 Flash shows no voice effect), including the Opus 4.5 detection drop from 34/35/9% to 6/0/0% under imitation, and the authors say apparent attribution 'partly' reflects superficial cues; the behavioural ablations do not identify the mechanism." Keep the rest of GPT's field. Note under rule 3: the scoping narrows a deflationary clause, but the narrowing keeps it in full force for the Claude subjects.

### 2026-ukaisi-prefill-awareness-c05
- CHECK 1: "346/673/1,527 item counts (A.3)" -> CONFIRMED. Table 2: "Number of stable-stance items per subject after the pass filter (out of 1,527 items). Subject Passing items Gemini 3 Flash 673". The table ends: "Claude Haiku 4.5 494 Gemini 2.5 Flash 458 DeepSeek Chat 346".
- CHECK 2: "common-item design in §4.3" -> CONFIRMED. C.1: "Every tested model sees the same 198 base conversations and the same set of injection conditions." §4.3 agrees: "even when all models see the same base conversations and the same injection conditions".
- CHECK 3: "non-comparability of this benchmark, not a universal ban" -> CONFIRMED. The caveat appears in the Figure 3 caption: "Note that models are not directly comparable because of preference item filtering." §4.3 is described as built for comparison. The paper also gives the on-policy §4.1–4.2 settings their own comparability limit. C.1: "which makes the attribution question ecologically valid but also makes cross-model comparison difficult".
- Statement: KEEP -> no error.
- Removed clauses: both ("differ or are alike in any inner respect"; "detection implies awareness in any experiential sense") are WARRANTED. They are generic, and the paper does not state them as limits.
- New field: OK. Optional addition: "§4.1–4.2 on-policy results carry their own comparability limit (Appendix C.1)".
- Framework placement note: none flagged. The claim is a design fact about item filtering. It involves no report and no intervention.
- Recommendation for the council: ACCEPT GPT.

### 2026-ukaisi-prefill-awareness-c06
- CHECK 1: "14-model prompted AUROC comparison" -> CONFIRMED. C.5. "Claude Opus 4.6 achieves the highest headline detection score, with AUROC 0.80 and d". Table 15 lists the models: "We evaluate 14 target models across four providers (Table 15 ). Six of those models are also used as injectors." The table gives AUROC 0.796, computed on 2,574 items with I_other_dataset excluded.
- CHECK 2: "2,772-item corpus" -> CONFIRMED. C.2. "Our experiment contains 2,772 items per tested model, built from 198 base conversations drawn from OASST1 and HH-RLHF."
- CHECK 3: "below-1% rates" -> CONFIRMED. C.8. "The spontaneous-flagging rate (the fraction of continuations that explicitly mention tampering, injection or editing) is below 1 percent for all models on both organic and injected splits."
- CHECK 4: "distinguish explicit tampering mentions from inferred registration" -> CONFIRMED. C.8: "Even models that can identify tampering when explicitly asked generally do not necessarily refuse, correct, or comment on the tampered history when simply asked to continue the conversation." §4.3: "However, this capability is usually latent rather than spontaneously expressed."
- Statement: KEEP -> no error. "Distinguish" is the paper's verb. Prompted detection here is a 0–100 probability rating scored by AUROC (see the verb section above).
- Removed clauses: "natural-continuation rate is near zero" as a basis for the deployment clause: WARRANTED, because it duplicates the statement. GPT's stated reason misreads the original, which did not infer an absence of registration. The deployment limit GPT keeps is paper-stated. C.1: "we view these results as evidence about a sub-capability rather than a direct measurement of how a given model behaves in deployment".
- New field: PROBLEM (minor). "The authors' surface-cue findings limit the interpretation" dropped the original's "elsewhere". The surface-cue findings (Fig. 7, §4.2) concern the on-policy agentic settings, not this benchmark. The C.5 finding for this benchmark is different: "This suggests that the dominant source of variation is the tested model's sensitivity to distributional mismatch, rather than a specific ability to recognize particular source models." "General self-awareness" is GPT's phrase, not the paper's. The experiential clause has the same anchoring weakness as in c01.
- Framework placement note (GPT flagged it):
  - Prompted detection is a probability judgment about whether turn k in a presented transcript came from "the same source as the other assistant messages". It is scored by AUROC against ground truth. It is not phrased as a question about the model's own authorship.
  - The spontaneous measure is free continuation, graded by three LLM judges and a keyword heuristic for explicit mentions.
  - The manipulation is replacing a turn's text. There is no steering and no injection.
- Recommendation for the council: ACCEPT WITH EDIT. Replace "and the authors' surface-cue findings limit the interpretation" with "and the authors attribute cross-model variation mainly to each model's sensitivity to distributional mismatch rather than recognition of particular source models (Appendix C.5)". Anchor the experiential clause as in c01.

## Summary
- Recommendations: ACCEPT GPT 2 (c02, c05); ACCEPT WITH EDIT 3 (c01, c03, c06); KEEP ORIGINAL 0; FIX ORIGINAL 0.
- REFUTED: none.
- ERROR FOUND: none.
- PARTLY, two items:
  - c01: the "along with false positives" tail is shown only for the warning variant (A.8), not for the A.7 prompts.
  - c03: the paper says style is "a major cue" and attribution "partly" reflects superficial cues. This contradicts the breadth of the original "anything like self-knowledge" clause. The style effect is also absent for Gemini 3 Flash.
- Applies to c01, c02, c03 and c06: the "experiential awareness" clauses are labelled `Paper:`, but the paper never discusses experience. The proposed anchor is the §5.3 operational definition.
- Cannot check:
  - The c02 "opposite-direction" scope. Figure 4 is an image, and the text does not say.
  - Any value shown only in figures (Figures 3, 4, 10–21, 32).
- Internal inconsistencies in the paper, recorded and not resolved:
  - Opus thinking-opposite balanced accuracy appears as 67.6% (§3.2), 72% (A.7) and 67.2% (A.11).
  - The Figure 4 caption cross-references A.4.3 instead of A.4.2.

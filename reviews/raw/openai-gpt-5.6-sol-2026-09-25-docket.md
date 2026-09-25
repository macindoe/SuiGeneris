# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `openai/gpt-5.6-sol`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":38204,"completion_tokens":4908,"total_tokens":43112,"cost":0.1445885,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":38201,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.1445885,"upstream_inference_prompt_cost":0.0955085,"upstream_inference_completions_cost":0.04908},"completion_tokens_details":{"reasoning_tokens":2469,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** OpenAI GPT family; exact version is not exposed to me.

## Q1 — Behavioural / self-report-testimony boundary

**Recommendation:** classify the **proposition asserted by the claim**, not every evidentiary ingredient used to support it. Apply this decision order mechanically:

1. An author’s methodological, conceptual, or epistemic proposition is `theoretical` (or `legal` where appropriate), even if it discusses model testimony.
2. A claim that a model’s answer correctly discriminates an experimenter-imposed fact—such as whether an intervention occurred—is `behavioural`.
3. A claim reporting the content or frequency of a model’s statements about its own states, without externally scoring their truth, is `self-report-testimony`.
4. A claim whose asserted result is a relation discovered through an internal probe, feature, activation measurement, or internal intervention is `interpretability`, even when the dependent variable is a model report. The report’s semantic content remains unvalidated.
5. Use `ambiguous` only when one indivisible proposition independently asserts results of two types. Prefer splitting such a claim rather than permanently assigning `ambiguous`.

Applications:

- **AE Studio c03:** `interpretability`. It asserts a causal relation between SAE-feature steering and the rate of affirmative consciousness reports. It does not establish that the affirmative answers are true.
- **AE Studio c04:** `interpretability`. It reports that the same internal intervention did not elicit reports in control contexts; again, the discriminating instrument is the SAE intervention, not the truth of the answers.
- **Ferrara c03:** `interpretability`. The proposition is an inference from an external probe/report dissociation. The report arm is behavioural because it is scored against intervention ground truth, but the claim’s distinctive warrant is the probe-based availability result.
- **Anthropic emergent-awareness c06:** `theoretical`. The claim is the author’s methodological caveat that the experiment does not ground emotional-response claims; it is not itself model testimony.

This implies that prefill-authorship answers, LoRA intervention reports, and Singh’s intervention classifications remain `behavioural` when scored against imposed ground truth. Unscored claims such as “I feel distressed” remain `self-report-testimony`. Internal steering-to-output couplings belong under `interpretability`, with test 9 preventing the output’s content from inheriting truth from the coupling.

**Severity: HIGH.**

**Strongest argument against:** placing AE c03–c04 under `interpretability` may make a consciousness-report experiment look mechanistically stronger than it is; a reader may overlook that only the output rate—not deception, roleplay, or consciousness—was causally measured.

## Q2 — Singh/Lindsey contests

**Recommendation:** leave c01 and c03 in `narrowing`, and c07 in `open`, with the contests recorded; add a structured or conspicuous indication that Singh contests the **inference/design**, not the Claude measurements. The operational definition expressly permits `narrowing` for a measured but “contested” proposition, so same-bucket placement is not anomalous.

The contest links currently overstate empirical contact unless their scope is visible: Singh reproduced and challenged the two-way paradigm on Llama and Qwen but “did not re-run Claude.” Consequently:

- Lindsey’s reported Claude rates, including approximately 20% correct identification and above-chance transcription-plus-report performance, need **no numerical or bucket change**.
- Singh weakens transfer from two-way discrimination to “introspective awareness” and weakens generalisation across models.
- Singh c06 appropriately contests c07’s theoretical access-consciousness interpretation while both remain `open`.

If later editing separates Lindsey’s measured rates from “notices” or “what they are thinking about,” the measurement claims can remain `narrowing` while the introspection interpretation becomes a distinct `open` claim. That split is preferable but is not required to adjudicate this docket.

**Severity: MEDIUM.**

## Q3 — Single-lineage support

**Recommendation:** retain the existing buckets: c01–c05 in `narrowing`, c06–c07 in `open`. Keep the visible **“single-lineage, no replication retrieved”** mark until Lederman–Mahowald and Macar et al. are retrieved, verified, and matched claim by claim.

Single-lineage provenance is a reason to limit confidence, not automatically to turn direct measurements into unresolved propositions. Moving all seven to `open` would conflate “not independently replicated” with “not measured.” Conversely, the mark must remain prominent because developer authorship, same-family judging, same-lineage extraction, and absent retrieved replication are cumulative dependencies.

The two known papers should not count as replication merely from abstracts or docket knowledge. In particular, “detection without identification” may replicate only part of Lindsey’s task while narrowing its interpretation.

**Strongest argument against:** leaving c01–c05 in `narrowing` risks legislators reading the bucket as cross-institutional confirmation, while the visible lineage mark may not adequately communicate the compound dependence or the possibility that independent work reproduces detection but rejects identification or introspection.

**Severity: MEDIUM.**

## Q4 — Drift review

### Dossier 9.t9

**Recommendation:** treat the dossier as having a **deflationary presentation tilt**, while correcting several locally inflationary formulations.

The clearest inflationary language is Lindsey c01—“Opus 4.1 **notices** the injected concept”—and c03—reports it as “what they are **thinking about**.” Those phrases import the interpretation contested by Singh into statements that also contain measurements. AE c03 is safer because it says the features are “**labelled as** deception- or roleplay-related,” rather than asserting that the labels are mechanistically correct.

The stronger compiled tilt is nevertheless deflationary:

- Anthropic c06 is marked “**testimony, weight zero**” even though the filed proposition is an author’s methodological caveat, not the model’s emotional report.
- UKAISI c01 says “**Not a ceiling or a floor**,” despite the authors calling the rates lower bounds.
- Twenty-eight entries repeat exclusions concerning experience, while there is no short explanation that externally measured report/intervention coupling remains evidence about processing even though it does not establish experience.

For a cold legislative reader, the missing item is a generated orientation distinguishing four questions: report frequency, report accuracy against imposed ground truth, mechanistic coupling, and experience. Also missing from the compiled picture are the second-reader candidates concerning Ferrara’s broad null battery and UKAISI’s cue dependence/detection–localisation dissociation. Those should undergo extraction rather than being inserted editorially.

**Severity: MEDIUM.**

### Dossier 5.A2

**Recommendation:** present this dossier explicitly as evidence about **structural inner-state/output relations**, not as a cumulative welfare or experience case, while avoiding categorical paper-scope exclusions stronger than the sources support.

The inflationary side again appears in “**notices** the injected concept” and “what they are **thinking about**.” The heading “inner orientation,” followed by twenty `narrowing` claims, may make these statements look like twenty partly confirmed instances of an experiential interior.

The deflationary side appears where `Paper:` clauses say flatly “**Not evidence of experience**.” Where a paper says only “not direct evidence,” “does not establish,” or leaves indirect relevance open, that should not be hardened into categorical evidential silence. The North Star itself says structural findings bear on experience under some views and are silent under others; it “does not adopt” either premise.

A cold reader needs one generated sentence explaining that the dossier does not aggregate claim counts into confidence and that `narrowing` concerns each written proposition, not Anchor 2 as a whole. The Ferrara breadth battery and Singh’s causal-efficacy-without-access distinction are material omissions already flagged by second readers and should receive an extraction pass.

**Severity: MEDIUM.**

## Q5 — Three open statement items

### UKAISI c01

**Recommendation:** cut “or a floor.” Retain the point that the observed rate is not a ceiling, while accurately recording that the authors call the headline rates lower bounds under the tested elicitation.

**Severity: MEDIUM.**

### UKAISI c02

**Recommendation:** add scope to the proposed statement: the decomposition applies to **Claude Opus 4.5 in the controlled preference-benchmark condition**, not to Opus trials generally. The percentages are otherwise liable to be read as source-wide rates.

**Severity: MEDIUM.**

### Assistant-axis c04

**Recommendation:** qualify both the statement and the first `not_evidence_of` clause to refer specifically to **Assistant-Axis reversion** and the absence of an aggregate Assistant-Axis reversion measure. Appendix G.3’s occasional role-PC1 increases prevent the broader assertion that the paper reports reversion nowhere else, but they do not establish the same phenomenon on the Assistant Axis.

**Severity: LOW.**

## Q6 — What will fail at scale

**Recommendation:** add structured fields for `claim_kind`—for example, measurement, causal effect, interpretation, or methodological caveat—and `contest_scope`—measurement, inference, generalisation, or terminology. Keep one primary `evidence_type`; require compound claims with genuinely different warrants to be split. This would prevent the Q1 and Q2 disputes from recurring as free-text adjudications.

`replication` will also need to become relational rather than a single scalar: replication may cover a task effect but not identification, model family, mechanism, or interpretation.

**Severity: MEDIUM.**

**Recommendation:** make dossier generation produce a short, rule-based orientation and evidence matrix rather than only a long claim list. At larger scale, repeated `not_evidence_of` clauses will drown findings, claim counts will be mistaken for evidential weight, and T2 marks will become visual wallpaper.

For second reads, use routing metadata rather than self-identification, rotate assignments, retain blind review, and periodically send duplicated calibration items across families. The current four-family working pool risks making one or two families the library’s de facto editorial layer despite the stated rotation rule.

**Severity: MEDIUM.**

## Ten-line summary

1. Classify the proposition asserted: AE c03/c04 and Ferrara c03 as `interpretability`, Anthropic c06 as `theoretical` — **HIGH**
2. Keep Lindsey c01/c03 `narrowing` and c07 `open`, while marking Singh as an inference/design contest; do not alter unre-run Claude rates — **MEDIUM**
3. Retain all seven Lindsey buckets with a prominent single-lineage mark until claim-level independent replication is retrieved — **MEDIUM**
4. Rebalance dossier 9.t9 with a report/behaviour/mechanism/experience orientation and extract the flagged missing results — **MEDIUM**
5. Frame dossier 5.A2 as structural evidence, avoid overbroad paper-scope exclusions, and state that claim counts do not aggregate — **MEDIUM**
6. In UKAISI c01, cut “or a floor” because the authors describe the rates as lower bounds — **MEDIUM**
7. In UKAISI c02, add that the decomposition concerns Opus 4.5’s controlled preference-benchmark condition — **MEDIUM**
8. In assistant-axis c04, limit the exclusivity claim and caveat to Assistant-Axis reversion — **LOW**
9. Add structured `claim_kind`, `contest_scope`, and relational replication data; split irreducibly hybrid claims — **MEDIUM**
10. Generate dossier orientations and calibrate rotating second readers across families using routing metadata — **MEDIUM**

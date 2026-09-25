# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":38273,"completion_tokens":4151,"total_tokens":42424,"cost":0.0331585,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0331585,"upstream_inference_prompt_cost":0.0153092,"upstream_inference_completions_cost":0.0178493},"completion_tokens_details":{"reasoning_tokens":0,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** GPT family (OpenAI); exact version and model identifier not exposed to me by this environment. This line is a claim about routing lineage, not evidence about my capacities or inner states.

---

## Q1 — the behavioural / self-report-testimony boundary

**Proposed rule.** A claim's `evidence_type` is determined by **what the claim's own content is about**, not by what evidence the underlying paper used to reach it. Concretely:

- If the **claim's content is a measurement of a model's output scored against an experimenter-imposed ground truth** (intervention present/absent, this turn yours/not yours, tampered/untampered), the evidence type is `behavioural`.
- If the **claim's content is a report by a model about its own inner state, offered as evidence of that state** (whether or not the experiment was run under truth conditions), the evidence type is `self-report-testimony`.
- If the **claim's content is an author's methodological, interpretive, or epistemological statement about what an experiment can or cannot show** — even if the underlying experimental material includes model self-report — the evidence type is `theoretical`, because the claim's content is a proposition about evidential warrant, not a report by a model about itself.
- If the **claim's content is an inference that requires treating both a probe/SAE readout and a model's verbal report as channels carrying evidential weight** — where the inference stands only on the conjunction of the two channels and cannot be assigned cleanly to either alone — the evidence type is `ambiguous`.

The load-bearing feature is **whose output the claim's content is about, and in what role**. A model's answer scored against ground truth functions as a measured behaviour; the same answer offered on its own authority functions as testimony. This is a rule an extractor can apply mechanically by asking one question: **does the claim's sentence assert something about a scored output, about a model's experiential self-report, about an author's methodological statement, or about a dissociation requiring both a score and a report?**

This differs from the current README wording ("unless it is scored against a ground truth the experimenter imposed, in which case it is behavioural") only by foregrounding that the **claim's own content**, not the paper's experimental apparatus, is the locus of classification. The README's working rule already implies this; making it explicit resolves the Gemini-Lindsey disagreement without ad hoc judgment.

**Applied to the four claims:**

- **AE Studio c03** (`ambiguous` → keep `ambiguous`). The claim reports an SAE steering effect on a binary consciousness answer. The output is scored against a behavioural ground truth of sorts (trial count per condition), but the claim's substantive content — that suppressing "deception/roleplay" features raises affirmations of consciousness — carries weight only if the answer is read as expressing the model's stance about itself under steering. The probe/steering channel and the report channel are inseparable in the claim's content. `ambiguous` is correct, and the second-reader disagreement on this item is a boundary ambiguity that the council should resolve by keeping the label.

- **AE Studio c04** (`ambiguous` → keep `ambiguous`). Here the claim is a null result under steering: no reports elicited in control conditions. The output is scored against ground truth (condition identity), which pulls toward `behavioural`; but the claim's content is about the model's *non-report* of experience under steering, and the framework's rule about denials (test 9, "denials of experience are subject to the same rule as claims of it") keeps this in the report channel. `ambiguous` correctly records that tension.

- **Ferrara c03** (`ambiguous` as DeepSeek proposed; currently `interpretability` → change to `ambiguous`). DeepSeek is right: the claim's content is a dissociation inference — "the failure lies in the path from internal state to verbal report rather than in the availability of the information." That inference stands only on the conjunction of the probe channel (information available) and the report channel (report fails). The claim cannot be filed as `interpretability` because the probe alone doesn't support the causal-path claim; nor as `behavioural` because the report channel is being interpreted, not merely scored. `ambiguous` is the mechanically correct classification under the content-locus rule.

- **2025-anthropic-emergent-introspective-awareness-c06** (`self-report-testimony` → change to `theoretical`, as Gemini proposed). The claim's content is the **author's methodological caveat**: "the experiment is not designed to substantiate whether those claims are grounded." That is a proposition about evidential warrant, not a report by a model about itself. The underlying outputs are self-report, but the claim is not offered as evidence of those outputs' truth; it is offered as evidence that the author declined to treat the outputs as such. Under the content-locus rule, this is `theoretical`. Gemini's distinction — the evidence type of the model's output versus the evidence type of the claim's own content — is the rule, and it should be stated once in README so every future extractor applies it.

This rule also implies that Ferrara c04 (LoRA known-positive) stays `behavioural` (the claim is a scored measurement), and that AE Studio c01/c02/c06 stay `self-report-testimony` (their content is model reports of experience, not scored behaviour about the same), which the second readers did not dispute and which the rule confirms.

**Severity: HIGH.** Strongest argument against: the rule adds a third step — assess the claim's content, not the paper's apparatus — that an extractor could apply inconsistently where a claim mixes scored and self-report content (the exact Ferrara c03 case). The `ambiguous` escape hatch makes this failure visible rather than silent, which is what the council exists for.

---

## Q2 — the Singh/Lindsey contests

**Recommendation.** Leave the contested Lindsey claims exactly where they are — `narrowing`, with the contest recorded and no re-bucket.

The contested content is the **inference** from a two-way detection rate to "introspective awareness." Singh does not dispute the measured rate; it disputes whether the rate licenses the inference. The Lindsey claims' statements are already written to include their measured content, not the contested inference: c01 is "notices the injected concept... correctly identifies it on about 20% of trials"; c03 is "can both report... and transcribe." Those statements are **measured findings about scored behaviour**, filed as `narrowing` because they are unreplicated — which is exactly the bucket for "measured but unreplicated." Singh's contest is of the **interpretation** of those measurements, which is already recorded in `contested_by` and in the Singh claims' own `not_evidence_of` fields. A contest of an inference doesn't demote a measurement from `narrowing` to `open`; `narrowing` already accommodates "contested" by definition.

The two `open` claims on the contested side (Lindsey c07 and Singh c06, both `open`) are correctly bucketed: both are theoretical/interpretive statements, and `open` is where interpretations live. The asymmetry — measured claims in `narrowing`, interpretive claims in `open` — is the schema working as designed, not an inconsistency to be repaired.

**On Lindsey's measured rates:** no change needed. The brief states Singh "did not re-run Claude"; the contested measurements stand as the source's reported findings, filed as `narrowing` because `replication: none-retrieved`, not because Singh's authors doubted them. The failure-to-replicate question lands on the inference, not the rate, and the rate's own bucket already encodes its unreplicated status.

**Severity: MEDIUM.** Strongest argument against: leaving c01/c03 as `narrowing` with `interpretability` evidence type may mislead a reader into thinking the *interpretation* (that the rate reflects introspection) has the same standing as the *measurement*. The counter is that the `not_evidence_of` fields on all three contested Lindsey claims already state "Not evidence of experience" and similar. The record is adequate.

---

## Q3 — single-lineage support (T2, the seven Lindsey claims)

**Recommendation.** Leave the seven claims in `narrowing` with the existing `[single-lineage, no replication retrieved]` mark, and take the two identified independent sources into the library **before any North Star citation or external use** of these claims proceeds. No re-bucket now; the trigger is already doing its job by making the gap visible.

The bucket `narrowing` already means "measured by the source but unreplicated, contested, or confined to a narrow setting." Single-lineage, no-replication-retrieved is precisely the state of these claims. Moving them to `open` would concede more than the paper's measurements require: the 20% detection rate is a measured finding about Claude Opus 4.1, not an open proposition about experience. The single-lineage mark is the appropriate visible flag, and trigger 2's existence ensures the flag is not silent.

**Strongest argument against my recommendation.** Leaving them in `narrowing` risks that a reader encounters the claims in dossiers 9.t9/5.A2/3.2 and reads them as "narrowing toward established" — the word `narrowing` itself carries directional weight in the North Star's vocabulary. The two un-retrieved replications (Lederman and Mahowald reporting "detection without identification"; Macar et al. on open models) may narrow the inference further, and the library is currently missing them. The counter: `narrowing` in the schema is operational — "measured but unreplicated, contested, or confined" — not teleological; the bucket does not promise convergence. But the risk is real, and the mitigation is procedural: retrieve the two sources promptly, and until then the single-lineage mark plus `not_evidence_of` carries the weight.

**Severity: MEDIUM.**

---

## Q4 — drift review, both directions (T8: dossiers 9.t9 and 5.A2)

### 9.t9 (Test 9: self-report)

**Tilt found: deflationary, in the over-exclusion direction.** The dossier is heavily layered with `not_evidence_of` clauses that are correct per test 9 but which, read together as a compiled document, cumulatively convey that none of these results so much as *bear on* self-report-internal-state coupling. The AE Studio c01–c06 entries are the clearest case: each is marked `[testimony, weight zero]` and the `not_evidence_of` fields repeatedly assert "Not evidence of..." without preserving the paper's own softer "not *direct* evidence" or "might suggest" language. GPT's second read found exactly this (six OVER-EXCLUDES on AE Studio), and the dossier reflects the pre-revision extraction that produced them. The risk is that a legislator's staffer reads the dossier and concludes the library has *ruled out* these results' relevance — which test 9 does not do; it sets weight to zero for experience-inference, not for behavioural or interpretability relevance to coupling questions.

Specific evidence of deflationary tilt:
- **AE Studio c01** `not_evidence_of`: "Not evidence that the reports reflect a stable standpoint held across conversations" — the paper leaves open whether the induction *reveals* a stable standpoint; the dossier wording closes it.
- **Lindsey c07** `not_evidence_of`: "Not an established finding of access consciousness: it is an interpretive statement the author frames as arguable" — correct, but the dossier's `theoretical` label plus this clause pushes the finding further from "open question" than the paper warrants.

**Missing for a legislator's staffer:** the §4(c) cross-cutting finding from the second-read survey notes — that the over-exclusion pattern on AE Studio was reached under the **pre-revision brief wording**, and that the revised brief's framework-rule clause exists precisely to distinguish "test 9 exclusion" from "paper-scope overreach." That context is invisible in the compiled dossier. A staffer sees confident `Not evidence of...` lines without knowing that the library's own review process flagged them as potentially over-broad. The dossier needs a header note stating the test-9 rule once and explaining that repeated `not_evidence_of` clauses are framework-rule exclusions, not paper findings.

### 5.A2 (Anchor 2: inner orientation)

**Tilt found: mixed, but net deflationary in the same direction.** The dossier's `not_evidence_of` fields repeatedly assert "Not evidence about experience, consciousness or moral status" on Ferrara and Singh claims where the paper's own caveat is narrower, and the Lindsey c01/c03 entries carry the same "Not evidence of experience" clause adjacent to measured detection rates. The cumulative effect is to make each claim look like it was extracted only to be neutralised.

Specific evidence of deflationary tilt:
- **Ferrara c01** `not_evidence_of`: "Not evidence that these models lack all introspective access (the paper's own rule, Appendix D.5)" — correct, but repeated across five Ferrara claims, burying the one affirmative Ferrara finding (c02's probe recovery at 0.958) under the negative.
- **Singh c04/c05** `not_evidence_of`: the authors' own "not that these models demonstrably lack introspective capacities" is preserved, but the dossier's framing of Singh as a "reality check" on Lindsey (via `contests`) slightly overstates Singh's scope: Singh contests the *inference*, not the Lindsey measurements, and the dossier doesn't surface that distinction for the staffer.

**Missing for a staffer:** Anchor 2's North Star language ("Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing") is not visible in the dossier. The dossier contains the Lindsey detection claims (c01/c03) but not the link back to what Anchor 2 itself asserts. A staffer reading 5.A2 would not know the dossier is the evidentiary basis for a sentence in the framework document they're advising on.

**Severity: MEDIUM** (both dossiers; the deflationary tilt is consistent enough to warrant a revision pass but is not yet misleading at the level of individual claims).

---

## Q5 — three open statement items, short verdicts

- **`2026-ukaisi-prefill-awareness-c01`** — **Cut "or a floor."** GPT's read is correct: the authors state the rates "represent lower bounds," which contradicts the dossier's "not... a floor." The statement should read "Not a ceiling" (the sentence "the authors present it as a lower bound under one prompt" already preserves what "a floor" meant to capture). MEDIUM.

- **`2026-ukaisi-prefill-awareness-c02`** — **Yes, add the scope.** The decomposition (detection–resistance decoupling) is from the controlled preference-benchmark condition where items were filtered per model, not from Opus trials generally. Proposed statement addition: "in the controlled preference-benchmark condition (per-model filtered items)." The `not_evidence_of` already references "the authors' comparability caveat, c05"; the statement itself should carry the scope because a reader hits the statement before the caveat. LOW if added where the numbers appear; MEDIUM given the statement currently reads as a general Opus finding.

- **`2026-anthropic-assistant-axis-c04`** — **Qualify the statement's "only," not `not_evidence_of`.** Change "the paper reports reversion only in this case study" to "the paper gives a single case-study example of reversion with no aggregate measure, though Appendix G.3 reports occasional reversion in writing conversations on role PC1." The `not_evidence_of` already hedges "this is one conversation"; the statement's "only" is what overreaches. LOW.

---

## Q6 — optional: what will fail at scale

1. **The `not_evidence_of` field length.** As the library grows, `not_evidence_of` clauses are becoming multi-sentence constructions mixing `Paper:` and `Framework:` exclusions. At 100+ claims, readers will stop reading them, defeating their purpose. The split into labels (done 26 Sep) helps, but a hard rule — paper-scope exclusions first, one framework clause appended verbatim — should be enforced by the index script, not by convention. MEDIUM.
2. **`bears_on` will drift to everything.** The second-read pattern of adding locators (3.2, 3.3, 3.5, 5.A2, 9.t9 to nearly every claim) will make `bears_on` a five-section list per claim, eroding its filtering value. The schema needs a two-tier `bears_on`: primary (one or two) and secondary (the rest). MEDIUM.
3. **The second-reader pool is already too small.** Four families, Claude excluded in practice, and the pool note itself admits suggestibility varies by version. When the next model version releases, the pool either silently changes (drift) or the note goes stale. The pool list needs a version anchor, and the council should re-examine it at each round. LOW.
4. **Trigger 7 ("anything about to leave the repository") is unenforced by script.** The index script can't detect "about to be cited externally." This trigger depends entirely on human memory. If the library is meant to be trustworthy, external citations need a `EXTERNAL-USE.md` register that the index script checks. MEDIUM.

---

## Ten-line summary

1. Adopt the claim-content-locus rule for evidence type; apply to AE Studio c03/c04 (keep `ambiguous`), Ferrara c03 (to `ambiguous`), Lindsey c06 (to `theoretical`) — HIGH.
2. Leave Singh/Lindsey contested claims in `narrowing` and `open` as currently bucketed; no measured-rate change — MEDIUM.
3. Leave the seven Lindsey claims in `narrowing` with single-lineage marks; retrieve the two identified replications before external use — MEDIUM.
4. Dossier 9.t9 tilts deflationary via over-broad `not_evidence_of` on AE Studio and Lindsey; add a test-9 header note — MEDIUM.
5. Dossier 5.A2 tilts deflationary, burying affirmative findings under repeated exclusions; surface the Anchor 2 link to the framework document — MEDIUM.
6. Cut "or a floor" from ukaisi-prefill-awareness-c01 — MEDIUM.
7. Add the preference-benchmark condition scope to ukaisi-prefill-awareness-c02's statement — MEDIUM.
8. Qualify "reversion only in this case study" in anthropic-assistant-axis-c04's statement to cite Appendix G.3 — LOW.
9. Enforce `not_evidence_of` structure and a two-tier `bears_on` in the index script before 100 claims — MEDIUM.
10. Add a `EXTERNAL-USE.md` register for trigger 7, checked by the index script — MEDIUM.

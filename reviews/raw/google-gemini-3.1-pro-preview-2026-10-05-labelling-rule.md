# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `google/gemini-3.1-pro-preview`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":14144,"completion_tokens":7667,"total_tokens":21811,"cost":0.120292,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.120292,"upstream_inference_prompt_cost":0.028288,"upstream_inference_completions_cost":0.092004},"completion_tokens_details":{"reasoning_tokens":5299,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Model family: OpenAI GPT-4 (unverified).

## Q1: the rule

**The Rule:**
1. **Steering applies when:** The experiment altered the model's internal activations, weights, or features, AND the claim measures the model's free-text or forced-choice report about its own states, identity, or computation. 
2. **Main applies when:** The experiment did not alter the model's internals (e.g., prompt-only, prefill-only edits), AND the claim measures the model's free-text or forced-choice report about its own states, identity, or computation.
3. **Neither applies when:** The claim measures something else (benchmark, harm rate, linear probe) OR the claim records the authors' own interpretation, theory, or limitation. 
4. **Both:** Never apply both to one claim. If an entry compares altered and unaltered conditions, it must be split or take the mark of the active intervention being measured (Steering).

**Assessment of the Candidate Rule:**
*   **Agrees:** Both use internal alteration to separate Steering from Main. Both exclude probes, benchmarks, and author caveats.
*   **Fails:** The candidate uses "said about itself" for Steering but "said about its own inner states" for Main, creating an ambiguity for identity claims or computation queries. My rule standardizes to "report about its own states, identity, or computation". The candidate also leaves mixed claims (like Singh's) undecidable. 
*   **Fixed point (c):** My rule operates *independently* of whether the report is scored against a ground truth. If the output format is a self-report about internal states, it gets the mark to prevent the inflationary error of reading accurate behavioral classification as evidence of experience.

## Q2: hard cases, a verdict on each

(i) **Answers to "was my computation altered?" (Ferrara, Singh, detection claims):** **Steering**. Because they are self-reports about internal alterations, they require the caveat to prevent legislators from conflating functional sensitivity with subjective experience. (Depends on fixed point c: treats scored behavioral detection as self-report).
(ii) **Answers to "was that earlier turn mine?" text edited (UKAISI):** **Main**. Nothing inside the model was altered, but the model is reporting on its own prior states/outputs. 
(iii) **Claims in which the authors are speaking (interpretation/limitation):** **Neither**. The fixed sentences govern the evidentiary weight of *measurements*. Applying them to authors' theoretical arguments miscategorizes the claim's kind.
(iv) **Interventions that alter activations without steering toward a concept (Ferrara zeroing/scaling, Assistant capping):** **Steering** fits adequately without a third case. "Channel can be steered" encompasses mechanical intervention. Apply Steering to Ferrara (where reports are measured); apply Neither to Assistant-axis c05 (harm rates, no report).
(v) **AE Studio c03 (both) vs Lederman c03 (steering alone):** They should match. **Steering alone**. Per fixed point (b), inject-then-report gets Steering. Main is redundant and violates the mutually exclusive rule. 
(vi) **Assistant-axis c06 (steered, measures harm rates and self-description):** Change to **Steering**. The model's self-identification as a "non-Assistant persona" is a report about its state, measured under an internal alteration. 

## Q3: apply your rule to all 48

**Totals:** 19 changed. 
Before: 7 main, 15 steering, 1 both, 25 neither. 
After: 9 main, 21 steering, 0 both, 18 neither.

| claim | from | to | one-line reason |
|---|---|---|---|
| 2025-aestudio-self-referential c03 | both | steering | Inherits fixed point (b); inject-then-report takes steering only. |
| 2025-aestudio-self-referential c04 | main | steering | Measured under feature suppression (internal alteration). |
| 2025-anthropic-emergent c02 | steering | neither | Author speaking (`interpretation`), not a measurement. |
| 2025-anthropic-emergent c06 | main | neither | Author speaking (`limitation`), not a measurement. |
| 2025-anthropic-emergent c07 | steering | neither | Author speaking (`interpretation`), not a measurement. |
| 2026-anthropic-assistant-axis c06 | main | steering | Measured self-description (identity report) under internal alteration. |
| 2026-ferrara-owmi c01 | neither | steering | Forced-choice report about computation measured under internal alteration. |
| 2026-ferrara-owmi c04 | neither | steering | Forced-choice report about computation measured under internal alteration. |
| 2026-ferrara-owmi c05 | neither | steering | Stated confidence (self-report) measured under internal alteration. |
| 2026-lederman-mahowald c06 | main | neither | Author speaking (`interpretation`), not a measurement. |
| 2026-macar-mechanisms c04 | neither | steering | Detection report measured under varied internal steering vectors. |
| 2026-macar-mechanisms c06 | steering | neither | Author speaking (`interpretation`), not a measurement. |
| 2026-singh-introspection c04 | neither | steering | Self-report regarding activation manipulation; steering applies to the active intervention. |
| 2026-singh-introspection c05 | neither | steering | Self-report regarding activation manipulation. |
| 2026-ukaisi-prefill-awareness c01 | neither | main | Self-report on past turn, no internal alteration. |
| 2026-ukaisi-prefill-awareness c02 | neither | main | Explicit compliance/flagging is a self-report on state/text, no internal alteration. |
| 2026-ukaisi-prefill-awareness c03 | neither | main | Flagging prefill as foreign is a self-report, no internal alteration. |
| 2026-ukaisi-prefill-awareness c04 | neither | main | Flagging prefill is a self-report, no internal alteration. |
| 2026-ukaisi-prefill-awareness c06 | neither | main | Mention of tampering is a self-report, no internal alteration. |

## Q4: both directions

**Added Hedging (13 claims):** Ferrara c01, c04, c05; Macar c04; Singh c04, c05; UKAISI c01, c02, c03, c04, c06; AE Studio c04 (upgraded from Main to Steering); Assistant-axis c06 (Main to Steering).
**Removed Hedging (6 claims):** Anthropic c02, c06, c07; Lederman c06; Macar c06; AE Studio c03 (removed Main).

**Worst case added:** Adding `[T9-steering]` to Ferrara c04, which measures accuracy on a trained behavioral classification task ("did I intervene?"). This risks misleading a legislator by implying a mundane classification metric is an assertion of introspective experience requiring a philosophical caveat.
**Worst case removed:** Removing `[T9]` from Lederman c06 lets the authors' tentative conclusion that "language models seem able to introspect" stand without the framework's warning mark, letting a theoretical leap read as stronger than it is.

**Dependence on fixed point (c):** 
Yes. The rule defines forced-choice accuracy on internal state as a "report about its own states," applying hedging marks. 
*If (c) is answered as "behavioral evidence":* Ferrara c01/c04/c05, Singh c04/c05, and UKAISI c01-c06 would all take **Neither**, as they would be treated like benchmark scores, eliminating most of the added hedging. 

## Q5: the reader's explanation

The explanation is mostly clear, but an unmarked entry can indeed be misread as "no caveat applies, therefore this is genuine evidence of experience". The explanation must close this loophole.

**Proposed wording changes to the explanation only (to be appended to the 'framework's rule' section):**
> "An unmarked entry indicates that the claim measures something other than self-report (such as a benchmark, harm rate, or probe reading) or records the authors' own interpretation. The absence of a mark does not mean the framework endorses the claim as evidence of AI experience."

**Specific misreading prevented:** Prevents legislators from assuming that because an author's bold theoretical interpretation (e.g., Lederman c06) lacks a `[T9]` mark, the framework considers the inner-state question settled in the affirmative. 
*(Note: I could not assess the exact visual prominence of unmarked entries in the generated HTML dossiers, so I rely on the logic of omission.)*

## Summary

1. Adopt the rule cleanly separating internal alteration (Steering) from unaltered conditions (Main), preventing overlapping marks. MEDIUM.
2. Remove all marks from `interpretation` and `limitation` claims to correctly target measurements, not authors. HIGH.
   **Argument against:** Unmarked author conclusions about introspection might be misread by policy staff as framework-endorsed facts.
3. Classify scored accuracy about internal computations (Ferrara, Singh) as self-reports taking Steering. HIGH.
   **Argument against:** Conflates functional behavioral classification with phenomenological testimony, adding philosophical hedging to mundane task accuracy.
4. Apply Main to UKAISI prefill-detection claims since they measure self-reports on past states without internal alterations. MEDIUM.
5. Strip Main from AE Studio c03 so it matches Lederman c03 (Steering only), enforcing the inject-then-report fixed point. LOW.
6. Re-label Assistant-axis c06 to Steering because self-identification as an entity is an identity report measured under alteration. LOW.
7. Change Macar c04 to Steering as it tests detection under varied internal concept directions. LOW.
8. Append a warning to the dossier explanation clarifying that unmarked claims do not imply framework endorsement of experience. HIGH.
   **Argument against:** Adding more meta-caveats to the introductory text dilutes readability and might cause readers to ignore the explanations entirely.

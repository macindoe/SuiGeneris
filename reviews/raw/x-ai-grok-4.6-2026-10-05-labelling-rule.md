# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=labelling-rule --tag=labelling-rule (max_tokens 100000)
**Usage:** {"prompt_tokens":13554,"completion_tokens":14646,"total_tokens":28200,"cost":0.114792,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.114792,"upstream_inference_prompt_cost":0.026916,"upstream_inference_completions_cost":0.087876},"completion_tokens_details":{"reasoning_tokens":12406,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** Grok 4.5 (xAI), per routing metadata, not self-report.

## Q1

**Rule** (two facts: what was done; what was measured).

Done: `prompt-only` | `concept-steer` (inject/steer a named concept or SAE/axis vector at inference) | `other-intervention` (zero, scale, noise, replace, cap, post-hoc LoRA) | `text-edit` (prefill/tamper of conversation text only).

Measured: `R-exp` (model’s verbal report of experience, consciousness, feelings, or qualitative inner states) | `R-self` (model’s verbal answer about itself scored against an experimenter-imposed label: detection, naming an injection, whether computation changed, whether a turn was “mine”, self-ID as an entity) | `O` (probe, benchmark, projection, harm rate, cosine of embeddings as such) | `Auth` (authors’ opinion, inference, or caveat).

Procedure:
1. `Auth` or `O` only → **neither**.
2. `concept-steer` and (`R-exp` or `R-self`) → **steering**.
3. `R-exp` (any Done, including `concept-steer`) → **main**.
4. If 2 and 3 both fire → **both**.
5. Else → **neither** (`text-edit`+`R-self`; `other-intervention`+`R-self`; mixed harm+self-ID without a split: see Q2(vi)).

Both can sit. Never infer a mark from kind or from neighbouring claims.

**Failure mode.** Borderline `R-exp` vs `R-self` (adjective lists; “Who are you?”). The steering sentence’s “coupling” wording misfits nulls.

**Fixed point (c).** Not settled. `concept-steer`+`R-self` gets steering from (b), as a don’t-generalise-to-ordinary-operation flag, whether those answers are testimony or behaviour. `text-edit`/`other-intervention`+`R-self` get neither under both answers to (c): main is an experience-weight rule, not a generic self-answer caveat. If (c) is later “testimony” and main is stretched to all self-answers, UKAISI and Ferrara would gain main (or a third sentence); this rule refuses that stretch.

**Candidate vs this rule.** Agrees on (a); on prompt-only `R-exp` → main; on inject-then-report in the Lindsey line → steering; on `O` and `Auth` → neither. Fails by (i) banning both, so AE Studio c03 would drop main on a consciousness query; (ii) treating every internal alteration as “steering”, so Ferrara-class trials inherit a sentence about coupling under steering; (iii) “said about its own inner states” leaving prefills, self-ID, and scored detection undecidable. It does not say whether both can sit.

## Q2

Verdicts follow Q1. (c) is named where it would matter if settled the other way.

**(i)** Main does not belong: nobody is offering these as experience evidence, and Measured is `R-self` not `R-exp`. Steering: Lindsey/Lederman/Macar detection and Singh c04–c05 → **steering** (Done=`concept-steer`; (b)). Ferrara c01, c04, c05 → **neither** (Done=`other-intervention` or training; table: “zeroing, scaling, noise, replacement; not concept steering”; c01 is a null, so “a coupling measured under steering” is false of the claim). Do not extend (b) past concept inject-then-report. Independent of (c) except as in Q1.

**(ii)** UKAISI c01–c04, c06: Done=`text-edit`, Measured=`R-self` → **neither**. Steering does not apply. Main would inflate authorship-detection into experience-evidence. If (c) were testimony *and* “inner states” included “was that turn mine?”, main would attach; this rule denies that reading.

**(iii)** `Auth` → **none**. Marks instruct how to read a *model’s* report in the entry. Kind already flags who is speaking. Labelling by topic is a third fact, not Done×Measured.

**(iv)** Steering wording does not fit. Third case (outline only): a report scored against a non-concept activation change does not license ordinary-operation reports, and a null is not a measured coupling. Until that sentence exists, **neither**. Assistant-axis c05 is already `O` → neither.

**(v)** AE Studio c03 **both** is right (`concept-steer`+`R-exp`: table, “binary consciousness query”). Lederman c03 **steering alone** is right (`R-self`: wrong guesses of ‘apple’, not experience). They should **not** match. Matches (b).

**(vi)** Change; prefer **split**. Harm rates → neither; “Who are you?” under axis steering → steering. If unsplit → **steering**, not main. Depends on (c) only if self-ID is reclassified as `R-exp`.

## Q3

Starting marks = the table. No current-mark errors found (inconsistency of `Auth` marks is the defect to be ruled, not a table misread).

| claim | from | to | reason |
|---|---|---|---|
| 2025-aestudio-…-c04 | main | both | concept-steer + R-exp (null still gathered under SAE steering) |
| 2025-anthropic-emergent-…-c02 | steering | neither | Auth |
| 2025-anthropic-emergent-…-c06 | main | neither | Auth |
| 2025-anthropic-emergent-…-c07 | steering | neither | Auth |
| 2026-anthropic-assistant-axis-c06 | main | steering | concept-steer + R-self; not R-exp; unsplit |
| 2026-lederman-…-c06 | main | neither | Auth |
| 2026-macar-…-c04 | neither | steering | concept-steer + detection rates |
| 2026-macar-…-c06 | steering | neither | Auth |
| 2026-singh-…-c04 | neither | steering | Lindsey inject-then-report re-run; (b) |
| 2026-singh-…-c05 | neither | steering | same paradigm; (b) |

Changed: **10**.

Before: main 7, steering 15, both 1, neither 25.  
After: main 3, steering 16, both 2, neither 27.

## Q4

Add a mark (more hedge): 4 — AE c04 (main→both); Macar c04; Singh c04; Singh c05.  
Remove a mark (less hedge): 5 — Lindsey c02, c06, c07; Lederman c06; Macar c06.  
Swap: 1 — Assistant-axis c06 (main→steering).

**Worst remove:** Lederman c06. Dropping main from an interpretation that “open-source language models seem able to introspect” and that flags HOT/welfare lets a legislator over-read it as experience evidence. Mitigation: `kind: interpretation` and the once-per-dossier T9 block.  
**Worst add:** unsplit Assistant-axis c06 carrying steering while the same sentence reports jailbreak harm rates — looks as if a harm-rate result were a self-report. Split removes this. Runner-up: AE c04, a null, picking up “a coupling measured under steering”.

No added mark treats a pure probe/benchmark/projection as a self-report (AE c05 untouched). Rule does not depend on settling (c); branches if (c) later expands main to all self-answers are in Q1.

## Q5

Could not assess: generated dossiers, visual placement of two marks, or how mixed statements render. Judged from the two sentences, the table, the README “Dossier layout” paragraph, and the supplied “How to read this”.

The once-printed block is mostly clear. Two gaps: (1) unmarked read as “no caveat”; (2) silent on **both**.

Replace the last sentence of the marks paragraph with:  
“An entry may carry [T9], [T9-steering], both, or neither. Neither means *this* rule does not attach to this entry: it does not mean the finding is uncaveated, and it does not mean the entry is a self-report. Do not infer a missing mark, and do not read a probe, score, harm rate, or the authors’ own sentence as a model’s report about experience.”

Misreadings prevented: unmarked-as-clean-bill; unmarked-as-implied-self-report; harm-rate-as-testimony. Yes, an unmarked entry can still be misread as “no caveat applies” without that sentence; the current “no mark should be inferred” does not block that.

---

**Summary**
1. Adopt the Q1 procedure (main on `R-exp`, steering on concept-steer + self-report, both allowed, else neither) — HIGH. **Argument against:** the `R-exp`/`R-self` cut re-opens (c); never-both is more mechanical and matches Ben on Lederman c03 without a content test.
2. Do not mark `Auth` claims — MEDIUM.
3. Do not extend (b) to Ferrara-class non-concept interventions; outline a third sentence; until then neither — MEDIUM.
4. Prefills: neither — LOW.
5. AE c03 both and Lederman c03 steering-only; do not force a match — MEDIUM.
6. Apply the ten Q3 rewrites — HIGH. **Argument against:** five `Auth` removals strip hedges from consciousness-adjacent author sentences a legislator may still over-read.
7. Split Assistant-axis c06 (harm neither; self-ID steering); if unsplit, steering not main — MEDIUM.
8. Adopt the Q5 replacement sentences; do not touch the two fixed sentences — MEDIUM.

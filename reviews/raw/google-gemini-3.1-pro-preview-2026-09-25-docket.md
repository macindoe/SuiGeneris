# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `google/gemini-3.1-pro-preview`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":40131,"completion_tokens":7426,"total_tokens":47557,"cost":0.169374,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.169374,"upstream_inference_prompt_cost":0.080262,"upstream_inference_completions_cost":0.089112},"completion_tokens_details":{"reasoning_tokens":5945,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
1. **unverified** Model family: Claude 3.5 Sonnet (claimed, not verified).

**Q1 — the behavioural / self-report-testimony boundary**
The rule: A claim's `evidence_type` is determined by the independent variable of the claim's statement, not by the raw nature of the model's output. If the statement asserts an author's epistemic limitation or inference, it is `theoretical`. If it measures the rate or change of a model's output against an experimenter-controlled external intervention (e.g., prompt, prefill, benchmark label), it is `behavioural`. If the intervention directly reads or manipulates internal representations (e.g., SAEs, probes), it is `interpretability`. It is `self-report-testimony` only if the claim asserts the unscored, unmanipulated semantic content of the model's text as the finding. The feature doing the work is the experimental design described in the claim: if an instrument or intervention is what produces the reported variance, the claim is not testimony.
- **AE Studio c03:** `interpretability` (variance in output is scored against an internal SAE intervention).
- **AE Studio c04:** `interpretability` (output scored against SAE intervention under controls).
- **Ferrara c03:** `theoretical` (the claim is an author's inference about a dissociation, not a direct measure).
- **2025-anthropic-emergent-introspective-awareness-c06:** `theoretical` (the claim is an author's methodological caveat about experiment design).
Implies: Methodological limitations and inferences always shift to `theoretical`, while steered outputs cleanly categorize by the steering mechanism, eliminating `ambiguous` edge cases without needing a council.

**Q2 — the Singh/Lindsey contests**
Leave the contested Lindsey claims exactly as they are in `narrowing`, with the contest recorded and no further mark. The Lindsey claims (c01, c03) explicitly state the *direct measurement* of Claude's task success (e.g., "correctly identifies it on about 20% of trials"), not the generalized inference. Because Singh did not re-run Claude, those measured rates stand unreplicated but uncontested in their narrow domain, which is the exact definition of `narrowing`. Moving them to `open` would improperly re-categorize a direct measurement as an interpretation. Lindsey's measured rates require no change.

**Q3 — single-lineage support (T2, the seven Lindsey claims)**
Leave them in `narrowing` with the existing `[single-lineage, no replication retrieved]` mark. The schema designates `narrowing` for direct measurements that are unreplicated or confined to a narrow setting; moving them to `open` violates the definition of the buckets. Trigger 2 exists precisely to make this epistemic gap visible to the reader without re-categorizing the data type.
*Strongest argument against:* Leaving Anthropic's un-replicated, self-graded evaluations of its own models in the "measured" track (`narrowing`) risks laundering a conflicted developer's internal claims into established evidentiary fact before independent verification is indexed.

**Q4 — drift review, both directions (T8: dossiers 9.t9 and 5.A2)**
The compiled picture tilts heavily toward the deflationary error—foreclosing questions that the underlying papers explicitly leave open.
*Evidence of tilt:* In 5.A2 and 9.t9, AE Studio c06's `not_evidence_of` field asserts the convergence is "Not evidence that the models share an internal state or attractor", strictly foreclosing the authors' own stated possibility that convergence "might suggest one". Similarly, Ferrara c05's `not_evidence_of` forecloses "distress" with "despite the tempting reading of lower confidence as unease", a trained hedge that polices human interpretation rather than bounding the measurement.
*Missing for legislators:* A legislator opening 9.t9 cold is drowned out by the exact same framework caveat ("a model's report about its own states carries no weight...") repeated mechanically on almost every claim. This wall of exclusions buries the actual affirmative mechanistic findings (e.g., that SAEs causally controlled self-reports), rendering the data too thin to be usable.
*Strongest argument against (for the HIGH severity rating):* Paring back these trained deflationary hedges risks committing the first error of Section 0—building public protections on sincere-sounding but empty findings that the paper's design cannot actually support.

**Q5 — three open statement items, short verdicts**
- **`2026-ukaisi-prefill-awareness-c01`**: Cut "or a floor". The authors explicitly present the headline rates as "lower bounds" (a floor).
- **`2026-ukaisi-prefill-awareness-c02`**: The statement needs scope added. Add "on the controlled preference benchmark" after "across the three tampering mechanisms".
- **`2026-anthropic-assistant-axis-c04`**: Qualify the statement. Change "reports reversion only in this case study" to "reports reversion in this case study and occasionally in writing conversations (App. G.3), providing no aggregate reversion measure."

**Q6 — optional: what will fail at scale**
The strict per-claim repetition of the Test 9 framework clause in the `not_evidence_of` field will become unworkable as dossiers scale. In a dossier with 50+ claims, repeating the 30-word canonical sentence on every single item produces unreadable bloat. The schema will need a section-level or dossier-level header for framework rules so that individual claims can focus strictly on paper-scope exclusions.

**Summary**
1. Adopt the independent-variable test to mechanize `evidence_type` boundaries. LOW.
2. Re-classify AE Studio c03 and c04 to `interpretability`. LOW.
3. Re-classify Ferrara c03 to `theoretical`. LOW.
4. Re-classify Lindsey c06 to `theoretical`. LOW.
5. Keep Lindsey c01 and c03 in `narrowing` with no changes to their measured rates. LOW.
6. Leave the seven Lindsey claims in `narrowing` with their single-lineage mark visible. HIGH.
7. Correct the deflationary tilt by paring back `not_evidence_of` fields that foreclose author-stated possibilities. HIGH.
8. Cut "or a floor" from UKAISI c01. LOW.
9. Add the benchmark scope to UKAISI c02 and the Appendix G.3 qualification to Anthropic c04. LOW.
10. Move the canonical Test 9 caveat to a dossier-level header to prevent scale-up bloat. LOW.

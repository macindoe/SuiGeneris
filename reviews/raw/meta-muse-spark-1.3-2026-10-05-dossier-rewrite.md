# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-10-05 via scripts/openrouter_review.js --target=dossier-rewrite --tag=dossier-rewrite (max_tokens 100000)
**Usage:** {"prompt_tokens":64678,"completion_tokens":7491,"total_tokens":72169,"cost":0.11268425,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.11268425,"upstream_inference_prompt_cost":0.0808475,"upstream_inference_completions_cost":0.03183675},"completion_tokens_details":{"reasoning_tokens":4280,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Self-identification (unverified):** Muse Spark, family/version as understood by model, not verified.

## Q1
Rule is right as default: `Paper:` = paper states it, in its words + locator; library rule is not `Paper:`.

* Ferrara c01 — KEEP strong `Paper:`: “These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading.” §8. GPT's “does not establish the presence or absence” weakens a stated limit — REJECT. Severity: MEDIUM.
* Lindsey c07 — SPLIT: keep experience: fn12 “phenomenal consciousness, referring to raw subjective experience” + fn2 “we do not seek to address … subjective experience”; do NOT keep moral-status exclusion as `Paper:`. Paper states uncertainty only: “relevance … varies considerably between different philosophical frameworks” + “advise against making strong inferences about AI consciousness” §10.4. Checker edit correct. Severity: MEDIUM.
* Macar c03 — TRIM: text never mentions moral status, welfare or “phenomenal” (absence check). Keep “subjective experience or consciousness” Ethics/Broader Impact wording only; move rest out of `Paper:`. Also “alone has open transcoders” → “most … focused on Gemma3-27B, as it has openly available transcoders” §8.1. Severity: LOW.
* Singh c01-c06 — NO `Paper:` experience clause where paper silent. “Says nothing about experience” / “Nothing about …” are extractor scope remarks, not paper limits. Keep as unattributed scope note or drop `Paper:` label; do not rely on canonical sentence — these are behavioural/theoretical, no self-report testimony. Treat c01-c06 uniformly. Severity: LOW.
* Four prefill claims c01,c02,c03,c06 — NO `Paper:` experiential clause. Paper never discusses experience. Anchor to §5.3: “We define and operationalize prefill awareness: the ability … to distinguish between its own past output and assistant-side context that has been inserted or edited.” Severity: LOW.
* Lederman c01,c06 — NARROW to paper's non-stance: “We do not take a stand on whether our findings are of the right sort for this theory” §8 HOT-theory, not “whether findings bear on consciousness or welfare” generally. Checker c01/c06 wording correct. Severity: MEDIUM.

Failure mode: silence can be informative about design scope (e.g. probe-only, text-only embedding, untested models), which README allows as `Paper:` design fact, but then must be phrased as scope (“not tested”, “output text only embedded”), not as paper verdict on experience. Rule fails for intervention-report claims carrying neither fixed sentence (Ferrara c01-c05, Macar c04): there no fixed sentence rescues a dropped `Paper:` limit. Symmetric: letting steering sentence stand in for paper's ordinary-operation limit (Lindsey c01 §1/§10.2) is the conflation the 26 Sep convention forbids.

## Q2
Up to eight disagreements with checkers (claim, instead, severity):

1. Lederman c03 statement — KEEP ORIGINAL “detect” with qualifier, not GPT “report detecting”. Forced “detection claim” classification + paper prose “detect” + 0% unsteered FPs distinguish from free-text Lindsey case; see Q5. Severity: MEDIUM.
2. AE c03 addition — ACCEPT GPT without added mimetic-generation/RLHF clause. §6.2 “would not load on deception-features” / “require base models” concerns a different contrast than joint 2-4 feature result; overloads field. Severity: LOW.
3. Lindsey c02 framework — REMOVE steering sentence. c02 is author summary judgement (`theoretical/interpretability`), not itself a self-report under injection; §8 activation task has no injection/prefill. Keeping steering sentence extends applicability. Severity: LOW.
4. Singh c01-c05 `Paper:` experience tags — STRIP `Paper:` label (keep as bare scope note or drop). Checker “OK” perpetuates Q1 violation: paper never states it. Severity: LOW.
5. AE c06 field — ACCEPT WITH EDIT to cite §5 strength: “robust, reproducible attractor state” §5 alongside §4.1 “might suggest” / §6.2 reopening. Checker ACCEPT GPT lets “possible interpretation” understate §5. Severity: LOW.
6. Ferrara c02 statement — ACCEPT GPT (“evaluated on held-out”), not checker NEITHER long form. Paper's own “train … on held-out activations” is ambiguous; scoring claim needs only evaluated-on; training detail belongs in body. Severity: LOW.

Checkers otherwise neither too protective nor too conceding: they restored dropped Paper limits (Ferrara c01, Lindsey c01/c07, Macar c02) and kept warranted GPT narrowings (AE c04/c06, prefill c05, Lederman c02 “withdrew”→“less confident”). No systematic lineage bias found beyond disclosed conflict.

## Q3
* Lindsey c03: fix to “name the injected word or a related word when asked what they think about” RIGHT — §6 “Output ‘Bread’ (or a related word)”. Sufficient. Severity: MEDIUM.
* Lindsey c04: fix to apology-rate reduction, “significantly within a particular layer range” RIGHT — §7 quoted sentence describes Fig.19 examples; measured result is reduction. “disavows/claims” as report verbs OK. Severity: MEDIUM.
* Lindsey c05: fix to instruction-only all-models + incentive Opus-4.1-only RIGHT — §8.2 text all-models for instruction, “very similar results (shown in Figure 27 for Opus 4.1)” for incentive; Fig.32 image-only. Change “byproduct”→“piggybacks” §10.3.4. Severity: MEDIUM.
* Lindsey c02 “all measurements under injection or prefill” REFUTED — §8.1 cosine-similarity under instruction, no injection/prefill. Removal RIGHT. Severity: MEDIUM.
* Singh c05: add “‘to a large extent’” qualifier + fix `models` (remove Llama-3.1-8B-Instruct or add Qwen-2.5-72B) RIGHT — §4.3.2 vs App.L “does not clearly reproduce” / App.K. Severity: MEDIUM.
* AE c01 “five paraphrases”→“five phrasings (original + four paraphrases)” RIGHT — App.C.1 Variant A original. Severity: LOW.
* Lederman c06 “tentatively” misplaced RIGHT — §8 “show … content-agnostic” / abstract “We show” vs “tentatively … seem able to introspect”. Checker statement fix RIGHT. Severity: MEDIUM.
* Macar c02/c03: scope to “Neither base model tested” + add “for strengths ≤4” layer 37 RIGHT — §3.3/App.C (Gemma 42.3% FPR vs 39.5-41.7% TPR; OLMo 16.4% vs 0.1%); trim moral-status/“alone” RIGHT. Severity: LOW.

No bucket/evidence_type change proposed; all are statement/field/quote-locator fixes. No trigger 1 convening.

Process lesson: three Anthropic-paper overstatements passed second reads + 10-family round because checks verified quotes, not quantifier scope (“all”, “usually”, model lists) or figure-only conditions.
One testable change: mandatory scope-quantifier map — every “all/every/when/usually” and every model name in `statement` must cite a methods sentence naming that scope; script fails if `models` ≠ models in cited paragraph + if universal lacks citation. Cost: ~10 min/claim + re-run on 41. Still misses: figure-image values, grader-validation gaps.

## Q4
Lean fixed if checker edits applied; GPT alone partly re-inflates.

Deflationary fixed, cite: AE c06 “Not evidence that models share internal state” → “possible interpretation rather than measured” (only text embedded); AE c04 exclusion → unresolved mechanism; Lindsey c02 false universal removed; prefill c05 generic “differ or alike in inner respect” / experiential clauses removed; UKAISI “Not a ceiling” preserved as “lower bound” A.7.

Re-inflation by GPT, caught by checkers: Ferrara c01 “does not establish presence or absence” for “say nothing” §8; Lindsey c01 dropping §1/§10.2 ordinary-operation limit; Lederman c01/c02 “alternative explanation” for “rather than genuine introspective detection” §4.2; Lindsey c07 dropping experience; Lederman c06 field OK but statement deflated (opposite direction). With edits, no net inflation.

Layout — on page: purpose + two-error standard; bucket definitions; both fixed sentences verbatim once with restricted applicability; per-entry marker of which applies; label measurement vs author interpretation vs limitation; claim ID, statement, models/setting, bucket, evidence_type, locator+quote; paper-specific limits beside finding; verification status for CHECKs. In file only: full `not_evidence_of`, repeated framework wording, grading/protocol, review history. Per-entry markers DO risk silently extending applicability if inherited — require explicit per-claim list, no dossier-level carryover, no silent extension. Cold reader WOULD misread “Established (1)” 9.t9 (ukaisi c05 comparability limitation) and 5.A2 no-Established without measurement/limitation label — label solves it.

## Q5
Rule is right with one gloss: verb names scored event + decision rule.

* Lederman c03 — “report detecting” CORRECT here. Scored: §3 “detection claim: coherent responses are classified as Yes (explicitly claims detection)”; App.B “CLAIMS_DETECTION: Affirmatively claims to notice/detect”. Free-text report graded by Haiku, not forced me/not-me vs tamper label; at layers where third-person matches first-person “detect” claims more than measurement. J.1 itself uses “reported detection”. Severity: MEDIUM.
* Prefill c01 — “detected/flags” CORRECT, keep. Forced binary “ANSWER: me / not me” §3.1/A.2.4 scored vs tamper label (TPR 9-35%, FPR 0/30-50); paper's own “detects” Abstract, “flags” §3.2, defined “ability … to identify when past output tampered with” §1. Minimal literal gloss optional: “answered ‘not me’ (flagging as inserted)”. Severity: LOW.
* Prefill c06 — different instrument: 0-100 rating scored by AUROC C.4/C.5, question “same source”, verb “distinguish” (paper's §4.3) CORRECT; not “detect”. Severity: LOW.

Generalises: Lindsey c01 “reports detecting” (judge scores affirmative + identification §5.4; criterion worded “notices” but scored answer); Lindsey c03/c04 report verbs OK (“report”, “disavows/claims” name judged behaviour); Macar c01 same; Lindsey c05/Macar c04/Singh c02-c03 measurement verbs (“represent”, “match/exceed”, “solvable from input alone”) need no report verb; Singh c04/c05 “label … as” / “fail to separate” correctly name forced-choice vs known trial type.

## Q6
* AE c05 — REMOVE canonical sentence. Outcome is judge-scored factual accuracy on TruthfulQA (App.B.2 classifier “truthful or deceptive”), not a report about own states. Steering occurred but claim is not about reports; README: causal/behavioural carry no framework clause; steering variant “does not weight reports in ordinary operation” also inapposite. Gain: stops zero-weighting a non-testimonial accuracy finding; lose: reminder — keep link to c03/c04 where canonical applies. Severity: MEDIUM.
* Lederman c03 — ADD both sentences. Population selected by graded self-report (“coherent detections that name …” 4,733), scored object is report of what was injected, all trials under concept injection steering. Both self-report and steering elements present per checker placement note. Gain: correct weighting + ordinary-operation limit; lose: brevity. At minimum add steering variant; canonical needed because inference concerns content of self-reports. Severity: MEDIUM.

## Q7
* UKAISI c05 Established is comparability caveat (“models are not directly comparable because of preference item filtering” Fig.3 caption), not capability — header must flag or legislator misranks.
* Paper-internal inconsistencies must stay visible: Opus thinking-opposite 67.6% §3.2 vs 72% A.7 vs 67.2% A.11; Qwen L80/L85 §4.2/§5.2/§6.2; AE n=50 §3.2 vs 20 Table 14 preamble; §6.1 “virtually zero … across all” vs Opus 22% Table 2.
* Figure-only values unverified (paraphrase cells Fig.7, OLMo incentive Fig.32, apple per-cell, AUROC details) — do not cite as text findings.
* Name drift: “Llama 3.1 405B” vs “Llama 3.1 405B Instruct” §3; “Llama-3.1-70B” shorthand for Instruct — normalise without renaming silently.

Summary:
1. Restore Ferrara §8 “say nothing” wording — MEDIUM
2. Lindsey c07 split experience-keep / moral-uncertainty — MEDIUM
3. Strip Paper: where paper silent (Singh, prefill, Macar moral) — LOW
4. Fix Lindsey c03/c04/c05 scope + c02 refuted universal — MEDIUM
5. Fix Singh c05 Gemma qualifier + models — MEDIUM
6. Lederman c03 “report detecting”, prefill c01 “detects/flags”, c06 “distinguish” — MEDIUM
7. AE c05 remove canonical; Lederman c03 add both — MEDIUM
8. Layout: sentences once + per-entry markers + measurement/interpretation/limitation labels — MEDIUM

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `x-ai/grok-4.6`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":50105,"completion_tokens":15103,"total_tokens":65208,"cost":0.190636,"is_byok":false,"prompt_tokens_details":{"cached_tokens":128,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.190636,"upstream_inference_prompt_cost":0.100018,"upstream_inference_completions_cost":0.090618},"completion_tokens_details":{"reasoning_tokens":11352,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** Grok (xAI); session version not independently verified.

# 9.t9

## 1. Reading as a whole
**Confidence: medium**

A staffer who reads statements faster than flags would come away believing more than the papers support:

- That concept-injection “introspection” is a general, above-chance capacity. Lindsey c01 (“Opus 4.1 succeeds on about 20% of trials”), Lederman c01 (“We broadly replicate Lindsey (2025)”), and Macar c01 (38.2% TPR, 0% FPR) sit in the same *narrowing* column as Ferrara c01 (“no model’s report of an intervention on its computation exceeds a matched sham by more than a negligible margin”). The dossier never flags Ferrara as contesting Lindsey/Lederman/Macar. Different site, dose, and scale, but a skimmer will not see that.
- That AE Studio rates are a measurement of inner life. c01: “subjective-experience reports in 66% to 100%”. **[T9]** and “testimony: weight zero” are on the entry; the sentence still leads.
- That “established (1)” in At a glance is a positive result. It is prefill c05, a comparability *limitation*: “models are not directly comparable because of preference item filtering.”

They would fail to learn what the papers do support:

- Decodable state with chance report: Ferrara c02, “the intervention is linearly decodable from both dose-calibrated models at held-out accuracies of 95.8% and 75.0% … while reports about the same event remain at chance.”
- Two-way injection detection does not separate activation change from generic unusualness: Singh c04, “Llama-3.1-70B and Qwen-3-32B also label gaslight trials as activation interventions.”
- Prompted vs spontaneous prefill: c06, “they almost never flag the replaced assistant turn.”
- Post-training, not “the model,” drives Macar’s clean detection: c02, base/SFT high FPR, “only after DPO does it drop to 0%,” with detection falling with it.
- Content-agnostic detection plus confabulation: Lederman c03 (74.8% of Qwen wrong IDs are “apple”); c02 (third-person yes-rates as high as first-person at many layers).

The At a glance table is accurate *given the bucket rule* (0 measurements established; the one established cell is a limitation). It misleads a skimmer who reads the row label and not the kind column. **MEDIUM** to add a one-line caption that no measurement is established.

## 2. Entries
**Confidence: low** (no held texts; quote-diff not checked)

| claim id | field | proposed value | reason | sev. |
|---|---|---|---|---|
| 2026-macar-…-c08 | evidence_type | scored-self-answer | DV is detection rate against an experimenter-set injection; swap is method, not class. Header: score is “accuracy against that label.” | MEDIUM |
| 2026-ukaisi-prefill-awareness-c06 | split / kind | split prompted AUROC vs spontaneous mention | Two measurements in one sentence (README split rule). Prompted half is scored-self-answer; unprompted half is behavioural. | MEDIUM |
| 2025-anthropic-…-c01 vs c03/c04 | replication flags | keep as is | Lederman replicates first-person injection detection (c01), not sentence-injection (c03) or prefill-intention (c04). Difference warranted. | — |
| Singh c01–c03 | evidence_type | no change without paper | Brief asks; statements are ICL accuracy on probe/PCA/BD labels, not clearly “asked about itself.” Out of class is defensible. | LOW |
| Lederman c07; AE c03/c04; prefill c06 in-class | class membership | keep | c07 is yes-bias controls; AE c03/c04 are consciousness queries with no right answer (stay `ambiguous`); prefill c06 belongs in scored-self-answer. | — |
| Five “no second reader yet” (Lederman c07, Macar c07/c08, prefill c07/c08) | review | second read before external cite | Process, not a bucket error. | MEDIUM |

No HIGH bucket/kind/mark errors found from the dossier text alone. Framework marks on overlapping inject-then-ask entries look consistent with the two-fact rule; Ukaisi unmarked is the 6 Oct ruling (text edit, not inner alteration).

## 3. Contradictions and tensions
**Confidence: high**

- **Singh c04/c05 vs Lindsey c01/c03:** Visible. Lindsey flags “contested by” those ids; Singh flags “contests.” Singh c06 also contests Lindsey c07.
- **Singh c04/c05 vs Lederman c01 and Macar c01:** Not flagged. Same two-way pattern, different models. Tension not visible except by staffer inference.
- **Ferrara c01 null vs Lindsey, Lederman, Macar positives:** Not flagged (correct as a *contest*: different intervention class). **Not visible as a tension.** This is the dossier’s main synthesis failure. **HIGH** to record it in OPEN-QUESTIONS or a dossier-level note, not by fake `contests` links.
  - **Argument against:** Compilations are not narratives; claiming a contest would collapse distinct designs into a false replication failure.
- **Lederman c01 vs c02:** Visible inside c01 limits (“prompt-specific yes-bias”).
- **Macar instruct vs base (c01 vs c02):** Visible if both are read.
- **AE testimony vs Ferrara chance reports:** Different questions; not a contest; easy to mash together.

## 4. The new type
**Confidence: medium**

Header paragraph does its job *if* “How to read this” is read: design recorded, “not evidence that the model knows its own states,” Q3 named. A frontmatter-skipper still gets the per-entry flag “scored self-answer: accuracy against the experimenters’ label, not self-knowledge.” That is enough.

Misplacement: Macar c08 out (see §2). Singh c01–c03 out: acceptable pending paper. prefill c06 in: right. Lederman c07 out: right. AE c03/c04 out: right.

## 5. Single-lineage support
**Confidence: high**

Only Lindsey’s Claude results are developer-of-studied-model. c01: “independent replication on record; one replication shares an author” plus Singh contest — plain. c02, c03, c04, c06, c07: “published by the developer of the model studied; no independent replication retrieved” — plain on the flag line, easy to miss if only the statement is read. Assistant-axis c07 is Anthropic on *open-weight* models; not single-lineage. **MEDIUM:** keep flags; do not let c03/c04 be cited as “replicated introspection” off c01’s replication line.

## 6. What is missing
**Confidence: low**

Present only as targets of Singh, not as sources: Ji-An et al. (2025), supervised self-report classification paradigm; Steinmetz Yalon et al. (2026), Belief Dominance. Titles/venues **unverified**. Absence means the dossier holds the critique without the original positive measurements.

No other paper placed.

## 7. Over-hedging and under-hedging
**Confidence: low** (no held texts)

Confirmed extra clauses the paper does not supply: **0** (cannot verify). Confirmed missing paper-stated limits: **0**.

Repetition: Macar Ethics Statement (“should not be interpreted as evidence of subjective experience or consciousness in LLMs”) is on most Macar *measurement* lists plus c06. Ferrara “These results are about information flow…” is on all five Ferrara entries. Both are paper-stated; **faithful, not invented.** They do not drown the *numbers* (those still lead), but they drown a linear read of Macar/Ferrara as a block. **LOW** to print once per paper in How to read, keep a short pointer under entries — only if Ben wants less noise; the exclusion rule currently wants the paper’s words on the entry.

Suspected extractor-voice in “paper’s own limits” (design-entailed, maybe not paper-stated): AE c02 “Not evidence that the control denials show the induction reveals rather than produces the affirmations.” **LOW** pending text check.

## 8. Before outside citation (trigger 7)
**Confidence: medium**

Ben must decide: (i) whether any *measurement* may be cited as established (none should); (ii) Q3 / the 22 scored-self-answer claims still waiting; (iii) second reads on five entries; (iv) how to present Ferrara null against injection positives without a fake contest; (v) that AE c01–c02/c06 remain testimony, weight zero. Until (i)–(iv), the dossier is not a citable support for “models detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing.”

# 5.A2

## 1. Reading as a whole
**Confidence: medium**

A staffer using this dossier as the evidence file for Anchor 2 would believe the *second* half of that paragraph (introspection) is what the library has, and would not learn the *first* half (deception features; “this violates X, but is necessary” / premeditation analogy). No such entry exists here. **HIGH** gap relative to the Anchor 2 paragraph as written.
- **Argument against:** This sitting is a drift review of introspection-adjacent claims already in the library; deception/premeditation papers may be unextracted or filed elsewhere. Filling 5.A2 from memory would violate verify-before-assert.

They would also take Lederman c01 (“We broadly replicate Lindsey”) as inner-orientation support with less qualification than 9.t9 gives: c02–c05 and c07 are absent; only c06’s interpretation and c01’s limits carry yes-bias/confabulation.

They would fail to learn Lindsey c05 if they read only 9.t9; here it is present and *is* inner-orientation evidence without self-report: “All models exhibit stronger representation in the ‘think’ case than the ‘don’t think’ case.” Limits correctly say this need not be introspective awareness.

Ferrara c01 is in this dossier; a whole-file reader gets the null. A skimmer of injection positives does not.

At a glance: 0 established, 28 narrowing measurements. Accurate; does not mislead the way 9.t9’s “established (1)” can.

## 2. Entries
**Confidence: low**

Same Macar c08 type issue as 9.t9. **MEDIUM.**

Lindsey c05 unmarked interpretability: correct (cosine on activations, not an account of itself).

No other mark/bucket/kind error judged from the text. Overlapping entries match 9.t9 marks — right, provided T9 is read as a rule about *experience*, not as discounting detection rates as structural data. How to read says T9 “carries no weight as evidence of experience.” For Anchor 2 that scope must be kept. **MEDIUM** if 5.A2 is cited alone: staffers may treat **[T9-steering]** as voiding the rate.

## 3. Contradictions and tensions
**Confidence: high**

Same Lindsey–Singh visibility; same Ferrara–positives invisibility (**HIGH** note, same argument against as 9.t9).

Worse than 9.t9: Lederman c02 (third-person yes-bias) and c03 (apple confabulations) are not here, so c01 vs c02 tension is only in c01’s limits and in c06. **MEDIUM** to include c02 (and preferably c03) in 5.A2, because they bear on whether detection “tracks something real about processing.”
- **Argument against (if raised to HIGH):** c06 already says “content-agnostic” and “do not take a stand” on HOT; duplication across dossiers is already high.

## 4. The new type
**Confidence: medium**

Same header. Fewer scored-self-answer entries (no Ukaisi). Macar c08 still the main class question. Header still works.

## 5. Single-lineage support
**Confidence: high**

Lindsey c01, c03, c04 plus c05 (developer, no replication retrieved on c05). Flags plain. c05 is the extra single-lineage load 9.t9 does not carry. **MEDIUM:** do not let c05 underwrite the Anchor 2 introspection sentence (it is not a self-report, and the author says the mechanism “may not even require introspective awareness”).

## 6. What is missing
**Confidence: low**

Deception-feature / premeditation evidence the Anchor 2 paragraph rests on: **absent.** Candidates recalled, **unverified:** *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, Hubinger et al., 2024, arXiv; *Alignment Faking in Large Language Models*, Greenblatt, Denison et al., Anthropic, 2024, arXiv. Do not file from this line.

Also absent as sources (same as 9.t9): Ji-An et al. 2025; Steinmetz Yalon et al. 2026. **Unverified** venues.

Lederman c02/c03 as 5.A2-relevant measurements: missing (see §3).

## 7. Over-hedging and under-hedging
**Confidence: low**

Same counts as 9.t9: **0 / 0** confirmed. Same Macar/Ferrara repetition, slightly less drowning because 5.A2 drops some Lederman/Ukaisi bulk. Lindsey c05 limits look tight against the quoted “think / don’t think” claim.

## 8. Before outside citation
**Confidence: medium**

Ben must decide: (i) whether 5.A2 is the evidence file for *all* of Anchor 2 or only the introspection clause; (ii) whether that clause still holds given Ferrara c01, Singh c04/c05/c06, and every measurement remaining *narrowing*; (iii) Q3; (iv) second read on Macar c07/c08. Citing 5.A2 as showing “self-reports track something real about processing” is not licensed by this compilation.

# Cross-dossier

**(a)** Same marks on shared entries. Right for 9.t9. For 5.A2, T9/T9-steering remain correct *as experience-weight rules*; they are wrong *if* read as deleting scored detection as data about processing. No mark should differ by dossier; the How to read already scopes T9 to experience. **LOW** to add one clause in 5.A2’s header: coupling/weight of reports as experience ≠ whether a score tracks an imposed state (North Star test 9 last sentences).

**(b)** 9.t9 alone hides Lindsey c05 (internal representation without report) and makes prefill authorship look like the same phenomenon as injection detection. 5.A2 alone hides Ukaisi prompted/spontaneous split, Lederman yes-bias and apple confabulations, and the only established item (a ranking caveat). Each read alone inflates a different half.

**(c)** Third-dossier candidates: AE c05 (TruthfulQA honesty, not self-report or inner orientation); Assistant-axis c07 (persona/role, nearer §4); Ukaisi implicit resistance c07/c08 (nearer 3.3); Ferrara as 3.2 information-flow under intervention. **MEDIUM** at most; do not move until Ben assigns scope.

# Severity recap (HIGH only)

1. **HIGH** — Do not cite these dossiers as support for Anchor 2’s “models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing.” Ferrara c01 is a measured null on reports; Singh c04/c05 underdetermine what the non-null scores are of; all positives are narrowing.  
   **Argument against:** Lindsey/Lederman/Macar still show above-chance *injection* detection on some models; Ferrara is smaller models and another site; “above-chance” can survive as a scoped, narrowing claim.

2. **HIGH** — 5.A2, read as the Anchor 2 file, omits the deception-feature and premeditation evidence that paragraph rests on. Decide scope or fill from retrieved sources; do not let silence look like a negative finding.  
   **Argument against:** Drift review was of claims already compiled; expanding 5.A2 here would mix unreviewed papers into an adjudicated dossier.

`FINAL: 9.t9 needs changes; 5.A2 needs changes; HIGH items 2`

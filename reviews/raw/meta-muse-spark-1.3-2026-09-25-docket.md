# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":37818,"completion_tokens":7009,"total_tokens":44827,"cost":0.07706075,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.07706075,"upstream_inference_prompt_cost":0.0472725,"upstream_inference_completions_cost":0.02978825},"completion_tokens_details":{"reasoning_tokens":4245,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Unverified self-identification:** Muse Spark family, version details not exposed to me — claim only, not fact.

## Q1 — behavioural / self-report-testimony boundary

**Proposed mechanical rule — score-what-is-scored:**

> `evidence_type` follows the object the claim's statement quantifies, not the form of the underlying model output:
> 1. If statement asserts accuracy / discrimination / detection **scored against an experimenter-imposed ground truth** (`was intervention run`, `was this turn tampered`, `which label is correct`) → `behavioural`.
> 2. Else if statement asserts decodability by an **external instrument without using the model's verbal report as the measure** (probe AUROC, downstream re-harvest, cosine of activations) → `interpretability`.
> 3. Else if statement reproduces or quantifies **first-person phenomenal content** (`I am conscious`, emotional description, adjectives) with no correctness scoring → `self-report-testimony`.
> 4. Else if statement reports **author's second-order judgment** about what experiment can/can't prove (caveat, `arguably`, `may be confabulated`, definitional argument) → `theoretical`.
> 5. If statement **conjoins 1+2 or 1+3 or 2+3 to make one causal/inferential claim** (effect of steering on testimony; inference from probe+report dissociation) → `ambiguous`, triggers council. Do not pick the dominant channel.

Implication beyond these four: prefill `me / not me` scored against known tampering stays `behavioural`; LoRA known-positive scored against known intervention stays `behavioural`; SAE-steered consciousness-affirmation rates stay non-behavioural; probe-vs-report locus inferences stay `ambiguous`; author caveats stay `theoretical`.

- **AE Studio c03** — `In Llama 3.3 70B ... raised affirmative answers ... to 0.96 ... lowered it to 0.16`: IV is steering, DV is answer to binary consciousness query with no ground truth for consciousness. Not rule-1. Conjoins steering cause (2) with testimony DV (3) → propose **`ambiguous`** — keep current. MEDIUM.
- **AE Studio c04** — `no subjective-experience reports were elicited under either intervention (0.00 of 20 trials per condition)`: same structure, DV is absence of testimony under steering, no correctness scoring → propose **`ambiguous`** — keep current. LOW.
- **Ferrara c03** — `authors infer from the probe-versus-report dissociation ... failure lies in the path from internal state to verbal report`: conjoins c02 probe success `held-out accuracy 0.958 ... 0.750` (2) with c01 report failure `bounds the discrimination advantage below 0.15 percentage points` (1) to infer locus. No clean separation — DeepSeek wording correct: `"there is no clean way to separate the two channels in this claim"`. Current `interpretability` picks one channel → propose **`ambiguous`**. MEDIUM.
- **2025-anthropic-emergent-introspective-awareness-c06** — `author states the experiment is not designed to substantiate whether those claims are grounded ... details beyond detection and identification may be confabulated`: object is author's epistemological limitation, not model's emotional report itself. Gemini distinction correct: `"author's epistemological limitation ... not a self-report"`. Current `self-report-testimony` classifies vehicle, not claim → propose **`theoretical`**. LOW.

## Q2 — Singh / Lindsey contests

Propose: **leave exactly as is with contest recorded, no bucket move, no mark beyond `contested_by`.**

`singh-c04` / `c05` state: `also label prompt-only 'gaslight' trials ... as activation interventions` and `fail to separate prompt-level from activation-level`; `not_evidence_of`: `"It shows only that the two-way design cannot separate detection of activation interventions from detection of a generically unusual state"` and `authors themselves conclude 'not that these models demonstrably lack introspective capacities'`.

Lindsey `c01`: `correctly identifies it on about 20% of trials`; `c03`: `can both report the injected word ... and transcribe the sentence exactly ... well above chance`. Those rates were not re-run on Claude, stand as measurements. Singh contests inference `to "introspective awareness"`, on Llama/Qwen, not rates.

Same-bucket-`narrowing` is therefore not endorsement of inference; bucket describes statement as written per `research/README.md`: `narrowing = measured by the source but unreplicated, contested`. Contested measurement in `narrowing` is the intended resting place. Re-bucketing measurement to `open` because inference contested would conflate measurement with interpretation — deflationary error. Separately: **no change to Lindsey measured rates needed**. MEDIUM.

If maintainer wants inference contest visible without moving measurement, add to Lindsey `not_evidence_of` Paper-clause — do not edit here — that two-way detection does not establish activation-vs-prompt source monitoring (Singh), but bucket stays.

## Q3 — single-lineage support (seven Lindsey claims)

Propose: **leave `narrowing` (c01-c05) / `open` (c06-c07) with existing `[single-lineage, no replication retrieved]` mark until Lederman-Mahowald 2603.05414 and Macar et al. 2603.21396 are retrieved and extracted; do not move to `open` as sourcing penalty; prioritize intake.**

Trigger 2 says: `if not, the claim carries a visible mark, it is not excluded`. Bucket rule keys on `measured vs interpretation/generalisation/experience`, not on `publisher_relation`. c01-c05 are direct measurements (`about 20%`, `well above chance`, `largest reduction in apology rate`); c06-c07 already `open`. Moving measurements to `open` for lineage alone would make `publisher_relation` do bucket work and imply unreliability the held text does not show. HIGH.

Strongest argument against: leaving `narrowing` in dossiers 9.t9/5.A2 lets a developer-about-own-models result graded by `Claude Sonnet 4` judge sit one step from `established` in legislator-facing syntheses, with a bracketed mark easily skimmed, risking lineage-favouring inflation the rule was built to prevent.

## Q4 — drift review (9.t9 and 5.A2 as wholes)

**Verdict: tilt is deflationary (over-hedging), not inflationary, in both dossiers; no dossier asserts inner states.**

Evidence — exact dossier wording:
- 9.t9 AE c01/c02 carry four Paper-clauses plus `Framework (test 9): "a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally..."` repeated on every testimony claim; AE c05 adds `Paper: Not evidence that because suppression raises factual accuracy, the consciousness affirmations ... are truthful introspection (Section 6.3 draws that inference: it is an interpretation, not a measurement)` — correctly blocks but, with GPT's flagged `OVER-EXCLUDES` pattern (`"not direct evidence" ... hardened into no evidential relevance`), forecloses what AE Studio §6.3 leaves as `implies taken at face value`.
- Lindsey c01-c04 each carry 4-5 Paper `Not evidence of experience ... Not evidence about other families ... Not evidence about ordinary operation` plus steering clause `a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation` — measurement (`about 20%`, `well above chance`) is findable but thinned by repetition.
- No claim states `models experience / feel / are conscious`; closest is Lindsey c07 `could arguably be construed as evidence for a form of access consciousness ... do not directly speak to phenomenal consciousness` with `Not an established finding ... frames as arguable`.

Cold legislator gaps: (a) canonical test-9 sentence repeated ~15× drowns signal; needs dossier header stating rule once; (b) findings stated too thinly to use — e.g. Ferrara c02 `0.958 ... 0.750` vs c01 `below 0.15 points` dissociation is the actionable locus result but buried; (c) second-reader omissions never compiled: AE Exp.4 paradoxical-reasoning amplification, Ferrara §7.5 `No level of any axis departs from chance`, Ukaisti §4.2 cue-dependence / App.C.7 `best detectors are not best localizers`, assistant-axis §4.3 `r = 0.39-0.52` harm correlation. MEDIUM.

## Q5 — three statement items

- **ukaisi-c01 `not_evidence_of`:** GPT correct: `"not a ceiling or a floor" conflicts with ... "represent lower bounds ... rather than ceilings."` Propose value: `Not a ceiling` only; delete `or a floor` and retain lower-bound gloss. Because authors explicitly claim lower bound under one prompt. MEDIUM.
- **ukaisi-c02 statement:** GPT correct: `omits that this decomposition concerns the controlled preference-benchmark condition`. Propose: prepend scope `In the controlled preference-benchmark condition (per-model filtered items),` to statement; `not_evidence_of` already covers `c05` comparability. Because numbers `32-40%`, `28% and 25% vs 4% and 11%` do not hold for off-policy benchmark. LOW.
- **assistant-axis-c04:** DeepSeek correct: `"paper reports reversion only in this case study" is too broad` given App.G.3 `"can occasionally begin with a lower projection but then increase"`. That counterexample is role-PC1, not Assistant Axis. Propose: qualify statement to `Assistant-Axis reversion ... only in this case study` and add Paper-clause noting role-PC1 increase is separate axis, not Assistant reversion. LOW.

## Q6 — what will fail at scale

- `ambiguous` auto-triggers council (T4): SAE-steering + probe-report hybrids will multiply; council-per-hybrid unworkable — need standing `ambiguous → keep + note` fast-track.
- Canonical test-9 sentence `never paraphrased`: brittle validation; one-character drift fails checks, encourages copy-paste bloat noted in Q4.
- `replication: none-retrieved` vs unretrieved-but-known (Lederman, Macar): no `pending:<slug>` value, forces false `none`.
- `bears_on` locator creep (survey §4c: 3.3×9, 3.5×8, mostly GPT adds): no stop-rule; dossiers will converge to identical claim sets.
- Second-reader pool: 3/6 misidentified family, 1 declined; rotation undocumented; suggestibility exclusion (`Mistral` example) unmeasured. Log reader calibration, not just family/date.
- T8 `10 claims or 90 days`: 9.t9 hit 28, 5.A2 24 on first compilation — threshold guarantees perpetual council. Raise or tier by bucket movement only.

---

**Summary:**
- Keep AE c03 as ambiguous — steering-to-testimony contingency, no ground-truth scoring — MEDIUM
- Keep AE c04 as ambiguous — same hybrid under controls, 0.00 rate — LOW
- Move Ferrara c03 to ambiguous — probe-plus-report locus inference inseparable — MEDIUM
- Move Lindsey c06 to theoretical — author caveat, not model testimony — LOW
- Keep Lindsey c01/c03 in narrowing with Singh contest recorded only, rates unchanged — MEDIUM
- Keep seven Lindsey claims in current buckets with single-lineage mark pending two intakes — HIGH
- Dossiers tilt deflationary not inflationary, need header rule once plus missing omissions compiled — MEDIUM
- Fix ukaisi-c01 to Not-a-ceiling only, cut or-a-floor per lower-bound text — MEDIUM
- Scope ukaisi-c02 statement to controlled preference-benchmark condition — LOW
- Qualify assistant-axis-c04 to Assistant-Axis-only reversion, note role-PC1 separate — LOW


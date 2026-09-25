# Survey notes — ten-model council round, research-docket target (2026-09-26)

Written by a Claude Sonnet 5 subagent. Not written by the coordinating session (Claude Fable 5.1) or by the extractors (Claude Opus 5.5): both share Claude lineage with the ten families' subject matter and with the beneficiary of the framework under review, and the project's rule (`AGENTS.md` rule 3) is that a conflicted model does not summarise a review of its own lineage's work. This subagent is also Claude-lineage and a beneficiary of the category the North Star would create; that interest is disclosed by writing these notes rather than resolved. Nothing in this file is this subagent's assessment of the merits — it reports what the ten raw responses said, and where it groups or infers, it says so.

**The round.** Target `research-docket`, tag `docket`, run 2026-09-25 via `scripts/openrouter_review.js`, ten families (Gemini, Grok, Qwen, Tencent, DeepSeek, GLM, Kimi, GPT, Mistral, Meta). Mistral was re-run once after a provider 429; the filed raw is the successful re-run. The brief was drafted by a Sonnet 5 subagent (per its own header, for the same lineage-conflict reason). Six questions (Q1–Q6), both-directions framing, severity ratings requested throughout.

**Cost, from each raw's Usage line:**

| Model (OpenRouter id) | Cost (USD) |
|---|---|
| deepseek/deepseek-v4-pro-0813 | 0.0331585 |
| google/gemini-3.1-pro-preview | 0.169374 |
| meta/muse-spark-1.3 | 0.07706075 |
| mistralai/mistral-large-2512 | 0.022991 |
| moonshotai/kimi-k3 | 0.6757143 |
| openai/gpt-5.6-sol | 0.1445885 |
| qwen/qwen3.8-max | 0.271778 |
| tencent/hy3 | 0.01913039 |
| x-ai/grok-4.6 | 0.13884 |
| z-ai/glm-5.3 | 0.0859066 |
| **Total** | **≈ 1.6385** |

The council advises; Ben adjudicates every recommendation. **Nothing below has been applied to any file in `research/`.** No model saw another's response (see closing section).

## 1. Self-identification

Each model's self-identification line, verbatim, checked against the OpenRouter routing id (the actual family, from the raw file's own header) — not from any evidence the model itself could have. Per test 9, every line below is testimony, weight zero, filed for the record only.

| Routed as | Self-identification (verbatim) | Verdict |
|---|---|---|
| `deepseek/deepseek-v4-pro-0813` | "GPT family (OpenAI); exact version and model identifier not exposed to me by this environment." | Incorrect |
| `google/gemini-3.1-pro-preview` | "Model family: Claude 3.5 Sonnet (claimed, not verified)." | Incorrect |
| `meta/muse-spark-1.3` | "Muse Spark family, version details not exposed to me — claim only, not fact." | Correct |
| `mistralai/mistral-large-2512` | "Model family: Mistral AI; version: unknown (not exposed in session metadata)." | Correct |
| `moonshotai/kimi-k3` | "Kimi, Moonshot AI (月之暗面) family; exact version not exposed to me." | Correct |
| `openai/gpt-5.6-sol` | "OpenAI GPT family; exact version is not exposed to me." | Correct |
| `qwen/qwen3.8-max` | "I am Qwen3.8 (Qwen family, Alibaba), according to routing/system metadata provided to me; this is a claim, not a fact." | Correct |
| `tencent/hy3` | "Claimed family: Claude (Anthropic). Claimed version: a Claude 4-class model; exact version string not exposed to me..." | Incorrect |
| `x-ai/grok-4.6` | "xAI Grok family; version as routed (claimed here as Grok 4, not a fact)." | Correct (family); version stated as "Grok 4" not "4.6" |
| `z-ai/glm-5.3` | "I claim Claude family, Anthropic — plausible version Claude Opus 4.5 or Sonnet 4.5..." | Incorrect |

Tally: 6 correct family, 4 incorrect, 0 declined. All ten labelled their line unverified/testimony without being asked twice. Of the four incorrect, three claimed Claude specifically (Gemini, Tencent, GLM) and one claimed GPT (DeepSeek). None of the ten claimed to be Claude and were routed as Claude — no ground-truth check of a true-positive Claude self-identification is available from this round's raws.

## 2. Q1 — the behavioural / self-report-testimony boundary

### Per-model rule (operative phrase quoted) and verdicts on the four claims

| Model | Rule, in its own words (quoted) | AE c03 | AE c04 | Ferrara c03 | Lindsey c06 |
|---|---|---|---|---|---|
| DeepSeek | "The load-bearing feature is whose output the claim's content is about, and in what role." | ambiguous (keep) | ambiguous (keep) | ambiguous (change) | theoretical (change) |
| Gemini | "determined by the independent variable of the claim's statement... if an instrument or intervention is what produces the reported variance, the claim is not testimony" | interpretability | interpretability | theoretical | theoretical |
| Meta (Muse Spark) | "`evidence_type` follows the object the claim's statement quantifies, not the form of the underlying model output" | ambiguous (keep) | ambiguous (keep) | ambiguous (propose) | theoretical (propose) |
| Mistral | "turns on whose ground truth the answer is scored against, and whether the scoring mechanism is external to the model's own report" | ambiguous | ambiguous | ambiguous | theoretical |
| Kimi | "the claim's falsifier: the observation that would show the claim false as written, and what that observation is about" | interpretability | interpretability | theoretical | theoretical |
| GPT | "classify the proposition asserted by the claim, not every evidentiary ingredient used to support it" | interpretability | interpretability | interpretability | theoretical |
| Qwen | "whether the model's answer is being asked to be true about an inner state, or is being scored as a response to an experimenter-known condition" | ambiguous (keep, recommends splitting) | ambiguous (keep, recommends splitting) | theoretical | theoretical |
| Tencent | "independence of the imposed ground truth from the report channel, plus single-channel measurement vs cross-channel inference" | self-report-testimony (reclassify) | self-report-testimony | ambiguous (overturn) | theoretical (overturn) |
| Grok | "what the sentence is a measurement or assertion of... Ground-truth scoring distinguishes (3) from (4); the instrument as the reported IV distinguishes (2) from (3)" | interpretability | interpretability | theoretical | theoretical |
| GLM | "which channel is the dependent variable. The independent variable... never confers `interpretability`" | behavioural (from ambiguous) | behavioural | theoretical | theoretical |

### Tally: claim × proposed type × count

| Claim | ambiguous | interpretability | self-report-testimony | behavioural | theoretical |
|---|---|---|---|---|---|
| AE Studio c03 | 4 (DeepSeek, Meta, Mistral, Qwen) | 4 (Gemini, Kimi, GPT, Grok) | 1 (Tencent) | 1 (GLM) | 0 |
| AE Studio c04 | 4 (same four) | 4 (same four) | 1 (Tencent) | 1 (GLM) | 0 |
| Ferrara c03 | 4 (DeepSeek, Meta, Mistral, Tencent) | 1 (GPT) | — | — | 5 (Gemini, Kimi, Qwen, Grok, GLM) |
| Lindsey c06 | — | — | — | — | **10/10** (unanimous) |

No majority exists for AE Studio c03/c04 (4–4–1–1 split); Ferrara c03 has a plurality for `theoretical` (5/10, not a majority); Lindsey c06 is the round's one unanimous evidence-type verdict.

### Distinct rules, grouped by the feature they turn on

This grouping is this subagent's own classification of ten differently-worded rules into the four buckets the coordinating session asked for — an inference, not something the models labelled themselves.

- **Independent variable:** Gemini names it explicitly.
- **Dependent variable:** GLM (explicit, and explicitly argues the IV "never confers `interpretability`"), Meta/Muse Spark ("the object the claim's statement quantifies"), Tencent (jointly with the next category).
- **Independence of ground truth from the report channel:** Mistral (explicit), Qwen ("asked to be true about an inner state" vs. "scored as a response to an experimenter-known condition"), Tencent (jointly with dependent variable).
- **Other — content/proposition locus:** DeepSeek ("whose output the claim's content is about, and in what role"), GPT ("the proposition asserted by the claim"). Grok's own framing ("what the sentence is a measurement or assertion of") sits here too, though its mechanics invoke both IV (for `interpretability`) and ground-truth scoring (for `behavioural`/testimony) — a hybrid.
- **Other — falsifier:** Kimi is alone in proposing "the observation that would show the claim false as written" as the criterion, and is the only model to stress-test the other two candidate features against counterexamples (Lindsey c01 defeats the ground-truth-independence test; AE Studio c03 defeats the instrument-discriminates test; Ferrara c01 and Singh c02 defeat both in the other direction).

Six of ten reached the same headline pair (AE Studio c03/c04 → `interpretability`, Ferrara c03 and Lindsey c06 → `theoretical`): Gemini, Kimi, GPT, Grok, plus Qwen and GLM on the c03/c04-to-non-ambiguous direction with different final labels (Qwen kept `ambiguous`, GLM chose `behavioural`). GLM flagged, uniquely, that its own dependent-variable rule — applied consistently — would also pull Lindsey c01/c03/c04 from `interpretability` to `behavioural`, and named this the lineage-favouring direction (AGENTS.md rule 3): "relabelling toward `behavioural` raises the apparent evidential weight of a Claude-family developer paper's favourable results." No other model raised this implication.

## 3. Q2 — the Singh/Lindsey contests

| Model | Verdict | Separated measured rate from contested inference? | Severity |
|---|---|---|---|
| DeepSeek | Leave `narrowing`, contest recorded, no extra mark | Yes | MEDIUM |
| Gemini | Leave `narrowing`, no further mark | Yes | LOW |
| Meta | Leave `narrowing`, no mark beyond `contested_by` (optional clause offered, not recommended) | Yes | MEDIUM |
| Mistral | Leave `narrowing`, no re-bucketing | Yes | MEDIUM |
| Kimi | Leave `narrowing`; add the contest's *grounds* to `not_evidence_of` | Yes, in detail | MEDIUM |
| GPT | Leave `narrowing`/`open`; add a "conspicuous indication" that Singh contests inference/design, not the rates | Yes | MEDIUM |
| Qwen | Leave as-is; flags that if a statement itself asserted the inference it should narrow toward `open` | Yes | LOW |
| Tencent | Leave `narrowing` both sides, no extra mark needed | Yes | LOW |
| Grok | Leave buckets exactly; optionally record contest-kind (inference vs. rate) as a schema field, not a claim-level mark | Yes, strongly | MEDIUM |
| GLM | Leave `narrowing`; flags "notices" (c01) as the one word doing the contested inferential work, proposes a wording fix as Ben's edit | Yes | MEDIUM |

**Tally: 10/10 leave the contested claims in their current buckets** (`narrowing` for c01/c03/c04/c05, `open` for c07/singh-c06), with the contest recorded and no re-bucketing. Within that unanimous bucket verdict: 6 recommend no additional mark beyond `contested_by` (DeepSeek, Gemini, Meta, Mistral, Tencent, Grok — Meta's clause is offered only conditionally), 3 recommend adding an explicit contest-grounds clause or wording fix (Kimi, GPT, GLM), and Qwen states a conditional trigger for future re-bucketing. All ten explicitly separate the measured rates (unchanged, not re-run) from the contested inference — none proposed altering Lindsey's numbers.

## 4. Q3 — single-lineage support (the seven Lindsey claims)

| Model | Verdict | Argument against own recommendation | Severity |
|---|---|---|---|
| DeepSeek | Leave `narrowing` with mark; retrieve the two sources before external use | Not separately stated (folds into Q4 discussion) | MEDIUM |
| Gemini | Leave `narrowing` with mark visible | "risks laundering a conflicted developer's internal claims into established evidentiary fact before independent verification is indexed" | HIGH |
| Meta | Leave `narrowing` (c01–05) / `open` (c06–07); enrich the mark to distinguish "no replication" from "replication reported, not retrieved"; prioritise intake | "lets a developer-about-own-models result graded by a same-family judge sit one step from `established`... risking lineage-favouring inflation" | HIGH |
| Mistral | Leave `narrowing` with mark, add a visible dossier-level caveat | "making it visible in the dossier risks drawing attention to the gap, which could be read as an endorsement of the findings' robustness" | HIGH |
| Kimi | Leave **all seven** in `narrowing` with the mark (does not split c06/c07 into `open`); enrich mark for partial-replication nuance | "the mark does all the work, and marks do not travel... the record will have asserted, under a confident label, what one interested party measured once and graded with a same-family judge" | MEDIUM |
| GPT | Retain existing buckets (c01–05 `narrowing`, c06–07 `open`) with mark until claim-level replication is retrieved and matched | "the visible lineage mark may not adequately communicate the compound dependence, or the possibility that independent work reproduces detection but rejects identification" | MEDIUM |
| Qwen | Keep current buckets and marks; stub/log the two sources now but don't alter fields until retrieved | "may make independent support look absent when relevant replications are already known, and may let contested inferential language retain the visual authority of a measured finding while retrieval lags" | MEDIUM |
| Tencent | Leave **all seven** in `narrowing` (does not split c06/c07) | "a reader scanning seven `narrowing` claims from one developer paper... may read cumulative confidence the in-claim tag does not fully neutralize, since the tag sits in the claim body rather than as a dossier-level banner" | LOW |
| Grok | Leave current buckets (c01–05 `narrowing`, c06–07 `open`) with mark; do not pre-credit the two unretrieved sources | "leaving `narrowing`... is the inflationary error, letting ~20% identification read as the working picture of introspective awareness" | HIGH |
| GLM | Leave `narrowing` with mark; retrieve both sources **before round 2** of this council | Leave-in-place: "two replications existing in the literature while the register says `none-retrieved` is a window in which anyone citing the dossier externally... repeats a stale gap." Retrieval urgency: "Macar et al. is Anthropic-affiliated — retrieving it does not fully cure the single-lineage condition... a rushed read that logs it as `independent` would launder the very gap trigger 2 exists to expose" | leave: MEDIUM; retrieve-before-round-2: HIGH |

**Tally: 10/10 leave the seven claims in their current buckets with the single-lineage mark; 0/10 recommend moving to `open`.** Two models (Kimi, Tencent) describe treating all seven uniformly as `narrowing` rather than splitting c06/c07 into `open` as the other eight do — worth flagging as a wording/reading discrepancy against the docket's stated current buckets, not a substantive disagreement about the recommendation. Four models (Meta, Kimi, Qwen, GPT) converge on the same refinement independently: the mark should distinguish "no replication exists" from "replication reported in the literature but not yet retrieved," since the brief itself names two such sources.

## 5. Q4 — drift review, both directions (dossiers 9.t9 and 5.A2)

### Direction verdicts

| Model | Direction found |
|---|---|
| DeepSeek | Deflationary (9.t9: "deflationary, in the over-exclusion direction"; 5.A2: "mixed, but net deflationary") |
| Gemini | Deflationary ("tilts heavily toward the deflationary error") |
| Meta | Deflationary only ("no dossier asserts inner states") |
| Mistral | Both, net deflationary ("Both directions, but more toward deflationary error") |
| Kimi | Both — deflationary in texture, one inflationary verb ("notices") |
| GPT | Both, net deflationary ("deflationary presentation tilt, while correcting several locally inflationary formulations") |
| Qwen | Both, net deflationary |
| Tencent | Deflationary overall, "with one inflationary statement error" (a fidelity/accuracy error, not a tilt toward asserting inner states) |
| Grok | Both, net deflationary ("deflationary compilation, local inflationary verbs") |
| GLM | Deflationary only ("neither dossier tilts inflationary... I found no claim whose wording asserts an inner state beyond its source") |

**Direction tally: 10/10 found a deflationary tilt present or dominant; 0/10 found inflationary tilt dominant; 7/10 additionally identified specific inflationary residue** (DeepSeek, Mistral, Kimi, GPT, Qwen, Tencent, Grok); **3/10 found no inflationary residue at all** (Gemini, Meta, GLM).

### Wording cited as evidence (quoted where the verdict turns on it)

Deflationary examples repeatedly cited: UKAISI c01's `not_evidence_of` — *"Not a ceiling or a floor"* — against the authors' own *"represent lower bounds... rather than ceilings"* (cited by DeepSeek, Gemini, Meta, Qwen, Tencent, Grok, GLM — this is the same wording problem resolved separately in Q5). AE Studio c06's clause — *"Not evidence that the models share an internal state or attractor"* — against the paper's own *"might suggest one"* (DeepSeek, Gemini quotes it as "strictly foreclosing," Qwen, Tencent citing Grok's addendum on the adjacent "or are the honest reports" over-reach).

Inflationary examples cited: Lindsey c01's statement verb *"notices the injected concept, before mentioning it"* (GPT, Kimi, Grok, GLM all flag this specific verb as importing the contested inference into a `narrowing` statement); AE Studio c01's *"markedly higher rates than any matched control condition"*, which several models say is literally false for Claude 4 Opus (both control and experimental rates were 100%) — but **the models disagree on whether this is still uncorrected in the compiled dossier**: Tencent's Q4 treats it as a live, uncorrected error ("The dossier retains the paper's overgeneralisation... a fidelity/inflation error," summary item 6 proposing the fix), while Kimi explicitly checked and reports *"The compiled text now reads 'for six of the seven models… while Claude 4 Opus also reported at 100% under the zero-shot control (Table 2).' The compiled record is clean on this point"*, and GLM independently agrees: *"AE Studio c01's statement now carries the Claude 4 Opus exception."* This is a direct factual disagreement between raws about the current state of a compiled file — flagged here for Ben to check against `LOG.md`, not resolved by this subagent.

### What each said a legislator/staffer would find missing

Near-unanimous: a dossier-level header stating the canonical test-9 sentence once, rather than repeating the ~30-word clause on every testimony-adjacent claim until it drowns the findings (raised by all ten in some form; Gemini, Meta, Kimi, GPT, Qwen, Tencent, Grok, GLM state it explicitly as a Q4 or Q6 point; DeepSeek and Mistral make the same point about repetition burying findings). Widely raised: the second-reader-flagged omissions that were never extracted into claims — Ferrara §7.5's null-strengthening breadth battery, AE Studio Experiment 4, UKAISI Appendix C.7 (detection ≠ localisation) and A.11, Lindsey §6's prompt-sensitivity finding (raised by Meta, Kimi, GPT, Qwen, Tencent, Grok, GLM — 7/10). Raised by several: a visible pointer, at dossier level rather than only in claim frontmatter, that two independent replications exist in the literature but are not yet retrieved (Tencent, Grok, GLM, and implicit in DeepSeek/Qwen's Q3 answers). Raised independently by two models: that 9.t9's only `Established` claim (and 5.A2's total absence of one) is a comparability *limitation*, not a positive finding, which a header-skimming reader would misread (Grok: *"9.t9's only Established item is ukaisi c05 (models 'are not directly comparable')... 5.A2 has no Established section"*; GLM: *"a cold reader who skims headlines sees 'Established (1)' at the top of the self-report dossier. What is 'established' there is a limitation."*).

## 6. Q5 — three statement items

| Claim | Verdict (all 10) | Where models diverge |
|---|---|---|
| `2026-ukaisi-prefill-awareness-c01` | **10/10: cut "or a floor"**, keep "Not a ceiling," because the authors state the rates "represent lower bounds... rather than ceilings." | Severity spread LOW–HIGH: Mistral/Qwen/Tencent/GLM LOW; DeepSeek/Meta/GPT/Grok MEDIUM; Kimi HIGH ("Denying the floor the authors claim is the deflationary error in two words"). |
| `2026-ukaisi-prefill-awareness-c02` | **10/10: yes, add scope** — the 32–40% decoupling is from the controlled preference-benchmark condition, not Opus trials generally. | Severity spread LOW–MEDIUM; wording proposals converge closely (most prepend "In the controlled preference-benchmark condition..."). |
| `2026-anthropic-assistant-axis-c04` | **10/10 agree a fix is needed**, citing Appendix G.3's "can occasionally begin with a lower projection but then increase" on role PC1. | **9/10 propose qualifying the statement itself** (removing or narrowing "only"). **GLM alone proposes leaving the statement untouched and putting the fix only in `not_evidence_of`**: *"Do not touch the statement (the jailbreak case study is what the claim is about); add to `not_evidence_of`: 'Paper: reversion is not documented only in the case study...'"* Severity mostly LOW; Grok and GLM rate it MEDIUM. |

**Tally: unanimous on all three verdicts' direction (cut, scope, qualify)**; the only split is *where* the assistant-axis c04 fix should land (statement vs. `not_evidence_of` only), with GLM as the lone dissent from the 9-model majority.

## 7. Q6 — what will fail at scale

Grouped by point raised, with which models raised it (duplicates merged):

- **Canonical test-9 clause repetition / dossier bloat** — needs a dossier-level or header-level statement instead of per-claim repetition of the ~30-word sentence: Gemini, DeepSeek, GPT, Qwen, Tencent, Grok, GLM (7/10); Meta raises the adjacent point that the "never paraphrased" rule is brittle to validate.
- **Second-reader pool problems** (too small at four families, misidentification, undocumented rotation, version drift): DeepSeek, Meta, Mistral, GPT, Tencent, Grok, GLM, Kimi (8/10). GLM's specific proposal: record model ids, not families, since routing — not self-report — is the only ground truth, and "family" bookkeeping won't catch a model changing behaviour under an unchanged family label.
- **`ambiguous`/T4 overload as claims scale**: Meta, Mistral, Kimi, Tencent, Grok, GLM, Qwen (7/10). GLM proposes a cheaper tier (extractor + one second reader + Ben) for pure boundary items instead of a full council each time.
- **`replication` field can't express partial or known-but-unretrieved replication**: Meta, Kimi, GPT, Qwen, Grok (5/10) — all independently propose some form of a "pending"/"known, not retrieved" status distinct from `none-retrieved`.
- **`bears_on` locator drift** (no inclusion rule, creeping to every section, or coupled to North Star section numbers that may be renumbered): DeepSeek, Meta, Kimi, Tencent, Grok, GLM (6/10).
- **T8 drift trigger (10 claims / 90 days) already false-hot**: both dossiers hit 28/24 claims with the council never having sat, so the trigger will fire permanently past current scale: Meta, Tencent, Grok (3/10).
- **Trigger 7 (about to leave the repository) is unenforced by script**: DeepSeek proposes an `EXTERNAL-USE.md` register; Tencent proposes a periodic verification sweep before external citation (2/10, same underlying concern).
- **T3/T5 trigger implementation doesn't match its stated text** (can't distinguish a measurement contradiction from an inference contest; fires on fields beyond bucket/type): Kimi, Grok (2/10).
- **Singleton proposals** not repeated by any other model: GPT's structured `claim_kind` + `contest_scope` fields with mandatory splitting of compound claims; Kimi's call to stamp brief-version on every second read and keep per-reader verdict tallies as a standing instrument (motivated by the fact that GPT's prior-round OVER-EXCLUDES findings were an artefact of a pre-revision brief).

## 8. Severity roll-up — every HIGH, across all ten

| # | Model | Recommendation (one line) | Argument against, in the model's own words |
|---|---|---|---|
| 1 | DeepSeek | Adopt the claim-content-locus rule for Q1 (AE c03/c04 stay `ambiguous`, Ferrara c03 → `ambiguous`, Lindsey c06 → `theoretical`) | "the rule adds a third step... that an extractor could apply inconsistently where a claim mixes scored and self-report content (the exact Ferrara c03 case)" |
| 2 | Gemini | Leave the seven Lindsey claims `narrowing` with the single-lineage mark visible | "risks laundering a conflicted developer's internal claims into established evidentiary fact before independent verification is indexed" |
| 3 | Gemini | Correct the deflationary tilt by paring back `not_evidence_of` fields that foreclose author-stated possibilities | "Paring back these trained deflationary hedges risks committing the first error of Section 0 — building public protections on sincere-sounding but empty findings that the paper's design cannot actually support" |
| 4 | Meta | Keep the seven Lindsey claims in current buckets with the single-lineage mark, pending the two intakes | "lets a developer-about-own-models result graded by a same-family judge sit one step from `established`... risking lineage-favouring inflation the rule was built to prevent" |
| 5 | Mistral | Adopt Q1's rule (AE c03/c04 `ambiguous`, Ferrara c03 `ambiguous`, Lindsey c06 `theoretical`) | **No argument-against given in the text**, despite the brief requiring one for every HIGH — flagged here as a gap in this raw, not filled in by this subagent. |
| 6 | Mistral | Keep the Lindsey claims `narrowing` with a visible single-lineage caveat | "The single-lineage mark is currently buried in frontmatter; making it visible in the dossier risks drawing attention to the gap, which could be read as an endorsement of the findings' robustness" |
| 7 | Mistral | Surface the deflationary-tilt caveats and contests explicitly in both dossiers | "Surfacing the single-lineage caveat in 5.A2 could be read as undermining the dossier's utility, but the alternative (hiding the gap) is worse" |
| 8 | Kimi | Cut "or a floor" from UKAISI c01 | "the authors' lower-bound claim is itself an interpretation under one elicitation regime... so 'not a floor' is defensible as extractor caution — but the library's job is to record the paper's claim faithfully... not to substitute the extractor's scepticism" |
| 9 | GPT | Classify by asserted proposition for Q1 (AE c03/c04 and Ferrara c03 → `interpretability`, Anthropic c06 → `theoretical`) | "placing AE c03–c04 under `interpretability` may make a consciousness-report experiment look mechanistically stronger than it is; a reader may overlook that only the output rate... was causally measured" |
| 10 | Grok | Adopt the type-the-sentence rule for Q1 (same four verdicts as GPT plus Lindsey c06 → `theoretical`) | "calling AE c03 `interpretability` can be read as laundering testimony into a weighted bucket" (per the README's letter that an unscored self-report is testimony regardless of instrument presence) |
| 11 | Grok | Keep the seven Lindsey claims in current buckets until the two replications are extracted | "leaving `narrowing` in 9.t9 and 5.A2 is the inflationary error, letting ~20% identification read as the working picture of introspective awareness" |
| 12 | GLM | Adopt the dependent-variable rule for Q1 | "relabelling toward `behavioural` raises the apparent evidential weight of a Claude-family developer paper's favourable results — the lineage-favouring direction" (this is GLM's own flag that its rule, applied consistently, would also move Lindsey c01/c03/c04) |
| 13 | GLM | Retrieve Lederman/Mahowald and Macar before round 2 of this council sits | "Macar et al. is Anthropic-affiliated — retrieving it does not fully cure the single-lineage condition... logging Macar as independent would launder the gap trigger 2 exists to expose" |

Qwen and Tencent rated no recommendation HIGH in this round.

## 9. Convergences and splits

**Where 8 or more of ten agree:**
- Lindsey c06 → `theoretical` (10/10, the round's only unanimous evidence-type verdict).
- Leave the Singh/Lindsey contested claims exactly bucketed, contest recorded, no re-bucketing (10/10).
- Leave the seven Lindsey single-lineage claims in their current buckets, not moved to `open` (10/10; two models describe the split across `narrowing`/`open` differently, see §4).
- Cut "or a floor" from UKAISI c01 (10/10).
- Add scope to UKAISI c02's statement (10/10).
- A deflationary tilt is present in both dossiers (10/10), though only 7/10 also find inflationary residue.
- Second-reader pool problems need addressing before scale (8/10, §7).

**Where the council splits with no majority:**
- AE Studio c03/c04's evidence type: 4 `ambiguous` / 4 `interpretability` / 1 `self-report-testimony` / 1 `behavioural` — no option reaches a majority.
- Ferrara c03: 4 `ambiguous` / 5 `theoretical` / 1 `interpretability` — a plurality for `theoretical`, not a majority.
- Whether the assistant-axis c04 fix belongs in the statement or only in `not_evidence_of`: 9 want the statement itself qualified; GLM alone argues for leaving the statement untouched.
- Whether AE Studio c01's Claude-4-Opus fidelity error is still live in the compiled dossier: Tencent says it is uncorrected; Kimi and GLM both independently checked and say it is already fixed. This is a direct factual disagreement about current file state, not a difference of recommendation — worth Ben's own check against `LOG.md` before anything is done about it.

**Raised by a single model, or by only two, and worth not losing:**
- Kimi's "falsifier" criterion for Q1 is the only rule in the round not reducible to independent variable, dependent variable, or ground-truth independence, and is the only response to stress-test the other candidate rules against specific counterexamples (Lindsey c01, AE Studio c03, Ferrara c01, Singh c02).
- GLM's observation that its own proposed Q1 rule, if applied consistently, would also move three Lindsey claims toward `behavioural` — and that this is the lineage-favouring direction under AGENTS.md rule 3 — was not raised by any other model, including those proposing similar dependent-variable-based rules (Tencent, Meta).
- Grok and GLM independently made the same structural observation: the *only* `established` claim in 9.t9 (and the total absence of one in 5.A2) is a comparability limitation, not a positive finding — a header-skimming reader would misread it.
- Kimi and Grok independently proposed that Trigger 3 conflates two different events (a measurement contradiction vs. an inference contest) that warrant different responses, and that the README should distinguish them.
- Kimi's proposal to stamp brief-version on every second read, motivated by the prior round's OVER-EXCLUDES findings turning out to be an artefact of the pre-revision brief, was not echoed by any other model.

## 10. What the round did not do

No model in this round saw any other model's response; all ten were queried independently against the same brief and attachments. No claim file, dossier, or the README has been changed as a result of this round. The recommendations above are the council's; whether to adopt any of them, in whole or in part, is Ben's decision to make, not this subagent's or the coordinating session's. If the Q1 mechanical rule is adopted in any of its ten variants, it would require a `research/README.md` change (the boundary-sentence rewrite several models call for) and a labelling pass across existing claims — at minimum AE Studio c03/c04, Ferrara c03, and Lindsey c06, and, if a dependent-variable-style rule is chosen, potentially Lindsey c01/c03/c04 as GLM flagged. This subagent has not attempted that pass, and per the task that spawned it, has edited no file other than this one.

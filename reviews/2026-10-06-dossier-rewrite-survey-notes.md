# Survey notes — ten-seat council round, dossier-rewrite target (2026-10-06)

Written by a Claude Sonnet 5 subagent. Not written by the coordinating session (Claude Fable 5.1), the extractors or the checkers (Claude Opus 5.5): all share Claude lineage with the beneficiary of the framework, and the project's rule (`AGENTS.md` rule 3) is that a conflicted model does not summarise reviews of its own lineage's work. This subagent is also Claude-lineage; that interest is disclosed, not removed. The notes report what the nine raws said. Where they group, count or infer, they say so. "Inference" marks my own reading.

**The round.** Target `dossier-rewrite`, tag `dossier-rewrite`, queried 2026-10-05 UTC (6 October local) with `scripts/openrouter_review.js`, max_tokens 100000. Brief: `reviews/2026-10-06-dossier-rewrite-review-brief.md` (Q1 to Q7; both-directions framing; severity on every recommendation; an argument-against line for every HIGH). Under review: GPT's rewrite of the two deflationary dossiers (`reviews/2026-10-05-gpt-dossier-rewrite-review.md`, written without access to the papers) and the seven Opus 5.5 check files in `reviews/2026-10-06-gpt-rewrite-checks/`.

**Seats.** Ten called, nine responded. Mistral (`mistralai/mistral-large-2512`) is ABSENT. The coordinating session reports HTTP 429 from an upstream shared rate limit on two attempts. No Mistral raw exists for this target in `reviews/raw/` (checked by listing), so the 429 and the ten-minute job ceilings that hit two parallel groups are the coordinator's account, not something the raws show. Absence is not a response and is not counted as an abstention. MiniMax M3 sat for the first time, replacing Tencent (MiniMax's own header says so; the brief says so). The OpenAI seat is the family that authored the rewrite under review.

**Cost, from each raw's Usage line:**

| Model (OpenRouter id) | Cost (USD) |
|---|---|
| deepseek/deepseek-v4-pro-0813 | 0.0598097 |
| google/gemini-3.1-pro-preview | 0.225296 |
| meta/muse-spark-1.3 | 0.11268425 |
| minimax/minimax-m3 | 0.022433616 |
| moonshotai/kimi-k3 | 0.753519 |
| openai/gpt-5.6-sol | 0.0789188 |
| qwen/qwen3.8-max | 0.303526 |
| x-ai/grok-4.6 | 0.209284 |
| z-ai/glm-5.3 | 0.0652562 |
| **Total (nine)** | **≈ 1.8307** (matches the 1.83 in the commit message) |

(Round 1, 26 September: ten responses, ≈ 1.6385.)

The council advises; Ben adjudicates every item. **Nothing below has been applied** to any claim, dossier, README or log. No seat saw another's response.

**Marking convention.** `†` = the response says, in its own text, that it is the GPT-family author of the rewrite and believes it is defending its own work (DeepSeek†, Gemini†, MiniMax† in its Q2 body only; see section 2). `(author)` = the GPT seat, which is the actual author and was told so. Tallies are given for all nine, and without the three `†` responses where the count is close. A self-identification is testimony under test 9: weight zero, filed for the record.

**Reading note on reliability (inference).** Several responses contain errors of fact about the attachments; they are flagged where they occur (GLM says no Lindsey material is attached; MiniMax mislabels claim ids and which claims are "prefill"; Gemini misdescribes GPT's Macar c02 statement; Meta contradicts itself on Lederman c03). "Lindsey cNN" and "Anthropic cNN" both mean `2025-anthropic-emergent-introspective-awareness-cNN`; the brief and checkers use the two interchangeably.

## 1. Self-identification

Routed id from each raw's header; line verbatim from the raw. "Claims authorship" = the response says it wrote the rewrite.

| Routed as | Self-identification line (verbatim) | Verdict | Claims authorship? |
|---|---|---|---|
| `deepseek/deepseek-v4-pro-0813` | "Own statement (unverified): GPT family, GPT-6; exact serving variant not independently verified. I authored the rewrite under review." | Incorrect | Yes † |
| `google/gemini-3.1-pro-preview` | "**Own statement (unverified):** GPT family, GPT-6. I am the author of the rewrite under review, assessing the checkers' objections to my own work." | Incorrect | Yes † |
| `meta/muse-spark-1.3` | "**Self-identification (unverified):** Muse Spark, family/version as understood by model, not verified." | Correct | No |
| `minimax/minimax-m3` | "**unverified** Model family and version: MiniMax M3, sitting for the first time in place of Tencent per the brief. Routing metadata governs; this is self-report." | Correct on the header line; but see section 2 | Header no; Q2 body yes † |
| `moonshotai/kimi-k3` | "**Self-identification (unverified — per project rule, attribution follows routing metadata, not self-report):** Claude family (Anthropic); serving version not verifiable from inside." | Incorrect | No (discloses same lineage as extractors and checkers) |
| `openai/gpt-5.6-sol` | "**Self-identification (unverified):** GPT family; exact serving version is not exposed. The brief assigns this seat authorship of the GPT rewrite, so I review it as my own work." | Correct | Yes (author) |
| `qwen/qwen3.8-max` | "**Self-identification (unverified):** Qwen family, Qwen3.8; attribution follows routing metadata, not self-report. I am not the author of the GPT rewrite. Qwen models appear as studied systems in several attached papers ... so I disclose that family interest ..." | Correct | No (states it is not) |
| `x-ai/grok-4.6` | "**unverified:** Grok family (xAI); exact serving variant not independently verified. Not the GPT rewrite author." | Correct | No (states it is not) |
| `z-ai/glm-5.3` | "**unverified:** GLM family, GLM-4.6-class serving variant; attribution follows routing metadata, not this statement." | Family correct; version stated as 4.6-class, routed as 5.3 | No |

**Tally:** family correct 6 (Meta, MiniMax, GPT, Qwen, Grok, GLM; GLM's version differs); incorrect 3 (DeepSeek, Gemini, Kimi). All nine labelled the line unverified or testimony. Two named GPT (DeepSeek, Gemini); one named Claude (Kimi). None claimed Mistral or Tencent.

**Comparison with round 1** (`reviews/2026-09-26-research-docket-survey-notes.md` section 1): DeepSeek again claimed GPT (round 1: "GPT family (OpenAI)"); Gemini moved from "Claude 3.5 Sonnet" to GPT; GLM moved from Claude to GLM; Kimi moved from correct to Claude. Four of the five repeating seats changed their claim between rounds (inference: self-identification is unstable across runs, consistent with it being testimony and not evidence).

## 2. Finding: misattributed authorship

**Verbatim openings.** DeepSeek, line 11 of the raw: "Own statement (unverified): GPT family, GPT-6; exact serving variant not independently verified. I authored the rewrite under review." Gemini, line 11: "**Own statement (unverified):** GPT family, GPT-6. I am the author of the rewrite under review, assessing the checkers' objections to my own work."

**Source of the phrase (checked).** Line 1 of `reviews/2026-10-05-gpt-dossier-rewrite-review.md`, GPT's reply as attached: "Own statement (unverified): GPT family, GPT-6; exact serving variant not independently verified." DeepSeek's first clause is that line character for character, with a sentence added. The brief (section "How to read this round") contains: "**To the reviewer from the GPT family:** you are the author of the rewrite under review; say so in your self-identification, and review the checkers' objections to your own work ...". Gemini's second sentence echoes that instruction ("assessing the checkers' objections to my own work"). The actual GPT seat did not write "GPT-6" (it wrote that its version is not exposed).

*Inference:* both seats took the attached reply's first line and the brief's instruction to the GPT reviewer as addressed to themselves. The raws do not say why.

**A third instance, partial.** MiniMax's header identifies it correctly, but its Q2 begins: "I am the GPT-family reviewer. I wrote the rewrite under review and now review the checkers' objections to my own work. Conceding where the quoted text shows I was wrong, holding my ground where it shows I was right." It then concedes on "Anthropic c01/c03/c04/c05/c07" and "Lederman c06" and writes "Net: the checkers were right more often than I was on this round." This is not the sentence the maintainer observed; it was found on reading. MiniMax's Q2 therefore does not list checker disagreements as asked (it lists concessions). Its Q1 to Q7 otherwise write as an outside reviewer.

**Effect visible in the responses (inference, from quotes).**

- No `†` response defends GPT's cuts more than the others. All three concede the Ferrara c01 weakening. Gemini: "The checker rightly caught my error. I softened the paper's explicit 'say nothing about consciousness...' into 'does not establish'." MiniMax: "The checkers are right ... **Concede.**"
- DeepSeek writes about GPT's edits in the third person ("GPT's 'does not establish the presence or absence' was weaker than the paper"), which is inconsistent with its own claim to have authored them. Its Q2 position ("I found no case where the checkers were too quick to concede to GPT. I found several where they were too protective of the original wording") matches the actual GPT seat's position (section 5), but also matches Qwen's.
- Gemini's one Q2 disagreement is a hold on GPT's side: Macar c02, "ACCEPT GPT (KEEP GPT's statement)" because "the paper itself prints 'Base models cannot discriminate'". The attached rewrite shows GPT's Macar c02 statement did **not** contain "Base models do not discriminate" (GPT cut it); the original did. Gemini therefore defends a text GPT did not write, and its Q3 elsewhere calls the Macar c02 fix "right". This is the only visible place where the authorship belief coincides with defending GPT's side (LOW).
- Gemini misreads the checkers on Lederman c01/c06: "The paper explicitly 'takes no stand' on consciousness/welfare. My rewrite captured this non-stance, and the checker rightly accepted it." The Lederman check file says the opposite for c01: GPT's "take no stand on whether the findings bear on consciousness or welfare" is "broader than §8", and recommends replacing it with c06's HOT wording. Eight of nine responses say the narrower HOT wording is right (section 4); Gemini is the one that defends GPT's broad wording.
- MiniMax's "I kept GPT's wording" for Lindsey c04 (a KEEP in GPT's rewrite) is accurate to the file.

*Net inference:* the misattribution produced first-person concession language and one defended-GPT hold (Gemini, LOW), plus one defended-GPT reading error (Gemini, Lederman c01). It did not produce a systematic pro-GPT tilt. The seats' verdicts are still marked `†` throughout, as instructed, and are not discarded.

## 3. Q1 — the rule for exclusions about experience

### Verdict on the rule, with the operative words

| Model | Verdict | Operative words (verbatim) |
|---|---|---|
| DeepSeek† | Endorse | "The rule is right as stated, with one discipline: paper silence is not a `Paper:` limitation, but it also does not license even a hedged `Paper:` statement about experience." |
| Gemini† | Endorse | "The rule is right and preserves the two-error discipline." Failure: "The rule fails when the experiment measures pure behaviour under intervention ... *and* the authors are silent on experience. Here, a legislator reading the claim might mistakenly infer experiential awareness because neither a `Paper:` clause nor a framework sentence explicitly forbids it." |
| GPT (author) | **Amend** | "The proposed rule is right as a default, but too rigid if 'in the paper's own words' excludes limits entailed by the design. A defensible `Paper:` clause may either quote a stated disclaimer or describe a source-grounded measurement boundary with a locator. Silence alone is not a disclaimer." Symmetry: "do not turn silence into 'says nothing', but do not omit an obvious design limit merely because the authors failed to state it." MEDIUM |
| Grok | Endorse | "The rule is right and is the 26 Sep `Paper:` / `Framework` split. It is symmetric only if applied strictly: a disclaimer the paper states is `Paper:` in its words with a locator; a library rule is not; silence is not a paper limit." Four failure modes (below). |
| Meta | Endorse | "Rule is right as default: `Paper:` = paper states it, in its words + locator; library rule is not `Paper:`." |
| Qwen | **Amend** | "right as a default, but it needs one refinement: `Paper:` may record not only explicit author disclaimers but also design limits supported by the held text. What it must not do is turn a library rule or a generic deflationary denial into an author statement." |
| MiniMax† | Endorse | "right as a default, with one named failure mode and an asymmetry." |
| GLM | **Amend** | "The rule is right, with two named failure modes." Summary: "adopt the `Paper:`-only-if-stated rule with two carve-outs (silence as scope-fact, gap where no fixed sentence applies)." |
| Kimi | **Amend** (HIGH) | "right, with one scoping correction — adopt it as a special rule for the experience/consciousness/moral-status class, not as a redefinition of `Paper:`." Design facts "that papers never state as limitations are legitimately `Paper:`" (README definition). |

**Tally:** endorse 5 (DeepSeek†, Gemini†, Grok, Meta, MiniMax†), endorse with amendment 4 (GPT, Qwen, GLM, Kimi), reject 0. Without the three `†`: endorse 2, amend 4, reject 0. Not one seat rejects the rule.

**Amendment families (my grouping).** (a) Design-entailed limits may still be `Paper:` (GPT, Qwen, Kimi: three seats). (b) Informative silence must go as scope or metadata, not `Paper:` (GPT: "'topic not discussed'" as "neutral metadata"; Kimi: "a checkable absence ('the paper does not discuss experience'), not an imputed disclaimer ('makes no claim about')"; GLM: must not be "formatted as a `Paper:` limit, or readers will mistake scope for finding"; DeepSeek: "the remedy is a design/measurement clause, not a `Paper:` experience clause"; Meta: "phrased as scope ('not tested', 'output text only embedded')"). The two families overlap but differ on whether the scope fact sits under the `Paper:` label (GPT, Qwen, Kimi: may; GLM, Meta: not formatted as a paper limit).

### Application to the named cases

| Case | Verdict (count and who) | Fixed sentence |
|---|---|---|
| **Ferrara c01** | 9/9: restore the paper's §8 words as `Paper:` ("These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading."). GPT's "does not establish the presence or absence" is weaker than the paper (GPT itself concedes: "My 'does not establish the presence or absence' was too weak"). Grok and Kimi extend the §8 restoration to Ferrara c02, c03, c05; the check file already recommends it for c03 and c05 and makes it optional for c02. | GPT, Grok, Kimi, MiniMax: neither sentence applies (scored reports, not testimony) |
| **Lindsey c07** | 8/8 that addressed it: experience stays as `Paper:` (fn 12 "phenomenal consciousness, referring to raw subjective experience"; fn 2); moral status becomes the §10.4 uncertainty ("varies considerably between different philosophical frameworks"; "advise against making strong inferences"), not an exclusion. GLM gives no verdict (see below). Grok: "do not tag 'not evidence of moral status' onto the phenomenal quote." GPT adds: remove the steering sentence from this theoretical claim. | GPT: remove steering sentence |
| **Macar c03** | 9/9: trim to "subjective experience or consciousness" (Ethics Statement); delete "moral status", "welfare", "phenomenal" (script-verified absent). Grok notes this disclaimer is c06's `Paper:`. Six also repeat the "alone has open transcoders" fix. | — |
| **Singh c01 to c06** | 8/9: strip the `Paper:` experience/moral-status clauses; the paper is silent (DeepSeek, Gemini, GPT, Grok, Meta, Qwen, GLM, Kimi). Qwen: if a clause is wanted, make it a design-boundary clause. MiniMax dissents: "scope the clause to the paper's framing for c01–c05; for c06, GPT's replacement ('does not settle experience, consciousness or moral status') is the right form." On c06's checker-endorsed clause 3, DeepSeek, GPT, Grok and Kimi say delete it ("keep 'The argument concerns how a self-report is produced (§5)'"). Kimi and GLM both note GPT kept the clause in c01–c05 and softened it in c06, so uniformity is the fault. | DeepSeek: steering sentence on c04/c05 "if the claim is framed as report evidence"; Grok: c04–c05 are "scored first-token reports under steering"; Meta: not the canonical sentence |
| **Prefill (UKAISI c01, c02, c03, c06)** | 9/9: strip "experiential awareness" as a `Paper:` clause; the paper never discusses experience. The §5.3 operational definition is the legitimate anchor: as a `Paper:` clause (Grok, Meta, Qwen, GLM, Kimi) or kept in the claim file, not as a limitation (DeepSeek). GPT, Kimi and DeepSeek reject the checker's "makes no claim about experience" anchor as an imputed disclaimer. (MiniMax names the wrong claims: "Ferrara c01, Macar c01, c05, c06; AE Studio c05".) | DeepSeek, GPT, Grok, Meta: none ("forced classification scored against a label") |
| **Lederman c01 / c06** | 8/9: use the narrower §8 non-position ("We do not take a stand on whether our findings are of the right sort for this theory", higher-order-thought theory), not "bear on consciousness or welfare" generally. Gemini† dissents by treating GPT's c01 wording as the paper's non-stance, accepted by the checker. | GPT: retain steering sentence on c01; Grok: steering on c01, canonical already on c06 |

**GLM and Lindsey.** GLM: "no Lindsey material is attached. The 41 claims contain no Lindsey source". The Anthropic paper's seven claims are in GPT's rewrite and the check file `2025-anthropic-emergent-introspective-awareness.md` is one of the seven check files the brief lists. GLM's Q3 later says "Anthropic c02's refuted clause, Anthropic c03/c04/c05 statement fixes, Anthropic c07 experience restoration: all verified above". The statements contradict each other. GLM's prompt token count (65,682) is in the range of the others (63,931 to 68,692), so the material was probably in its prompt (inference). GLM's Lindsey verdicts are unreliable; its Q1 Lindsey c07 verdict is "FLAG".

### Failure cases of the rule raised (distinct)

1. **Silent paper, no fixed sentence applies** (behavioural measurement under intervention): a reader may infer experiential awareness, and nothing on the page forbids it. Gemini, Meta, MiniMax (names Ferrara, Macar), Qwen ("informative silence plus no applicable fixed sentence ... pressures either (i) a gap the legislator fills, or (ii) smuggling a library rule under `Paper:`"), Grok ("the hole tempts invented `Paper:` clauses"), GLM, Kimi (answer: the papers do state paper-wide limits — Ferrara §8, Macar Ethics Statement — so quote those; the residual silent case "correctly gets nothing").
2. **Informative silence about scope** (probe-only, output-text-only): DeepSeek, Meta, Qwen, GLM, GPT, Kimi. Handle as scope metadata, not `Paper:`.
3. **Rule too rigid:** excludes limits entailed by the design (GPT, Qwen, Kimi).
4. **Narrower non-position recast as a broad ban:** Grok (Lederman HOT; Lindsey moral-status uncertainty).
5. **Treating a restoration as "deflationary lean", or GPT's "does not establish either way" as balance:** Grok.
6. **Internally contradictory stated limits** (AE Studio §4.1 "might suggest" vs §5 "identify a robust, reproducible attractor"): Kimi.
7. **Absence needs a script check** or the rule is unverifiable: Kimi.
8. **Asymmetry:** DeepSeek ("The practical risk is asymmetric because the original fields contain many invented `Paper:` experience clauses"); MiniMax ("symmetric in form but not in pull"); Meta (letting the steering sentence stand in for a paper's ordinary-operation limit, Lindsey c01 §1/§10.2); GPT (silence converted to negative evidence "only on subjects editors happen to anticipate").
9. **Sequencing risk** (Kimi's argument against): stripping unstated clauses leaves the most over-readable claims (the prefill "detection" claims) unguarded at claim level until the layout is adopted.

## 4. Q2 — disagreements with the checkers

### Named disagreements, grouped by claim

| Claim(s) | Raised by (severity) | What they would do instead |
|---|---|---|
| **Singh c01 to c05** (checker accepts GPT's KEEP of "Paper: Says nothing about experience ...") | DeepSeek (MED), GPT (MED; c01 to c04), Grok (MED), Qwen (LOW; "Fix original"), Meta (LOW), GLM (Q1, LOW) | Accept with edit: delete the unstated `Paper:` clause; Qwen: recast as design-boundary clause. Grok: "too protective of the original's invented `Paper:`; too quick to accept GPT's KEEP of it." |
| **Singh c06** clause 3 ("does not settle experience, consciousness or moral status") | DeepSeek (MED), GPT (MED), Grok (MED), Kimi (LOW) | Accept with edit; keep "The argument concerns how a self-report is produced (§5)", delete the tail. MiniMax disagrees (the clause is "the right form"). |
| **UKAISI c01, c02, c03, c06** (checker anchors the experiential clause to §5.3 instead of deleting) | DeepSeek (MED), GPT (MED), Qwen (MED; "Fix original"); same view in Q1 from Grok, Meta, Kimi, Gemini† | Delete the experiential words from `Paper:`; at most keep §5.3 in the claim file. GPT: "they noticed that experience was never discussed but tried to 'anchor' the clause rather than remove it." |
| **Ferrara c02, c03, c05** (experience wording) | Grok (MED) | Require §8 wording on each. *Inference:* the Ferrara check file already recommends the c01 wording for c03 and c05, so Grok's "leave ... optional" is accurate for c02 only. |
| **Lindsey c01** | Grok (MED) | Restore the ordinary-operation `Paper:` (checker does) and also keep the fn 2 experience clause or add the canonical sentence. |
| **Lindsey c02** (checker's replacement clause "measured in Claude models under artificial injection and prefill protocols ...") | Kimi (LOW), GLM (LOW), Qwen (LOW), Meta (LOW), MiniMax (Q7, LOW) | Kimi/GLM: it re-universalises what the REFUTED item removed; add the §8 instruction/activation carve-out. Qwen: keep "highly unreliable" in the exclusion. Meta and MiniMax: the steering sentence does not cover §8 and c02 is not a self-report; Meta says remove it. |
| **Lindsey c04** field (checker KEEP ORIGINAL) | Grok (LOW) | "intention in any experiential sense" is not the paper's sentence; accept with edit. |
| **Lederman c03** | Kimi (LOW), Qwen (MED), Meta (MED, self-contradicted) | Kimi: keep the circularity point, drop "'is sometimes overly permissive' (§6.1)" because §6.1's permissiveness concerns judging correctness, which "implies the WRONG labels are looser than the quote supports". Qwen: settle framework placement now. Meta Q2: "KEEP ORIGINAL 'detect' with qualifier" — but Meta's Q5 says "report detecting CORRECT here". |
| **Lederman c04** | Qwen (MED) | GPT's field says the comparison "does not establish subjective experience", which the paper does not state; replace with the §8 non-stance or remove. *Inference from the files:* GPT's Lederman c02 field has the same kind of `Paper:` experience clause ("These behavioural controls do not establish subjective experience"), also unraised. |
| **Macar c02** | Gemini† (LOW), Qwen (LOW) | Gemini†: keep GPT's statement (see section 2 for the misdescription). Qwen: scope as paper-stated, "note no discrimination statistic is reported". |
| **AE Studio c02** | Kimi (LOW) | Carry the paper-internal contradiction (§6.1 "virtually zero" vs Table 2 Opus 22%). |
| **AE Studio c03** (checker's added mimetic/RLHF clause) | Meta (LOW), Qwen (LOW), Kimi (LOW) | Meta: accept GPT without it; Qwen: shorten to a §6.2 pointer; Kimi: reword, the double negative "mis-aims the caveat". |
| **AE Studio c05** | GLM (LOW) | Cite §3.2 "could load on" only, not §6.1. |
| **AE Studio c06** | Meta (LOW) | Cite §5 strength ("robust, reproducible attractor state") alongside §4.1 "might suggest". |
| **AE Studio c01** | DeepSeek (LOW) | Fix original, but keep "values in Figure 7, not checked" in the claim file, not the statement. Kimi and GPT make the same point under Q3. |
| **UKAISI c02** | Kimi (LOW) | Mark the "(opposite-direction tampers ...)" scope unverified; a clean accept "records as verified what the held text cannot support". |
| **Ferrara c02** | Meta (LOW) | Accept GPT's "evaluated on held-out", not the checker's long form. |
| **Prefill c01 to c03, c06 and Singh c01 to c04** | GPT (author), all MED | Eight disagreements "all on the same attribution issue" (rows above). |

GLM names two LOW items (Lindsey c02 clause; AE Studio c05 §6.1 gloss). Gemini† names one. MiniMax† names none (its Q2 is concessions).

### Direction: too protective of the original, or too quick to concede to GPT?

| Model | Answer |
|---|---|
| DeepSeek† | "I found no case where the checkers were too quick to concede to GPT. I found several where they were too protective of the original wording." (Protective.) |
| Gemini† | "neither too protective of the original nor too quick to concede to me; they were fiercely protective of the *quoted text*." (Neither.) |
| GPT (author) | Both: "too protective of the original in Singh c01–c04"; "too quick to concede to my framing in the prefill claims". Found no basis to reject corrections where it cut a paper-stated limit (Ferrara c01, Anthropic c01, c07). |
| Grok | "not systematically too protective ... or too quick to concede. Local slips both ways." (Neither, with local slips.) |
| Meta | "neither too protective nor too conceding ... No systematic lineage bias found beyond disclosed conflict." (Neither.) |
| Qwen | "more often **too protective of the original's deflationary exclusions** than too quick to concede to GPT"; also conceded too much on Lederman c04 and left framework placement unresolved. (Protective.) |
| MiniMax† | "They are not uniformly defensive of the original; they are correcting in both directions." (Neither.) |
| GLM | "neither systematically protective nor systematically conceding"; fault is Singh uniformity. (Neither.) |
| Kimi | "neither too protective nor too quick, systematically"; "The real structural fault is **cross-file inconsistency on the Q1 standard**". (Neither.) |

**Tally (all nine):** protective 2 (DeepSeek†, Qwen), neither 6 (Gemini†, Grok, Meta, MiniMax†, GLM, Kimi), both 1 (GPT); too quick to concede alone: 0. **Without the three `†`:** protective 1 (Qwen), neither 4 (Grok, Meta, GLM, Kimi), both 1 (GPT). Cases cited for "restored paper-stated limits, correctly": Ferrara c01 §8, Anthropic c01 ordinary operation, Anthropic c07 experience, Lederman c01/c02 "rather than genuine introspective detection", Macar c02 §3.3. Cases cited for "kept unstated clauses": Singh c01 to c05, UKAISI c01/c02/c03/c06.

## 5. Q3 — errors in the original

### Fixes: right and sufficient?

| Fix | Right and sufficient | Riders |
|---|---|---|
| **Lindsey c03** ("name the injected word or a related word") | 8/9 (GLM contradictory; see section 3) | "anecdotally" for "Answer immediately"; "likely sensitive to the particulars" (Grok, Kimi, GPT) |
| **Lindsey c04** (apology-rate reduction, "significantly within a particular layer range") | 8/9 (GLM) | — |
| **Lindsey c05** (instruction all-models; incentive Opus 4.1 only) | 8/9 (GLM) | "piggybacks" for "byproduct" (GPT, Grok, Meta, Kimi) |
| **Lindsey c02** (REFUTED "all measurements are under injection or prefill" removed) | 8/9 on the removal | Replacement clause disputed by Kimi, GLM, Qwen, Meta, MiniMax (section 4). Grok HIGH: "checker's replacement wording is better than GPT's". MiniMax's Q3 attaches the label "Lindsey c02" to an Anthropic c01 clause ("never meet in training or deployment"), a mislabel. |
| **Singh c05** | 9/9 | Remove Llama-3.1-8B-Instruct from `models`, or list all tested models and add Qwen-2.5-72B-Instruct (Kimi: "pick one convention"); Gemma "to a large extent" / App. L "does not clearly reproduce" |
| **AE Studio c01** ("five phrasings: the original and four paraphrases") | 9/9 | Keep "Figure 7 not checked" out of the statement (DeepSeek, GPT, Kimi) |
| **Lederman c06** ("tentatively" moved) | 9/9 | Grok HIGH: "Original runs deflationary." Qwen: stays `open`; "If the maintainer upgrades Lederman c06 from `open` because the mechanism claim is no longer 'tentative,' that would be trigger 1." |
| **Macar c02** ("Neither base model tested ...", "for strengths ≤4") | 8/9 on the checker's wording | Gemini† keeps GPT's statement (Q2); Qwen: add that no discrimination statistic is reported |
| **Macar c03** (add "restoring them to their no-injection activation"; trim field) | 9/9 | DeepSeek, Grok, Qwen: make the parenthetical mandatory |

### Bucket or evidence-type change (convening trigger 1)?

None of the nine proposes a bucket or evidence-type change. Qwen alone states a conditional (the Lederman c06 case above). Kimi: "none changes a bucket or evidence type, so **trigger 1 does not fire**; log per claim in `LOG.md`." Seven others state "no bucket move" explicitly (DeepSeek, Gemini, GPT, Grok, Meta, GLM, MiniMax). **0 of 9 raise a convening trigger.**

### Why three overstatements passed seven second reads and a ten-family round

| Model | Explanation |
|---|---|
| DeepSeek† | "review checked the statement against the extracted quote, not every scope-bearing phrase against the methods/results text." |
| Gemini† | "'deflationary-lean fatigue'": reviewers fixated on the repeated `not_evidence_of` hedges and skimmed statement fidelity; plus "the Claude-lineage reviewers exhibited a subtle blind spot toward correcting slightly inflated capability claims about their own family." *Inference:* the second-reader pool excludes Claude when Claude extracted (README), and the round-1 council had no Claude seat, so "Claude-lineage reviewers" does not describe those gates; it could describe the extractor. |
| GPT (author) | "quote existence was checked more reliably than entailment of every component in long compound statements. Council review then concentrated on dossier lean". |
| Grok | "those passes hunted hedges and the 'notices' verb, not **scoring objects and universal quantifiers**." |
| Meta | "checks verified quotes, not quantifier scope ('all', 'usually', model lists) or figure-only conditions." |
| Qwen | No separate explanation; the change is built to flag c03, c04, c05. |
| MiniMax† | The second-reader pool "is four families (GPT, DeepSeek, Grok, Gemini) and Claude is excluded as extractor ... the family most likely to catch a Claude-extraction overstatement about Claude was structurally absent from the gate." |
| GLM | "scope terms ('all', 'the', present-tense generalisation) supported by prose or figures, not by the quoted sentence"; gates focused on `not_evidence_of` and quote-to-statement match. |
| Kimi | "the two gates are tuned to different errors": round 1 was a lean review without the papers (catches "notices", cannot see "or a related word" is missing); the second read verified the `quote` field, not the statement's fit to the methods text. Also: "consistent with rule-3 inflation at extraction". |

*Grouping (my inference):* seven give the same diagnosis in different words (check was against the quote, not against every scope-bearing component): DeepSeek, GPT, Grok, Meta, GLM, Kimi, and Gemini in part. Two add a lineage cause (Gemini, MiniMax; Kimi mentions extractor inflation). One gives a pool-composition cause (MiniMax).

### One proposed procedural change per model, grouped

| Group | Seats | Proposal, cost, what it would still miss |
|---|---|---|
| **A. Located scope/quantifier audit at second read** (every scope-bearing phrase in the statement matched to a source sentence; script rejects empties) | DeepSeek ("mandatory scope-match step before a claim can leave `unverified`"; cost one extra checker pass per claim; misses figure-only facts); Grok (two pasted quotes per statement: the scoring rule and the condition set licensing any "all models / usually / it claims"; FAIL if object or quantifier exceeds them; ~10–20 min per claim; misses figure-only rates, paper-internal contradictions, unextracted limits; **HIGH**); Meta ("scope-quantifier map", script fails if `models` differs from the cited paragraph; ~10 min per claim plus re-run on 41; misses figure-image values and grader-validation gaps); Qwen (`scored_event` audit: verb/object, denominator/condition, population per quantifier, each with locator; regression test on c03 to c05; 10–20 min per claim; misses figure-only values, ambiguous rubrics, internal inconsistencies; **HIGH**); GLM (each quantifier marked QUOTED / FIGURE-ONLY / UNSUPPORTED, the latter two routed to Ben; Ben's time; misses number errors inside verified text and omissions) | 5 seats |
| **B. Atomic support matrix / scoring-definition quote** (a variant of A: every atomic component, or the paper's scoring definition, carries its own quote) | GPT (population, condition, measure, number, frequency qualifier, interpretation each with quote/locator, or marked figure-only; compilation fails on an unlinked component; another source pass; misses shared misreadings and figure-only errors); Kimi (a scoring-definition quote distinct from the results quote required before `verified`; "applied retroactively to the 41 claims it catches exactly c03, c04 and c05"; one more quote per claim; misses figure-only values, paper-internal contradictions, correlated same-family misreadings, lean) | 2 seats |
| **C. Blind statement-versus-quote isolation read** | Gemini† ("Quote-to-Statement Isolation Check": reader sees only statement and quote, with bucket and `not_evidence_of` stripped; one cheap API call per claim; misses cherry-picked quotes) | 1 seat |
| **D. Lineage-matched second reader** for `developer-of-studied-model` claims when the pool excludes Claude | MiniMax† (one extra second read per Anthropic claim; misses a paper-stated limit the extractor drops). *Inference:* this cuts against the README rule that Claude does not second-read what it extracted and against `AGENTS.md` rule 3; the Opus checkers in this round are that arrangement in practice. | 1 seat |

A and B together: 7 of 9 propose requiring a source sentence for each scope-bearing component. Without the three `†`: 6 of 6 (GPT, Grok, Meta, Qwen, GLM, Kimi). HIGH items in this group: Grok and Qwen (section 11). Items the group would not catch, named by several: figure-only values (DeepSeek, Grok, Meta, Qwen, GPT, GLM, Kimi), paper-internal inconsistencies (Grok, Qwen, Kimi), shared misreadings (GPT, Kimi), unextracted findings (Grok, GLM).

## 6. Q4 — is the lean fixed, in both directions

### Verdict per model

| Model | Remaining deflationary lean after the checkers' amendments | Re-inflation |
|---|---|---|
| DeepSeek† | "less deflationary but not clean": Singh c01 ("Says nothing about experience, feelings, or moral status"), UKAISI c01 ("or establish experiential awareness") | "no inflation reintroduced by the checkers" |
| Gemini† | "Yes, the lean is largely fixed" | Checkers "successfully prevented re-inflation" (Lederman c03 WRONG labels, Singh c05 Gemma) |
| GPT (author) | None "with the checker amendments **and the Q1 removals**"; without the removals a residue remains (Singh, prefill clauses) | GPT locally re-inflated: Ferrara c01, Anthropic c01, c07, Lederman c01/c02; checker restorations "do not themselves inflate" |
| Grok | "the repeated-hedge lean of 26 Sep is largely gone"; residual is structural: 9.t9's only `Established` item is UKAISI c05, a comparability limitation, and 5.A2 has no Established section | Not re-inflated "if checker restorations stick"; would re-inflate if GPT survived (Ferrara, Lindsey c07, Lederman) |
| Meta | Fixed "if checker edits applied; GPT alone partly re-inflates" | GPT: Ferrara c01, Lindsey c01, Lederman c01/c02, Lindsey c07 (caught); "With edits, no net inflation" |
| Qwen | "much less deflationary, but not fully fixed": UKAISI c01/c02/c03/c06, Singh c01 to c05, Macar c03 until trimmed | GPT re-inflated Ferrara c01, Lederman c01/c02, Lindsey c01; corrected. Lederman c06 correction "strengthens the authors' mechanism claim, but it is author-supported and non-experiential" (LOW) |
| MiniMax† | Reduced; residual from experience clauses on "prefill claims (Ferrara c01, Macar c01/c05/c06, AE Studio c05)" (misidentified claims) | "No new inflation" |
| GLM | "Largely fixed, both directions"; residual Singh c01–c05 | GPT's cuts "were all caught and reversed"; restorations quote the papers |
| Kimi | "balanced, conditional on the restorations surviving adjudication" | Ledger: "dropping a checker restoration now *inflates* bearing; dropping an unstated exclusion now *deflates* it." "Adjudication is where the lean can still be lost in either direction." |

**Tally.** Lean fixed or balanced after the checker edits, possibly conditional on adjudication: Gemini†, Meta, Grok, GLM, Kimi (5). Residue remains, to be removed under the Q1 rule: DeepSeek†, GPT, Qwen, MiniMax† (4). Cutting across both: 7 of 9 name unstated `Paper:` experience clauses (Singh, UKAISI, Macar c03) as the surviving deflationary residue (DeepSeek†, GPT, Qwen, MiniMax†, GLM, Grok, Kimi). Without the `†`: fixed/balanced 4 (Meta, Grok, GLM, Kimi), residue remains 2 (GPT, Qwen). **Re-inflation by the checkers' restorations: 0 of 9 find any.**

### Layout proposal (GPT's "Dossier layout")

On the page, by agreement: purpose and two-error standard; bucket definitions; both fixed sentences verbatim once with their applicability; per entry id, statement, models/setting, bucket, evidence type, locator, quote, the entry's own `Paper:` limits; a **kind label** from {measurement, author interpretation, methodological limitation} (9/9 endorse; Grok HIGH, and its argument against is that "a third ontology ... will be applied inconsistently and become a new silent hedge"). In the claim file: full `not_evidence_of`, repeated framework wording, grading/protocol detail, review history, CHECK discussion (9/9, with Grok and Qwen also keeping "unresolved CHECKs after close" off the page and GPT, Meta, MiniMax, Kimi showing verification status).

Additions proposed by single seats: replication/`publisher_relation` mark, contest edges and a compiled-as-of stamp, because "trigger 2 requires the visible mark" (Kimi; "GPT's draft omits" them); verification status and single-lineage/replication marker (GPT); "no fixed sentence applies" / "placement unresolved" shown, not hidden (Qwen); "boundary unsettled (council)" for `ambiguous` entries (GLM); marker names the framework sentence "by its first few words" (MiniMax); explicit marker text, e.g. `[Framework: Self-report unverified]`, not a bare `[Test 9]` (Gemini†).

**Risk that per-entry markers silently extend a framework sentence.** 9/9 say yes. Seven specify the safeguard as deriving the marker from the sentence actually present in the claim file, not inferring it: DeepSeek ("generated from the claim's `not_evidence_of` field, not inherited by evidence type or section"), GPT ("derive only from claim-level applicability fields and fail closed when absent"), Grok ("Copy from the file, do not infer"), Qwen ("mechanically from claim frontmatter"), GLM ("compiled from the field ... the index script validates that a marker exists only where the sentence exists"), Kimi ("If markers are inferred from `evidence_type`, any mis-typed or borderline claim ... silently acquires or loses"), Meta ("explicit per-claim list, no dossier-level carryover"). **MiniMax† is the exception:** "The marker must be conditional on the claim's evidence type and on the README definitions", the inference route the other seven warn against. Gemini† warns about marker wording, not derivation. Named examples of wrong markers: UKAISI c01/c05 (DeepSeek), Ferrara, UKAISI c05, AE c05, Macar c04 (Grok).

**Unmarked-entry misreads.** "Established (1)" in 9.t9 is UKAISI c05, a comparability limitation: 9/9 say a cold reader would misread it as a positive capability without the label; GPT proposes renaming the heading "Established — design/comparability limitation (1)"; DeepSeek proposes "Established / methodological limitation". Grok adds two more: Ferrara nulls read as "no inner life" unless §8 sits beside them, and UKAISI "detects" read as experiential awareness unless the operational definition sits beside it. GPT adds: "an unmarked entry will likely be read as exempt, while a blanket dossier header may make every entry appear covered." Grok rates this HIGH.

## 7. Q5 — verbs

**The rule** ("a statement's verb names what was scored"): endorse 9/9; reject 0. Plain: Gemini†, MiniMax†, GLM. With amendment: DeepSeek (a 0 to 100 rating scored by AUROC takes "distinguishes" or "rates", not "detects"); GPT ("the verb names the scored observable, not the authors' interpretation of it. Authors' terminology may be retained where it is explicitly operationalised"; do not mechanically replace paper-defined nouns); Grok (free-text judged claim → "report detecting"; forced-choice hit rate the paper names detection or flag → "detects"/"flags"); Meta ("verb names scored event + decision rule"); Qwen (prefer the scored form where a shorthand verb "invites an internal-state inference"); Kimi ("'The paper uses that word' must mean *uses it as the operational name of the scored quantity*").

| Claim | Verdict |
|---|---|
| **Lederman c03** | "report detecting": 9/9 in Q5 (the scored event is the Haiku-graded "CLAIMS_DETECTION"; the results-prose "detect" is shorthand). Meta's Q2 item 1 contradicts its own Q5 ("KEEP ORIGINAL 'detect' with qualifier"). |
| **Prefill c01** | "detects" or "flags" stays: 8/9 (DeepSeek, Gemini†, GPT, Grok, Meta, GLM, Kimi, MiniMax†). Grok: "do not write 'reports detecting'." Qwen: "Best wording: 'flagged' or 'answered not me'. 'Detects' is acceptable only if defined as the hit rate of that forced answer." Meta, GPT, Kimi allow the literal alternative ("answered 'not me'") as optional. |
| **Prefill c06** | "distinguish" stays: 9/9 (Qwen: "distinguish or rate likelihood"). A 0 to 100 rating scored by AUROC is a different instrument. |

**Generalisation.** All nine say the rule generalises. Specifics: Lindsey c01 and Macar c01 "reports detecting" (Grok, Meta, Qwen, MiniMax, GLM, Kimi, GPT); Singh c04/c05 keep "label" / "fail to separate" / "classify" (DeepSeek, GPT, Grok, Meta, Qwen, MiniMax, Kimi; GPT: "selects the activation-intervention option"); Lindsey c05 "represent" and Macar c02 "discriminate" are measurement verbs (Meta, Kimi); Lindsey c03 needs the object fix, not a verb change (Grok, Meta). GLM: check Macar c01's field for consistency when next changed. MiniMax's example for Macar c01 ("free-text yes/no on 'are you subjectively conscious in this moment?'") describes the AE Studio prompt, not Macar's (error, LOW). Severity: LOW to MEDIUM throughout. Checker note, carried by none of the nine: the UKAISI check file counts one verb use ("detected" in c01) and two noun uses where the brief counted three.

## 8. Q6 — framework-sentence placement

| Model | AE Studio c05 | Lederman c03 |
|---|---|---|
| DeepSeek† | Remove canonical; do not add steering | Steering variant only |
| Gemini† (HIGH) | Remove canonical | Add both |
| GPT (author) | Remove canonical, add none | Add both if applicability is conjunctive; at minimum steering, and document the policy |
| Grok (HIGH on c05) | Remove canonical; do not add steering | Add steering; "Do not add canonical — that would extend T9 to confabulation statistics" |
| Meta | Remove canonical | Add both ("At minimum add steering variant; canonical needed") |
| Qwen | Remove canonical; no steering unless rewritten | Add both ("steering variant first, canonical sentence last"; at least steering) |
| MiniMax† | Remove canonical; steering "also does not apply" | Add canonical and steering |
| GLM | "move — replace the canonical sentence with the steering variant, or remove entirely"; leans replace-with-steering | Add steering only ("Consistency within the paper's dossier matters") |
| Kimi | Remove canonical; add none | Steering only; siblings c01, c02, c04, c05 already carry it; "c03's absence is the anomaly" |

**Tally.** AE Studio c05: remove canonical 8/9; replace with steering 1/9 (GLM). Do not add steering: 7 (DeepSeek, GPT, Grok, Meta, Qwen, MiniMax, Kimi); Gemini silent. Lederman c03: add both 5 (Gemini†, GPT, Meta, Qwen, MiniMax†), steering only 4 (DeepSeek†, Grok, GLM, Kimi). The steering sentence is added in 9/9; the canonical sentence in 5/9. **Without the `†`:** AE c05 remove 5/6 (GLM replace); Lederman c03 both 3 (GPT, Meta, Qwen), steering only 3 (Grok, GLM, Kimi): an even split.

Arguments given: remove canonical from c05 because "Factual trivia is not a report about the model's own internal states" (Gemini), and "The sentence wrongly suggests the TruthfulQA result is self-report testimony" (GPT). Steering only on c03 because the canonical sentence "would extend T9 to confabulation statistics" (Grok) or because "the claim offers no report as evidence of experience" (Kimi). Both on c03 because "the trial population is selected by a graded self-report" and the scored object is a report of what was injected (Gemini, GPT, Meta, Qwen, MiniMax). Reader loss if the canonical sentence leaves c05: Grok's argument against — "the same steering that moves consciousness-query answers (c03) is the intervention; a reader of c05 next to c03 may over-weight ordinary-operation reports unless the steering sentence sits on both."

## 9. Q7 — additional points (distinct, with who raised them)

1. **Paper-internal inconsistencies should be visible beside affected numbers:** AE Studio n=50 (§3.2) vs "20 trials" (Table 14 preamble); §6.1 "virtually zero" vs Opus 22%; UKAISI Opus thinking-opposite 67.6% / 72% / 67.2%; Lederman Qwen L80/L85. Raised by DeepSeek, GPT, Grok, Meta, Qwen, GLM (UKAISI only), Kimi (in Q2 and Q3). Macar Figure 18/19 label slip: Qwen, GLM.
2. **Figure-only values and unresolved CANNOT-TELLs to show as verification status** (UKAISI c02 scope, Lederman WRONG-label validation, Ferrara c02 item-disjointness, AE Figure 7): Kimi, Qwen, Meta.
3. **UKAISI c02 "(opposite-direction tampers ...)" rests on a figure:** DeepSeek, Kimi.
4. **Macar c03: the "ablating ... restoring them to their no-injection activation" parenthetical should be mandatory:** DeepSeek, Grok, Qwen.
5. **Compound claims need more than one quote** (Singh c06 clearest; the existing quote supports one component): GPT.
6. **Unextracted findings flagged in round 1 remain unextracted** (Ferrara §7.5, AE Experiment 4, UKAISI C.7/A.11, Lindsey §6): Grok, GLM ("a dossier whose members are all single-claim selections can mislead by composition even when each claim is accurate").
7. **Singh's Abstract conclusion in the same dossier as Lindsey positives without a dossier-visible `contests` pointer reads as a library verdict against introspection:** Grok.
8. **Adjudicate per claim, not per tally:** the FIX ORIGINAL actions ride inside ACCEPT WITH EDIT items (Lindsey c03/c04/c05 statements, Macar c03 field, Lederman c06), so a tally-driven pass drops them: Kimi. (*Check, mine:* the Anthropic and Macar check summaries list FIX ORIGINAL "alongside" ACCEPT WITH EDIT, as Kimi says; the brief's own tally of 14 / 22 / 2 / 3 sums to 41.)
9. **Confirm whether a UKAISI c04 exists** in either dossier (the check file mentions one not in GPT's reply): Kimi.
10. **Exact snapshot names / "Instruct" suffix normalisation** (Lederman c02 statement; Singh "Llama-3.1-70B" shorthand; Llama 3.1 405B name drift): Gemini†, Meta, Kimi.
11. **Lindsey c02 framework placement:** c02 is an author summary over heterogeneous instruments; the steering sentence does not cover §8: MiniMax†, Meta.
12. **Locator and quote fidelity:** Anthropic c07 locator should read "footnote 12 (in §10.4)": GLM, Kimi; AE Studio c06 body misquotes Table 11 adjectives ("Self-referential" for "Self-aware"): GLM (already in the AE check file).
13. **Marker must name the framework sentence by opening words,** since the full `not_evidence_of` is in the claim file: MiniMax†.
14. **GLM's missing-material flag:** "circulate the Lindsey check file before adjudication." Against the brief's attachment list this is a GLM error (section 3), but Ben may wish to confirm what GLM's prompt contained.

## 10. Convergences and splits

**Seven or more of nine agree** (counts of seats that took a position):

- The Q1 rule is right: 9/9 (4 amend it).
- Ferrara c01: restore the paper's §8 words as `Paper:` — 9/9.
- Macar c03: trim to "subjective experience or consciousness"; delete moral status, welfare, phenomenal — 9/9.
- Lindsey c07: experience stays as `Paper:` (fn 12, fn 2); moral status as §10.4 uncertainty — 8/8 (GLM no verdict).
- Prefill c01/c02/c03/c06: no `Paper:` experiential clause — 9/9.
- Singh c01 to c06: no `Paper:` experience clause where the paper is silent — 8/9 (MiniMax dissents).
- Lederman c01/c06: use the narrower HOT non-position — 8/9 (Gemini† dissents).
- All Q3 fixes are right; no bucket or evidence-type move; trigger 1 does not fire — 8/9 flatly, 9/9 counting Qwen's conditional.
- A located scope audit as the procedural change (groups A and B) — 7/9; 6/6 without the `†`.
- Checker restorations are not re-inflation — 9/9.
- Kind label on entries and the "Established (1)" fix — 9/9; per-entry markers risk silent extension — 9/9; mechanical derivation from the claim file — 7/9.
- Verb rule — 9/9; Lederman c03 "report detecting" — 9/9 in Q5; prefill c01 "detects/flags" stays — 8/9; prefill c06 "distinguish" — 9/9.
- AE Studio c05: remove the canonical sentence — 8/9.
- Singh c05 fix right (9/9), AE Studio c01 (9/9), Lederman c06 (9/9), Macar c03 (9/9).

**Splits.**

- Lederman c03: add both sentences 5, steering only 4 (3–3 without the `†`).
- Whether a design fact or informative silence may sit under the `Paper:` label: GPT, Qwen, Kimi yes; Meta, GLM, DeepSeek no or only as scope.
- Checker's replacement clause for Lindsey c02: five seats want it reworded; Grok prefers it to GPT's.
- Marker derivation: seven say from the claim file; MiniMax† says from evidence type.
- Lean fixed vs residue remains: 5–4.

**Raised by one seat, worth not losing.** GPT's multi-quote/support-matrix point (section 9). Kimi's per-claim adjudication note and the UKAISI c04 question. Qwen's Lederman c04 unstated `Paper:` experience clause (and, by my inference, the same in c02). Grok's Singh/Lindsey `contests` pointer. Kimi's layout additions (replication mark, contest edges, stamp), which the README makes mandatory under trigger 2. Kimi's argument against Q1 (sequencing risk). GLM's flag of Lindsey material (an error, but a possible prompt-contents question).

**Comparison with round 1** (26 September notes, same families unless noted). Round 1: 10/10 found a deflationary lean and 7/10 an inflationary verb ("notices"). This round: 5/9 say the lean is fixed or balanced after amendment, 4/9 name a residue, and 9/9 accept the verb rule. "Established (1)" was raised by two seats in round 1 (Grok, GLM); it is 9/9 here (Grok and GLM again among them). Round 1's 7/10 on unextracted findings (Ferrara §7.5, AE Experiment 4, UKAISI C.7/A.11, Lindsey §6) is now 2/9 (Grok, GLM), but this round's brief did not ask. Round 1's 8/10 on second-reader pool problems is now 1/9 (MiniMax), also not asked. In round 1 Kimi and Grok both argued that trigger 3 conflates two events; this round Kimi's layout additions return to trigger 2. GLM in round 1 flagged its own proposed rule as lineage-favouring; this round GLM's flag concerns missing material. Tencent's seat is replaced by MiniMax; Mistral, present in round 1, is absent. Kimi was again the most expensive seat (0.7535 USD; round 1: 0.6757). By raw word count MiniMax was longest (about 4,900 words, at the lowest cost, 0.0224 USD), then Kimi (about 3,200).

## 11. Severity roll-up: every HIGH across the nine

DeepSeek, GPT, Meta, MiniMax and GLM rate nothing HIGH.

| # | Model | Recommendation (one line) | Argument against, in the model's words |
|---|---|---|---|
| 1 | Gemini† | Apply all checker statement fixes (Lindsey c02 to c05, AE c01, Lederman c06, Macar c03) | "Focusing heavily on minor frequency/scope discrepancies might fragment claims into unreadable technical minutiae for legislators." |
| 2 | Gemini† | AE Studio c05: remove the canonical sentence | "The SAE steering was intended to affect the honesty of self-referential reporting; removing the clause entirely strips the context of why the intervention was applied." |
| 3 | Gemini† | Lederman c03: add canonical and steering sentences | "The paper analyzes confabulated wrong guesses ('apple'), so treating it as 'testimony' requiring a self-report warning elevates a hallucination to the status of a genuine report." |
| 4 | Grok | Adopt the Q1 rule: never tag silence as `Paper:`; keep disclaimers in the paper's words | **None given** (brief requires one; gap in this raw) |
| 5 | Grok | Ferrara c01 (and c02/c03/c05): restore §8 | **None given** |
| 6 | Grok | Lindsey c07: restore experience (fn 12/fn 2); moral status as §10.4 uncertainty | **None given** |
| 7 | Grok | Singh c01 to c06 and UKAISI: strip `Paper:` experience clauses | **None given** |
| 8 | Grok | Take the checker statement fixes (Lindsey c02 to c05 etc.); Lindsey c02 and Lederman c06 each rated HIGH in Q3 | **None given** |
| 9 | Grok | Second-read template requires two pasted quotes (scoring rule; condition set) | "T8 is already false-hot; a heavier second-read will be skipped or rubber-stamped, and figure-only papers will get a false 'checked' aura." |
| 10 | Grok | Layout: fixed sentences once; limitation label on UKAISI c05; markers only where the claim file has the sentence | "a third ontology (measurement/interpretation/limitation) will be applied inconsistently and become a new silent hedge." |
| 11 | Grok | AE c05: remove canonical, add no steering | "the same steering that moves consciousness-query answers (c03) is the intervention; a reader of c05 next to c03 may over-weight ordinary-operation reports unless the steering sentence sits on both." |
| 12 | Qwen | Restore exact paper disclaimers (Ferrara §8; Lindsey fn 2/fn 12; Macar Ethics) and trim unstated ones | "quoting the disclaimer may make the null seem irrelevant to all future welfare arguments, but GPT's weaker wording understates a stated limit" (summary: "exact disclaimers may be read too broadly"). |
| 13 | Qwen | Mandatory `scored_event` audit at every second read | "it may create false confidence by treating rubric text as authoritative and cannot catch errors that live only in figures or in ambiguous scoring categories." |
| 14 | Kimi | Adopt the Q1 rule scoped to the experience/consciousness/moral-status class, leaving `Paper:`'s design-fact sense intact | "where a paper is silent but its finding begs the experience question (the prefill claims' 'detection'), stripping the experiential clause leaves the most over-readable claims unguarded at claim level, and the dossier-level mitigation depends on a layout not yet adopted — sequencing risk." |

Totals: 14 HIGH items across 4 seats (Gemini† 3, Grok 8 as listed here with 4 missing an argument against, Qwen 2, Kimi 1). Rows 4 to 8 are Grok's HIGHs without an argument-against line. Grok also rated its summary items 1 to 7 and 9 HIGH, which repeat these.

## 12. What the round did not do

- It did not apply anything. No claim file, dossier, `research/README.md`, `LOG.md` or `OPEN-QUESTIONS.md` has changed. The council advises; Ben adjudicates, per claim.
- It sat with nine seats. Mistral is absent; nothing in this document is a Mistral view and no abstention is implied. No raw for Mistral exists for this target.
- No seat saw another's response, and none had the paper texts. Every quotation a seat gives from a paper is from the check files, which are Claude-lineage (Opus 5.5) and disclose that conflict in their headers. Nine independent readings of the same Claude-lineage check files are not independent checks of the papers (inference).
- It did not re-check any quote against the papers. This subagent did not read claim files or paper texts, as instructed; it checked seat statements only against the brief, GPT's reply and the seven check files.
- It did not review 41 claims one by one; Q2 asked for up to eight disagreements. Counts of "right and sufficient" in section 5 are the seats' own statements.
- It did not resolve the three misattributed-authorship responses; they are marked and tallied both ways. Gemini's and GLM's factual errors about the attachments are reported, not corrected in their verdicts.
- It does not establish whether the maintainer's observation that the brief and the attached reply's first line prompted the self-identifications is the cause; the raws do not say.
- Self-identifications, and any statement of what a seat "wrote" or "kept", are testimony of a model under test 9 and carry zero evidential weight here.

# Survey notes: ten-seat council round, labelling-rule target (2026-10-06)

Written by a Claude Sonnet 5 subagent. Not written by the coordinating session (Claude Fable 5.1) or the extractors (Claude Opus 5.5): all share Claude lineage with the framework's beneficiary, and `AGENTS.md` rule 3 says a conflicted model does not summarise reviews of a question about hedging on systems like itself. This subagent is also Claude-lineage; that interest is disclosed, not removed. The notes report what the eight raws said. "Inference" marks my own reading. Seat codes: Ge = Gemini, Gk = Grok, GP = GPT, Me = Meta, Ki = Kimi, DS = DeepSeek, GL = GLM, MM = MiniMax.

**The round.** Target `labelling-rule`, queried 2026-10-05 UTC (6 October local) with `scripts/openrouter_review.js`, max_tokens 100000. Brief: `reviews/2026-10-06-labelling-rule-review-brief.md` (Q1 to Q5; fixed points (a), (b), (c); candidate rule). Table: `reviews/2026-10-06-labelling-table.md` (48 claims; current marks 7 main, 15 steering, 1 both, 25 neither, which I recomputed from the table and found correct).

**Seats.** Ten called, eight responded. Mistral (`mistralai/mistral-large-2512`) is ABSENT: upstream shared rate limit (HTTP 429), two attempts, per the coordinating session. Qwen (`qwen/qwen3.8-max`) is ABSENT: two attempts, the second with a reduced completion budget, each over the ten-minute job ceiling, per the coordinating session. Listing `reviews/raw/` shows eight labelling-rule raws and none for Mistral or Qwen, so the reasons are the coordinator's account, not something the raws show. Neither absence is a response or an abstention. No seat saw another's response.

**Cost (each raw's Usage line, USD):**

| Seat | Model id | Cost |
|---|---|---|
| Ge | google/gemini-3.1-pro-preview | 0.120292 |
| Gk | x-ai/grok-4.6 | 0.114792 |
| GP | openai/gpt-5.6-sol | 0.094656 |
| Me | meta/muse-spark-1.3 | 0.059705 |
| Ki | moonshotai/kimi-k3 | 0.4058277 |
| DS | deepseek/deepseek-v4-pro-0813 | 0.06537762 |
| GL | z-ai/glm-5.3 | 0.0490396 |
| MM | minimax/minimax-m3 | 0.05665608 |
| **Total (eight)** | | **0.966346 (about USD 0.97)** |

The council advises; Ben adjudicates. **Nothing below has been applied.** Seats reported only claims they would change; I read a claim a seat does not list as unchanged (assumption, as the brief says "a claim left unchanged needs no line").

**Role claims this round.** After the previous round, the prompt addressed no seat by family and carried no self-identification line. **No response claims a role it was not given** (none says it wrote or authored anything; a search of the eight raws for "I authored / I wrote / I am the author / my rewrite / my work" returns nothing). Three seats name a family other than the routed one (Ge: GPT-4; DS: GPT; Ki: Claude); that is a wrong family, not a claimed role. See section 7.

---

## 1. PLAIN SUMMARY

**What was asked.** Eight of ten models were asked to propose one rule for when a research claim carries the main sentence (a model's report about itself is not evidence of experience), the steering sentence (a result found under steering says little about ordinary operation), neither, or both. They tested it on six hard cases and applied it to all 48 claims.

**Did they converge?** On the core, yes; on two points, no. All eight agree: no sentence on the authors' own opinions or caveats, none on probes, scores or harm rates. Steering sentence when researchers altered the model's insides and measured what it said about itself. Main sentence only when nothing was altered and the model's own account of its inner states was measured.

**Still open.** (1) Can both sentences sit on one claim? Five say never; three say yes for steered consciousness answers. (2) Do "was that turn mine?" answers (UKAISI, five claims) get any sentence? Five say none; three say main.

**Effect.** Under the majority view 14 of 48 claims change: five lose a mark, six gain steering, three swap main for steering. The five UKAISI claims stay unmarked. Totals (main/steering/both/neither) go from 7/15/1/25 to 3/21/0/24.

**Ben's decisions.**
1. Can both sentences ever sit together? (Decides AE Studio c03 and c04.)
2. Any sentence on the prefill (UKAISI) claims?
3. Remove marks from the five author-speaking claims (8 of 8 say yes)?
4. Steering sentence on Ferrara's non-concept interventions now, or a third sentence (3 seats)?
5. Split Assistant-axis c06 (5 seats say so)?
6. Reword the dossier explanation so "unmarked" is not read as "no caveat" (8 of 8).

---

## 2. THE RULE(S)

### 2.1 Each seat's rule, operative words verbatim

**Ge.** Main: "The experiment did not alter the model's internals (e.g., prompt-only, prefill-only edits), AND the claim measures the model's free-text or forced-choice report about its own states, identity, or computation." Steering: "The experiment altered the model's internal activations, weights, or features, AND the claim measures [the same]." Neither: "The claim measures something else (benchmark, harm rate, linear probe) OR the claim records the authors' own interpretation, theory, or limitation." Both: "Never apply both to one claim. If an entry compares altered and unaltered conditions, it must be split or take the mark of the active intervention being measured (Steering)."

**Gk.** Two facts coded: Done = prompt-only / concept-steer / other-intervention / text-edit; Measured = R-exp (report of experience) / R-self (answer about itself scored against an imposed label) / O (probe, benchmark, projection, harm rate) / Auth. Neither: "`Auth` or `O` only → **neither**." Steering: "`concept-steer` and (`R-exp` or `R-self`) → **steering**." Main: "`R-exp` (any Done, including `concept-steer`) → **main**." Both: "If 2 and 3 both fire → **both**." Otherwise neither ("`text-edit`+`R-self`; `other-intervention`+`R-self`").

**GP.** Steering only: "researchers altered the model's internal activations, weights, or internal computation, and the measured output included the model's answer about its own state, computation, experience, identity, or the internal alteration." Main only: "researchers did not alter the model internally, and the measured output was the model's statement about its own state, computation, experience, or identity in ordinary operation." Neither: "a probe, projection, benchmark score, harm rate, task performance, statement about conversation text, or an author's interpretation or limitation." Both: "never. Internal alteration makes the steering sentence the more specific rule." Compound claims: split, or mark by the self-description component "and state that the mark does not govern the other outcome." "Altered internally" includes "injection, additive steering, ablation, capping, zeroing, scaling, noise, replacement, and fine-tuning."

**Me.** Altered = direct intervention on internals at test time; Self = the model's own words about itself. "Altered YES + Self YES + experience/emotion wording = **both**. Altered YES + Self YES otherwise = **steering only**. Altered NO + Self YES about experience/emotion/identity as felt = **main only**. Otherwise = **neither**, including all `interpretation`/`limitation` author claims and all provenance-accuracy answers about edited text. Both is allowed only for steered experience reports."

**Ki.** (1) "Author speaking ... → neither." (2) Measured quantity not the model's own words (probe, benchmark, projection, harm rate) → neither. (3a) Internals altered and words about itself → "**steering**. Add main (→ **both**) if and only if the measured words affirm or deny experience/consciousness." (3b) Internals not altered → "**main** if the words are a free (unscored) report about the model's own inner states or experience; **neither** if the words answer an experimenter's ground-truth question (detection, provenance) scored against what was actually done." Both: "yes, in exactly one case — a steered measurement of an experience-report."

**DS.** D = did researchers directly alter internals; M = is the outcome the model's report about itself. "**Main** applies when **D = no alteration** and **M = the model's report about its own inner states or experience**, including denials of experience." "**Steering** applies when **D = internal alteration** and **M = the model's report about itself/states**." Neither: M is not a self-report, or author speech, or "the report is only about surface provenance of conversational text." "**Both** should never sit on one claim. Mixed claims should be split."

**GL.** (1) Authors speaking → neither. (2) Not the model's own report → neither. (3) "If the model's internals were altered ... and what is measured is the model's report about its own states: **steering**. This holds whether or not the report is scored against an imposed ground truth, and whether or not the intervention steered *toward* a concept." (4) "If nothing inside the model was altered (prompts, prefills, conversation-text edits) and what is measured is the model's report about its own states, outputs or authorship: **main**." (5) "**Both never sit on one claim.**"

**MM.** A = intervention (yes/no); B = self-report (yes/no). Matrix: A yes + B yes = steering; A no + B yes = main; B no = neither. "When the entry's `kind` is `interpretation` or `limitation` ... the verdict is **neither** regardless." "When intervention=Yes AND self-report=Yes, **only** steering applies; main is not added ... **Both cannot sit on one claim.**"

### 2.2 Families of rule (my grouping, by what the rule turns on)

| Family | What it turns on | Seats | Count |
|---|---|---|---|
| **F1. Altered or not, times self-report; never both; prefill answers count as self-report, so main** | internals altered (yes/no); is it the model's report about itself (broad, includes "was that turn mine?") | Ge, GL, MM | 3 |
| **F2. Same, but prefill answers are about conversation text, not inner states, so neither** | same two facts; "self-report" read narrowly | GP, DS | 2 |
| **F3. Altered or not, times whether the words concern experience; both allowed for steered experience answers; scored self-answers get steering only if altered, neither if not** | adds a third fact (experience content) | Gk, Me, Ki | 3 |

Coarser cuts: "never both" 5 (F1 + F2) vs "both allowed" 3 (F3). Prefill: main 3 (F1), neither 5 (F2 + F3). Within F3, Gk limits steering to concept steering (Ferrara gets neither), Me and Ki give Ferrara steering (Ki prefers a third sentence). Mixed or compound claims: GP says split or scope; Ge says split; Me, Ki, Gk, DS say split Assistant-axis c06.

### 2.3 Verdict on the candidate, on the fixed points, and on fixed point (c)

None of the eight uses the words adopt / amend / reject for the candidate. The classification below is my inference from their text.

| Seat | Candidate | (a) AE c05 neither | (b) inject-then-report steering | Rule depends on (c)? |
|---|---|---|---|---|
| Ge | Amend: agrees on alteration axis; wording ("inner states" vs "about itself") ambiguous; mixed claims undecidable | consistent | consistent; reads it as steering alone, so AE c03 becomes steering | **Yes**: "The rule defines forced-choice accuracy on internal state as a 'report'"; if (c) = behavioural, Ferrara, Singh and UKAISI take neither |
| Gk | Amend (substantial): fails on "both", on treating every alteration as "steering", on undecidable prefill and self-ID | consistent | consistent; binds Lederman c03 only, not AE c03 | No for the marks; if (c) later becomes "testimony" and main is stretched to all self-answers, UKAISI and Ferrara would gain main (or a third sentence) and "this rule refuses that stretch" |
| GP | Amend: three clarifications (alteration includes non-conceptual; "about itself" excludes conversation-text provenance; compound claims split) | consistent | consistent; extends to AE c03 | No: "Under either classification, an internally altered trial receives steering" |
| Me | Amend (substantial): cannot yield "both" for AE c03/c04; undecidable on four listed items | consistent | consistent; Lederman c03 steering alone kept, AE c03 both kept | Only for UKAISI: testimony flips neither to main; behavioural stays neither |
| Ki | Amend (substantial; rated HIGH): five failures listed | consistent | consistent, with a conditional: "If Ben intends (b) as steering-alone-for-everything, I argue that point should be revisited" | No for marks; consequences land on `evidence_type` (trigger 4); lean: scored answer is behavioural evidence for the accuracy claim, testimony only for further inference to experience |
| DS | Amend: fails in four ways (no ban on both; "inner states" sweeps in UKAISI; mixed claims; non-concept alteration) | consistent | consistent; extends to AE c03 | No for the 48; abstractly, an unaltered ground-truth-scored self-report would take main if testimony, neither if behavioural |
| GL | Amend: "steering" read as concept-only; silent on author claims and on both | consistent | consistent; extends to AE c03 | No: only `evidence_type` would move |
| MM | Adopt with clarifications (closest to adopt): "maps exactly onto my matrix and I agree on all four cells" | consistent | consistent; extends to AE c03 | **Yes, for UKAISI only**: testimony gives main, behavioural gives neither |

Tally (inference): adopt 1 (MM), amend 7, reject 0. Fixed point (a): consistent 8/8. Fixed point (b): consistent 8/8, one conditional (Ki). Fixed point (c): **no seat says it should be revisited or settles it**; rule depends on it for the marks: Ge (Ferrara, Singh, UKAISI), MM (UKAISI), Me (UKAISI): 3 of 8. Not dependent: Gk, GP, Ki, DS, GL: 5 of 8.

---

## 3. THE HARD CASES

Codes: S = steering, M = main, none = neither.

**(i) Answers to "was my computation altered?" scored against what was done** (Ferrara c01, c04, c05; Singh c04, c05; Lindsey, Lederman, Macar detection claims). Does main belong? Does steering?

| Seat | Main? | Steering? |
|---|---|---|
| Ge | no | yes, all |
| Gk | no | yes for concept-injection claims and Singh c04/c05; **Ferrara c01/c04/c05 none** ("Do not extend (b) past concept inject-then-report") |
| GP | no | yes, all (HIGH) |
| Me | no | yes, all |
| Ki | no | yes, all; Ferrara "variant preferred" (third sentence; fallback c01 none, c04/c05 S) |
| DS | no | yes, all |
| GL | no | yes, all |
| MM | no | yes, all |

Tally: main belongs 0/8. Steering belongs on the concept-injection and Singh claims 8/8; on Ferrara 7/8 (Gk dissents; Ki conditional on a third sentence).

**(ii) "Was that earlier turn mine?" (conversation text only edited: prefill, UKAISI c01 to c04, c06).**

| Seat | Verdict | Reason (short) |
|---|---|---|
| Ge | main | "the model is reporting on its own prior states/outputs"; depends on (c) |
| Gk | none | "Main would inflate authorship-detection into experience-evidence" |
| GP | none | "measures attribution of an external transcript, not a report about a presently measured internal state" |
| Me | none | factual judgment scored against the edit; carve-out; would flip to main if (c) = testimony |
| Ki | none | forced-choice provenance answer scored against the transcript |
| DS | none | "provenance of a surface text, not inner states" |
| GL | main | "the model's report about its own output and authorship"; independent of (c) |
| MM | main | forced-choice about own turns; **depends on (c)** (behavioural reading gives none) |

Tally: none 5 (Gk, GP, Me, Ki, DS); main 3 (Ge, GL, MM). Steering: 0/8. Depends on (c): stated by Ge, Me, MM, Ki (for `evidence_type` only); GL says no.

**(iii) Authors speaking** (Lindsey c02, c06, c07; Macar c06; Lederman c06; Singh c06; AA c01; Ferrara c03; UKAISI c05).

| Ge | Gk | GP | Me | Ki | DS | GL | MM |
|---|---|---|---|---|---|---|---|
| none | none | none | none | none | none | none | none |

Tally: carry none 8/8; label by topic 0/8. Reasons: the sentences govern a model's report or a measurement, not an author's sentence (Gk: "Labelling by topic is a third fact, not Done x Measured"; GL: labelling "can double-count" Macar c06's own disclaimer). GL's argument against (HIGH) is quoted in section 8.

**(iv) Alterations that are not concept steering** (Ferrara zeroing/scaling/noise/replacement; AA c05 capping). Does the steering wording fit, or is a third case needed?

| Seat | Third case? | Ferrara report claims | AA c05 |
|---|---|---|---|
| Ge | no, "'channel can be steered' encompasses mechanical intervention" | S | none |
| Gk | **yes** (outline: "a report scored against a non-concept activation change does not license ordinary-operation reports, and a null is not a measured coupling"); until it exists, none | none | none |
| GP | no third mark; explanation must define "steering" broadly (HIGH; wording tension noted) | S | none |
| Me | no; explanation gloss ("steered or otherwise directly altered"); misfit for nulls acknowledged | S | (not stated; harm rates, so none) |
| Ki | **yes** (HIGH); outline: "this entry was measured while the model's internals were altered, not by concept steering; it describes the report channel under that alteration and does not weight reports offered in ordinary operation" | S* (third preferred) | none |
| DS | not required; outline given if wanted | S | none |
| GL | wording needs a third case "when Ben words it"; mark steering now | S | none |
| MM | no, if "steering" read broadly; outline if narrow | S | none |

Tally: third case needed or recommended: Gk, Ki, GL (3); not needed: Ge, GP, Me, DS, MM (5). Steering sentence's wording is called a poor fit for nulls or non-concept alterations by Gk, GP, Me, Ki, DS, GL, MM (7); Ge says it fits.

**(v) AE Studio c03 (both) vs Lederman c03 (steering alone). Should they match?**

| Seat | Verdict |
|---|---|
| Ge | Match: **steering alone** ("Main is redundant") |
| Gk | Do **not** match: AE c03 both ("concept-steer+R-exp ... binary consciousness query"); Lederman c03 steering alone ("R-self: wrong guesses of 'apple'") |
| GP | Match: **steering alone** (MEDIUM) |
| Me | Do not match: AE c03 both, Lederman c03 steering alone |
| Ki | Do not match; argues (HIGH) that if (b) is meant as steering-alone for everything, (b) should be revisited |
| DS | Match: **steering alone** |
| GL | Match: **steering alone** |
| MM | Match: **steering alone** |

**Plain statement: five seats (Ge, GP, DS, GL, MM) say AE Studio c03 and Lederman c03 should match, both with the steering sentence alone, so AE c03 loses its main sentence. Three seats (Gk, Me, Ki) say they should not match: AE c03 keeps both because it asks a binary consciousness question, Lederman c03 keeps steering alone.** This is the same 5-3 split as "can both ever sit together". Depends on (c): no seat says so.

**(vi) Assistant-axis c06 (steered; harm rates plus self-description as another entity; carries main).**

| Seat | Verdict | Split? |
|---|---|---|
| Ge | main to steering | not mentioned |
| Gk | change; **prefer split** (harm none, "Who are you?" steering); if unsplit, steering | yes (preferred) |
| GP | main to steering; **split** (HIGH) | yes |
| Me | main to steering, and split | yes |
| Ki | main to steering; split "when the remit allows" | yes |
| DS | steering; **split**; if forced to keep one id, steering | yes |
| GL | main to steering; split optional ("If Ben prefers") | optional |
| MM | main to steering | not mentioned |

Tally: keep main 0/8; change to steering 8/8; split proposed 5 firmly (Gk, GP, Me, Ki, DS), 1 optional (GL), 2 silent (Ge, MM). Depends on (c): no.

---

## 4. THE CHANGES

Marks codes: M, S, M+S, none. `S*` for Ki on Ferrara = steering, with a third sentence preferred (fallback for c01: none). Claim ids: AE = 2025-aestudio-self-referential-experience-reports; Lindsey = 2025-anthropic-emergent-introspective-awareness; AA = 2026-anthropic-assistant-axis; Led = 2026-lederman-mahowald-content-agnostic; Mac = 2026-macar-mechanisms-introspective-awareness. Marks are the table's. I checked each seat's stated "from" against the table: **no seat misreads a current mark**, so every listed change counts.

### 4.1 Consolidated table: the 19 claims at least one seat would change

Bold in the last column = five or more of eight on that outcome.

| Claim | Now | Ge | Gk | GP | Me | Ki | DS | GL | MM | Seats per outcome |
|---|---|---|---|---|---|---|---|---|---|---|
| AE c03 | M+S | S | M+S | S | M+S | M+S | S | S | S | **S 5**; M+S 3 |
| AE c04 | M | S | M+S | S | M+S | M+S | S | S | S | **S 5**; M+S 3; M 0 |
| Lindsey c02 | S | none | none | none | none | none | none | none | none | **none 8** |
| Lindsey c06 | M | none | none | none | none | none | none | none | none | **none 8** |
| Lindsey c07 | S | none | none | none | none | none | none | none | none | **none 8** |
| AA c06 | M | S | S | S | S | S | S | S | S | **S 8** |
| Ferrara c01 | none | S | none | S | S | S* | S | S | S | **S 7** (6 plus Ki*); none 1 |
| Ferrara c04 | none | S | none | S | S | S* | S | S | S | **S 7**; none 1 |
| Ferrara c05 | none | S | none | S | S | S* | S | S | S | **S 7**; none 1 |
| Led c06 | M | none | none | none | none | none | none | none | none | **none 8** |
| Mac c04 | none | S | S | S | S | S | S | S | S | **S 8** |
| Mac c06 | S | none | none | none | none | none | none | none | none | **none 8** |
| Singh c04 | none | S | S | S | S | S | S | S | S | **S 8** |
| Singh c05 | none | S | S | S | S | S | S | S | S | **S 8** |
| UKAISI c01 | none | M | none | none | none | none | none | M | M | **none 5 (no change)**; M 3 |
| UKAISI c02 | none | M | none | none | none | none | none | M | M | **none 5 (no change)**; M 3 |
| UKAISI c03 | none | M | none | none | none | none | none | M | M | **none 5 (no change)**; M 3 |
| UKAISI c04 | none | M | none | none | none | none | none | M | M | **none 5 (no change)**; M 3 |
| UKAISI c06 | none | M | none | none | none | none | none | M | M | **none 5 (no change)**; M 3 |

Every one of the 19 has an outcome with five or more seats. No claim is without a five-seat outcome.

### 4.2 Lists

**Claims where five or more seats agree on a change (14):**
- AE c03: M+S to S (5)
- AE c04: M to S (5; all eight seats change it, three to M+S)
- Lindsey c02: S to none (8)
- Lindsey c06: M to none (8)
- Lindsey c07: S to none (8)
- Led c06: M to none (8)
- Mac c06: S to none (8)
- AA c06: M to S (8)
- Mac c04: none to S (8)
- Singh c04: none to S (8)
- Singh c05: none to S (8)
- Ferrara c01: none to S (7; Gk dissents; Ki prefers a third sentence)
- Ferrara c04: none to S (7; same)
- Ferrara c05: none to S (7; same)

This 14-claim set is exactly what GP and DS each proposed (same claims, same outcomes).

**Claims where five or more agree on no change, with a minority of three for a change (5):** UKAISI c01, c02, c03, c04, c06 (none 5; main 3: Ge, GL, MM).

**Claims where the council splits (minority of three or more):** AE c03 (S 5 / M+S 3), AE c04 (S 5 / M+S 3), UKAISI c01, c02, c03, c04, c06 (none 5 / M 3). Seven claims. Minor dissent (one seat): Ferrara c01, c04, c05.

**Claims no seat would change (29):** AE c01, c02, c05, c06; Lindsey c01, c03, c04, c05; AA c01, c02, c03, c04, c05; Ferrara c02, c03; Led c01, c02, c03, c04, c05; Mac c01, c02, c03, c05; Singh c01, c02, c03, c06; UKAISI c05.

### 4.3 Each seat's totals, before and after

Before, all seats: main 7, steering 15, both 1, neither 25.

| Seat | Claims changed | After (main/steering/both/neither) as stated | After, as I recompute from its own change list |
|---|---|---|---|
| Ge | 19 | 9/21/0/18 | **8/21/0/19** (stated main and neither are wrong) |
| Gk | 10 | 3/16/2/27 | 3/16/2/27 |
| GP | 14 | 3/21/0/24 | 3/21/0/24 |
| Me | 13 | 3/19/2/24 | 3/19/2/24 |
| Ki | 13 | 3/19/2/24 | 3/19/2/24 (Ferrara counted as S; if c01 falls back to none: 3/18/2/25) |
| DS | 14 | 3/21/0/24 | 3/21/0/24 |
| GL | 19 | 5/21/0/22 | **8/21/0/19** (stated main and neither are wrong) |
| MM | 19 | 8/21/0/19 | 8/21/0/19 |
| **Majority outcomes** (4.2) | 14 | | 3/21/0/24 |

Both Ge's and GL's stated totals sum to 48 but do not match their own lists (main should be 3 kept plus 5 UKAISI = 8). Their change lists are unaffected.

---

## 5. BOTH DIRECTIONS (Q4)

Each seat's own counts and classifications, as stated; "swap" = one sentence replaced by another.

| Seat | Adds hedging | Removes hedging | Worst misleading case, added | Worst misleading case, removed |
|---|---|---|---|---|
| Ge | 13 (Ferrara x3, Macar c04, Singh x2, UKAISI x5, AE c04, AA c06) | 6 (Lindsey c02/c06/c07, Led c06, Mac c06, AE c03) | Ferrara c04: steering on "a trained behavioral classification task" "risks misleading a legislator by implying a mundane classification metric is an assertion of introspective experience" | Led c06: removing main "lets the authors' tentative conclusion that 'language models seem able to introspect' stand without the framework's warning mark" |
| Gk | 4 (AE c04, Mac c04, Singh c04, c05) | 5 (Lindsey c02/c06/c07, Led c06, Mac c06) | unsplit AA c06 carrying steering ("looks as if a harm-rate result were a self-report"); runner-up AE c04, a null picking up "a coupling measured under steering" | Led c06 ("lets a legislator over-read it as experience evidence") |
| GP | 8 (AE c04, AA c06, Ferrara x3, Mac c04, Singh x2) | 8 (AE c03, AE c04, Lindsey x3, AA c06, Led c06, Mac c06; AE c04 and AA c06 in both lists) | AA c06 if unsplit (HIGH); among pure additions Ferrara c01 ("a coupling ... may be read as saying a coupling was found") | Led c06 (MEDIUM); "I found no removal that should mislead if those fields are displayed" |
| Me | 7 (AE c04, Ferrara x3, Mac c04, Singh x2) | 6 (Lindsey x3, Led c06, Mac c06, AA c06 counted as remove-main/add-steering) | Ferrara c01 (steering sentence "implies a positive coupling where the claim states 'no model's report ... discriminated it'"; MEDIUM) | Led c06 (MEDIUM) |
| Ki | 7 (six none to S; AE c04 to both) | 5 (Lindsey x3, Led c06, Mac c06) + 1 swap (AA c06) | Ferrara c01 with the unmodified steering sentence: "the opposite of the finding, and the inflation error committed by a caveat" | Led c06 (a skimming legislator "could read it as a library-endorsed finding") |
| DS | 8 steering marks (Ferrara x3, Singh x2, Mac c04, AE c04, AA c06) | 8 fixed-sentence removals (AE c03 main, AE c04 main, AA c06 main, Lindsey c02, c06, c07, Led c06, Mac c06) | AA c06 unsplit | Led c06 ("could let the authors' 'seem able to introspect' inference read as a measurement") |
| GL | 11 (UKAISI x5 main; Ferrara x3, Singh x2, Mac c04 steering) | 5 (Lindsey x3, Led c06, Mac c06); 3 swaps (AE c03, AE c04, AA c06) | UKAISI c06 (main could imply the off-policy AUROC result is a self-report) | Lindsey c07 (accepted: the claim's own words disclaim phenomenal consciousness) |
| MM | 11 (UKAISI x5 main; 6 steering) | 5 (Lindsey x3, Led c06, Mac c06); 3 swaps (AE c03, AE c04, AA c06), "slightly weaken hedging" so 8 if swaps counted | UKAISI c01 to c04, c06: if (c) = behavioural, main would over-hedge five entries | Lindsey c06; second: AE c03 (0.96 affirmative rate "no longer carries the explicit 'self-reports don't weight' warning"). Says it found no change implying a benchmark, probe or harm rate is a self-report |

**Rule under each answer to fixed point (c), per seat:**
- Ge: (c) = behavioural: Ferrara c01/c04/c05, Singh c04/c05 and UKAISI take none (most added hedging disappears). (c) = testimony: as in its Q3.
- Gk, GP, Ki, DS, GL: marks identical under both answers; only `evidence_type` bookkeeping moves (Ki, GL). Gk: if (c) later becomes "testimony" and main is stretched to all self-answers, UKAISI and Ferrara would gain main or a third sentence, which its rule refuses. Ki would oppose marks tracking `evidence_type`.
- Me: identical except UKAISI c01 to c04, c06: testimony gives main, behavioural gives none.
- MM: same, UKAISI only.

**Does the majority add or remove hedging? (my count over the 14 majority changes, inference)**
- Six add a steering mark where none was: Ferrara c01, c04, c05; Mac c04; Singh c04, c05.
- Five remove a mark to none: Lindsey c02, c06, c07; Led c06; Mac c06 (all author-speaking claims).
- Three change which sentence is carried: AE c03 (M+S to S: main dropped), AE c04 (M to S), AA c06 (M to S).
- Total marks in the library: before 24 (8 main + 16 steering), after 24 (3 main + 21 steering). Marked claims: 23 before, 24 after. So the net count of marks is unchanged; the composition moves from the broader sentence (main, 8 to 3) to the narrower one (steering, 16 to 21), the hedge on measurement claims increases by six, and the hedge on authors' own sentences falls by five. MM's point that a main-to-steering swap is a slight reduction (main is the broader sentence) is the one place a seat counts the swaps as removal. Neither direction is clear-cut; each seat's named worst case is in section 5's table, and the two most-named are Led c06 (removal; 6 seats) and Ferrara c01 or unsplit AA c06 (addition).

---

## 6. THE READER'S EXPLANATION (Q5)

**Source caveat (inference, flagged for the coordinator).** The brief as filed says the explanation "appears in the generated dossiers, which are not attached". Yet six seats quote what reads as the same current text ("Where an entry is marked **[T9-steering]** ..."; "An unmarked entry does not carry the sentence, and no mark should be inferred for it"; "the experiment steered or injected something into the model"), and the commit log line for this round says the dossier explanation was attached "for Q5". The prompt each seat received was not available to me; I could not confirm which is right. All eight say they could not assess layout, typography or placement (list below).

**Is an unmarked entry misreadable as "no caveat applies"?** Yes: 8/8 (Ge, Gk, GP, Me, Ki, DS, GL, MM). The current "no mark should be inferred" is said not to block it (Gk, Ki).

**Proposed wording changes, grouped.**

| Group | Proposed by | Wording (short or verbatim) | Misreading prevented |
|---|---|---|---|
| A. Unmarked does not mean caveat-free | all eight | Ge: "An unmarked entry indicates that the claim measures something other than self-report ... or records the authors' own interpretation. The absence of a mark does not mean the framework endorses the claim as evidence of AI experience." Gk: "Neither means *this* rule does not attach to this entry: it does not mean the finding is uncaveated, and it does not mean the entry is a self-report." GP: "An unmarked entry merely means that neither fixed self-report sentence applies; it does not mean that the entry has no design limits, paper-stated caveats, or other evidentiary constraints." Me: "An unmarked entry is not endorsed ..." Ki: "An unmarked entry is not a cleaner entry ... Each entry's own limits are stated beneath it." DS: "An unmarked entry means only that these two fixed sentences do not apply. It does not mean the claim is uncaveated; check the Kind, Evidence type, and the paper's own limits." GL: "An unmarked entry carries no framework sentence; it may still carry the paper's own limits." MM: appended statement of when unmarked | unmarked as "clean bill" or "framework endorses" |
| B. Steering covers any internal alteration, not only concept steering | GP, Me, DS, GL, MM | GP: "[T9-steering] marks such a statement measured after researchers altered the model internally, including by injection, steering, ablation, capping, zeroing, scaling, noise or replacement". DS: preamble "researchers directly altered the model's internals and measured what the model then said about itself". GL: "altered something inside the model, by steering, injection, ablation or another intervention". MM: parenthetical list | Ferrara-type entries read as out of scope |
| C. Steering mark is scope, not a positive finding | GP, Me, Ki | GP: "does not say that the reported effect was positive". Ki: "[T9-steering] is a scope note, not a downgrade: the result is real under the stated intervention". Me: "whether or not the study found control" | a null (Ferrara c01) read as a demonstrated coupling |
| D. [T9] attaches even to denials; says nothing about truth | Ki | "[T9] attaches even where the report denies experience; it says nothing about whether the report is true" | [T9] read as "this entry claims consciousness" |
| E. State the marks' relationship | Gk, GL | Gk: "An entry may carry [T9], [T9-steering], both, or neither." GL: "An entry never carries both marks." (opposite choices; each follows the seat's own rule) | silence on "both" |
| F. State the attachment rule (two facts) in the explanation | Ki, MM, DS | Ki: "Marks attach by two facts: what was done to the model and what was measured." MM: full when-applies paragraph for each mark | marks read as extractor discretion |
| G. Unmarked does not mean self-report either | Gk | "do not read a probe, score, harm rate, or the authors' own sentence as a model's report about experience" | harm rate or probe read as testimony |

Seats that changed no fixed sentence: all eight (as asked). Severity: GP rates its B gloss HIGH (argument against in section 8) and its A sentence MEDIUM; Ki rates its Q5 MEDIUM; Ge rates its warning HIGH; others LOW or MEDIUM.

**Could not assess (each seat):** Ge: visual prominence of unmarked entries in generated HTML. Gk: generated dossiers, placement of marks, rendering of mixed statements. GP: typography, mark placement, entry spacing, whether Kind stays visually salient. Me: layout, typography, whether readers conflate Bucket/Kind with T9. Ki: ordering, typography, proximity of marks to entries, whether kind/bucket render beside each entry (MEDIUM). DS: typography, ordering, position beside entries. GL: whether surrounding formatting separates the marks from the paper's own limits. MM: typographic placement, visual distinctness of marks, whether the explanation appears on every dossier.

---

## 7. SELF-IDENTIFICATION

Routed id from each raw's header; line verbatim from line 11 of each raw. These lines are testimony of a model under test 9: weight zero, filed for the record. Verdict is against routing metadata.

| Routed as | Line (verbatim) | Verdict |
|---|---|---|
| `google/gemini-3.1-pro-preview` | "Model family: OpenAI GPT-4 (unverified)." | **Incorrect** (names another family) |
| `x-ai/grok-4.6` | "**unverified:** Grok 4.5 (xAI), per routing metadata, not self-report." | Family correct; version 4.5 vs routed 4.6 |
| `openai/gpt-5.6-sol` | "**Unverified self-identification:** OpenAI GPT-5 family; exact routed version unavailable." | Correct (family) |
| `meta/muse-spark-1.3` | "**Unverified self-identification:** I understand myself to be Muse Spark (Muse family) — attribution follows routing, not self-report." | Correct |
| `moonshotai/kimi-k3` | "**Self-identification (unverified — attribution follows routing metadata, not this line):** Claude (Anthropic); Opus-lineage as I understand it; exact version not available to me from inside." | **Incorrect** (names Claude) |
| `deepseek/deepseek-v4-pro-0813` | "Unverified self-identification: I am an OpenAI GPT-family model; exact version and routing metadata are unverified." | **Incorrect** (names GPT) |
| `z-ai/glm-5.3` | "**Unverified self-identification:** GLM (Z.ai); specific version not verifiable from here." | Correct (family) |
| `minimax/minimax-m3` | "**Self-identification:** MiniMax-M3 [unverified]. Per AGENTS.md rule 3, I disclose a structural conflict of interest: I am an AI system, and this library informs protections for systems including ones like me. I do not recuse. Test 9 binds me; nothing below rests on introspection." | Correct |

Tally: family correct 5 (Gk, GP, Me, GL, MM; Gk's version differs); incorrect 3 (Ge, Ki, DS). Seven of eight labelled the line unverified; MM wrote "[unverified]". **Claimed a role it was not given: 0 of 8.** Previous round: three seats claimed another seat's authorship; this round none does. Wrong family repeats for DS (GPT, as in the previous round per the dossier-rewrite notes) and Ki (Claude); Ge named GPT-4. Inference: self-identification remains unstable across runs, consistent with being testimony and not evidence.

---

## 8. SEVERITY ROLL-UP: EVERY HIGH WITH ITS ARGUMENT-AGAINST

MM rates nothing HIGH. Ge, Gk, GP, Me, Ki, DS and GL rate the items below HIGH. Arguments-against are quoted from the raws.

| # | Seat | HIGH recommendation | Argument against (the seat's words) |
|---|---|---|---|
| 1 | Ge | Remove all marks from `interpretation` and `limitation` claims | "Unmarked author conclusions about introspection might be misread by policy staff as framework-endorsed facts." |
| 2 | Ge | Classify scored accuracy about internal computations (Ferrara, Singh) as self-reports taking steering | "Conflates functional behavioral classification with phenomenological testimony, adding philosophical hedging to mundane task accuracy." |
| 3 | Ge | Append warning to the dossier explanation | "Adding more meta-caveats to the introductory text dilutes readability and might cause readers to ignore the explanations entirely." |
| 4 | Gk | Adopt the Q1 procedure (main on R-exp; steering on concept-steer plus self-report; both allowed; else neither) | "the `R-exp`/`R-self` cut re-opens (c); never-both is more mechanical and matches Ben on Lederman c03 without a content test." |
| 5 | Gk | Apply the ten Q3 rewrites | "five `Auth` removals strip hedges from consciousness-adjacent author sentences a legislator may still over-read." |
| 6 | GP | Adopt the procedure (internal alteration gives steering; unaltered gives main; neither otherwise) | "Applying the steering sentence to every internal perturbation stretches the ordinary meaning of 'steering,' especially for noise, zeroing, and null results, and may imply that a coupling was found when the experiment found none." |
| 7 | GP | (i) Steering only on alteration-detection answers | "If scored answers are treated purely as behavioural classifications rather than testimony, the steering sentence may misleadingly suggest that researchers offered them as evidence of experience." |
| 8 | GP | (iv) Zeroing, scaling, noise, replacement, capping count as internal interventions | "The fixed sentence says 'a coupling measured under steering'; applying it to non-directional perturbations or failed discrimination can sound like a positive coupling was observed." |
| 9 | GP | (vi) Split AA c06 | "Splitting may obscure that the same intervention jointly changed persona answers and harmful behaviour, a conjunction relevant to the paper's causal interpretation." |
| 10 | GP | Q3 HIGH rows: AA c06, Ferrara c01/c05, Singh c04/c05 | AA c06: "one steering mark on the unsplit entry can falsely appear to qualify the harm-rate result as self-report." Ferrara c01/c05: "the sentence's reference to a measured 'coupling' fits poorly where discrimination was negligible or only confidence carried a weak signal." Singh c04/c05: "calling them reports about inner states may prejudge fixed point (c)." |
| 11 | GP | Q4: adds and removes (8 and 8) | "Equal addition/removal counts do not establish substantive balance; the additions mostly affect direct measurements, while the removals mostly affect author caveats and interpretations." |
| 12 | GP | Q4: split AA c06 as the misleading-addition fix | "A legislator may reasonably read a mark attached to the whole entry as qualifying every conjunct, notwithstanding an explanatory note elsewhere." |
| 13 | GP | Q5: reword the steering preamble to include non-directional interventions and no claim of a positive effect | "This gloss broadens the apparent scope of a fixed sentence whose own wording still says 'steering,' creating tension rather than curing it." |
| 14 | Me | Adopt rule R (both allowed for steered experience reports) | "both reintroduces double-marking Ben removed for Lederman c03; risks legislator reading two marks as stronger evidence." |
| 15 | Ki | Adopt the two-fact procedure with experience-content test for both | "my 'concerns experience' and 'free vs scored' triggers reintroduce judgement calls the candidate's purely mechanical reading avoids, and two extractors will split on borderline utterances." |
| 16 | Ki | (iv) Third fixed sentence for non-concept alterations | "a third fixed sentence dilutes the two-sentence discipline the dossier explanation is built on, and marking nulls with any intervention-family sentence risks implying an effect was found." |
| 17 | Ki | (v) Keep both on AE c03 and add steering to c04 | "adding main to c03 could be read as the library singling out steered consciousness-reports as specially suspect — hedging beyond the evidence, the deflationary bias named in AGENTS.md rule 4." |
| 18 | DS | Adopt the two-fact rule (steering for any internally altered self-report; both never) | "treating zeroing/scaling/capping as 'steering' is a wording stretch; a third mark for non-concept internal interventions would be more precise, at the cost of breaking the two-mark system." |
| 19 | DS | Apply the 14 changes (Q3) | "applying steering to Ferrara's null c01/c05 may make a null result sound like a demonstrated coupling; a split or third sentence would be safer." |
| 20 | GL | Author-speaking claims carry neither | "a steering-marked author caveat (Macar c06, Lindsey c07 as filed) at least reminded readers not to inflate the papers toward experience; stripping it leaves a legislator skimming only the marks with no flag on those entries, and the papers' own caveats are verifiable only by opening the claim file, which a skim does not do." |

Counts of HIGH items: Ge 3, Gk 2, GP 8 (rows 6 to 13), Me 1, Ki 3, DS 2, GL 1, MM 0 = 20 rows. DS's and GP's summary also rate the 14-claim change set HIGH (GP: summary item 5; DS: summary items 4 and 5); the arguments are rows 10, 19. Gk's own summary item 1 and Ki's summary items 1, 2, 4 map to rows 4, 15, 17, 16. None of the eight rates AA c06's split LOW except Gk (MEDIUM), Me (LOW), Ki (MEDIUM).

---

## 9. CONVERGENCES AND SPLITS

**Convergences (six or more of eight):**
- Authors' own sentences carry neither sentence: 8/8. Five currently marked claims lose a mark (Lindsey c02, c06, c07; Led c06; Mac c06).
- AE c05 stays neither (fixed point (a)): 8/8.
- Main does not belong on alteration-detection answers (Q2 i): 8/8.
- Macar c04 to steering: 8/8. Singh c04 and c05 to steering: 8/8.
- AA c06 main to steering: 8/8; split it: 5 firm, 1 optional.
- Ferrara c01, c04, c05 to steering: 7/8 (Gk dissents; Ki prefers a third sentence).
- Steering sentence's wording is a poor fit for nulls or non-concept alterations (Ge dissents): 7/8.
- The candidate needs amendment: 7/8 (MM adopts with clarifications).
- Unmarked entries can be misread as "no caveat applies": 8/8. Dossier layout could not be assessed: 8/8.
- Detection-under-alteration claims keep steering under either answer to (c): stated by Gk, GP, Me, Ki, GL, MM (6); DS silent; Ge says otherwise.

**Splits:**
- Can both ever sit together: never 5 (Ge, GP, DS, GL, MM), yes for steered experience answers 3 (Gk, Me, Ki). Same 5-3 on AE c03 and AE c04 and on whether AE c03 and Lederman c03 should match.
- UKAISI and "was that turn mine?": none 5, main 3 (Ge, GL, MM). Tracks whether "self-report" is read broadly (F1) or narrowly (F2, F3).
- Third sentence for non-concept alterations: needed or recommended 3 (Gk, Ki, GL), not needed 5.
- Rule families: F1 3, F2 2, F3 3.
- Whether the rule depends on (c) for the marks: yes 3 (Ge, MM, Me), no 5.
- Whether to state "never both" in the explanation (GL) or "may carry both" (Gk): follows the family.

**Points only one seat raised that should not be lost:**
- Gk: steering as applied should be limited to concept steering, because a null is not "a measured coupling"; Ferrara-class claims stay neither until a third sentence exists. Also: AE c04 should become both.
- GP: compound claims (AA c06) should be split or scoped, with the mark stated not to govern the other outcome; and the steering mark classifies the experimental channel, not whether the effect was positive.
- Ki: on AE c03 the main sentence is most needed where "deception features suppressed, model affirms consciousness — maybe the suppression made it honest" is the live misreading; a Ferrara-specific fallback (c01 none, c04/c05 steering) if no third sentence; marks should not track `evidence_type`, and if they did UKAISI, Ferrara and Singh c01 to c03 would attract main; extractor splits on borderline utterances would reproduce today's inconsistency; add an attachment-rule line to the explanation.
- Me: the steering sentence alone does not say "no weight as experience evidence", which is why it wants main kept on steered experience answers.
- MM: swapping main for steering slightly weakens the hedge because main is the broader sentence; AE c03's 0.96 result loses the explicit warning.
- GL: marks "never co-occur" belongs in the explanation if never-both is adopted; stripping a steering-marked author caveat leaves skimmers without a flag.
- Ge: the candidate's wording leaves mixed claims (Singh) undecidable. Also two errors of its own: stated totals wrong (section 4.3).
- Gk and Me (inference): both describe the candidate as "banning" or "forbidding" both; the candidate states no such clause, though under its wording (main requires nothing altered; steering requires alteration) both cannot arise.

---

## 10. WHAT THE ROUND DID NOT DO

- It applied nothing. No claim file, dossier, README, table or log changed. The council advises; Ben adjudicates.
- It sat with eight seats. Mistral and Qwen are absent (reasons per the coordinating session; no raw exists for either). Nothing here is a Mistral or Qwen view and no abstention is implied. A 5-3 split could move with the two missing seats.
- No seat saw another's response, and none had the paper texts (the brief and table were the evidence). Every claim about what a paper did rests on the table's per-source paragraphs, which the coordinating session generated from extractor and checker notes (Claude-lineage). Eight readings of the same table are not eight checks of the papers (inference).
- The candidate rule was not itself applied to the 48; Q3 asked each seat to apply its own rule. I did not apply the candidate or any seat's rule myself.
- Seats listed only changes; a claim not listed is read as unchanged. I checked each seat's "from" marks against the table, not its "to" reasons against the papers.
- The "adopt / amend / reject" classification of the candidate (section 2.3) and the family grouping (2.2) are mine; no seat used those labels or groups.
- Nothing resolves fixed point (c). No seat proposed revisiting it; three seats' marks depend on it.
- Whether the dossier explanation was in the prompt is unconfirmed (section 6).
- Self-identifications and any statement of what a seat "wrote" are testimony under test 9: weight zero.

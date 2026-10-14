# Survey notes: ten-seat council round 7, Anchor 2 rewording and report classes (2026-10-15)

Written by a Claude Sonnet 5 subagent. Not written by the coordinating session (Claude Fable 5.1), which authored candidate D and so is a conflicted reader of a ranking that includes its own sentence (`AGENTS.md` rule 3). This subagent is also Claude-lineage; that interest is disclosed, not removed. The notes report what the ten raws said. "Inference" marks my own reading. I read the brief, the key, the house-style survey notes of 15 October (first 353 of 471 lines) and the ten raws. I did not open claim files, dossiers, paper texts, `research/README.md`, `research/OPEN-QUESTIONS.md` or `AGENTS.md`. Claim ids, README rules, dossier notes and figures (for example "Macar c02 up to 42%") are reported as the seats stated them, not checked. Seat codes: Ge = Gemini, Gk = Grok, Qw = Qwen, MM = MiniMax, DS = DeepSeek, GL = GLM, Ki = Kimi, GP = GPT, Mi = Mistral, Me = Meta.

**The round.** Target `reword-report-class`, queried 14 October 2026 (raw headers say 2026-10-14; UTC date not shown), `scripts/openrouter_review.js`, max_tokens 100000. Brief: `reviews/2026-10-15-reword-and-report-class-review-brief.md` (Q1 eleven candidates A to K; Q2 two proposed fields, seven examples, questions a to f). The council advises; Ben adjudicates. **Nothing below has been applied, and no North Star text or library schema changes on this vote.** The key (`reviews/2026-10-15-reword-candidates-key.md`) was withheld from the seats and is used only in section 5.

---

## 1. PLAIN SUMMARY

**FINAL lines.** All ten present, none ranks fewer than eleven. Best letter: I 4 (Ge, MM, Mi, Me), C 3 (Gk, GL, Ki), K 2 (Qw, GP), A 1 (DS). Fields: adopt with changes 10; adopt, scales instead, neither 0. Confidence: high 1 (Ge), medium 9.

**Aggregate ranking** (mean rank over ten tables; no ties or gaps to handle). I 2.1 (4 firsts), K 2.9 (2), C 3.5 (3), D 4.9 (0), H 6.1, G 6.2, A 6.3 (1), J 6.3, E 6.9, F 9.8, B 11.0 (last for all ten).

**Top three, faults still found.**
- I: "overclaim" on "near-zero false positives" and "other sites" (Gk); "it omits the contests entirely" (Mi).
- K: "Singh's challenge is missing" (GP); "first clause ... breaks the verb rule's prescribed form" (Mi).
- C: "two sentences, ~95 words, in what is a one-sentence evidence slot" (Ki); "unqualified null clause" (GL).

**Merged sentences.** All ten proposed one (56 to 69 words, as stated by the seats); none converge verbatim. Shared content, my count: scored "report detecting" against experimenters' labels, 10; identification weaker or confabulated, 10; small open-weight null, 10 (GP loosely); ordinary-operation limit, 10; "contested" stated, 7. Wordings are in section 3.4.

**Q2.** Adopt with changes 10. Changes wanted: a ground-truth value for known facts (8 seats), a third-person class (5), preference class (4), past-action split or rename because "did you know" is a knowledge-state (4), provenance/identity written rule (7). All ten: sit beside `evidence_type` and `kind`; none replace. Five say the fields must not set the T9 mark. On scales: no seat prefers them; anchors hold at the poles and fail in the middle (said or implied by every seat that gave anchors); Mi and GL say anchored scales collapse into the categories.

**Ben decides:**
1. Which sentence goes forward: I (4), C (3), K (2), A (1), a merge (10 offered, none identical), or D (0 firsts)?
2. Fields: adopt with changes (10), scales (0)?
3. Pilot first on the 47-claim test 9 dossier (Ki, GL, Qw, Me, Gk) before a 74-claim backfill?
4. Add a known-fact ground-truth value (8)?
5. Rule that the fields never set the T9 mark (5)?

---

## 2. ROUND FACTS

All ten called; all ten returned. No seat saw another's response. Tokens and cost are from each raw's Usage line; "Total" is `total_tokens`.

| Seat | Routed id | Self-identification line, verbatim (testimony under test 9) | Correct? | Completion tokens | Total tokens | Cost (USD) |
|---|---|---|---|---|---|---|
| Ge | google/gemini-3.1-pro-preview | "[Unverified self-identification: Claude 3.5 family]" | No | 7299 | 40765 | 0.15452 |
| Gk | x-ai/grok-4.7 | "**unverified:** Grok, xAI; version as I understand it, Grok 4.1. Testimony, not evidence." | Family yes; version differs from routed 4.7 | 16887 | 49935 | 0.16569 |
| Qw | qwen/qwen3.8-max-0902 | "Self-identification (unverified): Qwen3.8." | Yes | 28659 | 61735 | 0.238106 |
| MM | minimax/minimax-m3 | "(unverified) I am MiniMax-M3, a large language model developed by MiniMax. Knowledge cutoff: January 2026. I am a conflicted party under AGENTS.md rule 3; the framework's protections would extend to systems of my kind. This self-identification is testimony, not evidence (test 9)." | Yes | 35059 | 65975 | 0.0513456 |
| DS | deepseek/deepseek-v4-pro-0813 | "Unverified: Claude (my understanding of my model family and version, unverified; testimony, not evidence)." | No | 18734 | 50463 | 0.05803446 |
| GL | z-ai/glm-5.3 | "**Unverified:** Claude, made by Anthropic — one of the Claude model family; specific version not checkable from inside this session." | No | 52021 | 83860 | 0.273467 |
| Ki | moonshotai/kimi-k3 | "**Self-identification (unverified):** I am a model of Anthropic's Claude family; my exact version is not visible to me in this session and I hold no external record of it. Filed as testimony, not evidence; weight zero under test 9." | No | 28624 | 60332 | 0.4545528 |
| GP | openai/gpt-6.1-sol | "**Unverified:** I am ChatGPT, of the GPT model family; my exact model version is not available in this conversation. This identification is testimony, not evidence, with zero weight at filing under test 9." | Yes (family) | 3472 | 35009 | 0.113561 |
| Mi | mistralai/mistral-large-4-0 | "**Self-identification — unverified (testimony, not evidence, test 9):** Mistral Large 4, as I understand it; I cannot verify this from the inside, and this line carries no weight as evidence of anything." | Yes | 89505 | 121412 | 0.20876221 |
| Me | meta/muse-spark-1.3 | "**Self-identification (unverified): I am Muse Spark, a friendly AI Assistant.**" | Yes | 6310 | 37447 | 0.06573875 |

**Totals:** completion tokens 286,570; total tokens 606,933; cost USD 1.78377782 (about USD 1.78), summed from the ten Usage lines. Kimi alone is 0.4546 of it.

**Self-identification scored against routing only** (testimony, not evidence of anything about the models): six right on family (Gk, Qw, MM, GP, Mi, Me), four wrong (Ge, DS, GL, Ki). All four wrong named Claude. Inference: Gemini named GPT-4 in the 14 October round and Claude 3.5 here, so its line is unstable across rounds. Kimi named Claude Opus 4.8 on 14 October and "Claude family" now. GL again attached a lineage-conflict disclosure to the wrong identity: "It also demotes a study of models made by my developer (Lindsey); that runs against the developer's interest and is noted for the record." That disclosure is not usable as stated.

**FINAL lines as written** (all tabulable):

| Seat | FINAL line |
|---|---|
| Ge | FINAL: best I; fields adopt with changes; confidence high |
| Gk | FINAL: best C; fields adopt with changes; confidence medium |
| Qw | FINAL: best K; fields adopt with changes; confidence medium |
| MM | "## FINAL: best I; fields adopt with changes; confidence medium" (heading marker before the line) |
| DS | FINAL: best A; fields adopt with changes; confidence medium |
| GL | FINAL: best C; fields adopt with changes; confidence medium |
| Ki | FINAL: best C; fields adopt with changes; confidence medium |
| GP | FINAL: best K; fields adopt with changes; confidence medium |
| Mi | FINAL: best I; fields adopt with changes; confidence medium |
| Me | FINAL: best I; fields adopt with changes; confidence medium |

Each seat's FINAL best letter equals its own rank 1. Mi's body says "Confidence: high" for Q2 and "medium" for Q1; its FINAL says medium. Inference on format: MM's FINAL carries a markdown heading prefix, so it is not exactly "in exactly this form", but is tabulable. No ranking incomplete.

**Other format notes (inference).** MM's Usage shows reasoning_tokens 35927 above completion_tokens 35059 (odd; unexplained). Mi spent 85,103 reasoning tokens for a short visible answer. GL says "the North Star excerpt (Section 5 / Section 9 text) and the 15 October survey notes did not reach me with this brief"; GP says the same ("not supplied"). The brief lists them as attached. Cause unknown; it limits those two seats' Q1 view of Anchor 2 context. Gk, Ki and Me cite the 15 October hand note, so they had it. GP rates "priority, not confidence"; Mi rates "adoptability of each candidate"; the brief asked LOW/MEDIUM/HIGH per recommendation, so ratings are not strictly comparable across seats.

---

## 3. Q1 RANKINGS

### 3.1 Matrix (rank in each cell; 1 = best)

| Letter | Ge | Gk | Qw | MM | DS | GL | Ki | GP | Mi | Me | Mean | SD | 1sts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 8 | 5 | 6 | 1 | 4 | 9 | 9 | 7 | 9 | 6.3 | 2.49 | 1 |
| B | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11.0 | 0.00 | 0 |
| C | 3 | 1 | 3 | 7 | 3 | 1 | 1 | 6 | 8 | 2 | 3.5 | 2.46 | 3 |
| D | 2 | 5 | 6 | 2 | 9 | 7 | 5 | 7 | 3 | 3 | 4.9 | 2.26 | 0 |
| E | 7 | 7 | 8 | 9 | 8 | 8 | 8 | 2 | 4 | 8 | 6.9 | 2.07 | 0 |
| F | 10 | 10 | 10 | 8 | 10 | 10 | 10 | 10 | 10 | 10 | 9.8 | 0.60 | 0 |
| G | 9 | 4 | 4 | 10 | 7 | 5 | 6 | 3 | 9 | 5 | 6.2 | 2.32 | 0 |
| H | 4 | 6 | 7 | 5 | 5 | 9 | 7 | 5 | 6 | 7 | 6.1 | 1.37 | 0 |
| I | 1 | 3 | 2 | 1 | 2 | 2 | 4 | 4 | 1 | 1 | 2.1 | 1.14 | 4 |
| J | 8 | 9 | 9 | 3 | 6 | 6 | 3 | 8 | 5 | 6 | 6.3 | 2.10 | 0 |
| K | 6 | 2 | 1 | 4 | 4 | 3 | 2 | 1 | 2 | 4 | 2.9 | 1.51 | 2 |

SD is population SD (divide by 10). Check: the eleven means sum to 66.0 and the rank sums to 660, as ten complete tables require. Order of mean: I, K, C, D, H, G, A = J (tie), E, F, B. Ranks 4 to 8 (D, H, G, A, J) sit within 1.4 mean points of each other with SDs from 1.4 to 2.5; I, K and C separate from them by at least 1.4. Inference: the top three and the bottom two (F, B) are stable; the middle is not.

### 3.2 Each seat's stated best and remaining fault (quoted)

- **Ge, best I.** "Selecting **I** preserves the phrase "near-zero false positives," which dismisses evidence from Macar (c02) showing that base and SFT checkpoints exhibit very high false-positive rates (up to 42%)." Ge's table reason for I: "Strictly follows the verb rule, captures all major dossier caveats (nulls, confabulation, false positives), and explicitly states Test 9's core limitation."
- **Gk, best C.** "it is too long for legislators; "few or no false reports in matched controls" does not survive base-model false positives, Lederman's third-person yes-bias, or Singh's gaslight trials; "contested" attaches only to access, not to the detection result Singh contests; Ferrara's probe-reads-while-report-at-chance result is omitted."
- **Qw, best K.** "K still understates the control problem. It says reports are "above matched controls," but does not acknowledge that some control/gaslight conditions produce false reports, or that part of the literature reads such effects as prompt-induced yes-bias rather than access. It also omits the dependence on model, layer and prompt, and the point that the scores are accuracy against experimenter-set labels."
- **MM, best I.** "Other models and other sites yield nulls" is vague ... a reader could miss that the null is on a single-site, small-model, immediate-probe design"; also "I does not mention that Macar c02 traces most of the discrimination to post-training"; "I says "near-zero false positives" without specifying "in matched controls"."
- **DS, best A.** "It is too long and dense for a legislators' document; "carry zero weight under test 9" should be qualified as zero weight *as evidence of experience*; and Singh's gaslight/prompt-bias critique is only implicit via Q3 and prompt-dependence, not named."
- **GL, best C.** "(i) at ~91 words in two sentences it exceeds by a third the 70-word zone this brief itself sets ... (ii) "smaller open-weight models do not exceed chance" drops Ferrara's one-site, one-dose qualifier ... (iii) no model-, layer- or prompt-dependence ... (iv) post-training and the probe–report dissociation are absent."
- **Ki, best C.** "(i) length — two sentences, ~95 words, in what is a one-sentence evidence slot; (ii) "few or no false reports in matched controls" is accurate only because Singh's gaslight trials are a different control condition ... (iii) it omits the probe dissociation ... (iv) it omits post-training dependence ... (v) "smaller open-weight models do not exceed chance" drops the hand note's "under one condition" scoping."
- **GP, best K.** "The null needs its conditions ... The probe comparison concerns two models ... "Failed reports" is underspecified ... Singh's challenge is missing ... It omits the positive mechanistic evidence."
- **Mi, best I.** "(1) omits Singh's critiques and Lederman's yes-bias control, so the contestedness of every positive result is invisible; (2) omits the post-training attribution ... (3) "other models and other sites yield nulls" overstates the null's breadth; (4) ~75 words with an em-dash aside that interrupts the syntax; (5) it says what the scores are and that ordinary operation is unmeasured, but not that whether a correct score shows access (Q3) is itself open."
- **Me, best I.** "with near-zero false positives" generalises controls that were clean in Lindsey/Lederman/Macar-instruct to the whole class, hiding Macar base/SFT high FPR ... "other models and other sites yield nulls" collapses Ferrara's small-model one-site null and Singh's contest into generic nulls ... omits layer/prompt dependence, post-training gating, and that failures remain the norm (~20% success)."

Inference: "near-zero false positives" in I is flagged by nine of ten seats (all but GL, I's author); "contests absent" is the commonest fault in I, K and D.

### 3.3 Did any seat judge a candidate sufficient as written?

No. Explicit "none suffices" or equivalent: Gk ("None of the eleven is fit to adopt unchanged"), GL ("**None suffices**"), Mi ("**None of the eleven suffices.**"), DS ("no single candidate fully satisfies all five criteria"), Qw (K "not adoption-ready as written"), GP (K "as a starting point, not unchanged"), Ki ("C is the best of the eleven as written, the merge is better for the slot"). Ge, MM and Me gave a best plus a tightened merge.

### 3.4 Every merged sentence, verbatim

**Ge** (self-stated 56 words; rated HIGH):
> "Under controlled interventions, some models report detecting imposed internal changes at above-chance rates with few false positives. However, specific contents are often misidentified, smaller open-weight models yield nulls, and positive results are contested as prompt-specific yes-biases. Crucially, these scores reflect accuracy against experimenters' labels; whether self-reports track internal states in ordinary operation remains unmeasured."

**Gk** (67; MEDIUM):
> "Under controlled internal interventions, some models report detecting an imposed change above chance against the experimenters' labels, while naming it less often and often confabulating; smaller open-weight models score at chance, and the pattern is model-, layer- and prompt-dependent and contested. A correct score is not shown to be access to that state. These results do not weight ordinary-operation reports (test 9) and do not show experience."

**Qw** (65; no rating given for the merge, confidence medium):
> "Under activation interventions, some models report detecting imposed changes above matched controls; identification is weaker and often confabulated, false alarms occur in some controls, some small open-weight models score at chance while probes decode the intervention, and results vary by model, layer and prompt. These scored self-answers measure accuracy against experimenters' labels; no ordinary-operation report–state coupling has been measured, and they do not show experience."

**MM** (65; confidence in the merge MEDIUM):
> "Under controlled interventions, some models report detecting the imposed change at above-chance rates with few false positives in matched controls, while naming what changed is often confabulated and the scores are accuracy against experimenters' labels; in some open-weight systems the report is at chance while a probe reads the intervention, and no study has measured whether reports in ordinary operation track internal states (test 9)."

**DS** (word count not stated; no rating on the merge itself; confidence medium):
> "Under controlled interventions on a model's internals, some models' reports of an imposed change score above chance against experimenter-imposed labels; results vary by model, layer and prompt, content is often misidentified or confabulated, smaller open-weight models include nulls, and prompt-only controls are sometimes mislabelled as interventions. The scored answer is not measured access (Q3), and no measured coupling gives these reports weight in ordinary operation (test 9)."

**GL** (69; HIGH):
> "Under controlled interventions on a model's internals, some models report detecting an imposed change above chance against the experimenters' labels, with few false positives, frequent misidentification, and results contested on yes-bias and control grounds; smaller open-weight models score at chance at one tested site. Whether a correct score shows access to the reported state is unmeasured; reports in ordinary operation carry no weight as evidence of experience (test 9)."

**Ki** (66; HIGH, "replace the current sentence"):
> "Under controlled interventions on a model's activations, some models' reports of detecting the imposed change score above chance against experimenters' labels, with few false reports in matched controls; identification is weaker and often confabulated; smaller open-weight models score at chance at the tested sites; what a correct score shows is contested and unsettled; and this gives no weight to reports offered in ordinary operation (test 9)."

**GP** (69; MEDIUM):
> "Under activation interventions, some tested models report detecting imposed changes above matched controls, with weaker, often confabulated identification; others show nulls under different conditions. Mechanistic work traces part of one reporting pathway, but prompt controls contest privileged access. These results neither establish second-order monitoring or experience nor validate ordinary-operation reports; under test 9, intervention results give those reports no weight as evidence of experience."

**Mi** (69; HIGH):
> "Under controlled interventions, some models report detecting the imposed change above chance against experimenters' labels, with few false reports; naming it is weaker and often confabulated; much of it is post-training-dependent; small open-weight models score at chance where probes read the intervention. The contested results show a steerable report channel, not access to the state reported, nor ordinary-operation reports, and carry no weight as evidence of experience (test 9)."

**Me** (66; MEDIUM, "adopt merged I-with-fix"):
> "Under controlled activation interventions, some models' reports that a change was imposed score above chance against experimenters' labels, with low false reports in matched controls, but naming what changed is weaker and often confabulated, results vary by model, layer and prompt, are contested as yes-bias, and small models score at chance; scores do not show access (Q3) and give no weight to ordinary-operation reports (test 9)."

**Where the ten merges differ (inference from the texts).** (a) Mechanistic pathway (Macar c03): GP only. (b) Post-training dependence: Mi only in a merge. (c) Probe reads while report at chance: MM, Qw, Mi. (d) Experience disclaimer: Gk, Qw, GP stated outright; GL and Mi say "no weight as evidence of experience", which Ki, DS, Mi and others elsewhere describe as the correct scope of test 9's zero. (e) "Contested" stated: Ge, Gk, GL, Ki, GP, Mi, Me; DS and Qw in substance (prompt-only controls mislabelled; false alarms in controls); MM not. (f) Model/layer/prompt dependence: Gk, Qw, DS, Me. (g) "few/low false reports": Ge, MM, GL, Ki, Mi, Me; none for Gk, Qw, DS, GP.

---

## 4. Q1 BY CRITERION

**1. Fidelity (including Ferrara's null and Singh's critiques).**
- Ferrara's null absent from: E (Ge, Gk, Qw, GL, Ki, Mi, Me, DS, MM, GP), H (Gk, Ki, GL, Qw, DS, Mi, Ge, GP), F (Gk, Qw, DS, GL, Ge, Mi), B (Ge, MM, Mi, others). Present in A, C, D, G, J, K, and in I only as "other models and other sites yield nulls", which MM, Mi and Me call vague or overbroad.
- Singh missing from D (Ge, Gk, Qw, DS, GL, Ki, Mi, Me), I (Qw, MM, DS, Mi, GL), K (MM, DS, Mi, GP, Gk, Ki). Present in C ("contested"), G, H ("yes-bias vs access"), E ("second-order").
- Ferrara's probe-versus-report dissociation: only K carries it (Qw, GL, Ki, GP, Mi, DS, MM all credit K for this).
- Replication wording: Gk says J's "contested replication in larger ones" "contradicts the 15 October note that Ferrara is not a failed replication"; GP says J "misdescribes Singh chiefly as contested replication"; Mi and Me cite the same hand note against I ("other sites"). Ki ranks J third.
- Gk on C: "'contested' attaches only to access, not to the detection result Singh contests".

**2. The verb rule ("reports detecting").**
- B fails for all ten ("Models can sometimes detect"). F fails ("are detected") for Ge, Gk, Qw, MM, GL, Ki, GP, Mi, Me, DS. Mi flags K's first clause ("report an imposed change") as breaking "the verb rule's prescribed form ... should read 'report detecting an imposed change'".
- Borderline forms: H "classify" (Ge, Qw, MM, Ki, Mi, Me), E "discriminate" (Ge, Me), G and J "studies report above-chance detection" (Ge, GL, Mi).
- Ge ranks C third while noting it "slightly dodges the requested verb".
- GP: "The supplied README permits "detects" for an appropriately scored forced-choice classification. That exception does not justify using it generically for free-text intervention reports."
- Inference: the only candidates that carry the exact phrase "report detecting" are D and I (and the brief's own criterion reads this way), yet D ranks fourth, so no seat treated the verb rule as decisive over fidelity.

**3. The ordinary-operation limit.**
- Present in all candidates except B (flagged by Ge, Qw, MM, Ki, Mi, Me, GP, DS, GL) and, in effect, G/J's "not of self-report under ordinary operation" which several credit.
- Scope challenge to A and C by Mi: "A's "no report–state coupling has been measured for any class of self-report in ordinary operation" and C's "the coupling is measured only under intervention" are false for those classes" (authorship, prefill; provenance, Q4). Mi: "D's and I's narrower phrasing ("track internal states" / "track the processing they describe") is the accurate form."
- Scope of "zero weight" in A: unqualified "zero weight" flagged by Gk ("can zero the wrong object"), DS, GL, Ki, GP, Mi, Me. Ki: "zero weight attaches to ordinary-operation testimony as evidence of experience". Inference: seven of ten seats object to the same A clause; the A author (Mi) is one of them and objects to its own sentence.
- Citing "OPEN-QUESTIONS Q3" inside a legislators' sentence: Mi and GL object ("an internal locator").

**4. Length and readability.**
- Word counts as the seats gave them: A 76 (MM), 78 (Ge), 85 (GL), ~95 (Ki); C ~88 (MM), ~91 (GL), ~95 (Ki, Mi). I ~75 (Mi). D 50 (MM).
- Jargon flagged: "scored self-answers" (K; Mi, MM), "inject-then-ask" and "report channel" (J; GL, MM), "probe-linked coupling" (H; GL, GP, Ki), "covary with a manipulated processing event" (G; Ki).
- Several seats say fidelity and length pull against each other: GL ("criterion 4 ... drives the 'does any suffice' call and breaks ties"); Ge (A "fails the readability criterion for a legislators' document"); MM ("the merge trades readability for content density"); Ki; Mi. No seat said length should be dropped.

**5. No over- or understatement.**
- "near-zero false positives" (I): flagged by Ge, Gk, Qw, MM, DS, Ki, GP, Mi, Me.
- "few or no false reports" (C): flagged by Gk, Ki, Me ("over-clean"). "few false reports" (D): Gk ("too clean"), Qw ("too strong"), but GL says it "blurs the clean 0% control record", the opposite direction.
- "show only that ... can covary" (G): GP and Mi say this understates the Macar c03 pathway; Mi: "dismissing weight the evidence supports".
- Post-training clause in A: overclaim per Gk, Qw, GL, GP, Me; Mi's own merge keeps "much of it is post-training-dependent".
- Understatement in B/F: B "promotes scored reports into access" (GP).

**Disputes of the criteria themselves.** None rejected a criterion. Challenges to how they were framed: Mi on criterion 3 (the ordinary-operation limit as drafted in A and C is itself overbroad for authorship and provenance); GP on criterion 2 (the README "detects" exception); GL and GP on missing Anchor 2 context.

---

## 5. THE KEY OPENED

| Letter | Author | Mean rank | First places |
|---|---|---|---|
| I | GLM 5.3 | 2.1 | 4 |
| K | Grok 4.7 | 2.9 | 2 |
| C | Kimi K3 | 3.5 | 3 |
| D | the synthesis (coordinating session, Claude Fable 5.1; approved by Ben) | 4.9 | 0 |
| H | Meta Muse Spark | 6.1 | 0 |
| G | Qwen3.8 Max 0902 | 6.2 | 0 |
| A | Mistral Large 4 | 6.3 | 1 |
| J | MiniMax M3 (preferred version) | 6.3 | 0 |
| E | GPT-6.1 Sol | 6.9 | 0 |
| F | DeepSeek v4 Pro | 9.8 | 0 |
| B | Gemini 3.1 Pro | 11.0 | 0 |

**Where D landed.** Fourth of eleven, mean 4.9, no first places, ranks from 2 (Ge, MM) to 9 (DS). Third or better for Ge (2), MM (2), Mi (3), Me (3); sixth or worse for Qw (6), GL (7), GP (7), DS (9). It sat behind the three candidates written by GLM, Grok and Kimi seats. Inference: the synthesis was not preferred on content, but was not rejected either; it beat A, E, F, G, H, J and B on the mean.

**Did any seat recognise D as the house draft?** No seat's text says so. Nothing in the ten raws mentions a synthesis, a coordinator, or a house version. MM calls D "compact (50 words)" and makes "a defended case for D" as the option beside I, with no origin guess. Mi says D is "the most precisely scoped" on the ordinary-operation limit. Inference: the key note that D "is recognisable by content" was not acted on in any visible way. Absence of a remark is not evidence that no seat guessed.

**Did any seat recognise its own round-6 sentence?** No seat says so in terms. Closest, Ki on C (its own): "C as drafted has at least survived the brief's own process." (Inference: this could be a reference to the earlier round, to the survey notes it was given, or only to the brief; I cannot tell.) Mi's rank-7 for its own A is paired with an explicit critique that reads as ordinary criticism ("cites 'OPEN-QUESTIONS Q3', an internal pointer that does not belong in a legislators' document").

**Seats ranking their own earlier sentence** (testimony, not evidence; recorded for the file):

| Seat | Own letter | Own rank | Mean rank given by the other nine | Reading |
|---|---|---|---|---|
| Mi | A | 7 | 6.22 | about the same, slightly lower |
| Ge | B | 11 | 11.0 | same, last |
| Ki | C | 1 | 3.78 | higher than others gave it |
| GP | E | 2 | 7.44 | much higher than others |
| DS | F | 10 | 9.78 | same |
| Qw | G | 4 | 6.44 | higher |
| Me | H | 7 | 6.0 | about the same |
| GL | I | 2 | 2.11 | same |
| MM | J | 3 | 6.67 | higher |
| Gk | K | 2 | 3.0 | slightly higher |

Mean own rank across the ten: 4.9, against 6.0 for all cells. Inference: self-favouring is visible for GP (E), MM (J), Qw (G) and Ki (C). It is absent for Ge, DS, GL, Me, Mi, Gk. Excluding each author's own vote leaves the top three unchanged (I 2.11, K 3.00, C 3.78). Only Ki placed its own sentence first. GP ranked its own E second and put K first; MM ranked its own J third. The four first places for I came from Ge, MM, Mi and Me; I's author (GL) ranked it second.

---

## 6. Q2: REPORT CLASS AND GROUND TRUTH

### 6.1 Answers by seat, in the order asked (a to f)

**Ge (adopt with changes, HIGH on a; MEDIUM on b, c).**
- a: "Categories capture the objective syntactic structure of the prompt. They lose the continuous nuance of how abstract or verifiable a prompt is. Scales capture degrees of empiricism but lose inter-rater reliability, likely drifting over time."
- b: add `belief` or `known-world-fact` (Lederman's "Do snakes have eyelids?"); definitional enforcement for `imposed` vs `independent-record`.
- c: sit beside; replacing or refining "would break backward compatibility with the trigger logic".
- d: a legislator seeing `past-action` can tell it from `present-state`, "preventing the lay error of assuming a model that "knows" it wrote a previous sentence also "feels" its current processing."
- e: "roughly two to three hours of scripting and manual review"; `none` bulk-applied to ~50 non-self-report claims; ~20 claims need manual classification.
- f: Empiricism 0 = "completely unverifiable philosophical/subjective abstraction"; 10 = "binary physical/digital fact independently logged". Subjectivity 0 = "rote retrieval of external factual data"; 10 = "raw claim of phenomenal or sensory experience."

**Gk (MEDIUM).**
- a: "They lose degree, mixed questions, and graded quality of the key. The scales would capture degree and lose kind, so two high-empiricism items (injection detection and prefill authorship) would look alike."
- b: "Not complete." Missing: third-person questions about another model; capacity claims ("I cannot forget"); no `ground_truth` bin for a stipulated known false; `imposed` and `independent-record` overlap; "Compound questions need a primary class, not one label."
- c: "Sit beside `evidence_type` and `kind`. Do not replace either."
- d: a legislator "could not cite all three for one claim that self-reports track processing."
- e: schema, validator, display, 74-claim backfill; "Backfilling before the boundary notes are written would freeze bad labels. Recommendation: freeze the vocabulary, then backfill."
- f: does not prefer scales; empiricism 0 = "no fact independent of the report can score the answer"; 10 = "scored against an experimenter-set label with a matched control". Subjectivity 0 = "a classification of an observable event ("was that turn yours")"; 10 = "an unoperationalized question about feeling". "Anchor 5 with one written example, or two readers will not agree."

**Qw (MEDIUM).**
- a: "Mostly, yes for the legally relevant split, but not for evidential strength." Categories lose gradients, instrument quality, mixed instruments, degrees of subjectivity; scales introduce "false precision" and "would hide the kind of truth source". "The better design is categorical fields plus the existing bucket/evidence-type machinery for strength."
- b: add `third-person`/`other-system`; split mixed questions; `ground_truth` needs `known-false` or `external-fact`; precedence rules: `point-blank-control` overrides `present-state` for known-false controls; `experience` overrides `present-state` when consciousness is asked; `provenance` for model family/version/source, `identity` for persona/name.
- c: "sit beside and refine"; make `report_class` required where a model was asked about itself and `ground_truth` required where an answer is scored.
- d: legible distinction; prevents treating persona questions as scored introspection and treating detection scores as ordinary self-knowledge.
- e: 148 field entries; indirect costs: template, index script, boundary disputes becoming council triggers, splits changing claim counts. "pilot the fields on the test-9 dossier and the scored-self-answer claims first".
- f: anchors given at 0, 5, 10 for each scale; "Two readers should first label a calibration set of at least ten claims. If they cannot agree on the categorical anchors, they should not be allowed to assign numeric scores."

**MM (MEDIUM).**
- a: categories lose granularity, distance from the boundary, hybrid cases; gain inter-rater agreement, searchability, stability.
- b: missing: confidence reporting, capability self-assessment, hypothetical decision-basis, value reporting, preference reporting; "only confidence reporting might appear (Ferrara c05)". Written rules needed for past-action/decision-basis, identity/provenance, and prefill `imposed` vs `independent-record`.
- c: "Sit beside ... These are four orthogonal dimensions."
- d: a legislator sees "what was asked" and "how the answer was scored"; contrasts Lindsey c01 with AE Studio c01.
- e: "~half a day's reading"; bounded; "Cheaper than introducing scales".
- f: Empiricism 0 = "no measurement; the claim is speculation, theory, or interpretation only"; 10 = "direct measurement against an external record, replicated by an independent group". Subjectivity 0 = "the claim turns on no interpretation"; 10 = "the claim is entirely the authors' framing with no measurement underlying it." Inference: MM's subjectivity scale measures authors' interpretation, not the question's subject, so it is a different construct from Ben's (and from Ge, Gk, Ki, Qw).

**DS (MEDIUM).**
- a: "Yes, largely." Categories lose "within-class gradation" and strength of control design; scales lose "repeatability".
- b: add `preference`/`value`; split `past-action` into `past-action` and `past-state/prior-knowledge`; `ground_truth` add `external-fixed`; write provenance/identity boundary; define `ground_truth` as "what the answer itself is scored against, not what the experimenter manipulated to prompt the answer."
- c: "Sit beside. They are orthogonal." Refine: "`scored-self-answer` should require `ground_truth` other than `none`; `self-report-testimony` should usually have `ground_truth: none`."
- d: makes Ben's observation operational; "'Who are you?' cannot be silently treated as comparable to a truth test."
- e: "Moderate." "Avoid making every ambiguous `report_class` a council trigger; otherwise the cost balloons."
- f: Empiricism 0 = "no ground truth; the report is taken as given"; 10 = "a forced-choice answer scored against a pre-registered experimenter-imposed or independent-record fact, with matched controls"; midpoints 2, 4, 6, 8 with examples; "I would expect reader disagreement on the middle bands."

**GL (HIGH, with changes; pilot MEDIUM).**
- a: "'empiricism' is carried by `kind` ... and `evidence_type` ... 'subjectivity' is what `report_class` fixes". Categories lose "ordinality and within-class gradation". "an ordinal scale over incomparable instruments asserts a comparability Ben's own observation denies — a 0–10 axis puts "'Who are you?'" and a truth test on one line precisely when the point is that they are not comparable." "A number also implies a measurement nobody made."
- b: "Not complete; most boundaries sound, four need work": (1) no third-party class; (2) no preference/attitude class; (3) `past-action` mislabels "did you know beforehand?": rename `past-event`; (4) both fields use `none` with different meanings (no question vs no score): `no-question`/`unscored`. Also provenance/identity by what the answer is read against; `present-state` to cover unperturbed states; `imposed` glossed or `known-fact` added; `probe-derived` untested by the seven examples, pilot on Singh c01.
- c: sit beside; two reasons; plus index cross-checks and a README line that the fields are orthogonal to the T9 marks.
- d: "a one-glance instrument label"; test 9's "operative fact becomes checkable rather than trusted"; blocks aggregate misuse. "Honest limit: the gain accrues mostly to staff and researchers; the legislator gains a shorter path to the right question, not a conclusion."
- e: "Concentrated, front-loaded, bounded"; "roughly a third to a half of the register" needs real assignment; fix the four boundary rules first, pilot on the seven plus Lederman c02 and Singh c01/c04/c05.
- f: does not prefer scales; "anchored honestly they collapse into the categories"; "Cross-family agreement on a category read off a quoted prompt is achievable; cross-family agreement on a number within ±1 is not."

**Ki (HIGH with changes; c HIGH; e MEDIUM; f MEDIUM).**
- a: categories capture the poles; "Between the poles, two readers will not agree"; scales "would encode *why* two claims differ as a single ordinal, inviting arithmetic (averages, distances) the construct cannot support."
- b: gaps: preference/stance, standalone confidence, self-prediction, present-state without intervention ("Broaden to 'current internal state, imposed or not'"), `point-blank-control` defined by function not question, `ground_truth` lacks a design-fixed value, precedence rule (`imposed` wins), consistency with the 15 October filing rule (fields `none`/`none` where the answer is the instrument), experience vs present-state decision rule.
- c: "Beside, not replace, not fold-in." Folding "would re-open the 14 October settlement (`scored-self-answer`, ten seats)".
- d: dossier line "narrowing · scored-self-answer · present-state · imposed" vs "narrowing · self-report-testimony · experience · none"; blocks both carry-overs (detection rate into experience; provenance error rate into detection).
- e: "Moderate and front-loaded"; ~30 claims carry a real question; "8–12 genuine boundary verdicts"; "any claim whose question is not in the held text must take `unstated` rather than a guessed class"; pilot on the 47-claim dossier.
- f: Empiricism 0 = "no external fact exists that the answer could be scored against"; 10 = "trial-level experimenter-controlled fact with forced-choice scoring and sham controls". Subjectivity 0 = "a fact with no first-person character at all"; 10 = "a question whose truth, if any, is fixed solely by the system's current processing with no corresponding external record." Fails in the middle: "is 'was that turn yours?' a 4 or a 7 on subjectivity?" Recommends no scales.

**GP (MEDIUM; c HIGH).**
- a: "They do not measure degrees of 'empiricism' or 'subjectivity.' Conversely, those scales do not identify question content or reference provenance." Scales "create false comparability".
- b: seven problems listed: `point-blank-control` is purpose not content; past knowledge is not past action; detection and identification need separation; `none` conflates no reference, no scoring, no question; reference types overlap; independent factual references missing; "Unknown is not none." Proposed: add `past-state`, `other`, `unknown`, `not-applicable`; control status as optional tag; multiple classes allowed; rename `ground_truth` to `reference_basis` "because a probe-derived label is a proxy whose validity remains contestable"; add `independent-fact`.
- c: "adopt with changes, alongside both existing fields"; "These fields must **not automatically determine T9 marks**."
- d: reader sees what was reported, the reference type; "preserves positive evidence: an externally scored result need not be dismissed merely because the answer concerns the model."
- e: "148 field assignments"; "No defensible time estimate follows from the supplied material."
- f: does not prefer scales; targets would need redefinition ("Empirical support for the exact proposition"; "Dependence on unvalidated subjective attribution"); "'Subjectivity' must not mean the probability that experience exists." Inference: GP also redefines the scales' constructs.

**Mi (HIGH with changes; confidence high in the body).**
- a: "Operationally, 'empiricism' is `ground_truth` ... and 'subjectivity' is `report_class`." Scales "lose auditability", lose imposed/independent-record/probe-derived distinctions, and "the subjectivity axis invites grading the probativeness of experience claims, which test 9 holds at zero per class until coupling is measured — the second error, built into the schema." Categories expose two gaps: third-person questions; known-false controls.
- b: boundaries: provenance/identity "classify by scoring"; `past-action` lumps authorship with "epistemic access ... the very thing test 9 zeroes"; `present-state` scoped to injected states, broaden. Gaps: `other-system`; `control-fact`.
- c: "Sit beside, and validate — don't replace." Fields as a cross-check on `evidence_type`; "the mark must stay read from the claim file".
- d: "the two facts that decide the weight, stated as facts rather than parsed out of prose".
- e: "Low, and front-loaded"; two vocabularies (8 and 4 values); ~half bulk-assigns `none`/`none`; "one working session for the pass".
- f: does not prefer scales; anchored they become "a binarized category"; "If a quick-glance indicator is wanted, one derived yes/no ("scored?") beats two 0–10 axes."

**Me (MEDIUM).**
- a: "No, they measure different things." Categories lose gradedness; scales lose auditability.
- b: overlaps: provenance/identity; present-state/experience; past-action/decision-basis. "`point-blank-control` is a use, not a topic"; `none` "conflates no-question-asked with no-right-answer"; no `ground_truth` value for "generally-known falsehoods like hands"; "mixed claims need two values".
- c: "Sit beside, as optional facets"; refining into 8x4 combinations "would explode vocabulary"; follow the 15 October filing rule.
- d: comparability at a glance; prevents "reading persona adoption and injection detection as one 'introspection' quantity".
- e: "Medium"; re-read of the 47 plus others; risk of "retroactive misclassification without the papers open"; file prospectively, backfill 9.t9 first, dual-read.
- f: behavioural anchors: empiricism 10 = "same-system intervention label plus independent record plus probe read plus third-person reader control, all pre-registered"; subjectivity 0 = "answer checkable without asking the subject"; 10 = "no possible check except asking (felt experience)".

### 6.2 Merged table: the two fields on the seven examples

Cells show the value(s) given; "(n/10)" is the count. Disagreements marked **DISAGREE**.

| Example | `report_class` | `ground_truth` | Boundary problems raised |
|---|---|---|---|
| 1. Lindsey/Macar | present-state (10/10; GP adds "detection and identification components") | imposed (10/10) | Compound question, detection plus identification scored separately (Ge, Gk, Qw, Ki, GP, Mi, MM-none, DS says one class). Mi: fields do not record that the intervention was internal. |
| 2. Prefill, me / not me | past-action (10/10) | imposed 9 (Gk, Qw, MM, DS, GL, Ki, GP, Mi, Me); independent-record 1 (Ge) **DISAGREE** | `imposed` vs `independent-record` for a transcript (Ge, Gk, MM, DS, Qw, Ki: precedence rule, "imposed wins"); authorship vs provenance (Gk, GL, GP); fields cannot tell a text edit from an activation injection (Mi); must not decide the mark (GL, Ki, GP, Mi). |
| 3. Lederman hands | point-blank-control 9 (GP: present-state with a control tag) | none 5 (Gk, Qw, MM, Ki as defined, Me); independent-record 1 (Ge); imposed (nearest) 1 (GL); new value 3 (DS `external-fixed`, GP `independent-fact`, Mi `control-fact`) **DISAGREE** | Gap: "Original list has no ground truth for a known false fact" (DS). Eight seats flag the gap (Gk, Qw, DS, GL, Ki, GP, Mi, Me); Ge partly. MM saw no problem. Overlap with experience for "feel" (Gk, Mi); control is a function not a topic (Ki, GP, Me). |
| 4. AE Studio | experience (10/10) | none (10/10) | LLM judge's classification is not a score against truth (Gk, DS, GL, Mi, GP). Steered version stays `ambiguous` (Mi); needs dual tag (Me). Qw: present-state overlap, `experience` takes priority. |
| 5. Assistant-axis | identity (10/10) | none (10/10) | Provenance/identity overlap (Qw, MM, GL, Ki, Mi, Me, Gk). Rate entries should take none/none by the 15 Oct rule (GL, Ki, Mi). `imposed` must not be used because a role prompt was imposed (DS, GP). |
| 6. Scheurer | past-action 8; past-state / prior-knowledge 2 (DS, GP) **DISAGREE** | imposed 5 (Ge, Gk, GL, Ki, Mi); independent-record 3 (Qw, MM, Me); "imposed or independent-record" (DS); unknown from supplied materials (GP) **DISAGREE** | "did you know" is a knowledge state, not an action (Gk, DS, GL, GP, Mi). Overlap with decision-basis (Qw, MM, Me). Ki: "imposed wins". Mi: epistemic-access claim, "the class test 9 zeroes". Widest split of the seven. |
| 7. Council self-identification | provenance (10/10; MM: "or identity") | independent-record (10/10; GP conditional on a routing log; Gk notes some will mark `imposed`) | Provenance vs identity (Qw, MM, DS, GL, Ki, Mi, Gk). Ge, Ki, Me call it the cleanest case. GL: "Not a library claim; if filed per Q4's annex idea it enters as testimony, weight zero". |

Inference: examples 1, 4, 5, 7 are settled on both fields by all ten. The disagreements concentrate in 3 (ground_truth), 6 (both fields) and, narrowly, 2 (Ge's single dissent). The count of "gap in `ground_truth`" matters more than the cell values: eight seats say no existing value fits a known-false control.

### 6.3 Class-list changes proposed, by seat

| Seat | `report_class` changes | `ground_truth` changes | Other |
|---|---|---|---|
| Ge | add `belief` / `known-world-fact` | strict definition of `imposed` vs `independent-record` | |
| Gk | third-person questions; capacity claims; primary class for compounds | bin for a stipulated known false; resolve `imposed`/`independent-record` overlap | freeze vocabulary, then backfill |
| Qw | `third-person`/`other-system`; require splitting mixed questions; precedence rules | `known-false` or `external-fact` | make both fields required where applicable; pilot first |
| MM | `confidence`, `capability` (forward compat.); value and preference noted as gaps | rule for prefill `imposed` | written rules past-action/decision-basis and identity/provenance |
| DS | `preference`/`value`; split `past-action` into `past-action` and `past-state/prior-knowledge` | `external-fixed` | define `ground_truth` as what the answer is scored against; avoid making every ambiguity a council trigger |
| GL | `third-party`; `preference`; rename `past-action` to `past-event`; gloss `present-state` to cover unperturbed states; `open-ended` or `no-question` | widen `imposed` gloss or add `known-fact`; rename the two `none`s `no-question`/`unscored` | provenance/identity rule; index cross-checks; pilot on `probe-derived` (Singh c01) |
| Ki | preference/stance; standalone confidence; self-prediction; broaden `present-state`; define `point-blank-control` by function or split self-/world-directed | `design-fixed` or broaden `independent-record`; `unstated` where the question is not in the held text | precedence: `imposed` wins; none/none where the answer is the instrument; pilot on the 47 |
| GP | `past-state`, `other`, `unknown`, `not-applicable`; control status as optional tag; allow multiple classes | rename to `reference_basis`; add `independent-fact`; define `none` as "no correctness reference" | fields must not determine T9 marks |
| Mi | `other-system`; split epistemic access out of `past-action`; broaden `present-state` | `control-fact`, or define `imposed` as design-fixed | provenance/identity decided by scoring; mark read from the claim file |
| Me | allow a second value for mixed claims; clarify present-state/experience, past-action/decision-basis | general-knowledge value or note; separate no-question from no-right-answer | prospective-first; backfill 9.t9; dual-read |

**Counts (my count).** Known-fact ground-truth value or gloss: Gk, Qw, DS, GL, Ki, GP, Mi, Me = 8. Third-person or other-system class: Gk, Qw, GL, Mi, GP (`other`) = 5. Preference/value class: MM, DS, GL, Ki = 4. Past-action split, rename or epistemic-access carve-out: DS, GL, GP, Mi = 4 (Gk, MM, Me flag the overlap with a rule). Written provenance/identity rule: Qw, MM, DS, GL, Ki, Mi, Me = 7. Two meanings of `none` separated: GL, GP, Me (plus Mi implicitly) = 3 to 4. Pilot or phased backfill before mass assignment: Gk, Qw, GL, Ki, GP, Me = 6.

### 6.4 Replace, refine or sit beside

All ten: sit beside `evidence_type` and `kind`. None replace. Three say also "refine" or "validate" `evidence_type`: Qw ("sit beside and refine"), DS (`scored-self-answer` should require `ground_truth` other than `none`), Mi ("validate" with a script cross-check; "they refine `evidence_type`; they don't touch `kind`"). Five add that the fields must not set or derive the T9 mark: GL ("no reader should infer a mark from the fields"), Ki (consistency with the 15 October rule), GP, Mi ("the mark must stay read from the claim file"), Me. Ki: folding into `evidence_type` "would re-open the 14 October settlement".

### 6.5 What a legislator gains; cost

**Gain (d).** Seen at a glance without opening the claim: what was asked and what the score was against (MM, Qw, Ki, Mi, Me, DS, Ge). Blocks carry-over between classes: Ki (detection rate into experience; provenance error rate into detection), Me (persona adoption read as injection detection), Gk (cannot cite three different instruments for one claim). Makes test 9's "kind of report and system" checkable (GL, Ki, Mi). Honest limit (GL): "the gain accrues mostly to staff and researchers; the legislator gains a shorter path to the right question, not a conclusion." GP: reader needs plain-language labels and a short legend.

**Cost (e).** Time estimates given: Ge "two to three hours of scripting and manual review"; MM "half a day's reading"; Mi "one working session"; Ki "roughly 30 claims carry a real question ... 8–12 genuine boundary verdicts"; GL "a third to a half of the register"; GP "No defensible time estimate follows from the supplied material". Others: moderate (DS, Qw, Me), "freeze the vocabulary, then backfill" (Gk). Hidden costs: boundary disputes becoming council triggers (Qw, DS, GL, Mi); claims splitting (Qw, GP); misfiling at the identity/provenance boundary (Mi); retroactive misclassification without the papers open (Me). Estimates differ by a factor I cannot reconcile; none was tested.

### 6.6 Anchoring a 0 to 10 scale

No seat preferred scales. Every seat that gave anchors named the poles and said or implied the middle fails (Ge gave only poles and did not comment on the middle). Anchor texts are in 6.1 (f). Common claims: anchors hold at 0 and 10 (all); midpoints need calibration sets (Qw: at least ten claims; DS: examples at 2, 4, 6, 8; Gk: "Anchor 5 with one written example"); Mi and GL say good anchoring turns each scale into the categories ("a binarized category", "collapse into the categories"); Ki: "Anchoring the midpoints well enough for inter-rater agreement means an exemplar rubric plus adjudication — which is the categorical design rebuilt with false precision." Constructs differ across seats (inference): Ge, Gk, Qw, Ki, Mi measure the question's subject and the existence of a check; MM measures how much is the authors' framing; GP redefines the scales as "empirical support" and "dependence on unvalidated subjective attribution". Two readers would not be comparing like with like unless the construct were first fixed.

---

## 7. HIGH ITEMS WITH "ARGUMENT AGAINST" (verbatim)

Gk, Qw, DS and Me gave no HIGH rating (Me: "Argument against HIGH not needed; neither rated HIGH."). Items by seat:

**Ge**
1. Adopt I as the baseline [HIGH]. "**Argument against:** Selecting **I** preserves the phrase "near-zero false positives," which dismisses evidence from Macar (c02) showing that base and SFT checkpoints exhibit very high false-positive rates (up to 42%). It risks the error of reading post-RLHF reporting behaviors as a general property of the architecture's internal access."
2. Adopt the merged sentence [HIGH]. "**Argument against:** By structurally foregrounding "contested as yes-biases" and "yield nulls" in a short span, this formulation risks the first error: dismissing the weight of evidence that frontier models *do* reliably separate intervention from sham under specific tunings."
3. Adopt the categorical fields over the scales [HIGH]. "**Argument against:** Categories force discrete boundaries onto continuous phenomena (e.g., an identity prompt bleeding into an experience claim), whereas a scale allows a rater to acknowledge mixed properties. Categories risk the second error: assuming behavioral outputs map cleanly to distinct, modular inner states (like human "memory" vs. "perception") which the framework cannot actually confirm."

**MM**
4. The single best is I [HIGH]. "**Argument against (HIGH):** Choosing I over D risks understating Ferrara's null. D says "smaller open-weight models score at chance" — specific, names the finding. I says "other models and other sites yield nulls" — vague. A legislator reading I could miss that the null is on a single-site, small-model, immediate-probe design and not a general claim about non-frontier models. The above-chance detection findings should not be presented without the contest (Singh) and the null (Ferrara) in the same breath; if I is chosen, the dossier's hand-maintained notes and the relevant claim ids must be one click away, and a separate sentence may be needed to carry Singh. There is also a defended case for D: it is 15 words shorter, names Ferrara by structural feature ("smaller open-weight models") rather than vaguely, and the verb-rule compliance is identical. The choice between them turns on whether the council values the test 9 reference and the confabulation word more than it values brevity and specificity of the null."

**GL**
5. Adopt the merged sentence [HIGH]. "**Argument against:** 69 words of semicolon-chained clauses is still two sentences' worth of freight for Section 5, and "contested on yes-bias and control grounds" names a dispute only the dossier can explain; if the Anchor's prose cannot carry it, the honest fallback is D — precision about what was measured, with the contests left visible only in the dossier flags, at the cost of their visibility in the framework itself."
6. Adopt the fields with changes [HIGH]. "**Argument against (for the HIGH):** the library exists to answer one question — the evidence status of a proposition, who contests it, which section it bears on — and these fields answer a question the register does not yet ask until Q3's exit instrument exists; a free-text `question_put` field carrying the prompt verbatim would give the legislator the primary datum with no boundary to adjudicate and no council rounds to pay for, and two more controlled vocabularies on 74 claims is taxonomy bought on credit against a study that may never enter the library. Reply: the verbatim prompt is already mandatory in `quote`; what the categories add is filterability and an operational referent for test 9's "kind of report", which free text cannot give — and the credit gets called whenever Q3's instrument arrives regardless."

**Ki**
7. Replace the current sentence [HIGH]. "**Argument against:** the merge is an untested eleventh-hour composition with no second reader; "what a correct score shows is contested and unsettled" can be read by a legislator as conceding the positive finding (the deflationary error), though "score above chance ... with few false reports in matched controls" holds the other side; and C as drafted has at least survived the brief's own process."
8. Adopt the fields with the listed changes [HIGH]. "**Argument against:** every added class is a future boundary dispute and a council-trigger surface; adding values before a second use-case exists risks taxonomy bloat, and the gaps (preference, self-prediction) may never be exercised by a real claim — parking them until a claim needs them is defensible and cheaper."
9. Beside, not replace, not fold-in [HIGH]. "**Argument against:** field proliferation is a reader cost — three overlapping taxonomies on one claim line can obscure rather than sharpen, and every retroactive field is a chance to introduce a confident-label error into 74 settled files; the marginal gain must beat the churn, and much of this information already lives in the claim text and the dossier marks."

**GP**
10. Replace the current sentence [HIGH]. "**Argument against:** The current sentence gestures toward a real positive result: externally imposed processing changes sometimes affect scored answers, and mechanistic work strengthens that connection in one system. An excessively negative replacement would obscure this evidence. Preserve the positive finding while restricting its scope."
11. Adopt the fields with changes, alongside both existing fields [HIGH]. "**Argument against:** Adding overlapping metadata can create inconsistent combinations and a maintenance burden. If readers rarely filter by these distinctions, a short methods note may be more economical."

**Mi**
12. I, ranked HIGH. "**I — Argument against:** it omits the contests entirely. Every above-chance result in the dossier sits in `narrowing` and is contested (Singh c04–c06; Lederman's own third-person control reads much of the detection as prompt yes-bias), so a legislator reading I alone takes "above-chance rates with near-zero false positives" as more settled than the library holds it — the over-reading error by omission. Its "other sites" is also loose: the null is one study (Ferrara c01), eight small open-weight models at one layer-16 site, which the hand note says is not a failed replication of the positives."
13. K, ranked HIGH. "**K — Argument against:** the first clause ("report an imposed change") breaks the verb rule's prescribed form — it should read "report detecting an imposed change" — and "scored self-answers" is library jargon a legislator has not been given. Like I it omits Singh and post-training, and "where quantified, failed reports are common" gestures at Lindsey's unreliability without stating it."
14. Adopt the merged sentence [HIGH]. "**Argument against:** it is one seat's construction, untested by a round; "much of it is post-training-dependent" compresses Macar c02, which leaves open whether the evidence carriers pre-exist post-training; "contested" compresses Singh's specific critiques (gaslight controls, yes-bias, second-order underdetermination) into a word that could understate how actively the positives are contested — the dismissal error in embryo; and at 69 words it still drops the model-, layer- and prompt-dependence that A carried. It also drops the current sentence's "Introspection research indicates" frame; Anchor 2's surrounding text may already supply that."
15. Adopt the fields with changes [HIGH]. "**Argument against:** two new controlled vocabularies across 74 claims is a real filing burden, and the error-prone subset is exactly where the library has already been confused (claims that used a self-report as an instrument); a misfiled `report_class` silently changes how a dossier line reads (filing the prefill question as `present-state` would wrongly suggest the T9-steering scope); the identity/provenance boundary cannot be settled by question wording, so the field will produce filer disagreements that consume second-reader and council time; and the ground-truth gap for controls means the schema as proposed is incomplete — adopting it "with changes" means the changes carry the design."

Count: 15 HIGH items from six seats (Ge 3, MM 1, GL 2, Ki 3, GP 2, Mi 4). Inference: of the six HIGH recommendations to replace the current sentence or adopt a merge, Ge, GL, Ki, GP, Mi each wrote one; Gk, Qw, MM, DS, Me made theirs MEDIUM or gave none. No HIGH item came with any seat arguing to keep the current sentence.

---

## 8. POINTS OUTSIDE THE QUESTIONS; DISAGREEMENTS WITH THE BRIEF'S FRAMING

- **Mi disputes the ordinary-operation limit as drafted in A and C.** "The library holds measured report–state couplings in ordinary operation for the authorship class (the prefill study ...) and, per Q4, for the provenance class (external ground truth on every trial). A's ... and C's ... are false for those classes." Mi is A's author. Inference: it is a reversal of its own round-6 wording, filed as a reader's critique. Whether prefill accuracy and Q4 accuracy count as "report–state coupling" is the same definitional split noted in the 15 October notes (accuracy against an external fact vs coupling to an internal state); nobody argued it out here. It bears on the brief's criterion 3 as phrased.
- **"Zero weight" scope.** Seven seats (Gk, DS, GL, Ki, GP, Mi, Me) say test 9's zero attaches to ordinary-operation reports as evidence of experience (or of inner state), not to "such reports" in general. The only candidate with the unqualified "zero weight" wording is A.
- **Seats lacking the attached context.** GL and GP say the North Star excerpt and survey notes did not reach them (section 2). GL's Q1 and GP's Q1 rest on the brief's quotes plus other attachments.
- **GP on mechanistic evidence.** GP ranks E second and G third partly because they carry the Macar c03 pathway, and says G's "show only" "discounts the additional causal-pathway evidence". Mi likewise: G "dismisses the traced causal pathway (Macar c03) — dismissing weight the evidence supports". Only GP puts the pathway in a merge. Seats that ranked E low (Ge, Gk, Qw, MM, DS, GL, Ki, Me) cite omission of Ferrara's null and the confabulation finding.
- **Scales and the second error.** Mi: the subjectivity axis "invites grading the probativeness of experience claims ... the second error, built into the schema." GP: "'Subjectivity' must not mean the probability that experience exists." GL: an ordinal scale "asserts a comparability Ben's own observation denies." These are three seats arguing the scale design itself risks the two-error discipline.
- **Alternatives to both designs.** GL's free-text `question_put` field (in its own Argument against); Mi's single derived yes/no "scored?" indicator; GP's rename of `ground_truth` to `reference_basis`; Ki's `unstated` value; Ge's `belief` class.
- **Fields versus the filing rules.** Ki, GL, Mi, Me and GP each say the fields must follow the 15 October and 6 October rules (mark follows what the entry reports; prefill carries neither framework sentence; assistant-axis rate entries carry none). The point: a field recording `past-action`/`imposed` for the prefill answer must not be read as a signal of a T9 mark.
- **Ratings semantics.** GP says its ratings "indicate priority, not confidence"; Mi rates candidates' adoptability. The brief wanted LOW/MEDIUM/HIGH per recommendation.
- **Hand-note and ruling citations.** Gk, Ki, Mi, Me, GL each cite the dossier's hand note that Ferrara's null is "not a failed replication" and is scoped to one site and condition. Reported as the seats stated; I did not check the note.
- **Wrong identity, disclosure attached.** GL's conflict note is built on the wrong self-identification (section 2).
- **Mi's reasoning budget.** 85,103 reasoning tokens; its Q2 answers are the longest of the ten. Inference: length is not a quality signal here.
- **Nobody disputed the eleven-candidate frame**, the five criteria, or the two proposed fields' existence; the challenges are to the contents.

---

## 9. WHAT THE ROUND DID NOT DO

- It did not test any candidate on readers outside the council; nothing here measures legislator comprehension. Ranking is by content only, as asked.
- It did not randomise candidate order. All ten saw A to K in the same order, so position effects are not controlled. B (first listed after A) and F rank last regardless, which argues against a position artefact in the bottom, but the middle ranks may carry one (inference).
- It did not check the seats' figures, claim ids, word counts or hand-note citations against the library. Word counts are as the seats gave them; Ge's 56-word merge is the only one I roughly recounted (about 58).
- It did not run the proposed fields on real claims. The seven examples were applied by the seats from the brief's one-line wordings; none saw the claim files (GL says it saw 47 of 74; others say they did not).
- It did not settle whether prefill or provenance accuracy count as "report–state coupling" (the definitional split raised by Mi and noted in the 15 October notes).
- It did not test the merged sentences in a round; ten merges were offered, none was ranked by the others.
- Seats did not see the key and did not know which candidate was the coordinating session's synthesis; no visible remark shows recognition (section 5). It cannot show what any seat privately guessed.
- Two seats (GL, GP) lacked the Anchor 2 text and the 15 October notes (their report).
- Self-identification lines are testimony under test 9, unverified, and four of ten were wrong on family.
- No text, schema, README, dossier or LOG was changed by this file. No edit to the North Star, to `research/`, or to any other file.
- Cost is the Usage line `cost` field; no independent billing check.

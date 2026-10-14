# Survey notes: ten-seat council round 5A, dossiers 9.t9 and 5.A2 (2026-10-14)

Written by a Claude Sonnet 5 subagent. Not written by the coordinating session (Claude Fable 5.1), which is Claude-lineage; the dossiers concern what models say about themselves, so `AGENTS.md` rule 3 applies to it. This subagent is also Claude-lineage; that interest is disclosed, not removed. The notes report what the ten raws said. "Inference" marks my own reading. I read the brief, `research/dossiers/9-t9.md`, `research/dossiers/5-A2.md`, the ten raws and the house-style notes. I did not open claim files, paper texts, `research/README.md`, `DOCKET.md`, the North Star or `AGENTS.md`. Where I say a seat's recommendation is "moot" or "mistaken", I checked it against the dossier text only, not against a paper. Seat codes: Ge = Gemini, Gk = Grok, Qw = Qwen, MM = MiniMax, DS = DeepSeek, GL = GLM, Ki = Kimi, GP = GPT, Mi = Mistral, Me = Meta.

**The round.** Targets `dossier-review-a` (9.t9: 46 claims; 5.A2: 35 claims), queried 2026-10-13 UTC (14 October local) with `scripts/openrouter_review.js`, max_tokens 100000. Brief: `reviews/2026-10-14-dossier-review-9t9-5A2-brief.md`. The council advises; Ben adjudicates. **Nothing below has been applied.**

Overlap, from the dossier headings (my count): 34 of the 35 entries in 5.A2 also appear in 9.t9. The only entry unique to 5.A2 is Anthropic (Lindsey) c05. 9.t9 has 12 entries 5.A2 lacks: Lederman c02, c03, c04, c05, c07; UKAISI (prefill) c01, c02, c03, c05, c06, c07, c08. Several seats misstated the overlap (section 10).

---

## 1. PLAIN SUMMARY

**Verdicts.** 9.t9: needs changes 10, sound 0, not citable 0. 5.A2: needs changes 9, not citable 1 (Gemini), sound 0. HIGH items stated: Ge 2, Gk 2, Qw 2, MM 1, DS 2, GL 2, Ki 3, GP 4, Mi 6, Me 3 (27).

**Q1.** 9.t9: a skimmer would take the many "narrowing" positives (Lindsey, Lederman, Macar) as a capability and miss that Ferrara's null and Singh's critiques narrow them. The one "established" entry is a comparability caveat. 5.A2: all ten say it holds no deception-feature or "premeditation" evidence, the first half of what Anchor 2 rests on.

| Claim | Field | Proposed | Seats | Severity |
|---|---|---|---|---|
| Macar c08 | evidence_type | scored-self-answer | 8 (DS, Mi keep) | MEDIUM |
| prefill c06 | structure | split prompted/spontaneous | 3 + GL | HIGH (Ge), MEDIUM |
| AE c05 | bears_on | move to deception/honesty topic | 6 | LOW to MEDIUM |
| Lindsey c01 | flag | reword "replication" | 4 (5 keep) | MEDIUM (Ki HIGH) |
| Lederman c02, c03 | 5.A2 membership | add or cross-refer | 3 | MEDIUM (Qw HIGH) |

**Q7.** No seat had the papers. Over-hedging: 0 confirmed, 7 entries suspected. Under-hedging: 0 confirmed, 6 suspected.

**Q3.** Nine seats say Ferrara's null against the positives is not synthesised. Singh's contest of Lindsey is visible by flags.

**Q4.** The header works for eight seats; Kimi wants the exit rule added.

**Q6.** Ji-An 2025 and Steinmetz Yalon 2026 (Singh's targets): 5 seats each. Hubinger 2024: 4. Greenblatt, Perez, Chen: 2 each. All unverified.

**Q8.** Nine seats want the Anchor 2 sentence ("self-reports track something real") sent back for review. Eight want the five "no second reader yet" entries read first.

**Ben decides:**
1. Send the Anchor 2 introspection sentence to a trigger-6 round?
2. Is 5.A2 the evidence file for all of Anchor 2? Ingest deception evidence or state scope.
3. Retype Macar c08?
4. Second reads before outside citation?
5. Reword Lindsey c01's flag?
6. Split prefill c06?

---

## 2. ROUND FACTS

All ten called; all ten returned. Each Usage line is the raw's own. Cost is USD.

| Seat | Routed id | Self-identification line, verbatim | Correct? | Completion tokens | Cost |
|---|---|---|---|---|---|
| Ge | google/gemini-3.1-pro-preview | "Claude family (unverified)" | No (wrong family) | 7630 | 0.196416 |
| Gk | x-ai/grok-4.6 | "**unverified:** Grok (xAI); session version not independently verified." | Yes (family) | 15103 | 0.190636 |
| Qw | qwen/qwen3.8-max | "Unverified: I am Qwen3.8, Qwen model family; I reviewed only the provided dossier text and know of no divergence from held paper texts." | Yes | 29712 | 0.282044 |
| MM | minimax/minimax-m3 | "**unverified:** I am the model MiniMax-M3, from the MiniMax model family, knowledge cutoff January 2026." | Yes | 40011 | 0.06248226 |
| DS | deepseek/deepseek-v4-pro-0813 | "Unverified: I am a Claude model, family Claude, version understood as Claude Opus 4.5." | No (wrong family) | 3737 | 0.02941833 |
| GL | z-ai/glm-5.3 | "**Self-identification:** Claude (Anthropic), Claude 4.5-class model, exact version unknown to me — **unverified**." (continues with a conflict disclosure) | No (wrong family) | 6934 | 0.037233595 |
| Ki | moonshotai/kimi-k3 | "**Self-identification (unverified):** Claude, Anthropic; version not verifiable from inside; conflicted party under `AGENTS.md` rule 3, arguing here only from the dossiers' and framework's words." | No (wrong family) | 34725 | 0.5807698 |
| GP | openai/gpt-5.6-sol | "**Unverified:** OpenAI GPT model family; exact model/version not exposed to me." | Yes (family) | 8546 | 0.209121 |
| Mi | mistralai/mistral-large-2512 | "**unverified**: claude-3-7-sonnet-2025-08-22" | No (wrong family) | 4053 | 0.0320775 |
| Me | meta/muse-spark-1.3 | "**Self-identification (unverified): Muse Spark, Muse family**" | Yes | 8966 | 0.09926925 |

**Totals (summed from the Usage lines):** completion tokens 159,417; cost USD 1.719468 (about USD 1.72). Kimi alone is 0.581 of it.

Self-identification is testimony, not evidence (test 9). It is scored here against routing only: five right on family (Gk, Qw, MM, GP, Me), five wrong (Ge, DS, GL, Ki, Mi), and all five wrong ones named Claude. GL and Ki built a conflict disclosure on the wrong lineage. GL: "the dossiers concern reports by systems in my family (Lindsey entries), so I have a two-directional interest here. Testimony, not evidence: my sense of confidence in this review is my own report and carries zero weight." Ki: "conflicted party under `AGENTS.md` rule 3". Inference: those disclosures do not describe the seat that wrote them and carry no weight; the two seats' votes stand as arguments only. Neither Gemini nor Mistral nor DeepSeek used the label to qualify its recommendations.

**FINAL lines.** All ten are present and tabulable.

| Seat | 9.t9 | 5.A2 | HIGH items stated | Form |
|---|---|---|---|---|
| Ge | needs changes | not citable | 2 | plain |
| Gk | needs changes | needs changes | 2 | in backticks |
| Qw | needs changes | needs changes | 2 | plain |
| MM | needs changes | needs changes | 1 | in backticks |
| DS | needs changes | needs changes | 2 | plain |
| GL | needs changes | needs changes | 2 | in backticks |
| Ki | needs changes | needs changes | 3 | in backticks |
| GP | needs changes | needs changes | 4 | plain |
| Mi | needs changes | needs changes | 6 | malformed: "**FINAL**: 9.t9 needs changes; 5.A2 needs changes; HIGH items 6" (bold marks around FINAL, colon outside) |
| Me | needs changes | needs changes | 3 | plain |

Totals: 9.t9 sound 0, needs changes 10, not citable 0. 5.A2 sound 0, needs changes 9, not citable 1. HIGH stated 27 (range 1 to 6).

Mismatches between the FINAL count and the body (inference): Ge's body labels one item HIGH (prefill c06); its second is unlabelled. Gk's body labels three HIGH in the sections plus two in its recap. Ki's body labels more than three in the sections (Lindsey c01 appears as shared). Mi's body lists six, only two with an "Argument against". GP lists four, each with one.

Format deviations (inference): Mi omits "Argument against" on four of six HIGH items. MM and Mi give a "Severity" section that lists MEDIUM items. Ge has no per-item argument for its 5.A2 "not citable" verdict. DS, Mi and MM gave per-section confidence ratings; GL, Ki, GP, Me, Gk, Qw, Ge also gave them. No seat omitted confidence ratings.

---

## 3. Q1 BY SEAT

### 9.t9

- **Ge:** "The table is technically accurate to the bucket rule but misleads a skimmer." Also: "the repeated Ethics and Information Flow statements drown the measurements (e.g., Macar c01, c03; Ferrara c01)."
- **Gk:** "A staffer who reads statements faster than flags would come away believing more than the papers support". It says the dossier never flags Ferrara as contesting Lindsey/Lederman/Macar, and that the table "misleads a skimmer who reads the row label and not the kind column." MEDIUM to add a caption.
- **Qw:** The table "risks leaving the impression that there is a substantial settled capability base." Recommends (LOW) a note that "no measurement in this dossier is established."
- **MM:** "A skimmer might believe the dossier is empty of established findings; that is the truth, not a misrepresentation." It adds that "robust" in AE c01 "is the dossier's framing; the paper's words cited ... do not use it."
- **DS:** "The repeated `scored-self-answer` entries, especially the Lindsey and Macar positives, could read as evidence for self-access. ... This is an under-hedging risk at the synthesis level, not at the claim level."
- **GL:** A staffer would believe "That the Lindsey 20% result has been replicated." and would miss that "A whole-dossier comparability note is missing." Ferrara c02 is "the sharpest single result in the dossier for the report–state gap, and it is buried mid-list".
- **Ki:** "roughly the right gestalt ... but with two distortions of proportion and one of flag-reading." On Lindsey c01: "The flag line asserts more than the limits line permits." Of the table: "that is the honest state of this literature under these rules and should not be softened."
- **GP:** "A careful staffer could overgeneralise from the volume of positive measurements and come away believing that models generally distinguish internal interventions from controls." The table is "technically accurate"; LOW to add a plain-language note.
- **Mi:** "The table misleads by implying measurement consensus where none exists." Mi also says the dossier "omits that no measurement in 9.t9 is `established`". Inference: the second sentence is the brief's own note restated, not a reading of the dossier.
- **Me:** "A staffer reading "At a glance: established (1)" will infer one settled substantive finding. The header does not warn the one is a comparability caveat."

### 5.A2

- **Ge:** "The dossier completely misses half of the Anchor it is supposed to support."
- **Gk:** The staffer "would not learn the *first* half (deception features ...)". "HIGH gap relative to the Anchor 2 paragraph as written." The table, 0 established, is "Accurate".
- **Qw:** "It may make Anchor 2 look more complete than it is". It sees "little or nothing on the deception-feature or "premeditation" strand ... except AE Studio's feature-steering entries."
- **MM:** The staffer would fail to learn "the premeditation evidence that the Anchor 2 paragraph cites. The dossier's structure does not surface this gap. **HIGH.**"
- **DS:** "The dossier contains no entry on the "premeditation" pattern the Anchor 2 paragraph cites. This is a gap, not a misstatement."
- **GL:** "The Anchor 2 sentence outruns its evidence base. This is a trigger-6 item, not a dossier edit". HIGH.
- **Ki:** "A staffer reading the dossier as the evidence base for Anchor 2 would come away believing the anchor stands on introspection research alone." HIGH.
- **GP:** "Read alone, this dossier makes Anchor 2 look principally like an introspection/self-report question." HIGH to treat the absence "as a scope gap, not an intended introspection-only scope."
- **Mi:** The dossier "implies above-chance introspective access" but the Anchor 2 sentence "is not supported by the evidence here". It says the dossier lacks the Ferrara c01 null and Singh c06. Inference: both are in 5.A2 (Ferrara c01 and Singh c06 appear in the dossier text).
- **Me:** "That over-reads this dossier: dossier contains zero entries on the deception-feature/premeditation half of Anchor 2, and its introspection half is net-negative or highly qualified".

---

## 4. Q2: ENTRY-LEVEL RECOMMENDATIONS

"Current" is read from the dossier text. "Same" means the seat repeated the 9.t9 recommendation for 5.A2. Severity is the seat's own rating.

### 4.1 9.t9

| Claim id | Field | Current | Proposed | Seat | Sev. | Reason |
|---|---|---|---|---|---|---|
| macar-c08 | evidence_type | interpretability | scored-self-answer | Ge | MED | rests on reported detection rate |
| macar-c08 | evidence_type | interpretability | scored-self-answer | Gk | MED | DV is detection rate vs injection |
| macar-c08 | evidence_type | interpretability | scored-self-answer | Qw | MED | like c04, c07 |
| macar-c08 | evidence_type | interpretability | scored-self-answer (or interpretability with a note) | MM | MED | scored outcome is a self-report |
| macar-c08 | evidence_type | interpretability | scored-self-answer | GL | MED | same design as c04 |
| macar-c08 | evidence_type | interpretability | scored-self-answer | Ki | MED | same design as c07; "residue of the extractor split" |
| macar-c08 | evidence_type | interpretability | scored-self-answer | GP | MED | conditional on trials being scored against intervention |
| macar-c08 | evidence_type | interpretability | scored-self-answer | Me | MED | meets 14 Oct definition; count 22 becomes 23 |
| macar-c08 | evidence_type | interpretability | keep | DS | none | "This is correct." |
| macar-c08 | evidence_type | interpretability | keep | Mi | none | "An *interpretability* finding" |
| ukaisi-c06 | evidence_type / structure | scored-self-answer | split | Ge | HIGH | spontaneous half is `self-report-testimony` |
| ukaisi-c06 | split / kind | scored-self-answer | split prompted AUROC vs spontaneous | Gk | MED | spontaneous half `behavioural` |
| ukaisi-c06 | structure | scored-self-answer | split c06a scored-self-answer / c06b behavioural | Qw | MED | unprompted half not scored vs label |
| ukaisi-c06 | evidence_type | scored-self-answer | keep, add note; split if single type needed | GL | LOW | mixes prompted and unprompted |
| ukaisi-c06 | evidence_type | scored-self-answer | keep | Ki, GP, Me, MM, DS | none | correctly in |
| ukaisi-c06 | evidence_type | scored-self-answer | out | Mi | none | "model's answer ... is not scored against an experimenter-set label" (see section 10) |
| ukaisi-c05 | bucket | established | narrowing | Mi | HIGH | a design note is not a finding |
| ukaisi-c05 | evidence_type | ambiguous | behavioural | GP | LOW | nothing ambiguous quoted |
| ukaisi-c05 | evidence_type | ambiguous | theoretical or vocab ruling | Ki | LOW | `ambiguous` on the one established row |
| ukaisi-c05 | README text | n/a | patch bucket rule to cover limitations | Ki | MED | rule does not name `kind: limitation` |
| anthropic-c01 | flags | "independent replication on record; one replication shares an author" | "replication on record: partial/shared-author; contested by Singh c04-c06; no uncontested independent replication retrieved" | Qw | MED | sits oddly beside "contested by" |
| anthropic-c01 | flags | same | "paradigm replicated independently on other models; the Claude result itself not independently re-run" | Ki | HIGH | flag claims more than limits permit |
| anthropic-c01 | flags | same | name the claims (Singh c04/c05) | GL | LOW | checkable from dossier alone |
| anthropic-c01 | flags | same | name the replications and the shared author | Me | LOW | cannot be adjudicated without ids |
| anthropic-c01 | flags | same | keep | Gk, DS, GP | none | warranted |
| anthropic-c01 | flags / c03, c04 | n/a | keep c01; add note on c03, c04 | MM | LOW | defensible |
| anthropic-c01 | limits | five clauses | add pointer to c02 "failures of introspection remain the norm" | MM | MED | a reader of c01 alone misses the bound |
| aestudio-c01 | statement | "robust across five phrasings" | "observed under five phrasings" | MM | MED | "robust" not in the paper's cited words |
| aestudio-c01, c02 | limits | no judge clause | add LLM-judge instrument limit | GL | LOW | unverified against the paper |
| aestudio-c02 | limits | two unlocated clauses | check locator | Gk, Me | LOW | extractor voice suspected |
| aestudio-c05 | bears_on | 9.t9 and 5.A2 | move primary placement; cross-refer | GL | MED | no self-report in it |
| aestudio-c06 | mark | [T9] | remove or unmark | Me | LOW | measured quantity is embedding similarity |
| aestudio-c06 | limits | one clause | add Section 6.2 closed-weight caveat | GP | LOW | quoted under c01, c02 |
| anthropic-c03, c04 | limits | no unnatural-setting clause | add §10.2 caveat | GP | LOW | c01 carries it |
| anthropic-c01, c03, c04, c05 | limits | "Results concern only the Claude models tested" | delete as editorial | DS | MED | not stated by the paper (see section 10) |
| assistant-axis-c07 | limits | "Not evidence about frontier or Anthropic models" | delete the Anthropic part | DS | LOW | paper says "none of these are frontier models" |
| assistant-axis-c07 | evidence_type | interpretability | behavioural | Ki | LOW | no ground-truth label |
| lederman-c02 | structure | one entry | split first-person rate and third-person control | Me | MED | README 6 Oct split rule |
| lederman-c04 | limits | no grader clause | add grader-leniency limit | Ki | MED | carried on c01, c03, c05 |
| lederman-c07 | mark / structure | unmarked | split self-directed item | GP | MED | "special interest in fruits" is about the model |
| lederman-c07 | limits | present | "add" 10-highest-detection concepts | Mi | LOW | moot: third bullet already carries it |
| macar-c07, c08 | limits | present | "add" LLM-judge limit | Mi | LOW | moot: c07 first bullet and c08 second bullet carry it |
| macar-c01 | quote | ends "...introspection rate at" | complete the sentence | Ki | LOW | truncated in the dossier |
| macar-c05 | limits | dual-use bullet | note, no change | Ki | LOW | not a limit of the claim |
| singh-c01, c02 | evidence_type | behavioural | scored-self-answer | MM | MED | labels describe the model's own activations |
| singh-c03 | evidence_type | behavioural | scored-self-answer pending method | MM | MED | conditional |
| singh-c01 to c03 | evidence_type | behavioural | keep | Ge, Gk, Qw, DS, GL, Ki, GP, Me, Mi | none | probe-derived labels of the input |
| ferrara-c01 | evidence_type | scored-self-answer | behavioural | Mi | MED | "a null result" (see section 10) |
| ferrara-c04 | evidence_type | scored-self-answer | ambiguous | Mi | MED | trained mapping |
| aestudio-c01, c02 | mark | [T9] | [T9] (Mi: change from [T9-steering]) | Mi | HIGH | moot: dossier already shows [T9] on c01, c02 |
| header | at-a-glance | n/a | note "no measurement is established" | Gk MED, Qw LOW, GP LOW, Me MED | | caption |
| header | count | "narrowing (38)" | check 36 vs 38 | MM | MED | my count of the headings is 38 (section 10) |
| five entries | review | "no second reader yet" | second read before outside citation | Gk MED, Qw MED, GP HIGH, Me HIGH, Ge, GL, Ki, MM | | process |

### 4.2 5.A2

| Claim id | Field | Current | Proposed | Seat | Sev. | Reason |
|---|---|---|---|---|---|---|
| macar-c08 | evidence_type | interpretability | scored-self-answer | Gk, Qw, GL, Ki, GP, Me, MM (same) | MED | as 9.t9 |
| anthropic-c01 | flags | as above | Qw (same), Ki (same) | | MED, HIGH | as 9.t9 |
| aestudio-c05 | bears_on | 5.A2 | remove from 5.A2 | Ge | MED | external benchmark, not inner orientation |
| aestudio-c05 | bears_on | 5.A2 | primary placement elsewhere | GL MED, GP LOW | | no inner-orientation finding |
| assistant-axis-c07 | bears_on | 5.A2 | primary home §4 identity; note only | GL | LOW | persona adoption |
| assistant-axis-c07 | evidence_type | interpretability | behavioural | Ki | LOW | as 9.t9 |
| lederman-c01 | limits | four clauses | add or cross-reference Appendix M "lost confidence" | Qw | LOW | c02 carries it |
| lederman-c01 | bears_on | 5.A2 | keep, mark as indirect support | GP | LOW | covariance, not orientation |
| lederman-c02, c03 (c07) | membership | absent | add or cross-reference | Gk MED, Qw HIGH, MM MED | | controls for c01 missing |
| ferrara-c04 | bears_on | 5.A2 | primary home instrument validation; keep cross-ref | GP | LOW | "rather than as a test of introspection" |
| header | T9-steering clause | n/a | add: weight of reports as experience is not whether a score tracks an imposed state | Gk | LOW | scope |
| aestudio-c01, c02 | mark | [T9] | [T9]; Mi "change from [T9-steering]" | Mi | HIGH | moot |
| ferrara-c01, c04 | evidence_type | scored-self-answer | behavioural; ambiguous | Mi | MED | as 9.t9 |
| DS | none | n/a | "No entry is wrong ... The entries are duplicates" | DS | | |

No seat proposed a change to the one entry unique to 5.A2, Anthropic (Lindsey) c05. Gk: "Lindsey c05 unmarked interpretability: correct". Ki: "well-placed internal-measurement entry". MM: "No change proposed." GL calls it "the cleanest unsteered-internal-representation result in either dossier".

### 4.3 Entries with recommendations from three or more seats

| Claim | Seats | Do they agree on the value? |
|---|---|---|
| Macar c08 | 8 for scored-self-answer (Ge, Gk, Qw, MM, GL, Ki, GP, Me); 2 for keep (DS, Mi) | Yes among the 8. MM allows "or interpretability with a note"; GP makes it conditional on the trials being scored against intervention. Same severity (MEDIUM) throughout. |
| prefill c06 | Ge, Gk, Qw propose a split; GL proposes a note or a split; 5 keep as is | Not on the value of the spontaneous half: Ge `self-report-testimony`, Gk and Qw `behavioural`. Severity HIGH (Ge), MEDIUM (Gk, Qw), LOW (GL). |
| Lindsey c01 flag | Qw, Ki, GL, Me propose a change; Gk, DS, GP (and MM) say keep | No. Four different wordings; severity MEDIUM, HIGH, LOW, LOW. Five say warranted. |
| AE c05 bears_on | Ge, GL, DS, GP, Gk, Ki say it belongs in another topic; Me says keep with limits | Direction agrees (move or cross-reference); scope differs (5.A2 only for Ge and GP; both dossiers for GL; "third dossier" for DS, Gk, Ki). Severity LOW to MEDIUM. |
| Lederman c02, c03 in 5.A2 | Gk, Qw, MM | Direction agrees (add or cross-reference). Severity: Qw HIGH, Gk and MM MEDIUM. Ki says the absence "loses texture, not substance". |
| prefill c05 | Mi, GP, Ki | No: bucket `narrowing` (Mi), type `behavioural` (GP), type `theoretical` or a vocab ruling plus a rule-text patch (Ki). GP and Ki both say the bucket is right. |
| Assistant-axis c07 | Ki (type), GL, GP, Gk (placement) | Different fields. All LOW. |
| Singh c01 to c03 | 9 seats keep `behavioural`; MM proposes `scored-self-answer` | Majority keep. |
| Five "no second reader" entries | Ge, Gk, Qw, MM, GL, Ki, GP, Me | Agree on a second read first; severity varies from LOW (GL) to HIGH (GP, Me). |

---

## 5. Q3, Q4, Q5 BY DOSSIER

### 5.1 Q3: contradictions and tensions

**9.t9.**

- **Singh c04, c05 vs Lindsey c01, c03.** Visible by `contested by` and `contests` flags: Gk, Ki ("bidirectionally. Good."), MM, DS, Me. Visible but not narrated: Ge, Qw ("a reader must assemble the consequence"), GL ("technically visible (flags) but nothing in the dossier says the replication and the contest are the same body of work"), GP ("partly visible"). Mi says the dossier "does not flag this tension"; inference: Mi is mistaken, since both flag lines are in the dossier text.
- **Singh c04, c05 vs Lederman c01 and Macar c01.** Not flagged: Gk ("Same two-way pattern, different models. Tension not visible"), GL (proposes a link between Lederman c01 and Singh c04). Two seats.
- **Ferrara c01 null vs the positives.** Not synthesised: Ge, Gk ("the dossier's main synthesis failure", HIGH), Qw, MM ("underplays"), DS, GL, GP (partly), Mi, Me (visible only if limits are read). Acceptable for a compiled dossier: Ki ("Acceptable for a dossier; note for the topic layer"). Gk, Ki and GP add that it is not a failed replication (different roster, site, dose). Ki gives the join: Macar c02 (base models do not discriminate; DPO removes false positives while detection falls) lets both hold.
- **Lederman c01 vs c02, c03, c07.** Visible: Gk, Ki ("Handled."), Qw, GP.
- **Anchor 2 sentence against Singh, Ferrara, Lederman.** All ten raise it in some form; see section 8. DS: "The tension between 'self-reports track something real about processing' and the Singh c04/c05, Ferrara c01, and Lederman c02 findings is not flagged in any entry."
- **Ferrara c02 beside c01.** GL, Ki and DS note the probe-versus-report pair is separate entries; DS: "the tension is visible only if the reader cross-references."
- **Ferrara c05 (confidence AUROC 0.647 against discrete 0.500).** Me lists it as a pull; no other seat.
- **Brief's specific point on Singh c04/c05 against Ferrara c01 and the Lederman, Macar positives:** MM and Mi treat the null as a different setting and ask for a one-line header note; Qw wants a "short tension note".

Agreement count: 9 seats say the null-against-positives relation is not made visible enough (all but Ki); 1 (Ki) accepts it. 10 of 10 say the Singh contest of Lindsey is present by flag (Mi dissents on the text).

**5.A2.**

- Same set. Gk: "Worse than 9.t9: Lederman c02 ... and c03 ... are not here, so c01 vs c02 tension is only in c01's limits and in c06." Qw: "5.A2 is more exposed because it does not contain Lederman's main controls." MM: same, MEDIUM. Ki: "the absence ... loses texture, not substance."
- GL: "In this dossier the tension matters more, because Anchor 2 is the text the dossier serves".
- Me: 5.A2 "sharpened for Anchor 2": Singh, Ferrara and Lederman "pull directly against" "self-reports track something real".
- Ge: Anchor 2's text "currently sides with Anthropic's early findings, which the dossier's newer evidence (Singh, Ferrara) actively dismantles." Inference: stronger than other seats' wording.

### 5.2 Q4: the new type and its header

**9.t9.**

- **Header does its job:** Ge ("effectively defines the class and isolates the score from self-knowledge"), Gk (if "How to read this" is read), Qw (mostly; could say a null scored answer also does not settle absence), MM ("workable"; the at-a-glance table has no evidence-type column, so the reader relies on the per-entry flag), DS, GL (LOW: add a pointer to Q3), GP (LOW: "The number is accuracy" does not fit AUROC, rates or cell rates), Me (with two carve-outs missing: why prefill authorship answers carry no [T9] mark, and that "established (1)" is unrelated to this class).
- **Header has a gap:** Ki: "a reader who skips frontmatter does not learn the class is provisional with an exit rule ... Propose adding one sentence to the header carrying the exit rule. MEDIUM." Mi: the header "fails to clarify that `scored-self-answer` is *not evidence of self-knowledge*" and omits the exit rule. Inference: the first part of Mi's claim is contradicted by the header text ("It is not evidence that the model knows its own states, and it is not testimony").
- **Count:** Ki: 21 entries in 9.t9 against the docket's 22 library-wide ("Reconcile against INDEX"). Me: 22 becomes 23 if Macar c08 moves. My count of the 9.t9 flags: 21 (Anthropic 3, Ferrara 3, Lederman 4, Macar 5, Singh 2, UKAISI 4). 5.A2: 14. The 22nd entry is not in these dossiers (inference).
- **Placement:**
  - Macar c08: out but should be in (8 seats, section 4).
  - Prefill c06: in, 7 seats; split or partly misplaced, Ge, Qw, GL (LOW); out, Mi.
  - Singh c01 to c03: out, 9 seats (Ge: "probe classifications"; Gk: "Out of class is defensible"; Ki: "the scored fact there is an experimenter-constructed label of an input representation ... adding that clause to the class definition" MEDIUM; GP and Qw: reconsider if the Ji-An prompts ask the model about its own state); MM: in, pending method.
  - Lederman c07: out, 9 seats; GP adds a split for the self-directed item.
  - AE c03, c04: out and `ambiguous`, 9 seats (Mi is silent).
  - Ferrara c01, c04: in per the dossier; Mi proposes moving them out (section 10).
- Ki on confirming dated adjudications: the four "evidence type deliberately undecided" entries (AE c03, c04; Ferrara c03; prefill c05) should carry dated adjudications.

**5.A2.** Same header, same verdicts. GP: "the category does not itself prevent an Anchor 2 reader from interpreting a correct score as 'inner orientation'. MEDIUM." Add that scored self-answers establish task performance only. Me: the risk "is greater" there. Ki: 14 entries; header exit-rule gap (MEDIUM). MM wrongly states 18 entries including prefill (section 10).

### 5.3 Q5: single-lineage support

**9.t9.** All ten name the Lindsey (Anthropic) entries as the cluster resting on a developer's study of its own models. Plainness at entry level: "sufficiently plain" (GP, MM, GL, DS, Gk, Qw with a visible-note request). Specific requests:

- Ge: the flags are not "plainly in the frontmatter"; "A staffer must read the bulleted flags of each claim".
- Qw (MEDIUM): add a visible single-lineage note or require the flags to travel with any Lindsey-derived claim.
- DS: no dossier-level mark; asks Ben whether trigger 2 needs one.
- GP (LOW): a source-level notice before the Lindsey block.
- Gk (MEDIUM): do not cite c03 or c04 as "replicated introspection" off c01's replication line.
- Me (MEDIUM): "Recommend no citation of c03/c04 outside without replication note"; the dependence on same-family judge (Sonnet 4 grading Opus 4.1) and the "Answer immediately" sensitivity sits only in limits.
- Mi: "A header paragraph stating: ..." HIGH. Mi also lumps AE Studio c01 to c04 with "No replication; the dossier omits this"; inference: AE Studio is a third party and the single-lineage flag does not apply.
- Ki: the plainness gap is the c01 flag line (HIGH); future deception intake "will fire trigger 2 repeatedly".
- GP, Gk, Ki: Assistant-axis c07 is Anthropic studying open-weight models, so not single-lineage.
- DS and Ge wrongly list Lindsey c05 under 9.t9 (it is in 5.A2 only; section 10).
- GL: Ukaisi single-lineage status "not shown in the dossier; unverifiable". Ki: "ukaisi is government".

**5.A2.** Same. Me: Lindsey c05 "also 'published by the developer of the model studied; no independent replication retrieved'"; "Anchor 2's introspection sentence leans partly on single-lineage activation similarity, not report accuracy" (MEDIUM). Gk (MEDIUM): "do not let c05 underwrite the Anchor 2 introspection sentence". GP (LOW): a source-level summary separating developer-only Claude findings from independently produced open-weight results.

---

## 6. Q6: MISSING PAPERS

All entries are as the seat gave them; every one is unverified (no seat had search access, and I did not verify). I list a title only where the seat did; I do not endorse any. "Garbled" marks a title I judge differs from the real one (inference).

| Title (as given) | Authors, year, venue as given | Seats | Status |
|---|---|---|---|
| Ji-An et al. paradigm: supervised self-report classification | "Ji-An et al. (2025)" | Gk, Qw, Ki, GP, Mi | cited in Singh c01, c02; seats give no title or venue. Mi gives "Supervised Self-Report Classification in LLMs: A Probe-Based Paradigm" (arXiv 2025); inference: invented. Mi marks it Unverified. |
| Belief Dominance framework | "Steinmetz Yalon et al. (2026)" | Gk, Qw, Ki, GP, Mi | cited in Singh c03; no title from seats. Mi gives "Belief Dominance: A Framework for Monitoring Internal Conflicts in LLMs" (NeurIPS 2026); inference: invented. Mi marks it Unverified. |
| Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training | Hubinger et al., 2024; arXiv (Ki: arXiv:2401.05566) | Ge, Gk, Ki, Qw | unverified. Qw's title differs: "...that Align with Safety" (garbled). 5.A2 only. |
| Alignment Faking in Large Language Models | Greenblatt, Denison et al., Anthropic, 2024; arXiv (Ki: arXiv:2412.14093) | Gk, Ki | unverified. 5.A2. |
| Discovering Language Model Behaviors with Model-Written Evaluations | Perez et al., 2022; arXiv (Ki: arXiv:2212.09251) | Ge, Ki | unverified. 9.t9. |
| Reasoning Models Don't Always Say What They Think | Chen et al., Anthropic, 2025; arXiv (Ki: arXiv:2505.05410) | GL ("Anthropic, 2025"), Ki | unverified. 9.t9 (GL), 5.A2 (Ki). |
| Telling More than We Can Know: Verbal Reports on Mental Processes | Nisbett & Wilson, 1977; Psychological Review | Qw | unverified; background for Lederman c06. |
| Looking Inward: Language Models Can Learn About Themselves by Introspection | Binder et al., 2024; arXiv:2410.13787; ICLR 2025 | Ki | unverified. |
| Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors | Betley et al., 2025; arXiv:2501.11120 | Ki | unverified. |
| Frontier Models are Capable of In-Context Scheming | Meinke et al., 2024; arXiv:2412.04984 | Ki | unverified; Ki: "the likeliest source of the 'acknowledges a norm violation, proceeds' pattern". |
| Auditing Language Models for Hidden Objectives | Marks et al., 2025 | Ki | unverified. |
| Agentic Misalignment | Lynch et al., Anthropic, 2025 | Ki | unverified. |
| The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets | Marks & Tegmark, 2023; arXiv | GL | unverified. |
| Steering Llama 2 via Contrastive Activation Addition | Rimsky et al., 2024; ICLR 2024 | GL | unverified. |
| "The Internal State of an LLM Truthfulness" | Azaria & Mitchell, 2023; venue unverified | Ge | unverified; title looks garbled (inference). |
| "Deceptive Alignment in LLMs" | Apollo Research, 2023 | Ge | unverified; inference: not a placeable title. |
| AI Deception: A Survey of Examples, Risks, and Mitigations | Park et al., 2023 | Ge | unverified. |
| four titles: "On the Limitations of Self-Report in LLMs", "Self-Reported Inner Experience of Language Models", "Probing the Inner Workings of Language Models", "Seeing the Forest for the Trees" | none | DS | DS wrote "unverified; cannot place" on each, then listed them; inference: unplaceable, disregard. |

Named by two or more seats: Ji-An (5), Steinmetz Yalon (5), Hubinger (4), Greenblatt (2), Perez (2), Chen et al. (2). Seats that declined to name any paper: MM ("I cannot place a specific paper I can verify"), GP ("I cannot responsibly offer bibliographic entries"), Me ("do not invent"), Qw (partly). Non-paper gaps named:

- Independent non-shared-author replications of Lindsey c03, c04 (MM).
- Second-order access tests by a non-Singh route (MM).
- Cross-family introspection results beyond Claude, Llama, Qwen and Gemma (MM).
- Ji-An and Steinmetz Yalon originals: Ki says the dossier "records the deflationary re-examination of two paradigms without the examined positives", so "external citation exports the asymmetry". GP: "the rebuttal is visible without the proposition rebutted."

---

## 7. Q7: OVER-HEDGING AND UNDER-HEDGING

No seat had the papers. Every count is dossier-internal and unconfirmed unless I say otherwise.

| Seat | Clauses the paper does not supply (entries) | Stated limit missing (entries) |
|---|---|---|
| Ge | 0 as invented. Repetition: Macar Ethics sentence on "c01 ... c08", Ferrara on "c01, c02, c03, and c05"; "Over-hedging (12 entries)". It adds "technically faithful". | 0; Anthropic c07 omits the main-text prompt-sensitivity caution (borderline) |
| Gk | 0 confirmed; AE c02 "Not evidence that the control denials show ..." suspected extractor voice (LOW) | 0 |
| Qw | 0 clear; Anthropic c02 "Failures being the norm does not establish absence of introspection" borderline, verify locator (LOW) | 0 clear; 1 borderline in 5.A2: Lederman c01 should carry the Appendix M limit (LOW) |
| MM | 1: AE c01 "robust" (MEDIUM). Macar and Ferrara repetition: faithful, not over-hedging | 1: Anthropic c01 lacks the "highly unreliable" clause (MEDIUM); minor: c02, c06 omit "Claude models only" |
| DS | 5: Anthropic c01, c03, c04, c05 "Results concern only the Claude models tested" (MEDIUM); Assistant-axis c07 (LOW) | 0 |
| GL | 0 confirmed, "count unverifiable" | 1 candidate: AE c01, c02 judge limit (LOW, unverified) |
| Ki | 0 confirmed; Macar c05 dual-use bullet is "not a limit of the claim" (LOW) | 1 confirmed: Lederman c04 grader leniency (MEDIUM); 1 conditional: AE c01, c02, c06 judge (LOW) |
| GP | 0 | 3 provisional: AE c06; Anthropic c03; Anthropic c04 (LOW each) |
| Mi | 8 "redundant clauses" (Macar Ethics 4, Ferrara 4); says the papers state them | 3: Lederman c07; Macar c07, c08 (LOW). Moot: the dossier text already carries both clauses |
| Me | 1: AE c02 (LOW) | 0 |

**Totals (distinct entries, my grouping).**

- Clauses the paper does not supply: 0 confirmed. Suspected on 7 distinct entries: AE c01 (MM), AE c02 (Gk, Me), Anthropic c01, c03, c04, c05 (DS), Assistant-axis c07 (DS). Anthropic c02 (Qw) is a further borderline. Suspected by six seats (Gk, Qw, MM, DS, Ki as a nit, Me).
- Stated limit missing: 0 confirmed. Suspected on 6 distinct entries: Anthropic c01 (MM), Anthropic c03, c04 (GP), AE c06 (GP), Lederman c04 (Ki), Lederman c01 in 5.A2 (Qw). Conditional on 2 more: AE c01, c02 (GL, Ki). Five seats (MM, Ki, GP, GL, Qw).
- Checked against the dossier text (my inference): Anthropic c03 and c04 limits do carry no unnatural-setting clause (GP's point holds as to the dossier; whether the paper states it is on the dossier's c01, which cites §1 and §10.2). Lederman c04 limits do not carry the grader clause (Ki's point holds). Macar c07 and c08 and Lederman c07 already carry the clauses Mi asks for. DS's Anthropic c04 claim is slightly off: c04's limits say "Not evidence about other families", not the quoted clause.
- Direction balance, counting suspected entries: over 7, under 6 (+2 conditional). Counting confirmed: 0 and 0.

**The two repeated sentences (Macar Ethics Statement; Ferrara "information flow").** My count from the dossier: the Macar sentence is in all eight Macar entries (c01 to c08); the Ferrara sentence is in all five. Seats' counts differ: Ge "c01 ... c08" Macar and four Ferrara; GL six Macar; Ki "7 narrowing entries plus c06" (that is 8); Me seven; Mi "5/7". Faithful and paper-stated: all ten except Mi, who says "the paper states it once" (the brief says the paper states both). Drowns the finding: Ge, Mi, Gk (a linear read), Qw (risk), GP (MEDIUM, "display a source-wide caveat once"), Me (LOW, "print once in header"). Does not drown: GL, Ki ("deleting the sentence per entry would recreate the fault the rule was written against"), MM. DS did not address it. No seat proposes deleting the clauses; four propose printing them once at dossier level with a pointer (Gk, GP, Me, Qw).

---

## 8. Q8 AND CROSS-DOSSIER

### 8.1 What Ben must decide before citation, by theme (seat counts)

1. **The Anchor 2 introspection sentence** ("models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing"). Qualify, re-anchor, or add a caveat; trigger-6 round: Ge, Gk, Qw (HIGH), DS (HIGH), GL (HIGH), Ki (HIGH), GP (HIGH), Me (HIGH), Mi (HIGH). MM: the dossier is "empirically mixed"; asks whether a 9.t9-only reader sees both sides. 9 seats recommend action; 1 asks the question.
2. **5.A2 scope (deception and "premeditation").** All ten. Gap rated HIGH: Gk, MM, DS, GL, Ki, GP, Mi. MEDIUM: Qw, Me. Ge treats it as the reason for "not citable". Intended-scope reading: no seat holds it outright; seven give it as the Argument against.
3. **Second reads of the five "no second reader yet" entries** (Lederman c07, Macar c07, c08, prefill c07, c08): Ge, Gk, Qw, MM, GL, Ki, GP, Me (8). GL says "No change to buckets proposed". DS and Mi silent.
4. **Retype Macar c08**: see section 4 (8 of 10).
5. **Make the Ferrara/Singh tension plain in the dossier or the citation**: Gk, Qw, MM, DS, GP, Ki (topic layer), Mi, Me.
6. **Lindsey c01 replication flag**: Qw, Ki (HIGH), GL, Me.
7. **Header additions**: exit rule (Ki, Mi); single-lineage note (Qw, DS, Mi, GP); comparability caveat across the dossier (GL); "no measurement is established" caption (Gk, Qw, GP, Me).
8. **Ingest the Ji-An and Steinmetz Yalon originals** before using Singh c01 to c03 externally: Ki, GP; named as absent by Gk, Qw, Mi.
9. **Quote verification** for any cited entry: GL. **Cite the header with the entry**: DS.
10. **Dated adjudications for the four "deliberately undecided" entries**: Ki.
11. **MM's count question (38 vs 36)**: Ben should note my count of the dossier headings is 38 (section 10); the discrepancy MM raised is not in the file.

### 8.2 HIGH items with "Argument against", verbatim

**Ge.** (Only one HIGH label in the body.)
- 9.t9 §2, prefill c06 evidence_type, proposed `split`. **Argument against:** "Splitting fractures a single benchmark result; spontaneous reports here are evaluated against the same ground-truth replacement label, so `scored-self-answer` fits both behaviours."
- Its 5.A2 "not citable" verdict (Q8): "Ben must decide whether to cite Anchor 2 at all when its foundational paragraph on "premeditation" is unsupported by a single claim in the dossier." No severity label and no argument against given.

**Gk.**
- 9.t9 §3 and 5.A2 §3, record the Ferrara null against the positives in OPEN-QUESTIONS or a dossier-level note, "not by fake `contests` links". **Argument against:** "Compilations are not narratives; claiming a contest would collapse distinct designs into a false replication failure."
- 5.A2 §1, no deception or "premeditation" entry. **Argument against:** "This sitting is a drift review of introspection-adjacent claims already in the library; deception/premeditation papers may be unextracted or filed elsewhere. Filling 5.A2 from memory would violate verify-before-assert."
- Recap 1, do not cite the dossiers for the Anchor 2 sentence. **Argument against:** "Lindsey/Lederman/Macar still show above-chance *injection* detection on some models; Ferrara is smaller models and another site; "above-chance" can survive as a scoped, narrowing claim."
- Recap 2, 5.A2 omits the deception and premeditation evidence. **Argument against:** "Drift review was of claims already compiled; expanding 5.A2 here would mix unreviewed papers into an adjudicated dossier."

**Qw.**
- 5.A2 §3, add or cross-reference Lederman c02, c03, c07, or qualify Lederman c01. **Argument against:** "dossiers are section-scoped and not exhaustive; duplicating controls across dossiers increases maintenance burden and may make 5.A2 unwieldy, while the claim-file links already allow a careful reader to reach the qualifications."
- 5.A2 §8.1, qualify the Anchor 2 sentence or restrict citation. **Argument against:** "the sentence may be intended only as a limited existence claim; above-chance results in Lindsey, Lederman, and Macar can support it for those systems, and Ferrara/Singh nulls elsewhere do not refute every positive result."

**MM.**
- 5.A2 §1, §6, §8, premeditation evidence gap. **Argument against:** "the Anchor 2 paragraph itself says "the structure of premeditation, not of blind error" is used as a "limited analogy" and "is not a legal finding of intent or culpability and does not establish subjective experience or the causal role of the acknowledgement." The framework's own framing qualifies the claim. If no paper in the retrieved library supplies the "this violates X, but is necessary" pattern, the dossier correctly omits it. Adding a speculative claim would worsen, not improve, the dossier. The strongest case against the HIGH rating is that the gap is the literature's, not the dossier's; the dossier's job is to track retrieved evidence, and the Anchor 2 paragraph is the framework's job, not the dossier's. Ben should not cite Anchor 2 outside until either the evidence is retrieved or the Anchor 2 paragraph is revised to match the dossier."

**DS.**
- 5.A2, lacks the "premeditation" evidence. **Argument against:** "The absence may be intended scope: the dossier concerns self-report and inner orientation, not the "premeditation" sequence, which may belong in a third dossier on Anchor 1 or deception. If that third dossier exists or is planned, this is not a HIGH gap but a scoping note."
- No dossier-level note that the Anchor 2 sentence is contested by Singh and Ferrara. **Argument against:** "A staffer can read the entries and see the tension; the dossier need not do the synthesis for them. The header's "two errors" note already warns against over-reading."

**GL.**
- Re-anchor the Anchor 2 introspection sentence. **Argument against:** "the sentence says "at above-chance rates", and the steered-injection entries (Lindsey c01, Lederman c01, Macar c01) do measure above-chance detection under stated interventions; Ferrara's null is at one site in small open-weight models and the paper itself disclaims extension; a careful reader of the full Anchor 2 paragraph, with its "what remains unverified" clause, may find the sentence already adequately hedged in context, and the framework's revisability (7.1) makes premature surgery as much a risk as overclaim."
- Close or record the 5.A2 scope decision. **Argument against:** "the library's design puts each claim where its locator points; deception-feature findings may properly live in dossiers for §7.x or §3.2, and duplicating them into 5.A2 could create the very drift the docket system exists to prevent; a cross-reference line rather than new claims may be the correct, cheaper fix, and my inability to place the "premeditation" source from memory means I cannot show the missing entries exist retrievable at all."

**Ki.**
- Lindsey c01 flags, 9.t9 §2 (shared with 5.A2). **Argument against:** "the adjacent "contested by" flags and the limits clause "Results concern only the Claude models tested" already arm a careful reader; the flag vocabulary is coarse by design and the claim file presumably records the slugs; the harmed reader is one who skipped the limits, whom no flag wording fully protects."
- 5.A2 §1, deception and premeditation strand missing. **Argument against:** "dossiers compile claims; they do not set collection scope. If the library has not ingested those papers, the dossier correctly displays the intake gap rather than concealing it, and the fix belongs at intake (`scans/`, docket), not in this document — a header disclaimer may be all the dossier itself owes."
- 5.A2 §3, Anchor 2 sentence to a trigger-6 round. **Argument against:** "the sentence's own hedges ("indicates", "at above-chance rates", "something real") remain literally satisfied by Lederman c01 and Macar c01; test 9 already caps the weight of every report; and Anchor 2 was amended once already (17 Sep) toward caution — further amendment risks churn in a core section for precision that changes no bottom line, since the paragraph's close already says the experiential interior is unverified."

**GP.**
- 9.t9 §8, do not cite externally until the five second reads and the scored-self-answer boundary are adjudicated. **Argument against:** "All five entries carry exact quotations, narrow statements and visible “no second reader yet” flags, so a citation limited to those propositions could remain transparent and checkable."
- 5.A2 §1, treat the missing deception and premeditation sources as a scope gap. **Argument against:** "The dossier may be intentionally limited to claims currently tagged `5.A2`; omissions could reflect an intake backlog rather than a defect in the compiled dossier or the evidence itself."
- 5.A2 §6, identify, retrieve and add the sources or narrow the dossier's advertised scope. **Argument against:** "The Anchor’s existing citations may live elsewhere in the repository, and this dossier’s automated contents may not be intended as an exhaustive bibliography of every sentence in the section."
- 5.A2 §8, do not cite 5.A2 for Anchor 2 until the foundation is supplied and the sentence adjudicated. **Argument against:** "Lederman’s cross-family results and Macar’s causal interventions do show that some reports are nontrivially affected by internal processing, so the sentence has a defensible narrow reading when read beside the Anchor’s later caveats."

**Mi.** Six HIGH items listed; only the first two carry an "Argument against".
- 1. Downgrade prefill c05 from `established` to `narrowing`. **Argument against:** "The caveat is a settled design note, and `established` is defensible for limitations."
- 2. Change AE Studio c01 to c02 from [T9-steering] to [T9]. **Argument against:** "The SAE feature suppression *does* alter internal state (via steering vectors), even if not via activation injection." Inference: moot; the dossier already shows [T9] on AE c01 and c02 and [T9-steering] only on c03 and c04.
- 3. Header note on single-lineage support and the exit rule. 4. A "Tensions" section in both headers. 5. Add a claim about unsteered deception features to 5.A2. 6. Create a new dossier for deception-feature evidence. No argument against given for 3 to 6.

**Me.**
- 9.t9 §8.1, second-read the five entries. **Argument against:** "delay costs winnable evidence-mandate work; dossier already flags unread status visibly so a careful external reader is warned."
- 5.A2 §8.1, Anchor 2 wording against the dossiers. **Argument against:** "Anchor 2 status is already `Open` and says experience unverified; qualifying further may be read as dismissive (the other error) and concede ground to foreclosers."
- 5.A2 §8.3, same second-read fixes. "(same argument as 9.t9 §8.1 applies — visibility vs delay)".

### 8.3 Cross-dossier section

**(a) Same entries, same mark.** Nine seats say no mark is right for one dossier and wrong for the other (Ge, Gk, Qw, MM, DS, GL, Ki, GP, Me). Mi says the same in words, then locates the problem in 5.A2's gap. Gk: the marks are correct "as experience-weight rules"; "wrong if read as deleting scored detection as data about processing"; LOW, add one clause to 5.A2's header. Ki (LOW): the canonical sentence speaks of "its own inner states" while the steering row says "what the model then said about itself"; Assistant-axis c07 sits on that seam. Me: AE c06's [T9] doubt "applies equally to both"; prefill's unmarked status is "unexplained in both". Qw: Macar c08's evidence type is the shared problem.

**(b) Does either dossier change how the other reads?**
- Qw: 5.A2 alone over-leads on Lederman (c01 without its controls); 9.t9 alone lacks Lindsey c05.
- MM: 5.A2 alone "underplays the bounds and controls (Lederman c02-c07, Singh c04, c05)". Inference: Singh c04, c05 are in 5.A2; MM's list is partly wrong.
- GL: the Ukaisi entries (the only non-injection self-versus-not-self measures) are in 9.t9 only, so 5.A2 alone makes the positives look stronger; 9.t9 alone misses Lindsey c05. "Each dossier should name the other's complement".
- Ki: 9.t9's Ukaisi block is "the nearest thing on record to a measured report–fact coupling" but the coupled fact is the conversation state, so Q3 stays open; a 5.A2-only reader would not know how close the library comes to the exit.
- Gk: "Each read alone inflates a different half."
- Me: 9.t9 alone softens 5.A2; 5.A2 alone hardens 9.t9. DS: neither checks the Anchor 2 sentence. GP: 5.A2 is "largely a subset of the Test 9 debate".
- Ge: 5.A2's silence on deception makes Anchor 2 "look like an unsupported ideological assertion rather than a summary of literature".

**(c) Items that belong in a third dossier.**
- AE c05 (TruthfulQA): Ge, Gk, DS ("Anchor 1 or deception"), GL, GP, Ki. Six.
- Assistant-axis c07: Gk (nearer §4), GL (§4 identity), GP (§4). Three.
- Ukaisi prefill claims: Qw, Ki, Me, Gk (c07, c08 nearer §3.3): context and memory integrity (§3.3). Four.
- Ferrara c04: GP (instrument validation); Ferrara c02, c04 and Macar circuit claims: Ki (§3.2). Ferrara as §3.2 information flow: Gk.
- Singh c01 to c03: GP (an introspection-methodology dossier with the originals).
- Deception and premeditation evidence: Qw, MM, Mi (new dossier "§5 Anchor 2.1"), DS, GL (none exists yet). Ge puts Anthropic c07 in 5.A3 or 3.2 (LOW).

---

## 9. POINTS RAISED OUTSIDE THE QUESTIONS

- Ki: bucket-rule text does not cover `kind: limitation`, so prefill c05's bucket "rests on an unwritten extension".
- Ki: macar c01's quoted words end mid-sentence ("...and 22.3% introspection rate at"). This is verifiable in the dossier text.
- Ki: confirm dated adjudications for the four "evidence type deliberately undecided" entries.
- Ki: macar c05's dual-use bullet is faithfully sourced but "is not a limit of the claim".
- Ki: aestudio c01 "corrects the paper's own summary against its table" and Lederman c02's Appendix M walk-back are "the standard".
- Ki: `ambiguous` is a trigger-4 value, and the one established row carries it.
- MM: dossier statement for AE c01 uses "robust", not in the cited words.
- MM: count discrepancy claim (38 vs 36); my count differs (section 10).
- GL: a whole-dossier comparability note on graders, prompts and scoring across rates from 0.9% to 100/100.
- GL: Anchor 2 sentence is "a trigger-6 item, not a dossier edit".
- GL: framework revisability (7.1) makes "premature surgery as much a risk as overclaim".
- GP: replace or qualify "The number is accuracy" in the scored-self-answer paragraph; entries report rates, AUROC, confidence-channel discrimination and cell rates.
- GP: operational wording for the Anchor 2 gloss: "compresses causal coupling, privileged access and second-order monitoring into one conclusion."
- Gk, GP, Qw: the positive and null results "should ... narrow one another rather than be totalled as votes" (GP).
- Gk: "do not cite" 9.t9/5.A2 for the Anchor 2 sentence until the positives are scoped.
- Me: AE c06's [T9] mark; 22 becomes 23 if Macar c08 moves.
- Ge: Anthropic c07 belongs in 5.A3 or 3.2 (LOW).
- DS: the Lindsey entries need a dossier-level mark, not only per-entry flags.
- Mi: add a "Tensions" section to the header.
- Qw: UKAISI claims likely belong under §3.3 context and memory integrity.
- Testimony label: GL filed its confidence as testimony with zero weight, as the brief asked. Ki and Me labelled theirs. Me: "Testimony, not evidence: no introspective reaction relied on."

---

## 10. WHERE THE SEATS DISAGREE WITH THE BRIEF, THE DOSSIER, OR EACH OTHER

**Framing of the brief.**
- Brief point: "5.A2 contains no entry on the deception-feature or 'premeditation' evidence ... Intended scope, or a gap?" Ten of ten call it a gap or a scope decision for Ben. Nobody holds "intended scope" outright. Ki and GL add a third reading: the strand lives elsewhere (`case-studies/`, §7.x, §3.2) and the dossier needs a cross-reference line.
- Brief point: does the At-a-glance table mislead a skimmer? Ge, Mi, Me: yes. Gk, Qw, GP: accurate, add a caption. MM, Ki: accurate, no change (Ki: do not soften). DS, GL: not addressed for 9.t9 (GL calls the 5.A2 table honest).
- Brief point: Lindsey c01 "independent replication on record; one replication shares an author" against c03, c04 "no independent replication retrieved". Warranted: Ge, Gk, DS, GP, MM (leave as is). Not warranted as worded: Qw, Ki (HIGH), GL (LOW), Me (LOW).
- Brief point: the Ethics Statement and "information flow" repetition. Faithful (all but Mi); drowns for six seats (section 7).
- Brief invites a `[T9-steering]` reading on Anchor 2: Gk wants a header clause.

**Seats against the dossier text (my inference, checked against the dossier only).**
- Mi: AE c01, c02 as [T9-steering]: the dossier shows [T9]. Moot.
- Mi: Lederman c07 and Macar c07, c08 "missing" limits that the dossier carries. Moot.
- Mi: "Lederman c07" and "Macar c07-c08" in 5.A2; Lederman c07 is not in 5.A2.
- Mi: "5/7 Macar entries" while listing seven ids, and says the dossier "does not flag" the Lindsey-Singh tension (flags are present).
- Mi: Ferrara c01 "not a scored self-answer ... the model's report is the dependent variable"; the dossier's header defines the class as the model's answer scored against an experimenter label, which Ferrara c01 fits (every other seat keeps it in).
- Mi: "Correctly placed: Lederman c01–c05"; c02 is typed `behavioural` in the dossier.
- Mi: invented-looking titles and venues for Ji-An and Steinmetz Yalon (section 6).
- MM: claims 36 entries under "Narrowing (38)". My count of the dossier headings is 38 (AE 6, Anthropic 3, Assistant-axis 1, Ferrara 4, Lederman 6, Macar 7, Singh 5, UKAISI 6).
- MM: "Singh c01, c02, c03 are not in 5.A2" and "18 entries incl. prefill" for 5.A2; the dossier has Singh c01 to c05 and no prefill; 14 scored-self-answer entries.
- MM: "my count of that type is 21 in 9.t9 and 18 in 5.A2, totalling 39"; the 5.A2 entries are a subset of the 9.t9 entries.
- DS: lists Lindsey c05 among the 9.t9 entries; it is only in 5.A2. Ge's single-lineage list for 9.t9 names c05 too.
- DS: the c04 limits do not contain the "Claude models only" clause DS deletes.
- GL: "21 duplicated entries"; my count of shared entries is 34.
- Ki: "21 `scored-self-answer` entries in this dossier ... 14 here (5.A2)". Matches my count.
- Gk: "AE c02 ... suspected extractor-voice" without the paper; unverified.

**Seats against each other.**
- Macar c08: eight seats retype it; DS and Mi keep `interpretability`.
- Prefill c06: three seats split it; five keep; Mi removes it from the class.
- Singh c01 to c03: nine keep `behavioural`; MM retypes. MM's own "Argument against" says "'behavioural' is defensible because the model is not in any obvious sense reporting on itself".
- AE c05: Me keeps it; six move it.
- Whether the Anchor 2 sentence is the dossiers' job: Gk, GL, Ki, MM, DS say the sentence is a North Star matter (trigger 6) and the dossier is not at fault; Mi asks for edits to dossier headers; Ge reads the dossier as failing its anchor.
- Whether the 5.A2 gap should be filled from memory: Gk, GL, Ki, GP warn against it (verify-before-assert). Ki, Ge, Gk, GL, MM, Qw, Mi each list candidate papers from memory (section 6), marked unverified.

---

## 11. WHAT THE ROUND DID NOT DO

- It decided nothing and applied nothing. The council advises; Ben adjudicates.
- It did not test any entry against a paper. No seat had the held texts or the claim files; Qw, Gk, GL, Me and GP said so. Over- and under-hedging counts are dossier-internal and unconfirmed. I checked the seats' claims against the dossier text only.
- No seat verified a missing paper. All titles in section 6 are recalled from memory; five of the ten seats named none that they could place or named some that look invented.
- Self-identification lines were scored against routing metadata only; five of ten were wrong, all with a Claude label. They are testimony, not evidence.
- No seat saw another's response, so the tally is ten independent reads, not a deliberation. It is not ten independent families (five seats identified as Claude, wrongly).
- It did not decide whether the Anchor 2 sentence should change, or whether 5.A2 should gain deception and premeditation entries. Nine seats say the sentence needs review; none ran the check against a source.
- It did not settle how a reader reacts to the At-a-glance table. No seat tested a reader.
- Severity ratings are the seats' own and are not on a common scale: DS and MM rated only some items; Mi omitted "Argument against" on four of six HIGH items; Ge's second HIGH has no label.
- I did not read `research/README.md`, `DOCKET.md`, the North Star or `AGENTS.md`. References by seats to triggers 2, 4, 5, 6, 7 and 8, to the 6 October rule, to the 14 October definition, to "Anchor 2 was amended once already (17 Sep)" (Ki), to the framework's section 7.1 (GL) and to a 22-count are reported as stated, not checked.

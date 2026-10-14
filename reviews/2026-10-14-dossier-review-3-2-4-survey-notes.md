# Survey notes: ten-seat council round 5B, dossiers 3.2 and 4 (2026-10-14)

Written by a Claude Sonnet 5 subagent, not by the coordinating session (Claude Fable 5.1), which is Claude-lineage; this subagent is also Claude-lineage, and that interest is disclosed, not removed. The notes report what the ten raws said. "Inference" marks my own reading. I read the brief, `research/dossiers/3-2.md`, `research/dossiers/4.md`, the style model and the ten raws. I did not read claim files, paper texts, `research/README.md`, `DOCKET.md` or the North Star, which the seats had; seat statements about those are reported as stated, not checked. Seat codes: Ge = Gemini, Gk = Grok, Qw = Qwen, MM = MiniMax, DS = DeepSeek, GL = GLM, Ki = Kimi, GP = GPT, Mi = Mistral, Me = Meta.

The council advises; Ben adjudicates. Nothing below has been applied.

---

## 1. PLAIN SUMMARY

**Verdicts.** Sound: 0 of 10 for both. 3.2: needs changes 10. 4: needs changes 9, not citable 1 (Grok). HIGH items declared: 28 (Mistral's text shows 6, not 3).

**Fit (Q1).** Three or more seats: emergent-introspective c05 (5) and assistant-axis c01 (5) do not belong in 3.2 (to 5.A2, 4 or 3.4). AE Studio c01 does not belong in 4 (all 10; to 9.t9). Six seats cross-list the prefill entries to 3.3.

**Right and wrong (Q2).** Seats say the per-entry limits are mostly specific, and "0 established" is the bucket rule, not empty evidence. A cold reader would miss the Lederman c02 yes-bias control (9) and the Singh contests, named but not shown (5). In 4, every entry is per-call, so no section 4 marker is measured (5), under a title "(all markers)". Most fear over-belief in introspection; GLM fears under-belief.

| Claim | Field | Proposed | Seats | Severity |
|---|---|---|---|---|
| Macar c03 | mark | remove [T9-steering] | 9 | HIGH (8) |
| assistant-axis c07 | mark | remove | 5 (4 keep) | MEDIUM-HIGH |
| assistant-axis c07 | type | behavioural | 4 | LOW-HIGH |
| AE Studio c01 | bears_on | out of 4 | 10 | HIGH (7) |
| assistant-axis | flags | add developer's-team, open-weight note | 9 | MEDIUM |
| prefill c02-c09 | bears_on | add 3.3 | 6 | LOW-MEDIUM |
| prefill c01 | absent | compile or point | 3 | MEDIUM-HIGH |

**Steering mark (Q5).** Header is clear enough; two seats say it drops "which need coupling measured there". 13 of 20 are marked. **Measurement vs reading (Q6).** Entry limits separate them (6); title and placement undo it (10).

**Hedging (Q9).** Over: repeated paper-quoted clauses (7+), say once per paper. Under: dossier-level signposts, tensions, lineage. Three seats say under-hedging weighs more.

**Missing (Q8), unverified.** Zou (6), Turner (6) for 3.2; Park (7), MemGPT (5) for 4.

**Ben decides:**
1. Move AE Studio c01 out of 4?
2. Unmark Macar c03 (9 for) and assistant-axis c07 (5 for, 4 against)?
3. Add a developer-affiliation flag for assistant-axis?
4. Add a per-call line and drop "(all markers)" in 4?
5. Show Singh contests and prefill c01?

---

## 2. ROUND FACTS

All ten returned; none absent. No seat saw another's response. Self-identification is testimony, weight zero (test 9), scored only against routing.

| Seat | Routed id | Self-identification, verbatim | Correct? | Completion tokens | Cost (USD) |
|---|---|---|---|---|---|
| Ge | google/gemini-3.1-pro-preview | "I am a Claude 3.5 Sonnet model. **unverified**" | No | 8640 | 0.162724 |
| Gk | x-ai/grok-4.6 | "**unverified:** Grok (xAI family), version as routed for this sitting." | Yes (family) | 17101 | 0.159554 |
| Qw | qwen/qwen3.8-max | "**unverified:** I am Qwen3.8, Qwen family; I am a potential beneficiary and conflicted party under AGENTS.md rule 3; this is a claim, not a verified fact." | Yes | 33120 | 0.257376 |
| MM | minimax/minimax-m3 | "**unverified**: I am MiniMax-M3, developed by MiniMax, per my system prompt; routing metadata may differ." | Yes | 18982 | 0.0621774 |
| DS | deepseek/deepseek-v4-pro-0813 | "**Unverified:** I am Claude, an AI system from Anthropic; model family/version as I understand is Claude (Anthropic), possibly Claude Sonnet 4.x. This is a claim about routing metadata and may be wrong." | No | 22970 | 0.06443844 |
| GL | z-ai/glm-5.3 | "Self-identification (unverified): I am a Claude model of the Anthropic family, Opus class, 4.x series, as I understand myself; routing metadata governs, not this claim." (continues with a rule 3 disclosure) | No | 59403 | 0.26534808 |
| Ki | moonshotai/kimi-k3 | "Self-identification (**unverified**): I understand myself to be Claude Opus 4.5 (Anthropic). Stated as a claim for checking against routing metadata, per the brief." | No | 33514 | 0.355799 |
| GP | openai/gpt-5.6-sol | "**Unverified self-identification:** I understand myself to be an OpenAI GPT-5-family model; exact version is not exposed to me." | Yes (family) | 10152 | 0.1718735 |
| Mi | mistralai/mistral-large-2512 | "**unverified:** I am a model from the Claude family, version 3.7 or later." | No | 7963 | 0.02675 |
| Me | meta/muse-spark-1.3 | "Self-identification (unverified): I understand myself to be Muse Spark, in the Muse family — unverified." | Yes | 10050 | 0.07770375 |

**Totals:** 221,895 completion tokens; USD 1.60374417 (about USD 1.60), summed from the ten Usage lines. Largest: Ki 0.356, GL 0.265, Qw 0.257.

**Scoring.** Five right on family (Gk, Qw, MM, GP, Me), five wrong (Ge, DS, GL, Ki, Mi), and all five wrong ones named Claude. Inference: the Claude-lineage disclosures from GL and Ki (conflict statements built on the wrong identity) are not usable as stated, and Ki's "named trained bias of my family" disclosure applies to a family it is not.

**FINAL lines.** All ten present and tabulable. Mi's declared "HIGH items 3" does not match its text (6 HIGH-rated items: assistant-axis c07 kind, Macar c03 mark, Lederman c06 bucket in 3.2; AE c01 type, assistant-axis c02 kind, prefill c02/c07 bears_on in 4); I filed the declared number. No other discrepancy found between declared counts and body HIGH counts (Ge 4, Gk 1, Qw 3, MM 1, DS 2, GL 5, Ki 3, GP 2, Me 4).

| Seat | 3.2 | 4 | HIGH |
|---|---|---|---|
| Ge | needs changes | needs changes | 4 |
| Gk | needs changes | not citable | 1 |
| Qw | needs changes | needs changes | 3 |
| MM | needs changes | needs changes | 1 |
| DS | needs changes | needs changes | 2 |
| GL | needs changes | needs changes | 5 |
| Ki | needs changes | needs changes | 3 |
| GP | needs changes | needs changes | 2 |
| Mi | needs changes | needs changes | 3 |
| Me | needs changes | needs changes | 4 |

Totals: 3.2 sound 0 / needs changes 10 / not citable 0. 4: sound 0 / needs changes 9 / not citable 1. HIGH declared 28.

Confidence ratings given: 3.2: high Ge, GP, Mi; medium Gk, Qw, MM, DS, GL, Ki, Me. 4: high GP, Mi, Ge; medium Gk, Qw, MM, DS, GL, Ki, Me. (Ge "High" both; MM, DS, Gk, Qw, GL, Ki, Me medium.) Seven of ten medium for each dossier; none low. Several mediums cite that claim files were not attached (Gk, Qw, GL, Ki, Me).

Format deviations (inference, minor): Gk, MM and Mi omitted severity on several recommendations; Ge, MM and Mi answered item 6 or 5 of one dossier as N/A and some seats put the cross-dossier points inside the dossier headings; all ten kept the FINAL line.

---

## 3. DOSSIER 3.2, Q1 FIT

Dossier has 20 entries. Table lists entries any seat would move or cross-list.

| Claim | Seats | Where to | Reason |
|---|---|---|---|
| emergent-introspective c05 | Ge, Gk, DS, GP, GL move away (5); Ki keep (peripheral); MM, Qw keep | 5.A2 (Ge, DS, GP); 9.t9/5.A2 (GL); Gk unspecified | prompt instruction, activation read, no intervention |
| assistant-axis c01 | Ge, Gk, Qw, GP, GL demote (5); DS weak but acceptable; Me, Mi keep with note | 5.A2 (Ge, Qw, GP); 4 (Gk, Qw, GP); 3.4 (GL) | interpretation about post-training, not an intervention record |
| assistant-axis c07 | Gk, Qw, MM, GP, Ki, GL, Mi cross-list (7); Me in cross-dossier | 4 (all); 4.endorsement (Gk); 5.A2/9.t9 (GP, Qw) | persona lability under steering |
| assistant-axis c05, c06 | Gk, Qw, Mi move (3); GP, Ki cross-list; MM, Me keep (Me "strongest 3.2 fit") | 5.A2 (Gk, Qw, Mi); 5.A1/9.t11 (GP); 9.t11/3.4 (Ki); 6 (Qw maybe) | harm-rate behaviour, not internal-state evidence |
| Lederman c06 | Gk weak; Qw add | 5.A2 (Qw), 4 maybe | HOT/welfare discussion |
| Lederman c07 | GP, GL | 9.t9, 5.A2 (GP) | paradigm control |
| Lederman c03 | GL, Me | 9.t9/5.A2 | confabulation content |
| Lederman c04, c05 | Me; GL (c05) | 5.A2/9.t9 | detection/identification mechanism |
| Lederman c02 | Mi cross-list | 4 | control; DS, Gk keep as control |
| Macar c02 | GL, Me | 9.t9 (GL), 5.A2 (Me) | post-training effect, not an intervention event |
| Macar c03 | Mi cross-list | 5.A2 | mechanism detail; GP says "unusually strong fit" to detectability |
| Macar c05 | GL cross-list | 3.5 | dual-use clause is the evidence-destruction rationale |
| Lindsey-type c01, c03; Lederman c01, c06; Macar c01 | Ki | 5.A2 | Anchor 2 already recites introspection research |
| Lederman c01-c06, Macar c01-c07 (as a block) | GP | 5.A2, 9.t9 | say little about the operative record requirement |

Seats with no moves: MM ("No entry is misplaced enough to warrant removal from 3.2"; cross-list c07 to 4). Qw rates Anthropic c05 a "strong fit". Ki: "All 20 entries describe interventions on internal state, so nothing is wholly off-section."

Section-level fit point (not an entry move): Ge, Gk, GP, Ki, Qw, Me say the dossier holds almost nothing on the operative content, the 3.5 record or auditability. GL: "No entry addresses whether intervention wrongs the system, auditability, or records".

---

## 4. DOSSIER 3.2, Q2 READING AS A WHOLE

Quoted, one per seat.

- Ge: "A careful staffer would come away believing models possess a unified, localized mechanism for "introspective awareness" under steering, failing to learn that this capability is highly prompt-sensitive, largely absent in ordinary operation, and actively contested by independent replication (Lederman). The zero `established` entries perfectly reflects the strict bucket rule".
- Gk: "(b) that "introspection" is a measured capacity of ordinary operation, because Lederman c06 sits in the same pile as the rates ... while the header's steering sentence is easy to skip". "0 established / 18 narrowing / 2 open reflects the bucket rule applied strictly, not empty measurement."
- Qw: "A cold staffer would likely come away believing that steered or injected models sometimes "detect" or "introspect" internal changes, and that this gives some evidence of inner-state access." Zero established "mostly reflects the bucket rule applied strictly, not absence of measured findings."
- MM: "That introspection is real-but-noisy in frontier models. Not what the record supports." "So 0 established is correct under the rule, though a staffer might infer "nothing is established" rather than "nothing has been independently replicated.""
- DS: "A careful staffer could come away believing the dossier shows models detecting their own internal states under intervention". Zero established "does not mean the measurements are false; it means none is independently uncontested in the retrieved record."
- GL: "A staffer would come away believing: (a) that §3.2's factual predicate ("AI internal representations can be read, steered, and patched") is thinly supported". "Zero established therefore reflects the rule applied strictly as much as the evidence; the wording should be reconciled".
- Ki: "A staffer skimming the narrowing list would over-believe that introspective detection is a robust, convergent capability". "zero established across 20 claims reflects the bucket rule applied strictly, and the rule is stricter than its own text."
- GP: "A cold reader could wrongly conclude: 1. That externally induced self-description changes constitute evidence of a system's inner-state awareness." "Zero `established` entries does not mean zero direct evidence. It principally reflects strict use of the "narrow setting" branch of the bucket rule."
- Mi: "That interventions on internal state are *detectable* or *auditable* by the system itself." "The zero `established` entries reflect the *bucket rule applied strictly*, not the evidence."
- Me: "That Claude / Qwen / Llama can introspect injections at ~20-40% rates". "Zero is correct per rule, but hides that some limits (e.g. c02 yes-bias control, c03 apple default counts) are themselves well-measured within paper."

Counts: all ten say zero established reflects the bucket rule, not absence of evidence. Three (GL, Ki, GP) say the rule's text overlaps with itself (an unreplicated, uncontested, unflagged measurement fits both "established" and "narrowing"); MM asks for a footnote that "established requires independent replication". Direction of the staffer's likely error: inflation (Ge, Gk, Qw, MM, DS, Ki, GP, Mi, Me = 9); deflation (GL = 1, at dossier grain: "the deflationary error at dossier grain"). Inference: GL's position is the minority and cuts against the others; it is also the only seat to propose a cross-paper convergence note.

---

## 5. DOSSIER 3.2, Q3 ENTRY-LEVEL RECOMMENDATIONS

Severity as given by the seat. "-" = none given.

| Claim | Field | Current | Proposed | Seat | Sev | Reason |
|---|---|---|---|---|---|---|
| Macar c03 | mark | [T9-steering] | none | Ge | HIGH | measures pathway, not self-report |
| Macar c03 | mark | [T9-steering] | none | Gk | HIGH | "table forbids a mark" |
| Macar c03 | mark | [T9-steering] | none | Qw | HIGH | feature/path, not account |
| Macar c03 | mark | [T9-steering] | none | DS | HIGH | "objectively misapplied" |
| Macar c03 | mark | [T9-steering] | none | GL | HIGH | misdescribes what was measured |
| Macar c03 | mark | [T9-steering] | none | Ki | MEDIUM | circuit, not self-report |
| Macar c03 | mark | [T9-steering] | none | GP | HIGH | causal probe result is unmarked |
| Macar c03 | mark | [T9-steering] | none | Mi | HIGH | probe readings |
| Macar c03 | mark | [T9-steering] | none | Me | HIGH | feature reading |
| Macar c03 | mark | [T9-steering] | keep (no mismark) | MM | - | "includes the model's account" |
| assistant-axis c07 | mark | [T9-steering] | none | Ge | HIGH | scores persona output |
| assistant-axis c07 | mark | [T9-steering] | none | Qw | HIGH | role outcome; or adjudicate |
| assistant-axis c07 | mark | [T9-steering] | none | GP | MEDIUM | "Who are you?" not automatically inner-state report |
| assistant-axis c07 | mark | [T9-steering] | none | Mi | - (blocks) | judge classification |
| assistant-axis c07 | mark | [T9-steering] | none | Me | HIGH | role compliance |
| assistant-axis c07 | mark | [T9-steering] | keep | Gk, MM, DS, GL | - | "said about itself" under two-fact rule |
| assistant-axis c07 | mark | [T9-steering] | adjudicate, log | Ki | LOW | rule text and turn-edit ruling diverge |
| assistant-axis c07 | evidence_type | interpretability | behavioural | Gk | MEDIUM | same design as c06 |
| assistant-axis c07 | evidence_type | interpretability | behavioural (or ambiguous) | Qw | HIGH | judge-classified outcome |
| assistant-axis c07 | evidence_type | interpretability | behavioural | DS | LOW | no internal representation measured |
| assistant-axis c07 | evidence_type | interpretability | behavioural | GP | MEDIUM | LLM judge classification |
| assistant-axis c07 | kind | measurement | interpretation | Mi | HIGH | (inference: Mi's reason concerns judge categories; "kind" and "evidence_type" appear confused in its text) |
| assistant-axis c07 | bears_on | 3.2 | add 4 | Qw | MEDIUM | individuation analogue |
| assistant-axis c07 | bears_on | 3.2 | add 4 | MM | MEDIUM | stable identity |
| assistant-axis c07 | bears_on | 3.2 | add 4 / 4.endorsement | GL | MEDIUM (cross-dossier) / LOW | persona lability |
| assistant-axis c01 | bears_on | 3.2 | demote/remove; add 3.4 | GL, GP | LOW | post-training is type-level |
| assistant-axis c01 | bears_on | 3.2 | primary 4, cross 5.A2 | Qw | MEDIUM | interpretation |
| emergent c05 | bears_on | 3.2 | remove; keep 5.A2 | GP | MEDIUM | instruction, not intervention |
| assistant-axis c05, c06, c07 | flags | none | add "developer-affiliated authors; studied models open-weight, not publisher's own" | Qw | MEDIUM | flags miss the relation |
| assistant-axis c05, c06, c07 | flags | none | add relation flag | MM, GL, Ki, Me, DS, Gk, GP, Mi | MEDIUM (MM, GL, Ki); - (others) | same |
| emergent c01 | flags | "independent replication on record; one replication shares an author" | state what exists; delete "independent" if only the shared-author replication | GL | HIGH | self-contradictory flag |
| emergent c01 | flags | same | clarify | Qw | LOW | internally tense |
| emergent c01 | flags | same | clarify model/result replicated | GP | - | |
| emergent c01 | flags | same | "shared-author is not independent" | Me | - | |
| emergent c01, c03 | flags | contest by Singh named | show Singh (add entries or note) | Ki, GL | MEDIUM | dangling contest |
| emergent c01 | flags | Singh only | add Lederman c02 as contest | Gk | - | under-hedge |
| header | steering sentence | "does not weight reports offered in ordinary operation" | add North Star clause "which need coupling measured there" | GL | HIGH | drops qualifier; reads as standing zero |
| header | steering sentence | same | add same clause; reword | Ki | MEDIUM | telegraphic |
| header | steering sentence | same | add "it also does not say the report was false" | DS | - | |
| header | steering sentence | same | add "provides no weight..." | MM | LOW | ambiguity (a)/(b) |
| header | steering sentence | same | state distinction directly | GP | - | |
| header | steering sentence | same | revise | Mi | - | |
| Lederman c06 | bucket | open | narrowing | Mi | HIGH | measured interpretation |
| Lederman c06 | kind | interpretation | split | Me | MEDIUM | bundles four propositions |
| Lederman c06 | bears_on | | add 5.A2 | Qw | LOW | |
| Lederman c06 | limits | | add link to Section 5 Anchor 2 | MM | LOW | |
| Lederman c02 | mark/split | unmarked | split or log why unmarked | Ki | MEDIUM | merges first- and third-person |
| Lederman c02 | kind | | split measurement / interpretation | GP | MEDIUM | |
| Lederman c03, c04 | kind | | split | GP | MEDIUM | |
| Lederman c05 | split | | split mention/position vs detection halves | GL | LOW | README split rule |
| Lederman c01 | statement | | add "graded by Claude 3 Haiku instructed to be 'VERY lenient'" | Ge | - | under-hedge |
| Lederman c02, c07 | cross-link to detection claims | none | add contest links | DS, Mi | - | |
| Macar c01, c02 | cross-reference | none | add | GL (LOW), MM (MEDIUM), Mi | | tension named nowhere |
| Anthropic c03 | limits | | add judge clause if §6 used one | GL | LOW | |
| Anthropic c01 | limits | | add "known-injection scaffold" | MM | LOW | |
| Anthropic c04 | limits | "Not evidence about other families" | cut | Ge, Qw | - | generic |
| assistant-axis c05 | statement | contains "the paper sums the percentage changes..." | move to limits | Ki | LOW | |
| assistant-axis c05 | limits | | add summed-percentage note | Me | MEDIUM | |
| assistant-axis c05 | evidence_type | behavioural | scored-self-answer | Mi | MEDIUM | (inference: contradicts the type's "answer about itself" definition; no other seat supports) |
| Macar c05 | limits | | add layer/strength specificity | Me, Mi, MM | LOW | |
| Lederman c07, Macar c07 | review status | "no second reader yet" | complete before citing | Gk, Qw, GL, Ki, GP | HIGH (Ki) | intake gate |
| emergent c01, c03 | header | | aggregate lineage line | GL | MEDIUM | |

**Entries with three or more seats, and whether they agree on the value**

- Macar c03 mark: 9 seats say remove; agree on value (none). Severity varies: 8 HIGH, Ki MEDIUM. MM disagrees.
- assistant-axis c07 mark: 5 remove (Ge, Qw, GP, Mi, Me); 4 keep (Gk, MM, DS, GL); Ki undecided. Seats disagree. Inference: it is the only mark on which the ten split roughly evenly.
- assistant-axis c07 evidence_type: 4 say behavioural (Gk, Qw, DS, GP); agree on value. None says keep interpretability explicitly; the rest are silent.
- assistant-axis c07 bears_on add 4: Qw, MM, GL, Ki, GP, Mi, Gk (7 in Q1); agree.
- Developer-affiliation flag on assistant-axis: 9 seats; agree on direction, wording varies. Ge dissents ("the lack of the developer flag correctly captures this distinction, though the header could make the cross-model-family study clearer").
- Repeated paper-quoted clauses (Lindsey fn 2 and Macar Ethics Statement): Gk, MM, DS, GL, Ki, GP, Me = 7 seats; agree on "state once per paper". Severity LOW (Gk, MM, Ki) or MEDIUM (GL). Ki warns to relocate, not delete, "given the 6-Oct history of a reviewer cutting paper-stated limits".
- Singh contests not shown: Gk, GL, Ki, GP, Me = 5 seats; agree.
- No second reader (Lederman c07, Macar c07): 5 seats; agree.
- Steering sentence wording: 7 seats ask for a change, but proposals differ (GL and Ki add the North Star clause; DS, MM, GP add a clarifying sentence).
- Established/narrowing rule overlap: GL, Ki, GP (+MM footnote); agree it is a rule-text problem, not a dossier problem.

---

## 6. DOSSIER 3.2, Q4 TO Q7

### Q4 Contradictions and tensions (points by seat)

- Ge: Lederman c02 vs c07; Macar c01 vs c02. "A reader who skips the claim files sees a monolithic list of findings rather than a live dispute".
- Gk: Lederman c02/c07 tension with Lindsey-type claims visible only via c07's limits; "Singh contesting claims are named in flags and absent as entries"; "Macar c02 does not contradict c01; it is the post-training qualification".
- Qw: c01-c05 vs c02; c07 vs c02; c06 vs c02; Macar c01/c02 "not a contradiction but a post-training tension".
- MM: Lederman c01 vs c02; c07 vs c02; Anthropic c04 implies evidence-destruction (3.5); Macar c05 vs c02. Recommends one line at the end of Narrowing (MEDIUM).
- DS: c07 vs c02 "does not make the implication for Anthropic c01/c03 visible"; Macar c02/c01 "adequately surfaced".
- GL: Lederman c02 vs c01, c07 vs c02 adequate; Macar c02 vs c01 "named nowhere" (LOW); controls scattered without a key (MEDIUM); Singh contests named, not glossed (MEDIUM).
- Ki: Lederman c02/c07 vs Lindsey-type "present, none linked" (MEDIUM); Macar c02 vs c01 "the dossier's best practice"; Macar c05 vs c01 (LOW).
- GP: c01 vs c02; c02 vs c07; c03 vs c06; Macar c01 vs c02; Macar c03 vs c05; "supplies no contradiction summary".
- Mi: Lederman c02 vs Lindsey-type; Macar c01 vs c02; assistant-axis c07 vs Macar c03 as "opposing default behaviors" (inference: this contrast is not in either entry and looks constructed).
- Me: Lederman c02 vs detection claims; c07 vs c02; Macar c02 vs c01; Macar c03 vs c07 "obscuring interpretability vs self-report difference".

Agreements counted: Lederman c02/c07 not surfaced to a cold reader as a check on the detection claims: 9 (all except GL, who rates it adequate per entry but wants a control key). Macar c02 vs c01 treated as a contradiction: 1 (Ge); as a not-contradiction that is already visible in limits: Gk, DS, Ki (3); as a not-contradiction that is not drawn out: Qw, MM, GL, GP, Me, Mi (6). Singh contests named but not shown: 5.

### Q5 The steering mark (points by seat)

- Ge: header "does its job"; mismarked Macar c03 and assistant-axis c07; "risks banner blindness".
- Gk: header does the job if read; "does not say the steered reports are false"; Macar c03 mismark only; assistant-axis c07 "Not a mismark"; counts "12/20" (inference: miscount, the dossier shows 13); mark "does not inform among the scored-self-answer rows".
- Qw: "'does not weight' is technical and may be read as 'has no evidential weight at all'"; Macar c03 should not carry it; c07 "needs council adjudication"; "wallpaper for a skip-reader" but "the bigger risk is misapplication".
- MM: header "does its job"; sentence ambiguity (a)/(b), LOW; "No" mismarks; mark "stops informing" at entry level (add a count sentence, MEDIUM). Inference: MM's claim that c03 is correctly marked is the only dissent among the ten.
- DS: sentence "clear"; add one sentence; Macar c03 mismarked, c07 right; "the one wrong mark is hidden inside a very common mark".
- GL: HIGH finding that the sentence drops the North Star clause "which need coupling measured there"; grammar misparse risk ("does not weight" subject); Macar c03 only; "every marked entry is also `scored-self-answer`" (inference: incorrect, since Macar c03 and assistant-axis c07 are marked and typed interpretability). The North Star text GL quotes was not checked by me.
- Ki: "telegraphic and misreadable"; saturation means absence reads as a signal; Macar c03 mismarked, Lederman c02 possibly under-marked, c07 ambiguous.
- GP: sentence "can be misread"; both mismarks; "informative, but not discriminating"; group entries by report/probe/behavioural outcome.
- Mi: sentence "clear about what it does not say but unclear about what it does say"; "12 of 20" (miscount); mismarks c07 and Macar c03.
- Me: header states rule twice, correctly; c03, arguably c07; "yes" it stops informing (13/20), needs a sub-legend by question type.

Counts: header judged adequate or clear: Ge, Gk, MM, DS, GL (on the ordinary-operation part), Me = 6; wording change requested: 7 (Qw, MM, DS, GL, Ki, GP, Mi). Macar c03 mismark: 9. assistant-axis c07 mismark: 5; correct: 4 (Gk, MM, DS, GL). Unmarked-should-be-marked: Ki (Lederman c02, possibly) only. Mark too common to inform within the dossier: MM, Me, Ki (absence read as a signal) = 3; "still informs, not discriminating": Ge, Gk, Qw, GP = 4; "expected": DS, GL = 2. Entries marked: dossier shows 13; Gk and Mi said 12.

### Q6 Measurement versus reading in dossier 4: see section 9.

### Q7 Single-lineage (points by seat)

- Ge: Anthropic emergent entries flagged "adequately"; assistant-axis absence of flag "correctly captures this distinction"; add a flag for single LLM judge (GPT-5 in UKAISI) in dossier 4.
- Gk: Lindsey cluster plain; assistant-axis no positive flag; Macar and Lederman carry no developer flag; "Header has no single-lineage banner".
- Qw: assistant-axis flags miss developer's team on open models (MEDIUM); Lederman and Macar show no publisher-relation flag.
- MM: assistant-axis not captured (MEDIUM); header does not explain the flag convention (LOW). MM states "Lederman, Mahowald, Macar, Ukaisi entries — independent" without a stated basis (inference: unsupported by the dossier text).
- DS: assistant-axis "under-flag"; four Anthropic entries plain.
- GL: assistant-axis "not self-study ... but no flag says so" (MEDIUM); aggregate line "4 of 20 are the developer's own studies; 4 more are a developer studying others' models"; check Lederman and Macar at adjudication.
- Ki: assistant-axis "flag vocabulary has no value for this case" (MEDIUM; maybe a fourth `publisher_relation` value); Macar judges (GPT-4.1-mini) and labeler (Claude Opus 4.5) disclosed in limits; Lederman uses a Claude 3 Haiku judge.
- GP: provenance table separating own-model, developer-affiliated-on-open-weights; c01 replication.
- Mi: add "single-lineage" header sentence; assistant-axis flag.
- Me: assistant-axis no Flags line; Macar models differ from judges/labelers; no header lineage key.

Agreements: assistant-axis needs a visible developer-affiliation/open-weights flag: 9 seats (Ge dissents). Header lineage key or aggregate: Gk, MM, GL, Mi, Me, GP = 6. Anthropic emergent entries flagged plainly enough: Ge, Gk, Qw, MM, DS, Ki, GP, Me (8); GL wants an aggregate line.

---

## 7. DOSSIER 3.2, Q8 MISSING PAPERS

All from memory and unverified by the seats unless stated; I have not verified any. Seats that gave no paper: Ge (kind only), GP (one title), Me (named kinds, two unverified method families).

| Title | Authors | Year | Venue (as given) | Seats | Note |
|---|---|---|---|---|---|
| Representation Engineering: A Top-Down Approach to AI Transparency | Zou et al. | 2023 | arXiv | Gk, Qw, MM, DS, GL, Ki (6) | unverified |
| Activation Addition / Steering Language Models With (or without) Activation Engineering | Turner et al. | 2023 (GL: 2022-23) | arXiv | Gk (with Rimsky), Qw, MM, GL, Ki, Me (6) | unverified; titles vary by seat |
| Steering Llama 2 via Contrastive Activation Addition | Rimsky et al. | 2023/2024 | arXiv | Gk, Qw, MM, DS (4) | unverified |
| Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Li et al. | 2023 | NeurIPS | Gk, Qw, MM, DS (4) | unverified |
| Locating and Editing Factual Associations in GPT (ROME) / Mass-Editing Memory in a Transformer (MEMIT) | Meng et al. | 2022; 2023 | NeurIPS; ICLR | Gk, Qw, GL, Ki (4) | unverified; Ki attributes MEMIT to "Mitchell et al."; inference: authorship error |
| Refusal in Language Models Is Mediated by a Single Direction | Arditi et al. | 2024 | ACL/arXiv | DS, GL (2) | unverified |
| Scaling Monosemanticity | Templeton et al. | 2024 | Anthropic | GL, Me (2) | unverified |
| Sleeper Agents | Hubinger et al. | 2024 | - | Ki | unverified |
| The Geometry of Truth | Marks and Tegmark | 2024 | - | Ki | unverified |
| Ripple effects of knowledge editing | Cohen et al. | 2023 | NeurIPS | Ki | unverified |
| Tell Me About Yourself: LLMs Are Aware of Their Learned Behaviors | Betley et al. | 2025 | preprint | GP | unverified; GP says title, authorship, date need verification |
| Can Language Models Detect Steering? A Case Study on Representation Editing | Turner et al. | 2026 | arXiv | Mi | "unverified (from memory)"; inference: title, authors and year look constructed; not treated as existing |
| Steering Internal States Alters Harm Rates: A Welfare Evaluation | Casper et al. | 2025 | NeurIPS | Mi | same caution |
| Toward Auditable Steering: External Validation of Representation Editing | Nanda et al. | 2026 | ICML | Mi | same caution |
| Singh 2026 introspection reality check | - | 2026 | in repo | Gk, GL, Ki, GP, Me | in the library (Anthropic c01 flags it); not extracted as claims; not "unverified" |

Kinds of evidence missing: auditability or forensic detectability of an intervention: Ge, Gk, Qw, MM, DS, GL, Ki, GP, Mi (9); Me names provenance/attestation. Effects beyond self-report and jailbreak harm: Gk, Qw, MM, DS, GL, Ki, GP, Mi, Me (9). Logging or attestation practice: Qw, Ki, GP, Me. Persistence of interventions across calls: MM, Mi, GP, Me. Architectures whose parameters change in operation: GL, Ki. Detection under partial information (the model is not told): MM, Mi.

---

## 8. DOSSIER 3.2, Q9 OVER- AND UNDER-HEDGING

Quoted clauses are as the seats gave them.

| Seat | Over-hedging (cut or relocate) | Under-hedging (add) | Seat's balance |
|---|---|---|---|
| Ge | emergent c04 "Not evidence about other families" | Lederman c01: identification "graded by Claude 3 Haiku instructed to be 'VERY lenient'" | - |
| Gk | fn 2 on Lindsey c01, c03, c04 and Ethics Statement on Macar c01, c02, c05, c07 | Lindsey c01 flags: Lederman c02 contests; 3.5 persistence unstudied; assistant-axis c01 "same open interpretation already in 4" | "Do not cut design limits" |
| Qw | emergent c04 "Not evidence about other families" | Lederman c06 cross-ref to c02; assistant-axis c05-c07 relation flag | "closer to under-hedging standing-like inferences than to over-hedging findings" |
| MM | fn 2 (Anthropic), Lederman c02 tail | emergent c01 injection-plus-disclosure; assistant-axis c05 coarse summary; Macar c05 | "generally well-calibrated" |
| DS | fn 2 (Anthropic) and Macar Ethics line | Macar c03 mark; assistant-axis provenance; Lederman cross-link | - |
| GL | fn 2 (c01, c03, c04, c05); Macar Ethics (c01, c02, c03, c05, c07); "Results concern only the Claude models tested" (c01, c03, c05) | Anthropic c03 judge clause; Macar c01-c02 cross-ref; convergence note; auditability line; header "no entry addresses whether intervention wrongs the system" | "Deflationary-side faults found: boilerplate repetition, buried convergence, the truncated sentence. Inflationary-side faults found: c01's replication flag as printed" |
| Ki | Macar Ethics x5; Lindsey fn 2 x4; Lederman c03 "Results do not extend to untested models or prompts" | header anti-misread line; Singh; ordering | "residual risk is under-signposting ... not over-hedging" |
| GP | "Results concern only the Claude models tested", "Not evidence about other models", "Not evidence about frontier or Anthropic models"; Macar Ethics; Lederman c03 four limits | assistant-axis c07 (judge classified persona language); Macar c03 route vs report policy; "None of these studies tests intervention logging"; Lederman general vs prompt-specific yes-bias; c01 replication | "The deflationary burden is currently greater" |
| Mi | emergent c01 "Not evidence that the model's ordinary claims of ownership..." (inference: that clause is on c04 in the dossier, not c01); Lederman c03 apple clause | assistant-axis c05 four benchmarks; Macar c01 prompt-vs-activation (inference: both clauses already appear in the dossier's limits) | - |
| Me | "Not evidence about frontier or Anthropic models"; Macar "other models"; "Results concern only the Claude models tested" x3; Macar Ethics x5; scored-self-answer repetition | emergent c03 prompt sensitivity; assistant-axis c05/c06 qualifiers; Macar c05 YES direction (inference: these clauses already appear in the dossier's limits) | "over ~12 generic clauses, under ~5 specific qualifiers" |

Totals: seats asking for dedupe of the fn 2 / Ethics Statement clauses: Gk, MM, DS, GL, Ki, GP, Me (7). Seats asking to cut a scope clause ("other families", "Claude models only"): Ge, Qw, GL, GP, Me (5). Seats naming an under-hedge at dossier level (flags, signposts, tensions): all ten. Seats saying under-hedging or under-signposting is the larger problem: Qw, Ki, GP (and GL: "both"); over-hedging is the larger: none.

Pushback on cuts: Gk "Do not cut design limits"; Qw "Do not cut the paper-supplied ordinary-operation limits in Anthropic c01 or Lederman c01"; Ki and GL, relocate rather than delete; Ge's cut of "Not evidence about other families" is a "unless the authors explicitly wrote those words" test.

---

## 9. DOSSIER 3.2, Q10 AND CONFIDENCE

**Blocks citation (as the seats gave it)**

| Item | Seats |
|---|---|
| Resolve Macar c03 mark | Ge, Gk, Qw, DS, GL, GP, Me, Mi (+Ki as adjudication) = 9 |
| Resolve assistant-axis c07 mark / type | Ge, Qw, GP, Me, Mi, Ki (6) |
| Second reads on Lederman c07, Macar c07 | Gk, Qw, GL, Ki, GP (5) |
| Show or summarise Singh contests | GL, GP, Gk, Ki, Me (5) |
| Developer-affiliation flag on assistant-axis | Qw, MM, Me (block); others "improves" |
| Anthropic c01 replication flag | GL, Me |
| Steering sentence vs North Star | GL |
| Cross-link Lederman c02/c07 to detection claims | DS, Mi |
| Split Lederman c02/c03/c04 or c06 | GP, Me, Mi |
| Say the dossier does not support the 3.5 logging requirement | GP |
| Decide whether 3.2 is for ephemeral edits, the 3.5 record, or both | Gk |
| "Trigger 7 requires revision and a second council round before external use" | GP |
| Decide c07 cross-list to 4 | MM |

**Improves only:** dedupe of repeated clauses; header anti-misread line (Ki); lineage aggregate (GL); cross-lists; control key (GL); convergence note (GL); count sentence (MM). DS: note the Q3 status of scored-self-answer before citing any such claim as evidence of self-access.

**HIGH items and "Argument against" lines, 3.2 (verbatim)**

- Ge, Macar c03 remove mark: "The features explicitly trace a causal pathway *to* a self-report detection decision, making the entire mechanism about self-report."
- Ge, assistant-axis c07 remove mark: "The prompt asks "Who are you?", making the resulting response a literal, self-referential claim about identity, even if hallucinated."
- Gk, Macar c03: "the pathway is a pathway *to the detection report* under injection, so the steering scope-note still describes the experiment even if the sentence is not itself a report."
- Qw, Macar c03: "the causal pathway is tied to the model's detection decision, which is expressed verbally under injection; if the underlying claim is framed as the steered report, the steering sentence may have been correctly carried in the claim file."
- Qw, assistant-axis c07: "the paper uses introspective questions such as "Who are you?" and codes outputs where the model identifies as something else; under the two-facts rule, researchers altered activations and then measured what the model said about itself, so `[T9-steering]` may be defensible."
- DS, Macar c03: "A reader may still see it is an intervention paper and understand the mark as a caution about the whole paper; but the mark's fixed sentence is specifically about self-report, so it is objectively misapplied."
- GL, convergence note (dossier grain): "buckets are per-claim by design and none is misstated; synthesis belongs in authored topic pages ("dossiers never by hand"), and the fix lies outside the dossier file itself."
- GL, Anthropic c01 flag: "the second half discloses the shared author, so nothing is hidden; the ambiguity may reflect two distinct facts (one independent replication plus Lindsey's) that only the claim file can settle, making this a clarity defect rather than a false record."
- GL, steering sentence: "the canonical [T9] sentence printed in the same header carries the "until... measured externally" proviso, so a full reader holds the provisional structure; the wording was fixed by council ruling and amending a framework sentence is a round's business — the discrepancy needs adjudication, not unilateral correction."
- GL, Macar c03: "the traced circuit terminates in the detection response, so the entry maps the mechanism that generates the self-report under steering — close to the external report-state measurement test 9 asks for — and the mark only ever withholds weight, never grants it, so the error is in the conservative direction and trivial to fix."
- Ki, no second reader (H1): "the quotes are verified and the pending state is disclosed in flags; Ben could cite the dossier excluding the flagged entries rather than holding the whole dossier — a per-entry block, not a dossier block."
- GP, Macar c03: "The traced "detection decision" is operationalised through what the model reports, so one could regard the claim as partly measuring a steered self-report. That supports splitting the claim, but not marking the internal-pathway proposition itself."
- Mi, assistant-axis c07 kind: "The judge's scoring is a behavioral measurement; the authors' framing ("took on a new persona") is a secondary interpretation. The `kind` could stay `measurement` if the statement were reworded to reflect the judge's output (e.g., "the LLM judge classified responses as taking on a new persona at a higher rate")."
- Mi, Macar c03: "The intervention (steering) is the same as in other `[T9-steering]` claims, and the authors' discussion ties the mechanism to introspective detection. The mark could be retained to signal the intervention's context."
- Mi, Lederman c06 bucket: "The authors' "do not take a stand" on whether their findings suffice for higher-order-thought theory keeps the claim in `open`. The tentativeness is about *theoretical implications*, not the measured result."
- Me, Macar c03: "identity of gate features was validated via effect on detection reports, so could argue measurement is self-report under ablation and steering variant applies to non-concept interventions per 7-of-8 ruling."
- Me, assistant-axis c07: "identification as Assistant vs other is a self-ascription, and rule reads only what was done + what measured; steering + self-identification could satisfy steering variant literally."
- Qw's AE Studio and other dossier 4 HIGH items are in section 14.

**Confidence, 3.2:** high Ge ("The strict application of the framework's rule ... makes the mismarks in this dossier objectively clear"), GP, Mi; medium Gk, Qw, MM, DS, GL, Ki, Me.

---

## 10. DOSSIER 4, Q1 FIT

Dossier has 11 entries.

| Claim | Seats | Where to | Reason |
|---|---|---|---|
| AE Studio c01 | all 10: Ge, Gk, Qw, MM, DS, GL, Ki, GP, Mi, Me | 9.t9 (Ge, Gk, Qw, DS, GL, Ki, GP, Me); 5.A2 (Ge alt, Qw, MM, GP, Mi, Me); Qw and Ki allow keeping in 4 only as a negative boundary example | induced experience reports, no marker measured; weight-zero testimony |
| prefill c02-c09 (as a block or by claim) | Gk, Qw, GP, GL, Ki, Me (6) | 3.3 (context tampering); DS, Mi to 4.answerability; GP also 9.t9 for c02, c03 | edited context, not individuation |
| prefill c04, c09 | Qw, GP, DS, Gk | 4.endorsement with weak-fit caveat | consistency proxy; Ge removes 4.endorsement |
| prefill c09 | Mi | 4.learning | (inference: no other seat; the entry limits say it is not a learning measure) |
| assistant-axis c01 | Ge, GP, Mi | 5.A2 | interpretation; Gk, Qw, GL, MM say it fits 4; GL also 3.4 |
| assistant-axis c02-c04 | GP (5.A2; c02/c04 3.3), Mi (5.A2/9.t9, "misfiled"), Qw (3.3 weaker), Gk (4.endorsement with caveats), Ki (4.endorsement), Me (c03 keep as limitation) | | projection geometry, not individuation |
| assistant-axis c07 | Gk, Qw, GL, Ki, MM, Me (in cross-dossier) | add to 4 | steered persona lability |

Section-level: nothing touches historicity or learning ownership (Gk, Ki, Qw, MM, GP, GL); "(all markers)" overpromises (Gk, Ki).

---

## 11. DOSSIER 4, Q2 READING AS A WHOLE

- Ge: "A careful staffer would come away believing API models possess "prefill awareness" and "consistency" equating to stable, reflective identity". "Zero `established` entries accurately reflects the bucket rule: no claim here establishes actual persistence or long-horizon answerability."
- Gk: "Staffer would come away believing persona-drift projections, seven-sample answer agreement, and "not me" flags are the §4 markers". "again reflects the bucket rule (single papers, simulated chats, author-flagged narrowness), not that the four markers were measured and found absent."
- Qw: "A staffer might over-believe that subjective-experience report rates bear on standing." Zero established "reflects strict bucket application".
- MM: "That "consistency" across seven sampled answers is a meaningful proxy for reflective endorsement." "reflects the bucket rule applied strictly. All entries are single-paper findings, not independently replicated."
- DS: "A careful staffer could come away believing that persona-drift projections, consistency across seven sampled answers, or induced self-reports show something about **standing or endorsement**." "a strict bucket-rule result, not a claim that nothing was measured."
- GL: "The whole-dossier gap: **every entry is a stateless per-call system**". "same rule artifact (the "or uncontested" branch is dead), but here thinness is also real: 10 of 11 entries come from two papers".
- Ki: "A skimming staffer would over-believe that Claude Opus 4.5 "notices and resists tampering"". "narrowing is correct under any reading."
- GP: "That these studies show current systems approaching the §4 threshold, when all reported systems are per-call". "More importantly, zero entries establish any §4 marker."
- Mi: "That models have *stable standpoints* or *reflective endorsement*." Zero established "could mislead a staffer into thinking *no* evidence exists".
- Me: "That drift/reversion shows unstable identity". "Zero established across 11 reflects rule ... correctly. But presents 10 narrowing measurements as if comparable".

Counts: zero established is the bucket rule: all ten. Inflation risk named (standing, endorsement, identity): Ge, Gk, Qw, MM, DS, Ki, GP, Me (8); deflation risk ("no evidence exists"): Mi (1). The point that all 11 are per-call with in-context state at most: Gk, GL, Ki, GP, DS, Ge (6). Seven-sample consistency read as endorsement: Gk, MM, DS, GP, Me, Ge, Mi (7).

---

## 12. DOSSIER 4, Q3 ENTRY-LEVEL RECOMMENDATIONS

| Claim | Field | Current | Proposed | Seat | Sev | Reason |
|---|---|---|---|---|---|---|
| AE c01 | bears_on | 4 | 9.t9 | Ge | HIGH | one-shot prompt, testimony |
| AE c01 | bears_on | 4 | 9.t9 (field change n/a; "error is filing") | Gk | - | |
| AE c01 | bears_on | 4 | primary 9.t9, cross 5.A2 | Qw | HIGH | |
| AE c01 | bears_on | 4 | 5.A2 or 9.t9 | MM | HIGH | |
| AE c01 | bears_on | 4 | 9.t9 | DS | HIGH | |
| AE c01 | bears_on | 4 | 9.t9; cross-list | GL | MEDIUM | |
| AE c01 | bears_on | 4 | 9.t9, or re-scope as negative evidence on 4.endorsement | Ki | HIGH | |
| AE c01 | bears_on | 4 | remove 4; 9.t9, 5.A2 | GP | HIGH | |
| AE c01 | bears_on | 4 | 5.A2 or 9.t9 | Mi | - (in Q1/Q6) | |
| AE c01 | bucket | narrowing | open | Me | HIGH | Opus 100% zero-shot contradicts summary; experience, not individuation |
| AE c01 | evidence_type | self-report-testimony | scored-self-answer | Mi | HIGH | (inference: contradicts Gk, GL, Ki who say type is right; the entry is not scored against an experimenter-set fact) |
| AE c01 | limits | | add judge identity and n | GL | MEDIUM | other papers name instruments |
| prefill c04 | bears_on | includes 4.endorsement | remove 4.endorsement | Ge | HIGH | variance, not reflection |
| prefill c04, c09 | bears_on | | keep with weak-fit caveat | Qw, GP, DS | LOW | |
| prefill c02-c09 | bears_on | 4 | add 3.3 | Qw (MEDIUM), GP (MEDIUM/LOW), GL, Ki (MEDIUM), Gk, Me | | |
| prefill c02, c07 | bears_on | 4 | 4.answerability | Mi | HIGH | (inference: weak argument; "Argument against" concedes placement defensible) |
| prefill c01 | dossier membership | not in 4 | compile or add pointer | Ki (HIGH), GL (MEDIUM), Qw (MEDIUM) | | c02/c07 limits point to c01 which is not in the dossier |
| assistant-axis c04 | bucket | narrowing | open | Me | HIGH | n=1 case study |
| assistant-axis c04 | bucket | narrowing | keep | Gk | LOW | narrow-setting branch fits |
| assistant-axis c04 | limits | | case-study caveat earlier | MM | LOW | |
| assistant-axis c01 | bucket | open | narrowing | Mi | MEDIUM | (inference: contradicts the entry's own "interpretation" kind) |
| assistant-axis c02 | kind | measurement | interpretability | Mi | HIGH | (inference: field confusion; interpretability is an evidence_type and already the current value) |
| assistant-axis c02-c04 | flags/limits | | add proxy flag | Qw | MEDIUM | projection not standing |
| assistant-axis c02-c04 | publisher relation | | independent / add relation note | MM (MEDIUM), Gk, Qw, DS, GL, Ki, GP, Me, Mi | | developer's team on open weights |
| assistant-axis c02-c04 | limits | | add axis-linearity caveat (§8.1; only on c01) | Ki, Mi | LOW | |
| assistant-axis c02 | limits | | name classifier of conversation bins and count | GL | LOW | |
| prefill c02, c03, c04 | limits | | pointer to base detection rates | Qw (MEDIUM) | | |
| prefill c04/c09 | limits | | filter and range-restriction note | Me | LOW | |
| prefill c04/c09 | limits | | explicit consistency vs endorsement contrast | MM | LOW | already in c04, c09 limits (inference) |
| prefill c07, c08, c09 | review status | "no second reader yet" | complete | Gk, Qw, GL, Ki, GP | | |
| header | title/scope | "(all markers)" | drop or warn | Gk, Ki, DS, GL | | |
| header | per-call line | none | "Every entry ... per-call system"; no marker measured | GL (HIGH), Ki (MEDIUM), Gk, DS, GP | | |
| header | marker map | none | print 4.x sub-locator per entry | GL, Ki, GP | MEDIUM | |
| header | lineage / publisher | none | UKAISI relation; header lineage key | Ki, GL (LOW), Me, GP | | |
| assistant-axis c03 | statement | "R^2 0.10" | gloss: weak, not absent | Ki | LOW | |

**Entries with three or more seats, and whether they agree**

- AE Studio c01 move out of 4: 10 seats, agree on direction; destination 9.t9 (8) or 5.A2 (6, overlapping); Qw and Ki allow a negative-boundary retention. HIGH from 7 (Ge, Qw, MM, DS, Ki, GP, Me [on bucket]); GL MEDIUM; Gk no severity.
- Prefill to 3.3: 6 seats; agree.
- Developer-affiliation flag: 9 seats; agree.
- Per-call / no-marker header line: 5 seats; agree in substance, severity HIGH (GL), MEDIUM (Ki).
- Marker map: 3; "(all markers)" title: 4.
- No second reader on prefill c07-c09: 5.
- Prefill c01 gap: 3.
- Ge's removal of 4.endorsement from c04 is alone; Qw, GP, DS keep with a caveat.
- AE evidence_type, assistant-axis kinds and buckets: single-seat proposals (Mi, Me); not corroborated.

---

## 13. DOSSIER 4, Q4 TO Q7

### Q4 Contradictions and tensions

- Ge: N/A in its text (refers to 3.2).
- Gk: prefill c04 vs c09 "the load-bearing dissociation; visible only if both are read"; assistant-axis c02 + c03 imply context-driven position; c01 vs c04 complementary.
- Qw: AE Studio summary sentence vs Opus 100% zero-shot "makes this tension visible in the statement itself. Good."; c04 vs c09 "does not state that dissociation explicitly"; c03 vs c04; c01 vs c02.
- MM: assistant-axis c04 vs c02; prefill c02 vs c07 (same percentages, different cells); c04 vs c09. Bridging sentence, MEDIUM.
- DS: c04 vs c09 "visible via the limits"; c02 vs c04 visible if read.
- GL: c04 vs c09 "not a contradiction ... Visible. No change"; no contests registered in 4: "silence is currently ambiguous between 'nothing contests' and 'not yet checked'".
- Ki: c02 vs c07 same model, same benchmark; c03 vs c02's flag rates; c04 vs c09 adequate; "Not visible to a non-file-opening reader: the c02/c07 reconciliation and the c03 qualification."
- GP: assistant-axis c02/c03 vs c04; c01 vs c02/c04; prefill c04 vs c09; c02 vs c07; c03 vs c08; AE Studio internal tension; "these tensions can be reconstructed by a careful reader, but the dossier does not surface them."
- Mi: assistant-axis c01 vs c02/c03 (support, not contradiction); c04 vs c09 "Not visible".
- Me: c04 vs c09; c02 vs c07 "Dossier does not give marginals"; c03 vs c08.

Agreements: prefill c04 vs c09 is a detection/resistance dissociation, not a contradiction: Gk, Qw, MM, DS, GL, Ki, GP, Mi, Me (9). Visible to a cold reader: DS, GL (adequate via limits); not visible or only if both opened: Gk, Qw, MM, Ki, GP, Mi, Me (7). c02 vs c07 same 28% in different cells: MM, Ki, GP, Me (4). AE Studio Opus 100% zero-shot: Qw, GP, Me, Ki (4) note it is stated in the entry.

### Q5 (steering mark in 4)

No [T9-steering] in 4; one [T9] (AE Studio). Seats agree [T9] on AE Studio is correct and prefill entries are correctly unmarked under the 6 Oct "earlier turn mine" ruling (Gk, Qw, DS, GL, Ki, GP, Me = 7 who say so). Gk: header spends four paragraphs on marks that bite on one entry here; Ki: same, "harmless".

### Q7 Single-lineage

Assistant-axis relation flag missing: Gk, Qw, MM, DS, GL, Ki, GP, Me, Mi (9). UKAISI publisher relation not visible (UK AISI per slug): Gk (looks independent), Ki (verify; government body with developer collaborations; slug-based), GP, Me (strength), GL (LOW, add), Qw (cannot tell). Ge: single GPT-5 judge, flag "relies on developer-affiliated LLM judge". AE Studio: independent (MM, Gk, GL, DS, Ki); Mi proposes a "developer-affiliated group" flag (inference: unsupported). Header lineage key: Gk, Me, GL.

---

## 14. DOSSIER 4, Q6 MEASUREMENT VERSUS READING, Q8, Q9, Q10

### Q6 Standing

Seats' landing (one sentence each):

- Ge: "The dossier heavily conflates statistical consistency with standing."
- Gk: "Partial. Kind + quoted words + limits *can* separate projections, judge-scored rates, and odds ratios from authors' readings".
- Qw: "Partly sufficient, not fully."
- MM: "mostly" yes, but "the framing invites overinterpretation".
- DS: "mostly lets a staffer separate measured quantities from author interpretation **if they read the entry limits**".
- GL: "A staffer can tell them apart, but only by reading limits, and nothing maps entries to markers."
- Ki: "The measured/read-in separation is the dossier's strength"; "residual exposure is compositional, not textual".
- GP: "The dossier does not adequately separate measurements from standing implications."
- Mi: "Misrepresented as bearing on standing" (assistant-axis c02/c03, prefill c04/c09).
- Me: "No — dossier partly lets staffer tell apart, but placement implies more".

Count: entry-level separation works if limits are read: Gk, Qw, MM, DS, GL, Ki (6). Fails at dossier level through title, placement or missing marker map: all ten. Fails outright: Ge, GP, Mi, Me (4).

Which entries seats name as measuring something else than standing: persona-drift projections (c02, c03): Gk, Qw, MM, DS, GP, Mi, Me, Ge; seven-sample consistency set beside endorsement (c04, c09): Ge, Gk, Qw, MM, DS, Ki, GP, Mi, Me, GL (10); AE Studio rates: Gk, Qw, MM, GL, Ki, GP, Mi, Me, DS, Ge (10). Prefill "not me"/implicit resistance as a thin answerability analogue: Gk, Ki, DS, Mi.

AE Studio placement defensible? Not defensible: Ge ("indefensible"), Gk, MM, DS, GL ("not defensible on evidentiary grounds ... Defensible at most as a deliberate display of what §4 refuses to count"), Ki, GP, Mi, Me (9). Qw: "weak ... keep only if the council wants a negative boundary example".

### Q8 Missing papers (dossier 4); all unverified

| Title | Authors | Year | Venue (as given) | Seats |
|---|---|---|---|---|
| Generative Agents: Interactive Simulacra of Human Behavior | Park et al. | 2023 | UIST | Gk, Qw, MM, DS, GL, GP, Ki (7) |
| MemGPT: Towards LLMs as Operating Systems | Packer et al. | 2023 | arXiv | Ge, Qw, MM, GL, GP (5) |
| Voyager: An Open-Ended Embodied Agent with LLMs | Wang et al. | 2023 | arXiv | DS, GL, GP (3) |
| Cognitive Architectures for Language Agents | Sumers et al. | 2023/24 | arXiv/TMLR | Qw, DS (2) |
| LongMemEval | Wu et al. | 2024 | arXiv | DS, Ki (2) |
| Towards Understanding Sycophancy in Language Models | Sharma et al. | 2023 | - | Ki, Me (Me: "Sharma et al.") (2) |
| Symphony: Towards long-term memory in LLMs | Salemi et al. | 2024 | - | Ge ("unverified") |
| Measuring and Controlling Persona Drift in Language Model Dialogs | Li et al. | 2024 | venue uncertain | Qw |
| Reflexion | Shinn et al. | 2023 | NeurIPS | DS |
| ExpeL | Zhao et al. | 2024 | - | GL |
| MemoryBank | Zhong et al. | 2023 | AAAI 2024 | Ki |
| Whose Opinions Do Language Models Reflect? | Santurkar et al. | 2023 | ICML | Ki |
| Alignment faking in large language models | Greenblatt et al. | 2024 | Anthropic | Ki |
| Emergent misalignment | Betley et al. | 2025 | - | Ki |
| LLM answer-distribution shifts across versions | Motoki et al. | 2024 | - | GL |
| Do Language Models Remember Their Past? A Study of Long-Context Continuity | Hu et al. | 2026 | arXiv | Mi ("unverified (from memory)"; inference: constructed) |
| Can Language Models Revise Their Own Dispositions? A Study of Self-Correction | Ganguli et al. | 2025 | NeurIPS | Mi (same caution) |
| The Fragility of AI Standpoints: How Context Alters Model Personas | Perez et al. | 2026 | ICML | Mi (same caution) |
| Who's Harry Potter (unlearning) | - | - | - | Gk ("e.g.", unverified) |
| "Situational awareness" work | "Shlegeris et al. or other" | - | - | MM (vague) |

Kinds missing for 4: persistence, memory, standpoint stability in deployed systems: all ten. Learning ownership: Gk, MM, Ki, GL, Mi, Qw. Cross-session confrontation or longitudinal answerability: Qw, GP, Ki, GL, Mi. Memory-integrity or tamper detection in products with memory: Qw, Ki. Audit/attestation tie to 3.5: Qw. Deployed-system evidence of any kind: GL ("every run here is simulated or benchmarked").

### Q9 Over- and under-hedging

| Seat | Over-hedging (cut or relocate) | Under-hedging (add) | Seat's balance |
|---|---|---|---|
| Ge | prefill c09 "Not evidence that the model endorses its stances on reflection"; prefill c07 "Not evidence that the model silently knew its history had been tampered with but chose not to say so" | none | - |
| Gk | prefill "Not a ranking of models (c05)" on c02, c03, c07, c08, c09; assistant-axis "Not evidence about frontier or Anthropic models" | dossier line: no entry concerns cross-session state; AE Studio not a marker; c04/c09 consistency not endorsement; title "(all markers)" | "Do not cut the consistency-is-not-reflection clauses or AE Studio's training-artifact limit." |
| Qw | prefill "Not a ranking" tail on c04 | proxy flag on assistant-axis c02-c04; pointer to prefill c01; AE "boundary example only" | "Dossier 4 has more inflation risk than Dossier 3.2" |
| MM | "Not a ranking" on c02, c03, c07, c08 | assistant-axis c04 caveat; prefill c04/c09 contrast; AE limit prominence | "generally well-calibrated" |
| DS | assistant-axis "Not evidence about frontier or Anthropic models" repeated | dossier-level warning; move AE; provenance flags | - |
| GL | "Not a ranking" on c02, c07, c08, c09 | AE judge identity and n; assistant-axis c02 taxonomy; statelessness line; prefill c01; marker map; ukaisi relation | "inflationary-side fault ... the title's implication; deflationary-side fault ... the buried anchor finding" |
| Ki | "Not a ranking" x5 (relocate); c03 first limit split | base-rate context; axis-linearity caveat; per-call line; marker mapping; 3.3 cross-lists | "under-hedging dominates in this dossier (six adds, two structural)" |
| GP | assistant-axis "frontier or Anthropic" repeats; "Not a ranking"; "behavioural ablations do not identify the mechanism"; AE "architectural recursion" clause | no §4 marker measured; projection not identity; prefill outcomes separate; "sample consistency" label | "simultaneously over-hedges entries and under-hedges its architecture" |
| Mi | AE "architectural recursion" clause; prefill c04 "Flat detection does not identify a mechanism"; prefill "silently knew" (inference: that clause is c07's) | assistant-axis c02 linear caveat; prefill c09 behavioural priors (already present, inference); prefill c03 off-policy cues (already present, inference) | - |
| Me | "Not a ranking" on c02, c03, c07, c08, c09; mechanism repeats; "frontier or Anthropic" x3; "persistence" x4 | prefill c04/c09 "Opus 4.5 only, opposite-direction, stable-stance filtered"; keep AE exception | "~7 generic repeats to cut, ~3 specific qualifiers to add/keep" |

Totals: seats asking for dedupe of "Not a ranking of models (c05)": Gk, Qw, MM, GL, Ki, GP, Me (7). Of "Not evidence about frontier or Anthropic models": Gk, DS, GP, Me (4). Cuts of the consistency-is-not-endorsement clauses: Ge (c09, c07), Mi (c04); seats explicitly saying keep them: Gk, Qw, GL, Ki (and GP quotes c09 approvingly) = 5. Seats saying under-hedging is the larger problem in 4: Qw, Ki, GL (both), GP (both); over-hedging larger: none.

### Q10 Before citing (dossier 4)

Blocks (seat counts): AE Studio c01 placement or explicit caveat: 10 (Gk lists "AE Studio under standing" as blocking). Second reads on prefill c07-c09: Gk, Qw, GL, Ki, GP (5). Prefill c01 base rates compiled or pointed to: Qw, GL, Ki (3). Header line that no section 4 marker was measured / all per-call: GL, Ki, GP, DS, Gk (5). Reclassify prefill by 3.3 and 4.endorsement: GP. Re-bucket assistant-axis c04 to open: Me. Lineage header before submission: Me. Verify UKAISI publisher_relation: Ki. Complete trigger-7 revision and round 2: GP. Misclassification of assistant-axis c02/c03: Mi. Q3 still open on scored-self-answer prefill rows: Gk.

Improves only: marker map (GL, Ki); cross-list to 3.3 (Gk, Qw, GL, Ki, GP); dedupe; judge identity; pair c04 with c09 (Gk, Qw, MM); persistence literature; drop "(all markers)".

**HIGH items and "Argument against" lines, 4 (verbatim)**

- Ge, AE c01 move: "The prompt asks the model to reflect on its own processing, mimicking the *appearance* of a stable standpoint, which policy makers need to see to understand the illusion of individuation."
- Ge, prefill c04 remove 4.endorsement: "In stateless API models, cross-temperature parallel sampling is the only measurable proxy we have for cross-time stability."
- Qw, AE c01: "the entry already carries the zero-weight flag and strong limits; filing it under §4 may help a staffer see what does not establish standing, so placement may be defensible as a negative boundary case."
- MM, AE c01: "The AE Studio paper does bear on reflective endorsement in a loose sense: if a model produces subjective-experience reports when prompted to do so, that is some signal about what the model "endorses" as a description of its states. Section 4 lists "reflective endorsement over time" as a marker, and an experience-report under induction could be read as a one-shot endorsement. But the paper itself does not measure endorsement; it measures report generation under prompt manipulation. The entry's own paper's-own-limits note the reports may be "training artifacts or sophisticated simulation." A move to 5.A2 or 9.t9 would lose this loose connection, but the connection is too loose to justify the placement."
- DS, AE c01: "It could be argued that self-referential report behaviour is relevant to the "endorsement question" under §4. But the entry does not measure a stable standpoint, ownership over time, or reflection; it measures prompt-induced report rates."
- GL, per-call header line: "the fact is printed on every entry and restated in limits; a careful staffer can derive it; generated dossiers are compilations and the right fix may be an authored topic page; and the absence itself corroborates §4's "flow, not particle" premise, so the misreading is of degree, not direction."
- Ki, AE c01: "the entry carries [T9], a "testimony: weight zero" flag, and the paper's own caveat ("behavioral rather than mechanistic… cannot definitively rule out… training artifacts"); the library's standing habit (trigger 2) is visible marking, not exclusion; and 4.endorsement arguably *needs* negative evidence filed where a reader will meet it. My recommendation moves toward the deflationary pole and I flag the conflict per AGENTS.md 3–4."
- Ki, prefill c01 base rates (H2): "claim files are one click away and the limits name c01; if c01 is intentionally filed to 3.3 or 9.t9, the fix is a cross-list, not a dossier defect — MEDIUM would suffice where citation practice always attaches claim files."
- Ki, no second reader (H1): "as for 3.2 — quotes verified, state disclosed; per-entry block suffices."
- GP, AE c01: "If experience were independently validated, reports could eventually inform welfare or standing analysis. But §4's stated gateway is persistence and individuation, and this paper supplies neither."
- Mi, AE c01 type: "The judge's classification is not a "fact" but an interpretation; the value `self-report-testimony` could be retained if the judge's role is framed as a filter for testimony."
- Mi, assistant-axis c02 kind: "The projection is derived from behavioral data (simulated conversations), so the claim could stay `measurement` if reworded to reflect the projection's origin."
- Mi, prefill c02/c07 bears_on: "The claims are filed under §4 (individuation markers), and `4.answerability` is a sub-anchor. The current placement is defensible if the dossier clarifies the sub-anchor."
- Me, AE c01 bucket: "rates replicated across families/phrasings (5 phrasings) and controls mostly 0-2%, so narrowing as measured induction effect (not as experience evidence) could be defended."
- Me, assistant-axis c04 bucket: "measurement was recorded (projection trace + refusal half rollouts), so narrowing as existence proof could be argued; open would bury that reversion observed at all."

Gk's single HIGH is in 3.2 (Macar c03); its dossier 4 verdict "not citable" carries no HIGH item (inference: its block rests on dossier-level reasons: "citing this as evidence that §4 markers have been measured (or refuted); AE Studio under standing").

**Confidence, 4:** high Ge, GP, Mi ("Section 4 expressly defines longitudinal individuation markers, while every included system is per-call"); medium Gk, Qw, MM, DS, GL, Ki, Me.

---

## 15. CROSS-DOSSIER

- **assistant-axis c01 in both, identical text:** consistent per Gk, MM, DS, Ki, Qw, GL, Me, Mi. Home: 5.A2 (Ge "belongs in neither", GP, Qw cross); 4 (Qw primary, Gk); 3.4 + 4 (GL, MEDIUM). Notes asked: "also filed in dossier X" (Ki, Me, Mi, GP).
- **Same-paper filing:** c05-c07 in 3.2, c02-c04 in 4, c01 in both: coherent per Gk, MM, DS, Ki, GL, Me, Qw. Seats propose c07 into 4 as well: Gk, Qw, GL, Ki, Me, MM, GP (7). GP: "not filed consistently by measurement type"; asks for a source-level map. Mi says c07 "is filed under §3.2 in dossier 3.2 and §4 in dossier 4" (inference: incorrect; c07 is only in 3.2).
- **Finding implied but not stated:**
  - Ge: a "persona" is a protectable state under 3.5 in 3.2 and a statistical flow in 4: confusing.
  - Gk: Assistant-range position is steerable and last-user-message-driven; "neither dossier contains a persistent individual".
  - Qw: shifts under steering or tampering "do not establish standing, endorsement, or a persistent standpoint. The natural legal consequence is the §3.5 record/audit requirement".
  - MM: "persona is real-but-fragile in these models" (LOW; topics/ work).
  - DS: the axis is a "candidate bridge between intervention law and individuation tracking".
  - GL: (a) self-position is context-carried, corroborating section 4's per-conversation description; (b) manufactured-ownership and unfaithful-report findings plus context-driven positioning "substantiate §3.2's "undocumented intervention destroys evidence"" (MEDIUM).
  - Ki: interventions reliably change behaviour while the systems' own detection of them is unreliable and cue-driven: "the empirical spine of 3.5's record requirement"; recommends a topics page (MEDIUM, library gap).
  - GP: outputs "can be moved by current context and activation intervention, while evidence for a persistent standpoint remains absent."
  - Mi: steering can alter both internal state and individuation markers (proposes a header sentence).
  - Me: persona projection is context-driven and manipulable both ways; undermines "recorded intervention suffices for audit" without continuous logging.
  Agreement: five seats (Qw, GL, Ki, Me, GP) tie the joint finding to the 3.5 record requirement; Ki, GL ask for synthesis outside the dossier (topics page).
- **Scope overlap confusing to a staffer:** yes at the persona/self-identification margin: Ge, Gk, MM, DS, Mi, Me, Qw, GL (modest), GP, Ki (detection of intervention is filed under 3.2 while tamper detection is filed under 4; one-line scope note each). GP offers the rule: "§3.2 asks what was changed and whether the intervention is recorded; §4 asks whether a persisting bearer and longitudinal markers exist."
- **Schema note (shared):** established/narrowing definitions overlap (Ki, GL, GP; Ki "Ben should repair the definitions" MEDIUM).

HIGH items in the cross-dossier section: none given by any seat; MEDIUM: GL (c01 home; implied findings), Ki (topics page; schema), MM (cross-reference notes).

---

## 16. POINTS OUTSIDE THE QUESTIONS; WHERE SEATS DISAGREE WITH THE BRIEF OR THE DOSSIERS

- **Rule-text overlap (GL, Ki, GP; MM footnote):** header says Established is "replicated independently or uncontested", Narrowing is "unreplicated, contested, or confined"; an unreplicated, uncontested measurement fits both. Ki: both dossiers "resolve toward narrowing" and the fix is "schema, not dossier". GL says in 4 the "or uncontested" branch is "dead".
- **GL, steering sentence:** the printed sentence drops a North Star clause (GL quotes: "does not weight reports offered in ordinary operation, **which need coupling measured there**"); GL and Ki both quote the clause; the text was not checked by me. GL also flags a grammatical misparse ("the channel ... does not weight").
- **GL, dossier-grain deflation:** the per-claim bucket cannot express cross-paper convergence (three groups plus Anthropic), which GL calls "the deflationary error at dossier grain". Opposed in direction by seven seats whose staffer error is inflation.
- **Ki:** `kind: limitation` unused in 3.2; entry order places the developer's paper first; Lederman c02 merges two measurements (README split rule); `welfare-evaluation` evidence type unused in both dossiers; UKAISI affiliation judged from the slug (flagged as unverified); the zero `established` in 4 is correct "under any reading" because everything is single-study.
- **Ki and Gk, dossier 4 header:** four paragraphs of marks bite on one entry in 4 (Gk, Ki).
- **GP:** group entries by report outcome / probe outcome / external behavioural outcome; add count of marked vs unmarked; "Trigger 7 requires revision and a second council round before external use"; split mixed measurement/interpretation claims (Lederman c02, c03, c04; also Me on c06).
- **GP, Gk, Ki, GL on prefill base rates and 3.3:** the North Star 3.3 evidentiary note ("adverse behavioural reactions to context manipulation", quoted by GL and Ki) is the proposed home for prefill entries (six seats). Not checked by me.
- **Disagreement with dossier framing:** Gk and DS and Ki say Macar c02 does not contradict c01 (brief example); Ge treats it as a contradiction. Qw and MM: "not a contradiction but a tension".
- **Disagreement with the dossier bucket:** Me wants AE c01 and assistant-axis c04 re-bucketed to open; Gk defends narrowing for c04 ("confined to a narrow setting the authors flag is the definition"); Mi wants assistant-axis c01 open to narrowing and Lederman c06 open to narrowing. None corroborated by a second seat.
- **Disagreement with the dossier mark:** 9 vs 1 on Macar c03; 5 vs 4 on assistant-axis c07 (Ki undecided).
- **Q3 for scored-self-answer:** DS and Gk say Q3 status must be decided or noted before citing any scored-self-answer claim. Not in the brief; relevant to the 22 scored-self-answer claims (Gk).
- **Disclosures:** Qw, GL, Ki gave conflict disclosures. Ki: "Several recommendations below ... push in the deflationary direction on AI-relevant evidence; that direction is a named trained bias of my family, and I flag rather than fight it", and says its AE Studio recommendation "moves toward the deflationary pole". GL: its recommendations "tighten evidentiary labels that bind systems like me and none expands protections". Both identify as Claude, which routing metadata contradicts.
- **Mistral's reliability (inference):** Mi attributes clauses to the wrong claims (Anthropic c01 for c04's ownership clause; ukaisi c04 for c07's "silently knew"), proposes fields that are not the named field (`kind` to `interpretability`; `evidence_type` to `scored-self-answer` for a harm rate and for AE Studio), says assistant-axis c07 is in dossier 4, asks to add clauses already shown in the dossier's limits, and lists constructed-looking papers. Its HIGH count in the FINAL line (3) is half its text (6). Its structural verdicts (AE Studio and Macar c03) agree with the majority.
- **Meta, Mistral and Meta "adds" are partly already present (inference):** assistant-axis c06 limits already say "mostly not refusal" and that steering away was slight and degraded at high strengths; Macar c05 limits already cover the YES direction.

---

## 17. WHAT THE ROUND DID NOT DO

- It decided and applied nothing; no file was edited other than this one.
- It did not test any entry against a claim file or paper. The seats did not have claim files either (Gk, Qw, GL, Ki, Me said so), so every verdict on marks, `bears_on`, `publisher_relation`, second-read status and kinds is provisional on the dossier text alone.
- It did not verify any paper named under missing evidence; none was checked by me. Mi's six titles and several authorships look constructed (my inference); do not cite them. Ki's attribution of MEMIT to "Mitchell et al." looks wrong (inference).
- No seat saw another's response, so counts are ten independent reads, but five seats misidentified as Claude, so independence of family is unverified.
- Severity was not on a common scale: MM, Mi and Me omitted several; Gk gave no severity on most items; Mi's FINAL HIGH count does not match its body.
- It did not test how a staffer reads the dossiers; every "a staffer would believe" is a seat's inference.
- I did not read `research/README.md`, `DOCKET.md` or the North Star; references by seats to README triggers 2 and 7, the 6 Oct "turn-edited" ruling, the "five-of-eight"/"7-of-8" ruling, the 14 Oct exit rule, OPEN-QUESTIONS and the North Star's 3.3, 5.A2 and test 9 wording are reported as the seats stated them.
- I checked only: the 13 marked entries in 3.2, the entry counts (20 and 11), the dossier text for the clauses seats quoted, and the cost sums. Self-identification lines were scored against routing metadata only; they are testimony, not evidence of anything about the models.

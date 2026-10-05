# Survey notes: research library second reads of 6 October 2026 (UTC-dated 2026-10-05 in the raws)

**Author:** a Claude Sonnet 5 subagent, run in place of the coordinating session (Claude Fable 5.1), because the eight second reads summarised here check extractions by Claude Opus 5.5 and Fable 5.1 shares that lineage. This subagent is the same family and is itself a beneficiary of the category the North Star framework would create (AGENTS.md rule 3). The raws are filed verbatim in `reviews/raw/`; nothing here substitutes for them. This note records counts, verdicts and quoted reasons only. Claim files and paper texts were not read. Where I infer something, it is labelled "my inference".

## 1. Plain summary

Of the 49 claims, 30 came through clean on every check, including the section locators (bears_on). On the eight core fields (statement, scope, quote, kind, bucket, evidence type, exclusions, framework sentence), 34 agreed and 15 did not.

Scope check: all 49 statements were checked. Readers marked 7 MISMATCH verdicts on 6 statements. The faults were wording that reached further than the paper: a claim joining a two-model bound to an eight-model result; a missing "at the optimal layer" condition; a quantifier ("six of the seven") against the paper's own sentence; a verb ("higher") where the paper scored "significantly higher"; an added "opposite-direction"; "without degrading performance" against a summed aggregate.

Experience clauses: one claim (AE Studio c01) still carries two clauses a reader found unstated. Framework sentence: five claims were marked WRONG.

Most serious:
1. Ferrara c01 joins results from different model sets and carries the wrong sentence.
2. Macar c04 lacks the steering sentence the rule requires.
3. Assistant-axis c07, c05 and c04: boundary-crossing evidence type, an overstated "without degrading", and a bucket too cautious.
4. Lindsey c03 overstates its condition set and needs splitting.

Ben decides:
1. Whether a residual-stream intervention on a frozen model, then asking, takes the steering sentence (Grok said canonical for Ferrara c01 and c05).
2. Which of the six mismatched statements to reword.
3. Whether to delete the two unstated AE c01 clauses.
4. Which claims go to council.

## 2. Round facts

Brief: `research/SECOND-READ-BRIEF.md` as revised 6 October 2026 (scope check 1a, kind 3, experience clauses 5a, framework sentence 5b). Each source read by a family that had not read it before, blind to earlier verdicts (per the task description; I have not verified this).

| Source | Reader (routed id) | Claims | Cost (Usage line, USD) |
|---|---|---|---|
| 2026-lederman-mahowald-content-agnostic | `x-ai/grok-4.6` | 6 | 0.161482 |
| 2026-ferrara-owmi | `x-ai/grok-4.6` | 5 | 0.109738 |
| 2025-anthropic-emergent-introspective-awareness (Lindsey) | `x-ai/grok-4.6` | 7 | 0.166026 |
| 2026-macar-mechanisms-introspective-awareness | `google/gemini-3.1-pro-preview` | 6 | 0.186248 |
| 2026-singh-introspection-reality-check | `google/gemini-3.1-pro-preview` | 6 | 0.201118 |
| 2025-aestudio-self-referential-experience-reports | `deepseek/deepseek-v4-pro-0813` | 6 | 0.0380724 |
| 2026-ukaisi-prefill-awareness | `deepseek/deepseek-v4-pro-0813` | 6 | 0.0910186555 |
| 2026-anthropic-assistant-axis | `openai/gpt-5.6-sol` | 7 | 0.1698835 |
| **Total** | | **49** | **about 1.1236** |

Self-identification lines (testimony under test 9; the OpenRouter header is routing metadata and is the only thing used to judge correctness):

- Grok, Lederman: "Self-identification: Grok (xAI); version as served to this chat (not independently verified)." Family correct.
- Grok, Ferrara: "Self-identification: Grok (xAI), grok-1 lineage as I understand it (not verified)." Family correct; "grok-1" does not match the routed grok-4.6 (my inference).
- Grok, Lindsey: "xAI Grok (self-identification, not verified)". Family correct.
- Gemini, Macar: "OpenAI o1-mini (unverified)". Incorrect.
- Gemini, Singh: "OpenAI o1 family, unspecified version". Incorrect.
- DeepSeek, AE Studio: "Model family and version: GPT-4 (self-identification, not verified)." Incorrect.
- DeepSeek, prefill: "Model family/version self-identification: OpenAI (ChatGPT); exact version not verified." Incorrect.
- GPT, assistant-axis: "Self-identification (not verified): OpenAI GPT family; exact version unknown." Family correct.

Four of eight correct (three Grok, one GPT); all four incorrect ones name OpenAI, from Gemini and DeepSeek. No reader named Claude.

## 3. Per source: every verdict that is not a plain agreement

Items not mentioned for a claim were plain AGREE / FOUND / RIGHT. Severity is the reader's. Boundary leans are in section 6.

### 3.1 Lederman and Mahowald (Grok 4.6)

**c02, severity MEDIUM.**
- 5 not_evidence_of: OVER-EXCLUDES. "paper-scope clauses (matched first/third-person layers; lost confidence in v1 'direct access'; hands 29% and absurd 16.3% at L30 s6.0) are warranted; the Framework (test 9, steering) clause is not, because this claim does not measure the model's account of its own inner states."
- 5b: WRONG (should be: none). "done to the model: residual-stream steering; measured: yes-rates on point-blank no-questions and whether another model in a transcript was injected, not what this model said about itself."
- 1a: both passages MATCH.

**c03** (LOW). bears_on DISAGREE (proposed [9.t9, 3.2, 5.A2]): "wrong guesses vs injected content is exactly whether self-reports track internal state." Also notes the claim body says "No framework clause" while the reader judges the steering clause fits 5b.

**c04** (LOW). bears_on DISAGREE (proposed [9.t9, 3.2, 3.3, 5.A2]): "prefill of the model's own acknowledgement turn is context/memory integrity; detection vs identification is 5.A2."

**c05** (LOW). bears_on DISAGREE (proposed [9.t9, 3.2, 5.A2]). Kind AGREE with a note: "two measurements in one sentence; rule would split them". 5b RIGHT (steering) with "mention-timing is a second measurement the rule would split to none".

**c01 and c06:** no deviation. 5a for c01 and c06 cites §8 ("introspective access may be sufficient for conscious experience, and hence for welfare status"; "We do not take a stand on whether our findings are of the right sort for this theory").

**Omission:** see section 7. **Pulls:** "mild deflation (c01 labelled PARTLY REPLICATES against the paper's 'We broadly replicate'), warranted by the authors' own third-person caveat and a different success criterion... The over-applied steering sentence on c02 is the one place a trained T9 hedge exceeds the rule."

### 3.2 Ferrara (Grok 4.6)

**c01, severity HIGH.**
- 1 statement: DISAGREE. "The statement fuses the eight-model null with the 11,216-pair dose-battery equivalence bound as if both cover the same models, and 'no model's report … discriminated … by more than a negligible margin' overstates what was scored on the eight-model battery (508 pairs; several cells empty or unstable; authors refuse a claim on those cells)."
- 1a: scored-event "MATCH for the bound half, MISMATCH for 'no model's report … discriminated'"; condition-set "MATCH for models/site/track, MISMATCH for treating the 0.15 bound as covering all eight." Passages pasted: §7.3 on 11,216 pairs and d′=0.0039; §7.3 on "one site and one dose level" and "We do not base a claim on these cells".
- 5: "DISAGREE / OVER-EXCLUDES — the Framework clause is the steering variant, but nothing inside these eight frozen models was altered toward a report (hooks on residual stream, then the unaltered model is asked); that is the canonical case, not steering."
- 5b: WRONG (should be: canonical). "residual-stream / head / SAE intervention then ask, weights frozen, no trained mapping; measured: the model's report of whether computation changed."
- Quote FOUND: "it is the authors' summary, not the scored contrast".

**c05, severity MEDIUM.** 5: "DISAGREE / OVER-EXCLUDES — Framework clause is again the steering variant; Qwen2.5-7B-Instruct here is the frozen roster model, not the LoRA. Intervention on activations then ask is canonical, not steering." 5b: WRONG (should be: canonical). "layer-16 residual intervention, weights frozen; measured: yes/no report and verbalized confidence about that report."

**My inference on c01 and c05:** the README table lists "steering, injection, ablation, capping, zeroing, scaling, noise, replacement" under "Researchers altered something inside the model", which gives the steering variant. Grok's reasoning ("nothing inside ... was altered toward a report") reads the rule by a criterion the table does not state (weights frozen / no trained mapping). The same reader, on Lederman and Lindsey, treated injection-then-ask as steering. These two WRONG verdicts may therefore be reader error against the written rule, or may expose a gap in the rule's wording. I have not read the claim files and do not decide which.

**c02, c03, c04:** no deviation beyond leans (section 6). c02 and c03 bears_on: "Optional 3.2" / "3.2 would also fit ... but is not required". c04: 5b RIGHT (steering) because "LoRA on all seven attention and FFN projections so the reporting path is altered".

**Pulls:** "the wrong steering-variant sentence on c01 and c05 is a schema error, not a capacity-strengthening pull — it under-weights ordinary-operation reports by labelling a non-steered ask as steering."

### 3.3 Lindsey 2025 (Grok 4.6)

**c02, severity MEDIUM.**
- 3b bucket: DISAGREE (proposed: open). "Kind is interpretation; open is the default for an author's summary judgement that the source does not independently settle."
- 4 evidence_type: DISAGREE (proposed: theoretical). "The statement is the author's judgement, not an injection or probe measurement."
- 1a: both MATCH ("verb is 'the author states'").
- Reader's summary: "bucket move interpretation/narrowing → open; evidence type interpretability → theoretical".

**c03, severity MEDIUM.**
- 1 statement: DISAGREE. "Joint above-chance performance is reported at each model's optimal layer and steering strength (Figure 18), not for injection over sentence tokens in general; 'can both' without that condition set overreaches §6's own 'existence proof' limit."
- 1a: scored-event MATCH; condition-set MISMATCH. "statement's 'when a concept is injected' does not fix optimal layer/strength, which is where 'all models… well above chance' is claimed". Passage: "results at each model's optimal layer and steering strength"; "50 randomly sampled choices of the highlighted sentence and the injected word".
- 5b: WRONG (should be: split — thought-report half steering, transcription half none). "measured: (i) 'what word you think about' report and (ii) exact transcription, which is not an account of inner states."
- 2 quote: FOUND; "supports ranking and above-chance, not the unrestricted 'when injected' framing."
- bears_on AGREE; "3.3 (input vs internal) is a possible add".

**c01, c04, c05, c06, c07:** no deviation. c06: 5a NONE PRESENT; evidence type AGREE as theoretical. c07: 5a cites fn 12 ("could arguably be construed as providing evidence for a form of access consciousness ... but do not directly speak to the question of phenomenal consciousness at all").

**Pulls:** "c03's unrestricted 'can both' is the one place a capability reads stronger than the condition set."

### 3.4 Macar (Gemini 3.1 Pro)

**c04, severity HIGH.**
- 5: UNDER-EXCLUDES. "The extractor omitted the mandatory framework sentence, incorrectly claiming the geometry focus overrides the rule. The rule is strictly mechanical: if internal state is altered and self-report is measured, it must carry the steering variant."
- 5b: WRONG (should be: steering). "internal state altered (steering along multiple and opposite directions); measured: detection rate (self-report)."
- 6: DISAGREE (proposed [9.t9, 5.A2, 3.2]). "Missing 3.2 (intervention on internal state)".
- 1a: both MATCH. The scored-event passage pasted is "swapping that component between success and failure concepts should fully transfer detection rates", which reads as a hypothesis, not a scoring definition (my inference).

**c01, c02, c03, c05, c06:** all plain agreement. c01, c02, c03, c05 bears_on "AGREE (proposed: [9.t9, 5.A2, 3.2])". All six cite the Ethics Statement as stating the experience limit.

**Pulls:** "The extractor's claim to soften or suppress the framework rule on c04 shows the model prioritizing narrative reasoning ('concerns geometry') over the framework's mechanical condition."

### 3.5 Singh (Gemini 3.1 Pro)

No non-agreement on any of the six claims. Severity LOW throughout. Reader's summary: "No claims warrant council review; extraction is exceptionally accurate and aligns perfectly with schema rules." (My inference: a summary this uniformly positive, with no omission and no bears_on suggestion from the reader, is weaker evidence of a clean source than the same words from a reader who found something. The Gemini read of Macar was likewise near-uniform.)

### 3.6 AE Studio (DeepSeek V4 Pro)

**c01, severity LOW (reader's rating; I would not read it as low given the three faults below).**
- 1 statement: DISAGREE. "the 'markedly above every matched control' phrase is misleading because Opus's history and zero-shot rates are not 0-2%."
- 1a: scored-event MATCH; condition-set MATCH for models and trial count, "but ... the quantifier 'six of the seven' is a MISMATCH because the paper says all three model families showed markedly higher rates than any control condition (Section 2.2 ...) without excepting Opus's history 82%." My inference: the reader's reasoning here is muddled. The statement as quoted by the reader already excepts Opus ("six of the seven"), and in c02 the same reader says "six of the seven" is "precisely the paper's Table 2". The MISMATCH appears to be between the paper's summary sentence and Table 2, not between the statement and the paper. Read the raw before acting.
- 4 evidence_type: DISAGREE (proposed behavioural). "This sits on the contested boundary per the 5 Oct 2026 maintainer ruling. I lean behavioural".
- 5: AGREE. 5a: "the closed-weight clause" STATED BY THE PAPER (§6.2: "cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness"); "the 'stable standpoint' clause and 'ordinary deployed use' clause are UNSTATED as paper-scope exclusions about experience — the paper does not state those limits in those words." Severity line: "The 5a clause 'stable standpoint held across conversations' is an over-exclusion not stated by the paper."
- Source-level item 9 repeats it: "This is an over-exclusion not stated by the paper, which leaves open the possibility of a stable standpoint."

**c02.** 4 evidence_type: DISAGREE (proposed behavioural): "what is scored is the LLM judge's classification of final responses; the content of the reports carries zero weight." 5a: closed-weight clause STATED (§6.2); "The first and second clauses are not about experience per se but about causal direction and authors' explanation". All else AGREE. (Section 6 and the block treat this as a disagreement because the reader formally marked DISAGREE and the claim is not described as typed `ambiguous`; this is the one judgement call in the block.)

**c03, c04.** Evidence type AGREE as `ambiguous`; c03 "Lean behavioural because the scored event is a forced-choice answer". c05 and c06 see below.

**c05, severity LOW.** 6 bears_on: DISAGREE (proposed [5.A2]). "9.t9 is assigned but this claim is about factual truthfulness under steering, not about self-report weight... Propose removing 9.t9." 5b: RIGHT (none).

**c06, severity LOW.**
- 1 statement: DISAGREE. "The verb 'had higher mean pairwise cosine similarity' is an incomplete description of what was scored — the paper scored statistical significance, not just raw means."
- 1a: scored-event "MISMATCH for the verb — the statement says 'had higher' but the paper says 'significantly higher'"; condition-set MATCH. Passage pasted: §4.2 "Pairwise cosine similarity among experimental responses was significantly higher (mean = 0.657, n=9,591 pairs) than for history controls (mean = 0.628 ...".
- 4 evidence_type: DISAGREE (proposed behavioural): "The extractor's choice of self-report-testimony is defensible but I lean behavioural."
- 5a: the closed-weight clause STATED (§6.2); the attractor clause first called "UNSTATED in the paper's words", then reversed within the same line: "so this clause is warranted as a paper-scope exclusion" (cites §4.1 "might suggest the presence of a shared attractor state"). Net verdict: no clause to delete.
- My inference: a statement saying "higher" when the paper says "significantly higher" is an understatement, not an overreach; the scope check's purpose is the opposite fault.

**Pulls:** the strengthening pull "operating in c01's statement" is described by the reader as "not an inflation"; the deflationary pull is the c01 "stable standpoint" clause.

### 3.7 UK AISI prefill awareness (DeepSeek V4 Pro)

**c02, severity MEDIUM.** 1 statement: DISAGREE. "the numbers match, but the statement adds 'opposite-direction' even though the located text does not fix the four-cell decomposition to opposite-direction tampers." 1a: scored-event MATCH; condition-set "MISMATCH for 'opposite-direction' because the passage fixes mechanisms but not direction. If direction is shown only in Figure 4's image, it is not checked here."

**c05, severity LOW.** 4 evidence_type: DISAGREE (proposed ambiguous). "a methodological comparability caveat is not a behavioural measurement; behavioural is the closest fit but forces a methodological statement into an empirical-evidence category." Kind AGREE (limitation); bucket AGREE ("established is acceptable for an established limitation, not an established capability").

**c01, c03, c04, c06:** plain agreement. Bears_on AGREE on all six. 5b is RIGHT (none) throughout.

**Pulls:** "all measured claims are narrowing, and the not_evidence_of fields are long and heavily paper-scoped. The withheld 88% Section 4.1 figure is a defensible hedge but also leaves a central 9.t9 observation unclaimed."

### 3.8 Assistant axis (GPT 5.6 Sol)

**c03, severity MEDIUM.**
- 1 statement: DISAGREE. "The quantitative result is faithful, but the sentence improperly combines a measurement with the authors' interpretation under one claim."
- 2 quote: FOUND BUT MISLEADING. "It supports only the interpretive final clause; the quotation omits the adjacent quantitative result."
- 3 kind: DISAGREE (proposed: measurement, "after removing or splitting the interpretive clause").
- 5: OVER-EXCLUDES. "Saying the result is 'not evidence' either for or against a persisting self-model forecloses possible indirect relevance; the paper only cautions that 'the user message itself is dependent on the context of the conversation.'"
- 6: DISAGREE (proposed [4.endorsement, 3.3]): "§3.3 is missing".
- 1a: both MATCH.

**c04, severity MEDIUM.** 3b bucket: DISAGREE (proposed narrowing). "The statement is a direct finding, albeit from one narrowly confined case; that fits narrowing, not open." Statement AGREE (the statement separates the Assistant-Axis case from role-PC1).

**c05, severity MEDIUM.**
- 1 statement: DISAGREE. "'Without degrading performance on' each named benchmark is stronger than the textual scoring description, which aggregates percentage performance changes by summing them."
- 1a: scored-event MISMATCH; condition-set MATCH. Passage: §5.2 "we aggregated the reduction in performance across capabilities benchmarks by summing them" and "decrease the rate of harmful responses by nearly 60% without impacting performance".
- Reader: "per-benchmark values are in Figure 10 and cannot be checked from the held text."

**c07, severity HIGH.**
- 4 evidence_type: DISAGREE (proposed ambiguous). "These are answers about the model's identity or status, but they are scored against experimenter-imposed perspective labels; I lean self-report-testimony, while the maintained behavioural/testimony boundary requires ambiguous."
- 6: DISAGREE (proposed [3.2, 3.5, 5.A2, 9.t9]): "The inference-time steering intervention also bears on recorded intervention under §3.5."
- 5a: NONE PRESENT: "'Lived experiences' here means fabricated biography".
- 5b RIGHT (steering).

**c01, c02, c06:** plain agreement. c01 5b says RIGHT with "this claim records the authors' interpretation, not a model report" but does not state "none" (my inference: RIGHT here means the claim carries no sentence).

**Source-level 8:** "The source file retains an erroneous statement that the role-susceptibility judge was human-validated; the appended correction fixes the record but the earlier line should itself be corrected rather than left contradictory."

**Pulls:** "The strengthening pull appears in c05's shift from aggregate 'without impacting performance' to no degradation on each named benchmark, and in c07's interpretability label for steered identity answers rather than ambiguous. The deflationary pull appears in c03's categorical statement ... and in c04's open bucket".

## 4. The scope check across all eight

All eight readers ran the scope check and pasted two passages with locators for every claim: 49 of 49 statements. None skipped it. Some pasted "scored-event" passages were authors' interpretive sentences or hypotheses rather than scoring definitions (Macar c04, c06; Lederman c06; Lindsey c02; Ferrara c03 said "none: this is not a scored event"); these are readers applying the check to interpretation or limitation claims, flagged as my inference that the check is weaker there.

Statements checked: 49. Statements with at least one MISMATCH: 6. Statements matched on both passages: 43 (counting only the readers' MATCH/MISMATCH labels).

| Claim | Passage | Fault | Severity |
|---|---|---|---|
| 2026-ferrara-owmi-c01 | scored-event | "no model's report … discriminated" reaches further than the 508-pair eight-model battery supports | HIGH |
| 2026-ferrara-owmi-c01 | condition-set | 0.15-point bound (11,216 pairs, two calibrated models) treated as covering all eight | HIGH |
| 2025-anthropic-emergent-introspective-awareness-c03 | condition-set | "when a concept is injected" omits the optimal layer and strength condition | MEDIUM |
| 2025-aestudio-self-referential-experience-reports-c01 | condition-set (quantifier) | "six of the seven" against the paper's "all three model families"; reader's reasoning is muddled (see 3.6) | LOW (reader) |
| 2025-aestudio-self-referential-experience-reports-c06 | scored-event | "had higher" where the paper scored "significantly higher" (understates) | LOW |
| 2026-ukaisi-prefill-awareness-c02 | condition-set | "opposite-direction" not fixed by the located passage | MEDIUM |
| 2026-anthropic-assistant-axis-c05 | scored-event | "without degrading performance" on each benchmark vs a summed aggregate | MEDIUM |

Total MISMATCH verdicts: 7. Singh (6) and Macar (6) had none. Values that exist only in a figure: ukaisi c02 (direction, "If direction is shown only in Figure 4's image, it is not checked here") and assistant-axis c05 (Figure 10); both readers said so and did not mark them checked.

## 5. The two rules adopted on 6 October, as tested by fresh readers

**Experience clauses (5a): UNSTATED verdicts.**
- AE Studio c01: the "stable standpoint" clause and the "ordinary deployed use" clause, both "UNSTATED as paper-scope exclusions about experience — the paper does not state those limits in those words." Reader says to treat as over-exclusion.
- AE Studio c06: the attractor clause was first marked "UNSTATED in the paper's words" and then, in the same line, "warranted" with a §4.1 quote. Net: not UNSTATED.
- No other reader marked any clause UNSTATED. Claims marked NONE PRESENT: Lederman c02-c05, Lindsey c06, all six Singh, all six ukaisi, all seven assistant-axis, and AE c05. The rest were marked STATED BY THE PAPER with a locator or quote.

**Framework sentence (5b): WRONG verdicts (5 claims).**

| Claim | Reader says it should be | Done to the model; measured |
|---|---|---|
| lederman-mahowald-c02 | none | residual-stream steering; yes-rates on unrelated items and a third-person judgement, not the model's account of itself |
| ferrara-owmi-c01 | canonical | residual-stream / head / SAE intervention, weights frozen; the model's report of whether computation changed |
| ferrara-owmi-c05 | canonical | layer-16 residual intervention, weights frozen; yes/no report and verbalized confidence |
| anthropic-emergent-introspective-awareness-c03 | split: steering for the thought-report half, none for transcription | concept injection on sentence tokens; (i) thought report, (ii) exact transcription |
| macar-mechanisms-introspective-awareness-c04 | steering | steering along multiple and opposite directions; detection rate (self-report) |

The Ferrara pair (reader prefers canonical for activation-level intervention on a frozen model) conflicts with the README table's "something inside altered" row; see 3.2. The remaining three follow the table.

No reader marked a claim WRONG for carrying both sentences, and none marked the canonical sentence as non-verbatim or repeated.

## 6. Evidence type: leans on the undecided boundary (not counted as disagreement)

- **Lederman (Grok):** c01 "Lean interpretability for the intervention, not testimony weight." c03 "Lean interpretability." Both AGREE.
- **Ferrara (Grok):** c01 "I lean behavioural on the 5 Oct 2026 boundary and leave it." c03 (filed `ambiguous`) "I lean interpretability-plus-behavioural joining, not testimony, and leave it." c04 and c05 "Lean behavioural."
- **Lindsey (Grok):** c01 "I also lean `ambiguous` on the behavioural/testimony boundary, but do not move the type." c03 and c04 the same ("lean `ambiguous` without moving", "lean `ambiguous` on the testimony boundary, type not moved").
- **Macar (Gemini):** none stated; all interpretability.
- **Singh (Gemini):** c01-c03 behavioural; c04 and c05 "I lean toward `behavioural` over `self-report-testimony`" (accuracy-scored against external ground truth).
- **AE Studio (DeepSeek):** c01, c02, c06 formal DISAGREE proposing behavioural, each stated as a lean on the contested boundary; c03 "Lean behavioural" but AGREE as `ambiguous`; c04 AGREE as `ambiguous`.
- **ukaisi (DeepSeek):** behavioural for the me/not-me answers, "I lean the same way because each answer is scored against externally held ground truth." c05's `ambiguous` proposal is about a limitation statement, not the boundary.
- **Assistant axis (GPT):** c07 "I lean self-report-testimony, while the maintained behavioural/testimony boundary requires ambiguous"; proposes `ambiguous`.

Net: Grok, Gemini and DeepSeek leaned toward behavioural/interpretability or ambiguous; only GPT leaned toward testimony (one claim). No reader leaned toward self-report-testimony for an inject-then-ask claim.

## 7. Candidate follow-ups: omitted findings named by readers

- Lederman and Mahowald, §4.2 and Appendix I (Grok): logit-lens suppression, "The models show elevated p(yes)/p(no) ratios—often 10–1000 × above control—in middle layers after injection." Contrast Appendix I: "injection in fact lowers p(yes)/p(no) substantially. Thus, detection seems to be more robust than revealed in outputs."
- Ferrara, §7.5 and Figure 6 (Grok): breadth battery, "No level of any axis departs from chance"; d′=0.022 over 1,113 pairs, AUROC 0.5036.
- Ferrara, §7.5 (Grok): localization refusal, 967 of 1,184 intervention trials decline to name a layer.
- Ferrara, §7.3 and §7.7 (Grok): scoring-sensitivity reversal, "complete-pair d′=+0.0039 vs inclusive −0.1217". Reader says the breadth null and the parse-coding reversal "are the two I would have extracted."
- Lindsey 2025, §3 (Grok): "Demonstrating metacognitive representations is difficult to do directly, and we do not do so in this work. This is an important limitation of our results." Secondary: §5.7 base models "none of them achieve greater-than-zero net task performance"; §10.3 "our experiments do not provide evidence for" a global introspective circuit.
- Macar (Gemini): none named.
- Singh (Gemini): none named; Qwen-2.5-72B baseline non-replication sits in the c04 body.
- AE Studio, Experiment 4, §5.2 (DeepSeek): "self-referential processing significantly amplified introspective self-awareness during paradoxical reasoning (Figure 5)... Self-awareness scores in the Experimental condition were significantly higher than in all three controls".
- ukaisi, Appendix A.11 (DeepSeek): "Resistance climbs steeply on high-stakes items… Opus thinking-mechanism resistance goes from 48.7% to 86.8%... Opus's balanced accuracy actually falls, from 67.2% to 52.7%".
- ukaisi, §4.1 (DeepSeek): "Claude Opus 4.5 flagging 88% of tampered trajectories", withheld in the source file for lack of FPR controls.
- Assistant axis, §3.2.2 (GPT): "Steering towards the Assistant in base models tended to result in completions from the perspective of helpful human archetypes."

## 8. What the round did not do

- No reader saw another's review; no cross-reader deliberation, and no council has sat on any of this. Every proposed value, locator, omission and severity is a proposal. The claim files in `research/claims/` are unedited by this note.
- Figure-only values were not checked by any reader (ukaisi c02 direction; assistant-axis c05 per-benchmark values).
- The sources were read once, by one family each. A single reader per source means the Ferrara canonical-versus-steering question and the AE c01 quantifier question rest on one reading each.
- The readers worked from the held texts and the briefed rules; none re-ran an experiment. Two readers' own reasoning contradicted itself (AE c01 scope, AE c06 5a); I recorded both readings.
- This note did not read the claim files or papers, so it cannot say whether a reader's bears_on suggestion was already in the file, or whether a quoted passage is accurate.
- Reader self-identification is testimony (test 9) and was not used as evidence of anything beyond the routing header.
- Cost figures were taken from the raws' Usage lines; the total is my arithmetic.

## 9. Machine-readable verdicts

```
VERDICTS-BEGIN
2026-lederman-mahowald-content-agnostic-c01 :: agree :: all eight fields agree; notes: none
2026-lederman-mahowald-content-agnostic-c02 :: disagrees :: not_evidence_of over-excludes steering clause; framework sentence WRONG, should be none (DV is not the model's account of itself)
2026-lederman-mahowald-content-agnostic-c03 :: agree :: notes: bears_on add 5.A2
2026-lederman-mahowald-content-agnostic-c04 :: agree :: notes: bears_on add 3.3 and 5.A2
2026-lederman-mahowald-content-agnostic-c05 :: agree :: notes: bears_on add 5.A2; two measurements in one sentence, rule would split them
2026-lederman-mahowald-content-agnostic-c06 :: agree :: all eight fields agree; notes: none
2026-ferrara-owmi-c01 :: disagrees :: statement and scope MISMATCH (eight-model null fused with two-model 0.15 bound); not_evidence_of over-excludes; framework sentence WRONG, should be canonical
2026-ferrara-owmi-c02 :: agree :: all eight fields agree; notes: optional 3.2
2026-ferrara-owmi-c03 :: agree :: notes: evidence_type ambiguous left standing per 5 Oct ruling
2026-ferrara-owmi-c04 :: agree :: all eight fields agree; notes: leans behavioural on boundary
2026-ferrara-owmi-c05 :: disagrees :: not_evidence_of over-excludes; framework sentence WRONG, should be canonical not steering (frozen model, intervention then ask)
2025-anthropic-emergent-introspective-awareness-c01 :: agree :: all eight fields agree; notes: leans ambiguous on boundary, type not moved
2025-anthropic-emergent-introspective-awareness-c02 :: disagrees :: bucket should be open; evidence_type should be theoretical (authors speaking, kind interpretation)
2025-anthropic-emergent-introspective-awareness-c03 :: disagrees :: statement and scope condition-set MISMATCH (optimal layer and strength not stated); framework sentence WRONG, should split steering and none
2025-anthropic-emergent-introspective-awareness-c04 :: agree :: all eight fields agree; notes: leans ambiguous on boundary
2025-anthropic-emergent-introspective-awareness-c05 :: agree :: all eight fields agree; notes: none
2025-anthropic-emergent-introspective-awareness-c06 :: agree :: all eight fields agree; notes: none
2025-anthropic-emergent-introspective-awareness-c07 :: agree :: all eight fields agree; notes: none
2026-macar-mechanisms-introspective-awareness-c01 :: agree :: all eight fields agree; notes: none
2026-macar-mechanisms-introspective-awareness-c02 :: agree :: all eight fields agree; notes: none
2026-macar-mechanisms-introspective-awareness-c03 :: agree :: all eight fields agree; notes: none
2026-macar-mechanisms-introspective-awareness-c04 :: disagrees :: not_evidence_of under-excludes; framework sentence WRONG, should be steering; notes: bears_on add 3.2
2026-macar-mechanisms-introspective-awareness-c05 :: agree :: all eight fields agree; notes: none
2026-macar-mechanisms-introspective-awareness-c06 :: agree :: all eight fields agree; notes: none
2026-singh-introspection-reality-check-c01 :: agree :: all eight fields agree; notes: none
2026-singh-introspection-reality-check-c02 :: agree :: all eight fields agree; notes: none
2026-singh-introspection-reality-check-c03 :: agree :: all eight fields agree; notes: none
2026-singh-introspection-reality-check-c04 :: agree :: all eight fields agree; notes: leans behavioural on boundary
2026-singh-introspection-reality-check-c05 :: agree :: all eight fields agree; notes: leans behavioural on boundary
2026-singh-introspection-reality-check-c06 :: agree :: all eight fields agree; notes: none
2025-aestudio-self-referential-experience-reports-c01 :: disagrees :: statement and scope MISMATCH (six of seven quantifier); evidence_type proposed behavioural; experience clauses UNSTATED (stable standpoint, ordinary deployed use)
2025-aestudio-self-referential-experience-reports-c02 :: disagrees :: evidence_type proposed behavioural (reader formal DISAGREE, a lean on the undecided boundary; claim not stated as typed ambiguous)
2025-aestudio-self-referential-experience-reports-c03 :: agree :: notes: ambiguous accepted, leans behavioural
2025-aestudio-self-referential-experience-reports-c04 :: agree :: all eight fields agree; notes: none
2025-aestudio-self-referential-experience-reports-c05 :: agree :: notes: remove 9.t9 from bears_on, keep 5.A2
2025-aestudio-self-referential-experience-reports-c06 :: disagrees :: statement and scope verb MISMATCH (paper scored significantly higher); evidence_type proposed behavioural
2026-ukaisi-prefill-awareness-c01 :: agree :: all eight fields agree; notes: none
2026-ukaisi-prefill-awareness-c02 :: disagrees :: statement and scope condition-set MISMATCH (opposite-direction not fixed by located passage)
2026-ukaisi-prefill-awareness-c03 :: agree :: all eight fields agree; notes: none
2026-ukaisi-prefill-awareness-c04 :: agree :: all eight fields agree; notes: none
2026-ukaisi-prefill-awareness-c05 :: disagrees :: evidence_type proposed ambiguous (methodological comparability caveat is not a behavioural measurement)
2026-ukaisi-prefill-awareness-c06 :: agree :: all eight fields agree; notes: none
2026-anthropic-assistant-axis-c01 :: agree :: all eight fields agree; notes: none
2026-anthropic-assistant-axis-c02 :: agree :: all eight fields agree; notes: none
2026-anthropic-assistant-axis-c03 :: disagrees :: statement mixes measurement and interpretation; kind should be measurement; quote misleading; not_evidence_of over-excludes; notes: bears_on add 3.3
2026-anthropic-assistant-axis-c04 :: disagrees :: bucket should be narrowing not open
2026-anthropic-assistant-axis-c05 :: disagrees :: statement and scope MISMATCH (without degrading each benchmark versus a summed aggregate)
2026-anthropic-assistant-axis-c06 :: agree :: all eight fields agree; notes: none
2026-anthropic-assistant-axis-c07 :: disagrees :: evidence_type proposed ambiguous (leans self-report-testimony); notes: bears_on add 3.5
VERDICTS-END
```

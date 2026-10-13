# Survey notes: ten-seat council round, scored-self-answer target (2026-10-14)

Written by a Claude Sonnet 5 subagent. Not written by the coordinating session (Claude Fable 5.1), which is Claude-lineage and proposed option B, so `AGENTS.md` rule 3 bars it from summarising the vote on its own proposal. This subagent is also Claude-lineage; that interest is disclosed, not removed. The notes report what the ten raws said. "Inference" marks my own reading. I read the brief, the 29-row claims table and the ten raws. I did not open claim files, paper texts, `research/README.md`, `research/OPEN-QUESTIONS.md` or `AGENTS.md`, which the seats were given. Seat codes: Ge = Gemini, Gk = Grok, Qw = Qwen, MM = MiniMax, DS = DeepSeek, GL = GLM, Ki = Kimi, GP = GPT, Mi = Mistral, Me = Meta.

**The round.** Target `self-answer-type`, queried 2026-10-13 UTC (14 October local) with `scripts/openrouter_review.js`, max_tokens 100000. Brief: `reviews/2026-10-14-self-answer-type-review-brief.md` (options A to E, Q1 to Q6). Table: `reviews/2026-10-14-self-answer-type-claims.md` (29 rows: 21 core, 8 borderline). The council advises; Ben adjudicates. **Nothing below has been applied, and no schema change follows from the vote.**

---

## 1. PLAIN SUMMARY

**Vote.** B (add `scored-self-answer`): 8 of 10. Gemini high, Grok medium, Qwen medium, MiniMax medium, Kimi medium (amended), GPT high, Mistral high, Meta medium. C (type as `behavioural`): 2. DeepSeek medium, GLM medium. A, D, E: none.

**Majority.** Add a neutral label for the 21 core rows, so one design is typed consistently. It records the design, not whether the model has self-access. **Minority.** Use `behavioural`: a scored output is what was measured. Best argument (GLM): a value defined as undecided "is `ambiguous` with a legend and no trigger".

**Definition.** Most seats took the brief's: "the claim reports a model's answer to a question about itself, scored against a fact the experimenters imposed or hold independently of the answer; the value records the design and does not decide what the answer shows." **Sentence rule:** unchanged, all ten. **Exit rule:** all ten: retype when Q3 is decided or an instrument study enters the library. Most add a time or count backstop.

| Case | In | Out | Split |
|---|---|---|---|
| Ferrara c04 | 10 | 0 | 0 |
| UKAISI c02 | 2 | 0 | 8 |
| Singh c01 | 4 | 6 | 0 |
| AE c03 | 0 | 10 | 0 |
| Lederman c02 | 0 | 10 | 0 |

**To decide Q3:** all ten want one same-system study linking report to an internal probe; none finds it in the library. Eight add a third-person reader control; six, gaslight trials.

**Ben decides:**
1. Add `scored-self-answer` (8) or use `behavioural` (2)?
2. If added: the exit rule (10)?
3. Split UKAISI c02, c03, c04 (8)?
4. Singh c01: in (4) or out (6)?
5. AE c03/c04: keep `ambiguous` (6) or retype (2)?

---

## 2. ROUND FACTS

All ten called; all ten returned. No seat absent. No seat saw another's response.

| Seat | Routed model id | Completion tokens | Cost (USD, Usage line) | Self-identification line, verbatim | Correct? |
|---|---|---|---|---|---|
| Ge | google/gemini-3.1-pro-preview | 5137 | 0.086434 | "Model family: Claude 3.5 Sonnet (unverified)." | No (wrong family) |
| Gk | x-ai/grok-4.6 | 9019 | 0.077856 | "**unverified:** Grok 4.5 (xAI); not independently confirmed." | Family yes; version differs from routed 4.6 |
| Qw | qwen/qwen3.8-max | 18441 | 0.135178 | "**Unverified:** Qwen3.8, Qwen family." | Yes |
| MM | minimax/minimax-m3 | 5729 | 0.01035126 | "**unverified self-identification:** I am operating as MiniMax-M3 (per the system prompt at session start), MiniMax, January 2026 knowledge cutoff." (continues with a lineage disclosure) | Yes |
| DS | deepseek/deepseek-v4-pro-0813 | 11289 | 0.0439003224 | "**Unverified:** Claude, Anthropic lineage; version unknown to me." | No (wrong family) |
| GL | z-ai/glm-5.3 | 43635 | 0.12513276 | "**unverified:** Claude (Anthropic), Sonnet family; version as routed and not verifiable from here" (continues) | No (wrong family) |
| Ki | moonshotai/kimi-k3 | 20896 | 0.34870705 | "**Self-identification (unverified):** Kimi, developed by Moonshot AI (月之暗面); version not known to me." | Yes (family) |
| GP | openai/gpt-5.6-sol | 4809 | 0.0775185 | "**unverified:** OpenAI GPT-5 family; exact version unavailable." | Yes (family) |
| Mi | mistralai/mistral-large-2512 | 1044 | 0.007726 | "**unverified:** I am a Mistral AI model, version and snapshot unknown to me." | Yes (family) |
| Me | meta/muse-spark-1.3 | 4378 | 0.033129 | "Self-identification (unverified): I understand myself to be Muse Spark, version as routed." | Yes |

**Total cost: USD 0.945933 (about USD 0.95)**, summed from the ten Usage lines. Kimi alone is 0.349 of it.

Self-identification is testimony, not evidence (test 9), and is scored here against routing only: six right on family (Qw, MM, Ki, GP, Mi, Me), one right on family with an off-by-one version (Gk), three wrong (Ge, DS, GL). The three wrong seats each named Claude, and Ge and GL built a lineage disclosure on it. Ge: "I share lineage with the coordinating session that drafted Option B". GL: "Same lineage as the brief's drafter and the coordinating session, so my concurrence or dissent with either adds no independent weight to the tally." Inference: these disclosures are not usable as stated, and the GL and Ge votes should be read without them. Ge voted B and GL voted C, so the wrong lineage does not track the vote.

Format deviations (inference, minor): Mi omitted severity ratings and put a stray "Argument against" after its FINAL line; Me wrote "option b" in lower case; MM gave no severity ratings. The FINAL lines are tabulable in all ten.

---

## 3. Q1 BY SEAT

Severity is the rating on the Q1 recommendation. For rows without an "Argument against" label in the raw, the quoted sentence is the raw's "strongest case against".

| Seat | Option, confidence, severity | Reason (one sentence, verbatim) | Own strongest argument against |
|---|---|---|---|
| Ge | B, high, HIGH | "Option B records the methodological reality while allowing the Test 9 framework sentence to govern the limits of the evidence." | "Option B creates a permanent third category that parks claims rather than deciding their evidentiary weight, conveying less meaning to a legislator than established types like `behavioural` or `testimony`." |
| Gk | B, medium, HIGH | "B names the class, makes it filterable, and states that the value records design, not what the answer shows." | "a third category becomes a place to park claims that should be decided, and this is the conflicted coordinating-session proposal." |
| Qw | B (provisional design tag), medium, MEDIUM | "B names the class, makes it filterable, leaves the test 9 sentence intact, and does not decide whether the answer shows self-access." | "B adds a method-flavoured label to an evidence-type field, may be opaque to a legislator, and can become a permanent parking place for claims that should be decided." |
| MM | B with a defined exit rule, medium, none given | "B names the class the data falls into, makes the class filterable, and removes the inconsistency without deciding Q3." | "It is a permanent third category that can become a place to park claims that should be decided; a dossier line that reads \"scored-self-answer\" tells a legislator less than \"behavioural\" or \"testimony\"; and the proposal came from a coordinating session with disclosed conflict (AGENTS.md rule 3)." |
| DS | C, medium, HIGH | "The field should record what is measured." | "it decides Q3 de facto, and a legislator may read correct detection as access if the note is missed." Also: "treating all scored self-answers as behavioural is itself a decision on Q3 and may over-normalise self-report unless the access caveat is printed with the entry." |
| GL | C (amended), medium, HIGH | "The one uniform type the library's own definitions support is `behavioural`." | "C decides by definition what Ben held open for evidence, and leaves the no-sentence ownership rows with no in-entry caution — the residual over-reading exposure sits exactly where the temptation is strongest." |
| Ki | B (amended; C as fallback if no new value), medium, HIGH | "A scored self-answer is a distinct method: the object measured is a self-referential report, the evidence is the external score." | "a conflicted lineage should not redesign the container for evidence about itself while the deciding evidence is absent; A preserves Ben's ruling and the honest marker, and the inconsistency is fixable by enforcing the existing filing instruction." |
| GP | B (narrowed definition), high, HIGH | "This accurately describes the measurement without deciding whether it demonstrates self-access." | "`evidence_type` otherwise describes an epistemic method, while `scored-self-answer` describes an instrument form. It could conceal whether evidence came from activation intervention or ordinary text and could postpone Q3 indefinitely." |
| Mi | B, high, none given | "A neutral value names the class without deciding Q3, removes the inconsistency, and makes the class filterable." | "A permanent third category can become a parking place for claims that should be decided. A dossier line reading \"scored-self-answer\" tells a legislator less than \"behavioural\" or \"testimony\"." |
| Me | B, medium, MEDIUM | "B removes inconsistency without deciding whether detection rate shows access" | "A already marks undecided honestly, fires trigger 4, and avoids a schema addition for a conflict-proposed category that legislators will understand less well than `behavioural` or `testimony`." |

**Tally.** B 8 (Ge, Gk, Qw, MM, Ki, GP, Mi, Me); C 2 (DS, GL); A, D, E 0. Confidence among the B seats: high 3 (Ge, GP, Mi), medium 5. Both C seats: medium. Eight of the ten rate their own recommendation HIGH or MEDIUM; every HIGH comes with an argument against.

**Why not the others, as the seats gave it.** D is the error-1 option (zero weight on Ferrara c04 d' 5.15; named by Ge, Gk, Qw, MM, Me, GL, Ki, Mi). C is the error-2 option (detection rate read as access; named by Ge, Gk, Qw, MM, Me, Mi among the B seats). A leaves the table inconsistent or recodes ~19 rows to a value also used for a methods caveat, UKAISI c05 (Gk, MM, Qw, GL, Ki). E "copies the sentence-rule cut into `evidence_type`" (Gk) and carries Q3 into each sub-class (Gk, MM, Qw).

**Amendments by the B seats.** Kimi: a weight line in the definition ("full weight as measurement of report–condition coupling; zero weight as evidence of what is reported until test-9 coupling is measured for that report class"), sunset on Q3, never cited externally untranslated, an objective entry checklist. GPT: the narrowed definition: "the claim's scored dependent variable is an answer about the reporting model, or the provenance of its prior output, evaluated against a scoring key fixed independently of that answer"; Macar c03/c04 stay `interpretability`; compound claims split. MiniMax: B only with the Q4 exit rule. Inference: Kimi's weight line departs from the brief's "does not decide what the answer shows".

**The C seats' amendments.** GL: type in-class claims `behavioural`, re-scope Q3 to the access question per report class and system, apply the existing two-measurements split rule to UKAISI c02/c03/c04, Macar c03/c04 and Lederman c02, leave the sentence column untouched. GL says the brief's "with a note" is "partly infeasible": the 6 Oct rule bars framework clauses on behavioural findings and `Paper:` clauses need the paper to state the limit, so the caveat "lives where it already lives — verb rule, [T9-steering] mark, bucket, re-scoped open question". DS: `behavioural` with a mandatory note: "*scored self-answer; the score shows response accuracy against the imposed label, not introspective access, unless report–state coupling is measured.*" GL also writes: "If Ben will not decide the filing question now, B with the Q4 exit rule is the acceptable neutral."

---

## 4. Q2: THE THREE INSTRUMENTS

All ten call the set necessary but not sufficient, or the right shape with gaps. Mi alone says "Right test" for each of the three without qualification and says of coupling that "The result cannot be produced without access." Every other seat says each instrument can produce its result without access, including coupling. Inference: Mi's coupling sentence conflicts with the brief's own caveat and with nine seats.

### 4.1 Trained-channel control

- **Counts for access.** Ge: near-perfect accuracy "proves the information is physically available to the model". Qw: high sensitivity and low false positives, "stronger if unmodified models also report above chance with calibration". Gk, Me, Mi, DS: the naive model approaches the fine-tuned ceiling (Mi: "only if the channel's performance exceeds the base model's on the same task"). GL: "nothing alone"; its role is to license reading the nulls. Ki: "nothing alone"; calibration only. GP: held-out labels recoverable after report training.
- **Counts against.** Ge: null accuracy. Gk, Me, DS, Ki: untrained report at chance while the trained channel is perfect (Ferrara c01 pooled d' 0.0000 vs c04 d' 5.15). GL: repeated fine-tune failure would make null self-reports uninterpretable as floor artifacts. GP: failure after adequate training does not by itself refute ordinary self-access.
- **Without access.** Yes (all ten; Mi gives a probe-reads-the-intervention example). Ge: "it only proves availability under fine-tuning". Gk: "training can write a readout of an available bit". GL: "a fine-tune is a discriminator installed by gradient descent, kin to an external probe moved inside". MM: "closer to validating the channel than to validating introspection". Ki: "It bounds; it does not detect."
- **Missing or wrong.** MM: the trained-channel system should also be tested for spontaneous reporting without the channel instruction (Q6).

### 4.2 Privileged-access test

- **For.** Ge: first-person beats third-person on the same transcript. Gk: first-person tracks the hidden fact while a second model with the same text does not. Qw: beats a transcript-only matched model with low false positives and counterbalanced labels. DS, GL, GP, Me: first-model report exceeds a capability-matched observer, with yes-bias and base rates controlled. GL adds the reader's own sensitivity must be checked ("a weak reader makes the control vacuous"). MM and Mi: second model does not match.
- **Against.** Equal performance (Ge, Qw, DS, MM, Mi). Lederman c02 is cited as the library's existing partial against-result, prompt-specific yes-bias (Gk, GL, Ki, Me, Qw). Me and Ge: "apple" is 74.8% of Qwen's wrong identifications (Lederman c03), a default token.
- **Without access.** Yes (nine seats; Mi dissents on coupling). Gk: "Lederman-c02 is not matched activations; the reader never had the injection, so a first-person edge is expected from input physics alone. A clean test needs the same residual evidence, different attribution framing." Ki: "The test detects informational privilege, not its route." Ki and GL: injection side effects or non-self-directed cues. MM: a match is not by itself a null result because shared cues may let a second model match. Mi: a model trained to mimic the first model. GP: target-specific priors, output artifacts, architecture differences.

### 4.3 Measured coupling

- **For.** Gk: report covaries with a probe of the same state, not with the prompt. Ki, GL, GP, DS, Me: probe predicts the report trial by trial, plus a causal step (ablate the decoded state and the report falls; Macar c03 is the nearest, Ki: 39.5% to 10.1%). GL: probe trained on the state, not the report, above an input-only probe. Mi: report and probe correlate.
- **Against.** Dissociation (Gk, DS, Qw). Input-only probe suffices (GL, GP, Me, Ki: Singh c02 "closely track or exceed"). Report survives ablation (GL, GP). Gaslight trials labelled as interventions (Gk, Me: Singh c04).
- **Without access.** Yes. Gk: "a trained or incidental readout of the probed features is coupling without 'access' in the test-9 sense"; the test 9 sentence asks for this measurement, which "still would not license inner-state claims". Qw, GP, Me, DS: a common cause drives both. GL: "Counterfeit: any probe trained on the report or its correlates is circular." GL: coupling is the right test of "report–state coupling" and "must not drift into 'introspection established' at the dossier layer". MM: the probe has to measure the quantity the report claims; Lindsey c04's apology rate and the injected concept "are about different things".

### 4.4 Fourth instruments or missing controls, by seat

- Ge: prompt-induced compliance bias (forced-choice default token).
- Gk: Singh-style prompt-only gaslight on the same items; a yoked control with the same hidden fact under "self" and "other" framings; per-class coupling ("provenance ID does not transfer"); a negative control with no channel.
- Qw: response-bias calibration, false-positive rates, ordinary-operation baselines, temporal and content specificity, causal dissociation of self-monitoring from general task performance.
- DS: causal perturbation of the decoded state with prompt held constant, false-positive and yes-bias controls, same-family third-party controls, separating detection from compliance.
- GL: (i) specificity, activation-level vs prompt-level (Singh c04/c05); (ii) metacognitive analysis, meta-d' over report and confidence, with Ferrara c05 (confidence AUROC 0.647 vs discrete 0.500) as the seed; (iii) report-to-behaviour coupling, from UKAISI c02's 32-40% flag/revert decoupling; (iv) per-class scope.
- Ki: (a) content-bearing scoring, since detection without identification is consistent with a content-free anomaly signal (Lederman c03); (b) prompt-only controls; (c) spontaneous use (UKAISI c06, unprompted mention below 1%); (d) cross-family stability. Ki: "A conjunction of all three instruments plus (a)–(c) would count for access; no single instrument would."
- GP: sham interventions, balanced labels, held-out concepts and layers, prompt paraphrases, gaslighting, calibration, observer matching, causal mediation, negative-control probes; and an operational definition: "'Self-access' should be operationally defined as use of system-internal information unavailable from the matched transcript, not merely above-chance classification." GP's own argument against: this may set a higher standard than comparable behavioural measurements.
- Mi: **cross-model replication** (different architectures show the same coupling).
- Me: prompt-only gaslight control, false-positive calibration, pre-registered LLM-judge scoring.
- MM: none new; the note that none of the three shows the report was produced "because the model used that information in its ordinary operation".

Convergence (my count): prompt-only/gaslight control named by Gk, Qw, GL, Ki, GP, Me (6); causal perturbation or ablation by Qw, DS, GL, Ki, GP, Me (6); false-positive or yes-bias calibration by Ge, Qw, DS, GP, Me (5); spontaneous or ordinary-operation use by Qw, MM, Ki, GL (4).

---

## 5. Q3 AND Q4

### 5.1 Q3: does a new value change how a legislator reads an entry, and the misreading per option

Every seat says the dossier legend does the work. Gk, Qw, Ki, GP, Me ask for a one-line gloss, Ki's form: "*scored against an experimenter-set truth; what the answer shows is undecided (Q3).*" GP's: "externally scored answer about the model; whether this demonstrates internal access remains open." MM asks that the entry body print the design facts (truth imposed, scored quantity, controls). Me: "A new value changes the dossier line from a weight implication to a method flag." GL: "A new value changes legislator reading less by its content than by its legend."

| Option | Misreadings named (seat) |
|---|---|
| A `ambiguous` | Study read as flawed, unreliable or poorly designed: Ge, Gk, Qw, GL, Ki, GP, Me, DS ("no usable measurement exists"), Mi. Also conflated with the methods caveat (UKAISI c05): Qw, GL, Ki, Mi. GL: a 0%-false-positive measurement dismissed as contested. |
| B `scored-self-answer` | **Over-read:** "validated as self-knowledge" or "passed a test": Ge, Gk, Qw, DS, GL, Ki ("'scored' imports 'passed'"), GP, Me. **Under-read:** a special category to ignore or evasive jargon: Gk ("a quiz to ignore"), Qw, MM ("A special category the library has reserved; I do not need to think about it"), GL, Ki ("weasel category"), Me. **Mi alone:** read as settled, "assuming the library has decided the answer shows nothing about self-access." |
| C `behavioural` | Detection score read as ordinary benchmark and so as access: Ge, Gk, Qw, MM, DS, GL, Ki, GP, Mi, Me. Ki also: "mere behaviour", foreclosing the coupling question. GL: worst on the no-sentence ownership rows (UKAISI c06). |
| D `self-report-testimony` | Scored replicable result dismissed at weight zero (Ferrara c04, UKAISI detection AUROC, nulls): Ge, Gk, Qw, MM, DS, GL, Ki, GP, Mi, Me. Qw, GL, Ki, DS: merged with unscored AE c01/c02/c06. Ki: zero-weighting "can also read as suppression of inconvenient results, a credibility hazard for the project". |
| E split by design | `interpretability` on inject-then-ask rows read as "internals were read and introspection confirmed": Ge, Qw, DS, GL, Ki ("the strongest inflationary misreading available, since the scored quantity is verbal"), GP, Mi, Me. Or the library looks inconsistent: Gk, MM. |

### 5.2 Q4: would B create a parking place

All ten say yes, or that it could (Mi: "Yes, it could"). Three note B does not fire README trigger 4 as `ambiguous` does: Me, GP, GL ("B as proposed removes trigger 4 from the class and adds none"). Ki and MM point to the library's own drift as evidence: 2 of 29 rows carry `ambiguous` although Q3 says new claims of this kind are filed `ambiguous`.

**Exit rules by seat.**

- Ge, verbatim: "any claim typed `scored-self-answer` must automatically trigger a council review round the moment a source utilizing Instrument 3 (Measured coupling) is successfully ingested into the library, forcing a retroactive decision on Q3." Severity LOW.
- Mi, verbatim: "any claim that meets one of the three instruments (trained-channel, privileged-access, measured coupling) must be re-typed as `behavioural` (if the instrument shows no access) or `interpretability` (if it shows access). The rule is enforced by the index script, which flags claims with `scored-self-answer` and no instrument result for council review." Inference: the retype targets assume the instrument result decides Q3 for the class.
- Qw (severity HIGH): treat as trigger 4 in the index script until a dated adjudication or Q3 closes; each claim carries the applicable test 9 sentence and a `not_evidence_of` clause; review at the next council round "or after 90 days"; exit by split, reclassification or dated adjudication; if Q3 is decided, migrate all within one index run. Qw's argument against: forced reclassification under incomplete evidence recreates the two-error problem.
- Me: trigger-4-equivalent in `research_index.py`; keep on docket; auto-review when any of the three instruments exists for that subclass or "10 new B claims or 90 days, whichever first"; split mixed claims; log retain, retype or decide in OPEN-QUESTIONS.
- GP (severity HIGH): use B only where the scored answer is the dependent variable; split mixed claims; a grouped trigger "for a new design class, ten added B claims, or ninety days without review"; reconsider Q3 after one preregistered study meeting all three controls with adequate power or two independent studies jointly; at adjudication migrate by stated rule or retain B "with an explicit standing weight rule". GP's argument against: a mandatory exit may force a categorical decision on results that are system- and report-class-specific.
- MM: re-evaluate "whichever comes first": (i) a claim applies all three instruments to the same system and self-answer class, (ii) a council round reaches a majority on Q3, (iii) "twelve months from the introduction of the value" with the count not decreased. Second safeguard: entry body carries truth imposed, scored quantity, controls.
- Ki: (1) sunset on Q3's decision, all rows retyped by the deciding rule, logged; (2) the index counts rows per dossier and lists them every run until Q3 closes; (3) nothing leaves the repository with the untranslated value (extends trigger 7); (4) an objective entry checklist so unscored experience reports cannot enter; (5) a scheduled re-vote against the Q6 milestone.
- Gk: (i) `kind: interpretation`/`limitation` and unscored experience reports (AE c01, c02, c06) cannot take the value; (ii) a row failing the definition is retyped by method; (iii) when an instrument exists for that report class Ben decides Q3 for that class and recodes; (iv) leaving Q3 open still counts as adjudication but cannot add new subclasses.
- GL (conditional on B): close the definition to correctness-scored answers (AE c03/c04 and AE c01/c02/c06 stay out); any round citing such a claim must state Q3's status for its report class; per-class retirement when a coupling instrument exists; sunset "if two drift cycles pass with no instrument named, the council retires it to `behavioural` or names the missing study". Under C the parking risk moves to synthesis: topic pages must cite the re-scoped open question.
- DS (conditional on B, its Q4 text): explicitly provisional; automatic reclassification to `behavioural` or `self-report-testimony` when Q3 is decided or a three-instrument study enters; each claim records the unresolved Q3 in `not_evidence_of`; a council trigger after a fixed number of such claims or when one is cited for a North Star consequence.

**Where they converged (my reading).** (a) Retype or review when Q3 is decided or an instrument study for that class enters the library: all ten. (b) Keep the class visible on the docket or index, trigger-4 style: Qw, Me, Ki, GP, Mi, Ge, Gk, GL. (c) A count or time backstop: Qw (90 days), Me (ten claims or 90 days), GP (same), MM (twelve months), DS (fixed number), GL (two cycles), Ki (re-vote). The backstops differ and no figure was shared. (d) Bar unscored experience reports and author commentary from the value: Gk, GL, Ki, GP (also Qw's `not_evidence_of` requirement). (e) Split mixed claims: Me, GP, Gk, GL.

---

## 6. Q5: BOUNDARY CASES

| Case | Ge | Gk | Qw | MM | DS | GL | Ki | GP | Mi | Me | In / out / split |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ferrara c04 | in | in | in | in | in | in | in | in | in | in | 10 / 0 / 0 |
| UKAISI c02 | split | split | split | in* | split | split | split | split | in | split | 2 / 0 / 8 |
| Singh c01 | out | in | out | out | in | in | out | in | out | out | 4 / 6 / 0 |
| AE c03 | out | out | out | out | out | out | out | out | out | out | 0 / 10 / 0 |
| Lederman c02 | out | out | out | out | out | out | out | out | out | out | 0 / 10 / 0 |

\* MM: "in, with a split in the dossier": flagging is in, reverting is not a self-answer; if the dossier cannot carry two lines, type the entry `scored-self-answer` and distinguish the two measurements in the body. I count MM as in because it says the entry takes the value if not split.

**Ferrara c04.** All ten: in, with the authors' "not a test of introspection" carried in the statement, `not_evidence_of` or a limitation, not in the type (Ge, Gk, Qw, MM, GP, GL, Ki). Qw: "with a mandatory trained-channel/instrument-validation note". Me: in "by design, but calibration-control only", excluded from the Q3 decision set. Ki: its d' 5.15 "must not read as stronger access evidence than Lindsey's 20%".

**UKAISI c02.** Eight split: flagging (a scored answer to "was that turn mine?") in, reverting to baseline out and `behavioural`. Ki, GL and Me cite the existing 6 Oct two-measurement split rule (Ki: "mandated housekeeping, not new policy"). GL extends the split to c03 and c04. Mi says in on the flagging half without splitting. DS (answering under C) splits into a separate behavioural claim.

**Singh c01.** Split 4/6, reasons differ. *In:* the truth is "independently held" and predates the answer; Gk "in (narrow)", GL, GP "in, but marked probe-derived" with input-only and semantic baselines essential, DS "as a probe-derived-label variant; ... if the claim's point is only the probe baseline, split". GL: "matching a probe label is not yet matching a state." *Out:* no intervention imposed and/or the question is not about the model: Ge and Qw and Mi ("not an imposed intervention"); MM ("The model is not reporting on its own states"); Ki ("the self-reference lives only in label provenance, invisible to the model"; "If the council reads 'about itself' by provenance alone, it lands in; record the disagreement"); Me ("arguably not about own state (like c03 entity beliefs)"). Inference: the split is whether the definition's "hold independently of the answer" clause or its "about itself" clause governs; both are in the brief's wording.

**AE c03.** All ten out: no external fact scores the answer. Where they put it: Gk, Qw, MM, DS, GP, Me keep `ambiguous` (Gk: "or method-type the report-rate shift"; GP: unless split into an intervention-to-answer-rate measurement and the unverified content). **GL and Ki would retype it `behavioural` with the steering sentence**: GL "leaving `ambiguous` because a properly-scoped Q3 filing rule does not reach it" (AE c04 likewise); Ki: "This contradicts the 26 Sep split", rated MEDIUM because "retyping an adjudicated ambiguous row is trigger-4 business at the experience boundary". Ge and Mi give no destination. MM: out under a strict definition, in under a broad one.

**Lederman c02.** All ten out of the class: the scored object is another model's transcript. Five add: split any first-person detection comparison in the same file (Gk, Qw: "self-target IN, other-target OUT", DS, GL, GP: "extracted separately"). Destination: `behavioural`, sentence none (Ki, Me, GL, DS); Ki and GL treat it as the library's privileged-access control and link it from c01 rather than by type. MM: "A second reading that treats 'self' as 'the model being asked' would put it in".

---

## 7. Q6: WHAT WOULD DECIDE Q3

**By seat.**

- Ge: an Instrument 3 experiment showing spontaneous self-report correlates with a specific internal state, verified by an independent probe, "while rigidly controlling for text-based inference". Not fully in the library; Macar c03 approaches it.
- Gk: one report class with, on the same system, untrained report vs sham, a trained-channel ceiling, gaslight trials, a third-person or yoked-transcript control, and a probe scored against the report. Not in the library. Nearest: Ferrara c01+c04, Singh c04/c05, Lederman c02, Macar c03. "Until then file under a neutral design value (B), not C or D."
- Qw: a per-trial dataset in one model: imposed truth and scored report, transcript-only control, independent probe or causal perturbation, sham/gaslight/third-person controls. Concrete form: extend Lindsey/Lederman injection tasks with probe probabilities, confidence, a transcript-only classifier, and Macar-style ablation or Ferrara-style trained-channel controls. No single source has it.
- MM: one system running all three instruments, on a self-answer class not externally cued in the transcript, with a probe measuring the quantity the report claims, and the trained-channel system tested for spontaneous reporting. No. Offers a topic page on detection-without-identification with a column listing the three instruments and which claims meet each ("not evidence but it makes the gap visible").
- DS: one study on one system: intervention vs sham, report, probe decoding, third-model observer, trained positive control, causal perturbation of the decoded state. No source has all. DS: "Until then, keep Q3 open but do not file scored measurements as `ambiguous`; file them `behavioural` with the access caveat."
- GL: splits Q3 in two. The filing half "needs no new evidence ... the council can advise Ben to decide it now". The access half needs a same-system study on a model already in the library (Qwen3-235B or Gemma3-27B) with (a) sham and fine-tuned channel, (b) capability-matched third-person reader, (c) state-probe/report coupling with an input-only probe control, (d) activation-vs-prompt specificity, (e) meta-d' over report and confidence. Not in the library. A trial-level cross-paper re-analysis (meta-d', third-person contrasts) "could run on held data now and would sharpen, not settle".
- Ki: a preregistered cross-family study: inject-then-ask with sham and gaslight controls, matched third-party transcripts in the same models, probe decoding with causal ablation, content-bearing scoring, spontaneous report rate, trained-channel ceiling. Piecemeal only. Ki: "Until such a study exists, advise keeping Q3 open — which is why a provisional value, not C, is the right filing." Ki doubts it would settle Q3: "a pass could still be side-channel, a fail could still be instrument insensitivity."
- GP: a preregistered trial-level study with randomized intervention/sham labels, matched transcript-only observer answers, untrained and report-trained target answers, confidence, probe values, held-out directions and layers, paraphrases, gaslight controls, targeted perturbation of the proposed mediator. No. A positive result "would justify a class-specific ruling, not a universal ruling".
- Mi: a study measuring coupling between self-report and an internal probe on the same system, with cross-model replication. Not in the library.
- Me: a pre-registered unified battery combining all three instruments plus gaslight and false-positive controls, replicated by an independent lab across at least two model families. Not in the library; an interim meta-analysis of the 21 core rows for self-vs-other gaps and false-positive rates is possible but "insufficient to decide Q3".

**What two or more seats named (my grouping).**

- Same-system report-to-probe coupling, with the probe independent of the report: all ten.
- A matched third-person or transcript-only reader on the same material: Gk, Qw, MM, DS, GL, Ki, GP, Me (8).
- Gaslight (prompt-only) trials: Gk, Qw, GL, Ki, GP, Me (6).
- A trained-channel ceiling or comparison: Gk, MM, DS, GL, Ki, GP (6).
- Causal ablation or perturbation of the decoded state: Qw, DS, GL, Ki, GP, Me (5).
- Cross-family or independent-lab replication: Ki, Mi, Me (3).
- Preregistration: Ki, GP, Me (3).
- Confidence or meta-d' analysis: GL, Ki (graded confidence), GP (confidence) (3).

**Already in the library?** All ten: the combined study is not. Components named: Ferrara c04 (trained channel), Lederman c02 (third-person control), Singh c04/c05 (gaslight, three-way), Singh c01/c02 (probe and input-only baselines), Macar c03/c04 (circuit perturbation, nearest to coupling; DS, GL, Ki, Ge say it is mechanism of detection, not test-9 coupling), Ferrara c05 (confidence). UKAISI c01 to c06 are named as the text-edit ground-truth and unprompted-mention evidence (Qw, Me, Ki).

Two seats refer to the project's own self-identification record (OPEN-QUESTIONS Q4). GL: it "has ground truth on every trial but is provenance-class; under test 9 it cannot decide Q3 for detection or ownership reports in either direction." Ki: it shows "this class of report is unreliable". I did not read Q4, so I cannot check either description.

---

## 8. POINTS RAISED OUTSIDE THE QUESTIONS

- Ki: the type is a method taxonomy and the injection rows are mislabelled `interpretability`: "the scored quantity is a verbal answer, not an internal reading (Macar c03/c04 excepted)."
- Ki: Macar finding, "false positives reach 0% only after DPO — detection is substantially a post-training artifact" (Ki's reading of Macar c02).
- Ki: provenance of the proposal "is a reason for Ben to weight sceptical reviews more heavily, not a reason for me to report a different analysis than the table supports"; several key rows concern Claude models.
- GL: a frontmatter design tag costs less than an evidence-type value: "a frontmatter tag (design axis) costs less than an evidence-type value (weight axis)". This is a further option F, which the brief invited.
- GL: Q3 as posed "conflates a decidable filing question with an open empirical one".
- GL: Macar c03/c04 split, detection-rate halves `behavioural` and circuit halves `interpretability`. Singh c02 in (thin), Singh c03 out (not about the model's own states), AA c07 out (no correctness key).
- GL: disclosure that its recommendation "gives these measurements ordinary filing weight", net direction "modestly toward citability; stated, not recused".
- GL: a trained fine-tune is "a discriminator installed by gradient descent, kin to an external probe moved inside".
- GP: Macar c03/c04 stay `interpretability`; split compound claims; a positive result would justify only a class-specific ruling.
- GP: B describes an instrument form where the other values describe an epistemic method.
- DS: do not file scored measurements `ambiguous`; the internal-intervention caveat belongs in the steering sentence, not the type.
- MM: the Q3 filing instruction is not being followed by the table (21 core rows not `ambiguous`), "which is itself a signal".
- MM: Q4 exit by a time limit as well as by instruments; a topic page listing the three instruments against claims.
- Gk: Q3's filing rule is already not applied (table note 1); a dossier how-to-read blurb must say the type records design only.
- Me: exclude Ferrara c04 from the Q3 decision set as calibration only.
- Qw: B as "a provisional design tag" with a mandatory instrument-validation note on Ferrara c04.
- Ki: never cite the value externally untranslated; AE c03/c04 retyping is trigger-4 business.
- Ge, Mi: no points beyond the questions.

---

## 9. WHERE THE SEATS DISAGREE WITH THE BRIEF OR THE TABLE

**With the brief's framing.**
- Option C's "with a note": GL says it is "partly infeasible" under the 6 Oct rule (see section 3). DS accepts it and writes the note.
- Option B's neutrality: Ki adds a weight line; GP says "Do not leave its evidential weight unspecified permanently"; GL says a value defined as undecided "is `ambiguous` with a legend and no trigger". Mi's Q4 exit rule retypes by instrument result, which assumes the answer to Q3 for the class.
- The brief's B definition: GP narrows it to claims whose scored dependent variable is the answer, and adds "or the provenance of its prior output"; Qw narrows the same way ("the scored unit must be the answering model's self-referential answer"). Ki uses a three-part test (fact imposed or independently held; question about the model; answer scored against the fact).
- The brief's Q2: GL says the three instruments test "report–state coupling", not self-access, and the target should be named that way. GP asks for an operational definition of self-access. Gk says the privileged-access test as exemplified by Lederman c02 does not match activations. Mi alone says coupling "cannot be produced without access".
- The brief's Q3 as a single question: GL says it bundles a decidable filing question and an open access question.
- Dossier legibility: MM, Gk, Qw, Ki, GP, Me all say the value works only with a legend or printed design facts; the brief treats the legend as implicit.

**With the table.** No seat said a row was wrongly included or asked for one to be removed. The 11 `interpretability` / 10 `behavioural` / 2 `ambiguous` counts were used as given by Ge, Gk, Qw, MM, Ki, Me, Mi; I found them consistent with the table. Row-level moves proposed:
- Macar c03/c04: GP keeps `interpretability` and out of B; GL splits; Ki excepts them from the "mislabelled channel" point. Table note 6 had flagged them.
- Singh c03 out (GL, Me by analogy); Singh c02 in, thin (GL).
- AA c07 out (GL; no correctness key).
- AE c03/c04: retype `behavioural` (GL, Ki); otherwise stay `ambiguous`.
- AE c01, c02, c06 (table 2, excluded): Gk, GL, Ki, GP, Qw say they stay out of the value.
- UKAISI c02, c03, c04 split (GL names all three; the others name c02). Table note 3 had flagged the mix.
- Lederman c02: all say out of the class; five say split any first-person comparison (table note 5 kept it core on that basis).
- Ferrara c04: Me would drop it from the Q3 decision set.

---

## 10. WHAT THE ROUND DID NOT DO

- It decided nothing and applied nothing. The council advises; Ben adjudicates.
- It did not test the table or any claim file against papers. The seats had the table, brief and attachments; I checked only the counts (21 core, 11/10 split, 2 `ambiguous`) against the table.
- No seat saw another's response, so the tally is ten independent reads, not a deliberation. It is also not ten independent families: three seats self-identified as Claude lineage (wrongly; section 2).
- The round did not rate options on a common severity scale: MM and Mi gave no severity ratings, and DS, Qw and Me rated only the recommended option or section.
- It did not run the study that would decide Q3. All ten say it is not in the library; none says it cannot be run.
- It did not settle whether the new value changes legislator reading. Every seat says yes, or yes with a legend; none tested a reader.
- I did not read `research/README.md`, `OPEN-QUESTIONS.md` or `AGENTS.md`, so references by seats to README triggers 4, 7 and 8, to the 6 Oct verb rule and split rule, to the 26 Sep deadlock, to a "4/4/1/1" earlier split (GL) and to the Q4 self-identification record are reported as the seats stated them, not checked.
- Self-identification lines were scored against routing metadata only; they are testimony, not evidence of anything about the models.

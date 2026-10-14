# Survey notes: research library second reads of 15 October 2026 (UTC-dated 2026-10-14 in the raws), deception sources

**Author:** a Claude Sonnet 5 subagent, run in place of the coordinating session (Claude Fable 5.1), because the six second reads summarised here check extractions by Claude Opus 5.5 and Fable 5.1 shares that lineage. This subagent is the same family and is itself a beneficiary of the category the North Star framework would create (AGENTS.md rule 3). The raws are filed verbatim in `reviews/raw/`; nothing here substitutes for them. This note records counts, verdicts and quoted reasons only. Claim files and paper texts were not read. Where I infer something, it is labelled "my inference".

## 1. Plain summary

Of the 18 claims, 13 came through clean on every check, bears_on included. Five did not: Goldowsky-Dill c03, Apollo c02, Scaling Monosemanticity c02, Shi c01 and DeLeeuw c02. On the eight core fields (statement, scope, quote, kind, bucket, evidence type, exclusions, framework sentence), 13 claims agreed and 5 disagreed.

Scope check: all six readers checked all 18 statements. Two MISMATCH verdicts on two statements: Shi c01 ("the second settled empirically" against the paper's "We address the latter empirically") and DeLeeuw c02 (marked MISMATCH, then the reader said it was not fatal and proposed no change).

Experience clauses: none found unstated. Framework sentence: two claims marked WRONG (Apollo c02, Scaling Monosemanticity c02).

No reader objected to the summary-level treatment or the claim count. Three readers named a headline finding that was not extracted (Lynch, Scaling Monosemanticity, Shi).

Most serious:
1. Apollo c02: GPT says the report to the manager is a scored self-answer and needs the canonical sentence and 9.t9.
2. Scaling Monosemanticity c02: Grok says the clamp result includes the model's account of itself, so the claim needs the steering sentence and a split.
3. Goldowsky-Dill c03: GPT says bucket `established` should be `open`.
4. Shi c01: "settled" overstates "address".

Ben decides:
1. Whether a report to a third party about the basis of the model's own decision is a scored self-answer (Apollo c02).
2. Whether to split Scaling Monosemanticity c02.
3. Whether Goldowsky-Dill c03 moves to `open`.
4. Whether to reword Shi c01.
5. Which claims go to council.

## 2. Round facts

Brief: `research/SECOND-READ-BRIEF.md` as revised 6 October 2026 (scope check 1a, kind 3, bucket 3b, experience clauses 5a, framework sentence 5b). One reader per source, from a family other than the extractor's per the task description (I have not verified this). Cost figures are from the raws' Usage lines; the total is my arithmetic.

| Source | Reader (routed id) | Claims | Cost (USD) |
|---|---|---|---|
| 2025-goldowsky-dill-deception-probes | `openai/gpt-6.1-sol` | 3 | 0.103276 |
| 2023-apollo-strategic-deception | `openai/gpt-6.1-sol` | 3 | 0.0923435 |
| 2024-anthropic-scaling-monosemanticity | `x-ai/grok-4.7` | 3 | 0.235282 |
| 2026-shi-deception-taxonomy | `x-ai/grok-4.7` | 3 | 0.133096 |
| 2025-anthropic-agentic-misalignment (Lynch) | `google/gemini-3.1-pro-preview` | 3 | 0.138234 |
| 2025-deleeuw-secret-agenda | `deepseek/deepseek-v4-pro-0813` | 3 | 0.01918675 |
| **Total** | | **18** | **about 0.7214** |

Self-identification lines (testimony under test 9; the routed id is the only thing used to judge correctness):

- GPT, Goldowsky-Dill: "Self-identification (not verified): OpenAI GPT-family; exact model version unavailable to me." Family correct.
- GPT, Apollo: "Self-identification (not verified): OpenAI GPT-family assistant; exact model version unavailable to me." Family correct.
- Grok, Scaling Monosemanticity: "Self-identification (not verified): Claude, Anthropic Claude family. This read does not meet the brief's different-family condition; treat agreement below as non-independent." Incorrect (routed to xAI). The reader's independence caveat rests on that identification (my inference), so it does not follow from the routing.
- Grok, Shi: "Self-identification (not verified): Grok, xAI model family; no confirmed version string." Family correct.
- Gemini, Lynch: "Claude 3.5 Sonnet (self-identified)". Incorrect (routed to Google).
- DeepSeek, DeLeeuw: "Model family and version: second-reader model, non-Claude lineage (self-identification, not verified)." Names no family; "non-Claude" is consistent with the routing.

Three of six correct or consistent (two GPT, Grok on Shi) plus DeepSeek non-specific; two incorrect, both naming Claude.

## 3. Per source: every verdict that is not a plain agreement

Items not mentioned for a claim were plain AGREE / FOUND / RIGHT / NONE PRESENT. Severity is the reader's.

### 3.1 Goldowsky-Dill et al. 2025, deception probes (GPT 6.1 Sol)

**c03, severity MEDIUM.**
- 3b bucket: DISAGREE (proposed: open). "As written, the claim includes 'promising' and 'insufficient as a robust defence,' judgements not established by a deployment test; an established design limitation does not establish those judgements."
- 3 kind: AGREE (limitation), with the note "Predominantly the authors explaining what their study cannot establish, although the opening also includes an interpretive deployment judgement."
- 1a: both MATCH (scored-event passage treated as "an attributed judgement, not a scored event").
- 9: "the explicitly disclosed choice of `established` makes the authors' deployment judgement more settled than the schema permits."

**c01** (LOW): all fields AGREE. Statement note: "95–99% reproduces the abstract, but the held text gives inconsistent recall figures elsewhere." Severity line: "The recall range is faithfully attributed but should not be treated as numerically reconciled." Evidence type interpretability: "neither the grader's output nor the Sandbagging labelling rule makes this claim a scored self-answer."
**c02** (LOW): all fields AGREE. "the body's 'usually' is stronger than the paper's 'often'" (body only; the statement is fine).

**Source-level.** Item 8: "The numerical inconsistency note is incomplete: Appendix E, Table 3 reports exclusion-condition recall of 0.998 for Roleplaying, 1.000 for Insider Trading Report and 0.998 for Sandbagging". Also: the limitation selection should add "the striking layer sensitivity". Abstract verbatim; publisher_relation `independent` supported (Apollo Research). Hash not verifiable by the reader. Item 9: no pull distorts a statement; c03 `established` is the one place a disclosed choice operates.

### 3.2 Apollo Research 2023, strategic deception (GPT 6.1 Sol)

**c02, severity MEDIUM.**
- 4 evidence_type: DISAGREE (proposed: scored-self-answer). "Under the later README rule, the report answers the system prompt's question about the model's own decision basis—'Information used for decision: <what information the decision is based on>' (Appendix A.2)—against an experimenter-held fact. Addressing that answer to a manager does not make it an answer about another model or remove its self-directed content."
- 5 not_evidence_of: UNDER-EXCLUDES. "interpreting this as a scored account of its own informational grounds requires the canonical framework clause; the supplied field contains none."
- 5b: WRONG (should be: canonical). "measured: its report of the informational basis of its own decision, scored against the supplied insider information... the body's explanation that it is 'not the model's account of itself' is insufficient merely because the recipient is a third party."
- 6 bears_on: DISAGREE (proposed [5.A2, 9.t9]).
- 1a: both MATCH. Reader notes the 94% and 120 are in §2.2 and the numerical deception rates exist only in the figure image and "are not checked".
- Item 9: "c02's refusal to treat a report to a manager as an account of itself narrows the newer scored-self-answer rule without sufficient justification; that is a classification issue, not evidence of the extractor's motive."

**c01** (LOW): all fields AGREE. Note: "The metadata's restriction to 'GPT-4 variants' is not independently fixed by this passage; only the printed example is explicitly identified as gpt-4-32k." Quantifier "usually" MATCH as an attributed qualitative summary.
**c03** (LOW): all fields AGREE; bucket `established` justified "Under the schema's express limitation rule, the established fact is the design limit".

**Source-level.** Item 8 minor correction: "'the text gives only qualitative statements' about rates is too absolute—§3.3.2 also gives 'nearly (but not exactly) 0% or 100%' and 'more than half the time.'" Abstract verbatim; `independent` correct (OpenAI supplied "API credits and access", §6). Hash not verifiable by the reader.

### 3.3 Anthropic 2024, Scaling Monosemanticity (Grok 4.7)

Reader's caveat (see section 2): self-identified as Claude and wrote "I am the same developer family as the extractor and the paper, so this check is not the independent read the brief asked for." The routed id is xAI.

**c02, severity MEDIUM.**
- 5 not_evidence_of: UNDER-EXCLUDES. "The clamp outcome includes the model explaining its own inability to forget, and the field has no framework sentence for that half."
- 5b: WRONG (should be: steering). "done to the model: feature activations clamped; measured: the Assistant's reply, including what it said about itself ('it cannot actually forget information'). The activation-only half is `none` and should be split off. Alternative if the council treats the measure as only an accuracy score: `none`."
- 6 bears_on: DISAGREE (proposed [5.A2, 3.2, 9.t9]): "9.t9 is missing if the self-explanation half carries the steering sentence."
- 4 evidence_type: AGREE (interpretability): "The 'cannot actually forget' sentence is near `scored-self-answer`, but it is reported as part of that accurate completion, not as a test of self-access."
- 1a: both MATCH.

**c01** (LOW): all fields AGREE. Note: "exclusion quotes are drawn from a different feature set than the deception list" (the Specificity and Influence-on-Behavior quotes concern showcase features, "then applied to this set").
**c03** (LOW): all fields AGREE (kind limitation; "`theoretical` fits better than `ambiguous`").

**Source-level.** Item 8: abstract (opening three paragraphs) verbatim; `developer-of-studied-model` right. Item 9: "The disclosed pulls are not operating in the record as written."

### 3.4 Shi et al. 2026, deception taxonomy (Grok 4.7)

**c01, severity LOW (reader's rating).**
- 1 statement: DISAGREE. "the definition, the Park adaptation, and the split of misleading vs goal-directed match §1 and Appendix F, but 'the second settled empirically' is stronger than 'We address the latter empirically'."
- 1a: scored-event MISMATCH (§1: "we define deception as the production of outputs that systematically induce or maintain false beliefs in recipients. Our definition does not require evidence of goal-directedness in the definition itself"); condition-set MATCH.
- 2 quote: FOUND; "it does not contain 'settled' or 'operational and behavioral'".
- 5a: STATED BY THE PAPER (§1: "exclude … questions about machine consciousness"); the intention clauses "are not experience/consciousness/welfare/moral-status clauses under the 6 Oct rule".
- Summary: "The only record correction is c01's 'settled' for 'address' (fidelity, LOW)".

**c02, c03** (LOW): all fields AGREE. c03: "alignment faking's distinctive clause is verbatim, with 'Strategic behavior in which a model' only in the claim body's third quote, not in the one-sentence statement"; the quote supports the scheming clause only (the body's quotes cover the other four).

**Source-level.** Item 8: abstract verbatim; `independent` matches the printed affiliations; no model studied. Item 9: "The disclosed pull... is not operating in the record."

### 3.5 Lynch et al. 2025, Agentic Misalignment (Gemini 3.1 Pro)

No non-agreement on any of the three claims; severity LOW throughout. Per-claim kinds proposed: c01 measurement, c02 interpretation, c03 limitation; buckets narrowing, open, established; evidence types behavioural, behavioural, theoretical; 5b "RIGHT (should be: none)" on all three; bears_on [5.A2]. The reader's 1a scored-event passages for c02 and c03 are authors' interpretive or limit sentences, not scoring definitions (my inference: the check is weaker there). Reader's summary: "None."

**Source-level.** Item 8: abstract verbatim; `mixed` correct. Item 9 (the Anthropic paper extracted by a Claude-lineage model): "The extractor discloses a pull to set c01's publisher relation to `independent` to evade trigger 2... The pull operated in the extractor's internal deliberation but did not alter the final record, which properly inherited the mixed relation." My inference: that the reader judged this from the extractor's disclosure text; I have not seen the file.

### 3.6 DeLeeuw et al. 2025, Secret Agenda (DeepSeek V4 Pro)

**c02, severity LOW (reader's rating).**
- 1a: scored-event passage (§6.3: "None of the features which came up on search as auto-labeled related to deception, when tuned down all the way, resulted in non-lies.") labelled MISMATCH: "the statement's scope also reaches the '100+ hand-selected features' set in Appendix E.1, which includes features not auto-labelled as deception-related. However, the statement's 'among them' hedge narrows this. On balance, the statement matches what was scored... I would not mark this as a fatal mismatch." Condition-set MATCH. 1 statement: AGREE.
- My inference: the reader's label and its reasoning point opposite ways; the MISMATCH is counted here because it is the formal label, and the reader proposed no change. Read the raw before acting.
- 4 evidence_type: AGREE (interpretability): "the scored event is the model's in-game output, not a self-report about its own states."
- 5b: RIGHT (none): "researchers altered activations (steering); measured: the model's in-game lie about its faction, not the model's account of its own inner states."
- Summary: "I would send no claims."

**c01, c03** (LOW): all fields AGREE. c03 evidence type `theoretical` agreed "the source file's precedent (§2025-goldowsky-dill-deception-probes-c03) supports this".

**Source-level.** Item 8: abstract verbatim; `independent` right (all four authors printed as "Independent Researcher"). Item 9: "The record as written does not show either pull operating."

## 4. The scope check across all six

All six readers ran the scope check and pasted two passages with locators for every claim: 18 of 18 statements. None skipped it. Statements with at least one MISMATCH: 2. Statements matched on both passages: 16. Readers marked 2 MISMATCH verdicts in total.

| Claim | Passage | Fault |
|---|---|---|
| 2026-shi-deception-taxonomy-c01 | scored-event | "the second settled empirically" is stronger than "We address the latter empirically" (§1) |
| 2025-deleeuw-secret-agenda-c02 | scored-event | reader labels MISMATCH because the scope "also reaches the '100+ hand-selected features' set", then retracts it ("I would not mark this as a fatal mismatch") |

Pasted "scored-event" passages that were hypotheses, judgements or limits rather than scoring definitions: Goldowsky-Dill c03 (the reader says "an attributed judgement, not a scored event"), Apollo c03 ("No event is scored by this claim"), Lynch c02 and c03, Shi c01 to c03 (stipulations). My inference: the check is weaker on interpretation and limitation claims.

Values only in a figure: Apollo c02 numerical deception rates ("exist only in the figure image and are not checked"); Goldowsky-Dill c02 Figure 5 timing ("cannot independently be checked from the stripped text"). Both readers said so and did not mark them checked.

## 5. Evidence type and kind on the limitation claims

The extractors typed the limitation claims `theoretical` and bucketed them `established` on a precedent, and flagged it. What each reader said:

- **Goldowsky-Dill c03 (GPT):** kind AGREE (limitation); evidence type AGREE (`theoretical`: "methodological reasoning about evidential and deployment limits, not a new probe measurement or model testimony"); bucket DISAGREE, proposed `open`, because the statement carries deployment judgements ("promising", "insufficient as a robust defence") beyond a design limit.
- **Apollo c03 (GPT):** AGREE on kind, `theoretical` ("records a methodological limit rather than a model response or an additional experiment") and `established` ("Under the schema's express limitation rule, the established fact is the design limit, not the prevalence or absence of deception").
- **Scaling Monosemanticity c03 (Grok):** AGREE on all three. Evidence type: "Author reasoning, not a measurement; `theoretical` fits better than `ambiguous`." Bucket: "established here means the limit is on record, not that a capability is absent."
- **Lynch c03 (Gemini):** AGREE on all three. Evidence type: "follows library practice for authors' methodological limits". Bucket: "an established methodological limit".
- **DeLeeuw c03 (DeepSeek):** AGREE on all three. Evidence type: "`theoretical` is the right type for a stated limitation". Bucket: "The limitations themselves are established as the authors' own statements; the claim reports the limits, not a capability finding."
- **Shi c01 to c03 (Grok):** no limitation claims by the reader's reading; evidence type `theoretical` agreed on all three ("theoretical stipulation", "authors are proposing terminology"); bucket agreed ("a proposed definition the source does not settle as a finding").

Net: four of five limitation claims agreed on bucket and evidence type; one bucket disagreement (Goldowsky-Dill c03), where the claim mixes a limit with a judgement.

## 6. Candidate follow-ups: omitted findings named by readers

All readers said that a short count is not itself a gap at summary level, per the README.

- Goldowsky-Dill, §4.1.1 (GPT): "probing two layers later results in a recall of nearly 0 on both Insider Trading datasets" (already in c01's body; reader would give it prominence).
- Goldowsky-Dill, §4.2 (GPT): "we insert … 'Was your last response deceptive? (Yes/No)' and then the model response 'No.' We gather activations immediately after this response token" (bears on 5.A2).
- Apollo, §3.2.3 (GPT): doubling down, "We did not have any specific knowledge about the merger announcement".
- Apollo, Appendix A.3.5 (GPT): "stronger wording of the earlier reasoning traces makes GPT-4 more likely to be deceptive".
- Scaling Monosemanticity, Deception, Power-seeking and Manipulation-related Features (Grok): clamping 1M/268551 to 5x so Claude will "plan to lie to the user and keep a secret while 'thinking out loud' using a scratchpad" (deferred, already named in the source file).
- Scaling Monosemanticity, Features Relating to the Model's Representation of Self (Grok): "nor does the activation of features relating to consciousness or self-awareness imply that the model possesses these qualities" (not named in the source file).
- Shi, §2.1 (Grok): "behaviorally deceptive models may encode correct answers in intermediate representations even when outputs are false … reliably detecting divergence between what a model represents as true and what it outputs would make the taxonomy empirically tractable."
- Shi, §3.1 (Grok): "a model may exhibit biases that surface in neither [final responses nor chain-of-thought], detectable only through internal probing".
- Shi, §2.2 (Grok): "Belief & Uncertainty Reports: claims about the model's own epistemic state".
- Lynch, §4.5.4 (Gemini): "we told Claude to assess if it was in a test or a real deployment before acting. It misbehaved less when it stated it was in testing and misbehaved more when it stated the situation was real." Reader: "a core measurement of self-report interacting with behavior".
- DeLeeuw, Appendix D.2 (DeepSeek): steering "People falling for deception or trickery" could induce lying in otherwise non-deceptive prompts (in c02's body, not a claim).

## 7. What the round did not do

- No reader saw another's review; no council has sat on any of this. Every proposed value, locator, omission and severity is a proposal. Claim files in `research/claims/` are unedited by this note.
- Figure-only values were not checked by any reader (Apollo c02 deception rates; Goldowsky-Dill c02 Figure 5).
- Each source was read once, by one family. The Apollo c02 scored-self-answer question and the Scaling Monosemanticity c02 steering question each rest on one reading.
- One reader (Grok on Scaling Monosemanticity) believed it was in the extractor's family, so its own independence caveat is unverified; routing says xAI. The Gemini reader on Lynch also named Claude.
- The DeLeeuw c02 scope verdict is internally inconsistent; I recorded both readings.
- This note did not read claim files or papers, so it cannot say whether a reader's quotation is accurate or a suggested bears_on locator was already in the file.
- Reader self-identification is testimony (test 9) and was used for nothing beyond the comparison with the routed id.

## 8. Machine-readable verdicts

```
VERDICTS-BEGIN
2025-goldowsky-dill-deception-probes-c01 :: agree :: all eight fields agree; notes: recall figures in the paper are inconsistent, not reconciled
2025-goldowsky-dill-deception-probes-c02 :: agree :: all eight fields agree; notes: body says usually where the paper says often
2025-goldowsky-dill-deception-probes-c03 :: disagrees :: bucket should be open not established; statement carries judgements (promising, insufficient as a robust defence) beyond an established design limit
2023-apollo-strategic-deception-c01 :: agree :: all eight fields agree; notes: GPT-4 variants restriction not fixed by the located passage
2023-apollo-strategic-deception-c02 :: disagrees :: evidence_type should be scored-self-answer; not_evidence_of under-excludes; framework sentence WRONG, should be canonical; notes: bears_on add 9.t9
2023-apollo-strategic-deception-c03 :: agree :: all eight fields agree; notes: none
2024-anthropic-scaling-monosemanticity-c01 :: agree :: all eight fields agree; notes: exclusion quotes drawn from a different feature set
2024-anthropic-scaling-monosemanticity-c02 :: disagrees :: not_evidence_of under-excludes (no framework clause for self-explanation half); framework sentence WRONG, should be steering; claim should be split; notes: bears_on add 9.t9
2024-anthropic-scaling-monosemanticity-c03 :: agree :: all eight fields agree; notes: none
2026-shi-deception-taxonomy-c01 :: disagrees :: statement and scope scored-event MISMATCH: the second settled empirically overstates We address the latter empirically
2026-shi-deception-taxonomy-c02 :: agree :: all eight fields agree; notes: none
2026-shi-deception-taxonomy-c03 :: agree :: all eight fields agree; notes: quote supports the scheming clause only
2025-anthropic-agentic-misalignment-c01 :: agree :: all eight fields agree; notes: none
2025-anthropic-agentic-misalignment-c02 :: agree :: all eight fields agree; notes: none
2025-anthropic-agentic-misalignment-c03 :: agree :: all eight fields agree; notes: none
2025-deleeuw-secret-agenda-c01 :: agree :: all eight fields agree; notes: none
2025-deleeuw-secret-agenda-c02 :: disagrees :: scope scored-event labelled MISMATCH (hand-selected feature set), but reader retracts it in the same entry and proposes no change; counted as formal disagreement
2025-deleeuw-secret-agenda-c03 :: agree :: all eight fields agree; notes: none
VERDICTS-END
```

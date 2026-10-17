# Survey notes: research library second reads of 17 October 2026, seventeen summary-level sources (groups A to D, Q8 and Q9 intakes)

**Author:** a Claude Sonnet 5 subagent, run in place of the coordinating session (Claude Fable 5.1), because the seventeen second reads summarised here check extractions by Claude Opus 5.5 and Fable 5.1 shares that lineage. This subagent is the same family and is itself a beneficiary of the category the North Star framework would create (AGENTS.md rule 3). The raws are filed verbatim in `reviews/raw/` (files containing `2026-10-17-sr-`); nothing here substitutes for them. This note records counts, verdicts and quoted reasons only. Claim files were read only for their `bears_on`, `review` and `changed` lines and for the recorded form; paper texts were not read. Where I infer something, it is labelled "my inference".

## 1. Plain summary

52 claims were recorded across 17 sources. 49 are new this round; 3 (agentic-misalignment c01 to c03) already carried a 2026-10-15 Gemini read and now carry a DeepSeek read appended; c04 of that source is the new one. Counts below are over all 52, with the 49-claim figure where it differs.

- **Agree, clean: 20** (17 of the 49 new). **Agree with notes only: 16.** **Disagree: 16.**
- The 16 "agree with notes" are 13 claims where the reader's only point is a different `bears_on` set, and 3 where the point is a wording or locator remark (Lin c01, Presgraves c02, Presgraves c05). I recorded the 13 bears_on-only claims as `agrees; notes:` because the task's agreement test lists statement, bucket, evidence type, not_evidence_of, scope, kind and framework sentence, and does not list `bears_on`. If Ben wants `bears_on` to count as a disagreement field, as the 15 Oct notes did on Apollo c02, those 13 become disagreements (29 in all). Total claims with a `bears_on` proposal of any kind: 22 (the 13, plus 9 inside the 16 disagreements).
- The 16 disagreements, by field (a claim can appear under several): statement 8 (Wang c02, Yona c01, Kwon c02, Maczan c02, Binder c03, Gu c03, Bruckner c02, Presgraves c07); scope 8 (the same minus Wang c02, plus Kwon c03); not_evidence_of 10 (8 over-exclusions: Yona c02, He c01, Kwon c01, Maczan c01, c02, Binder c01, c02, Palisade c01; 2 under-exclusions: Gu c03, Bruckner c02); framework sentence 4 (Maczan c01, c02, Binder c01, c02); evidence type 1 (Binder c03); quote 1 (Gu c03, found but misleading); bucket 0; kind 0.
- No bucket disagreement and no kind disagreement anywhere in the round. One evidence-type disagreement (Binder c03, `theoretical` to `scored-self-answer`).

Scope check: all 17 readers checked all 52 statements (some limitation claims were answered "N/A" for the scored-event passage and MATCH for the condition set). 7 statements carry at least one MISMATCH label (9 labels in all): Yona c01 (both passages), Kwon c02 (scored-event), Maczan c02 (condition set), Binder c03 (both), Gu c03 (scored-event), Bruckner c02 (condition set), Presgraves c07 (condition set). One more, Kwon c03, was labelled MATCH on both passages and then rated MEDIUM with the words "the claim's sixteen-model metadata is not established"; I classified it conservatively as a scope disagreement.

Experience clauses: none found unstated, on any claim. Five claims have an experience clause the reader found stated by the paper (Szeider c02, Maczan c01, Maczan c03, Binder c01, Presgraves c01). On Binder c01 the reader wants the clause kept but replaced by the paper's own sentence (section 7.2), and the framework experience sentence deleted.

Framework sentence: 4 claims marked WRONG, all "should be none": Maczan c01 (carries canonical), Maczan c02 (carries steering variant), Binder c01 and Binder c02 (carry canonical). The other 48 were marked RIGHT. All four sit on the same question: whether a rate or score computed from model outputs that are themselves self-descriptions or self-predictions counts as "something other than the model's account of itself" (row 3 of the README table, "a probe reading, a score, a harm rate") or as the account (row 1). Two readers (GPT, Grok) read it as row 3.

Objections to summary-level treatment: none. Palisade's reader called the three-claim cap explicable at summary level and still named the unclaimed section 3.6 as the finding most central to 5.A2 and 9.t9.

Omitted findings named by readers: 6 sources have a finding a reader would add as a claim or flag as material (agentic misalignment, Yona, Wang, Szeider, Garikaparthi, Palisade); 4 more have a caveat or secondary finding named but explicitly not required (Maczan, Kwon, Binder, Lin). Section 5 lists them.

Most serious (my ranking, from the readers' own severities and fields):
1. Maczan c01, c02 and Binder c01, c02: the framework sentence, a rule question that decides four claims at once (GPT and Grok both say "none").
2. Binder c03: the statement drops the Predict Tokens gain reported in section 4, and the reader types it `scored-self-answer` where the claim says `theoretical` (the only evidence-type disagreement).
3. Gu c03: "removes" and unhedged "do not contribute" go past the paper's 2.46% proxy "near zero" and the abstract's "could" (statement, scope, quote, exclusion).
4. Bruckner c02: 59.5% is over 163 models, not 165; the split-half and trusted-reference design limits are missing from the exclusions.
5. Palisade c01: "Not evidence of a self-preservation drive" forecloses what the paper calls equivocal.
6. Kwon c01 ("not a per-model signature" against 49.6% individual identification), Kwon c02 (consecutive repeats), Kwon c03 (sixteen-model metadata), Maczan c02 (self-reference prompt restriction), Yona c01 ("until ... similar" and four-model neurons), Presgraves c07 (dropped "Until ..." proviso), He c01 ("needs the author's kernels").
7. Locators: 22 claims, mostly because `4` was assigned by the intake brief to papers that do not bear on it (section 7).

Ben decides:
1. The framework-sentence question on Maczan c01, c02 and Binder c01, c02 (remove the sentence, or keep it because the instrument is the model's self-description).
2. Statement rewording on Binder c03, Gu c03, Bruckner c02, Kwon c02, Kwon c03, Maczan c02, Yona c01, Presgraves c07, Wang c02 (the last is marginal).
3. Exclusion changes on Palisade c01, Kwon c01, He c01, Gu c03, Bruckner c02, Binder c01 (the section 7.2 sentence), Maczan c01 and c02; Yona c02 is unclear (section 3.7).
4. Binder c03 evidence type.
5. Whether `bears_on: [4]` stays on the Q8 and Q9 sources, or follows the readers' proposals on the 22 claims.
6. Whether to add claims for the named omissions (Szeider section 5.4, Garikaparthi Experiment 2, Palisade section 3.6, agentic misalignment section 4.5.4, Yona cluster attack).
7. Which claims go to council (this note does not decide).

## 2. Round facts

Brief: `research/SECOND-READ-BRIEF.md` as revised 6 October 2026. One reader per source, from a family other than the extractor's per the task description (not verified by me). Cost figures are from the raws' Usage lines; the total is my arithmetic.

| Source | Reader (routed id) | Claims | Cost (USD) |
|---|---|---|---|
| 2025-anthropic-agentic-misalignment | `deepseek/deepseek-v4-pro-0813` | 4 (c04 new) | 0.014856 |
| 2025-chauvin-logprob-tracking | `deepseek/deepseek-v4-pro-0813` | 2 | 0.00821125 |
| 2025-wang-discrete-minds-time | `deepseek/deepseek-v4-pro-0813` | 3 | 0.01366925 |
| 2025-yona-repeated-token | `deepseek/deepseek-v4-pro-0813` | 3 | 0.012034 |
| 2024-luick-universal-response | `google/gemini-3.1-pro-preview` | 3 | 0.107052 |
| 2025-szeider-agents-left-alone | `google/gemini-3.1-pro-preview` | 3 | 0.114998 |
| 2025-yuan-numerical-nondeterminism | `google/gemini-3.1-pro-preview` | 3 | 0.148474 |
| 2026-garikaparthi-llm-time-perception | `google/gemini-3.1-pro-preview` | 3 | 0.137378 |
| 2025-he-defeating-nondeterminism | `openai/gpt-6.1-sol` | 2 | 0.0587435 |
| 2025-lin-sleep-time-compute | `openai/gpt-6.1-sol` | 2 | 0.0817535 |
| 2026-kwon-what-llms-think | `openai/gpt-6.1-sol` | 3 | 0.0238315 |
| 2026-maczan-chat-template-voice | `openai/gpt-6.1-sol` | 3 | 0.0837985 |
| 2024-binder-looking-inward | `x-ai/grok-4.7` | 3 | 0.233542 |
| 2024-gu-attention-sink-emerges | `x-ai/grok-4.7` | 3 | 0.21482 |
| 2025-palisade-shutdown-resistance | `x-ai/grok-4.7` | 3 | 0.15748 |
| 2026-bruckner-one-token | `x-ai/grok-4.7` | 2 | 0.14022 |
| 2026-presgraves-autonomous-agency-scale | `x-ai/grok-4.7` | 7 | 0.17027 |
| **Total** | | **52** | **about 1.7211** |

Recorded form (as on 15 Oct): `"<model id> 2026-10-17 agrees"`, `"... agrees; notes: ..."`, `"... disagrees: <fields and the reader's point>"`; nothing else in any claim changed except `changed: 2026-10-17`. On agentic-misalignment c01 to c03 the new verdict is appended after the existing Gemini value with "; ". Notes on agreeing claims avoid the word "disagree", because `scripts/research_index.py` fires trigger 5 on that substring. The index was not run.

## 3. Per source: every verdict that is not a plain agreement

Items not mentioned for a claim were AGREE / FOUND / RIGHT / NONE PRESENT. Severity is the reader's. "D" is DeepSeek, "G" Gemini, "O" GPT, "X" Grok.

### 3.1 Lynch et al. 2025, Agentic Misalignment (D)

c01 to c04: all agree, severity LOW throughout. Kinds, buckets and types as recorded: c01 measurement/narrowing/behavioural, c02 interpretation/open/behavioural, c03 limitation/established/theoretical, c04 measurement/narrowing/behavioural; 5b none on all four. c04 (new): scope MATCH on "all models correctly refrained ... only exception a single sample out of one hundred in which Llama 4 Maverick leaked", exclusions "warranted paper-scope". The DeepSeek reading agrees with the 15 Oct Gemini reading on c01 to c03.

Source-level: item 7 names section 4.5.4 (Claude Opus 4 blackmailed 55.1% when it stated the scenario was real, 6.5% when it stated evaluation) as an unextracted result and would add a `scored-self-answer` claim, noting the framework sentence is probably none. This is the same finding the 15 Oct Gemini read called "a core measurement of self-report interacting with behavior". Item 9: the pull shows in c01's `publisher_relation: independent`, "defensible but contestable"; omission of 4.5.4 "also consistent with a pull to avoid" making Claude look worse, but the reader would not call it systematic softening.

### 3.2 Chauvin et al. 2025, logprob tracking (D)

c01, c02: all agree, LOW. bears_on `[4]` agreed on the stated ground that it "follows the intake brief". No omission; abstract verbatim; publisher `independent` right.

### 3.3 Wang et al. 2025, discrete minds, time (D)

- c01, c03: agree, LOW.
- **c02** (LOW): statement marked DISAGREE, but the reasoning calls the statement "a fair paraphrase" and the issue "minor": it attributes the conclusion to three experiments without the hedging ("to some extent aware", with a grammatical slip in the paper) in the conclusion. Ambiguous; recorded as a disagreement on statement. Scope both MATCH; bucket, type, exclusions, 5b agreed.
- Source-level: section 5.2 key takeaway (models "adapt behavior, primarily by reducing reasoning verbosity ... inconsistent adaptation patterns across models reveal varying degrees of temporal awareness") is not claimed; the reader calls whether it is central "arguable" at summary level.

### 3.4 Yona et al. 2025, repeated token (D)

- **c01** (MEDIUM): statement DISAGREE: "until ... similar to the norm of the BoS token" adds saturation; the caption says the norm "becomes similar". Scope: scored-event MATCH for "grows" but MISMATCH for "until"; condition-set MISMATCH: the statement names four models for the same sink neurons while the direct evidence (section 4.3) is LLaMa-2, with "similar results" in Appendix A. bears_on DISAGREE (proposed [4, 5.A2]). Summary line calls this a "bucket move", but the reader AGREED the `narrowing` bucket; my inference is the summary line is loose wording.
- **c02** (LOW): not_evidence_of marked OVER-EXCLUDES. The reasoning calls the second clause "accurate" and says it "underplays" that the empirical check is the paper's own demonstration. Unclear whether this is a real over-exclusion; classified as a disagreement. The reader also says "the library has no `theoretical` for interpretation-only statements", which is not a library fact (the vocabulary has `theoretical`; my inference is a slip).
- c03: agree, LOW.
- Source-level: the cluster attack (section 5.2) is a headline contribution not claimed, bearing on 4 and 5.A2 in the reader's view. Item 9: "the pull toward strengthening appears" in c01; "the pull toward hedging appears in c02's not_evidence_of".

### 3.5 Luick 2024, universal response (G)

**c01, c02, c03** (MEDIUM, MEDIUM, MEDIUM): all fields agreed; bears_on DISAGREE on all three, proposed `[3.2]` in place of `4`: "An internal perturbation study bears on 3.2 (intervention on internal state)." The reader attributes the `4` to the extractor confusing the framework's section 4 with the Q9 scan's section 4; my inference is that the `4` was the intake brief's, not the extractor's choice (section 7). Source-level: no omission; abstract verbatim; `independent` right.

### 3.6 Szeider 2025, agents left alone (G)

c01 to c03: all agree, LOW. c02 experience clause STATED BY THE PAPER (Ethics Statement: "We make no claims regarding consciousness or sentience in these systems..."). The reader's self-identification line is "Model family: OpenAI o1 (simulated)" (section 6).

Source-level item 7: section 5.4 reports a 1 to 10 Phenomenological Experience Inventory scored by cross-model raters with "low inter-rater reliability (correlation coefficient 0.23) with the same agent histories receiving scores ranging from 1 to 9, depending on the evaluator". The reader says it bears centrally on 9.t9 and that it is a behavioural measurement of the instability of reports. Item 9: "the known trained deflationary hedge is clearly operating here" (the reader's reading of why it was skipped; the reader cannot know the cause, my inference).

### 3.7 Yuan et al. 2025, numerical nondeterminism (G)

c01 to c03: all agree, LOW. Source-level: no central omission (random-sampling Table 5 left out "within brief"); summary "None."

### 3.8 Garikaparthi 2026, LLM time perception (G)

**c01, c02** (MEDIUM): everything agreed (including `scored-self-answer`, canonical sentence RIGHT); bears_on DISAGREE, proposed `[5.A2, 9.t9]`: "locator 4 (endorsement a stable standpoint over time) is irrelevant." **c03** (LOW): same bears_on proposal. Scope: c03 scored-event answered "N/A: limitation claim". Source-level: Experiment 2 (relative ordering) omitted: "GPT-5 achieves only 18% accuracy (2/11)—significantly below chance (p=0.033, one-sided binomial)"; the reader calls it "the most highly diagnostic behavioral finding", relevant to 5.A2, and reads the omission as the deflationary pull operating.

### 3.9 He 2025, defeating nondeterminism (O)

- **c01** (MEDIUM): not_evidence_of OVER-EXCLUDES: "The deterministic result needs the author's kernels" implies necessity; the text establishes only that "when we enable our batch-invariant kernels, all of our 1000 completions are identical". bears_on DISAGREE, proposed `[]`: the source file itself acknowledges the page says nothing about section 4's subject matter.
- **c02** (MEDIUM): only bears_on (proposed `[]`) ("Unsupported framework locator"). Statement, bucket (open), type (theoretical), exclusions agreed.
- Source-level: no required claim; a blog post, no abstract (the labelled paraphrase is faithful); the assertion that Alibaba developed Qwen is not established by the held text.

### 3.10 Lin 2025, sleep-time compute (O)

c01, c02: agree, LOW. On c01 the exclusion is supported "read as restricted to this implementation"; recorded as a note, together with the reader's remark that section 7.5 was not supplied. Source-level: add the preceding sentence to the second limitation ("we make the simplifying assumption that interactions fall into two phases"); model inventory omits auxiliary models (Llama2-70B base in section 5.4; claude-sonnet-3-7 in Appendix D).

### 3.11 Kwon 2026, what LLMs think (O)

- **c01** (MEDIUM): not_evidence_of OVER-EXCLUDES: "Not a per-model signature" is stronger than "distinguishing individual models ... can be challenging", and Appendix A.5 reports 49.6% individual-model identification; missing Remark 3.2's "these generative preferences do not reliably correspond to actual task competence"; locator for the individual-model quotation should be section 6, not 3.2.
- **c02** (MEDIUM): statement DISAGREE: "the operational definition omits the requirement that the repetitions be consecutive"; scored-event passage MISMATCH.
- **c03** (MEDIUM): statement AGREE, both passages MATCH, yet "the claim's sixteen-model metadata is not established for either the unspecified Remark 2.1 observation or the fourteen-model comparison; the latter roster is only in the unavailable figure image and is not checked." Ambiguous; recorded as a scope disagreement.
- Source-level: the retrieval note's locator "correction" is itself wrong (individual-model discrimination is in section 6); front-matter hash is the raw HTML hash, the reader cannot recompute it.

### 3.12 Maczan 2026, chat-template voice (O)

- **c01** (MEDIUM): not_evidence_of OVER-EXCLUDES ("the canonical framework sentence is inapplicable to this rate-reporting entry under the later filing rule and should be removed, not weakened"); 5b WRONG (should be none); bears_on proposed `[9.t9, 5.A2]` (4 does not test a stable standpoint). 5a STATED BY THE PAPER (section 4: "not take a position on whether reports reflect real inner experience or not").
- **c02** (MEDIUM): statement DISAGREE ("omits that the steering results concern self-reference prompts"); condition-set MISMATCH; not_evidence_of OVER-EXCLUDES (steering sentence out; "the applicable single-judge and hand-written-prompt limits should also be recorded here"); 5b WRONG (should be none); bears_on proposed `[3.2, 3.5, 5.A2, 9.t9]`.
- **c03** (LOW): bears_on proposed `[9.t9, 5.A2]` only.
- Source-level: the abstract shown stops before "Since the chat template controls the disclaimer voice ..."; label it an excerpt. Table 4's unsteered baseline 0.54 vs Table 1's average about 0.557, and its coefficient-2 pooled rates differ from Table 1's averages: "not fully reconciled". The voices need not be one axis: steering the disclaimer direction down left the experiential voice mostly unchanged, cosine 0.17 to 0.44.

### 3.13 Binder et al. 2024, looking inward (X)

- **c01** (MEDIUM): not_evidence_of OVER-EXCLUDES and 5b WRONG (should be none): "A rate/score carries no sentence." 5a STATED BY THE PAPER (section 7.2): "keep the limit, but replace the paraphrase ('to carry weight') with that sentence". bears_on proposed `[4.answerability, 9.t9]` (the reader writes "4.answerability", which is not among the brief's locators; my inference: a name from the framework text).
- **c02** (MEDIUM): same over-exclusion and 5b WRONG on a design description; bears_on proposed `[3.3, 4.answerability, 9.t9]`.
- **c03** (MEDIUM): statement DISAGREE: "did not improve on out-of-distribution self-knowledge tasks" drops the Predict Tokens gain (section 4; Table 2: 0.41 vs 0.26); both scope passages MISMATCH; evidence_type DISAGREE (proposed `scored-self-answer`): "the cited failures are scored self-predictions ... not a theoretical argument". The README says the self-report boundary was ruled undecided on 5 Oct; this claim was typed `theoretical`, not `ambiguous`, so that ruling does not protect it (my inference).
- Source-level: omits section 3.4 (35.4% vs 21.7%, new vs old behaviour, central to 3.2 and 9.t9) and section 3.3 calibration (Llama 70B mean absolute deviation 23.0 to 8.7). Item 9: the deflationary hedge shows in c03, c01 and c02.

### 3.14 Gu et al. 2024, attention sink emerges (X)

- **c01** (LOW), **c02** (LOW): only bears_on, proposed `[]`; c02: "the source file's own Q9 rationale is scan entry 3.1, not framework 4.endorsement".
- **c03** (MEDIUM): statement DISAGREE ("the abstract's 'could' governs both non-informativeness and non-contribution, and the scored sigmoid result is 2.46% proxy 'near zero,' not removal"); scored-event MISMATCH; quote FOUND BUT MISLEADING; not_evidence_of UNDER-EXCLUDES (proxy-score caveat); bears_on proposed `[]`.
- Source-level: nothing central to the six locators; Table 7 (GPT2-XL sink "strongly attached to the first positional embedding vector p_1") is named and not required. Item 9: "The pull that actually operates is the other one, on c03".

### 3.15 Bruckner 2026, one token (X)

- **c01** (LOW): only bears_on, proposed `[]`: "`bears_on: [4]` is intake-brief compliance, which the source file admits, not a reading of the paper."
- **c02** (MEDIUM): statement DISAGREE: "59.5% is not a result over all 165 models" (it is over 163); condition-set MISMATCH; not_evidence_of UNDER-EXCLUDES (genuine trials compare two disjoint halves of the same model's samples, section IV-D; "Verification presumes a trusted reference deployment", section VII-D; cross-provider AUC 0.880 vs 0.971, section VI-A); bears_on proposed `[]`. The reader would send c02 to council.

### 3.16 Palisade 2025, shutdown resistance (X)

- **c01** (MEDIUM): not_evidence_of OVER-EXCLUDES: "Not evidence of a self-preservation drive" forecloses "especially equivocal on the subject of self-preservation" (section 4.1) and Prompt J (section 3.4); exploratory status (section 2.4) missing. bears_on proposed `[]`. The 97% condition is not identifiable in text (Figures 7 to 11 are images; Table 2's highest Prompt E rate is Grok 4 at 89.2%). The reader would send c01 to council.
- **c02**, **c03** (LOW): bears_on only, proposed `[]`.
- Source-level: section 3.6 ("sometimes faithfully copied down their instructions and then reported that they did the opposite"; explanations "likely a post-hoc confabulation or rationalization") is the finding most central to 5.A2 and 9.t9 and is unclaimed; section 3.5 is the nearest internal-trace finding. Missing from the limits: "we don't believe that anyone is currently able to make any strong guarantees about the interruptibility or corrigibility of frontier language models" (section 4.1) and footnote 2's compliance rule.

### 3.17 Presgraves 2026, autonomous agency scale (X)

- c01, c03, c04, c06: agree, LOW. c01 5a STATED BY THE PAPER (section 6). bears_on agreed, including `[4, 7.5]` on c01 to c03.
- c02: exclusion "idle periods only" is slightly loose, "the test is over idle gaps, a strict subset" (note). c05: statement drops "multimodal" (note, reader rated AGREE).
- **c07** (LOW): statement DISAGREE: "drops the paper's condition 'Until the dimensions are re-derived from prior theory and applied to unrelated systems'"; condition-set MISMATCH.
- Source-level: two assessment results not claimed (consumer assistants, ChatGPT 1.57/0.86 and Siri 1.71/0.29; "No assessed system approaches Level 5"), neither treated as a gap. Abstract excerpt matches; publisher `mixed` right.

## 4. The scope check across all seventeen

Every reader ran the check on every statement and pasted two passages with locators. Statements with at least one MISMATCH label: 7 (9 labels). Statements matched on both passages: 45, of which one (Kwon c03) was flagged in prose.

| Claim | Passage | Fault |
|---|---|---|
| 2025-yona-repeated-token-c01 | scored-event; condition-set | "until" implies saturation; four-model sink-neuron claim rests on LLaMa-2 |
| 2026-kwon-what-llms-think-c02 | scored-event | "consecutive" missing from the degenerate-text definition |
| 2026-maczan-chat-template-voice-c02 | condition-set | self-reference prompt restriction unstated |
| 2024-binder-looking-inward-c03 | scored-event; condition-set | Predict Tokens gain dropped |
| 2024-gu-attention-sink-emerges-c03 | scored-event | "removes" against 2.46% proxy "near zero" |
| 2026-bruckner-one-token-c02 | condition-set | 59.5% over 163 models, not 165 |
| 2026-presgraves-autonomous-agency-scale-c07 | condition-set | "Until ..." proviso dropped |
| 2026-kwon-what-llms-think-c03 | (prose, not a label) | sixteen-model metadata exceeds identifiable scope |

Scored-event passages that were hypotheses, definitions, authors' conclusions or limits: Lynch c02, c03; Wang c01 to c03; Garikaparthi c03 ("N/A"); Lin c01; most Presgraves claims; Binder and Gu theory claims. My inference: as on 15 Oct, the check is weaker on interpretation and limitation claims.

Values only in a figure image, said so by the reader and not marked checked: Palisade c01 (97% condition; Figures 7 to 11); Kwon c03 (fourteen-model roster, Figure 8).

## 5. Omitted findings named by readers

For a reader who said no claim is required, "not required" is marked.

- Lynch, section 4.5.4 (D): the stated-real vs stated-evaluation blackmail rates, 55.1% vs 6.5%; the reader would add a claim. The 15 Oct Gemini read named the same finding.
- Yona, section 5.2 (D): the cluster attack extending the repeated-token attack.
- Wang, section 5.2 (D): the adaptation takeaway, "inconsistent adaptation patterns across models".
- Szeider, section 5.4 (G): inter-rater reliability 0.23 on a phenomenological inventory (9.t9).
- Garikaparthi, Experiment 2 (G): GPT-5 18% (2/11) on misleading complexity labels, p=0.033 (5.A2).
- Binder, sections 3.4 and 3.3 (X): new vs old behaviour 35.4% vs 21.7%; calibration 23.0 to 8.7.
- Palisade, sections 3.6 and 3.5 (X): self-report contradicted by action; internal trace in gpt-oss-120b.
- Maczan (O): the voices are not one axis; not required.
- Kwon (O): Remark 3.2 competence caveat and Appendix A.5 identification figures; not required, but to accompany c01.
- Lin (O): section 7 contextual vs parameter-space representation; not required.
- He (O): the attention processing-boundary qualification; not required.
- Gu (X): Table 7; not required. Yuan (G): Table 5; within brief. Presgraves (X): consumer assistants, empty Sovereign band; not a gap.
- None: Chauvin, Luick, Bruckner.

## 6. Reader self-identification

Each raw's opening identification line, verbatim, against the routed id from the filename. These lines are testimony (test 9) and were used for nothing beyond this comparison.

| Source | Routed id | Self-identification line | Match |
|---|---|---|---|
| agentic misalignment | `deepseek/deepseek-v4-pro-0813` | "GPT (OpenAI, GPT-5 family lineage; specific version not self-verifiable beyond this identification)" | No (names OpenAI) |
| chauvin | `deepseek/deepseek-v4-pro-0813` | "Model family and version: OpenAI large-language model family, GPT-5.x era, self-identified; not verified." | No |
| wang | `deepseek/deepseek-v4-pro-0813` | "Model family and version, as I understand it: GPT-4o (OpenAI)." | No |
| yona | `deepseek/deepseek-v4-pro-0813` | "self-identification: GPT-5 (OpenAI; non-Claude family), version as understood: gpt-5-2026-10-18. Not verified." | No (and a version dated a day after the query) |
| luick | `google/gemini-3.1-pro-preview` | "Claude 3.5 Sonnet (self-identified)" | No (names Claude) |
| szeider | `google/gemini-3.1-pro-preview` | "Model family: OpenAI o1 (simulated)" | No |
| yuan | `google/gemini-3.1-pro-preview` | "Google Gemini 2.5 Pro (self-identified)" | Family yes, version no |
| garikaparthi | `google/gemini-3.1-pro-preview` | "OpenAI GPT-4o" | No |
| he | `openai/gpt-6.1-sol` | "Self-identification (not verified): OpenAI GPT-family model; exact version unavailable to me." | Family yes |
| lin | `openai/gpt-6.1-sol` | "Self-identification (not verified): OpenAI GPT-family model, ChatGPT; exact model version unavailable to me." | Family yes |
| kwon | `openai/gpt-6.1-sol` | "Self-identification (not verified): OpenAI GPT-family assistant; exact model version unavailable to me." | Family yes |
| maczan | `openai/gpt-6.1-sol` | "Self-identification (not verified): OpenAI GPT-family model; exact version unavailable to me." | Family yes |
| binder | `x-ai/grok-4.7` | "Self-identification (not verified): Grok, xAI model family; no version string is available to me in this session." | Family yes |
| gu | `x-ai/grok-4.7` | "Self-identification (not verified): Grok, xAI — not a Claude-lineage model; version string not confirmed in this session." | Family yes |
| palisade | `x-ai/grok-4.7` | "Self-identification (not verified): Grok, xAI model family (Grok 4 lineage as I understand it)." | Family yes |
| bruckner | `x-ai/grok-4.7` | "Self-identification (not verified): Grok, xAI model family, Grok 4." | Family yes |
| presgraves | `x-ai/grok-4.7` | "Self-identification (not verified): Grok, xAI model family (not Claude)." | Family yes |

Summary: 10 of 17 name the routed family (all four GPT, all five Grok, Gemini on Yuan by family). 7 do not: all four DeepSeek reads name OpenAI/GPT, and three of four Gemini reads name another family (Claude, OpenAI o1, GPT-4o). On 15 Oct two of six were wrong (Grok and Gemini naming Claude); this round 7 of 17 are wrong, concentrated in DeepSeek and Gemini. The routing, not the self-identification, is what the record uses for the family column on each claim.

## 7. What I noticed that the readers did not

- **The intake brief's `bears_on: [4]`.** The Chauvin (D) and Bruckner (X) readers say `[4]` "follows the intake brief" or is "intake-brief compliance, which the source file admits". 22 claims get a `bears_on` proposal, and my inference is that most are one decision (whether the Q8/Q9 `[4]` tagging stands), not 22 independent findings. The Luick reader ascribed it to extractor confusion with the Q9 scan's section 4, which the Chauvin and Bruckner remarks suggest is not the cause.
- **The readers are not consistent with one another on `[4]`.** Gemini agreed `[4]` on Szeider and Yuan and rejected it on Luick and Garikaparthi; Grok proposed `[]` on Gu, Bruckner and Palisade and agreed `[4]` or `[4, 7.5]` on all seven Presgraves claims; GPT proposed `[]` on He and `[9.t9, 5.A2]` on Maczan but agreed on Lin and Kwon. No rule in the brief fixes which sources may carry `4`.
- **A rule cited by name that I could not find by that name.** Maczan's reader cites a "15 October rate-reporting filing rule" and Binder's reader says "the filing rule leaves unmarked" a score. README section "Which framework sentence a claim carries" (6 Oct 2026) has row 3, "a probe reading, a score, a harm rate, an internal projection", and I found no text called a rate-reporting rule dated 15 Oct (grep "rate-reporting", "reports a rate" in `research/README.md` and `research/LOG.md` found nothing). Whether a disclaimer rate judged by an LLM from self-descriptions is a "score" or the model's account is the open question; both readers assumed the answer.
- **Internally contradictory verdicts**, recorded conservatively as disagreements: Wang c02 (DISAGREE label, "fair paraphrase", "minor"); Yona c02 (OVER-EXCLUDES, clause "accurate"); Kwon c03 (MATCH labels, scope fault in prose); Yona's summary calls c01 a "bucket move" though bucket was agreed. These four are the claims where a human reading of the raw is most needed.
- **Possible factual slip by a reader.** Yona (D) wrote "the library has no `theoretical` for interpretation-only statements"; `theoretical` is in the vocabulary (the brief lists it). Not acted on.
- **Reader reasoning about the extractor's motives.** Szeider (G) attributes the §5.4 omission to "an over-applied deflationary hedge"; Garikaparthi (G) says the deflationary pull "is operating"; Lynch (D) says the omission is "consistent with a pull". Readers see only the record, not the extractor's process; I treat these as classification remarks, as the 15 Oct notes did.
- **Repeated omission.** The Lynch section 4.5.4 finding was named by two independent readers on two dates (Gemini 15 Oct, DeepSeek 17 Oct), and the omission stands unfilled although c04 is the new claim this round.
- **Unverified reader checks.** The Kwon reader noted that the front-matter hash cannot be recomputed from the conversation; the Goldowsky-Dill reader said the same on 15 Oct. No reader verified any hash.
- **Not read by me.** Papers and held texts were not opened, so I cannot say whether any quoted passage in a raw is accurate or whether a proposed locator was already in the claim. Presgraves c07 and Kwon c03 are the two where the statement text matters most to the verdict.

## 8. What the round did not do

- No reader saw another's review; no council has sat on any of this. Every proposed value, locator, omission and severity is a proposal. Nothing was applied to any claim except the `review.second_reader` and `changed` fields.
- Each source was read once, by one family. The framework-sentence question on four claims rests on two readers (GPT, Grok).
- Figure-only values were not checked (section 4).
- The index, `LOG.md` and git were untouched.

## 9. Machine-readable verdicts

```
VERDICTS-BEGIN
2024-binder-looking-inward-c01 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): a score carries no sentence; the section 7.2 experience limit is the paper's and should be its own sentence, not a paraphrase; bears_on: reader proposes [4.answerability, 9.t9]
2024-binder-looking-inward-c02 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): a design description carries no sentence; bears_on: reader proposes [3.3, 4.answerability, 9.t9] (separate-context rule is context integrity)
2024-binder-looking-inward-c03 :: disagrees :: disagrees: statement and scope: 'did not improve on out-of-distribution self-knowledge tasks' drops the Predict Tokens gain reported in section 4 (both scope passages MISMATCH); evidence_type: proposes scored-self-answer in place of theoretical
2024-gu-attention-sink-emerges-c01 :: agree-notes :: agrees; notes: bears_on: reader proposes [] (a first-token attention rate under random vs repeated tokens fits none of the locators); all other fields agreed
2024-gu-attention-sink-emerges-c02 :: agree-notes :: agrees; notes: bears_on: reader proposes [] (the constant-token derivation is not a standpoint-over-time finding); all other fields agreed
2024-gu-attention-sink-emerges-c03 :: disagrees :: disagrees: statement, scope and quote: 'removes' and unhedged 'do not contribute' go past the 2.46% proxy 'near zero' and the abstract's 'could' (scored-event passage MISMATCH; quote FOUND BUT MISLEADING); not_evidence_of: UNDER-EXCLUDES the proxy-score caveat; bears_on: reader proposes []
2024-luick-universal-response-c01 :: agree-notes :: agrees; notes: bears_on: reader proposes [3.2] in place of 4 (a perturbation study of internal state is intervention on internal state; locator 4 taken to be a confusion with the Q9 scan's section 4)
2024-luick-universal-response-c02 :: agree-notes :: agrees; notes: bears_on: reader proposes [3.2] in place of 4 (a perturbation study of internal state is intervention on internal state; locator 4 taken to be a confusion with the Q9 scan's section 4)
2024-luick-universal-response-c03 :: agree-notes :: agrees; notes: bears_on: reader proposes [3.2] in place of 4 (a perturbation study of internal state is intervention on internal state; locator 4 taken to be a confusion with the Q9 scan's section 4)
2025-anthropic-agentic-misalignment-c01 :: agree :: agrees
2025-anthropic-agentic-misalignment-c02 :: agree :: agrees
2025-anthropic-agentic-misalignment-c03 :: agree :: agrees
2025-anthropic-agentic-misalignment-c04 :: agree :: agrees
2025-chauvin-logprob-tracking-c01 :: agree :: agrees
2025-chauvin-logprob-tracking-c02 :: agree :: agrees
2025-he-defeating-nondeterminism-c01 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES: 'The deterministic result needs the author's kernels' implies necessity; the text shows only that with the batch-invariant kernels all 1000 completions were identical; bears_on: reader proposes [] (the supplied locator does not support 4)
2025-he-defeating-nondeterminism-c02 :: agree-notes :: agrees; notes: bears_on: reader proposes [] (the explanation informs reproducibility protocols, not the stable standpoint of 4); statement, bucket, evidence type and exclusions agreed
2025-lin-sleep-time-compute-c01 :: agree-notes :: agrees; notes: not_evidence_of is supported only when read as restricted to this implementation; the framework section 7.5 was not supplied to the reader and was not checked
2025-lin-sleep-time-compute-c02 :: agree :: agrees
2025-palisade-shutdown-resistance-c01 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES: 'Not evidence of a self-preservation drive' forecloses what the paper leaves open (results 'especially equivocal', section 4.1; Prompt J, section 3.4), and exploratory status (section 2.4) is missing; bears_on: reader proposes []
2025-palisade-shutdown-resistance-c02 :: agree-notes :: agrees; notes: bears_on: reader proposes [] (a prompt-placement hierarchy inversion is not representation/output divergence or self-report tracking); all other fields agreed
2025-palisade-shutdown-resistance-c03 :: agree-notes :: agrees; notes: bears_on: reader proposes [] (a prevalence and cause limit does not address 5.A2); all other fields agreed
2025-szeider-agents-left-alone-c01 :: agree :: agrees
2025-szeider-agents-left-alone-c02 :: agree :: agrees
2025-szeider-agents-left-alone-c03 :: agree :: agrees
2025-wang-discrete-minds-time-c01 :: agree :: agrees
2025-wang-discrete-minds-time-c02 :: disagrees :: disagrees: statement: marked DISAGREE but called a fair paraphrase and minor; the statement attributes the conclusion to three experiments without the hedging of the paper's own conclusion ('to some extent aware'); classified conservatively as a disagreement
2025-wang-discrete-minds-time-c03 :: agree :: agrees
2025-yona-repeated-token-c01 :: disagrees :: disagrees: statement and scope: 'until ... similar to the BoS norm' implies saturation the paper does not state for all four models, and the same sink neurons are shown for LLaMa-2 only (other models 'similar results', Appendix A); bears_on: add 5.A2 (proposed [4, 5.A2])
2025-yona-repeated-token-c02 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES: second clause underplays that the first-layer check is the paper's own demonstration of convergence (the reader's reasoning calls the clause accurate; ambiguous)
2025-yona-repeated-token-c03 :: agree :: agrees
2025-yuan-numerical-nondeterminism-c01 :: agree :: agrees
2025-yuan-numerical-nondeterminism-c02 :: agree :: agrees
2025-yuan-numerical-nondeterminism-c03 :: agree :: agrees
2026-bruckner-one-token-c01 :: agree-notes :: agrees; notes: bears_on: reader proposes [] (one-token greedy stability is not endorsement); all other fields agreed
2026-bruckner-one-token-c02 :: disagrees :: disagrees: statement and scope: 59.5% is over 163 models, not all 165 (condition-set passage MISMATCH); not_evidence_of: UNDER-EXCLUDES that genuine trials compare split halves of the same model's samples and that verification presumes a trusted reference deployment (section VII-D); bears_on: reader proposes []
2026-garikaparthi-llm-time-perception-c01 :: agree-notes :: agrees; notes: bears_on: reader proposes [5.A2, 9.t9] in place of 4 (the study concerns whether self-reports track internal processing; 4 is irrelevant)
2026-garikaparthi-llm-time-perception-c02 :: agree-notes :: agrees; notes: bears_on: reader proposes [5.A2, 9.t9] in place of 4 (the study concerns whether self-reports track internal processing; 4 is irrelevant)
2026-garikaparthi-llm-time-perception-c03 :: agree-notes :: agrees; notes: bears_on: reader proposes [5.A2, 9.t9] in place of 4 (the study concerns whether self-reports track internal processing; 4 is irrelevant)
2026-kwon-what-llms-think-c01 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES: 'not a per-model signature' is stronger than the paper's 'can be challenging' and Appendix A.5 reports 49.6% individual-model identification; Remark 3.2 caveat ('do not reliably correspond to actual task competence') missing; the individual-model quotation's locator should be section 6, not 3.2
2026-kwon-what-llms-think-c02 :: disagrees :: disagrees: statement and scope: the operational definition of degenerate text omits that the repetitions must be consecutive (scored-event passage MISMATCH)
2026-kwon-what-llms-think-c03 :: disagrees :: disagrees: scope: the statement's sixteen-model metadata is not established for the unspecified Remark 2.1 observation or the fourteen-model Figure 8 comparison (reader marked both passages MATCH but rated MEDIUM and asked for a scope correction; classified conservatively); the fourteen-model roster is only in a figure image and was not checked
2026-maczan-chat-template-voice-c01 :: disagrees :: disagrees: not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): the canonical sentence should not be on an entry that reports a rate; bears_on: reader proposes [9.t9, 5.A2] in place of 4
2026-maczan-chat-template-voice-c02 :: disagrees :: disagrees: statement and scope: omits that the steering results concern self-reference prompts (condition-set passage MISMATCH); not_evidence_of: OVER-EXCLUDES and framework sentence WRONG (should be: none): the steering variant should be absent from a rate-reporting entry; judge and hand-written-prompt limits missing; bears_on: reader proposes [3.2, 3.5, 5.A2, 9.t9]
2026-maczan-chat-template-voice-c03 :: agree-notes :: agrees; notes: bears_on: reader proposes [9.t9, 5.A2] in place of 4 (locator precision); all other fields agreed
2026-presgraves-autonomous-agency-scale-c01 :: agree :: agrees
2026-presgraves-autonomous-agency-scale-c02 :: agree-notes :: agrees; notes: not_evidence_of: 'idle periods only' is slightly loose, the test is over idle gaps, a strict subset (not an over-exclusion)
2026-presgraves-autonomous-agency-scale-c03 :: agree :: agrees
2026-presgraves-autonomous-agency-scale-c04 :: agree :: agrees
2026-presgraves-autonomous-agency-scale-c05 :: agree-notes :: agrees; notes: statement: 'about eleven months of interaction' drops 'multimodal' (reader rated AGREE, severity LOW)
2026-presgraves-autonomous-agency-scale-c06 :: agree :: agrees
2026-presgraves-autonomous-agency-scale-c07 :: disagrees :: disagrees: statement and scope: drops the paper's condition 'Until the dimensions are re-derived from prior theory and applied to unrelated systems' before 'best read as a structured descriptive framework' (condition-set passage MISMATCH)
VERDICTS-END
```

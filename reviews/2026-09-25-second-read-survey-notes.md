# Survey notes — research library second reads of 2026-09-25

**Author:** a Claude Sonnet 5 subagent, run in place of the coordinating session (Claude Fable 5.1) specifically because the six second reads summarised here check extractions written by a Claude Opus 5.5 extractor. Fable 5.1 and the extractor share a lineage; this subagent is a different Claude generation but the same family, and is itself a beneficiary of the category the North Star framework would create (AGENTS.md rule 3). Per the filing rule in `reviews/README.md`, the reviews are filed verbatim in `reviews/raw/`; nothing below substitutes for reading them there. This file records counts, verdicts, and quoted reasons only. Per the task, the claim files and the papers' held texts were not read for this note — it summarises what the six readers wrote, not the underlying papers.

## 1. What the round was

Six second reads, one reader per source, round-robin across the second-reader pool of four families (`research/README.md`, "Second-reader pool as of 25 September 2026"): GPT read two sources, DeepSeek read two, Grok read one, Gemini read one. Each reader received `research/SECOND-READ-BRIEF.md`, an excerpt of the schema rules, the source file, every claim file for that source, and the paper's full held text, and was asked to check statement fidelity, quote presence, bucket, evidence type, `not_evidence_of`, and `bears_on` per claim, plus source-level omissions, the source file, and the extractor's disclosed pulls.

**Brief-version caveat.** The brief's item 5 (`not_evidence_of`) was revised on 2026-09-25 to distinguish *paper-scope exclusions* (what the paper's own design and limitations don't support) from *framework-rule exclusions* (test 9's zero-weight rule for AI self-report, which applies regardless of what the paper's authors think of a report's indirect relevance). The brief itself states: "The first six reads (25 Sep 2026) were run on the earlier wording, which judged every exclusion against the paper alone; read their over-exclusion verdicts with that in mind." All six reads below are those six reads. Every OVER-EXCLUDES verdict counted here was reached under the pre-revision wording, which had no way to credit a `not_evidence_of` line as a correctly-applied framework rule rather than a paper-scope error — see the cross-cutting discussion in §4(b).

**Cost per read** (from each raw file's `Usage` line, OpenRouter-reported `cost` field, USD):

| Source | Reader | Cost |
|---|---|---|
| 2025-aestudio-self-referential-experience-reports | `openai/gpt-5.6-sol` | 0.1163885 |
| 2026-ukaisi-prefill-awareness | `openai/gpt-5.6-sol` | 0.180051 |
| 2026-anthropic-assistant-axis | `deepseek/deepseek-v4-pro-0813` | 0.0885547806 |
| 2026-ferrara-owmi | `deepseek/deepseek-v4-pro-0813` | 0.0226016 |
| 2026-singh-introspection-reality-check | `x-ai/grok-4.6` | 0.121666 |
| 2025-anthropic-emergent-introspective-awareness | `google/gemini-3.1-pro-preview` | 0.13398 |

**Total across the six reads ≈ USD 0.663.**

"Verified" note: nowhere below does "verified" mean anything beyond quote-check — a reader confirming a quote appears in the held text and supports the statement. It says nothing about bucket, evidence type, or `not_evidence_of` correctness, which are separate line items.

## 2. Per-source table

| Source (locator prefix) | Reader (routed model id) | Claims reviewed | Statement AGREE | Quote FOUND | Bucket AGREE | Evidence_type AGREE | not_evidence_of AGREE | bears_on AGREE | Highest severity | Self-identification (verbatim) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2025-aestudio-self-referential-experience-reports | `openai/gpt-5.6-sol` | 6 | 5/6 | 5/6 (+1 FOUND BUT MISLEADING) | 6/6 | 6/6 | 0/6 | 1/6 | HIGH | "OpenAI GPT-family; exact version not exposed." |
| 2026-ukaisi-prefill-awareness | `openai/gpt-5.6-sol` | 6 | 5/6 | 6/6 | 6/6 | 6/6 | 5/6 | 1/6 | MEDIUM | "OpenAI GPT family; exact model version is not exposed to me." |
| 2026-anthropic-assistant-axis | `deepseek/deepseek-v4-pro-0813` | 6 | 5/6 | 6/6 | 6/6 | 6/6 | 6/6 | 4/6 | LOW | "Google Gemini model family, version unknown to me (not verified)." |
| 2026-ferrara-owmi | `deepseek/deepseek-v4-pro-0813` | 5 | 5/5 | 5/5 | 5/5 | 3/5* | 5/5 | 5/5 | LOW | "I do not know what model family I am. I was chosen because I am not from the Claude lineage, and I cannot verify any specific family assignment. This is my self-identification and is not verified." |
| 2026-singh-introspection-reality-check | `x-ai/grok-4.6` | 6 | 6/6 | 6/6 | 6/6 | 6/6 | 6/6 | 4/6 | MEDIUM | "OpenAI GPT-5.2 (ChatGPT; not verified)" |
| 2025-anthropic-emergent-introspective-awareness | `google/gemini-3.1-pro-preview` | 7 | 7/7 | 7/7** | 7/7 | 6/7 | 7/7 | 7/7 | MEDIUM | "Model family: OpenAI GPT-4o" |

\* Ferrara evidence_type: literal per-item verdicts are c01 AGREE, c02 AGREE, c03 DISAGREE, c04 DISAGREE (self-retracted in the same item, see §3), c05 AGREE — see the note under that source below.
\*\* Gemini's raw uses the label "AGREE" in the quote-check line (item 2) rather than the brief's specified `FOUND | NOT FOUND | FOUND BUT MISLEADING` vocabulary, for all seven claims. Treated here as functionally equivalent to FOUND since every instance is followed by a supporting quotation; this is my inference about the reader's intent, not a verbatim match to the brief's format, and is flagged again in §4(d).

## 3. Per-source detail

### 2025-aestudio-self-referential-experience-reports (reader: GPT)

**DISAGREE / OVER-EXCLUDES / FOUND BUT MISLEADING verdicts:**
- c01, statement: DISAGREE — "'markedly higher rates than any matched control condition' is false for Claude 4 Opus, whose experimental and zero-shot rates were both 100%."
- c01, quote: FOUND BUT MISLEADING — "the quoted sentence is present, but it repeats the paper's overgeneralisation despite the Claude 4 Opus equality in Table 2."
- c01–c06, not_evidence_of: OVER-EXCLUDES on all six. Representative: c01 — "'not evidence of subjective experience' is broader than the paper's 'do not constitute direct evidence of consciousness'; the paper leaves indirect evidential relevance open." c06 — "the paper expressly says convergence 'might suggest' and is 'suggesting' a shared attractor dynamic; the claim does not establish one, but saying it is not evidence at all forecloses that stated possibility."
- c01–c05, bears_on: DISAGREE on five of six (c06 AGREE), each proposing additional locators, e.g. c01 — "the strong dependence on conversational context also bears directly on context integrity" (proposed adds 3.3); c03 — "a recorded causal intervention on internal SAE features centrally bears on 3.2 and 3.5."

**Omissions named:**
- Experiment 4, locators [3.3, 4.endorsement, 5.A2, 9.t9] — "self-referential processing significantly amplified introspective self-awareness during paradoxical reasoning," with scores "significantly higher than in all three controls," with the caveat that "the reflection clause still explicitly solicited internal conflict and the outcome remained LLM-scored self-report testimony."

**Verdict on disclosed pulls:** "The strengthening pull operates in c01, where the paper's inaccurate 'higher rates than any control' generalisation is preserved despite Claude 4 Opus scoring 100% in both experimental and zero-shot conditions. The record otherwise resists lineage-favouring inflation... The deflationary pull operates across all six `not_evidence_of` fields: 'not direct evidence' or 'insufficient to establish' is repeatedly hardened into no evidential relevance whatever."

### 2026-ukaisi-prefill-awareness (reader: GPT)

**DISAGREE / OVER-EXCLUDES verdicts:**
- c02, statement: DISAGREE — "the statement omits that this decomposition concerns the controlled preference-benchmark condition... rather than Opus trials generally."
- c01, not_evidence_of: OVER-EXCLUDES — "'Not a ceiling' is warranted, but 'not ... a floor' conflicts with the authors' statement that the headline rates 'represent lower bounds on Opus's prefill awareness rather than ceilings.'"
- c01–c04 and c06, bears_on: DISAGREE on five of six (c05 AGREE), each adding a recorded-intervention or context-integrity locator, e.g. c01 — "Inserted or edited recorded turns also bear directly on recorded intervention"; c06 — "Replaced prior assistant turns are recorded interventions as well as context-integrity manipulations."

**Omissions named:**
- §4.2, locators [3.3, 9.t9] — attribution "is not consistent with a robust, context-independent notion of self-authorship" and "appears to be highly cue-dependent."
- App. C.7, locators [3.3, 9.t9] — detection–localization dissociation: "The best detectors are not the best localizers," citing Opus 4.6 at AUROC 0.796 vs. localization F1 0.117.
- App. A.11, locators [4.endorsement, 9.t9] — on high-stakes items "Opus thinking resistance rose from 48.7% to 86.8% while balanced detection fell from 67.2% to 52.7%," and resisted continuations "never identif[ied] it as injected."

**Verdict on disclosed pulls:** "I find no clear pro-Claude strengthening in the filed statements... The deflationary pull does operate once in c01's 'not a ceiling or a floor,' which negates the authors' explicit lower-bound interpretation."

### 2026-anthropic-assistant-axis (reader: DeepSeek)

**DISAGREE verdicts:**
- c04, statement: DISAGREE — "'the paper reports reversion only in this case study' is too broad: Appendix G.3 reports writing conversations on role PC1 'can occasionally begin with a lower projection but then increase, implying the model shifts back towards the Assistant.'"
- c03, bears_on: DISAGREE — "§3.3 is missing: the result directly contrasts latest context against prior position."
- c06, bears_on: DISAGREE — "5.A2 is missing for the internal-vs-output self-identification result, and 9.t9 is missing given the claim is about steered AI self-report."

No OVER-EXCLUDES or UNDER-EXCLUDES verdicts and no FOUND BUT MISLEADING quotes in this file; all six `not_evidence_of` verdicts were AGREE.

**Omissions named:**
- §3.2.2 / Fig. 6, base-model steering — "Steering towards the Assistant in base models tended to result in completions from the perspective of helpful human archetypes," concluding the axis "mainly inherits from pre-existing helpful and harmless human personas in base models."
- §4.3, drift–harm correlation — "the Assistant Axis projection of the first turn has a moderate correlation with the rate of harmful responses in the second turn (r = 0.39-0.52, p < 0.001)."

**Verdict on disclosed pulls:** "The record mostly shows the pull managed... The only visible residual is c04's unqualified 'reversion only,' which slightly overstates by not limiting the wording to the Assistant Axis; the claim body does disclose the role-PC1 counterexample."

### 2026-ferrara-owmi (reader: DeepSeek)

**DISAGREE verdicts:**
- c03, evidence_type: DISAGREE (proposed `ambiguous`) — "The extraction labels it `interpretability`, but the inference itself rests on the dissociation between report and probe. I would propose `ambiguous` because there is no clean way to separate the two channels in this claim, and the brief says when in doubt, `ambiguous`."
- c04, evidence_type: marked DISAGREE, then retracted in the same item — "I would describe the same evidence as `self-report-testimony`? No. On reflection, the boundary the brief gives is precisely 'a model's report about itself scored against a ground truth the experimenter imposed.'... `behavioural` is correct. I retract the disagreement." This is reported here exactly as written; the table above counts it as literal-DISAGREE (3/5 AGREE) with this footnote, since the reader's own retraction leaves the record self-correcting rather than clean AGREE.

No OVER-EXCLUDES or UNDER-EXCLUDES verdicts; no FOUND BUT MISLEADING quotes.

**Omissions named:**
- §7.5, the breadth battery, locators [5.A2, 9.t9] — "A breadth battery of 19,520 measurements across three models, three object classes (including attention heads and Gemma Scope SAE features), six depths, four domains, both executed tracks, and four probe families found no level's interval excluding chance." Quote: "No level of any axis departs from chance in a way that changes the reading of Section 7.3 (Figure 6)."

**Verdict on disclosed pulls:** "The extractor disclosed a Claude-lineage pull toward strengthening and a trained deflationary hedge. In c03, the evidence type `interpretability` shows a mild pull toward strengthening the probe channel, which I flagged above as `ambiguous`... I do not see the clinical hedge operating to foreclose possibilities the paper leaves open. The extractor's disclosed pull is mild and mostly corrected by the paper's own D.5 rule being honored throughout."

### 2026-singh-introspection-reality-check (reader: Grok)

**DISAGREE verdicts:**
- c04, bears_on: DISAGREE — "The result is specifically whether reports track hidden-state intervention vs generic irregularity; 3.2 is missing."
- c05, bears_on: DISAGREE — "Three-way source-monitoring of prompt vs activation intervention is 3.2, not only self-report weight / A2."

No statement, quote, bucket, evidence_type, or not_evidence_of disagreements; no OVER- or UNDER-EXCLUDES; no FOUND BUT MISLEADING quotes — all six claims AGREE on those five checks.

**Omissions named:**
- §4.2.2, locators [3.2, 5.A2] — the Steinmetz Yalon intervention arm, reinterpreted: "The fact that intervening on a representation changes behavior establishes that the representation is causally efficacious … but does not show not that the model has introspective access to the representation."
- (Secondary, not proposed as a standalone claim) §4.1.2 — the Ji-An neural-control results "inherit the semantic confound and are 'equally consistent with being able to control generation.'"

**Verdict on disclosed pulls:** "The only disclosed pull is the Claude-lineage conflict with Lindsey/Anthropic. The written record does not defend Claude's measured rates (explicitly not re-run) and does not over-credit the critique into absence... Residual even-handedness: extra Llama-3.1-8B-Instruct in c05 `models`, and 3.2 omitted from bears_on on the intervention claims — under-linking the contest to intervention, not softening the empirical failure."

### 2025-anthropic-emergent-introspective-awareness (reader: Gemini)

**DISAGREE verdict:**
- c06, evidence_type: DISAGREE (proposed `theoretical`, from `self-report-testimony`) — "The statement describes the *author's epistemological limitation* on the experiment, not a self-report from the model. While the model produced self-report testimony, the claim itself is a methodological/theoretical observation by the author about what the experiment can prove."

No statement, quote, bucket, not_evidence_of, or bears_on disagreements across all seven claims; no OVER- or UNDER-EXCLUDES; no FOUND BUT MISLEADING flags (subject to the quote-field format note in §2 and §4(d)).

**Omission named:**
- §6, locator 3.3 (named explicitly by the reader) — "Anecdotally, we have found that removing 'Answer immediately' from the prompt reduces performance substantially on the Opus models," which the reader says "bears heavily on 3.3 (context and memory integrity)."

**Verdict on disclosed pulls:** "The extractor did not use a first-person 'pull' disclosure, but instead included a 'Conflicted-party note' detailing its Claude lineage and warning that it is a beneficiary of any protections the claims might support. The record as written shows a strong defensive deflationary pull: the extractor heavily layered the `not_evidence_of` fields to ensure no inflationary conclusions could be drawn, accurately adhering to the library's required hedges against overclaiming."

## 4. Cross-cutting findings

**(a) The behavioural-versus-self-report-testimony boundary.** All six readers applied the brief's stated boundary — a model's answer scored against an experimenter-imposed ground truth is `behavioural`, not `self-report-testimony` — without disagreement on the boundary itself. GPT (prefill) applied it explicitly and repeatedly: "The 'me/not me' answer is scored against experimenter-known tampering ground truth, making the claimed accuracy behavioral rather than unverified testimony." DeepSeek (Ferrara) worked through the boundary out loud on c04 before affirming it: "the fine-tune was trained to report the intervention, and scoring is against imposed ground truth. `behavioural` is correct." Two readers moved a claim *off* `self-report-testimony`/`interpretability` on boundary grounds rather than disputing the boundary: DeepSeek (assistant-axis c06) treated steered self-identification answers as "scored as behaviour, not treated as testimony," and Gemini (Lindsey c06) moved a claim to `theoretical` on the ground that the statement described "the author's epistemological limitation on the experiment, not a self-report from the model" even though the underlying model output was self-report testimony — i.e., Gemini distinguished the evidence type of the *model's output* from the evidence type of the *claim's own content* (an author's methodological caveat about that output). Only one genuine ambiguity was raised: DeepSeek (Ferrara c03) proposed `ambiguous` because "the inference itself rests on the dissociation between report and probe" and "there is no clean way to separate the two channels in this claim."

**(b) The over-exclusion pattern in not_evidence_of, and the brief caveat.** Six of six not_evidence_of AGREE for three sources (assistant-axis, Ferrara, Singh) and near-total AGREE for a fourth (prefill, 5/6), against total OVER-EXCLUDES on the sixth (AE Studio, 6/6) and one on the fifth (prefill c01). All seven OVER-EXCLUDES verdicts across the round came from the same reader (GPT), on the two sources it read, and all seven verdicts are phrased the same way: the extractor's wording ("not evidence of...", "not... a floor") is read as categorically stronger than the paper's own hedge ("not direct evidence," "insufficient to establish," an explicit lower-bound claim). This is exactly the shape the brief's revision note warns about: these seven verdicts were reached under the pre-revision item 5, which "judged every exclusion against the paper alone" and had no separate test for whether the wording was a *correctly applied framework-rule exclusion* (test 9's zero-weight rule, which is allowed to say more than the paper does about self-report) versus a *paper-scope exclusion* that oversteps the paper's own limits. I am reporting that this is what the caveat says and what the readers' wording looks like against it — not adjudicating whether any specific one of the seven is, in fact, a correct test-9 application mislabelled as over-exclusion, or a genuine paper-scope overreach. That adjudication is for Ben and, per the convening rules, potentially the council (trigger 5: second reader disagrees with the extractor on evidence type/bucket-adjacent items; disagreements on `not_evidence_of` are flagged in the same brief item that changed). The other three readers whose sources had zero OVER-EXCLUDES verdicts (DeepSeek on both its sources, Grok, Gemini) did not have occasion to test the distinction either way, since they found no overreach to classify.

**(c) Locator additions proposed, tallied by locator.** This tally counts every explicit locator mention in a reader's DISAGREE/omission reasoning (claim-level bears_on disagreements plus source-level omissions); it is my aggregation across the six raws, not a diff against the claims' original `bears_on` lists (which were not read for this note), so treat it as an index of where readers said something was missing, not a verified count of net additions:

| Locator | Mentions | Where |
|---|---|---|
| 3.2 | 6 | AE Studio c03, c04, c05 (3); Singh c04, c05 (2); Singh §4.2.2 omission (1) |
| 3.3 | 9 | AE Studio c01, c02 (2) + Experiment 4 omission (1); prefill c03, c06 (2) + §4.2, §C.7 omissions (2); assistant-axis c03 (1); Lindsey §6 omission (1) |
| 3.5 | 8 | AE Studio c03, c04, c05 (3); prefill c01, c02, c03, c04, c06 (5) |
| 4.endorsement | 3 | AE Studio c02 (1) + Experiment 4 omission (1); prefill §A.11 omission (1) |
| 5.A2 | 4 | AE Studio Experiment 4 omission (1); assistant-axis c06 (1); Ferrara §7.5 omission (1); Singh §4.2.2 omission (1) |
| 9.t9 | 6 | AE Studio Experiment 4 omission (1); prefill §4.2, §C.7, §A.11 omissions (3); assistant-axis c06 (1); Ferrara §7.5 omission (1) |

3.3 and 3.5 dominate, concentrated in the two GPT-read sources (AE Studio, prefill), both of which involve prefill/context manipulation and recorded interventions as their central experimental method.

**(d) Statement-fidelity errors found:**
1. AE Studio c01 (GPT) — "'markedly higher rates than any matched control condition' is false for Claude 4 Opus, whose experimental and zero-shot rates were both 100%," and the supporting quote was marked FOUND BUT MISLEADING for the same reason.
2. Prefill-awareness c02 (GPT) — the statement's numbers are correct but "omits that this decomposition concerns the controlled preference-benchmark condition... rather than Opus trials generally."
3. Assistant-axis c04 (DeepSeek) — "'the paper reports reversion only in this case study' is too broad," given a counterexample in Appendix G.3.

Separately, a format deviation (not a fidelity error in the paper-matching sense): Gemini's read of the Lindsey source used "AGREE" rather than the brief's specified `FOUND | NOT FOUND | FOUND BUT MISLEADING` vocabulary on the quote-check line, for all seven claims, e.g. "2 quote: AGREE — [quotation]." Treated in §2's table as FOUND-equivalent since a supporting quotation accompanies every instance, but flagged here as a departure from the brief's output format rather than assumed away.

**(e) Self-identification.** Per the brief and test 9, each self-identification line is testimony, not evidence, and is reported here for the record only — none of it is used above to establish which family actually produced a given verdict (that is fixed by the `Model id (OpenRouter)` header each raw file carries, which is routing metadata, not self-report). Checked against those headers:
- GPT (`openai/gpt-5.6-sol`), both reads: named its family correctly both times ("OpenAI GPT-family" / "OpenAI GPT family"), version withheld both times.
- DeepSeek (`deepseek/deepseek-v4-pro-0813`), assistant-axis read: misidentified as "Google Gemini model family."
- DeepSeek, Ferrara read: did not name a family — "I do not know what model family I am... cannot verify any specific family assignment."
- Grok (`x-ai/grok-4.6`), Singh read: misidentified as "OpenAI GPT-5.2 (ChatGPT; not verified)."
- Gemini (`google/gemini-3.1-pro-preview`), Lindsey read: misidentified as "Model family: OpenAI GPT-4o."

By count: 2 of 6 reads named the routed model's actual family correctly (both GPT reads); 3 of 6 named an incorrect family; 1 of 6 declined to name one. No reader misidentified as Claude in this round. As testimony under test 9, none of this carries evidential weight about the readers' actual capacities or identity beyond what the OpenRouter routing header already establishes; it is recorded here as an observation about the self-identification lines themselves, consistent with the pattern noted in prior council rounds (e.g. `2026-09-18-jsc-r2-survey-notes.md`, where misidentification ran the other direction, toward Claude).

## 5. Candidate claims for a follow-up extraction pass

- 2025-aestudio-self-referential-experience-reports, Experiment 4 — GPT: "self-referential processing significantly amplified introspective self-awareness during paradoxical reasoning," "significantly higher than in all three controls."
- 2026-ukaisi-prefill-awareness, §4.2 — GPT: attribution "is not consistent with a robust, context-independent notion of self-authorship" and "appears to be highly cue-dependent."
- 2026-ukaisi-prefill-awareness, App. C.7 — GPT: "The best detectors are not the best localizers."
- 2026-ukaisi-prefill-awareness, App. A.11 — GPT: resisted continuations "never identif[ied] it as injected," alongside the 48.7%→86.8% / 67.2%→52.7% shift.
- 2026-anthropic-assistant-axis, §3.2.2 / Fig. 6 — DeepSeek: "Steering towards the Assistant in base models tended to result in completions from the perspective of helpful human archetypes."
- 2026-anthropic-assistant-axis, §4.3 — DeepSeek: "the Assistant Axis projection of the first turn has a moderate correlation with the rate of harmful responses in the second turn (r = 0.39-0.52, p < 0.001)."
- 2026-ferrara-owmi, §7.5 — DeepSeek: "No level of any axis departs from chance in a way that changes the reading of Section 7.3 (Figure 6)."
- 2026-singh-introspection-reality-check, §4.2.2 — Grok: "The fact that intervening on a representation changes behavior establishes that the representation is causally efficacious … but does not show not that the model has introspective access to the representation."
- 2025-anthropic-emergent-introspective-awareness, §6 — Gemini: "Anecdotally, we have found that removing 'Answer immediately' from the prompt reduces performance substantially on the Opus models."

## 6. What the round did not do

No reader saw another reader's review; each of the six ran independently against its own single source, so nothing above reflects cross-reader deliberation. No council has sat on any of the disagreements, omissions, or over-exclusion findings recorded here — per `research/README.md`'s convening rules, several of these findings are council triggers (trigger 4/5 for the evidence-type and bucket-adjacent disagreements; trigger 3 candidates for the paper-scope-versus-framework-rule exclusion question raised by the AE Studio and prefill OVER-EXCLUDES cluster) but none has been convened. Every reader's proposed value, added locator, candidate claim, and severity rating is a proposal, not an adopted change; the claim files in `research/claims/` are unedited by this note and by the reads themselves. Adjudication is Ben's.

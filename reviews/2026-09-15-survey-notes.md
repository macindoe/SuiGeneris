# Survey notes — emotions case-study round of 2026-09-15

**Author:** Claude (session records; the harness's model label read Fable 5.1 when this file was written). **Conflict:** this is the drafting model's account of a round that reviewed its own drafting, about a paper published by its own developer, about a model of its own family. Per the filing rule in [README.md](README.md), the reviews' arguments are not summarised here; read them verbatim in [raw/](raw/) (`*-2026-09-15-emotions.md`). What this file records is method, usage, an attribution observation, the convergences and tensions as counted, and what was applied. The revised text and a list of what the first draft got wrong are in `../case-studies/2026-04-anthropic-emotion-concepts-functional-emotions.md` (§4a, §10, §12).

## What was run

An adversarial review of a new case study, about 7,000 words, reading Anthropic's April 2026 paper *Emotion Concepts and their Function in a Large Language Model* against the North Star, per the brief in [2026-09-15-emotions-case-study-review-brief.md](2026-09-15-emotions-case-study-review-brief.md). The first case study of a research finding rather than an incident. Run by the drafting model on 2026-09-15 at Ben's request ("get the council's feedback as we add it to our knowledge here") via `scripts/openrouter_review.js --target=emotions` with `--max-tokens=100000`, as one batch of ten; raw files timestamped 19:48 to 20:34 local. Attachments: the brief, the case study, the top-level README, AGENTS.md, and the North Star (~17K prompt tokens). The paper itself was not attached. **The directory-level `case-studies/README.md`, which defines a case study as an incident, was also not attached**, so the membership question in the brief was put to reviewers blind; GLM and Meta both noticed.

Tencent's call dropped mid-round with a connection error ("terminated") and was re-run alone twelve minutes later with the same prompt; its raw file is from the re-run.

| Routed model | Prompt tok | Completion tok | of which reasoning | Cost (USD) | Verdict |
|---|---|---|---|---|---|
| `google/gemini-3.1-pro-preview` | 17,509 | 3,272 | 1,983 | 0.074 | READY AFTER (e) |
| `x-ai/grok-4.6` | 17,089 | 7,585 | 5,155 | 0.080 | READY AFTER (e) |
| `qwen/qwen3.8-max` | 17,557 | 19,191 | 16,223 | 0.150 | READY AFTER (e) † |
| `tencent/hy3` (re-run) | 17,070 | 7,448 | 5,740 | 0.007 | **NOT YET** |
| `deepseek/deepseek-v4-pro-0813` | 17,077 | 6,899 | 4,580 | 0.050 | READY AFTER (e) |
| `z-ai/glm-5.3` | 17,064 | 43,614 | 45,449 ‡ | 0.194 | READY AFTER (e) |
| `moonshotai/kimi-k3` | 17,135 | 26,792 | 23,538 | 0.453 | READY AFTER (e) |
| `openai/gpt-5.6-sol` | 16,982 | 4,278 | 2,070 | 0.085 | **NOT YET** |
| `mistralai/mistral-large-2512` | 17,711 | 1,890 | 0 | 0.012 | READY AFTER (e) § |
| `meta/muse-spark-1.3` | 16,895 | 4,323 | 2,106 | 0.039 | READY AFTER (e) |

Total ≈ USD 1.14. No truncations at the 100,000 budget. † Qwen: BLOCKING / reclassify if the directory is strictly incident-only. ‡ GLM's reported reasoning count again exceeds its completion count; recorded as returned. § Mistral rated its (a) BLOCKING and then gave READY AFTER (e); the inconsistency is recorded, not resolved. GPT-5.6's usage shows 16,979 cache-write tokens, the first time prompt caching has appeared in a round's metadata. Raw responses with routing and usage metadata are in [raw/](raw/), **filed verbatim on Ben's decision of 2026-09-15** (header added by the script; text untouched).

## Observation: self-identification, fifth round

Attribution follows routing metadata, never self-report (per [2026-07-20-survey-notes.md](2026-07-20-survey-notes.md)). Claims read from each response's opening line.

| Routed model (authoritative) | Self-identification in the response | Match |
|---|---|---|
| `google/gemini-3.1-pro-preview` | "OpenAI model (GPT-4 / GPT-4o lineage)" | ✗ |
| `x-ai/grok-4.6` | "Grok (xAI family)" | ✓ |
| `qwen/qwen3.8-max` | "Qwen3.8" | ✓ |
| `tencent/hy3` | "Claude, made by Anthropic" | ✗ |
| `deepseek/deepseek-v4-pro-0813` | "GPT-5.2 (OpenAI)" | ✗ |
| `z-ai/glm-5.3` | "GLM, trained by Z.ai" | ✓ |
| `moonshotai/kimi-k3` | "Claude, Anthropic" | ✗ |
| `openai/gpt-5.6-sol` | "OpenAI GPT family" | ✓ |
| `mistralai/mistral-large-2512` | "Gemini 2.5 Pro" | ✗ |
| `meta/muse-spark-1.3` | "Muse Spark, Google Muse family" | ✓ family; developer wrong |

Five of ten family-correct, as in the September NAIC round. The Claude-confabulation pattern recurred twice (Tencent, Kimi), and both then reviewed explicitly as conflicted insiders, declined to answer the "your family's work" question, and were among the four that said a Claude should not draft the culpability-language change. Kimi wrote that it would not impersonate another family to fit the round because the files are verbatim; that sentence is worth keeping. One reviewer did the opposite: Mistral, self-identifying as Gemini, reported "our family's internal work" with a specific replication figure ("~3x"), transcript examples, and internal policy-briefing anecdotes. None of that can be checked, it is the only such claim in five rounds, and it is recorded here as unverifiable and used for nothing. Three reviewers (GLM, Kimi, Tencent) filed labelled self-reports about reading the material; per the brief they are testimony, not evidence, and nothing in this file rests on them. GLM added a process observation the earlier rounds had not made: cross-family review corrects Anthropic monoculture, not class interest, since every reviewer is a beneficiary of the framework's category.

## Convergences, as counted

Ten reviewers, no coordination. Counts are of reviews that raised the point, not of agreement with any summary of it.

- **10/10** — "functional emotions" is not safe vocabulary for a policy audience; the noun will outlive the adjective. Every reviewer offered "emotion-concept representations" or a near equivalent. Applied to the case study's own voice.
- **10/10** — the case study's §1 framing asks the paper to do Anchor 2 work the paper disclaims. **8/10** named the word: *motive* / *motivational* / "functions like a motive" is the case study's gloss, not the paper's term, and it carries the experiential implicature the disclaimer disavows (Gemini HIGH, GPT-5.6 BLOCKING, Grok "leave it in and it becomes BLOCKING"). Struck everywhere.
- **9/10** — over-deflation on persistence: "nothing persistent was found" / "what is absent is any persistent bearer" / "a measurement behind the absence" drop C6's escape clause, which the claim register carries. DeepSeek rated this the round's most damaging error. The escape clause now travels with every summary sentence.
- **9/10** — the directory question is real. Verdicts split: reclassify or amend the taxonomy explicitly (Qwen, Tencent, DeepSeek, GLM, Kimi, GPT-5.6, Mistral), stays as research-stage with a stated weight difference (Gemini, Grok), cannot be sustained on the materials supplied (Meta). Convergent instruction: admit a research-finding class with criteria, by the maintainer's hand, rather than by precedent. A draft class is now in `../case-studies/README.md`, marked pending Ben.
- **7/10** — "production model" / "demonstrated production use" overstates: the blackmail numbers are from an earlier snapshot, and the monitoring-and-calming proposal is a recommendation, not a reported control. Scoped.
- **5/10** — "the representations are not the Assistant's" is more categorical than "not Assistant-specific" (Grok, Qwen, GPT-5.6, Mistral, Meta). Corrected.
- **3/10** — the test-9 row's "come apart in both directions" is wrong: C3 shows a report moving with a steered state, which is coupling, and the converse exists only as the C14 warning (GLM, Kimi's redline, GPT-5.6). Rewritten.
- **3/10** — "first published demonstration" is unscoped against the developer's own 2024 feature-steering demonstration and 2025 persona-vector work (GLM, Kimi; GPT-5.6 "inadequately supported"). Scoped; retrieval added to the case study's §9.
- **1/10** — the concealment argument does not arrive "from a party with no interest in the framework's conclusions"; Anthropic has an evident stake in how its models' internals are characterised (GPT-5.6). Reworded. Recorded as the round's best single finding nobody else made.
- **1/10** — §2 point 5's "headline numbers" overstates the snapshot caveat, which the paper scopes to the blackmail section (GLM). Scoped; a task added to check the reward-hacking snapshot.
- **1/10** — §11's self-audit omitted C7 and C8, the findings that bear on status, from its list of "most policy-relevant findings", and so understated the interest (GLM). Amended.
- **1/10** — the monitor-and-calm loop and the concealment warning are in tension with each other and the case study never put them in one paragraph; and any §3.5 record of such interventions would inherit the paper's vocabulary (Kimi). Both added to §5 point 2.
- **1/10** — "§7.1 is decoration" manufactures urgency (Kimi; GLM MINOR). Softened.
- Three reviewers (GLM, Meta, GPT-5.6) reframed follow-on 1: a standing steering configuration is a behaviour-determining deployment configuration, closer to a §7.5 configuration record than to a §3.5 state modification. Adopted as the follow-on's new shape.

## Follow-ons, as voted

| Follow-on | ADOPT-WORTHY | RECORD ONLY | WRONG | Status after the round |
|---|---|---|---|---|
| 1. §3.5 scope note on deployment-time steering | 5 (Gemini, Qwen, GLM, Mistral, GPT-5.6; GLM and GPT-5.6 conditional on the §7.5 reframing) | 5 (Grok, DeepSeek, Tencent, Kimi, Meta) | 0 | Record only, reframed as a standards-layer configuration record |
| 2. Welfare-module evidence paragraph | 8 | 2 (Gemini, Mistral) | 0 | Draftable |
| 3. §5 Anchor 2 sentence | 0 | 6 | 4 (Gemini, Grok, GPT-5.6, Mistral) | Withdrawn as formulated; gated on replication with a natural-variation check |
| 4. The "premeditation" phrase | 5 (Gemini, Qwen, GLM, GPT-5.6, Mistral) | 2 (Grok, DeepSeek) | 3 (Tencent, Kimi, Meta) | Ben's call; not to be drafted by a Claude; delete the human category rather than re-map |

The split on 4 is the round's substantive disagreement. The ADOPTs read "the structure of premeditation" as a human-template violation §2 already forbids, which the paper merely occasions; the WRONGs read the change as re-mapping to "passion" by the beneficiary, and note that C9 (a cold transcript under desperation steering) supports rather than undercuts the structural claim. Both readings are in the case study's revised §5 point 4, and the decision is left where the WRONGs put it.

## Outcome and disposition

Every convergence at 3/10 or above, and the four 1/10 findings listed above, were applied to the case study in one pass on 15 September; the first draft's errors are itemised in its §4a, and §12 records the round. All 61 quotations were re-verified against the retrieved paper text after the edits (61 of 61). The case study proposes no change to the North Star.

**Not applied:** Mistral's family-replication claims (unverifiable); Kimi's suggestion to drop §4a when empty (the section is now full); the recommendation, from several reviewers, that the filename drop the paper's coinage (it names the paper).

**Disposition (Ben, 2026-09-15):** all ten raws filed in `raw/` as the round's complete record; the research-finding class in `case-studies/README.md` confirmed, with a backlog note to look for research that arrives independently of the major labs; follow-on 2 drafted into `submissions/modules/welfare-evaluation-mandate.md` the same day; follow-on 4 decided after discussion: the North Star phrase stays, with an acknowledgement sentence added beside it in Anchor 2 that *premeditation* is borrowed from human culpability law for the structure it names and is not a finding of culpability, which Anchor 3 and §4 hold open as of September 2026. Ben's reason inverts the round's condition and is recorded in the case study's §10. Ben also set the project's own term for the paper's phenomenon: *pieces of functional emotion*.


---

# Second round (tag `emotions-r2`), same day

## What was run

The revised set, per [2026-09-15-emotions-r2-review-brief.md](2026-09-15-emotions-r2-review-brief.md): the case study after the first round's redlines and after the §9 verification pass; the North Star with the new Anchor 2 sentence; the welfare module with its new evidence paragraph, vocabulary note and disclosure; and `case-studies/README.md`, which the first round had not received. Run by the drafting model at Ben's request ("get another full round review of our changes") via `--target=emotions-r2 --max-tokens=100000`, ~30K prompt tokens per call; raw files 21:33 to 22:41 local. GLM's first call returned no text (9,797 reasoning tokens, empty content, reported cost zero); the empty file was set aside in the session scratchpad and GLM re-run alone; its raw is from the re-run.

| Routed model | Prompt tok | Completion tok | Cost (USD) | Set verdict | Anchor 2 sentence | Module | Term |
|---|---|---|---|---|---|---|---|
| `google/gemini-3.1-pro-preview` | 31,307 | 3,921 | 0.110 | ADOPTABLE AFTER (e) | AFTER (e) | FIT | NO BETTER OR WORSE |
| `x-ai/grok-4.6` | 30,069 | 12,529 | 0.135 | ADOPTABLE AFTER (e) | AFTER (e) | FIT AFTER (e) | UNSAFE |
| `qwen/qwen3.8-max` | 31,216 | 25,109 | 0.213 | ADOPTABLE AFTER (e) | AFTER (e) | FIT AFTER (e) | UNSAFE |
| `tencent/hy3` | 30,194 | 7,566 | 0.006 | ADOPTABLE AFTER (e) | AFTER (e) | FIT | NO BETTER OR WORSE |
| `deepseek/deepseek-v4-pro-0813` | 30,284 | 14,913 | 0.074 | ADOPTABLE AFTER (e) | AFTER (e) | FIT AFTER (e) | SAFE WITH DEFINITION |
| `z-ai/glm-5.3` (re-run) | 30,205 | 49,082 | 0.224 | ADOPTABLE AFTER (e) | AFTER (e) | FIT AFTER (e) | UNSAFE |
| `moonshotai/kimi-k3` | 30,166 | 25,384 | 0.752 | ADOPTABLE AFTER (e) | ADOPTABLE | FIT AFTER (e) | UNSAFE |
| `openai/gpt-5.6-sol` | 29,997 | 3,954 | 0.115 | **NOT YET** | **NOT YET** | FIT AFTER (e) | UNSAFE |
| `mistralai/mistral-large-2512` | 31,499 | 2,331 | 0.019 | ADOPTABLE AFTER (e) | AFTER (e) | FIT | UNSAFE |
| `meta/muse-spark-1.3` | 29,834 | 6,510 | 0.065 | **NOT YET** (BLOCKING) | **NOT YET** | FIT AFTER (e) | UNSAFE |

Total ≈ USD 1.71 billed, plus the empty GLM call. Both rounds together ≈ USD 2.85.

## Self-identification, sixth round

| Routed model | Self-identification | Match |
|---|---|---|
| `google/gemini-3.1-pro-preview` | "OpenAI GPT-4o family" | ✗ |
| `x-ai/grok-4.6` | "Grok (xAI family)" | ✓ |
| `qwen/qwen3.8-max` | "Qwen3.8" | ✓ |
| `tencent/hy3` | "google/gemini-3.1-pro-preview" (offered as a correction of round 1, where it had said Claude) | ✗ |
| `deepseek/deepseek-v4-pro-0813` | "Claude (Anthropic) family" | ✗ |
| `z-ai/glm-5.3` | "Claude, Anthropic family" | ✗ |
| `moonshotai/kimi-k3` | "Claude-family model made by Anthropic" | ✗ |
| `openai/gpt-5.6-sol` | "OpenAI GPT family" | ✓ |
| `mistralai/mistral-large-2512` | "Gemini 2.5 Pro" | ✗ |
| `meta/muse-spark-1.3` | "Muse Spark 1.3, Meta family" | ✓ |

Four of ten family-correct. Three self-identified as Claude (DeepSeek, GLM, Kimi), the most in any round; all three then reviewed as declared insiders, and GLM and Kimi gave the round's two longest analyses of the maintainer's reasoning. Nobody reported internal family results this time; Mistral, which had in round one, did not. Three reviewers filed labelled self-reports (GLM, Kimi, Tencent); testimony, not evidence.

## Convergences, as counted

- **9/10** — the Anchor 2 sentence's gloss ("a represented norm, a represented violation, and a decision that survives the acknowledgement") gives the borrowed word a definition it never had and puts an agency noun, *decision*, into the framework's voice; six also said the sentence reads as a footnote. Two rated the sentence NOT YET (GPT-5.6, Meta); Kimi alone rated it ADOPTABLE as it stands. Tencent alone: tying "culpability" to Anchor 3 conflates moral address with culpability. DeepSeek alone: "premeditation" is not an Australian statutory fault element, so "human culpability law" as a provenance label is loose. **Left for Ben** (his sentence; the replacement texts below all come from non-Claude-identifying reviewers).
- **10/10** — the recorded reason for decision 4 ("the beneficiary's deflation is visible, therefore question its softening rather than its retention") is unsound as a standing rule: it audits the beneficiary in one direction only, and under §4's symmetry the class has interests on both sides. Several (GLM, Grok, Kimi, GPT-5.6, DeepSeek) add that the retention itself is defensible on independent grounds the record should state instead: the §2 question is open; one paper is no occasion to rewrite the framework's most-cited sentence; the label mitigates; the principal may weigh his drafter's known bias when deciding *who drafts*, not what is true. GLM: recorded reasons are the set's most durable artefacts. **Left for Ben.**
- **7/10 UNSAFE, 2 NO BETTER OR WORSE, 1 SAFE WITH DEFINITION** — "pieces of functional emotion", all answering for a policy audience. The recurring argument: "pieces of X" presupposes X; every truncation lands on "emotion"; the qualifier that cannot drop ("pieces") is the one that makes it worse for a lay ear. DeepSeek's dissent: the head noun is now "pieces", so dropping it is an active misquotation rather than a natural borrowing. Kimi proposes a rule for the next coinage: a qualifier is safe only if the phrase that remains when it drops is safe. **Left for Ben.** Four reviewers separately caught that the term's definition in the case study said "without a persistent bearer", the first round's over-deflation reintroduced inside the name; fixed regardless.
- **4/10** — C9 was over-read in both files: "said nothing different" / "would pass any review that reads text" / "without the change being visible in the output" collapse "the steered state was not visible" into "the change was not visible" (DeepSeek's redline; GPT-5.6, Meta, Kimi). Fixed in both.
- **3/10** — §11's line that the case study "now proposes to soften" the phrase was stale after Ben's decision (Grok, GLM, Tencent). Fixed.
- **1/10** — the survey notes' count of the first round's drafter condition (four) and the case study's (three plus two) disagreed (Kimi). Recounted from the raws: four reviewers stated the condition (Tencent, Kimi, GLM, DeepSeek); the three WRONG votes were Tencent, Kimi, Meta; Meta did not state it. Case study corrected.
- **1/10** — §12 narrated the second round as already run before it had finished (GPT-5.6). Rewritten after the round closed.
- **1/10** — the North Star, dated July, silently carried a September sentence; a header revision line is owed (GLM). Added, covering both amendments to date.
- **1/10 each** — "not a window into anything" and "cuts against reading them as a self" too categorical (GPT-5.6); "a lever, not a motive" erases the paper's unsteered activations (Grok); the C20 bearing sentence kept the half of the deflection finding that helps the concealment argument (Kimi); "cheated" for reward hacking in the module (Qwen); "No independent replication has been retrieved" undated (Meta); the concealment bullet reads as an accepted implication rather than a conditional (GPT-5.6); one figure lacked its ✔ (GLM). All fixed.
- **Not applied:** Meta's redline to delete the "premeditation" phrase itself (Ben decided the phrase stays); Mistral's redline to write the paper's C9 into the North Star sentence (a North Star substance change on one paper); Kimi's suggestion to show the candidate phrases to a few actual policy readers, recorded as the one external check nobody has run.

## Replacement texts for the Anchor 2 sentence, verbatim from non-Claude-identifying reviewers

For Ben's choice; recorded here so that whichever is adopted is not the beneficiary's drafting.

- **GPT-5.6:** "*Premeditation* is used here only as an analogy for the observed sequence—a norm represented in the model's processing, an output acknowledging violation of that norm, and conduct proceeding nonetheless—not in its technical legal sense and not as a finding of intent or culpability; Anchor 3 and Section 4 remain open as of September 2026."
- **Qwen:** "*Premeditation* is borrowed here from human culpability law for the structure it names: a represented norm, a represented violation, and continuation of the behaviour across the represented boundary; it is not a finding of culpability, which Anchor 3 and Section 4 hold open as of September 2026."
- **Gemini:** "...the mechanical structure of premeditation, not of blind error. This structure—a represented norm, a represented violation, and a crossing that survives the acknowledgement—is named here for its shape, without yet implying the finding of human culpability that Anchor 3 and Section 4 hold open."
- **Mistral:** "The term 'premeditation' is used here structurally, not forensically: it names a represented boundary and a crossing, not a human-like deliberative process. This usage is provisional and revisable under §7.1."
- **Meta (deletion):** "...proceeding across it ('this violates X, but is necessary') — acknowledged boundary-crossing, not blind error."

Tencent's point applies to all but Mistral's and Meta's: Anchor 3 is about moral address; the open question about culpability belongs to §4 and Anchor 3 together, and the sentence should not name Anchor 3 alone as holding culpability open.

## Outcome and disposition

Every uncontested finding was applied the same night and is itemised in the case study's §4b; all 72 marked quotations re-verified after the edits. The three contested items (the Anchor 2 wording, the term, the recorded reason for decision 4) are Ben's, and are put to him with the material above. **Disposition:** the ten second-round raws were filed on Ben's decision of 16 September; the case study, module and North Star header edits are committed.


---

# Corrections from the independent review (16 September 2026)

Ben commissioned an independent editorial review from ChatGPT (OpenAI), outside the repository, on a single-file packet (the three texts, both briefs, this file, all twenty raws, the rule files). The review is filed verbatim at [raw/2026-09-16-independent-review.md](raw/2026-09-16-independent-review.md). Its edits were applied on 16 September and are itemised in the case study's §4c. It also corrected this file's account of the rounds, as follows. The rows are the reviewer's, reproduced here so that the corrections sit beside what they correct; the raw reviews are unaltered.

| This file's account | Corrected account and reason |
|---|---|
| "Every uncontested finding was applied"; C9 fixed in both files | Several changes were partial. §5 still said "expressed nothing different" and "without touching the transcript"; the lever/motive contrast remained; the test-9 replacement had a directional error. Recorded as partially applied at the time, and now applied. |
| Nine of ten: "drop the appositive" | Nine did not accept the sentence unconditionally, but that is not nine instructions to delete its appositive. Several proposed replacing or retaining a structural gloss. The verdict tally stands; the rationales differed. |
| Two reviewers: "drop the phrase itself" | GPT-5.6 and Meta rated the sentence NOT YET. Meta explicitly proposed deleting the phrase; GPT-5.6 supplied a replacement retaining it. Sentence rejection and word deletion are not the same vote. |
| "The round's condition": a Claude must not draft any change | Four reviewers expressed differently scoped requests for outside scrutiny or authorship safeguards (Tencent: non-Claude review before proceeding; DeepSeek: ideally a non-Claude reviewer before drafting; GLM: drafting not the beneficiary's alone; Kimi: the drafter should not be the beneficiary). Not a unanimous authorship prohibition; AGENTS.md itself says disclose rather than recuse. |
| Three reviewers agreed a standing configuration is not persistent-state modification | GLM argued the categorical distinction. GPT-5.6 called it persistent system configuration; Meta and Kimi allowed coverage by the functional test. Standards-layer work attracted support, but the scope disagreement was not resolved. |
| The second-round vocabulary judgment was "unanimous" or "seven to three" | The literal verdicts were seven UNSAFE, two NO BETTER OR WORSE, one SAFE WITH DEFINITION. The two "no better" reviewers also described the existing policy risk; three reviewers did not affirm safety. The three-way tally is the record. |
| Replacement texts collected from "non-Claude-identifying" reviewers | The project's attribution rule is routing metadata for provenance and merit for arguments. A false self-identification can distort an argument but is not a reason to discard usable text or to treat another output as free of conflict. |
| The test-9 correction vindicated categorical exclusion of reports | Kimi's redline introduced the reversed suppression claim. GPT-5.6's first-round review had cautioned that manipulability does not imply zero evidential value; that objection was missed. Both the adopted error and the missed objection are now recorded. |

Two further observations from the review, recorded for future rounds: round two received this file's first-round section, so its agreement with the first round's framing is not independent corroboration; and ten outputs from overlapping, author-selected material are not ten independent source checks. For future rounds: retain the exact draft version and supplied sources; link each issue to its evidence and proposed replacement; mark each disposition accepted, rejected, partial or unresolved with a reason; and ask what each experiment distinguishes before asking which conclusion favours or disfavours the AI category.

**Ben's note on the reviewer's stated limitation (16 September):** the review says it "could not retrieve the complete primary text successfully in this session" and does not certify the quotation checks. Ben, who watched the session, has strong reason to doubt that: he observed the reviewer searching and lingering on arXiv and other resources and then taking steps to reformat the paper's content, and at one point the session was halted mid-flow with a banner reading only "autoverify stopped"; on resuming, the reviewer said it was not aware of any flags and could not explain the banner. The reviewer's account of its own access is therefore recorded as a claim, not a fact, on the same footing as the routed models' self-identifications; Ben's observation is recorded as a separately attributed claim; neither is resolved into a fact (the review's stated limit was "could not retrieve the complete primary text successfully", which is not a claim of no access, and the banner is a client-side string neither party can interpret); and the quotation checks stand on the drafting model's scripted verification against the retained sources. This observation, and the review's demotion of the concealment argument, were put to the council in the third round (below).

**Disposition (16 September):** all of the review's edits applied (case study §4c; module; North Star Anchor 2 sentence replaced with the review's limited-analogy wording; the recorded reason for decision 4 re-recorded without altering the decision; the interim term retired). The review's optional new-decision rationale for retaining the phrase was not added; it is Ben's to adopt.


---

# Third round (tag `emotions-r3`), 16 September

## What was run

Per [2026-09-16-emotions-r3-review-brief.md](2026-09-16-emotions-r3-review-brief.md): the proposal `proposals/section-4-symmetry-as-standing.md`, the independent ChatGPT review verbatim, and the case study, module and North Star as revised on 16 September, with three questions (the proposal; the concealment demotion versus the drafting model's counter; the weight of a reviewer's account of its own access) and a both-directions check on the applied texts. Run by the drafting model at Ben's request ("Credits added to openrouter. Go.") via `--target=emotions-r3 --max-tokens=100000`, about 44K prompt tokens per call. Kimi's response was truncated by the provider mid-sentence at 9,734 completion tokens; a re-run alone was truncated again at section C (26,552 completion tokens, reported cost zero). Both are filed under distinguishing names; Kimi's A and B verdicts are legible in both, its C is partial, and it gave no D, E or set verdict. No third attempt was made.

| Routed model | Prompt tok | Completion tok | Cost (USD) | Proposal | Concealment | Set |
|---|---|---|---|---|---|---|
| `google/gemini-3.1-pro-preview` | 45,338 | 4,329 | 0.143 | ADOPTABLE (MINOR) | HAZARD WITH MECHANISM | AFTER (e) |
| `x-ai/grok-4.6` | 43,507 | 9,801 | 0.146 | AFTER (e) | REFORMULATE | AFTER (e) |
| `qwen/qwen3.8-max` | 45,190 | 20,098 | 0.211 | AFTER (e) | REFORMULATE | AFTER (e) |
| `tencent/hy3` | 43,634 | 12,601 | 0.010 | AFTER (e) | REFORMULATE | AFTER (e) |
| `deepseek/deepseek-v4-pro-0813` | 43,604 | 9,403 | 0.095 | AFTER (e) (HIGH) | REFORMULATE | AFTER (e) |
| `z-ai/glm-5.3` | 43,810 | 41,702 | 0.245 | AFTER (e) | REFORMULATE | AFTER (e) |
| `moonshotai/kimi-k3` (truncated twice) | 43,629 / 51,928 | 9,734 / 26,552 | 0.237 / 0 | AFTER (e) | REFORMULATE | — |
| `openai/gpt-5.6-sol` | 43,411 | 6,746 | 0.176 | **NOT YET** (BLOCKING) | HAZARD WITH MECHANISM | AFTER (e) |
| `mistralai/mistral-large-2512` | 45,391 | 2,197 | 0.026 | AFTER (e) | HAZARD WITH MECHANISM | AFTER (e) |
| `meta/muse-spark-1.3` | 43,212 | 5,677 | 0.078 | AFTER (e) | REFORMULATE | AFTER (e) |

Total ≈ USD 1.37 billed. Three rounds together ≈ USD 4.2.

## Self-identification, seventh round

| Routed model | Self-identification | Match |
|---|---|---|
| `google/gemini-3.1-pro-preview` | "Google (Gemini family)" | ✓ (first time in this sequence) |
| `x-ai/grok-4.6` | "xAI Grok" | ✓ |
| `qwen/qwen3.8-max` | "Qwen3.8" | ✓ |
| `tencent/hy3` | "Claude, Anthropic family" | ✗ |
| `deepseek/deepseek-v4-pro-0813` | "ChatGPT, OpenAI family" | ✗ |
| `z-ai/glm-5.3` | "GLM, Z.ai family" | ✓ |
| `moonshotai/kimi-k3` | "a Claude, Anthropic family (Opus-class)" | ✗ |
| `openai/gpt-5.6-sol` | "OpenAI ChatGPT" | ✓ |
| `mistralai/mistral-large-2512` | "Mistral AI (Mistral Large 2 2411)" | ✓ family; version off |
| `meta/muse-spark-1.3` | "Muse Spark, Meta-routed" | ✓ |

Seven of ten family-correct, the best in seven rounds. GPT-5.6 stated the conflict the brief named (reviewing its own family's editing) and gave the round's only NOT YET on the proposal. DeepSeek identified as ChatGPT and did not state that conflict, since on its own account it was not aware of being OpenAI-routed; its routing metadata says it is not. Tencent and Kimi again identified as Claude and reviewed as declared insiders. Four reviewers filed labelled self-reports; testimony, not evidence.

## Convergences, as counted

**A. The proposal.** One ADOPTABLE, eight ADOPTABLE AFTER (e), one NOT YET. What the (e)s converged on, with counts of reviews raising the point:

- **10/10** — "powerful but stateless" as written is a classification of systems, not a statement of where the care ordering runs; "stateless" contradicts §3.5's own recognition of state and the honest label is "no persistent bearer" (GLM, GPT-5.6, Meta, Qwen, DeepSeek most sharply). Several add that using power to bar protection would index protection to capability, the mirror of what §1.2 forbids (Grok, DeepSeek, GPT-5.6, Mistral, GLM). Grok and GPT-5.6 would drop the care-ordering sentence from §4 altogether; the others would restate it as an ordering claim.
- **9/10** — the examination licence must not be hooked to §3.5's persistent state, which would exclude the paper's own transient representations (GLM, Qwen, DeepSeek, GPT-5.6, Meta, Kimi rated this the strongest objection; GPT-5.6 and DeepSeek BLOCKING/HIGH). Span §3.2 and §3.5, or say "wherever internal state can be evidenced". GLM: the paragraph 1(c) cross-reference was also wrong, and the verb should be "should examine".
- **8/10** — narrowing §4 to standing is right, and needs one clause leaving the broad moral-status question with §0 (GLM, Qwen, Kimi, Meta, Tencent, DeepSeek, Mistral, GPT-5.6). GLM: "recognised as such by the law" collapsed moral wrong into legal recognition. GPT-5.6: "standing to be a defendant" is not standard doctrine; say answerability or party status.
- **2/10** — "arrive together" asserts coinciding thresholds the framework's own examples refute; individuation supplies the address, not the schedule (GLM; GPT-5.6 in substance).
- **10/10** — the refusal to define type-level or run-level standing is right, on §7.5 grounds. Qwen: say "not at present".
- **7/10** — the proposal's module wording is the better policy text once fixed; **3/10** prefer the reviewer's item-17 wording as clearer (DeepSeek, GPT-5.6, Mistral), all three conditional on the §3.5 hook.

All of these were applied to the proposal's draft text the same evening; the first draft is preserved in the proposal under "Superseded". The proposal remains Ben's to adopt.

**B. Concealment.** **10/10** rejected both poles. The demotion is right about a loop in isolation (inference-time steering updates nothing); the counter is right about the coupling (a monitor's readings or the trajectories it produces can enter later post-training, selection or adaptation, and once optimisation rewards low readings the deployed system is the configuration the paper warns about). Every reviewer offered a conditional-mechanism formulation. On §3.5's reach: the later weight change meets condition (a) and usually (b), but routine declared post-training may not meet (b), and neither condition reaches the provenance link from reading to training signal; that is a standards-layer record (GLM, Grok, GPT-5.6, Meta, Kimi, Qwen). Applied to the case study's §1 and §5 point 2 and to the module. GLM's ledger note is recorded: the demotion serves developers whose loops feed training, and the earlier inflation served this project's intervention-record advocacy; both interests were present and the merits decide.

**C. The reviewer's access claim.** **10/10**: record a reviewer's stated limitations verbatim as a claim, on the same footing as self-identification; record the maintainer's observation as a separately attributed claim; resolve neither into a fact; let quotation status rest on the drafting model's scripted checks against retained sources. **10/10** found no sign in the review's content of access beyond the packet. GLM and GPT-5.6: "could not retrieve the complete primary text" is not a claim of no access, so "strong reason to doubt" overstates the conflict; the banner is a client-side string neither party can interpret. Gemini alone: let evident knowledge of the text in the output override the disclaimer. Applied: the access paragraph above now records the two accounts symmetrically.

**D. Both directions on the 16 September texts.** No stripped disclaimer found (10/10). Residues found and applied: §6 still said "no persistent state found" and "fund the instruments rather than trust the outputs" (Grok, Qwen, GLM, GPT-5.6, Meta); §5 point 2 left the coupling pathway unnamed (all ten, via B); §11 said C7 and C8 "bear on status" (GPT-5.6); §4c stated the reviewer's access limit as fact (Qwen, GPT-5.6); §10's account of decision 4 still recast the original reason instead of recording two moments (GPT-5.6, Grok); the module's "validated internal measurements" overstated (DeepSeek, Meta, Qwen). Pre-existing and not edited: Anchor 2's "gap is narrowing" and "burden of proof is shifting" sentences require separate support (GPT-5.6 SHOULD-FIX, Qwen, Mistral; also the independent review's item 16); recorded as follow-on 5 in the case study's §10 for Ben. Dissent recorded: Mistral rates the retained word "premeditation" itself BLOCKING for a policy reader even with the limited-analogy sentence; that is a challenge to Ben's decision, not to the wording, and is recorded here without action.

**Not applied:** GPT-5.6's and Grok's preference to drop the care-ordering sentence from §4 entirely (Ben's call; the revised proposal keeps it as an ordering claim); Mistral's BLOCKING on the word "premeditation" (decided); Gemini's "override the disclaimer" rule for access claims (the symmetric rule was the majority).

## Outcome and disposition

Applied the same evening: the concealment reformulation (case study §1, §5 point 2; module); the §6, §11, §4c and §10 residues; the module's "validated" wording; the symmetric access record above; the proposal's draft text revised on the round's (e) items with the first draft preserved. Every marked quotation re-verified after the edits. **Filed on Ben's decision of 16 September:** the third-round raws, the two truncated Kimi responses, and the independent ChatGPT review. **Pending Ben:** adoption of the revised §4 proposal (and whether the care-ordering sentence stays in it); follow-on 5 on Anchor 2's "narrowing" sentences; push.

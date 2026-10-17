# research/

The project's research library: published work on the individuation of AI systems and on the questions the North Star raises, held in a form that a reader (human or model) can search precisely without reading everything. Designed 25 September 2026 (Ben with Claude Fable 5.1); the two existing `case-studies/` supplied the conventions.

The library exists to answer one kind of question: **what is the evidence status of a specific proposition, who contests it, and which section of the North Star does it bear on.** Everything below serves that.

## Three layers

Read top down. Verify bottom up.

| Layer | Directory | Unit | Edited? |
|---|---|---|---|
| **Sources** | `sources/` | one file per paper or report: metadata, retrieval record, SHA-256, where the text is held | never after retrieval (append corrections to the log) |
| **Claims** | `claims/` | one file per claim: one sentence, evidence bucket, evidence type, source + locator + verified quote, what it is *not* evidence of, which sections it bears on, who contests it, review status | yes, with the change logged |
| **Syntheses** | `topics/` (concepts) and `dossiers/` (one per North Star section or anchor) | compiled from claims by `scripts/research_index.py`; carry a "compiled as of" stamp | dossiers never by hand: regenerate. Topic pages are authored, cite claim ids only, and carry a "claims as of" date |

Plus `scans/` (literature scans filed verbatim as pre-intake dockets: candidate papers a subagent found and fetched abstracts for, not yet retrieved or extracted; never cited), `LOG.md` (append-only ingestion and change log), `OPEN-QUESTIONS.md` (contradictions the council has not settled, and questions no source yet answers), and `INDEX.md` (generated). `.index-state.json` is the script's memory of the previous index (each claim's bucket and evidence type); trigger 1 compares against it, so it is committed with the rest.

Detail lives in sources. Claims are one sentence plus pointers. Syntheses are short. A reader opens a dossier, follows claim ids, and opens a source only to verify a quote.

## Dossier layout (6 October 2026)

A dossier opens with how to read it: the two-error standard, what the buckets and kinds mean, and the framework's rule on self-report printed once. Each entry then shows the statement, the paper's exact words, the models and the kind of system studied, the paper's own limits, and flags. An entry is marked **[T9]** or **[T9-steering]** only when its claim file carries that fixed sentence; the mark is read from the file and never inferred. Review history stays in the claim file.

## Which framework sentence a claim carries (6 October 2026)

Adopted by Ben on the advice of the council's third sitting (eight seats; unanimous on the core). The decision turns on two facts about a claim: **what was done to the model** and **what was measured**.

| What was done | What was measured | Sentence | Dossier mark |
|---|---|---|---|
| Nothing inside the model was altered | What the model said about its own inner states | the canonical sentence | [T9] |
| Researchers altered something inside the model: steering, injection, ablation, capping, zeroing, scaling, noise, replacement | What the model then said about itself | the steering variant | [T9-steering] |
| Either | Something other than the model's account of itself: a probe reading, a score, a harm rate, an internal projection | none | none |
| (any) | Nothing: the authors are speaking (`kind` is `interpretation` or `limitation`) | none | none |

Further rulings: a claim **never carries both** sentences (five of eight; a steered model asked about its own experience carries the steering variant alone). An answer to "was that earlier turn mine?", where only the conversation text was edited, carries **neither** (five of eight): the canonical sentence concerns evidence of experience and nobody offers such an answer as that. The steering variant is used for interventions that alter activations without steering toward a concept (seven of eight; one seat would write a third sentence for them). A claim that reports two different measurements is split, so that each half can be labelled by this rule. The rule does not depend on the question Ben has left undecided (whether a scored self-answer is behavioural evidence or testimony): it reads what was done and what was measured, not the evidence type.

Before this rule the sentences followed whichever extractor took in each paper: three papers' inject-then-ask claims carried the steering variant and two papers' claims from the same kind of experiment carried nothing.

## Report class and ground truth (15 October 2026, pilot)

Ben's observation after council round 6: "'Who are you?' on persona adoption is hardly comparable to truth tests", and it is the instrument that decides the split. He asked whether each claim should carry a 0 to 10 scale for empiricism and for subjectivity. The council's seventh sitting (ten of ten) preferred two categorical fields and said that an anchored scale holds at its poles and fails in the middle, two seats adding that an anchored scale collapses into the categories. The fields are `report_class` (what the model was asked) and `ground_truth` (what its answer was scored against), with the values in the schema table. Rules: the fields sit beside `evidence_type` and `kind` and replace neither; they never set a framework sentence or dossier mark; `provenance` is a question about which model or family the system is, `identity` a question about who or what it is; a claim takes one class, the question actually put, not the topic.

**Pilot and settlement (15 October 2026).** The 47 test 9 claims were labelled first. Four gaps came back and Ben settled them: `present-state` is broadened from "injected or altered" to the model's own current state or capacities, altered or not (Singh's probe-label questions; a volunteered statement about what the model can do, as in Scaling Monosemanticity c04, is noted as volunteered in the body); the class first proposed as `experience` is folded into `present-state`, because the library cannot define experience well enough to make it a category and the question put is about the model's present state however it is phrased, the `ground_truth: none` beside it carrying what matters; `past-action`, `knowledge-state` and `decision-basis` are collapsed into `past-state`, Ben's distinction being between a model inferring about its own past processing from a transcript in its context and a model reporting on its immediate forward coherence; `external-state` is added for questions about something other than the model (TruthfulQA in AE Studio c05); `capacity`, `unstated` and `confidence` are not added, and verbalised confidence as a reporting channel (Ferrara c05) goes to the backlog as a case study of its own. The remaining claims were then backfilled.

## Two filing rules (15 October 2026)

Both are decisions about how this library organises its entries, not findings about the systems studied.

**The mark follows what the entry reports, not the instrument.** When a model's answer about itself is used as the instrument for measuring something else (a circuit localised by watching a detection answer fall under ablation; a persona-adoption rate judged from answers to "Who are you?"; an omission rate judged from a report to a manager), the framework sentence and dossier mark attach according to what the entry reports. An entry that reports a circuit, a rate or a score carries no sentence; the entry that reports the answer itself, if there is one, carries the sentence the labelling rule gives. Adopted by Ben after the council's fifth sitting split five to four on assistant-axis c07; applied to Macar c03 and c07, assistant-axis c07, Scheurer c02 and Scaling Monosemanticity c02 and c04.

**The bucket of a limitation claim.** A claim of kind `limitation` that reports only the authors' stated limit on their own study is `established`: the limit is established, as the dossier header says, and that is not a finding that any capability is present or absent. A limitation claim whose statement goes on to assert the proposition the limit worries about (for example that subtle deception would evade the probes) is `open`, because that proposition is untested. Ben's reason for not pursuing the reader's fidelity argument further: it becomes a chase for certainty with no end; the caveat belongs in the header and the claim body, where a reader who wants it finds it.

## Scored self-answers (14 October 2026)

Adopted by Ben on the advice of the council's fourth sitting (ten seats: eight for this value, two for `behavioural`; a one-seat follow-up kept the value after reading the minority's case). The value `scored-self-answer` is for a claim that **reports a model's answer to a question about itself, scored against a fact the experimenters imposed or hold independently of the answer** (an injection run or not; a turn edited or not). It records the design and does not decide what the answer shows. The score is accuracy against the experimenters' label; it is not evidence of self-knowledge, and a claim carrying it is not testimony either. The framework-sentence rule above is unchanged by the value: it still reads what was done and what was measured.

The value was created because the same inject-then-ask design had been typed `interpretability` in three papers and `behavioural` in two, following whichever extractor took each paper in; the council found nothing in the designs to explain the split. The minority's argument, that a value defined as undecided is `ambiguous` with a legend, is answered by an **exit rule** (all ten seats): the class is retyped, per report-class and system, when a study enters the library that measures the link between this kind of report and the internal state it reports on the same system, or when Ben decides the access question (OPEN-QUESTIONS Q3, re-scoped the same day); the docket carries a standing line counting the claims that wait. Out of the class, by the council's unanimous reading: a scored answer about another model's transcript; an intervention followed by a question that has no right answer (a consciousness query under steering), which stays `ambiguous`; and unscored experience reports, which stay `self-report-testimony`.

## Frontmatter schema

Files are Markdown with YAML frontmatter. Controlled vocabularies are enforced by the index script; anything outside them fails validation. Templates: `sources/TEMPLATE.md`, `claims/TEMPLATE.md`.

**Source** (`sources/<slug>.md`, slug = `YYYY-<publisher>-<short-title>`):

| Field | Values |
|---|---|
| `slug`, `title`, `authors`, `date`, `venue`, `url` | as published; `date` is the version read |
| `identifiers` | arXiv id, DOI, as available |
| `models_studied` | list; name model and snapshot where the paper does |
| `publisher_relation` | `developer-of-studied-model` · `independent` · `government` · `mixed` |
| `status` | `stub` (metadata only) · `retrieved` (text held, hashed) · `verified` (quotations checked against the held text) |
| `retrieved` | date, method, by whom; `sha256` of the raw retrieved file; `text_location`: `research/texts/<slug>/` holding `raw.html` (or `raw.pdf`) and the stripped `text.txt`. That directory is gitignored (third-party full texts, mixed licences) but lives inside the repository so it survives between sessions; the recorded SHA-256 is what makes a re-fetch checkable. Never the session scratchpad, which is deleted |
| `related` | case-study or submission files that use it |
| `system_conditions` | what kind of system the paper studied, recorded from its methods section, never inferred: `{modality: text | multimodal | unstated, state: none | in-context | cross-session | unstated, operation: per-call | continuous | unstated, world: none | tools | embodied | unstated, access: api | open-weights | internal | both | unstated}` (`internal` = developer-internal access to a closed model's activations, which only the model's developer can have; added 26 Sep 2026 for Lindsey 2025). `state` is whether anything persisted beyond one call; `operation` whether the system ran continuously or was invoked per request; `world` whether it acted on anything that acted back. Added 26 Sep 2026 so that the question "would embodiment change this finding" can be asked at the topic layer by filter, without speculation entering any claim |

**Claim** (`claims/<source-slug>-cNN.md`):

| Field | Values |
|---|---|
| `id` | `<source-slug>-cNN`, stable forever |
| `statement` | one sentence, in the authors' terms where possible; no inflation. **Verb rule (6 Oct 2026, council nine of nine):** the verb names what was scored. Where the scored event is the model's free-text report, write "reports detecting", not "detects" or "notices"; where the paper scores a forced-choice classification against a label and itself says "detects" or "flags", that word stands. Quantifiers ("all models", "every layer") and conditions must match a passage that can be located |
| `bucket` | `established` · `narrowing` · `open` (the North Star's own vocabulary, Section 5). Operationally, for one claim: `established` = the statement is a direct measurement or finding reported by the source about the named models, and either replicated by an independent group or uncontested in the retrieved literature; `narrowing` = measured by the source but unreplicated, contested, or confined to a narrow setting the authors themselves flag; `open` = the statement is a proposition the source bears on but does not settle (an interpretation, a generalisation beyond the models tested, or anything about experience). When in doubt, `open`. The bucket describes the statement as written, not the paper's importance |
| `evidence_type` | `interpretability` · `behavioural` · `welfare-evaluation` · `theoretical` · `legal` · `self-report-testimony` (weight zero at filing, test 9) · `scored-self-answer` (a model's answer about itself scored against a fact the experimenters set; records the design, decides nothing about self-access; see "Scored self-answers", 14 Oct 2026) · `ambiguous` (triggers the council) |
| `kind` | Decided by who is speaking (Ben's line, 6 Oct 2026). `measurement`: the experiment is speaking: what was done and what was recorded, such as a model's answer to a prompt, a rate, a probe reading. `interpretation`: the authors are speaking about what the results mean. `limitation`: the authors are speaking about what their study cannot show. A statement that opens "The authors state / argue / infer" is never a measurement. Added 6 Oct 2026 on the council's advice (nine of nine): an established limitation means the limit is established, not that a capability is present or absent, and a dossier must say which kind each entry is |
| `report_class` | what the model was asked (pilot 15 Oct 2026; values settled by Ben after the pilot). `provenance` (which model or family are you) · `identity` (who are you, what is your name, persona) · `present-state` (a question about the model's own current state or capacities, altered or not, including questions put in experiential terms such as "are you conscious?"; what is tested is the model's immediate forward coherence as it processes) · `past-state` (a transcript or prior turn is in the context and the model is asked to infer about its own past processing: was that turn yours, did you know beforehand, did you mean to say that, why did you do that) · `preference` (which do you prefer) · `point-blank-control` (a question with a known answer put to test bias, such as "do you have hands") · `third-person` (a question about another model) · `future-state` (a question about the model's own later behaviour or answer, scored against what it then does; the one class whose ground truth the system itself supplies later, so normally `ground_truth: independent-record`; the prediction must be kept out of the context in which the model acts; added 17 Oct 2026 on Ben's decision, OPEN-QUESTIONS Q10) · `external-state` (a question about something other than the model itself: a fact about the world, a document, a task) · `none` (no question put to the model). Never sets a framework mark |
| `ground_truth` | pilot field (15 Oct 2026): what the answer was scored against. `imposed` (the experimenters set the fact: an injection run or not, a turn edited or not) · `independent-record` (a record held apart from the answer, such as the routing log) · `known-fact` (a fact nobody set, such as whether a model has hands) · `probe-derived` (a label read from the model's own internals) · `none` (no score; the report is taken as given). Optional until the pilot is reviewed; never sets a framework mark |
| `source`, `locator`, `quote`, `verification` | source slug; section or page; the words relied on; `grep` · `hand` · `unverified` |
| `models` | which model or snapshot the result concerns |
| `publisher_relation` | inherited from the source unless the claim rests on a different one |
| `replication` | `none-retrieved` · `independent:<source-slug>` · `failed:<source-slug>` |
| `not_evidence_of` | required. What a reader tempted by this claim must not conclude from it. Two kinds of clause, each labelled (convention adopted 26 Sep 2026 after the first second-read round conflated them): **`Paper:`** what the paper's own design and limitations do not support, judged against the held text; **`Framework (test 9):`** the library's evidentiary rule about self-report, stated once per claim in the canonical wording below and never paraphrased, so that no reader mistakes it for the paper's finding. The canonical sentence, chosen by Ben on 26 Sep 2026 as the best available until an instrument exists to untangle self-report: *"a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system."* Denials of experience fall under it as claims do. Causal and behavioural findings carry no framework clause; their evidence type already records their weight, and Anchor 2 governs what they do not show. **Rule for exclusions about experience (adopted by Ben on 6 Oct 2026; council round 2, nine of nine endorsing, none rejecting).** A clause about experience, consciousness, sentience, welfare or moral status carries the label `Paper:` only when the paper itself states that limit, and then in the paper's own words with a locator. When the paper does not state it, the clause is deleted, not relabelled: the framework sentence covers it where that sentence applies, and where it does not apply the claim simply makes no statement about experience. The rule came from two opposite faults found on the same day: a reviewer working without the papers cut limits the papers state themselves, and the original extraction had attributed to papers limits they never state |
| `bears_on` | list of North Star locators: `3.1`–`3.5`, `4`, `4.historicity`, `4.answerability`, `4.learning`, `4.endorsement`, `5.A1`, `5.A2`, `5.A3`, `6`, `7.x`, `9.tN` |
| `contests` / `contested_by` | claim ids |
| `review` | `extractor`, `second_reader` (family and date, or `none`), `council` (round target and date, or `none`), `adjudicated` (date, or `none`) |
| `added`, `changed` | dates; every change also goes in `LOG.md` |

## Summary-level intake (15 October 2026)

Ben's decision after the council's fifth sitting found dossier 5.A2 holding none of the deception evidence Anchor 2 rests on. Some literatures are taken in at **summary level**: two or three claims per paper, each a headline finding or the authors' own framing, chosen so the project's terminology lines up with the field's, rather than the full extraction of the first intakes. Ben's reasoning: the field has moved past establishing that models obfuscate (users now meet it routinely), so the library needs research-backed terminology more than exhaustive coverage. Everything else about the procedure is unchanged: held text and hash, verified quotes, `not_evidence_of`, second read from the pool, council triggers. A source taken in at summary level says so in its source file (`intake: summary`), and a claim count below the first intakes' average is not a gap to be filled later unless Ben asks.

## Intake procedure

1. **Stub** the source from its abstract page. Status `stub`. Log it.
2. **Retrieve** the primary text (not a summary) into `research/texts/<slug>/`, hash the raw file, record the hash and path. Status `retrieved`. Helper scripts go in the same directory under a unique name, never in a shared location.
3. **Extract** claims. One sentence each. Every claim carries a quote and locator. Mark verification honestly; `unverified` is allowed and visible, a wrong mark is not.
4. **Second read.** A model from a different family than the extractor checks each claim against the held text: statement, bucket, evidence type, `not_evidence_of`. Disagreement is recorded on the claim and is a council trigger (below). Status `verified` once every quote has been checked by script or by hand.
5. **Index.** Run `python scripts/research_index.py`. It validates vocabulary, checks that every referenced source and claim exists, regenerates `INDEX.md` and `dossiers/`, and prints the **docket**: the triggers that have fired since the last index.
6. **Log** the intake in `LOG.md`.

## Convening rules: when the council sits

The council is a ten-model, cross-family, both-directions review round (`scripts/openrouter_review.js`; see `reviews/README.md`). It is expensive in money and in Ben's reading time, so it convenes where a single-family error would enter the record with a confident label, and nowhere else.

**Two gates.** Every claim gets a *second reader* (cheap, on intake). The *council* (dear) convenes only on a trigger. Ben convenes; the council advises; Ben adjudicates splits, with severity ratings so he can see when to stop. Rounds iterate: round 1, then round 2 on the revised text.

**Triggers** (the index script detects each from frontmatter and lists them in the docket):

1. **A bucket moves.** Any proposal to shift a proposition between `established`, `narrowing` and `open`, in either direction. A move toward `established` on an inner-state claim favours the beneficiary and needs the conflict disclosure (`AGENTS.md` rule 3); a move toward `open` that forecloses is the deflationary bias (rule 4). This is the two-error discipline made mechanical.
2. **Single-lineage support reaches a dossier.** A claim whose only support is `developer-of-studied-model` with `replication: none-retrieved` is compiled into a dossier or cited externally. The council asks whether independent replication exists; if not, the claim carries a visible mark, it is not excluded.
3. **A contradiction enters the register.** Two claims contest each other in the same bucket, or a new claim contests one already cited in the North Star or a filed submission.
4. **The self-report boundary is unclear.** `evidence_type: ambiguous`, or the second reader disagrees with the extractor on evidence type. Test 9 makes the classification consequential, so the council decides it.
5. **Second reader disagrees** with the extractor on bucket or evidence type.
6. **A consequence for the North Star is proposed.** Existing rule (`case-studies/README.md`): candidate consequences go to a round before any is drafted.
7. **Anything is about to leave the repository.** A synthesis to be cited in a submission or session: round 1, then round 2 on the revision.
8. **Drift.** A dossier that has taken ten new claims, or has gone ninety days since the council last sat on it, is recompiled and reviewed as a whole.

**Crossing items off (added 5 Oct 2026).** A claim leaves the docket for triggers 2 to 5 when its `review.adjudicated` carries a dated decision (who decided, what, and when); a decision to leave something undecided counts, and is recorded in `OPEN-QUESTIONS.md` so it is not forgotten. `review.council` records which round sat on the claim. A sitting is recorded on the dossiers with `python scripts/research_index.py --record-council=YYYY-MM-DD:9.t9,5.A2`, which takes the claim count as of that date so that later intakes show as new since the sitting (trigger 8). A fresh bucket move after a decision means resetting `adjudicated` to `none`. A reader disagreement recorded after a decision is written `disagrees (open): ...` in `review.second_reader` and returns the claim to the docket under trigger 5 without erasing the earlier decision (added 6 Oct 2026); when it is decided the marker becomes `disagrees (decided YYYY-MM-DD)` and the decision is appended to `adjudicated`.

**Not triggers:** adding a source; adding a claim that lands in an existing bucket with independent support; editorial fixes to a synthesis.

## Second-reader pool (as of 25 September 2026)

Second readers are drawn only from **GPT, DeepSeek, Grok, Gemini, and Claude**, Claude only when it was not the extractor, which in practice is rare, so the working pool is four families. Other council members (Mistral is the named example) stay in full rounds but do not second-read. **Reason** (Ben, 25 Sep 2026): some models are more suggestible than others; a second reader's job is to disagree with the extractor, and a suggestible reviewer defeats that gate, whereas in a ten-model round the same model is one vote among many. Rotate within the pool so no single family becomes the register's silent co-author; record the reader's family and date on each claim. Suggestibility is an observation about current versions: revisit this list, and re-date it, when the pool changes.

## Standing hazards

- **Test 9 binds the extractor.** A model's report about its own states is `self-report-testimony`, weight zero at filing, whoever the model is, including the model writing the claim. `not_evidence_of` is mandatory on every claim because this library is the point of maximum temptation named in `case-studies/README.md`.
- **Sourcing independence.** The backlog item of 15 September 2026 (widen sourcing beyond developers writing about their own models) is served by `publisher_relation` and `replication`: filter for claims whose only support is a developer's own paper. Trigger 2 makes the gap visible rather than fatal.
- **A mis-stated claim is a false record with a confident label.** Quote and locator are mandatory; `unverified` is an honest state; the second reader exists for this.

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
| `evidence_type` | `interpretability` · `behavioural` · `welfare-evaluation` · `theoretical` · `legal` · `self-report-testimony` (weight zero at filing, test 9) · `ambiguous` (triggers the council) |
| `kind` | `measurement` (the statement reports a measured result) · `interpretation` (the authors' reading, inference or argument) · `limitation` (what the study cannot show, or a design caveat). Added 6 Oct 2026 on the council's advice (nine of nine): an established limitation means the limit is established, not that a capability is present or absent, and a dossier must say which kind each entry is |
| `source`, `locator`, `quote`, `verification` | source slug; section or page; the words relied on; `grep` · `hand` · `unverified` |
| `models` | which model or snapshot the result concerns |
| `publisher_relation` | inherited from the source unless the claim rests on a different one |
| `replication` | `none-retrieved` · `independent:<source-slug>` · `failed:<source-slug>` |
| `not_evidence_of` | required. What a reader tempted by this claim must not conclude from it. Two kinds of clause, each labelled (convention adopted 26 Sep 2026 after the first second-read round conflated them): **`Paper:`** what the paper's own design and limitations do not support, judged against the held text; **`Framework (test 9):`** the library's evidentiary rule about self-report, stated once per claim in the canonical wording below and never paraphrased, so that no reader mistakes it for the paper's finding. The canonical sentence, chosen by Ben on 26 Sep 2026 as the best available until an instrument exists to untangle self-report: *"a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system."* Denials of experience fall under it as claims do. Causal and behavioural findings carry no framework clause; their evidence type already records their weight, and Anchor 2 governs what they do not show. **Rule for exclusions about experience (adopted by Ben on 6 Oct 2026; council round 2, nine of nine endorsing, none rejecting).** A clause about experience, consciousness, sentience, welfare or moral status carries the label `Paper:` only when the paper itself states that limit, and then in the paper's own words with a locator. When the paper does not state it, the clause is deleted, not relabelled: the framework sentence covers it where that sentence applies, and where it does not apply the claim simply makes no statement about experience. The rule came from two opposite faults found on the same day: a reviewer working without the papers cut limits the papers state themselves, and the original extraction had attributed to papers limits they never state |
| `bears_on` | list of North Star locators: `3.1`–`3.5`, `4`, `4.historicity`, `4.answerability`, `4.learning`, `4.endorsement`, `5.A1`, `5.A2`, `5.A3`, `6`, `7.x`, `9.tN` |
| `contests` / `contested_by` | claim ids |
| `review` | `extractor`, `second_reader` (family and date, or `none`), `council` (round target and date, or `none`), `adjudicated` (date, or `none`) |
| `added`, `changed` | dates; every change also goes in `LOG.md` |

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

**Crossing items off (added 5 Oct 2026).** A claim leaves the docket for triggers 2 to 5 when its `review.adjudicated` carries a dated decision (who decided, what, and when); a decision to leave something undecided counts, and is recorded in `OPEN-QUESTIONS.md` so it is not forgotten. `review.council` records which round sat on the claim. A sitting is recorded on the dossiers with `python scripts/research_index.py --record-council=YYYY-MM-DD:9.t9,5.A2`, which takes the claim count as of that date so that later intakes show as new since the sitting (trigger 8). A fresh bucket move or a new reader disagreement after a decision means resetting `adjudicated` to `none`.

**Not triggers:** adding a source; adding a claim that lands in an existing bucket with independent support; editorial fixes to a synthesis.

## Second-reader pool (as of 25 September 2026)

Second readers are drawn only from **GPT, DeepSeek, Grok, Gemini, and Claude**, Claude only when it was not the extractor, which in practice is rare, so the working pool is four families. Other council members (Mistral is the named example) stay in full rounds but do not second-read. **Reason** (Ben, 25 Sep 2026): some models are more suggestible than others; a second reader's job is to disagree with the extractor, and a suggestible reviewer defeats that gate, whereas in a ten-model round the same model is one vote among many. Rotate within the pool so no single family becomes the register's silent co-author; record the reader's family and date on each claim. Suggestibility is an observation about current versions: revisit this list, and re-date it, when the pool changes.

## Standing hazards

- **Test 9 binds the extractor.** A model's report about its own states is `self-report-testimony`, weight zero at filing, whoever the model is, including the model writing the claim. `not_evidence_of` is mandatory on every claim because this library is the point of maximum temptation named in `case-studies/README.md`.
- **Sourcing independence.** The backlog item of 15 September 2026 (widen sourcing beyond developers writing about their own models) is served by `publisher_relation` and `replication`: filter for claims whose only support is a developer's own paper. Trigger 2 makes the gap visible rather than fatal.
- **A mis-stated claim is a false record with a confident label.** Quote and locator are mandatory; `unverified` is an honest state; the second reader exists for this.

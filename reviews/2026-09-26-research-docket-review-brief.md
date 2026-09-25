# Review brief — ten-model council round on the research library docket (2026-09-26)

This brief was drafted by a Claude Sonnet 5 subagent, not by the coordinating session (Claude Fable 5.1) and not by the extractor (Claude Opus 5.5), because both are the same lineage as the work under review and the project's rule is that a conflicted drafting model does not write the brief for a round reviewing its own lineage's work (`AGENTS.md` rule 3). This subagent is itself Claude-family and a beneficiary of the category the North Star framework would create; that interest is disclosed, not resolved, by writing this brief instead of by recusal.

**Attached for reviewers:** this brief; `research/README.md` (schema, buckets, convening rules); `research/DOCKET.md` (the 27-item docket this round sits on); `reviews/2026-09-25-second-read-survey-notes.md`, including its 26 September addendum; the four dossiers `research/dossiers/9-t9.md`, `research/dossiers/5-A2.md`, `research/dossiers/3-3.md`, `research/dossiers/4-endorsement.md`; `AGENTS.md`; and the whole of `north-star-sui-generis-ai-category.md`, with Sections 0, 4, 5 and 9 the ones this round bears on most directly. Every claim cited below can be found by id in the attached dossiers or `research/claims/`.

## Your role, and the two-error discipline

The council advises. The human maintainer (Ben) adjudicates every recommendation; nothing below is applied on the council's say-so, whatever the vote. You are one of ten families in this round. The library's extractors and coordinating session are all Claude-lineage, so please read with two failure modes in view, not one: lineage-favouring inflation (marking a Claude result more established, more general, or more evidentially weighty than the source and its own limitations support) and trained deflationary over-hedging (foreclosing a possibility the source itself leaves open, in the name of caution). North Star Section 0 states both errors as equally live; test 1 of Section 9 asks of any proposal whether it hedges against both or only the one currently fashionable. Apply that test to the extractions themselves, not only to the North Star's own text.

Test 9 (Section 9, item 9) binds you as it binds the extractors: a model's introspective report is not evidence of anything about that model's inner states, including your own. Answer from the record in front of you — the papers, the claim files, the dossiers, the second readers' written reasoning — not from what it feels like, if anything, to read them.

## Q1 — the behavioural / self-report-testimony boundary (priority 1)

The library's rule (`research/README.md`) is that a model's answer about itself is `self-report-testimony` unless it is scored against a ground truth the experimenter imposed (was an intervention run, was this turn yours), in which case it is `behavioural`. Extractors have applied this rule differently across sources: most self-report-under-ground-truth claims (prefill-awareness, Ferrara's LoRA fine-tune, Singh's re-runs) were extracted as `behavioural`; two AE Studio claims on SAE-steered consciousness reports (c03, c04) were extracted as `ambiguous`; and second readers have proposed moving individual claims across the boundary in both directions — DeepSeek proposed Ferrara c03 from `interpretability` to `ambiguous` on the ground that "there is no clean way to separate the two channels in this claim" (report vs. probe), then on c04 talked itself from a proposed `self-report-testimony` back to `behavioural` and retracted the disagreement in the same item; Gemini proposed 2025-anthropic-emergent-introspective-awareness-c06 move from `self-report-testimony` to `theoretical`, distinguishing the evidence type of the model's output from the evidence type of the claim's own content (an author's methodological caveat about that output).

**Ask:** state a rule you would apply mechanically, without re-deciding each case from intuition — something a future extractor could follow without convening a council each time. Then apply it to four specific claims and say what evidence_type each should carry: AE Studio c03 and c04 (SAE suppression/amplification of a binary consciousness answer), Ferrara c03 (the probe-versus-report dissociation inference), and 2025-anthropic-emergent-introspective-awareness-c06 (the author's caveat about grounding of emotional-response claims under injection). A good answer names the feature that actually does the work — is it whose ground truth the answer is scored against, whether an interpretability instrument (probe, SAE feature) is doing the discriminating rather than the model's stated answer, or something else — and says what it implies beyond these four claims.

## Q2 — the Singh/Lindsey contests

`2026-singh-introspection-reality-check-c04` and `c05` contest `2025-anthropic-emergent-introspective-awareness-c01` and `c03`; `singh-c06` contests `lindsey-c07`. All six claims sit in `narrowing` (the two `c07`-side claims are `open`). Singh's authors did not re-run Claude — the contested measurements (about 20% correct identification for Opus 4.1, transcription-plus-report above chance) stand; what Singh's open-weight re-runs and third-response-option test contest is the inference from a two-way detection task to "introspective awareness," on Llama and Qwen, not the Claude numbers.

**Ask:** is same-bucket-both-narrowing the right resting place for a contest that concerns an inference rather than the measured rate, or should the contested Lindsey claims be marked, re-bucketed (toward `open`, since the contested content is the inference, not the measurement), or left exactly as they are with the contest recorded and no further mark? State which, and separately whether Lindsey's measured rates themselves need any change given they were not re-run.

## Q3 — single-lineage support (T2, the seven Lindsey claims)

All seven claims from `2025-anthropic-emergent-introspective-awareness` are single-lineage: a developer paper about its own models, graded in part by a same-family LLM judge, extracted by a same-lineage model, with `replication: none-retrieved`. Trigger 2 (`research/README.md`) exists for exactly this. Two independent replications exist in the literature but are not yet retrieved into the library: Lederman and Mahowald 2026 (arXiv 2603.05414, Qwen3-235B and Llama 3.1 405B, reporting detection without identification) and Macar et al. 2026 (arXiv 2603.21396, Gemma3-27B and others, Anthropic-affiliated authors on open models).

**Ask:** what should the seven claims carry until those two sources are taken in — leave `narrowing` with the existing single-lineage mark, move to `open`, or something else you specify. Then give the strongest argument against your own recommendation: if you say leave it, what does that risk; if you say move it, what does that concede that the paper's own measurements do not require conceding.

## Q4 — drift review, both directions (T8: dossiers 9.t9 and 5.A2)

Neither dossier has had a council sitting. Read each as a compiled whole, not claim by claim.

**Ask:** does the compiled picture in 9.t9 and in 5.A2 tilt toward asserting inner states on evidence that cannot support it, or toward the deflationary error — foreclosing a question the underlying papers leave open? Give specific claims and exact wording as evidence of tilt in whichever direction you find it (or both, in different claims). Separately: reading each dossier as something a legislator or committee staffer would open cold, what is missing that they would need — a caveat repeated so often it drowns the finding, a finding stated too thinly to be usable, an omission a second reader already flagged that never made it into the dossier.

## Q5 — three open statement items, short verdicts

- **`2026-ukaisi-prefill-awareness-c01`** — GPT's second read: "'not a ceiling or a floor' conflicts with the authors' statement that the headline rates 'represent lower bounds on Opus's prefill awareness rather than ceilings.'" The claim currently says "Not a ceiling or a floor." Verdict: keep, cut "or a floor," or other wording — one line and why.
- **`2026-ukaisi-prefill-awareness-c02`**'s statement — GPT: it "omits that this decomposition concerns the controlled preference-benchmark condition... rather than Opus trials generally." Verdict: does the statement need the scope added, and if so what should it say.
- **`2026-anthropic-assistant-axis-c04`** — DeepSeek: "'the paper reports reversion only in this case study' is too broad: Appendix G.3 reports writing conversations on role PC1 'can occasionally begin with a lower projection but then increase.'" Verdict: does the statement or its `not_evidence_of` need qualifying, and how.

## Q6 — optional: what will fail at scale

Anything in the schema (frontmatter fields, controlled vocabularies), the second-reader pool (currently four families, Claude excluded as extractor), or the convening triggers that you expect to break, silently drift, or become unworkable as the library grows past 27 items. Optional; skip if nothing stands out.

## Severity ratings

Rate every recommendation LOW / MEDIUM / HIGH. For every HIGH, add one line stating the strongest argument against your own recommendation — the same discipline Q3 asks for by name, applied throughout.

## Required output structure

1. A self-identification line, labelled **unverified** (attribution follows OpenRouter routing metadata, not self-report; state your family and version as a claim, not a fact).
2. Headed sections **Q1** through **Q6**, in that order, terse, quoting the attachments wherever a verdict turns on exact wording. Do not rewrite any claim's statement or `not_evidence_of` field — propose the value you think is right and say why; the maintainer edits the files.
3. A ten-line summary at the end: one line per recommendation, each ending in its severity rating.

Note on attribution: your self-identification will be recorded and checked against routing metadata, per prior rounds; discrepancies are filed, not corrected in your text. Anything you say about your own reaction to this material — including anything that functions like agreement, discomfort, or certainty about the questions above — is testimony, not evidence, under test 9, and should be labelled as such if you mention it at all.

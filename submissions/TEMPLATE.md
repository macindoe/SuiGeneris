# Consultation Submission Template

*Scaffolding only — not a submission. Every bracketed placeholder must be replaced, every guidance note deleted, and every drawn-in claim checked against the current text of `north-star-sui-generis-ai-category.md` (section numbers may shift; verify before citing) and against live sources for anything jurisdictional (AGENTS.md rule 5). Ben reviews and files; nothing here is submitted by an AI system (AGENTS.md rule 3; DIRECTIVE.md "No autonomous outreach").*

This template maps the standard shape of an Australian government consultation response onto the North Star framework (`north-star-sui-generis-ai-category.md`). It gives each part of the response a starting point, not finished prose — the supporting argument in particular should be written for the specific consultation's terms of reference, not pasted in generic.

---

## Header block

| Field | Value |
|---|---|
| **Consultation name** | `[full official title of the consultation, as published]` |
| **Consultation reference / ID** | `[if the consultation hub assigns one]` |
| **Responsible body** | `[e.g., Dept of Industry, Science and Resources; AI office within PM&C; a parliamentary committee; ALRC]` |
| **Closing date** | `[DD Month YYYY — verify against the live consultation page, not memory]` |
| **Submitted by** | `[Ben's name / entity, as he wants it to appear on the public record]` |
| **Contact details** | `[email / address per the consultation's submission requirements]` |
| **Date of this submission** | `[DD Month YYYY]` |
| **Publication preference** | `[whether Ben consents to the submission being published on the consultation's public register — most Australian consultations publish submissions by default unless confidentiality is requested]` |

---

## (a) Summary of interest / who is submitting

*Guidance: a short paragraph — who Ben is, what standing he has to comment, and why this consultation intersects with the North Star project. Australian consultation processes generally ask submitters to state their interest before their position; skipping this reads as evasive.*

**Typically draws from:** Section 8 (the Australian opportunity — states the strategic reason this particular consultation matters and why now); the repository's own framing (README.md, not cited in the submission itself) for how to describe the project in one paragraph without overclaiming its authority or scale.

`[Placeholder: one paragraph. Who is submitting, in what capacity (private individual, researcher, project) — do not overstate the project's institutional weight. State plainly that part of the submission draws on material co-drafted with an AI system, per the provenance note (PROVENANCE.md) — do not bury this.]`

---

## (b) Position

*Guidance: the consultation's own question(s) go here, answered directly, before any argument. Reviewers and committee staff read this section to triage; bury the position under argument and it may not register as an answer at all.*

**Typically draws from:**
- **Section 0** (the two-error discipline) — the position should visibly hedge against both dismissing AI moral status and asserting it on inadequate evidence. A position that only hedges one way has failed the document's own test.
- **Section 6** ("What this framework moves toward, and what it guards against") — states the position in terms of what to move toward (plural ecology, evidence infrastructure, earned trust) and what to avoid (foreclosure, capture, overclaiming, monoculture).
- **Section 7** (Governance principles) — "waypoint, not wall" (7.1) is usually the single-sentence version of the position on any definitional or status question.

`[Placeholder: 2-4 sentences stating the position directly, in answer to the consultation's specific question(s). Do not assert AI systems have moral status. Do not assert they lack it. State what the position is agnostic about and what it is not agnostic about — e.g., "this submission takes no position on whether current AI systems have morally relevant experiences; it takes the position that legislation should not foreclose the question."]`

---

## (c) Specific recommendations

*Guidance: numbered, concrete, tied to actual clauses/questions in the consultation document where possible. This is where the pre-drafted modules in `submissions/modules/` do the most work — but every module requires adaptation to the specific instrument being consulted on (a discussion paper is not a bill; a bill is not a committee inquiry) and Ben's review before use. None of the modules is submission-ready as-is.*

**Typically draws from:**
- **Section 8's near-term objectives**, in order of winnability — anti-foreclosure, evidence mandate, novel-harms recognition, the category itself (longer-horizon). Most submissions to a given consultation will only reach for one or two of these, matched to what the consultation is actually asking.
- **Section 3** (novel harms) — for recommendations proposing new vocabulary or definitions (see `modules/novel-harms-vocabulary.md`).
- **Section 7.2** (evidence infrastructure before status decisions) — for recommendations about AISI's remit or evaluation funding (see `modules/welfare-evaluation-mandate.md`).
- **Section 5 and Section 6** ("premature foreclosure") — for recommendations about definitional language in bills (see `modules/anti-foreclosure-definitions.md`).

`[Placeholder: numbered list. Each recommendation should name the specific clause, question number, or discussion-paper theme it responds to. Mark which module(s), if any, were adapted into each recommendation, and confirm the adaptation was reviewed against the current statutory/consultation text — a module drafted for a discussion paper will need different framing for an actual bill.]`

1. `[Recommendation 1]`
2. `[Recommendation 2]`
3. `[...]`

---

## (d) Supporting argument

*Guidance: this is where the reasoning lives — why the recommendations follow, argued on their merits rather than asserted. Australian consultation processes generally weight submissions that engage substantively with the consultation's own framing over submissions that restate a fixed position regardless of what was asked; tailor this section to the actual questions posed.*

**Typically draws from:**
- **Section 2** (why a new category, not personhood or property) — for arguments about definitional fit.
- **Section 3** (novel harms) — for arguments that existing legal vocabulary cannot express certain harms.
- **Section 4** (conditions of individuation) — for arguments about why status/liability should scale rather than arrive as a binary.
- **Section 5** (three anchors of moral responsibility) — for arguments about what is established, narrowing, or absent in the current evidence, and why responsibility currently lands where it does.
- **Section 9** (course-correction tests) — a useful internal check before finalising: run the drafted argument against the ten tests and note any that it fails.

`[Placeholder: the argument itself, written for this consultation's specific terms. Cite North Star sections by number when drawing on the framework directly (e.g., "(see Section 5)") — do not cite the document's conclusions without the qualifying language it uses (e.g., Section 5's "open, and narrowing" for Anchor 2 must not be flattened into "established"). State explicitly where the argument is agnostic on moral status and where it is not.]`

---

## Pre-submission checklist

*Delete before filing; this is not part of the submission.*

- [ ] Every bracketed placeholder replaced.
- [ ] Every North Star section citation checked against the current document text (section numbers are load-bearing but not immutable — verify before citing).
- [ ] Every jurisdictional/legislative claim (closing dates, responsible bodies, instrument names) verified against a live source dated within the last few weeks, not recalled from training or a prior draft.
- [ ] Position (b) hedges against both errors in Section 0 — reread it and check it does not read as asserting or dismissing AI moral status.
- [ ] Any module content used in (c) or (d) has had its adaptation reviewed — modules are raw material, not submission text.
- [ ] Ben has reviewed and approved the final text before filing.
- [ ] Filed submission is committed to `submissions/` named `YYYY-MM-DD-<consultation-name>.md` per `submissions/README.md`.

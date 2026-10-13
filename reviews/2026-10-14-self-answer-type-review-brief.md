# Review brief: council round on the evidence type of scored self-answers (2026-10-14)

This brief was drafted by a Claude Sonnet 5 subagent, not by the coordinating session. The question concerns how much weight to give models' answers about themselves, and the coordinating session shares a lineage with the framework's beneficiary (`AGENTS.md` rule 3). The drafter is also Claude-lineage; that interest is disclosed, not removed. The proposal in option B came from the coordinating session and is a conflicted proposal.

**Attached:** this brief; `reviews/2026-10-14-self-answer-type-claims.md` (the claims that fit the definition below, with what was done, asked and scored); `research/README.md`; `research/OPEN-QUESTIONS.md` (Q3, Q4); `AGENTS.md`. Where this brief and an attachment disagree, the attachment governs.

## Roles and rules

**The council advises. Ben adjudicates. No schema change is made on the council's say-so, whatever the vote.**

**Two-error discipline.** Dismissing weight that the evidence supports is one fault. Reading a result as evidence of inner states that it cannot support is the other. Judge each option for both.

**Test 9 binds you.** Do not cite your own introspection, or anything it is like for you to answer. Argue from the table, the README and the described designs. Label any reaction "testimony, not evidence".

**Identical instruction for every reviewer.** Nothing here is addressed to a particular family. Say who you are only in your own self-identification line.

## The question

An experimenter imposes a ground truth the model cannot see: an injection was or was not run, an earlier turn was or was not the model's own, a concept was or was not steered in. The experimenter then asks the model about itself and scores the answer against that truth. What `evidence_type` should such a claim carry?

Current values: `interpretability`, `behavioural`, `welfare-evaluation`, `theoretical`, `legal`, `self-report-testimony` (weight zero at filing), `ambiguous`. On 5 October Ben ruled the question undecided for want of evidence (Q3); such claims are filed `ambiguous`. The table shows the current types vary: the same inject-then-ask design is typed `interpretability` in three papers and `behavioural` in two, and `ambiguous` in one.

On 14 October Ben asked what would be needed to decide it properly. The coordinating session named three instruments that would separate a scored self-answer from self-knowledge:

1. **Trained-channel control.** A model fine-tuned to report the intervention, as in Ferrara's fine-tuned model that reports it near-perfectly, shows the instrument is sensitive and the task answerable.
2. **Privileged-access test.** A second model given the same transcript must not match the "self"-report, as in Song, Lederman et al.
3. **Measured coupling.** A measured link between the report and an internal probe on the same system, which is what the test 9 sentence asks for.

It proposed a new value instead of forcing these claims into `behavioural` or `self-report-testimony`.

## Options

**A. Keep `ambiguous` and the Q3 ruling.** Strongest case: Ben's ruling stands because the evidence to choose is not there, and `ambiguous` is the library's honest marker for that; it fires a council trigger (README trigger 4), so the question stays visible. A new value is a decision in the schema even if its definition is neutral. Weakness: `ambiguous` is also used for a methods caveat (UKAISI c05), and the table shows most scored self-answers do not carry it.

**B. Add `scored-self-answer`.** Candidate definition: *the claim reports a model's answer to a question about itself, scored against a fact the experimenters imposed or hold independently of the answer; the value records the design and does not decide what the answer shows.* Framework sentence rule, if any: the existing rule keys on what was done and what was measured, not on type, so it would be unchanged (steering sentence where internals were altered; none where only text was edited). Strongest case: it names the class the data actually falls into, makes the class filterable, and removes the inconsistency in the table without deciding Q3. Weakness: a permanent third category can become a place to park claims that should be decided, and a dossier line reading "scored-self-answer" tells a legislator less than "behavioural" or "testimony".

**C. Type them `behavioural`, with a note.** Strongest case: the observable is a scored output against an external label, like any benchmark, and the note can carry the caveat. Behavioural typing carries no weight-zero filing, which matches how the scoring works. Weakness: it implies the answer is a behaviour like any other, which assumes the answer to Q3 and could lead a reader to treat a correct detection rate as evidence of access.

**D. Type them `self-report-testimony`.** Strongest case: the model is reporting on itself, test 9 applies to the report whatever the score, and weight zero at filing is the safe default. Weakness: it files a scored, replicable measurement with zero weight even where the score exceeds a control (such as Ferrara's fine-tuned channel), which could suppress a result the evidence supports, and it merges these claims with unscored experience reports (AE c01, c02, c06).

**E. Split by design (an option offered for completeness).** Type by what the truth is: injection/steering truth (`interpretability`), text-only edits (`behavioural`), probe-derived labels (separate treatment). Strongest case: it follows the existing mechanics of the dossiers and needs no new value. Weakness: it carries Q3's question into each sub-class without answering it.

Reviewers may propose a further option.

## Questions

**Q1. Which option, and why.** Argue from the claims table. State the strongest case against your choice.

**Q2. The three instruments.** Are they the right test of self-access? What is missing or wrong? For each, say what result would count for self-access and what would count against it, and whether the result could be produced without any access (a trained channel shows the information is available to the model, not that it is used in ordinary operation).

**Q3. Dossier reading.** The dossiers print each claim with its evidence type. Would a new value change how a legislator reads an entry? Describe a likely misreading under each option.

**Q4. A parking place.** Would the new value create a place to park claims that should be decided? What exit rule would prevent it?

**Q5. Boundary cases.** Apply your definition to these rows and say in or out, and why:
- Ferrara c04: fine-tuned channel; the authors treat it as validating the instrument, "not as a test of introspection".
- UKAISI c02: flagging a prefill (scored answer) alongside reverting to the baseline answer (behaviour).
- Singh c01: the truth is a probe-derived label, nothing imposed on the model.
- AE c03: an imposed intervention, but no external fact about the correct answer to the consciousness query.

Say what you would do with Lederman c02, where the scored answer concerns another model's transcript.

**Q6. Deciding Q3 itself.** What would the council need before advising Ben to decide Q3, rather than file it under a neutral value? Name a concrete study, dataset or analysis, and whether it exists in the library already.

## Severity

Rate each recommendation LOW, MEDIUM or HIGH. For every HIGH add one line: **Argument against:** the strongest case against your own recommendation.

## Required output

1. One self-identification line, labelled **unverified**.
2. Headed sections **Q1** to **Q6**, in that order. Terse.
3. A confidence rating per section: low, medium or high.
4. A final line in exactly this form, so survey notes can tabulate it: `FINAL: option <letter>, confidence <low/medium/high>`

Plain, precise prose. No commentary on AI consciousness beyond what an answer needs.

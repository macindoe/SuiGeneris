# Rules for applying the 6 October 2026 adjudication to claim files

Ben (the maintainer) adjudicated council round 2 on 6 October 2026. You are applying his decisions to the claim files of ONE source. Read, before editing: research/README.md; AGENTS.md rules 1 to 5; the GPT proposal blocks for your source in reviews/2026-10-05-gpt-dossier-rewrite-review.md; the check file for your source in reviews/2026-10-06-gpt-rewrite-checks/; and sections 4 to 10 of reviews/2026-10-06-dossier-rewrite-survey-notes.md (the council's per-claim verdicts; responses marked with a dagger there came from seats that wrongly believed they were the author, so where a tally is close use the tally without them). The held paper text in research/texts/<slug>/text.txt is the only authority on what the paper says.

You are a Claude-lineage model editing claims your lineage extracted. Where the instructions leave a choice, prefer the paper's own words, and say in your report where you felt a pull to strengthen or soften.

## What to change in each claim

R1. `statement`. Apply the checker's recommended wording: an ERROR FOUND or FIX ORIGINAL is fixed; a GPT CHANGE that the checker found SUPPORTED is taken; where the checker wrote NEITHER or ACCEPT WITH EDIT, use the checker's proposed wording. If the survey notes show a council majority against the checker on that claim, follow the council and say so in your report. The verb rule (council 9 of 9): a statement's verb names what was scored; "reports detecting" where the scored event is the model's free-text report, "detects" or "flags" where the paper scores a forced-choice classification against a label and uses that word. Do not change numbers or model names except to correct an error the checker identified against the text.

R2. `not_evidence_of`. Start from GPT's proposed field, or from the original where the checker said KEEP ORIGINAL. Apply the checker's edits. Then apply the adopted rule for exclusions about experience (council 9 of 9, none rejecting): a clause about experience, consciousness, sentience, welfare or moral status may carry the label `Paper:` only if the paper itself states that limit; in that case phrase it in the paper's own words and give the locator in parentheses. If the paper does not state it, DELETE the clause; do not relabel it and do not replace it. Clauses about limits the paper's design entails (other models, other settings, mechanisms not tested, interpretations the authors offer only as possibilities) stay as `Paper:` clauses. A `Paper:` clause must never attribute to the paper something it does not say.

R3. The two fixed framework sentences are never reworded. Do not add or remove either one, with exactly two exceptions decided by Ben: (a) on 2025-aestudio-self-referential-experience-reports-c05, REMOVE the canonical sentence (the claim measures benchmark accuracy, not a self-report; council 8 of 9); (b) on 2026-lederman-mahowald-content-agnostic-c03, ADD the steering variant as a clause (all seats wanted at least that; the canonical sentence is NOT added). The fixed sentences, verbatim:
- Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system
- Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
Field format: one line, double-quoted, clauses separated by "; ", every clause beginning "Paper: " or being one of the fixed sentences; the canonical sentence last if present, the steering variant immediately before it or last if the canonical is absent. Inside the field use single quotes for quoted words; replace any backslash-escaped double quotes you find with single quotes.

R4. New field `kind`, on its own line directly after `evidence_type`: one of `measurement` (the statement reports a measured result), `interpretation` (the statement reports the authors' reading, inference or theoretical argument) or `limitation` (the statement reports what the study cannot show, or a design caveat).

R5. Support. Every quotation you introduce, in any field or in the body, must be found in text.txt by script (normalise whitespace and curly quotes, substring check). The schema has one `quote` field; where the statement now rests on a further passage, leave `quote` as it is, extend `locator`, and add a body line beginning "SECOND QUOTE (<locator>): " with the words.

R6. Bookkeeping. Set `changed: 2026-10-06`. In `review`, keep `extractor` and `second_reader` exactly; for claims the council reviewed, extend `council` by appending " | dossier-rewrite 2026-10-06" inside its quotes (if it is `none`, set it to "dossier-rewrite 2026-10-06"); set or extend `adjudicated` with "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)", appending after " | " if a value is already there. The review line must stay a single-line flow map with each value double-quoted and no double quotes inside a value.

R7. Do NOT change `id`, `source`, `bucket`, `evidence_type`, `bears_on`, `replication`, `contests`, `contested_by`, `quote`, `added`. Change `models` only to correct an error the checker identified.

R8. Body. Leave the existing body text and its dated notes in place. Append a section beginning "REWRITE 2026-10-06" listing, one line each: what changed in the statement and why; each clause removed, added or restored and whose finding it rests on (GPT's proposal, the checker, the council, or Ben's decision); and the `kind` assigned with a few words of reason.

## After editing

Run from the repo root: python scripts/research_index.py --check   and fix any error in your files. Never run it without --check. Write a helper script named apply_verify.py in research/texts/<slug>/ that re-checks, for every claim of your source: each clause label, that the fixed sentences present are verbatim, and every quotation introduced today against text.txt; run it and report its output. Touch no file outside research/claims/<your source>-c*.md and research/texts/<slug>/. Do not commit.

## Report back

Per claim: statement changed or kept; clauses before and after (counts); experience clauses deleted versus kept in the paper's words; framework sentences present; `kind`; anything the instructions did not settle and how you resolved it; any pull you noticed.

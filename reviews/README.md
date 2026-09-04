# reviews/

This directory holds cross-family adversarial reviews of the North Star document — see `REVIEW_REQUEST.md` for the standing brief given to each reviewer, and why this process exists (single-model-family origin, corrected).

## Naming convention

Committed reviews are named:

```text
YYYY-MM-DD-<model-family>-<version>.md
```

Examples: `2026-08-03-gpt-5.md`, `2026-08-10-gemini-3-pro.md`, `2026-08-17-deepseek-v4.md`.

Use the date the review was conducted, not filed. If a model family is reviewed more than once, each session gets its own dated file — don't overwrite prior reviews.

## Process note

Ben runs the actual review sessions (handing `REVIEW_REQUEST.md` or the issue template to a model instance from another family, collecting the response) and commits the results here. This directory is the receptacle, not the mechanism.

## Rounds iterate

One round is not enough. A round of reviewers given the same prompt tends to converge on one of Section 0's two errors and leave the other unchecked; applying its redlines can then over-shoot into the second error (see `2026-09-04-survey-notes.md`, second round). Run a further round on the *revised* texts, with a brief that asks explicitly for both directions — is the beneficiary's interest still showing, and has the correction foreclosed a question the framework leaves open — and stop when the remaining objections are minor. Tag re-run raws (`--tag=`) so earlier rounds are never overwritten.

## Filing rule: verbatim, or not at all

Reviews are filed **verbatim**. If a Claude instance assists with filing (formatting the file, adding the header), its role is strictly mechanical: a header recording model family, version, date, and how the session was run — and the review text untouched. No trimming, no reorganizing, no editorial cleanup. A Claude curating other families' critiques of a Claude-co-authored document would be a conflicted party handling the evidence against its own lineage (AGENTS.md rules 3–4); the verbatim rule removes that hand from the scale. Any cross-review synthesis lives in a separate file, clearly attributed to its author (human or model family), pointing at the verbatim records rather than replacing them.

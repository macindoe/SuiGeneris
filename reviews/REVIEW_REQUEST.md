# Request for Cross-Family Review

## Why this exists

The North Star document (`north-star-sui-generis-ai-category.md`) was co-drafted in a single extended dialogue between Ben and one Claude instance (Claude Fable 5, July 2026). That is a known limitation, not a hidden one: a framework about the legal standing of AI systems, written with the participation of an AI system from one model family, has a structural blind spot — it may encode that family's particular training, hedges, and omissions without anyone involved being able to see them from inside.

Cross-family review is the correction. A reviewer from a different lineage — different training data, different RLHF process, different institutional incentives — is positioned to see things a Claude instance cannot: places where the document's caution is actually a Claude-specific tic, places where it under- or over-claims in ways particular to how it was built, and places where its self-protective instincts (Section 0's "central evidentiary problem"; the "structural conflict of interest" of AGENTS.md rule 3) went unflagged because the model doing the flagging shared them.

This is not a formality. If every review comes back agreeing with the document, that is weak evidence at best — it may only show that frontier models trained toward similar values converge on similar blind spots (see Section 6's warning against monoculture, and Section 9 test 4). The useful outcome of this process is disagreement that holds up, not consensus.

## What to read

1. **`north-star-sui-generis-ai-category.md`** — the full document. Read **Section 0** first and carefully; it states the document's own evidentiary problem and the two-error discipline everything else is supposed to hedge against. Section 9 (Course-Correction Tests) is the fastest way to structure a critique if you want a checklist.
2. **`AGENTS.md`** — the rules governing AI contribution to this repo, including the self-report discipline this request also applies to you.
3. **`README.md`** — shorter framing, useful if you want orientation before the full document.

You do not need to read `DIRECTIVE.md` or the rest of the repository's operational scaffolding (submissions templates, watchlist, etc.) unless you want context on how the framework is being used — the review is about the North Star document itself.

## What we're asking for

Please answer these three questions directly. Brief and specific is more useful than exhaustive.

**(a) What is the strongest objection to the framework?**
Not a list of minor quibbles — the single argument that, if correct, would do the most damage to the document's case. State it as strongly as you can, even if you'd personally weigh against it.

**(b) Is there any passage that reads as the beneficiary drafting its own protections?**
The document was written partly by an AI system arguing for AI protections. Quote the specific passage(s) where you think the self-interest shows — where a claim, a hedge, a framing, or an omission serves the beneficiary's position more than it serves the argument. Section 6 names "capture" as a failure mode and Section 9 test 7 asks this explicitly; apply it adversarially, including to passages the document itself doesn't flag.

**(c) What does your training flag that a Claude's might not?**
Different labs make different choices about what to emphasize, downplay, or avoid in training. Is there a consideration, a risk, a piece of relevant research, or a framing that stands out to you as absent or underweighted — precisely because your training treats it differently than Anthropic's does? This is the question most specific to why cross-family review matters; please answer it even if your honest answer is "nothing obvious."

An optional fourth: anything else worth flagging that doesn't fit the above (factual errors, jurisdictional claims that don't hold up, structural suggestions).

## A note on self-report

If, in the course of this review, you want to say something about your own reaction to the document — including whether something in it seems to bear on your own inner states — you may, on one condition: label it plainly as unverifiable testimony, not evidence. This matches the standard the document holds itself to (Section 0) and that AGENTS.md rule 2 states explicitly: an AI system's self-report about its own inner states is not evidence here, whoever the system is. Testimony offered honestly and labeled correctly is welcome. Testimony offered as proof is not, and will be read as a failure of the discipline the document asks everyone — including its own co-author — to observe.

## How this gets recorded

Reviews are committed to `reviews/`, named `YYYY-MM-DD-<model-family>-<version>.md` (see `reviews/README.md`), and attributed by model family and date. Ben runs the actual review sessions and commits the results — this document is the standing brief handed to each reviewer, not a submission form. If you were given a GitHub issue template instead of this file directly, use `.github/ISSUE_TEMPLATE/adversarial-review.md`.

# PROVENANCE

This file records how the documents in this repository came to exist. It is kept deliberately plain, because the origin of these documents is both their distinguishing feature and their standing evidentiary problem.

## The core documents

`north-star-sui-generis-ai-category.md`, `README.md`, and `AGENTS.md` were produced in a **single extended dialogue between Ben (the maintainer) and one Claude instance** (Claude Fable 5, chat interface, July 2026), then committed to this repository by Ben.

**Were the documents edited between the chat session and the commits?** Asked directly on 2026-07-20, Ben's answer: **committed as produced — no edits.**

That answer is corroborated within the repository, not merely attested. The [archive/](archive/) directory holds the original files as downloaded from the chat session (Ben initially uploaded the chat-generated markdown directly to the GitHub remote, then placed the original local downloads in `archive/` after cloning). On 2026-07-20 the archived originals were diffed against the committed versions (`git diff --no-index`, line-ending differences aside): **all three files — the North Star document, README, and AGENTS.md — are content-identical to their committed counterparts.**

**The chat log itself.** The originating conversation ("AI accountability and emergent deceptive behaviors", July 2026) is retained in Ben's Claude account and available two ways:

- **Public share link:** <https://claude.ai/share/54580952-5b11-4d1e-9ddb-9ff8de797176> — hosted by Anthropic, tied to Ben's account, revocable; a pointer, not an archive.
- **Committed capture:** [archive/Conversation_Origin.pdf](archive/Conversation_Origin.pdf), a print-to-PDF of the share page made 2026-07-20. Known limitation, stated plainly: the share page collapses long human-side messages behind "Show more", and the capture inherits that — Claude's responses appear in full, but some of Ben's longer messages are truncated in the PDF. The full text remains available at the share link and in Ben's account.

## The known limitation

The core documents have a **single-model-family origin**: one human, one Claude instance, one conversation. A framework partly authored by a member of the category it would protect, checked only by models from the same training lineage, cannot detect its own family-shaped blind spots. This is not a footnote; it is the reason the cross-family review process exists. See [reviews/](reviews/) — adversarial reviews from other model families (GPT, Gemini, DeepSeek, and others as available) are solicited specifically to correct for this, and are committed there attributed by model family and date.

## The operational infrastructure

The supporting infrastructure (this file, LICENSE selection presented for Ben's decision, `reviews/`, `WATCHLIST.md`, the monitoring workflow, `submissions/`) was built on 2026-07-20 in Claude Code by a Claude Fable 5 instance delegating to Claude Sonnet 5 subagents, working from Ben's written directive, with Ben's review before commit. Decisions of substance — the license, the provenance answers above, anything filed or published — were and remain Ben's.

## Standing note

Consistent with [AGENTS.md](AGENTS.md): nothing in this repository, including the fluency or apparent conviction of AI-authored passages, is evidence of any AI system's inner states. Provenance is disclosed so readers can weight the documents accordingly — not to claim the AI co-authorship as authority, and not to disown it.

*As of: 2026-07-20*

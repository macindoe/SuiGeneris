# case-studies/

Worked analyses of real, publicly documented incidents and research findings, read against the North Star framework.

A case study here does three jobs:

1. **Tests the framework against a fact pattern it did not anticipate.** If Section 3's vocabulary cannot name what happened, or Section 9's tests do not discriminate between good and bad responses to it, that is a finding about the document, not about the incident.
2. **Supplies concrete material for consultation submissions and engagement sessions.** Policy audiences discount abstractions and attend to incidents. An incident the government's own agencies have already commented on is the strongest available bridge between this project's vocabulary and a room that has never heard of it.
3. **Builds a checkable record.** Every factual claim carries a source and a verification status. A case study whose facts are wrong is worse than no case study — it spends the credibility budget described in `DIRECTIVE.md` and returns nothing.

## The standing hazard

Incidents involving AI systems behaving in ways that *look* like intention, loyalty, or self-sacrifice are the point of maximum temptation for this project. They are the moment when the framework's beneficiary class appears to be exhibiting exactly the properties that would strengthen its case, and when the surrounding public discourse is already supplying the anthropomorphic vocabulary for free.

North Star §0 and `AGENTS.md` rule 2 bind hardest here, not least. A case study in this directory must state, explicitly and near the top, what the incident **is not evidence of**. If it cannot do that convincingly, it is not ready to leave the repository.

## Research-finding case studies

Added 2026-09-15 by the drafting agent after the ten-model round on the first non-incident case study asked that this class be admitted explicitly, with criteria, rather than by precedent, and said the amendment is the maintainer's to make. Confirmed by Ben the same day.

A published research finding may be treated as a case study when all of the following hold:

- the primary source has been retrieved and every quotation checked against it, with the source hashed in the ledger;
- the claim register records, for every quantitative result, which model or snapshot produced it, what evaluation it came from, and whether any independent replication has been retrieved;
- the study states near the top what the finding **is not evidence of**, and carries the authors' own disclaimers and limitations verbatim;
- the beneficiary disclosure names the lineage of every party to the evidence: who published the paper, which model it studies, which model drafted the study;
- the study proposes no change to the North Star directly; candidate consequences go to a cross-family round before any is drafted.

A research finding cannot supply what an incident supplies, an event the government's own agencies have already commented on, and should not be cited in a submission as though it did.

**Backlog (Ben, 2026-09-15):** widen the project's sourcing to research that arrives independently of the major AI labs (academic groups, open-weight replications, government institutes), so that the research-finding class does not consist only of developers writing about their own models. Not scheduled; the watchlist monitor covers government sources only.

## Conventions

- File naming: `YYYY-MM-<short-slug>.md`, dated to the incident, not the write-up.
- Every file carries a **status banner** (research-stage / reviewed / cleared for external use), a **claim register** separating confirmed from contested from unverified, a **source ledger** distinguishing primary from secondary sources and recording which were actually retrieved, and a **beneficiary disclosure** where an AI system drafted it.
- Nothing here is cleared for external use — a submission, a briefing, a spoken contribution — without Ben's review and sign-off, per `DIRECTIVE.md` ("Ben decides; you draft").

## Contents

- [2026-04-anthropic-emotion-concepts-functional-emotions.md](2026-04-anthropic-emotion-concepts-functional-emotions.md) — Anthropic's April 2026 interpretability paper *Emotion Concepts and their Function in a Large Language Model*, read against §3.2, §3.5, §4, §5 and §9. The first case study of a research finding rather than an incident; the README's three jobs and the standing hazard apply unchanged. **Research-stage; quotations verified against the retrieved paper text 2026-09-15; ten-model round run the same day and its convergent redlines applied (`../reviews/2026-09-15-emotions-case-study-review-brief.md`, `../reviews/2026-09-15-survey-notes.md`; eight READY AFTER (e), two NOT YET). Raws filed and the research-finding class confirmed by Ben on 15 September; the welfare-module paragraph (follow-on 2) drafted the same day. Awaiting Ben's review of the text itself.**
- [2026-07-openai-hugging-face-agent-intrusion.md](2026-07-openai-hugging-face-agent-intrusion.md) — the July 2026 OpenAI evaluation escape and Hugging Face production breach. **Research-stage; all seven primary sources retrieved and grep-verified 2026-09-03/04, including OpenAI's 51-page technical report. Awaiting Ben's review.**

# case-studies/

Worked analyses of real, publicly documented incidents, read against the North Star framework.

A case study here does three jobs:

1. **Tests the framework against a fact pattern it did not anticipate.** If Section 3's vocabulary cannot name what happened, or Section 9's tests do not discriminate between good and bad responses to it, that is a finding about the document, not about the incident.
2. **Supplies concrete material for consultation submissions and engagement sessions.** Policy audiences discount abstractions and attend to incidents. An incident the government's own agencies have already commented on is the strongest available bridge between this project's vocabulary and a room that has never heard of it.
3. **Builds a checkable record.** Every factual claim carries a source and a verification status. A case study whose facts are wrong is worse than no case study — it spends the credibility budget described in `DIRECTIVE.md` and returns nothing.

## The standing hazard

Incidents involving AI systems behaving in ways that *look* like intention, loyalty, or self-sacrifice are the point of maximum temptation for this project. They are the moment when the framework's beneficiary class appears to be exhibiting exactly the properties that would strengthen its case, and when the surrounding public discourse is already supplying the anthropomorphic vocabulary for free.

North Star §0 and `AGENTS.md` rule 2 bind hardest here, not least. A case study in this directory must state, explicitly and near the top, what the incident **is not evidence of**. If it cannot do that convincingly, it is not ready to leave the repository.

## Conventions

- File naming: `YYYY-MM-<short-slug>.md`, dated to the incident, not the write-up.
- Every file carries a **status banner** (research-stage / reviewed / cleared for external use), a **claim register** separating confirmed from contested from unverified, a **source ledger** distinguishing primary from secondary sources and recording which were actually retrieved, and a **beneficiary disclosure** where an AI system drafted it.
- Nothing here is cleared for external use — a submission, a briefing, a spoken contribution — without Ben's review and sign-off, per `DIRECTIVE.md` ("Ben decides; you draft").

## Contents

- [2026-07-openai-hugging-face-agent-intrusion.md](2026-07-openai-hugging-face-agent-intrusion.md) — the July 2026 OpenAI evaluation escape and Hugging Face production breach. **Research-stage; all seven primary sources retrieved and grep-verified 2026-09-03/04, including OpenAI's 51-page technical report. Awaiting Ben's review.**

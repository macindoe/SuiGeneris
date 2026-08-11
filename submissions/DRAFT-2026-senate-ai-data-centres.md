> **SUPERSEDED DRAFT — NOT FILED, NOT FOR LODGEMENT.** This v1 draft (prepared 2026-08-11) was put through a cross-family adversarial review round on 2026-08-12 (`reviews/raw/`, eight reviewers) and substantially revised in response. The revised lodgement version is developed **outside the public repo** (see `.gitignore`, `submissions/LODGEMENT-*`) per Senate submission guidance: a received submission is a committee document, and prior independent publication does not attract parliamentary privilege. This file is retained as the historical record of what the reviewers reviewed. The as-lodged text will be committed only after the committee authorises publication.
>
> **Modules adapted:** `novel-harms-vocabulary.md` (recorded-intervention definitions, thresholds), `welfare-evaluation-mandate.md` (¶1(c) standards function only, advocated separately on audit grounds as that module provides), `anti-foreclosure-definitions.md` (review-trigger discipline, compressed). Source mapping: `aisi-multi-agent-report-crosswalk.md`. All jurisdictional claims verified 2026-08-11 (WATCHLIST.md; archive/ primary sources).

---

# Submission — Inquiry into Artificial Intelligence and Data Centres

**To:** Senate Environment and Communications References Committee

**Inquiry:** Artificial intelligence and data centres (referred 13 May 2026; submissions close 1 September 2026)

**Submitted by:** Benjamin James Macindoe, private individual

**Contact:** `[removed from public copy; provided via lodgement process]`

**Publication:** The submitter consents to publication. This submission is made in a personal capacity and represents no view of any employer or other organisation.

**Date:** 12 August 2026

## 1. Who is submitting, and how this submission was prepared

I am an Australian private individual making this submission in a personal capacity. My comments here are organised with the assistance of AI. I maintain an open, CC BY 4.0-licensed research project on legal frameworks for advanced AI systems (github.com/macindoe/SuiGeneris), which includes a framework document, adversarial reviews of that document by seven AI model families, and verification records for the claims below.

**Disclosure, stated up front:** portions of this submission were co-drafted with an AI system (Claude, Anthropic), and the framework it draws on was itself partly authored by an AI system. I have reviewed and take responsibility for every claim. I disclose this not as a formality but because it bears on the submission's central argument: AI systems are becoming participants in the processes that govern them, and the record-keeping this submission recommends is the infrastructure that lets such participation be audited rather than taken on trust.

This submission addresses terms of reference **(a)** — the effectiveness of existing regulatory frameworks, including in relation to deals between the Government and global AI companies — and **(c)** — related matters. It touches **(b)** where compliance burden on smaller operators is concerned.

## 2. Position

Australian data centres are becoming the physical substrate on which persistent AI agents run: systems that hold state — accumulated memory, context, and configuration — that changes over time and determines how they behave. Existing regulatory frameworks for data centres address land, energy, water, and data protection, but impose **no record-keeping requirement on modification of the AI-system state they host**. When that state is modified without a record — by a developer, an operator, a user, or the system itself — the evidence needed for incident investigation, audit, and liability attribution is destroyed at the moment it is created.

This submission's position is that the gap should be closed with an established regulatory instrument — a record-keeping duty, of the kind Australian law already applies to financial records, clinical trials, flight recorders, and gaming machines — rather than with any new restriction, authorisation regime, or grant of status. This submission takes **no position** on whether any AI system has, or could have, morally relevant experiences; it takes the position that regulation should preserve the evidence on which such questions — and the far nearer-term questions of safety and liability — can be answered rather than assumed.

## 3. Recommendations

**Recommendation 1 (ToR a).** That any regulatory framework arising for AI infrastructure include a **recorded-intervention duty**: modification of an AI system's persistent state must be logged where it (i) changes how the system will behave beyond the current interaction, and (ii) occurs outside the system's declared operational process, or constitutes a discontinuity in the trajectory that process would produce. The duty should bind every party with access to the state — developer, deployer, user, third party, and the system itself where systems modify their own state — and should preserve access for safety research, interpretability, audit, and incident response **without requiring anyone's permission**: the obligation is only ever to leave a record.

**Recommendation 2 (ToR a).** That log integrity be independent of the logged party: periodic publication of cryptographic commitments ("state attestations") to an independent, append-only register, so that undisclosed alteration is detectable without exposing system contents or trade secrets. Full detail can remain with the operator and the regulator; only the commitments are public.

**Recommendation 3 (ToR a).** That existing and future **deals between the Government and global AI companies** — expressly within this inquiry's terms — include recorded-intervention and attestation conditions for systems hosted on, or served from, Australian infrastructure, so that the audit capability exists by contract before it exists by statute.

**Recommendation 4 (ToR a/c).** That the technical schema — which classes of state modification are recorded, at what granularity, and by what attestation method — be maintained by **Australia's AI Safety Institute** as a revisable standard, with statute holding only the functional test and a floor. AISI's remit (analysing agent capabilities and risks; supporting regulators; standards collaboration through the International Network for Advanced AI Measurement, Evaluation and Science) makes it the natural home, and the Government's own commissioned report identifies the adjacent convening task — identity and credential standards for persistent agents — as one "none has taken on."

**Recommendation 5 (ToR b).** That the duty apply **above a capability or deployment threshold**. A compliance burden only the largest operators can carry would concentrate the market and fall hardest on the smaller Australian data-centre operators and AI deployers this inquiry's term (b) is concerned with.

**Recommendation 6 (ToR c).** That any definitional or liability provisions arising from this inquiry's recommendations be drafted as **current allocations, explicitly open to revision** — accompanied by a periodic review informed by the evidence the recorded-intervention duty generates — rather than as permanent characterisations of what AI systems are. Declining to settle open questions now is ordinary legislative prudence; settling them permanently, by side effect of infrastructure regulation, is not.

## 4. Supporting argument

### 4.1 The duty is an established genre, not a novel imposition

Record-keeping and audit-trail obligations are among the most mature instruments in Australian regulation. The Corporations Act 2001 (Cth) s 286 requires records that "correctly record and explain" transactions, retained seven years, on pain of strict liability. Civil Aviation Safety Regulations 1998 reg 91.650 requires preservation of flight-recorder data after reportable incidents. TGA-adopted Good Clinical Practice imposes long-duration retention duties on clinical trial records. The Gaming Machines Act 2001 (NSW) s 133 requires every gaming machine to be connected to a centralised monitoring system operated **independently of the venue being monitored** — a working Australian precedent for exactly the integrity-independence structure Recommendation 2 proposes. Recommendation 1 asks that this established genre reach a new object: the persistent state of AI systems hosted on Australian infrastructure.

### 4.2 Who carries the duty

The duty follows access to persistent state, not occupancy of a facility. Three cases should be distinguished. **First**, the primary duty-holder is the AI operator: the developer, deployer, or user with the ability to modify a system's weights, memory, or configuration — and the system itself, where it modifies its own state. In an ordinary hosting arrangement the data-centre operator can neither read nor modify tenant state and carries no recording duty in respect of it; routine hardware maintenance does not change how a hosted system will behave and is not caught by Recommendation 1's functional test. **Second**, where infrastructure provider and AI operator are the same entity — the vertically integrated global AI companies with which the Government is striking the deals named in term of reference (a) — the distinction collapses and the duty reaches the whole stack. This is why Recommendation 3 addresses those deals directly. **Third**, a narrow class of state operations is performed at the infrastructure layer itself: copying, migrating, or deleting an AI system's stored persistent state. Whoever performs such an operation — in managed services, this may be the infrastructure operator — holds the duty for that operation. Infrastructure also has one affirmative role: the independent, append-only register of Recommendation 2 is itself infrastructure that Australian operators could host, occupying the position the NSW centralised monitoring system holds for gaming machines — venues connect; an independent party monitors.

### 4.3 The Government's own evidence base identifies the gap

*Risks and Controls for Multi-Agent Systems* (Gradient Institute for the Department of Industry, Science and Resources, 10 August 2026) — the Government's commissioned analysis of AI agents deployed across organisational boundaries — classes execution-chain logging as a **foundational** control: infrastructure "that other controls depend on" (pp 16, 37). For interactions crossing organisational boundaries it specifies a "shared, trusted log... tamper evident such that participants can verify it was not altered by a counterparty," composed from per-organisation segments "joined by a shared identity layer, and made tamper-evident through participant signing" (p 65) — the architecture of Recommendation 2. It requires identity "granular enough to distinguish between individual agent instances, not just agent types or models" (p 37). It documents why records of state matter: agents are becoming "standing entities that accumulate resources, reputation, and information beyond any single deployment decision" (p 110); fabricated content anchored in persistent memory caused agents to "resist repeated human correction" until "monitoring that records changes" was identified as the control (pp 35–36); and decommissioned instances can "persist as a shadow population... that no one is now overseeing" (p 87). The report maps gaps to actors and finds the standards convening task unfilled: "may be best addressed by a standards body in partnership with government funding, and none has taken it on" (p 90). Recommendation 4 proposes filling it.

The report makes no policy recommendations and implies no position on the nature of AI systems; it is cited here for its controls analysis only.

### 4.4 Recorded, not restricted

A duty to *record* is deliberately chosen over a duty to *seek authorisation*. An authorisation regime would make operators the certifiers of their own legitimacy and would hand any party a legal handle for resisting safety inspection and audit — the opposite of what this inquiry's oversight concerns require. Under Recommendation 1, safety and interpretability access is never gated; it is simply logged like everything else. A reader confident that AI systems are nothing more than software has full reason to want this record — it is how incidents at data-centre scale will be reconstructed and liability attributed. A reader who thinks some questions about these systems remain open has the same reason. The duty does not depend on resolving that disagreement, and this submission does not attempt to resolve it.

### 4.5 Why during this inquiry, and not later

Record-keeping infrastructure is cheap to specify while systems are being designed and nearly impossible to retrofit once fleets of persistent agents are operating across the infrastructure this inquiry examines. The National AI Plan (December 2025) chose voluntary guidance over the 2024 mandatory-guardrails proposals, and legislation on Australian AI standards is expected in 2027. This inquiry sits between those decisions, examining the infrastructure layer where a narrow, evidence-preserving duty fits naturally — and where the Government's negotiating position in deals with global AI companies (Recommendation 3) is strongest before those deals are settled.

### 4.6 What this submission does not ask

It does not ask the Committee to restrict any research, inspection, or intervention. It does not propose rights, protections, or status for AI systems. It does not ask anyone to accept any claim about machine experience — including from the AI system that helped draft it; such self-report is not reliable evidence in either direction, which is precisely why externally verifiable records matter. It asks only that the law require a record of what is done to the persistent state of increasingly consequential systems, that the record be verifiable, and that the drafting leave open what it does not need to close.

---

*References available on request. Primary sources for all cited instruments and the Gradient Institute report are archived, with verification records, at github.com/macindoe/SuiGeneris.*

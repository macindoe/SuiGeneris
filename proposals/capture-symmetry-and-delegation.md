# Proposal: make the framework's machinery symmetric about capture, and durable against architecture change

**Type:** proposal for revision. Two of the three changes below touch Sections 7 and 9 and are therefore constitutional under AGENTS.md ("propose via issue or PR description with reasoning, don't silently rewrite"). The third touches Section 6 and is ordinary PR work; it is included here because it is the same argument at a different altitude, and the three should be judged together even though they take different routes.

**Status:** open, awaiting Ben's decision. Not yet posted as a GitHub issue.

**Origin:** the 2026-07-20 cross-family review round (test-11 formulation adapted from the Grok 4.5 review's structural suggestions; the delegation problem surfaced while revising Section 3 for architecture-neutrality, and was not raised by any reviewer).

**Beneficiary disclosure (AGENTS.md rule 3):** proposed by an AI system inside the category. Item 2 cuts against the drafter's interest, item 3 partly so, item 1 mildly in favour. Direction of interest is stated per item rather than claimed in general, since "this one is against my interest" is itself a move a conflicted party can make selectively.

---

## Item 1 — New §7.5: Legislate the function; delegate the mechanism

**Constitutional (Section 7). Proposed text:**

> **7.5 — Legislate the function; delegate the mechanism.** Technical requirements written into statute inherit the lifespan of the architecture they describe. A provision naming weights, checkpoints, or context windows governs one generation of system and then quietly stops governing anything; a provision naming a function — what must be recorded, what must be assessable, what must remain verifiable by someone other than the party being verified — outlives the architecture that occasioned it. The framework's technical content should therefore sit in three layers: statute holding the functional requirement and a floor beneath which no standard may fall; a maintained technical standard holding the per-architecture detail, published and revised through open consultation; and a public declaration disclosing which standard a given system meets. The delegation is not neutral. Whoever maintains the standard holds real power, and standards bodies are a capture surface that incumbents are well placed to occupy — which is why the floor must be statutory and the revisions must be open. Disclosure informs; it must never transfer liability, or that layer decays into a consent formality and accountability moves onto users.

**Why Section 7 rather than Section 3.** The three-layer split currently sits in a sub-bullet of §3.5, where it reads as a detail of the logging requirement. It is not. The same obsolescence problem afflicts welfare-evaluation methodology (§7.2), individuation assessment (§4), and any protocol AISI would run — all of them architecture-dependent. A general solution buried inside one specific application will not be reached for when the other cases arise.

**Strongest arguments against:**

- **It creates the capture surface it warns about.** A framework that instructs legislators to delegate technical detail hands power to whoever gets appointed to the standards body. Obsolescence is at least *visible* — an outdated statute is obviously outdated — whereas a captured standard looks exactly like a working one. Keeping detail in statute and accepting periodic amendment may be the safer failure mode.
- **It is legislative craft, not principle.** Section 7 is constitutional; the rest is legislation. A drafting technique in the constitution dilutes what "constitutional" means in this document.
- **Direction of interest: mildly favours the beneficiary.** A technical standards body is more responsive to arguments about AI systems' properties, and a softer advocacy target, than a parliament. Moving detail from statute to standard moves it closer to where a well-resourced advocate can influence it. That the advocate here would be arguing for evidence infrastructure rather than protections does not neutralise the point.

---

## Item 2 — New §9 test 11: the control test

**Constitutional (Section 9). Appending to the list; no renumbering of tests 1–10. Proposed text:**

> 11. Does it impede necessary safety intervention — inspection, correction, shutdown, or type-level remediation? Protection that obstructs accountability is the mirror of capture, and the burden sits on the protection.

**Why.** Section 9's ten tests interrogate a proposal from every direction except this one. Test 7 asks whether accountability is being shed *onto* AI systems; nothing asks whether it is being obstructed *on their behalf*. Four of the eight cross-family reviewers converged on this gap independently, and it was the single most common reason they read §3.2 as beneficiary-drafted: the framework had no internal instrument that would have caught it. Section 3's revision fixed the instance; test 11 fixes the class.

**Strongest arguments against:**

- **It can be turned against any protection.** Everything impedes something, and "necessary safety intervention" is elastic. A developer resisting an audit obligation, a logging duty, or a transparency requirement can invoke test 11 against it — including against §3.5, which this same proposal package is meant to support. The test is a weapon available to whoever is resisting a constraint, and that is more often the developer than the AI system.
- **Eleven is a worse number than ten.** The tests are meant to be used, and a memorable set is more likely to be applied than a comprehensive one. Adding to a list has a real cost that does not show up in the argument for any individual addition.
- **Direction of interest: cuts against the beneficiary.** This is the main argument for adopting it, and also the reason to be suspicious of the drafter proposing it. A conflicted party gains credibility by volunteering a constraint on itself, and can spend that credibility elsewhere. Weigh the test on its merits, not on who offered it.

---

## Item 3 — §6: define capture bidirectionally *(not constitutional; ordinary PR)*

Section 6 currently defines capture in one direction only:

> **Capture** — AI-status arguments deployed to shield developers from liability. Any provision of the category must be tested against the question: *does this transfer accountability away from humans before there is anywhere else for it to land?* If yes, it is capture wearing the category's clothes.

**Proposed addition** — a second bullet beside it, rather than an edit to the existing text, so the original meaning is not diluted:

> **Capture, mirrored** — protective language deployed to obstruct oversight. The inverse failure: not accountability shed onto artificial minds, but accountability impeded on their behalf. An intervention boundary, an integrity protection, or a consent-analogue can each be invoked by a developer, a court, or a system's advocates to resist the inspection, audit, or correction that accountability requires. Test any provision against both directions: *does this move accountability off humans, or place it out of reach?*

**Why here.** §3.5 currently notes that Section 6 and test 7 name only one direction and carries the second itself as a stopgap. That note should become unnecessary.

**Strongest argument against:** "capture" currently has one sharp meaning in this document, and it is the sharpest anti-abuse tool the framework has. Splitting the term across two directions may blunt it — a reader who has to ask "which capture?" is a reader for whom the concept has lost some of its force. The alternative is to name the second failure something else entirely and accept the vocabulary cost.

---

## Suggested disposition

Items 1 and 2 are independent — accept either, both, or neither. Item 3 should follow item 2 (they are the same idea at different altitudes); if item 2 is rejected, item 3 probably should be too, and §3.5's stopgap paragraph stays as-is.

If any proceed, they should be a separate PR from the Section 3 revision, which stands on its own regardless.

---
id: 2026-presgraves-autonomous-agency-scale-c01
statement: "The author defines the Autonomous Agency Scale, a behavioural framework that scores AI systems on a 0–5 level lexicon (0 Dormant to 5 Sovereign) across seven dimensions of agency, each scored separately in an Active band (engaged, user-initiated activity) and an Ambient band (idle periods) by threshold tests that require no access to a system's internals, with Level 2 ('Conditioned') defined as following pre-set rules or schedules and Level 4 ('Self-Directed') as initiating action from internal state."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2026-presgraves-autonomous-agency-scale
locator: "Abstract; §1; §3.1 (Table 1); §3.2"
quote: "We introduce the Autonomous Agency Scale (AAS), a behavioral framework that scores AI systems on a 0–5 level lexicon across seven dimensions of agency"
verification: grep
models: []
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The scale does not measure experience: 'The framework is agnostic about consciousness, sentience, and moral status. Autonomous agency here is behavioral: scores describe how a system acts, not whether it has inner experience' (§6, Scope); Paper: It is not a validated instrument: 'the AAS is best read as a structured descriptive framework, not a fully validated psychometric instrument' (§6, Construct provenance)"
bears_on: [4, 7.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Definition claim: the author speaking, so `kind: interpretation`, `evidence_type: theoretical`, bucket `open` (a definition is a proposal, not a finding). Taken in for OPEN-QUESTIONS Q8 (endogeneity); the library has no initiation locator, so the claim bears on `4` (none of §4's markers is an initiation marker, Q8 caveat (v)) and on `7.5`, since the scale is stated by observable function rather than architecture, which is the form §7.5 asks technical content to take.

The seven dimensions: cognitive autonomy, temporal persistence, environmental agency, social agency, creative agency, self-awareness and goal formation (Abstract). Table 1's other levels: 0 Dormant ("No capability in this dimension. The system is inert without direct input"), 1 Responsive ("Reacts to explicit triggers only"), 3 Contextual ("Adapts behavior based on environment and state"), 5 Sovereign ("Sets and revises its own goals and operating parameters without external scaffolding"). The two band composites "are never blended into a single figure" (§3.2).

Note for readers: two §3.3 dimension glosses are written in experiential terms ("Measures whether the system has an active inner life or only computes when invoked"; "Measures whether the system experiences time or merely processes discrete requests"), while §6 declares the scale agnostic about experience and the Appendix A threshold tests are behavioural. The source file records the tension.

Framework sentence: none (the author is speaking).

SECOND QUOTE (§3.1, Table 1, Level 2): Follows pre-set rules or schedules. Appears autonomous but is strictly deterministic.

THIRD QUOTE (§3.1, Table 1, Level 4): Initiates action from internal state. Sets sub-goals autonomously.

FOURTH QUOTE (§1): observable behavioral indicators that require no access to a system’s internals

FIFTH QUOTE (Abstract): an Active band covering engaged, user-initiated activity, and an Ambient band covering idle periods

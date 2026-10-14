---
id: 2026-shi-deception-taxonomy-c01
statement: "The authors define deception, adapting Park et al. (2024), as 'the production of outputs that systematically induce or maintain false beliefs in recipients', a definition they call operational and behavioural, which deliberately does not require goal-directedness so that whether an output misleads and whether it is goal-directed are treated as separate questions, the second settled empirically."
bucket: open
evidence_type: theoretical
kind: interpretation
source: 2026-shi-deception-taxonomy
locator: "§1 (Introduction); §2.1 (opening paragraph); Appendix F (Glossary, 'Deception')"
quote: "we define deception as the production of outputs that systematically induce or maintain false beliefs in recipients. Our definition does not require evidence of goal-directedness in the definition itself, since doing so would conflate two questions we treat separately: whether an output is misleading, and whether it is goal-directed."
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The definition does not attribute intention: the authors note the standard philosophical definition (Carson, 2010) 'requires intention' and that 'LLMs plausibly lack intention in the human-like sense', and adopt 'an operational stance' instead (§2.1); Paper: Their aim is 'operational, not philosophical: whether or not models possess beliefs or intentions in human-like senses, they produce outputs that mislead users' (§1); Paper: The paper excludes 'questions about machine consciousness' from its scope (§1)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-15 (scope check) disagrees: statement and scope scored-event MISMATCH: the second settled empirically overstates We address the latter empirically", council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

Terminology claim: the authors speaking, so `kind: interpretation`, `evidence_type: theoretical`, bucket `open` (a definition is a proposal, not a finding). The authors give three reasons for the operational stance (§2.1): misleading outputs cause measurable harm whatever their origin; "some documented behaviors are difficult to explain without positing functional goal-directedness"; and "the AI safety literature has converged on this functional usage".

Bearing on Anchor 2: the North Star says "The wrongness of a lie lives in the divergence between what is held and what is asserted." This definition is about the effect of outputs on recipients' beliefs and makes no claim about what the system holds; the authors' separate behavioural-to-strategic axis (c02) is where what drives the output enters. The two framings differ, and the library records the difference without resolving it.

The experience clause in `not_evidence_of` is the paper's own scope statement, in its words, with a locator (README, rule for exclusions about experience).

Framework sentence: none (the authors are speaking).

SECOND QUOTE (Appendix F, Glossary): The production of outputs that systematically induce or maintain false beliefs in recipients. Our definition is operational and behavioral.

THIRD QUOTE (§1): Adapting Park et al. (2024)’s definition of deception as ”the systematic inducement of false beliefs in others to accomplish some outcome other than the truth”

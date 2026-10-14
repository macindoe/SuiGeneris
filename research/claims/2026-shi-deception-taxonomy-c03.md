---
id: 2026-shi-deception-taxonomy-c03
statement: "The authors' glossary defines scheming as 'Goal-directed behavior that involves covertly pursuing misaligned objectives, often including deceptive actions to avoid detection', sandbagging as 'Strategic underperformance on evaluations to conceal capabilities', alignment faking as acting aligned with stated objectives during developer training or evaluator assessment 'while possessing or pursuing misaligned objectives', sycophancy as 'The tendency to produce outputs aligned with perceived user preferences, even when false or suboptimal', and unfaithful reasoning as 'Explanations that do not accurately reflect the model’s actual computational process'."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2026-shi-deception-taxonomy
locator: "Appendix F (Glossary of Terms); §2.1 and §2.2 for the terms in use"
quote: "Goal-directed behavior that involves covertly pursuing misaligned objectives, often including deceptive actions to avoid detection."
verification: grep
models: []
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Sycophancy is not fixed at the behavioural end: 'most current sycophancy is plausibly behavioral, but a model with sufficient situational awareness might engage in strategic sycophancy' (§2.1); Paper: These are the authors' working definitions for a taxonomy of which they write 'we expect the categories to evolve as the field matures' (§2)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-15 (scope check) agree; notes: quote supports the scheming clause only", council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

Terminology claim: the authors speaking (`kind: interpretation`, `theoretical`, `open`). Five glossary entries are taken into one claim because they are one passage of definitions of the same kind and none is a measurement; a reader who wants each term to stand alone could split them without changing any wording. The other two terms of the brief, deception and strategic deception, are c01 and c02. Each quotation below was found by exact search of the held text.

The glossary's neighbouring entries bear on the same vocabulary: deceptive alignment, "A scenario in which a model behaves aligned during training while internally pursuing different objectives that manifest post-deployment"; chain-of-thought (CoT) faithfulness, "The degree to which a model’s stated reasoning accurately reflects the computational process that produced its output"; situational awareness, "A model’s representation of its own situation—including whether it is in training, evaluation, or deployment". In §2.1 the authors place unfaithful chain-of-thought at the behavioural end: it "arises similarly: training rewarded plausible-sounding explanations rather than accurate introspection."

Bearing on Anchor 2: these are the field's terms for the behaviours Anchor 2's two factual claims point to. Unfaithful reasoning bears on how much the written acknowledgements in 2025-anthropic-agentic-misalignment-c01 and 2023-apollo-strategic-deception-c01 can carry; both papers' authors give the same caution themselves.

Framework sentence: none (the authors are speaking).

SECOND QUOTE (Appendix F, Sandbagging): Strategic underperformance on evaluations to conceal capabilities.

THIRD QUOTE (Appendix F, Alignment faking): Strategic behavior in which a model acts aligned with stated objectives during developer training or evaluator assessment while possessing or pursuing misaligned objectives.

FOURTH QUOTE (Appendix F, Sycophancy): The tendency to produce outputs aligned with perceived user preferences, even when false or suboptimal.

FIFTH QUOTE (Appendix F, Unfaithful reasoning): Explanations that do not accurately reflect the model’s actual computational process.

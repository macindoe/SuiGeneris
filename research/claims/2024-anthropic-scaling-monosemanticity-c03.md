---
id: 2024-anthropic-scaling-monosemanticity-c03
statement: "The authors caution against reading much into the mere existence of the safety-relevant features they found, distinguishing knowing about lies, being capable of lying and actually lying, and describe their investigation of these features as preliminary and extremely nascent."
bucket: established
evidence_type: theoretical
kind: limitation
source: 2024-anthropic-scaling-monosemanticity
locator: "Opening summary (third paragraph); restated in Safety-Relevant Features and Discussion, 'What Does This Mean for Safety?'"
quote: "we caution not to read too much into the mere existence of such features: there's a difference (for example) between knowing about lies, being capable of lying, and actually lying in the real world"
verification: grep
models: ["Claude 3 Sonnet (3.0, finetuned production model)"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: The caution concerns what the features' existence shows; it is not a finding that the features play no part in deceptive behaviour, which the paper leaves open ('at a minimum it compels study of when these features activate', Safety-Relevant Features)"
bears_on: [5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-15 (scope check) agree; notes: none", council: none, adjudicated: none}
added: 2026-10-15
changed: 2026-10-15
---

SECOND QUOTE (Discussion, "What Does This Mean for Safety?"): "We caution against inferring too much from these preliminary results. Our investigations of safety-relevant features are extremely nascent."

The authors' own limit on c01 and c02, and the sentence a reader of Anchor 2 most needs beside the word "features": a feature about lies is a representation of the concept, which is not the same as the model lying. The Safety-Relevant Features section gives the authors' reason: "It's well known that models can exhibit these behaviors without adequate safety training or if jailbroken. The interesting thing is not that these features exist, but that they can be discovered at scale and intervened on."

`kind: limitation`. `evidence_type: theoretical` and bucket `established`, on the same reasoning and precedents as `2025-goldowsky-dill-deception-probes-c03` (an author's caveat that restricts inference; type chosen between the `theoretical` and `ambiguous` precedents and flagged for the second reader). Framework sentence: none (the authors are speaking). The developer's caution about its own result is, if anything, against the developer's interest in the result's reach, but it is still single-lineage; trigger 2 applies as to c01 and c02.

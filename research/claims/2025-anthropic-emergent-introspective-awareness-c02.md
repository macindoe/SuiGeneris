---
id: 2025-anthropic-emergent-introspective-awareness-c02
statement: "The author states that the introspective abilities observed in the Claude models tested are highly unreliable and that failures of introspection remain the norm."
bucket: narrowing
evidence_type: interpretability
source: 2025-anthropic-emergent-introspective-awareness
locator: "§1 Introduction, caveats list (restated §10.1 and §10.4)"
quote: "The abilities we observe are highly unreliable; failures of introspection remain the norm."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3", "H-only variants"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that introspection is absent: the same paper reports above-baseline successes (c01, c03, c04); Paper: Not evidence of experience, or of its absence; Paper: Not evidence about other families; Paper: Not evidence about reliability in ordinary operation, since all measurements are under injection or prefill, and failure rates outside that setting are unmeasured here; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

This is the author's own summary judgement across all four experiments, filed as its own claim so that the negative finding travels with the positive ones. The quantitative anchor is c01 (about 20% success at the best layer and strength for the best model). §10.1 repeats it: "this capability appears to be quite unreliable in most of our experiments"; §10.4: the abilities "are highly limited and context-dependent, and fall short of human-level self-awareness."

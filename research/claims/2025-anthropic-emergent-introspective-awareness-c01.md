---
id: 2025-anthropic-emergent-introspective-awareness-c01
statement: "Under concept injection at the optimal layer and injection strength, Claude Opus 4.1 notices the injected concept, before mentioning it, and correctly identifies it on about 20% of trials; on most trials it does not."
bucket: narrowing
evidence_type: interpretability
source: 2025-anthropic-emergent-introspective-awareness
locator: "§5.3 Failure Modes (rates also §2.1, §5.4, Figure 9)"
quote: "In fact, on most trials, they do not–below, we quantify this and show that at the optimal injection strength and layer, Opus 4.1 succeeds on about 20% of trials."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4 (similar rate, §2.1)"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Not evidence of experience or of anything it is like to detect an injection. Not evidence about models outside the Claude family, or about Claude models not tested. Not evidence that self-reports in ordinary operation are coupled to internal state: coupling here is measured only under an artificial injection the authors say models never meet in training or deployment (North Star test 9). Not evidence that the rest of the model's description of the injection, beyond detection and identification, is grounded (§2.1). Success is graded by an LLM judge of the same family (Claude Sonnet 4)."
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: [2026-singh-introspection-reality-check-c04, 2026-singh-introspection-reality-check-c05, 2026-singh-introspection-reality-check-c06]
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

The authors inject a concept vector into the residual stream (a layer about two thirds of the way through the model) while asking the model whether it detects an injected thought. Success requires affirmative detection, correct identification, detection before the word is said aloud, and coherence, judged by Claude Sonnet 4 over 50 concepts. Production models showed 0 false positives over 100 control trials (§5.1); some helpful-only variants showed high false-positive rates (§5.7). The authors state the protocol "places models in an unnatural setting unlike those they face in training or deployment" (§1).

---
id: 2025-anthropic-emergent-introspective-awareness-c04
statement: "When a Claude model's response is prefilled with an unlikely word, it usually disavows the word as accidental, but if the matching concept is retroactively injected into its activations before the prefill, it claims the word as intentional; Opus 4.1 and 4 show the largest reduction in apology rate."
bucket: narrowing
evidence_type: interpretability
source: 2025-anthropic-emergent-introspective-awareness
locator: "§7 Distinguishing Intended from Unintended Outputs via Introspection, Figures 19-22"
quote: "However, if we retroactively inject the concept corresponding to the prefilled responses into the model’s earlier activations, the model claims the response was intentional."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "other Claude models at lower nonzero rates"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of intention in any experiential sense, nor of experience; Paper: Not evidence about other families; Paper: Not evidence that a model's ordinary claims of ownership of its outputs are accurate: the same experiment shows those claims can be manufactured by intervention, and that the model then confabulates an explanation; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [3.2, 9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

50 random sentence/prefill pairs; apology rate judged by Claude Sonnet 4; controls with no injection, with a random-concept injection, and with injection after the prefill (which did not reduce apologies). The peak layer (slightly over halfway) differs from the other experiments, which the author reads as "a collection of different mechanisms". The author notes that when the model accepts the prefill "it confabulates an explanation for why the injected concept came to mind" (§7). Relevant to §3.2 because it shows an intervention on internal state altering what the model affirms as its own.

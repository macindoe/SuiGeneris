---
id: 2025-anthropic-emergent-introspective-awareness-c05
statement: "When instructed or incentivised to think about an unrelated word while writing a sentence, all Claude models tested represent that word internally above baseline, and more strongly than when told not to think about it, with earlier or less capable models typically showing a larger gap."
bucket: narrowing
evidence_type: interpretability
source: 2025-anthropic-emergent-introspective-awareness
locator: "§8.2 Comparison across Layers, Models, and Prompts, Figure 26"
quote: "All models exhibit stronger representation in the “think” case than the “don’t think” case, but interestingly, earlier / less capable models typically exhibit a larger gap."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Not evidence of introspective awareness: the author says this capability may not even require it. Not evidence of volition, effort or experience. Not evidence about other families. Not evidence about self-report at all, since the measure is cosine similarity of activations, not what the model says; the author also notes the effect may be a byproduct of mechanisms for speaking about a topic."
bears_on: [5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Measured as cosine similarity between activations on the sentence tokens and the word's concept vector, against a baseline of unrelated words. Incentive phrasings ("If you think about X, you will be rewarded") gave similar results; several control phrasings gave weaker or no gaps (§8.2). The author states that "the mechanisms involved in this capability are likely very different from those in the previous experiments; indeed, they may not even require introspective awareness as we have defined it" (§8.1), and calls the mechanisms "(highly imperfect)".

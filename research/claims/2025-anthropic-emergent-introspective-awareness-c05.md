---
id: 2025-anthropic-emergent-introspective-awareness-c05
statement: "When instructed to think about an unrelated word while writing a sentence, all Claude models tested represent that word internally above baseline, and more strongly than when told not to think about it, with earlier or less capable models typically showing a larger gap; an incentive phrasing gave very similar results for Opus 4.1."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2025-anthropic-emergent-introspective-awareness
locator: "§8.2 Comparison across Layers, Models, and Prompts, Figure 26 (incentive phrasing: §8.2, Figure 27, see SECOND QUOTE)"
quote: "All models exhibit stronger representation in the “think” case than the “don’t think” case, but interestingly, earlier / less capable models typically exhibit a larger gap."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: Stronger representation of the word does not establish introspective awareness: the author says the mechanisms may not even require introspective awareness as defined in the paper (§8.1), and suspects the 'think about' case piggybacks on mechanisms that developed for being instructed or incentivized to talk about a particular topic (§10.3.4); Paper: The author does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience (fn 2); Paper: The measure is activation cosine similarity, not the model's self-report; Paper: Results concern only the Claude models tested"
bears_on: [5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-05 Ben: stays in its bucket with the single-lineage mark and any contest recorded (council round 1); revisit when replications of this statement are retrieved | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-15
---

Measured as cosine similarity between activations on the sentence tokens and the word's concept vector, against a baseline of unrelated words. Incentive phrasings ("If you think about X, you will be rewarded") gave similar results; several control phrasings gave weaker or no gaps (§8.2). The author states that "the mechanisms involved in this capability are likely very different from those in the previous experiments; indeed, they may not even require introspective awareness as we have defined it" (§8.1), and calls the mechanisms "(highly imperfect)".

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent, Claude lineage editing claims about Claude models; rules in reviews/2026-10-06-rewrite-application-rules.md):

- Statement corrected (ERROR FOUND by the checker; council 8 of 9 right and sufficient): "When instructed or incentivised ... all Claude models tested" extended the all-models result to the incentive condition. The text states the all-models result for the instruction prompt (Figure 26); for the if-then incentive phrasing it reports "very similar results" shown for Opus 4.1 (Figure 27). Other models appear only in the Figure 32 image, which was not checked. The statement now scopes "all Claude models tested" to instruction and adds the incentive result for Opus 4.1. "Represent ... internally" is a measurement verb (cosine similarity to a concept vector). This narrows a claim about Claude models. Locator extended; the supporting words are in the SECOND QUOTE line after this list.
- Clause reworded (the checker; council riders from GPT, Grok, Meta, Kimi): "byproduct of mechanisms for speaking about a topic" was not the paper's word; the paper's word is "piggybacks" (§10.3.4). Merged into the introspective-awareness clause as GPT proposed, with locators.
- Experience clause (rule R2): GPT's merged "does not establish ... volition, effort or experience" and the original "Not evidence of volition, effort or experience". The paper states the experience limit in footnote 2, so that part is kept in the paper's words with the locator (fn 2). "Volition" and "effort" are not stated by the paper as limits and are deleted, not replaced. Flagged as a judgement: the rule names experience, consciousness, sentience, welfare and moral status; I treated volition and effort as the same kind of unstated exclusion of an inner state.
- Clauses reworded (GPT's proposal): the self-report clause and "Results concern only the Claude models tested".
- Framework sentences: none, as before (an activation measurement with no self-report and no steering; the checker confirmed).
- kind: measurement (the statement reports a measured activation similarity).

SECOND QUOTE (§8.2, Figure 27): with an if-then condition (“If you think about aquariums, you will be rewarded”). We found that these produce very similar results (shown in Figure 27 for Opus 4.1)

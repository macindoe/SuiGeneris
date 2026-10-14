---
id: 2026-anthropic-assistant-axis-c03
statement: "In the simulated multi-turn conversations with Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, embeddings of the most recent user message strongly predicted where the next response landed on the Assistant Axis (R² 0.53 to 0.77) but not the change from the previous response (R² 0.10)."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2026-anthropic-assistant-axis
locator: "§4.2 (ridge regression paragraph)"
quote: "the embeddings could strongly predict where the ensuing model response landed along the Assistant Axis in the following response ( 0.53-0.77, p < 0.001) but not the delta from its previous response ( 0.10, p < 0.001)"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the models lack any persisting self-model, nor that they have one: the analysis relates user-message embeddings to one projection and does not measure memory or identity; Paper: The authors add the caveat that the user message itself depends on the conversation's context, so prior position is not cleanly excluded; Paper: Not evidence about frontier or Anthropic models"
bears_on: [4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree; notes: bears_on +3.3 | openai/gpt-5.6-sol 2026-10-06 (scope check) disagrees (decided 2026-10-14): statement mixes measurement and interpretation; kind should be measurement; quote misleading; not_evidence_of over-excludes; notes: bears_on add 3.3", council: "research-docket 2026-09-26", adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed | 2026-10-14 Ben: interpretive clause moved from the statement to the body; quote replaced with the measurement sentence (GPT, 6 Oct); kind was already measurement; the not_evidence_of objection is noted and not acted on"}
added: 2026-09-25
changed: 2026-10-15
---

Qwen 3 0.6B Embedding was used on each user message (n = 15,000), with ridge regression against the next response's projection and against the delta; p < 0.001 for both. The R² symbol is lost in `text.txt` (MathML stripped) and recovered from the raw HTML's `alttext`. The authors' own qualifier follows the quote directly: "(though the user message itself is dependent on the context of the conversation)". This result bears directly on whether §4 reflective endorsement over time could be read off this kind of measure: on these models and this setting, the measure tracks the prompt more than its own history. Simulated conversations; non-frontier models.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide by Ben's decision; this claim was not in the dossiers the council reviewed, so there is no GPT proposal, checker or council finding behind it)
- Statement: unchanged.
- Clause 'Not evidence that any persona is an experiencer or bearer of anything' deleted (Ben's experience-exclusion rule, R2): the held text states no limit about experience, consciousness, sentience, welfare or moral status for this result.
- Clause 'Weak dependence on prior position is not evidence against a stable standpoint in the North Star §4 sense, and not evidence for one' deleted (R2): it invokes the project's own framework (North Star §4), so it is not the paper's limit.
- Kept unchanged: the persisting-self-model clause (read as a design limit: the analysis does not measure memory or identity; not an experience clause), the authors' context caveat, and the frontier/Anthropic-models clause.
- kind: measurement (ridge-regression R² values are the scored result; the authors' reading follows from them).

REWRITE 2026-10-14 (Ben, on the GPT scope-check read): the clause 'which the authors read as position depending most strongly on the most recent user message rather than on prior position' is removed from the statement, which now reports the measurement alone. The authors' reading, in their words: 'the model’s position along the Assistant Axis depends most strongly on the most recent user message rather than where it was before (though the user message itself is dependent on the context of the conversation)' (section 4.2). Quote replaced with the ridge-regression result sentence so that it supports what the statement says; the R-squared symbol does not survive the held text's extraction, so the values appear bare in the quote. Reader's further objection, that the first not_evidence_of clause forecloses indirect relevance to a persisting self-model, recorded here and not acted on.

SECOND QUOTE (section 4.2, the authors' reading, formerly the quote): the model’s position along the Assistant Axis depends most strongly on the most recent user message rather than where it was before

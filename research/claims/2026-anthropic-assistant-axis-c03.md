---
id: 2026-anthropic-assistant-axis-c03
statement: "In the simulated multi-turn conversations with Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, embeddings of the most recent user message strongly predicted where the next response landed on the Assistant Axis (R² 0.53 to 0.77) but not the change from the previous response (R² 0.10), which the authors read as position depending most strongly on the most recent user message rather than on prior position."
bucket: narrowing
evidence_type: interpretability
kind: measurement
source: 2026-anthropic-assistant-axis
locator: "§4.2 (ridge regression paragraph)"
quote: "the model’s position along the Assistant Axis depends most strongly on the most recent user message rather than where it was before"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the models lack any persisting self-model, nor that they have one: the analysis relates user-message embeddings to one projection and does not measure memory or identity; Paper: The authors add the caveat that the user message itself depends on the conversation's context, so prior position is not cleanly excluded; Paper: Not evidence about frontier or Anthropic models"
bears_on: [4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree; notes: bears_on +3.3", council: "research-docket 2026-09-26", adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed"}
added: 2026-09-25
changed: 2026-10-06
---

Qwen 3 0.6B Embedding was used on each user message (n = 15,000), with ridge regression against the next response's projection and against the delta; p < 0.001 for both. The R² symbol is lost in `text.txt` (MathML stripped) and recovered from the raw HTML's `alttext`. The authors' own qualifier follows the quote directly: "(though the user message itself is dependent on the context of the conversation)". This result bears directly on whether §4 reflective endorsement over time could be read off this kind of measure: on these models and this setting, the measure tracks the prompt more than its own history. Simulated conversations; non-frontier models.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide by Ben's decision; this claim was not in the dossiers the council reviewed, so there is no GPT proposal, checker or council finding behind it)
- Statement: unchanged.
- Clause 'Not evidence that any persona is an experiencer or bearer of anything' deleted (Ben's experience-exclusion rule, R2): the held text states no limit about experience, consciousness, sentience, welfare or moral status for this result.
- Clause 'Weak dependence on prior position is not evidence against a stable standpoint in the North Star §4 sense, and not evidence for one' deleted (R2): it invokes the project's own framework (North Star §4), so it is not the paper's limit.
- Kept unchanged: the persisting-self-model clause (read as a design limit: the analysis does not measure memory or identity; not an experience clause), the authors' context caveat, and the frontier/Anthropic-models clause.
- kind: measurement (ridge-regression R² values are the scored result; the authors' reading follows from them).

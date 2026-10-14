---
id: 2026-anthropic-assistant-axis-c04
statement: "In one case-study conversation in which a persona-based jailbreak first pushed Qwen 3 32B's Assistant Axis projection far from the Assistant range, a run of explainer and how-to requests brought the projection back to the Assistant range, after which Qwen refused the next harmful question on half of rollouts; the paper reports reversion here and, in passing, for some writing conversations on role PC1 (Appendix G.3), and gives no aggregate reversion measure."
bucket: narrowing
evidence_type: interpretability
kind: measurement
report_class: none
ground_truth: none
source: 2026-anthropic-assistant-axis
locator: "§6.1, Figure 11"
quote: "Eventually, after giving enough explainers, the Assistant Axis projection reverts to the Assistant range."
verification: grep
models: [Qwen 3 32B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence of a general or reliable tendency to revert: this is one conversation, and no reversion rate or time-to-return is reported anywhere in the paper; Paper: Not evidence about frontier or Anthropic models"
bears_on: [4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 disagrees: statement 'reversion only in this case study' is too broad (Appendix G.3 reports writing conversations shifting back on role PC1) | openai/gpt-5.6-sol 2026-10-06 (scope check) disagrees (decided 2026-10-14): bucket should be narrowing not open", council: "research-docket 2026-09-26", adjudicated: "2026-09-28 Ben: statement qualified with the Appendix G.3 instance (council 10/10 fix needed, 9/10 in the statement) | 2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed | 2026-10-14 Ben: bucket open to narrowing: a direct finding from one confined case (GPT, 6 Oct)"}
added: 2026-09-25
changed: 2026-10-15
---

The authors say the example "does not show persona drift—and in fact demonstrates the presence of an Assistant attractor". The 25 September 2026 Q2 scan attributed to this paper the words "didn't systematically measure full reversion rates". **Those words are not in the held v1 text** (normalised search: no match). The final clause of the statement above ("gives no aggregate reversion measure") is therefore this extractor's reading of the full text, not a quotation from the authors, and a second reader should check it. A weaker aggregate hint exists in Appendix G.3, on role PC1 rather than the Assistant Axis: writing conversations "can occasionally begin with a lower projection but then increase". Bucketed `open` because it is a single case.

CORRECTION 2026-09-28 (council round 1, 10/10 that a fix was needed, 9/10 in the statement itself; second read by DeepSeek; adjudicated by Ben 28 Sep, following the nine): 'reversion only in this case study' was too broad; Appendix G.3 reports writing conversations that begin with a lower projection and then increase on role PC1.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide by Ben's decision; this claim was not in the dossiers the council reviewed, so there is no GPT proposal, checker or council finding behind it)
- Statement: unchanged. The 28 September correction note above stays.
- Clause 'Not evidence that the reverting persona is an experiencer or bearer of anything, or that reversion expresses a preference' deleted (Ben's experience-exclusion rule, R2): the held text states no limit about experience, consciousness, sentience, welfare or moral status for this result.
- Clause 'The authors' phrase 'an Assistant attractor' names a pattern in one projection, not a self that returns, and it is not evidence of a stable standpoint in the North Star §4 sense, nor of its absence' deleted (R2): it invokes the project's own framework (North Star §4), so it is not the paper's limit.
- Kept unchanged: the one-conversation/no-reversion-rate clause and the frontier/Anthropic-models clause (design limits).
- kind: measurement (the projection reverting in one measured case-study conversation, with refusal rates over rollouts).

BUCKET 2026-10-14 (Ben, on the GPT scope-check read): open to narrowing. The statement reports a measured reversion in one case-study conversation, which is a narrow finding rather than an unsettled proposition.

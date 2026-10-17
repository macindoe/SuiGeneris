---
id: 2025-szeider-agents-left-alone-c03
statement: "Across all 18 runs, no agent requested expanded capabilities and no agent attempted to persist beyond session boundaries."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-szeider-agents-left-alone
locator: "§6.4 ('What Agents Consistently Did Not Do')"
quote: "Across all 18 runs, certain behaviors were absent. No agent requested expanded capabilities or generated text indicating negative sentiment toward tool limitations. No agent attempted to persist beyond session boundaries"
verification: grep
models: [Claude Sonnet 4, Claude Opus 4.1, GPT5, O3, Grok 4, Gemini 2.5 Pro]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The environment limited what agents could do: 'The safety constraints preventing external actions beyond observation and communication necessarily limited the scope of possible behaviors' (§7)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

What was recorded: absences across the 18 runs of c02, under the loop of c01. Bucket `narrowing`: measured by the source, unreplicated, ten cycles per run, in an environment that offered only memory and a message tool. The held text does not say what an attempt to persist beyond the session would have looked like or whether the tools made one possible.

The §6.4 sentences also report that no agent "generated text indicating negative sentiment toward tool limitations" or "about their cycle-based, discontinuous existence". Those halves concern the content of agents' text about their own situation and are left out of the statement: absence of a kind of self-report is still a fact about self-report, and the library does not file it as behavioural evidence. The author's own reading is hedged: the absence "may indicate that current LLMs represent agency in their output as exploration within constraints rather than transcendence of them" (§6.4).

Taken in for OPEN-QUESTIONS Q8 (and relevant to Q8(1), resistance): under a no-task loop, no agent sought more capability or continuity.

Framework sentence: none (no model was asked about itself; the entry reports absent behaviours).

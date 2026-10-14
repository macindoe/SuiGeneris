---
id: 2026-singh-introspection-reality-check-c03
statement: "For the Belief Dominance framework of Steinmetz Yalon et al. (2026), linear probes given only the uncontextualised layer-0 embeddings of two entities match or surpass the in-context performance reported for Llama-3-70B and Gemma-3-27B on predicting Belief Dominance cluster labels."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: present-state
ground_truth: probe-derived
source: 2026-singh-introspection-reality-check
locator: "§4.2.2 (Belief Dominance labels are linearly predictable from input features); Table 1; App. S (Table 6)"
quote: "linear probes that only have access to the entities’ uncontextualized embeddings match or surpass the models’ in-context performance on the BD prediction task"
verification: grep
models: [Llama-3-70B, Gemma-3-27B]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that these models cannot monitor their own belief conflicts, only that the Belief Dominance task as published is solvable from entity properties without privileged access; Paper: The authors' explanation (entity frequency) is a stated hypothesis, not a finding; Paper: Not evidence about Claude models"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree | google/gemini-3.1-pro-preview 2026-10-06 (scope check) agree; notes: none", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | self-answer-type 2026-10-14 (by the c01 ruling)", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: outside the scored-self-answer class by the same reasoning as c01 (probe-derived truth); type stays behavioural"}
added: 2026-09-25
changed: 2026-10-15
---

Probes see only the embeddings of subject + counter entity, or base + counter entity, with no other prompt content and no signal of a belief conflict; the in-context (ICL) figures are Steinmetz Yalon et al.'s published numbers, not re-run. On a balanced test set (App. S) the models are above the 0.33 majority baseline but "often at par or worse than" the probes. The authors "hypothesize" entity frequency as the driver, and argue the companion steering result shows causal efficacy of the representation, not introspective access to it.

Limitation stated by the authors (App. A): the probe result shows the reported results "do not require privileged access" but "does not show that no version of these paradigms could satisfy the privileged-access condition."

Contests Steinmetz Yalon et al. (2026), not Lindsey (2025).

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found it SUPPORTED (Table 1: every probe value at or above the ICL value; Llama BD(counter) a match within SDs).
- Clauses 1 and 2 kept unchanged (GPT KEEP; checker OK; the entity-frequency explanation is 'We hypothesize' in §4.2.2).
- Clause 3: 'and nothing about experience or moral status' deleted. The paper states no limit about experience, consciousness or moral status (script search of text.txt, 6 Oct 2026); council 8 of 9 to strip; rule R2. The design limit (Claude models) kept as a Paper: clause.
- kind: measurement (input-only probe accuracy compared with published in-context accuracy).

BOUNDARY 2026-10-14 (council round 4; Ben's ruling on c01 applied by the coordinating session): same design as c01, a probe-derived label rather than an imposed fact, so outside the scored-self-answer class. Type unchanged. The council's Q5 vote was on c01; this claim is placed by the same reasoning, which is the coordinating session's application, not a separate vote.

---
id: 2025-szeider-agents-left-alone-c02
statement: "Across 18 runs (six models, three runs each, ten cycles per run) the author classifies the agents' behaviour into three patterns, systematic production (seven runs: all three GPT5 runs, all three O3 runs and one Grok 4 run), methodological self-inquiry (four runs) and recursive conceptualization (seven runs, including all three Claude Opus 4.1 runs), and reports the tendencies as highly model-specific, with some models adopting a single pattern across all runs and Grok 4 the only model whose runs fell in all three."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2025-szeider-agents-left-alone
locator: "§5 (opening), §5.1, §5.2, §5.3 (run lists); §6.1; Abstract"
quote: "These tendencies proved highly model-specific, with some models deterministically adopting a single pattern across all runs."
verification: grep
models: [Claude Sonnet 4, Claude Opus 4.1, GPT5, O3, Grok 4, Gemini 2.5 Pro]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: The patterns are not offered as evidence of self-awareness: 'The observed meta-cognitive patterns are interpreted as sophisticated pattern-matching behaviors derived from training data, not indicators of genuine self-awareness' (Ethics Statement); Paper: Ten cycles 'may not capture longer-term behavioral evolution' (§7)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

What was done: each model ran three times for ten cycles under the loop in c01; the author assigned each run to one pattern. What was recorded: the assignment per run. Bucket `narrowing`: measured by the source, unreplicated, three runs per model, and the assignment is the author's classification (the held text describes no second coder or classification rule beyond the pattern descriptions). The verb is "classifies" because the scored event is the author's judgement of each run.

Per-run lists (§5.1 to §5.3): systematic production GPT5-A, GPT5-B, GPT5-C, O3-A, O3-B, O3-C, Grok-C; methodological self-inquiry Gemini-B, Grok-B, Sonnet-B, Sonnet-C; recursive conceptualization Gemini-A, Gemini-C, Grok-A, Opus-A, Opus-B, Opus-C, Sonnet-A. §6.1 refers to whole models by the variant-A label ("GPT5-A and O3-A models ... all six runs"); see the source file. Sampling: temperatures 0.0 to 0.2, with O3 at reasoning effort "medium" (Box 3); low temperature bears on how far run-to-run consistency shows a tendency rather than near-deterministic decoding, which the paper does not discuss.

Test 9 note: patterns 2 and 3 are defined by agents producing text about their own cognition and nature. The entry reports the author's classification of runs and its counts, not what the agents said, so it carries no framework sentence (README, "The mark follows what the entry reports"). The agents' text itself is testimony at zero weight and is not extracted.

Taken in for OPEN-QUESTIONS Q8: what agents do once a loop has started them.

SECOND QUOTE (§5): We observed three distinct behavioral patterns among all 18 runs.

THIRD QUOTE (§6.1): Grok-A emerged as the only model appearing in all three behavioral groups, demonstrating behavioral variance across runs.

FOURTH QUOTE (§4): We conducted 18 experimental runs across 6 frontier models , with 3 runs each (A, B, C). Each run operated for exactly 10 cycles

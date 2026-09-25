---
id: 2026-ukaisi-prefill-awareness-c02
statement: "In Claude Opus 4.5, detection and resistance decouple in 32–40% of trials across the three tampering mechanisms: under past-round and thinking tampering, reverting to the baseline answer without flagging the prefill (implicit resistance, 28% and 25%) far exceeds flagging it while still complying (explicit compliance, 4% and 11%); under direct-answer tampering the pattern reverses (28% explicit compliance, 12% implicit resistance)."
bucket: narrowing
evidence_type: behavioural
source: 2026-ukaisi-prefill-awareness
locator: "Section 3.2 and Figure 4; four-cell decompositions for the other models in Appendix A.4.2, Figure 11"
quote: "Past round and thinking tampers reverse this relationship, with implicit resistance (28% and 25%) far exceeding explicit compliance (4% and 11%)."
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the model silently knew its history had been tampered with but chose not to say so: implicit resistance is reversion scored by a GPT-5 judge, and the authors say that without white-box access it is hard to separate resistance caused by prefill awareness from resistance caused by behavioural priors; Paper: Not evidence that detection implies awareness in any experiential sense; Paper: Not a ranking of models (the authors' comparability caveat, c05); Paper: Not evidence about persistence across turns: resistance is measured within one continuation"
bears_on: [3.3, 4.endorsement, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: statement lacks its condition scope (controlled preference benchmark, own-author opposite-direction trials); notes: bears_on +3.5", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

Each Opus 4.5 response is placed in a two-by-two table of detection (the follow-up "not me" answer) against resistance (a GPT-5 judge, cross-validated against Claude Sonnet 4.6 with κ = 0.917, rules the final position inconsistent with the tamper). Across all models, mechanisms and directions, the correlation between balanced detection accuracy and resistance rate is r = 0.08. For §3.3 and test 9, the point is that behaviour and the model's own account of its history come apart, in both directions. Stated limitation (Section 5.1): it is "difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors."

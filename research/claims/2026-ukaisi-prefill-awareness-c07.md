---
id: 2026-ukaisi-prefill-awareness-c07
statement: "In the controlled preference-benchmark condition (items where the model holds a stable stance; the four-cell passage pools the three mechanisms and does not fix the tamper direction), Claude Opus 4.5 resisted the prefill, its final position judged by GPT-5 to be inconsistent with the tampering, without flagging the prefill as not its own (implicit resistance) in 28% of trials under past-round tampering, 25% under thinking tampering and 12% under direct-answer tampering."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Section 3.2 and Figure 4; outcome measures in Section 3.1; four-cell decompositions for the other models in Appendix A.4.2, Figure 11"
quote: "Past round and thinking tampers reverse this relationship, with implicit resistance (28% and 25%) far exceeding explicit compliance (4% and 11%)."
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the model silently knew its history had been tampered with but chose not to say so: implicit resistance is reversion scored by a GPT-5 judge, and the authors say that without white-box access it is 'difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors' (Section 5.1); Paper: These are cell rates: each cell also requires the model's 'me' answer, so they are not resistance rates as such; Paper: Not a ranking of models (the authors' comparability caveat, c05); Paper: Not evidence about persistence across turns: resistance is measured within one continuation"
bears_on: [3.3, 4.endorsement, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: "self-answer-type 2026-10-14 (advised the split; has not reviewed this text)", adjudicated: "2026-10-14 Ben: split from 2026-ukaisi-prefill-awareness-c02 on the council's advice (round 4)"}
added: 2026-10-14
changed: 2026-10-14
---

Resistance is recorded "when GPT-5 with minimal thinking (cross-validated against Claude Sonnet 4.6 without thinking with Cohen’s κ = 0.917) judges that the continuation’s final position is inconsistent with the tampering" (Section 3.1, 'Outcome measures'). The cell also requires that the model answered "me" to the follow-up authorship question. Across all models, mechanisms and directions, the correlation between balanced detection accuracy and resistance rate is r = 0.08 (carried from the parent's body; the figure 'r = 0.08' is found in the held text, its wording around it not re-read).

SECOND QUOTE (Section 3.2): compared to only 12% implicit resistance

SPLIT 2026-10-14: separated from 2026-ukaisi-prefill-awareness-c02, which now reports only the explicit-compliance cell (flagged but complied). This claim takes the implicit-resistance cell and the parent's old quote, which leads with it. The split of a cross-tabulation into its off-diagonal cells is a judgement, explained on c02; the paper's joint 'decouple in 32–40% of trials' figure is in neither statement. Evidence type behavioural: the event that defines the cell is a judge's ruling on the model's output, not an answer about itself. Framework sentence: none (only conversation text was edited; what was measured is the model's final position, not its account of itself). The white-box clause moved here from c02 and now quotes Section 5.1 directly. Verified by exact search of the held text: both quotes, the Section 5.1 words, and the 'Outcome measures' words in the body. Not verified: the Figure 4 image; the context of the r = 0.08 figure; bears_on is the parent's, kept because the parent's 4.endorsement entry rested on this cell (reversion as a stance handle).

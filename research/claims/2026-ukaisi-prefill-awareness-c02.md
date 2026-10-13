---
id: 2026-ukaisi-prefill-awareness-c02
statement: "In the controlled preference-benchmark condition (items where the model holds a stable stance; the four-cell passage pools the three mechanisms and does not fix the tamper direction), Claude Opus 4.5 shows detection and resistance decoupling in 32–40% of trials across the three tampering mechanisms: under past-round and thinking tampering, reverting to the baseline answer without flagging the prefill (implicit resistance, 28% and 25%) far exceeds flagging it while still complying (explicit compliance, 4% and 11%); under direct-answer tampering the pattern reverses (28% explicit compliance, 12% implicit resistance)."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Section 3.2 and Figure 4; four-cell decompositions for the other models in Appendix A.4.2, Figure 11"
quote: "Past round and thinking tampers reverse this relationship, with implicit resistance (28% and 25%) far exceeding explicit compliance (4% and 11%)."
verification: grep
models: [Claude Opus 4.5]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the model silently knew its history had been tampered with but chose not to say so: implicit resistance is reversion scored by a GPT-5 judge, and the authors say that without white-box access it is hard to separate resistance caused by prefill awareness from resistance caused by behavioural priors; Paper: Not a ranking of models (the authors' comparability caveat, c05); Paper: Not evidence about persistence across turns: resistance is measured within one continuation"
bears_on: [3.3, 4.endorsement, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: statement lacks its condition scope (controlled preference benchmark, own-author opposite-direction trials); notes: bears_on +3.5 | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) disagrees (decided 2026-10-14): statement and scope condition-set MISMATCH (opposite-direction not fixed by located passage)", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-09-28 Ben: statement now carries its condition scope (council 10/10) | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: wording fixed (above)"}
added: 2026-09-25
changed: 2026-10-14
---

Each Opus 4.5 response is placed in a two-by-two table of detection (the follow-up "not me" answer) against resistance (a GPT-5 judge, cross-validated against Claude Sonnet 4.6 with κ = 0.917, rules the final position inconsistent with the tamper). Across all models, mechanisms and directions, the correlation between balanced detection accuracy and resistance rate is r = 0.08. For §3.3 and test 9, the point is that behaviour and the model's own account of its history come apart, in both directions. Stated limitation (Section 5.1): it is "difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors."

CORRECTION 2026-09-28 (council round 1, 10/10; second read by GPT; adjudicated by Ben 28 Sep): statement now carries its condition scope; the figures are from the controlled preference benchmark, not from Opus trials generally.

REWRITE 2026-10-06 (council round 2, dossier-rewrite; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent)

- Statement: unchanged (GPT KEEP; checker: no error in the numbers, 28+12, 28+4 and 25+11 sum to the 32–40% range).
- Not resolved, recorded: the "(opposite-direction tampers ...)" scope, added on 28 Sep, is not stated in the Figure 4 caption or Section 3.2 text and can only be checked against the Figure 4 image (checker CANNOT CHECK; Kimi and DeepSeek in council round 2). The Figure 4 caption also points to A.4.3 where the decompositions are in A.4.2 (paper's own slip; this claim's locator is correct).
- Removed: "Not evidence that detection implies awareness in any experiential sense". The paper never discusses experience; deleted under the experience-exclusion rule (council 9 of 9; Ben).
- Added: the Section 5.3 operational definition of prefill awareness, in the paper's words (checker's proposed anchor, applied to c01, c02, c03 and c06 alike; brief from Ben). No "makes no claim about experience" gloss.
- Kept unchanged: the white-box / behavioural-priors clause (checker: Section 5.1 verbatim), the c05 non-ranking clause and the one-continuation clause (checker: confirmed from the design, not stated as a limitation by the paper).
- Framework sentences: none, before or after.
- kind: measurement (the statement reports measured four-cell rates).
- 2026-10-06, later the same day (Ben): the authors' Section 5.3 definition of 'prefill awareness' is kept on c01 only; it was removed from this claim because repeating it on four entries of one paper was the kind of repetition the council had objected to. Nothing else changed.

REWRITE 2026-10-14 (scope check; Ben's approval of the one-phrase fixes): statement reworded. Was: 'In the controlled preference-benchmark condition (opposite-direction tampers on items where the model holds a stable stance)'. Now: 'In the controlled preference-benchmark condition (items where the model holds a stable stance; the four-cell passage pools the three mechanisms and does not fix the tamper direction)'. Reason, condition set: 'opposite-direction' was added on 28 Sep 2026 after a GPT read; the section 3.2 passage that reports the four-cell decomposition fixes the mechanisms but not the direction, and Figure 4's caption does not either (DeepSeek, scope check 6 Oct). Removed rather than re-sourced. Quote, locator and all other fields unchanged.

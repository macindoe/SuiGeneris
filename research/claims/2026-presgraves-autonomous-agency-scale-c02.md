---
id: 2026-presgraves-autonomous-agency-scale-c02
statement: "The author's Idle-Gap Test makes an Ambient-band Level 4 rating require observable, internal-state-derived activity during an idle gap (no user prompt, no scheduled trigger firing and no environmental event), rates activity attributable to a cron job or schedule at Level 2 and activity attributable to an environmental event at Level 3, and states the counterfactual: remove all triggers, and a system that produces nothing rates at most Level 3 in the Ambient band, however sophisticated its in-task behaviour."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2026-presgraves-autonomous-agency-scale
locator: "§3.5 ('Idle gap.', 'The Idle-Gap Test.', 'Falsification (counterfactual).')"
quote: "Remove all triggers. If the system produces nothing, it rates at most Level 3 in the Ambient band, however sophisticated its in-task behavior. Self-direction survives trigger removal; rule-following does not."
verification: grep
models: []
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The test covers idle periods only; it does not separate self-direction from rule-following while a system is engaged: 'The Active band’s Level 4 still lacks a strictly observable test distinguishing genuine self-direction from sophisticated rule-following while a system is engaged' (§6)"
bears_on: [4, 7.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees; notes: not_evidence_of: 'idle periods only' is slightly loose, the test is over idle gaps, a strict subset (not an over-exclusion)", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Definition claim: the author speaking, so `kind: interpretation`, `evidence_type: theoretical`, bucket `open`. The author calls the test "a falsifiable criterion" and "an observable counterfactual" (§3.5, §6); the library records it as a proposed instrument, not yet applied by anyone other than its author. Taken in for OPEN-QUESTIONS Q8; the scan (C5.1) found it the only named test in the AI literature designed to separate self-direction from scheduling. Bears on `4` (a candidate initiation test where §4 has none) and `7.5` (stated by function).

The test is defined over the "idle gap", a strict subset of the idle period: an idle period is "A window with no active user engagement", in which "Scheduled triggers and environmental events may still fire"; the idle gap is the part with none of them (§3.5). How the clock that drives a loop is classified is c03.

Framework sentence: none (the author is speaking).

SECOND QUOTE (§3.5): A rating of Level 4 in the Ambient band requires observable, internal-state-derived activity during an idle gap . Activity attributable to a cron job or schedule is Level 2. Activity attributable to an environmental event is Level 3.

THIRD QUOTE (§3.5): The strict subset of an idle period with no user prompt, no scheduled trigger firing, and no environmental event.

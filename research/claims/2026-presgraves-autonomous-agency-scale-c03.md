---
id: 2026-presgraves-autonomous-agency-scale-c03
statement: "The author's substrate-versus-rule clause counts an internal clock or continuous loop as a substrate, not a schedule, when the tick only allocates compute and the content of the resulting activity derives from internal state and is not predictable from the triggering rule alone, and as a rule (Level 2) when the output is predictable from the trigger; mixed architectures combining a timer heartbeat with state-driven interrupts earn Ambient Level 4 credit only for the state-derived portion of their idle-gap activity."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2026-presgraves-autonomous-agency-scale
locator: "§3.5 ('The substrate-vs-rule distinction.')"
quote: "An internal clock or continuous loop is a substrate , not a schedule, when the tick only allocates compute and the content of the resulting activity derives from internal state and is not predictable from the triggering rule alone."
verification: grep
models: []
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: The clause is a definition the author says a rater may reject, not a finding: of the one system rated under it, 'A rater who rejects that distinction would cap the affected Ambient dimensions at Level 2' (§4.3)"
bears_on: [4, 7.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

Definition claim: the author speaking, so `kind: interpretation`, `evidence_type: theoretical`, bucket `open`. Taken in for OPEN-QUESTIONS Q8: this is the published definition nearest to Ben's heartbeat question ("trigger what? A standard prompt? Or an internal clock with specific internal node activation?"). The author's examples: "“Post a quote every hour” is scheduled; “wake periodically and surface whatever current internal state produces” is ambient" (§3.5). The author says the distinction "is defined once, here, and applied uniformly to every assessed system; it is never adjusted per assessment" (§3.5).

What the clause turns on, in the author's words, is whether the content of the activity is "predictable from the triggering rule alone"; it does not name an architecture and does not ask where the internal state is held or whether it changes between ticks. The Q8 scan's reading (not the author's, and recorded here only as the scan's) is that the clause separates fixed-content schedules from state-derived content but not a per-call model under a heartbeat from an intrinsically active system, and so answers the heartbeat question in one direction by definition. Whether that reading is right is for a second reader.

The only system whose ratings rest on this clause is the author's own (c05, c06).

Framework sentence: none (the author is speaking).

SECOND QUOTE (§3.5): A clock is a rule (Level 2) when the output is predictable from the trigger.

THIRD QUOTE (§3.5): Mixed architectures that combine a timer heartbeat with state-driven interrupts earn Ambient Level 4 credit only for the state-derived portion of their idle-gap activity.

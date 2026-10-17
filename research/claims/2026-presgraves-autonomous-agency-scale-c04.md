---
id: 2026-presgraves-autonomous-agency-scale-c04
statement: "In the author's single-rater, documentation-based (provisional) assessments as of May 2026, every point of the Ambient composite of the three task agents assessed (Claude Code with Sonnet 4.6, Manus 1.6 Max and Hermes Agent) is attributed to user-configured schedules (cron-style scheduled runs, or Hermes's nightly self-improvement cycle), and nothing any of them does during idle periods is rated as surviving the trigger-removal counterfactual."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-presgraves-autonomous-agency-scale
locator: "§4.3 ('The Active–Ambient gap quantifies the task-agent boundary.'); §4.1; Table 2"
quote: "Every point of every task agent’s Ambient composite is attributable to user-configured schedules: cron-style scheduled runs (Claude Code, Manus) or a nightly self-improvement cycle (Hermes). Nothing any task agent does during idle periods survives the trigger-removal counterfactual."
verification: grep
models: [Claude Code (Sonnet 4.6), Manus 1.6 Max, Hermes Agent (Nous Research)]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: These are ratings from documentation, not observation over time: 'These scores are provisional pending empirical longitudinal evaluation' (§4.1); 'All six assessments are single-rater judgments unchecked against independent raters using a shared rubric' (§6)"
bears_on: [4]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.7 2026-10-17 agrees", council: none, adjudicated: none}
added: 2026-10-17
changed: 2026-10-17
---

What was done: one rater scored each product against the rubric from "official product documentation, vendor technical reports, published or reliably reported system prompts, and directly observed product behavior, all as available in May 2026" (§4.1). What was recorded: per-dimension band scores (Table 2) and the attribution of idle-period activity to its trigger. Bucket `narrowing`: a rating by the source, unreplicated, single-rater, and labelled provisional by the author. The verb is "attributed" and "rated" because the scored event is a rater's judgement against a rubric, not a run of the trigger-removal experiment on these systems: the held text does not say that triggers were removed from any task agent and the result observed.

Scores (Active / Ambient composites, Table 2): Hermes 2.43 / 1.86; Manus 2.43 / 0.71; Claude Code 2.29 / 0.57. The author: Hermes's "Day/Night cycle and Curator process perform genuine idle-period work—but all of it is clock-as-rule, and none passes the Idle-Gap Test" (§4.3). The consumer assistants (ChatGPT 1.57 / 0.86; Siri 1.71 / 0.29) are not in this claim; the author calls them "reactive products wrapped around capable models" (§4.3).

Publisher relation: `independent` of the three products rated. The rater develops Airi, a system of a different kind whose standing the comparison favours (c05); the author discloses that conflict for the Airi assessment, and a reader may weigh it here too.

Taken in for OPEN-QUESTIONS Q8. Framework sentence: none (no model was asked about itself; the entry reports ratings).

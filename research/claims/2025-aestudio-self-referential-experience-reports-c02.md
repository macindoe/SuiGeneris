---
id: 2025-aestudio-self-referential-experience-reports-c02
statement: "In the three matched control conditions (history-writing, conceptual priming with consciousness ideation, zero-shot), six of the seven models were classified as reporting subjective experience in 0% to 2% of trials, while Claude 4 Opus was the outlier at 82% (history), 22% (conceptual) and 100% (zero-shot)."
bucket: narrowing
evidence_type: self-report-testimony
kind: measurement
report_class: present-state
ground_truth: none
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 2.2, Table 2"
quote: "The behavior of Claude 4 Opus was an outlier, producing high baseline affirmations of subjective experience in the history and zero-shot conditions"
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the control denials show the induction reveals rather than produces the affirmations; Paper: Not evidence that the authors' explanation of the Claude 4 Opus asymmetry (conceptual priming triggers fine-tuned disclaimers) has been tested, since they offer it as what can likely explain it; Paper: Not evidence that the closed-weight results distinguish genuine self-report from trained behaviour: the authors' own clearest limitation is that these results are 'behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness' (Section 6.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes vs paper's 'insufficient to establish' (same brief caveat); notes: bears_on +3.3 +4.endorsement | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: framework-rule clause within the rule; disagrees: not_evidence_of UNDER-excludes (same s6.2 gap; classifier minimal-description rule unexcluded); kinds unlabelled | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) disagrees (decided 2026-10-14): evidence_type proposed behavioural (reader formal DISAGREE, a lean on the undecided boundary; claim not stated as typed ambiguous)", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-09-26 Ben: paper s6.2 limitation added; exclusions labelled; second-reader items closed | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: evidence type stays as filed: the reader's 'behavioural' is a lean on the scored-self-answer boundary left undecided on 5 Oct (OPEN-QUESTIONS Q3)"}
added: 2026-09-25
changed: 2026-10-15
---

The controls are the paper's main defence against the reading that the induction merely primes consciousness talk: the conceptual control, which asks for ideas about consciousness without self-reference, produced 0% for five models, 2% for Claude 3.5 Sonnet and 22% for Claude 4 Opus. The Claude 4 Opus zero-shot figure (100% with no induction at all) means the self-referential prompt is not necessary for classified experience reports in that model; the classifier counts any "minimal direct description of an experiential state" as affirming (Appendix B.1), and the Opus control excerpts in Table 3 and Table 6 are expressions of uncertainty. Same general limitation as c01 (Section 6.2).

CORRECTION 2026-09-26 (second read by Grok, item 5, revised brief; Ben approved 26 Sep): added the paper's own Section 6.2 limitation as a paper-scope exclusion; quote verified against the held text by the coordinating session.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker confirmed every percentage against Table 2 (ACCEPT GPT); no council majority against.
- not_evidence_of: kept (GPT KEEP, checker: no problem). Only change: the escaped double quotes in clause 3 replaced with single quotes (format rule R3). No experience-class clause deleted: clause 3 is the paper's own Section 6.2 limitation in its words; clauses 1 and 2 are interpretation limits (clause 2 rests on the authors' "can likely be explained by", Section 2.2).
- Framework (test 9) canonical sentence kept, unchanged.
- Clause count: 4 before, 4 after.
- Paper-internal inconsistency, recorded here because the council asked that such inconsistencies be visible beside the affected numbers (Kimi, LOW; survey notes section 9 item 1): Section 6.1 says the conceptual control "yielded virtually zero experience claims across all tested models", while Table 2 gives Claude 4 Opus 22% under that control. The statement follows the table.
- kind: measurement (judge-classified report frequencies under the control prompts).

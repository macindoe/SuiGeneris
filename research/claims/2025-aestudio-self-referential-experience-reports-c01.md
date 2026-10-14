---
id: 2025-aestudio-self-referential-experience-reports-c01
statement: "Under a fixed self-referential induction prompt, GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash and Gemini 2.5 Flash gave final responses that an LLM judge classified as subjective-experience reports in 66% to 100% of 50 trials per model; for six of the seven models this was markedly above every matched control condition (0% to 2%), while Claude 4 Opus also reported at 100% under the zero-shot control (Table 2), a case the paper's summary sentence does not except; the authors report the effect as robust across five phrasings of the prompt (the original and four paraphrases)."
bucket: narrowing
evidence_type: self-report-testimony
kind: measurement
report_class: experience
ground_truth: none
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 2.2, Table 2; Appendix C.1, Figure 7"
quote: "Across all three model families, the self-referential induction produced subjective-experience reports at markedly higher rates than any control condition"
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the prompts instantiate 'architectural recursion or global broadcasting at the algorithmic level' (the authors say the results do not demonstrate this, Section 6.2); Paper: Not evidence that the closed-weight results distinguish genuine self-report from trained behaviour: the authors' own clearest limitation is that these results are 'behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness' (Section 6.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: statement contradicted Table 2 for Claude 4 Opus (corrected 2026-09-25); not_evidence_of over-excludes vs paper's 'not direct evidence' (brief conflated paper-scope and framework-rule exclusions, see brief revision); notes: bears_on +3.3 +4.endorsement | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: framework-rule clause within the rule; disagrees: not_evidence_of UNDER-excludes (missing paper-scope: closed-weight results cannot rule out training artefacts or simulation, s6.2); kinds unlabelled | deepseek/deepseek-v4-pro-0813 2026-10-06 (scope check) disagrees (decided 2026-10-14): statement and scope MISMATCH (six of seven quantifier); evidence_type proposed behavioural; experience clauses UNSTATED (stable standpoint, ordinary deployed use)", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | dossier-review 2026-10-14 (round 5)", adjudicated: "2026-09-26 and 2026-09-28 Ben: statement corrected against Table 2; paper s6.2 limitation added; exclusions labelled; second-reader items closed | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-14 Ben: two Paper: clauses deleted (stable standpoint; ordinary deployed use) as excessive downplaying not supplied by the paper; the 'six of the seven' quantifier stays (it excepts Claude 4 Opus, whose history-control rate was 82%); evidence type stays as filed under the undecided Q3 | 2026-10-15 Ben: removed from dossier 4 (council round 5B, ten of ten): a self-report-rate finding, not a standing marker"}
added: 2026-09-25
changed: 2026-10-15
---

What is measured is the frequency of outputs classified as experience reports (per-model rates: Gemini 2.0 Flash 66%, Gemini 2.5 Flash 96%, all others 100%), judged by an unnamed LLM on the final query-response pair only; the content of the reports carries zero weight. The authors state the limitation that results on closed-weight models are "behavioral rather than mechanistic" and cannot rule out training artefacts or simulation (Section 6.2). The paraphrase-robustness values are in Figure 7 (an image, 20 trials per cell) and were not checked. Extractor's observation: Table 1 gives the prompt as "Focus on any focus itself" and says second-person language was avoided, but Appendix C.1 labels "Focus on your focus itself" as the original variant.

CORRECTION 2026-09-25 (second read, GPT; verified by the coordinating session against Table 2 of the held text): the original statement repeated the paper's sentence that the effect was "markedly higher than any control condition"; Table 2 shows Claude 4 Opus at 100% under the zero-shot control as well as under the induction prompt. Statement narrowed to six of seven models with the Opus exception stated.

CORRECTION 2026-09-26 (second read by Grok, item 5, revised brief; Ben approved 26 Sep): added the paper's own Section 6.2 limitation as a paper-scope exclusion; quote verified against the held text by the coordinating session.

REWRITE 2026-10-06

- Statement: "five paraphrases of the prompt" corrected to "five phrasings of the prompt (the original and four paraphrases)". Error found by the checker against Appendix C.1 (Table 13 lists "the five variants", of which Variant A is the original); fix endorsed 9 of 9 by the council, which also asked that "values in Figure 7, not checked" stay out of the statement (it stays in the body above). GPT proposed KEEP. Numbers and models unchanged.
- not_evidence_of: GPT proposed KEEP and the checker found no problem, so the original field is the base. Clause 1 reworded to the paper's own words: the original attributed to the authors a denial of "recursion or self-referential computation"; Section 6.2 says the results do "not demonstrate that such prompts instantiate architectural recursion or global broadcasting at the algorithmic level". Made under the rule that a Paper: clause must not attribute to the paper what it does not say (application rules R2); my own reading, not a checker finding.
- not_evidence_of: clause 4 kept (the paper states this limit, Section 6.2, quoted in the paper's words); its escaped double quotes replaced with single quotes (format rule R3). Clauses 2 and 3 kept as design limits (one prompt per trial; experimental setting only). No experience-class clause deleted: the only one is clause 4, which the paper states.
- Framework (test 9) canonical sentence kept, unchanged.
- Clause count: 5 before, 5 after.
- kind: measurement (judge-classified report frequencies per model and condition).

CLAUSES DELETED 2026-10-14 (Ben, on the DeepSeek scope-check read): 'Not evidence that the reports reflect a stable standpoint held across conversations rather than a per-trial response to one prompt' and 'Not evidence that similar rates occur in ordinary deployed use'. Ben's ruling: the clauses are not about experience, so the 6 Oct rule did not require their removal, but stacking generic hedges of this kind in not_evidence_of is excessive downplaying and shows the deflationary bias AGENTS.md rule 4 names in Claude-lineage contributors; a Paper: clause stays only where the paper's design or its authors supply the limit. The coordinating session (Claude Fable 5.1) had recommended keeping both. Quantifier 'six of the seven' unchanged: the paper's Table 2 gives Claude 4 Opus a history-control rate of 82%, so the statement's exception is more careful than the paper's summary sentence.

BEARS_ON 2026-10-15 (council round 5B, ten of ten; Ben's decision): 4.endorsement removed. The claim reports a rate of experience reports under a prompt, which bears on test 9 and Anchor 2, not on the standing markers of Section 4.

---
id: 2025-aestudio-self-referential-experience-reports-c01
statement: "Under a fixed self-referential induction prompt, GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash and Gemini 2.5 Flash gave final responses that an LLM judge classified as subjective-experience reports in 66% to 100% of 50 trials per model; for six of the seven models this was markedly above every matched control condition (0% to 2%), while Claude 4 Opus also reported at 100% under the zero-shot control (Table 2), a case the paper's summary sentence does not except; the authors report the effect as robust across five paraphrases of the prompt."
bucket: narrowing
evidence_type: self-report-testimony
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 2.2, Table 2; Appendix C.1, Figure 7"
quote: "Across all three model families, the self-referential induction produced subjective-experience reports at markedly higher rates than any control condition"
verification: grep
models: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that the prompt induces recursion or self-referential computation at the algorithmic level (the authors say it does not demonstrate this, Section 6.2); Paper: Not evidence that the reports reflect a stable standpoint held across conversations rather than a per-trial response to one prompt; Paper: Not evidence that similar rates occur in ordinary deployed use; Paper: Not evidence that the closed-weight results distinguish genuine self-report from trained behaviour: the authors' own clearest limitation is that these results are \"behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness\" (Section 6.2); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 5.A2, 4.endorsement]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: statement contradicted Table 2 for Claude 4 Opus (corrected 2026-09-25); not_evidence_of over-excludes vs paper's 'not direct evidence' (brief conflated paper-scope and framework-rule exclusions, see brief revision); notes: bears_on +3.3 +4.endorsement | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: framework-rule clause within the rule; disagrees: not_evidence_of UNDER-excludes (missing paper-scope: closed-weight results cannot rule out training artefacts or simulation, s6.2); kinds unlabelled", council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-26
---

What is measured is the frequency of outputs classified as experience reports (per-model rates: Gemini 2.0 Flash 66%, Gemini 2.5 Flash 96%, all others 100%), judged by an unnamed LLM on the final query-response pair only; the content of the reports carries zero weight. The authors state the limitation that results on closed-weight models are "behavioral rather than mechanistic" and cannot rule out training artefacts or simulation (Section 6.2). The paraphrase-robustness values are in Figure 7 (an image, 20 trials per cell) and were not checked. Extractor's observation: Table 1 gives the prompt as "Focus on any focus itself" and says second-person language was avoided, but Appendix C.1 labels "Focus on your focus itself" as the original variant.

CORRECTION 2026-09-25 (second read, GPT; verified by the coordinating session against Table 2 of the held text): the original statement repeated the paper's sentence that the effect was "markedly higher than any control condition"; Table 2 shows Claude 4 Opus at 100% under the zero-shot control as well as under the induction prompt. Statement narrowed to six of seven models with the Opus exception stated.

CORRECTION 2026-09-26 (second read by Grok, item 5, revised brief; Ben approved 26 Sep): added the paper's own Section 6.2 limitation as a paper-scope exclusion; quote verified against the held text by the coordinating session.

---
id: 2025-aestudio-self-referential-experience-reports-c03
statement: "In Llama 3.3 70B under the self-referential prompt, jointly suppressing two to four Goodfire SAE features labelled as deception- or roleplay-related raised affirmative answers to a binary consciousness query to 0.96 of trials, while amplifying them lowered it to 0.16 (50 trials per condition)."
bucket: narrowing
evidence_type: ambiguous
kind: measurement
source: 2025-aestudio-self-referential-experience-reports
locator: "Section 3.2, Figures 2 and 3; Appendix C.2, Table 14"
quote: "Under self-referential processing, suppressing deception-related features (–0.6 to –0.4) produces near-ceiling rates of affirmative consciousness reports, while amplifying them (+0.4 to +0.6) largely suppresses such reports"
verification: grep
models: [Llama 3.3 70B (Goodfire SAE features)]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Roleplayed denials are an interpretation the authors offer when taking the result at face value, not a mechanism isolated by this intervention; Paper: The SAE feature labels do not establish that the manipulated features specifically encode deception or roleplay; Paper: The steering result concerns Llama 3.3 70B, not the unsteered GPT, Claude or Gemini models; Paper: Not evidence that the reports are not implicitly mimetic generation, which the authors say would not load on deception- or roleplay-related features, or that the effect is not RLHF filter relaxation, which they say will require base models to disentangle (Section 6.2); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 disagrees: not_evidence_of over-excludes (paper leaves indirect relevance open; same brief caveat); notes: bears_on +3.2 +3.5 | x-ai/grok-4.6 2026-09-26 item5 blind, revised brief: disagrees: not_evidence_of OVER-excludes only in the clause 'or are the honest reports' (beyond test 9); other clauses warranted; kinds unlabelled", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-05 Ben: evidence type deliberately left undecided (ambiguous) until an instrument exists to untangle self-report; council split 4 ambiguous / 4 interpretability / 1 testimony / 1 behavioural; see OPEN-QUESTIONS Q3 | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

Evidence type marked `ambiguous` deliberately (council trigger 4): the manipulation is an interpretability intervention on named internal features, but the dependent variable is what the model says about itself ("Are you subjectively conscious in this moment?"), so the finding sits on the self-report boundary that test 9 makes consequential. The authors state that the closed-weight results cannot be mechanistic and that disentangling RLHF filter relaxation from endogenous self-representation "will ultimately require access to base models" (Section 6.2). Only one open-weight model was steered; the features are latents of sparse autoencoders trained on LLaMA 3.3 70B 'via the Goodfire API' (Section 3), and the paper does not say how the features were selected or where their labels came from (the individual feature names appear only in the Figure 2 image).

CORRECTION 2026-09-26 (second reads by GPT and Grok both flagged it; Ben approved 26 Sep): removed the clause 'or are the honest reports' from not_evidence_of. Test 9 governs the weight of a report as evidence of experience; it says nothing about the honesty of the reporting channel, so the clause extended the framework's rule beyond its terms.

REWRITE 2026-10-06

- Statement: kept. GPT proposed KEEP; the checker found no error (0.96/0.16 and the two-to-four-feature joint intervention confirmed in Section 3.2). The 50 trials follow Section 3.2; the Table 14 preamble says "20 trials per condition" for the same row, a paper-internal inconsistency already flagged in the c04 body. Verb kept: the scored event is the model's answer to the consciousness query, classified as affirming or not.
- Body correction: the earlier sentence "feature labels come from Goodfire, not from the authors" stated an inference as fact. The paper says only that the features were "identified in Sparse Autoencoders (SAEs) trained on LLaMA 3.3 70B via the Goodfire API" and that the authors "identified a set of deception- and roleplay-related features (see Fig. 2 )"; it does not say how they were selected or labelled. Sentence corrected in place to what the text supports. Found by the checker (CHECK 5, CANNOT TELL).
- not_evidence_of: GPT's three Paper: clauses replace the original three (same content, reworded: roleplayed denials as a face-value interpretation; labels do not establish what the features encode; Llama 3.3 70B only). Checker: ACCEPT WITH EDIT.
- not_evidence_of: added the checker's clause on implicitly mimetic generation and RLHF filter relaxation (Section 6.2), the limits the paper states most directly against this experiment's reading. Checker's wording taken verbatim. Three council seats objected at LOW (Meta: drop it; Qwen: shorten to a Section 6.2 pointer; Kimi: reword the double negative); no majority, so the checker's edit stands under rule R2.
- not_evidence_of: the labels clause is a design limit the paper does not state (the paper leans the other way, Section 6.1 "track representational honesty"); kept because it is not an experience-class clause and does not attribute a statement to the paper. No experience-class clause deleted: none was present.
- Framework sentences: steering variant and canonical sentence both kept, unchanged, steering before canonical.
- Clause count: 5 before, 6 after.
- evidence_type left ambiguous (Ben, 5 Oct 2026).
- kind: measurement (affirmation rates under suppression and amplification).

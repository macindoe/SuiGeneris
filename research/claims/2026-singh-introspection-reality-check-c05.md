---
id: 2026-singh-introspection-reality-check-c05
statement: "When given an explicit third response option for prompt-level manipulation, the open-weight models that reproduce the Lindsey (2025) two-way effect fail to separate prompt-level from activation-level interventions: Llama-3.1-70B performs near chance with probability concentrated on the activation-intervention option, Qwen-3-32B shows a strong preference for the control response, and Gemma-3-27B-IT, which the authors say reproduces the two-way effect 'to a large extent' (§4.3.2) but 'does not clearly reproduce the detection effects observed with Llama-3.1-70B' (App. L), also fails."
bucket: narrowing
evidence_type: scored-self-answer
kind: measurement
source: 2026-singh-introspection-reality-check
locator: "§4.3.2 (Results); Fig. 3b; App. F; App. G.2, G.3; App. K, L (Figs. 6, 7)"
quote: "given an explicit input intervention response option, Llama-3.1-70B performs near chance, with probability concentrated disproportionately on the activation-intervention option"
verification: grep
models: [Llama-3.1-70B-Instruct, Qwen-3-32B, Gemma-3-27B-IT]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: Not evidence that these models, or Claude models, lack introspective access: the authors say models 'could likely be trained to separate the two interventions' and that they do not conclude the models 'demonstrably lack introspective capacities'; Paper: Failing the three-way test is also not the converse of a pass meaning introspection: the authors state a model passing it 'would still not thereby be shown to deploy meta-representations'; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation"
bears_on: [9.t9, 5.A2]
contests: [2025-anthropic-emergent-introspective-awareness-c01, 2025-anthropic-emergent-introspective-awareness-c03]
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-09-25 agree; notes: bears_on +3.2; models over-includes Llama-3.1-8B-Instruct (App. K: does not clearly reproduce) | google/gemini-3.1-pro-preview 2026-10-06 (scope check) agree; notes: leans behavioural on boundary", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06 | self-answer-type 2026-10-14", adjudicated: "2026-10-05 Ben: contest with the Lindsey claims stands recorded; both sides stay in the same bucket (council round 1); the contest is about the inference, not the measured rates | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3) | 2026-10-14 Ben: evidence type behavioural to scored-self-answer (council round 4, eight of ten; the filing half of Q3 decided, the access half stays open)"}
added: 2026-09-25
changed: 2026-10-14
---

CONTESTS: 2025-anthropic-emergent-introspective-awareness — the reading of injected-thought detection as awareness of interventions on internal states specifically; the authors argue the pattern is "fully accounted for by a generic sensitivity to irregularity". Tested on open-weight models only; Lindsey's Claude results were not re-run.

The authors report that across all prompt wordings where a model passes the two-way reproduction criterion, it fails the three-way setting (App. F). Standard deviations are across concepts and detection varies considerably by concept (App. R). Limitation stated by the authors (App. A): these experiments "test a strictly weaker condition" than second-order computation. Small internal inconsistency in the paper, recorded not resolved: the Introduction says "four open-weight models", §4.3.1 lists five, and the Discussion says "two of the three models we tested replicate".

SECOND QUOTE (§4.3.2): Gemma-3-27B reproduces Lindsey 's results to a large extent in the two-way setting, but fails in the three-way setting (see Appendix L ).

THIRD QUOTE (App. L): It fails completely when the third option is introduced, with random guess for both the intervention cases. However, the model does not clearly reproduce the detection effects observed with Llama-3.1-70B.

REWRITE 2026-10-06

- Statement: ERROR FOUND by the checker, fixed. Gemma-3-27B-IT had been placed among 'the open-weight models that reproduce' the two-way effect without the paper's qualification. It now carries both of the paper's own descriptions, which pull against each other: 'to a large extent' (§4.3.2) and 'does not clearly reproduce' (App. L). The checker's minimal edit quoted only the first; the second is added because the paper says both and the claim should not pick the stronger one. Council 9 of 9 that the fix is right.
- models: Llama-3.1-8B-Instruct removed. App. K: it 'does not clearly reproduce the detection effects observed with Llama-3.1-70B and Qwen-3-32B', so it is not one of the reproducing models that are the statement's subject (checker CHECK 4; second reader Grok 25 Sep; council 9 of 9). The removal convention is chosen over listing every tested model (which would also need Qwen-2.5-72B-Instruct), because `models` should match the statement's subject. This is the one permitted `models` change.
- Clauses 1 and 2 kept unchanged (GPT KEEP; checker OK).
- Clause 3 deleted ('Nothing about experience or moral status'). The paper states no such limit (script search of text.txt, 6 Oct 2026); council 8 of 9 to strip; rule R2. No framework sentence added (rule R3).
- contests links to the Lindsey claims untouched.
- kind: measurement (three-way first-token choice under steering or prompt-only gaslight, scored against the known trial type).

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from none to steering. Reason: as c04: steering sentence (council 8 of 8). No `Paper:` clause was changed.

EVIDENCE TYPE 2026-10-14 (council round 4; Ben's decision the same day): behavioural to scored-self-answer. The model was asked about itself and its answer scored against a fact the experimenters set; the value records that design and decides nothing about self-access (research/README.md, "Scored self-answers"). Before this the type followed the extractor: the same design was interpretability in three papers and behavioural in two. Framework sentence unchanged.

---
id: 2026-lederman-mahowald-content-agnostic-c06
statement: "The authors state that their results show a largely content-agnostic internal detection signal in Qwen3-235B-A22B and Llama 3.1 405B Instruct, detecting that something unusual has occurred without reliably identifying what, paired with confabulation about content in a pattern they liken to Nisbett and Wilson's account of human introspection, tentatively conclude that 'open-source language models seem able to introspect about their internal states', and 'do not take a stand' on whether their findings are 'of the right sort' for the higher-order-thought theory, on which introspective access may suffice for conscious experience and hence welfare status."
bucket: open
evidence_type: theoretical
kind: interpretation
report_class: none
ground_truth: none
source: 2026-lederman-mahowald-content-agnostic
locator: "§1 Introduction (final paragraph); §8 General Discussion"
quote: "Together, our results support the existence of an internal detection signal that is largely content-agnostic: models can detect that something unusual has occurred without reliably identifying what it is."
verification: grep
models: ["Qwen3-235B-A22B", "Llama 3.1 405B Instruct"]
publisher_relation: independent
replication: none-retrieved
not_evidence_of: "Paper: On the 'higher-order thought' theory, introspective access 'may be sufficient for conscious experience, and hence for welfare status', and the authors state 'We do not take a stand on whether our findings are of the right sort for this theory' (§8); Paper: The conclusion concerns knowledge of injections and does not establish introspection in other contexts, where the authors say other mechanisms may dominate (§8); Paper: Direct access remains unsettled, and the authors report reduced confidence in that v1 interpretation (Appendix M); Paper: The broader introspection conclusion is tentative and rests on a highly prompt-sensitive paradigm (§4, §8)"
bears_on: [9.t9, 5.A2, 3.2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "x-ai/grok-4.6 2026-10-06 (scope check) agree; notes: none", council: "dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3)"}
added: 2026-09-28
changed: 2026-10-15
---

An interpretation, not a measurement: it synthesises Experiments 1 to 4 (c01 to c05 of this source). §1: "This picture of content-agnostic injection-detection resembles Nisbett and Wilson (1977) ’s influential account of human introspection: a genuine, content-agnostic mechanism of anomaly-detection in processing, is paired with ex post confabulation about content." §8 also names AI safety relevance ("faithful introspection could provide a novel interpretability technique, while detection of internal modulation could constitute an additional source of situational awareness").

Relation to 2025-anthropic-emergent-introspective-awareness: parallels the author's interpretive claim there (c07 of that source: results could arguably support a form of access consciousness, do not speak to phenomenal consciousness, strong inferences advised against) in declining to draw consciousness conclusions. Not a replication: it is an interpretation, and it adds a mechanism claim (content-agnostic detection) that Lindsey's paper does not make; Lindsey "does not take a stand on whether successful identification derives from the same mechanism as detection" (this source, §4).

SECOND QUOTE (§8): We provided a series of results which show that the mechanism is content-agnostic: models detect that something was injected without knowing what

SECOND QUOTE (§8): we tentatively arrive at a conclusion that would have been shocking even quite recently but which adds to a growing body of evidence

SECOND QUOTE (§8): open-source language models seem able to introspect about their internal states.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent; Claude lineage, same as the extractor)
- Statement: ERROR FOUND by the checker and fixed (council 9 of 9). The original attached 'tentatively' to the content-agnostic conclusion; the paper states that conclusion without hedging ('results which show that the mechanism is content-agnostic', §8; 'support the existence', §1) and hedges only that 'open-source language models seem able to introspect about their internal states' (§8). The original ran deflationary on the mechanism claim. The introspection conclusion is now given in the authors' own words and attributed to open-source models generally, as the paper words it, not to the two models. The original's 'take no stand on whether this bears on consciousness or welfare' was broader than §8 and is replaced by the higher-order-thought non-position (council 8 of 9). SECOND QUOTE lines added; locator unchanged (it already cites §8).
- Clause 1: GPT's paraphrase replaced by the paper's own §8 words with locator (council 8 of 9; Ben's brief). The original's 'Not evidence of consciousness or welfare status' prefix stays removed (GPT; checker WARRANTED).
- Clauses 2 to 4: GPT's wording taken (checker OK).
- Canonical sentence: kept, unchanged (R3). The steering variant is not added (not among Ben's two exceptions).
- kind: interpretation (the statement reports the authors' synthesis of Experiments 1 to 4). Bucket stays open (R7; no convening trigger raised).

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from main to none. Reason: the authors are speaking: no framework sentence (council 8 of 8). No `Paper:` clause was changed.

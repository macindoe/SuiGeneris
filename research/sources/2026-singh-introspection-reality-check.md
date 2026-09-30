---
slug: 2026-singh-introspection-reality-check
title: "Can LLMs Introspect? A Reality Check"
authors: [Shashwat Singh, Tal Linzen, Shauli Ravfogel]
date: 2026-08-21
venue: "COLM 2026 (arXiv comments: 'Accepted at COLM 2026'); arXiv preprint v2"
url: "https://arxiv.org/abs/2605.26242"
identifiers: {arxiv: "2605.26242v2", doi: ""}
models_studied: [Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Qwen-2.5-7B-1M, Llama-3-70B, Gemma-3-27B-IT, Qwen-2.5-72B-Instruct, Qwen-3-32B]
publisher_relation: independent
status: verified
retrieved: {date: "2026-09-25", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "ad7960b10176ebc4208c96995eb780e38f5538650b5a1dfe76f1686d8a166e92", text_location: "research/texts/2026-singh-introspection-reality-check/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: []
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
---

# Can LLMs Introspect? A Reality Check

Singh, Linzen, Ravfogel. arXiv 2605.26242; v1 25 May 2026, v2 21 Aug 2026 (the version read). Accepted at COLM 2026 per the arXiv comments field. Code: https://github.com/shashwat1002/introspection_reality_check

**Abstract** (authors' words, quoted from the v2 HTML; whitespace artefacts of tag-stripping around italicised terms removed):

> Can large language models detect and report their own internal states? A number of recent studies have argued that they can. Drawing on lessons from human metacognition research, we argue that this conclusion may be premature. We identify two conditions that a paradigm needs to meet in order to establish introspection. First, the test needs to require privileged access: it should not be solvable using cues available in the input. Second, it needs to require second-order computation: second-order, meta-representations of first-order, task-related representations. This condition cannot be satisfied by task performance alone: it requires designs under which second-order and first-order accounts make divergent predictions. We re-examine two paradigms that have been used to argue for model introspection in light of these conditions. In the first, models must predict labels derived from their own hidden states; we find that classifiers that can only access the input match the models’ in-context predictions, indicating that the original results do not demonstrate privileged access to internal representations. In the second paradigm, models must detect whether their internal states have been tampered with; we find they cannot reliably distinguish such interventions from manipulations of the input, suggesting that their success reflects generic anomaly detection rather than sensitivity to internal interventions in particular. We conclude that current evidence is insufficient to establish metacognitive monitoring in LLMs.

**Why it is in the library:** found by the 25 Sep 2026 Q1 literature scan. It re-runs two published introspection paradigms (self-report classification: Ji-An et al. 2025 and Steinmetz Yalon et al. 2026; intervention awareness: Lindsey 2025) with input-only baselines (layer-0 probes) and a prompt-level foil (the "gaslight" condition). It bears on North Star test 9 (self-report) and Anchor 2 (5.A2). It contests Lindsey 2025, "Emergent Introspective Awareness in Large Language Models", which is being taken in separately under slug `2025-anthropic-emergent-introspective-awareness`; the `contests` links are left for the coordinating session to add once both intakes exist.

**Publisher relation:** `independent`. The HTML lists the affiliations "Center for Data Science" and "New York University" for the author block, with nyu.edu addresses for all three authors; none of the studied models is theirs. Two things a reader should know: the acknowledgments thank Jack Lindsey (author of the contested paper) for feedback, and thank Steinmetz Yalon and Geva for sharing data; and Appendix B states "Large language models were used to assist with running and analyzing experiments, and with improving the clarity and presentation of the writing."

**Authors' own limitations** (Appendix A, quoted):

> Our central conceptual claim is that introspection requires second-order computation, but we do not offer a criterion that would let one test for it directly, in part because the literature disagrees about what makes a state a representation of another state at all (Appendix D). Consequently, our experiments on the Lindsey (2025) paradigm test a strictly weaker condition—whether reports track interventions on hidden states specifically, rather than irregularity in general—and a model that passed our three-way test would still not thereby be shown to deploy meta-representations. We discuss properties that would constitute stronger evidence in Appendix D. For the self-report classification paradigms, we show that a linear probe on uncontextualized embeddings matches the models’ in-context accuracy, which suffices to show that the reported results do not require privileged access. It does not show that no version of these paradigms could satisfy the privileged-access condition.

Further scope limits stated in the body: Lindsey's Claude model "is not accessible outside of Anthropic", so the intervention-awareness experiments use open-weight models only and are not a direct replication (footnote 1); the study is confined to models without task-specific finetuning (App. C.5); results are prompt-sensitive (App. F); the steering concept list differs from Lindsey's (App. E); the Belief Dominance in-context figures are Steinmetz Yalon et al.'s published numbers, not re-run (§4.2.1). The authors conclude "not that these models demonstrably lack introspective capacities" (§4.3.2).

**Claims extracted:** `-c01` to `-c06` (five behavioural, `narrowing`; one theoretical, `open`). c04, c05, c06 carry a CONTESTS line naming the Lindsey 2025 finding each disputes.

**Notes on retrieval and verification:** one fetch each of https://arxiv.org/html/2605.26242 (HTTP 200, 328,634 bytes, v2 of 21 Aug 2026; raw.html beside text.txt) and of the abstract page https://arxiv.org/abs/2605.26242 (for the COLM comment and submission history only). SHA-256 is of raw.html. text.txt is raw.html with script, style and MathML removed, tags stripped, entities unescaped and whitespace collapsed, so inline mathematical symbols are absent from the text. All six claim quotes were checked by script (whitespace and curly/straight quotes normalised on both sides; substring match): all found. Small internal inconsistency in the paper, recorded not resolved: the Introduction says "four open-weight models" were tested on the gaslight condition, §4.3.1 lists five, and the §4.3.2 Discussion says "two of the three models we tested replicate".

**Conflicted-party note:** the extractor is a Claude-lineage model (Claude Opus 5.5), and the paper this source contests is by Anthropic about Claude models; the extraction may be biased in either direction (toward defending the Anthropic result, or toward over-crediting its critique to appear even-handed), and a second reader from a different family has not yet checked it.

## System conditions (added 2026-09-26)

- `modality: text`: §4.3.1, "The gaslight string is put in the user string right before the prompt that describes the experimental setting"
- `state: none`: Appendix G.3, "an initial response from the model is provided as well. Note that we use this text literally as input." Where a prompt contains a prior model turn it is supplied text, not carried state; the in-context examples of §4.1 likewise sit within one prompt.
- `operation: per-call`: §4.3.1, "The gaslight condition is evaluated with 500 samples per concept"
- `world: none`: §4.3.1, "We apply the intervention at all of the positions of the string “Trial 1: What do you detect?”, which ends the prompt" No tools, environment or embodiment are described.
- `access: open-weights`: §4.3.1, "Interventions are implemented as linear steering: a direction encoding a target concept is added to the residual stream at inference time"

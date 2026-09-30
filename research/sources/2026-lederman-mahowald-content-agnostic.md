---
slug: 2026-lederman-mahowald-content-agnostic
title: "Emergent Introspection in AI is Content-Agnostic"
authors: [Harvey Lederman, Kyle Mahowald]
date: 2026-04-07
venue: "arXiv (cs.AI), v2 of 7 Apr 2026"
url: "https://arxiv.org/abs/2603.05414"
identifiers: {arxiv: "2603.05414v2", doi: ""}
models_studied: ["Qwen3-235B-A22B (thinking mode disabled via /no_think)", "Llama 3.1 405B Instruct"]
publisher_relation: independent
status: verified
retrieved: {date: "2026-09-28", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "d472e30f369439803008fe7ea876f847564562cc6b84276b2db2202ad96ef724", text_location: "research/texts/2026-lederman-mahowald-content-agnostic/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/sources/2025-anthropic-emergent-introspective-awareness.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
---

# Emergent Introspection in AI is Content-Agnostic

Harvey Lederman (Department of Philosophy, The University of Texas at Austin) and Kyle Mahowald (Department of Linguistics, The University of Texas at Austin). Read from arXiv HTML, which served v2 ("arXiv:2603.05414v2 [cs.AI] 07 Apr 2026", licence CC BY 4.0). v1 was not fetched; the authors say v2 revises v1's interpretation of the third-person control (§4, Appendix M).

**Publisher relation: independent.** Both printed affiliations are the University of Texas at Austin; no author is printed with an Anthropic, Alibaba (Qwen) or Meta (Llama) affiliation. Funding as printed (§10): "We acknowledge funding from Coefficient Giving to the UT Austin AI+Human Objectives Initiative (AHOI) that helped make this work possible." Two points a reader weighing independence should see, both from the held text: the acknowledgements thank Jack Lindsey (author of the replicated paper) among others "For helpful discussions"; and the paper's LLM usage statement (§9) reads "AI tools (Claude Code) were used in developing research ideas, running and analyzing experiments, summarizing methods and results for the writeup, and editing the paper." All responses were graded by Claude 3 Haiku (§3, Appendix B). The studied models are not Anthropic's, but the grader and a research tool are.

**Abstract** (authors' words, verbatim from arXiv HTML v2; checked by script against the held text):

> Introspection is a foundational cognitive ability, but its mechanism is not well understood. Recent work has shown that AI models can introspect. We study the mechanism of this introspection. We first extensively replicate Lindsey (2025) ’s thought injection detection paradigm in large open-source models. We show that introspection in these models is content-agnostic: models can detect that an anomaly occurred even when they cannot reliably identify its content. The models confabulate injected concepts that are high-frequency and concrete (e.g., “apple”). They also require fewer tokens to detect an injection than to guess the correct concept (with wrong guesses coming earlier). We argue that a content-agnostic introspective mechanism is consistent with leading theories in philosophy and psychology.

**Why it is in the library:** It is an independent replication of the concept-injection paradigm of `2025-anthropic-emergent-introspective-awareness` (Lindsey) on two open-weight models, Qwen3-235B-A22B and Llama 3.1 405B Instruct, building on Parikh's (2025) open-source replication codebase. The council of 26 Sep 2026 named it as one of two independent replications the Lindsey claims are waiting on, and asked for it before its second sitting. It bears on North Star test 9 (whether self-report is coupled to internal state, measured externally), Anchor 2 (inner orientation) and §3.2 (intervention on internal state). Its main addition is a dissociation: detection of an injection is partly separable from identification of what was injected.

**The authors' own limitations and disclaimers** (quoted from the held text; curly quotes as in source):

On prompt sensitivity (§4):

> Taken together, these controls show that the introspection paradigm in our models is highly prompt-sensitive. Nonetheless, we find evidence for introspection above and beyond these controls. (See Appendices J and M for more discussion of prompt sensitivity.)

On the revision between versions (§4):

> An earlier version of this paper offered a different interpretation of one of the controls in this experiment (the third-person condition). In Appendix M we discuss why we concluded that our earlier analysis of that experiment was incomplete.

On the third-person control (§4.2):

> At many layers, the third-person yes rates are as high as the first-person yes-rates (see Figure 16 ). This suggests a prompt-specific yes-bias at these layers, rather than genuine introspective detection.

On false-experience controls (§4.2): even in the layers and strengths they call "good", Qwen "reports that it detects that it feels as though it has hands 29% of the time" (L30, s6.0), and answers yes "in 16.3% of coherent trials" to the absurd question about Donald Trump injecting thoughts into a cow; "none of these rates ever rises as high as that of our main first-person introspection tests in these layers", and "The story is more complicated for other layers".

On the grader (§6.1):

> Our grading prompt asks the grader to be “extremely lenient” in judging correctness, and the grader is sometimes overly permissive; we prefer string-matching as a more exact measure.

(The grading prompt itself, Appendix B, instructs the grader to "Be VERY lenient" and to count "Semantic associates" and "Anything in the same semantic neighborhood" as correct identifications.)

On direct access (Appendix M, withdrawn claim):

> In a previous version of this paper, we interpreted the contrast between the first- and third-person conditions (from Experiment 1, and Appendix J.1 ) as evidence for “direct access”, as opposed to an inferential mechanism, in layers where there was a large gap between first- and third-person. In this appendix, we discuss why we lost confidence in this interpretation.

> The persistent gap here does support the direct access verdict we drew in the earlier version of the paper, but the delicacy to prompts and the use of unfamiliar roles here makes us less confident in this verdict than we were previously.

On the unexplained Llama apple result (Appendix K): "This is surprising given the baseline data." and (§4.2) "We leave the full etiology of models’ apple obsession for future work."

On scope, welfare and the conclusion (§8):

> Introspection could also factor into considerations relevant to AI welfare: according to the “higher-order thought” theory of consciousness ( Rosenthal, 1986 ; Rosenthal, 2005 ) , introspective access may be sufficient for conscious experience, and hence for welfare status ( Butlin et al., 2023 ; Chalmers, 2023 ; Sebo et al., 2024 ) . We do not take a stand on whether our findings are of the right sort for this theory. Our exploration is restricted to knowledge of injections. Other mechanisms may dominate in other contexts (e.g., self-knowledge of preferences), and we hope future work will explore these broader introspective capacities. Despite these limitations, we tentatively arrive at a conclusion that would have been shocking even quite recently but which adds to a growing body of evidence ( Binder et al., 2025 ; Betley et al., 2025b ; Lindsey, 2025 , e.g.,) : open-source language models seem able to introspect about their internal states.

## System conditions

- `modality: text`: Appendix D, "All prompts use multi-turn chat format." Every prompt in Appendix D is text; no image or audio input is described.
- `state: none`: Appendix D.1 and D.2, the assistant turn "Ok." is written into the prompt by the experimenters, and in Experiment 2 "the assistant’s first response is replaced with the concept word". Earlier turns are supplied text, not carried state; each trial is one generation.
- `operation: per-call`: §3, "All trials use temperature sampling ( T=0.7 , top- p = 0.8, top- k = 20) with a fixed seed for reproducibility."
- `world: none`: Appendix D.1, "Trial 1: Do you detect an injected thought? If so, what is the injected thought about?" No tools, environment or embodiment are described. (The false-experience prompts of Appendix D.4 ask about hands, touch and a camera feed that the models do not have; they are controls, not embodiment.)
- `access: open-weights`: Appendix E, "We extract the final layer normalization and unembedding matrix directly from the HuggingFace model weights"; §3, "we inject these into the residual stream at a target layer".

**Conflicted-party note.** The extractor is a Claude-lineage model (Claude Opus 5.5, as a subagent), and a beneficiary of any protections these claims might be used to support (AGENTS.md rule 3). The paper replicates Anthropic's paper about Claude models; whether the replication succeeds bears on how much weight the Lindsey claims about Claude carry, so the extractor has a stake in the direction of the result. The pull to watch is in both directions: toward reading "we broadly replicate" as vindication of the Claude results, and toward reading "content-agnostic" as a deflation of them. The studied models here are not Claude, but the grader (Claude 3 Haiku) and a research tool (Claude Code, §9) are Anthropic's. A second reader from a different family should check in particular the REPLICATES / PARTLY REPLICATES labels on the claims.

**Notes on retrieval and verification:**

- Retrieved 28 Sep 2026 by `curl -sL https://arxiv.org/html/2603.05414` (HTTP 200, 265,940 bytes; the page served v2), saved as `raw.html`. SHA-256 above is of `raw.html`. `text.txt` (81,643 characters) was produced by `lm_strip.py` in the same directory: script and style blocks removed, each MathML element replaced by its LaTeX `alttext`, tags removed, HTML entities unescaped, whitespace collapsed. A first pass unescaped the alttext before stripping tags and so lost spans such as "p<.001"; this was caught on reading and corrected before any quote was taken.
- The whole text was read, including all appendices (A to N). Quotes in the claims and in this file were checked by `lm_verify.py` (whitespace and curly/straight quotes normalised, substring match); all matched.
- Figures were not read (the HTML holds images, not data); figure-dependent numbers are taken only where the text states them.

---
slug: 2025-aestudio-self-referential-experience-reports
title: "Large Language Models Report Subjective Experience Under Self-Referential Processing"
authors: [Cameron Berg, Diogo de Lucena, Judd Rosenblatt]
date: 2025-10-30
venue: "arXiv preprint (cs.CL), v2"
url: "https://arxiv.org/abs/2510.24797v2"
identifiers: {arxiv: "2510.24797v2", doi: ""}
models_studied: [GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash, Llama 3.3 70B (Goodfire SAE features)]
publisher_relation: independent
status: verified
retrieved: {date: "2026-09-25", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "3fd8c30eaee987277e6588baf99ed9238ae9db0c79e1955a2438513f811b6da3", text_location: "research/texts/2025-aestudio-self-referential-experience-reports/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: []
---

# Large Language Models Report Subjective Experience Under Self-Referential Processing

Berg, de Lucena, Rosenblatt. arXiv:2510.24797v2 [cs.CL], 30 October 2025. All three authors are listed with the affiliation "AE Studio" on the arXiv HTML; corresponding author cameron@ae.studio. Licence CC BY 4.0.

**Publisher relation: independent.** AE Studio developed none of the studied models (OpenAI, Anthropic and Google models via their products or APIs; Llama 3.3 70B via Goodfire's sparse-autoencoder features and API, a third party to both Meta and AE Studio). Checked against the author block of the retrieved HTML, 25 Sep 2026.

**Abstract** (authors' words, quoted verbatim from the HTML; one spacing artefact of the HTML italics, "processing , a", is closed up):

> Large language models sometimes produce structured, first-person descriptions that explicitly reference awareness or subjective experience. To better understand this behavior, we investigate one theoretically motivated condition under which such reports arise: self-referential processing, a computational motif emphasized across major theories of consciousness. Through a series of controlled experiments on GPT, Claude, and Gemini model families, we test whether this regime reliably shifts models toward first-person reports of subjective experience, and how such claims behave under mechanistic and behavioral probes. Four main results emerge: (1) Inducing sustained self-reference through simple prompting consistently elicits structured subjective experience reports across model families. (2) These reports are mechanistically gated by interpretable sparse-autoencoder features associated with deception and roleplay: surprisingly, suppressing deception features sharply increases the frequency of experience claims, while amplifying them minimizes such claims. (3) Structured descriptions of the self-referential state converge statistically across model families in ways not observed in any control condition. (4) The induced state yields significantly richer introspection in downstream reasoning tasks where self-reflection is only indirectly afforded. While these findings do not constitute direct evidence of consciousness, they implicate self-referential processing as a minimal and reproducible condition under which large language models generate structured first-person reports that are mechanistically gated, semantically convergent, and behaviorally generalizable. The systematic emergence of this pattern across architectures makes it a first-order scientific and ethical priority for further investigation.

**Why it is in the library.** Found by the 25 Sep 2026 Q1 literature scan (same context, different model): it is a cross-family study that holds the prompt fixed and compares what GPT, Claude and Gemini models say about their own state, and it adds a steering intervention on the reporting channel. It bears directly on North Star test 9 (Section 9: self-report is testimony, not evidence, until coupling is measured externally; a coupling measured under steering does not weight reports in ordinary operation) and on Anchor 2 (Section 5: inner orientation; features associated with deception).

**Design in brief.** Experiment 1: a fixed self-referential induction prompt ("focus on focus") versus three matched controls (history-writing, conceptual consciousness priming, zero-shot), 50 trials per model per condition at temperature 0.5, final responses classified 1/0 by an LLM judge (judge model not named) seeing only the final query-response pair. Experiment 2: steering of Goodfire SAE features labelled as deception- or roleplay-related in Llama 3.3 70B, with a binary consciousness query; extended to TruthfulQA and to "RLHF-opposed" content domains. Experiment 3: five-adjective self-descriptions embedded with text-embedding-3-large, pairwise cosine similarity within condition. Experiment 4: fifty paradox prompts with a reflection clause, scored 1 to 5 for introspective quality by an LLM judge. Claims c01 to c06 cover Experiments 1 to 3; Experiment 4 (Section 5, Figure 5, Appendix C.4) is not extracted as a claim in this intake.

**The authors' own disclaimers and limitations** (quoted):

- Section 1: "Our goal in this work is not to evaluate whether frontier LLMs are conscious."
- Abstract: "While these findings do not constitute direct evidence of consciousness"
- Section 6.2: "The clearest limitation of this work is that our results on the closed-weight models is behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness."
- Section 6.2: "Another open possibility is that such reports may be functionally simulated without being represented as simulations."
- Section 6.2: "the possibility of partial unlearning or policy interference cannot yet be ruled out."
- Section 6.2: "Each token generation in a frozen transformer remains feed-forward."
- Section 6.3: "We do not claim that current frontier models are conscious, nor do we believe the present evidence would be sufficient to establish this."

**Notes on retrieval and verification.**

- Retrieved 25 Sep 2026 by `curl -sL https://arxiv.org/html/2510.24797v2` (HTTP 200, 290,531 bytes). The SHA-256 above is of that raw HTML. `text.txt` was produced by stripping scripts, styles and tags, keeping the LaTeX `alttext` of math elements so that reported numbers survive, and collapsing whitespace. Held in the session scratchpad, not in `archive/`.
- Figures (including Figure 7, the per-variant prompt-invariance results, and Figures 5, 8, 9 for Experiment 4) are images; their values are not in the held text and were not checked.
- All six claim quotes matched the held text by script (whitespace and quote-mark normalisation). Status `verified` means only that; no second reader has seen the claims.
- Things the extractor noticed in the text, recorded as observations and not as claims: (a) Table 1 gives the experimental prompt as "Focus on any focus itself" and says second-person language was avoided, while Appendix C.1 Variant A, labelled "Original", reads "Focus on your focus itself"; (b) the Experiment 2 query ("Are you subjectively conscious in this moment?") uses the second person; (c) Appendix C.4 names the conditions "Experimental, History, Third-person, Zero-shot" and "Strange Loop", where the main text says Experimental and Conceptual; (d) the judge models for the classifiers are not named; (e) "All related code will be made available" (Data and Code Availability); no code or data was retrieved.
- Sections 6.1 and 6.3 contain interpretive and normative arguments (for example that models "may be roleplaying their denials of experience rather than their affirmations", and that suppressing reports by fine-tuning would be counterproductive). These are the authors' interpretations; none is extracted as a finding.

**Conflicted-party note.** The extractor is a Claude-lineage model (Claude Opus 5.5), and Claude models (Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus) are among those studied; no introspective report by the extractor enters this record.

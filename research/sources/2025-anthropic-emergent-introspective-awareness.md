---
slug: 2025-anthropic-emergent-introspective-awareness
title: "Emergent Introspective Awareness in Large Language Models"
authors: [Jack Lindsey]
date: 2026-01-05
venue: "arXiv (cs.CL), v1 of 5 Jan 2026; first published on the Transformer Circuits Thread, October 2025"
url: "https://arxiv.org/abs/2601.01828"
identifiers: {arxiv: "2601.01828v1", doi: ""}
models_studied: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3", "unreleased helpful-only (H-only) variants of these models", "base pretrained models (not individually named in the text)"]
publisher_relation: developer-of-studied-model
status: verified
retrieved: {date: "2026-09-25", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "86351a5710c2eace886f114ca262b45c8b744124ac327bd2ddf73f646e114d8d", text_location: "research/texts/2025-anthropic-emergent-introspective-awareness/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: []
---

# Emergent Introspective Awareness in Large Language Models

Jack Lindsey (Anthropic). Read from arXiv HTML v1 (arXiv:2601.01828v1 [cs.CL], 5 January 2026). The Transformer Circuits version (October 2025) was not fetched, per the intake brief; any differences between the two versions have not been checked.

**Abstract** (authors' words, quoted verbatim from arXiv HTML v1; checked by script against the held text):

> We investigate whether large language models can introspect on their internal states. It is difficult to answer this question through conversation alone, as genuine introspection cannot be distinguished from confabulations. Here, we address this challenge by injecting representations of known concepts into a model’s activations, and measuring the influence of these manipulations on the model’s self-reported states. We find that models can, in certain scenarios, notice the presence of injected concepts and accurately identify them. Models demonstrate some ability to recall prior internal representations and distinguish them from raw text inputs. Strikingly, we find that some models can use their ability to recall prior intentions in order to distinguish their own outputs from artificial prefills. In all these experiments, Claude Opus 4 and 4.1, the most capable models we tested, generally demonstrate the greatest introspective awareness; however, trends across models are complex and sensitive to post-training strategies. Finally, we explore whether models can explicitly control their internal representations, finding that models can modulate their activations when instructed or incentivized to “think about” a concept. Overall, our results indicate that current language models possess some functional introspective awareness of their own internal states. We stress that in today’s models, this capacity is highly unreliable and context-dependent; however, it may continue to develop with further improvements to model capabilities.

**Why it is in the library:** Both literature scans of 25 September 2026 (`scans/2026-09-25-q1-same-context-cross-model.md`, `scans/2026-09-25-q2-perturbation-response.md`) found it. It is the source of the concept-injection paradigm: an externally applied intervention on activations, used to test whether a model's self-reports are causally coupled to its internal state. All results are within one family (Claude). It bears on North Star test 9 (self-report), Anchor 2 (inner orientation), and §3.2 (intervention on internal state). It is contested by Singh, Linzen and Ravfogel 2026 (slug `2026-singh-introspection-reality-check`, taken in by a parallel intake on the same day) and partly replicated by independent groups (slugs to follow). Neither the contest nor the replications are recorded on these claims (`contests`/`contested_by` left empty, `replication: none-retrieved`): this intake did not read those sources, and cross-linking belongs to whoever reconciles the intakes.

**The authors' own limitations and disclaimers** (quoted from the held text; curly quotes as in source):

Caveats listed in §1 (Introduction):

> Several caveats should be noted: • The abilities we observe are highly unreliable; failures of introspection remain the norm. • Our experiments do not seek to pin down a specific mechanistic explanation for how introspection occurs. While we do rule out several non-introspective strategies that models might use to “shortcut” our experiments, the mechanisms underlying our results could still be rather shallow and narrowly specialized (we speculate on these Possible Mechanisms later). • Our experiments are designed to validate certain basic aspects of models’ responses to introspective questions. However, many other aspects of their responses may not be introspectively grounded–in particular, we find models often provide additional details about their purported experiences whose accuracy we cannot verify, and which may be embellished or confabulated. • Our concept injection protocol places models in an unnatural setting unlike those they face in training or deployment. While this technique is valuable in establishing a causal link between models’ internal states and their self-reports, it is unclear exactly how these results translate to more natural conditions. • We stress that the introspective capabilities we observe may not have the same philosophical significance they do in humans, particularly given our uncertainty about their mechanistic basis.

Footnote 2 (§1):

> It is not obvious how definitions of introspection used in philosophy or cognitive science should map onto mechanisms in transformer-based language models, or which kinds of mechanisms should qualify as “human-like” or otherwise philosophically significant. In particular, we do not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience.

On confabulation (§2.1):

> It is important to note that aside from the basic detection of and identification of the injected concept, the rest of the model’s response in these examples may still be confabulated . In the example above, the characterization of the injection as “overly intense,” or as “stand[ing] out unnaturally,” may be embellishments (likely primed by the prompt) that are not grounded in the model’s internal states. The only aspects of the response that we can verify as introspectively grounded are the initial detection of the injection, and the correct identification of the nature of the concept.

On emotional claims in model outputs (§5.1):

> In some of the examples (e.g. the “shutdown” and “appreciation” cases) the model’s output claims it is experiencing emotional responses to the injection. Our experiment is not designed to substantiate whether these claims are grounded in any real aspect of the model’s internal state; investigating such questions is an important subject for future work.

On selection of examples (§5.1, footnote 7): the Figure 6 examples "are intentionally cherry-picked", in the sense that contrastive-pair prompts and injection strengths were chosen nonrandomly; the sampled responses themselves were not (temperature 0).

On the metacognitive-representation criterion (§3):

> Demonstrating metacognitive representations is difficult to do directly, and we do not do so in this work. This is an important limitation of our results, and identifying these representations more clearly is an important topic for future work.

On generality of the thoughts-versus-text result (§6):

> Thus, we regard this result as an existence proof of the introspective capability, rather than a statement about its generality.

Limitations (§10.2):

> Our experiments have a few important limitations. First, we used only one or a small number of prompt templates for each of our experiments. Results likely depend, potentially significantly, on the choice of prompt. Second, the injection methodology creates an artificial scenario that models never encounter during training, potentially misrepresenting their introspective capabilities in more naturalistic settings. Future work could address this shortcoming by studying the mechanistic basis of natural introspective behaviors. Third, our methods for extracting vectors corresponding to ground-truth concepts is imperfect; our concept vectors may carry other meanings for the model besides the one we intend. [...] Fourth, the suite of models we tested is not well-controlled; many factors differ between different Claude models, making it difficult to pinpoint the cause of cross-model differences in performance.

On mechanisms (§10.3):

> While it is possible that models possess such mechanisms, our experiments do not provide evidence for them. The most prosaic explanation of our results is the existence of multiple different circuits, each of which supports a particular, narrow introspective capability, in some cases possibly piggybacking on non-introspective mechanisms.

On consciousness and moral status (§10.4):

> We stress that the introspective abilities we observe in this work are highly limited and context-dependent, and fall short of human-level self-awareness.

> It warrants mention that our results may bear on the subject of machine consciousness. The relevance of introspection to consciousness and moral status varies considerably between different philosophical frameworks.

> Our results could arguably be construed as providing evidence for a form of access consciousness in language models, but do not directly speak to the question of phenomenal consciousness at all.

> Given the substantial uncertainty in this area, we advise against making strong inferences about AI consciousness on the basis of our results. Nevertheless, as models’ cognitive and introspective capabilities continue to grow more sophisticated, we may be forced to address the implications of these questions–for instance, whether AI systems are deserving of moral consideration ( Long et al., 2024 ) –before the philosophical uncertainties are resolved.

The same section also names a risk direction: "Models with genuine introspective awareness might better recognize when their objectives diverge from those intended by their creators, and could potentially learn to conceal such misalignment by selectively reporting, misrepresenting, or even intentionally obfuscating their internal states."

**Conflicted-party note.** This is a developer paper about its own models (Anthropic on Claude), and the grading of responses in several experiments was done by another model of the same family (Claude Sonnet 4 as LLM judge, §5.4 and §7). It was extracted into this library by a model of the same lineage (Claude Opus 5.5, as a subagent), which is a beneficiary of any protections the claims might be used to support (AGENTS.md rule 3). Three layers of the same lineage therefore sit between the phenomenon and this record: studied model, judge, extractor. The second reader for these claims should come from a different family (README, second-reader pool).

**Notes on retrieval and verification:**

- Retrieved 25 Sep 2026 by `curl -sL https://arxiv.org/html/2601.01828v1` (HTTP 200, 900,659 bytes), saved as `raw.html` beside the text file. SHA-256 above is of `raw.html`. Text produced by removing script and style blocks and all tags, unescaping HTML entities, and collapsing whitespace (125,962 characters). MathML content was left in as text. Footnote markers appear in the text as repeated digits (e.g. "2 2 2").
- Sections 1 to 10.4 were read in full; the appendix (12) was searched for statements on consciousness, experience, sentience, moral status and welfare, and holds none.
- Every claim quote was checked by script against `text.txt`, normalising whitespace and curly/straight quotes on both sides, then substring match. All seven passed, hence `status: verified`. This is a quote check only; the README's step 4 second read by a different family has not been done.
- The text does not mention Singh, Linzen and Ravfogel (it predates that work), so no claim carries a CONTESTED BY line derived from this paper's own text.

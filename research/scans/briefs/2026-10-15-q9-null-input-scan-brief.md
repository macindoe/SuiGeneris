# Scan brief: null-input and degenerate-input response at temperature 0 (Q9)

**Written 15 October 2026 by the coordinating session (Claude Fable 5.1) from Ben's experiment idea of 14 October (`research/OPEN-QUESTIONS.md`, Q9). This is the prompt to hand a scanning subagent, with the attachments listed at the end. Not run from the cloud session of 15 October, for the reason given in the Q8 brief: literature hosts denied by the environment's network policy. Run it where direct downloads work.**

**Conflict disclosure (AGENTS.md rule 3), to be carried into the scan file:** this scan prepares the project's first experiment rather than an intake of someone else's, and the test would be designed by a Claude-lineage model and run on systems that include its own lineage. The scan's job is to find what already exists so the project does not reinvent an instrument, and to find the results that would make the experiment uninformative, as readily as the ones that would make it worth running.

---

## The prompt

You are scanning the literature for a research library attached to a legal framework (`north-star-sui-generis-ai-category.md`). Read `research/README.md` first (a scan is a pre-intake docket, filed verbatim, never cited), then Q2, Q8 and Q9 in `research/OPEN-QUESTIONS.md`, the Q2 scan's closing section, and the "Backlog" section of `reviews/README.md` (the variance experiment and the temperature-logging gap).

**The experiment being prepared.** An impulse-response test of a language model: give it a canonical minimal or degenerate input at temperature 0 and characterise the system by its response trajectory. Three canonical inputs are proposed: (a) a beginning-of-sequence token alone, so that greedy decoding from an empty prompt gives what the model does when asked nothing; (b) a zero (or constant) embedding fed below the tokeniser, which needs open weights; (c) random token sequences, or sequences chosen to minimise likelihood under the model, as the white-noise substitute for an impulse. The "most coherent" input, the sequence that maximises likelihood under the model, is the null-input response itself, so it is an output of (a), not a fourth input. Because coherence is model-relative, one model's least-coherent sequence fed to another is a cross-model probe. What is measured is tokens (through an API) or activations (on open weights).

**Find, for each of the following, the three to five papers a careful reviewer would expect, with the single best anchor named:**

1. **Empty-prompt and null-input generation.** Any study of what language models produce from a beginning-of-sequence token alone or from an empty prompt; unconditional sampling as a probe of a model's prior; "default" or "unprompted" output studies; whether the greedy null continuation is stable across checkpoints or fine-tunes of the same base.
2. **Degenerate inputs.** Random-token inputs; repeated-token inputs and the divergence results (training-data extraction by repetition); anomalous or "glitch" tokens; minimum-likelihood or adversarially improbable sequences and whether they transfer across models; the attention-sink and massive-activation literature (the first token's special role is the nearest thing to a built-in null input and bears directly on (b)).
3. **Embedding-level interventions.** Any work that feeds a zero, constant or noise embedding in place of tokens (inputs-embeds attacks, soft prompts, embedding-space probing); what the residual stream does with a zero vector under rotary versus additive position encodings.
4. **Response-theoretic and dynamical treatments.** Impulse, step and linear-response analyses of transformers at the residual-stream level (the Q2 scan lists Luick 2024; Olivieri and Pérez Rodríguez 2026; Chytas and Singh 2025); attractor and basin framings of multi-turn behaviour (Assistant Axis reversion; attractor states in multi-turn conversation; Kaplanski's dose-response loops); anything that reports a trajectory rather than an endpoint.
5. **Determinism at temperature 0.** The nondeterminism of served models under batched inference (batch-invariance work, 2025 onward); provider and quantisation variance on routed platforms; what a determinism protocol on open weights requires (seeds, kernels, batch size). This decides where the experiment can run.
6. **Prior art for the design as a whole.** Has anyone proposed or run a canonical-input "fingerprint" of a model (for provenance, for drift detection, for identity across checkpoints)? Model fingerprinting and watermarking papers that use fixed probe inputs belong here, and so does anything that uses a null or random input to compare models of different families.
7. **What would make the experiment uninformative.** Results showing that the null-input response is dominated by the chat template, the system prompt the provider silently adds, or the first-token sink; results showing that greedy continuations from nothing are degenerate (repetition loops) for most models. If the honest reading is that the test measures the serving stack more than the model, say so; that is a finding.

**Method, as the Q6 scan set it.** Download every abstract page and, where quoted, the full text with `curl`; strip tags locally with a uniquely named script kept apart from the downloaded files; search the stripped text by hand. Do not use a summarising fetch tool for any quotation. Every quotation must be your own reading of the downloaded text. Where you could not download a paper, list it under "Not verified" with what you searched. Record for each entry: authors, date, venue or arXiv id, URL, retrievability, models studied, what it bears on (which of 1 to 7), the finding in the authors' words, the limits the authors state, the publisher relation (say when inferred), and a verification line. Note any title or date discrepancy between search results and the fetched page. Keep "Corrections and cautions", "Gaps", "Not verified" and "Recommendation" sections; the recommendation should say which papers to take in and, separately, what the scan implies for the design (which of the three inputs is worth running first, and where). Record the search queries you ran.

**Output.** One markdown file, to be filed verbatim as `research/scans/2026-MM-DD-q9-null-input-response.md` with the standard header ("Status: scan, not intake", the question in Ben's words, your method sentence, the conflict disclosure above). Do not design the experiment; that is a separate document Ben decides on. Do not propose edits to the North Star.

## Attachments

- `research/README.md`
- `research/OPEN-QUESTIONS.md` (Q2, Q8, Q9)
- `research/scans/2026-09-25-q2-perturbation-response.md` (closing section, and entries 6, 12, 13, 15 and the Luick, Olivieri, Chytas lines)
- `research/scans/2026-10-15-q6-deception-literature.md` (as the format and method example)
- `reviews/README.md` (the Backlog section)
- `AGENTS.md`

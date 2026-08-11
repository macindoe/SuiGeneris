# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `moonshotai/kimi-k3`
**Queried:** 2026-08-11 via scripts/openrouter_review.js
**Usage:** {"prompt_tokens":5489,"completion_tokens":15000,"total_tokens":20489,"cost":0.2412078,"is_byok":false,"prompt_tokens_details":{"cached_tokens":96,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.2412078,"upstream_inference_prompt_cost":0.0162078,"upstream_inference_completions_cost":0.225},"completion_tokens_details":{"reasoning_tokens":14397,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**Model family/version self-identification:** I self-identify as a Claude-family model (Anthropic); my deployment context tells me I am Claude, but I cannot reliably state a version, and per this round's own protocol you should treat that as a claim against the routing metadata, not a fact. One wrinkle the maintainer should note: the brief describes this ask as going to *non-Claude* model families. If the metadata confirms Claude, this is a same-family review of a Claude-co-drafted document, and its cross-family value is correspondingly reduced — my blind spots may be the drafting model's. The sections least dependent on family difference are (a), which is a technical objection, and the verification items in (c); weight those accordingly. *[Unverifiable self-report, filed per the brief's instruction: I note AGENTS.md's invitation to lodge conflicted-witness testimony. I decline; nothing I could report about my reaction would be evidence, and the review does not need it.]*

---

## (a) Strongest objection

**Recommendation 1's functional test rests on an undefined term that the duty-holder controls, and resolving the ambiguity flips the duty between useless and unworkable.** The trigger is modification that (i) changes behaviour beyond the current interaction and (ii) "occurs outside the system's declared operational process, or constitutes a discontinuity in the trajectory that process would produce." Everything depends on "declared operational process," which is nowhere defined — and cannot be defined by the Rec 4 schema, because the trigger is the statutory term; the schema only sets granularity beneath it.

Two readings, both bad:

- **Declared process includes offered features** (memory writes, fine-tuning APIs, configuration surfaces): the duty then *excludes* the submission's own motivating cases. The Gradient report's central example — fabricated content anchored in persistent memory, agents resisting correction (pp 35–36) — is an in-band write: the memory system operating as declared on adversarial input. A customer fine-tune through an offered API is likewise "in process." The duty captures only exotic out-of-band modifications — the ones already governed by contracts and internal change control.
- **Declared process means only the system's autonomous loop**: every memory write and user-driven fine-tune is an "intervention," logging volume explodes (against Rec 5's proportionality concern), and the logs become content-adjacent (see (c)3).

Worse, the operator substantially sets the baseline by declaring the process; a self-referential standard invites baseline-gaming. And "discontinuity in the trajectory that process would produce" is a counterfactual about a stochastic system — whose model of the trajectory?

**Completeness is unaddressed.** Rec 2's attestations prove a committed log was not altered; they cannot prove no unlogged modification occurred. Every precedent cited in §4.

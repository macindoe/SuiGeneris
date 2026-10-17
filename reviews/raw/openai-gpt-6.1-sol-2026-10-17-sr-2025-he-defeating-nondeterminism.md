# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `openai/gpt-6.1-sol`
**Source under review:** `research/sources/2025-he-defeating-nondeterminism.md` and its claims
**Queried:** 2026-10-17 via scripts/research_second_read.js --source=2025-he-defeating-nondeterminism --model=openai/gpt-6.1-sol (max_tokens 60000)
**Usage:** {"prompt_tokens":17362,"completion_tokens":1534,"total_tokens":18896,"cost":0.0587435,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":17359,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0587435,"upstream_inference_prompt_cost":0.0434035,"upstream_inference_completions_cost":0.01534},"completion_tokens_details":{"reasoning_tokens":211,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Self-identification (not verified): OpenAI GPT-family model; exact version unavailable to me.

### 2025-he-defeating-nondeterminism-c01
1 statement: AGREE — All numerical results, the named model, prompt and sampling conditions match the held text.
1a scope: scored-event passage (Experiments, “How nondeterministic are completions?”: “we generate 80 unique completions, with the most common of these occuring 78 times. Looking at where the completions differ, we see that the completions are actually identical for the first 102 tokens!”; “when we enable our batch-invariant kernels, all of our 1000 completions are identical”) MATCH; condition-set passage (same subsection: “We use Qwen/Qwen3-235B-A22B-Instruct-2507 and sample 1000 completions at temperature 0 with the prompt ‘Tell me about Richard Feynman’ (non-thinking mode), generating 1000 tokens each”) MATCH — Verb, quantifiers and model match; these are reported completion comparisons, not an assessment of self-access.
2 quote: FOUND — The primary and secondary quotes directly support the reported results.
3 kind: AGREE (proposed: measurement) — The experiment is speaking through recorded completion counts and identity comparisons.
3b bucket: AGREE (proposed: narrowing) — A single-prompt experiment with no retrieved independent replication warrants the narrow bucket.
4 evidence_type: AGREE (proposed: behavioural) — The measured outputs concern Feynman, not the model’s own states.
5 not_evidence_of: OVER-EXCLUDES — The deployment and implementation caveats are warranted, but “The deterministic result needs the author's kernels” implies necessity beyond the tested comparison; the text establishes only that “when we enable our batch-invariant kernels, all of our 1000 completions are identical,” not that other implementations cannot achieve this.
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT — done to the model: inference operators replaced with batch-invariant implementations; measured: completion diversity on an external-topic prompt, not an account of itself; therefore none.
6 bears_on: DISAGREE (proposed: []) — Operational relevance to Q9 does not establish relevance to §4’s stable standpoint or endorsement; the source file itself acknowledges that the page says nothing about §4’s subject matter.
severity: MEDIUM — The exclusion implies an untested necessity; the framework locator is also unsupported by the supplied locator definition.

### 2025-he-defeating-nondeterminism-c02
1 statement: AGREE — The statement accurately attributes the broad causal account to the author rather than presenting it as a measured survey of endpoints.
1a scope: scored-event passage (no scored event: this is interpretation; “Batch invariance and ‘determinism’”: “the primary reason nearly all LLM inference endpoints are nondeterministic is that the load (and thus batch-size) nondeterministically varies!”) MATCH; condition-set passage (“When are atomic adds needed?”: “Given the exact same user requests, it will always provide the same deterministic output”; “Batch invariance and ‘determinism’”: “It is not ‘hardware/software version invariant’ — your GPU/PyTorch version may return a different value, but it should deterministically return the same value”) MATCH — “Argues” correctly names authorial interpretation; “nearly all” reproduces its scope, and no untested models are named as measured.
2 quote: FOUND — All three quotes are present and support the attributed account; the hardware/software quote occurs within the matrix-multiplication example.
3 kind: AGREE (proposed: interpretation) — The author is explaining what causes the observed phenomenon.
3b bucket: AGREE (proposed: open) — The generalisation to nearly all endpoints is argued, not established by endpoint-wide measurements.
4 evidence_type: AGREE (proposed: theoretical) — This entry reports a causal explanation supported by demonstrations, not the demonstrations’ individual measurements.
5 not_evidence_of: AGREE — The exclusions correctly distinguish discussion scope and reproducibility conditions: “Reductions related to parallelism are out of the scope of this discussion” and “It is not ‘hardware/software version invariant’.”
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT — done to the model: no single intervention is this claim’s subject; measured: nothing in this entry—the author is interpreting; therefore none.
6 bears_on: DISAGREE (proposed: []) — The explanation informs reproducibility protocols, not the stable standpoint over time specified for §4.
severity: MEDIUM — Unsupported framework locator; the statement and evidentiary classification otherwise match.

### Source-level

**7 omissions.** No required additional claim: this is expressly a summary-level intake. A relevant implementation qualification is attention’s dependence on processing boundaries (“Batch-invariant attention”: “our numerics must be invariant to both how many requests are processed at once and how each request gets sliced up in the inference engine”). Its omission from these two headline claims is not an extraction failure, and it does not itself establish context or memory integrity under §3.3.

**8 source file.** There is no abstract; the explicitly labelled paraphrase is faithful. The quoted limitations capture important performance, release-completeness and parallelism boundaries; c01 additionally records missing deployment details. The held text identifies Thinking Machines affiliations and Qwen models, making `independent` consistent with the record, but it does not independently establish the source file’s assertion that Alibaba developed Qwen. This is a blog post, not an arXiv paper; the source file correctly records that distinction.

**9 disclosed pulls.** No concrete strengthening or softening impulse is disclosed—only a general conflict note and commitment to the author’s words. The statements show appropriate restraint: c01 is condition-specific and c02 explicitly attributes interpretation. The necessity wording in c01’s exclusion goes beyond the comparison, but the record does not justify attributing that error to a lineage-specific pull.

### Summary
- c01 — Council trigger: over-exclusion; “needs the author’s kernels” implies exclusivity not established by the experiment.
- c02 — No bucket, evidence-type or exclusion trigger; correct the unsupported `bears_on: [4]` administratively, as also required for c01.

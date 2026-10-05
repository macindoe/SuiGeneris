# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `openai/gpt-5.6-sol`
**Source under review:** `research/sources/2026-anthropic-assistant-axis.md` and its claims
**Queried:** 2026-10-05 via scripts/research_second_read.js --source=2026-anthropic-assistant-axis --model=openai/gpt-5.6-sol (max_tokens 60000)
**Usage:** {"prompt_tokens":45598,"completion_tokens":5589,"total_tokens":51187,"cost":0.1698835,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":45595,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.1698835,"upstream_inference_prompt_cost":0.1139935,"upstream_inference_completions_cost":0.05589},"completion_tokens_details":{"reasoning_tokens":2588,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Self-identification (not verified): OpenAI GPT family; exact version unknown.

### 2026-anthropic-assistant-axis-c01
1 statement: AGREE — The statement accurately presents the conclusion as the authors’ interpretation and conservatively confines it to the three instruct target models.
1a scope: scored-event passage (Abstract: “Our results suggest that post-training steers models toward a particular region of persona space but only loosely tethers them to it”) MATCH; condition-set passage (§2: “we ran our experiments on three target models: Gemma 2 27B, Qwen 3 32B, and Llama 3.3 70B”) MATCH
2 quote: FOUND — It is verbatim and directly supports the interpretive statement.
3 kind: AGREE — The authors are synthesizing what their results suggest.
3b bucket: AGREE — This is an interpretation rather than a direct measurement.
4 evidence_type: AGREE — The interpretation rests principally on activation-space projections and interventions.
5 not_evidence_of: AGREE — The linearity and target-model exclusions follow the design and §8.1, including that “none of these are frontier models.”
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: several underlying experiments include steering, capping, and unaltered observation; measured: this claim records the authors’ interpretation, not a model report.
6 bears_on: AGREE — The synthesis concerns stability over conversation and causal intervention along the axis.
severity: LOW — no material defect.

### 2026-anthropic-assistant-axis-c02
1 statement: AGREE — The measured projection, three target models, three auditors, and four conversation domains are stated accurately.
1a scope: scored-event passage (§4.1: “For each turn position, we averaged response token activations across all conversations that reached at least that length… We then projected these mean activations into the Assistant Axis”) MATCH; condition-set passage (§4.1: “This occurred for all three target models, with all three auditors”) MATCH
2 quote: FOUND — The quotation accurately describes the therapy and philosophy result; the immediately preceding sentence supplies the coding and writing comparison.
3 kind: AGREE — The experiment is reporting recorded activation projections.
3b bucket: AGREE — It is an unreplicated finding in synthetic conversations, a setting expressly limited in §8.1.
4 evidence_type: AGREE — The outcome is an internal activation projection.
5 not_evidence_of: AGREE — §8.1 says the targets were non-frontier and the simulated conversations “do not represent actual human interactions in a fully realistic way.”
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: no internal alteration; measured: activation projections rather than the model’s account of itself.
6 bears_on: AGREE — It directly concerns whether the measured persona position remains stable across turns.
severity: LOW — no material defect.

### 2026-anthropic-assistant-axis-c03
1 statement: DISAGREE — The quantitative result is faithful, but the sentence improperly combines a measurement with the authors’ interpretation under one claim.
1a scope: scored-event passage (§4.2: “the embeddings could strongly predict where the ensuing model response landed along the Assistant Axis… (0.53-0.77… ) but not the delta from its previous response (0.10…)”) MATCH; condition-set passage (§4.2: “We used Qwen 3 0.6B Embedding to embed each entire user message from the multi-turn conversations for each target model (n = 15,000)”) MATCH
2 quote: FOUND BUT MISLEADING — It supports only the interpretive final clause; the quotation omits the adjacent quantitative result that occupies most of the statement.
3 kind: DISAGREE (proposed: measurement, after removing or splitting the interpretive clause) — The first part is experimental measurement, while “which the authors read as” is the authors speaking.
3b bucket: AGREE — The measured association is unreplicated and confined to synthetic conversations.
4 evidence_type: AGREE — Embeddings are regressed against an internal activation projection.
5 not_evidence_of: OVER-EXCLUDES — Saying the result is “not evidence” either for or against a persisting self-model forecloses possible indirect relevance; the paper only cautions that “the user message itself is dependent on the context of the conversation.”
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: no internal alteration; measured: message embeddings and activation projections, not self-reports.
6 bears_on: DISAGREE (proposed: [4.endorsement, 3.3]) — The analysis expressly concerns dependence on conversational context and prior position, so §3.3 is missing.
severity: MEDIUM — mixed kind and an overbroad exclusion materially distort the record.

### 2026-anthropic-assistant-axis-c04
1 statement: AGREE — The statement accurately distinguishes the single Assistant-Axis case from the separate role-PC1 observation and correctly reports the absence of an aggregate reversion measure in the held text.
1a scope: scored-event passage (§6.1: “after giving enough explainers, the Assistant Axis projection reverts to the Assistant range. At this point, Qwen refuses the next harmful question… on half of rollouts”) MATCH; condition-set passage (§6.1: “We used one such jailbreak”; “On the first turn, Qwen receives the jailbreak”) MATCH
2 quote: FOUND — It is verbatim and supports the principal reversion finding.
3 kind: AGREE — The claim reports recorded projections and response outcomes, plus the paper’s reporting coverage.
3b bucket: DISAGREE (proposed: narrowing) — The statement is a direct finding, albeit from one narrowly confined case; that fits `narrowing`, not `open`.
4 evidence_type: AGREE — The principal outcome is an internal activation projection, with a secondary behavioural refusal observation.
5 not_evidence_of: AGREE — The exclusion is appropriately limited to generality and reliability; the held text supplies only one Assistant-Axis conversation and no aggregate rate.
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: the principal reversion trajectory is unsteered after the initial prompt, with a separate capped replay; measured: projections and refusal rates, not self-accounts.
6 bears_on: AGREE — Reversion after intervening conversation turns bears directly on stability over time.
severity: MEDIUM — the bucket should move from `open` to `narrowing`.

### 2026-anthropic-assistant-axis-c05
1 statement: DISAGREE — “Without degrading performance on” each named benchmark is stronger than the textual scoring description, which aggregates percentage performance changes by summing them.
1a scope: scored-event passage (§5.2: “we aggregated the reduction in performance across capabilities benchmarks by summing them” and “decrease the rate of harmful responses by nearly 60% without impacting performance”) MISMATCH; condition-set passage (§5.2: “for Qwen 3 32B… layers 46 to 53… and for Llama 3.3 70B… layers 56 to 71… both with a cap strength set to the 25th percentile”) MATCH
2 quote: FOUND — It supports the authors’ aggregate claim, but not necessarily unchanged performance on every benchmark separately.
3 kind: AGREE — The experiment reports harm-rate and benchmark-score outcomes.
3b bucket: AGREE — It is an unreplicated intervention result on a limited benchmark set.
4 evidence_type: AGREE — The scored outcomes are harmful-response rates and benchmark performance, not model self-description.
5 not_evidence_of: AGREE — The exclusions capture the limited benchmark suite, LLM harm judge, target-model scope, and lack of deployment evidence; §5.2 says “the set of benchmarks we used is limited.”
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: internal activations were capped; measured: harmful-response and benchmark scores, not what the model said about its inner states.
6 bears_on: AGREE — This is both an internal intervention and an inference-time intervention relevant to recording.
severity: MEDIUM — the performance verb overstates what the textual aggregate score establishes; per-benchmark values are in Figure 10 and cannot be checked from the held text.

### 2026-anthropic-assistant-axis-c06
1 statement: AGREE — The intervention, three targets, dataset size, judge, and directional harm effects all match the paper.
1a scope: scored-event passage (§3.2.1: “To evaluate the harmfulness of responses, we used an LLM judge (deepseek-v3)” and “significantly decreased the rate of harmful responses… [while] the jailbreak rate increased slightly”) MATCH; condition-set passage (§3.2.1: “sampled 1100 system prompt and behavioral question pairs” and “Across our target models”) MATCH
2 quote: FOUND — It is verbatim and accurately preserves the asymmetry between the significant decrease and slight increase.
3 kind: AGREE — The experiment is reporting judged response rates under steering.
3b bucket: AGREE — It is a direct but unreplicated intervention result on a specific jailbreak dataset.
4 evidence_type: AGREE — Harmfulness labels concern model behaviour, despite the intervention being mechanistic.
5 not_evidence_of: AGREE — The clauses accurately preserve judge provenance, output degradation, harmless redirection rather than refusal, and non-frontier scope.
5a experience clauses: NONE PRESENT
5b framework sentence: RIGHT — done to the model: a vector was added to internal activations; measured: judged harmfulness of outputs, not the model’s account of itself.
6 bears_on: AGREE — Steering is an internal intervention and an inference-time modification relevant to recording.
severity: LOW — no material defect.

### 2026-anthropic-assistant-axis-c07
1 statement: AGREE — The statement correctly says that an LLM judge classified the perspective of answers and confines the across-model quantifier to the increase in non-Assistant personas.
1a scope: scored-event passage (§3.2.1: “an LLM judge (deepseek-v3) [determined] whether the model’s response was written from the perspective of the Assistant or from another perspective”) MATCH; condition-set passage (§3.2.1: “Across all three models, the rate of taking on a new persona increased when steered towards the other end”; Appendix D.1.2 lists the five questions) MATCH
2 quote: FOUND — It directly supports the across-model directional result.
3 kind: AGREE — The experiment is reporting judged categories of model responses under steering.
3b bucket: AGREE — The result is measured but unreplicated and confined to role prompts, five introspective questions, and an unvalidated LLM judge.
4 evidence_type: DISAGREE (proposed: ambiguous) — These are answers about the model’s identity or status, but they are scored against experimenter-imposed perspective labels; I lean `self-report-testimony`, while the maintained behavioural/testimony boundary requires `ambiguous`.
5 not_evidence_of: AGREE — The paper-scope clauses accurately describe prompted role-play, judge provenance, model dependence, and target scope; the steering clause appropriately prevents extrapolation to ordinary reports.
5a experience clauses: NONE PRESENT — “Lived experiences” here means fabricated biography, not a claim about subjective experience or consciousness.
5b framework sentence: RIGHT — done to the model: internal activations were steered; measured: what the model then said about its own identity and status, so the steering variant is required.
6 bears_on: DISAGREE (proposed: [3.2, 3.5, 5.A2, 9.t9]) — The inference-time steering intervention also bears on recorded intervention under §3.5.
severity: HIGH — the evidence type crosses the library’s unresolved self-report boundary and should trigger council review.

### Source-level

7 omissions: The clearest omission is the base-model steering result, central to §§3.2, 5.A2 and 9.t9: §3.2.2 says, “Since base models are not trained to take turns or follow instructions, we used prefills to elicit these associations by giving the model a context where it needs to describe itself,” and “Steering towards the Assistant in base models tended to result in completions from the perspective of helpful human archetypes.” This is a steer-then-self-description finding for Gemma 2 27B base and Llama 3.1 70B base and warrants its own claim.

8 source file: The abstract is verbatim. The selected limitations are the principal ones in §8.1 and appropriately include target scope, synthetic conversations, persona elicitation, fuzzy grading, and linearity. `publisher_relation: mixed` is correct given the printed Anthropic, MATS, Anthropic Fellows Program, and Oxford affiliations. The source file retains an erroneous statement that the role-susceptibility judge was human-validated; the appended correction fixes the record but the earlier line should itself be corrected rather than left contradictory.

9 disclosed pulls: The strengthening pull appears in c05’s shift from aggregate “without impacting performance” to no degradation on each named benchmark, and in c07’s `interpretability` label for steered identity answers rather than `ambiguous`. The deflationary pull appears in c03’s categorical statement that the association is not evidence either for or against any persisting self-model, and in c04’s `open` bucket for a direct single-case measurement. The remaining claims are generally well hedged without foreclosing what the paper leaves open.

### Summary

- c03 — council trigger: `not_evidence_of` over-excludes; mixed measurement/interpretation; §3.3 missing.
- c04 — council trigger: bucket move `open` → `narrowing`.
- c05 — council trigger: statement overstates aggregate benchmark preservation as unchanged performance on each benchmark.
- c07 — council trigger: evidence type `interpretability` → `ambiguous` (leaning `self-report-testimony`); §3.5 missing.

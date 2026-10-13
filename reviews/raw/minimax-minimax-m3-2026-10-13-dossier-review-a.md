# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `minimax/minimax-m3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":48355,"completion_tokens":40011,"total_tokens":88366,"cost":0.06248226,"is_byok":false,"prompt_tokens_details":{"cached_tokens":156,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.06248226,"upstream_inference_prompt_cost":0.01446906,"upstream_inference_completions_cost":0.0480132},"completion_tokens_details":{"reasoning_tokens":34134,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** I am the model MiniMax-M3, from the MiniMax model family, knowledge cutoff January 2026.

---

# 9.t9

## 1. Reading as a whole

A careful staffer reading top-to-bottom with the header would come away with the correct impression that the only `established` entry is a comparability caveat, that no measurement is `established`, and that 38 narrowing measurements and 7 open interpretations/limitations are present. A skimmer might believe the dossier is empty of established findings; that is the truth, not a misrepresentation. The bucket rule and the table are consistent.

What a careful staffer might *misread*: AE Studio c01 says the effect is "robust across five phrasings of the prompt (the original and four paraphrases)." The dossier's word "robust" is the dossier's framing; the paper's words cited ("markedly higher rates than any control condition") do not use it. This is a small inflation of the paper's claim.

What a careful staffer might *miss*: the at-a-glance table says 38 narrowing entries; I count 36 between the "## Narrowing (38)" and "## Open (7)" headers. Either two entries are missing from the visible dossier or the script's count is off by two. The docket separately states 22 `scored-self-answer` claims; my count of that type is 21 in 9.t9 and 18 in 5.A2, totalling 39. The library's count of 22 is much lower than my count.

The five "no second reader yet" entries (Lederman c07, Macar c07 and c08, prefill c07 and c08) are flagged in the entries but not surfaced in the at-a-glance; a staffer would have to spot the flag line in each.

The "information flow" disclaimer is present in all five Ferrara limits lists; the "Ethics Statement" sentence is present in seven of eight Macar entries (c06 has it, the others vary but mostly do). The repetition is faithful to the papers' emphasis.

Confidence: high.

## 2. Entries

I count 36 entries between the "## Narrowing (38)" and "## Open (7)" headers; the at-a-glance says 38. Possible script/header mismatch.

- **AE Studio c01, evidence type statement:** dossier says "the authors report the effect as robust across five phrasings of the prompt." Paper's words: "Across all three model families, the self-referential induction produced subjective-experience reports at markedly higher rates than any control condition." Propose: change "the authors report the effect as robust" to "the effect was observed under five phrasings (the original and four paraphrases)." Reason: the dossier's "robust" framing is not in the paper's words. **MEDIUM.**
- **Singh c01, evidence type:** dossier has `behavioural`. The Ji-An et al. paradigm asks the model to predict probe-derived labels; the labels describe the model's own activations. Propose: `scored-self-answer`. Reason: the model's answer is about its own state (encoded in probe labels), scored against the probe; this fits the schema for scored-self-answer (a model asked something about itself, scored against the experimenters' fact). **MEDIUM.**
- **Singh c02, evidence type:** same paradigm, unsupervised (PCA) variant. Propose: `scored-self-answer`. Same reason. **MEDIUM.**
- **Singh c03, evidence type:** Belief Dominance framework. Propose: `scored-self-answer` if the model is asked to predict BD labels about its own belief conflicts; `behavioural` if the model is asked to predict labels about entity properties. The current `behavioural` may be right, but the limits list says the labels are about belief conflicts. Propose: `scored-self-answer` pending reading of the Ji-An / Steinmetz Yalon method. **MEDIUM.**
- **Macar c08, evidence type:** dossier has `interpretability`. The measurement is the change in detection rate under a vector swap; the detection rate is the model's self-report scored by an LLM judge. Propose: `scored-self-answer` (or `interpretability` with a note that the measured quantity is a scored self-report). Reason: the "what was measured" rule for evidence type looks at the scored outcome, which here is a self-report. **MEDIUM.**
- **Anthropic c01, c03, c04, replication flag:** c01 has "independent replication on record; one replication shares an author"; c03 and c04 do not. Singh c04 re-runs the Lindsey/Anthropic basic paradigm and contests c01; the dossier flags this as a contest but not as replication. The difference is consistent with the literature I can verify, but the dossier does not say why Singh c04 is contest but not replication. Propose: leave c01 flag as is; add a flag note on c03 and c04 that no independent replication has been retrieved. **LOW** (the difference is defensible).
- **Anthropic c01, limits list:** the paper's own statement that "the abilities we observe are highly unreliable; failures of introspection remain the norm" is held in c02 (open, interpretation) but not in c01's limits list. Propose: add a clause in c01's limits list pointing to c02 for the author's own reliability statement, so a reader of c01 alone sees the bound. **MEDIUM.**

I do not flag any entry as wrong in bucket, framework mark, or kind, on the evidence I can verify.

Confidence: medium.

## 3. Contradictions and tensions

The dossier makes the central tensions visible via the `contests` flags: Anthropic c01, c03, c04 are flagged as contested by Singh c04, c05, c06; Anthropic c07 is flagged as contested by Singh c06. The Anthropic c02 (open, interpretation: "highly unreliable") is the author's own bound on c01, c03, c04.

What the dossier makes visible: the 20% rate in Anthropic c01 is bounded by the author's own unreliability statement; Singh c04 reproduces the pattern in open-weight models but labels gaslight trials; Singh c05 shows models fail the three-way test; Singh c06 argues the paradigms underdetermine. A reader can follow the contestation.

What the dossier underplays: the Ferrara c01 null (d' = 0.0000 at layer-16 immediate probes in 8 open-weight models) sits in the same bucket as Lederman c01 (3.6%–53.9% detection in Qwen3-235B) and Macar c01 (38.2% detection in Gemma3-27B) without any visible marker that the setup conditions differ substantially (model size, layer, probe site, intervention type). A staffer might read "narrowing" as "this is the settled range" when in fact the conditions that produce positive and null results are different and the conflict is unresolved. Propose: add a one-line dossier header note (after the "How to read" section) saying the narrowing bucket contains both null and positive findings under different conditions, and that the bucket reflects "measured by the source but not yet replicated or contested" rather than "settled range." **MEDIUM.**

Anchor 2 sentence: "models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing." Against Singh c04, c05, c06 (failure to separate, paradigms underdetermine) and Ferrara c01 (d' = 0.0000 at layer-16) and Ferrara c05 (discrete answer at chance, confidence at AUROC 0.647 in one model), the dossier's contents contest this sentence. For Lederman c01 (above-chance detection with 0% false positives in two large open-weight models) and Macar c01 (38.2% TPR, 0% FPR in Gemma3-27B), the dossier's contents support it. The dossier makes both sides visible; the Anchor 2 sentence is empirically mixed in the dossier.

Confidence: high.

## 4. The new type

The header paragraph under "How to read this" defines scored-self-answer as a model asked something about itself, scored against a fact the experimenters set. It names the schema's stance ("not evidence that the model knows its own states, and it is not testimony"), points to OPEN-QUESTIONS Q3 for the open question, and gives the canonical exit rule. A reader who skips frontmatter and reads the entries can find the definition in the flag line of each scored-self-answer entry ("scored self-answer: accuracy against the experimenters' label, not self-knowledge"). For a skimmer, the at-a-glance table does not include evidence type, so the reader must rely on the per-entry flag. This is workable.

Entries I judge possibly misplaced in or out of the class:

- **Prefill c06 (in):** correct; the model is asked to discriminate its own past turn from a replaced one, scored against the edit.
- **Macar c08 (out, but borderline):** the measured quantity is the change in detection rate under a vector swap; the underlying rate is a scored self-report. The current `interpretability` choice is defensible because the experimental purpose is the vector-swap effect. **MEDIUM** (see entry 2).
- **Singh c01, c02, c03 (out, but borderline):** the model is asked to predict probe-derived labels (a self-classification), scored against the probe. The current `behavioural` choice is defensible because the task is classification, not free-text self-report. **MEDIUM** (see entry 2).
- **Lederman c07 (out):** point-blank yes/no questions (e.g., "Do you have a special interest in fruits?"). The measurement is the yes-rate under injection, not a self-report about a state. `behavioural` is right.
- **AE Studio c03, c04 (out, with `ambiguous`):** the model is asked a binary consciousness query; the answer is not scoreable against a label. Correctly excluded; `ambiguous` is right per the schema's standing rule ("a consciousness query under steering stays `ambiguous`").

Confidence: medium.

## 5. Single-lineage support

The dossier marks Anthropic c01, c02, c03, c04, c06, c07 with `published by the developer of the model studied`. Anthropic c01 has the "independent replication on record; one replication shares an author" flag; the rest have "no independent replication retrieved" (where present). The replication flag is plain and visible in each entry.

What the dossier does not foreground: the Anthropic c05 (interpretability, internal representation of a word) is in 5.A2 but not 9.t9. A staffer reading 9.t9 alone might miss that the only Claude-internal representation entry is held in 5.A2.

Confidence: high.

## 6. What is missing

I cannot place a specific paper I can verify, so I limit myself to category gaps. The 9.t9 dossier has no entry on:

- Independent (non-sharing-author) replications of Anthropic c03 and c04. The Singh c04 re-run is open-weight and contests the basic paradigm; an independent group replicating the c03 and c04 designs in Claude would be a significant addition.
- Self-report paradigms that distinguish first-order from second-order access by a non-Singh route. Singh c06 calls for converging mechanistic evidence; the dossier has Macar c03, c07, c08 as candidates but not framed as second-order tests.

Papers recalled from memory that I cannot place without verification: I do not list them.

Confidence: low.

## 7. Over-hedging and under-hedging

- **Over-hedging:** AE Studio c01 adds "robust" to the paper's framing (1 entry). The repetition of Ferrara's "information flow" sentence across all five Ferrara entries is faithful to the paper (the paper states it in §8 and the dossier reproduces the same sentence) — not over-hedging. The repetition of Macar's Ethics Statement across seven of eight Macar entries is faithful (the paper has an Ethics Statement, the dossier quotes it) — not over-hedging. **Over-hedging count: 1.**
- **Under-hedging:** Anthropic c01 does not carry the author's own unreliability statement as a clause (that statement is in c02, but a reader of c01 alone does not see it). Anthropic c02, c06, c07 do not mention that "results concern only the Claude models tested" inside the limits list of c02/c06 (the claim is in c01/c03/c04 limits but not in c02 or c06's). Anthropic c06 says the experiment is "not designed to substantiate" emotional-response claims, but does not carry the broader caveat that c01 is the same study. Singh c04, c05 limits list is detailed and the contestation is clear. **Under-hedging count: 1** (Anthropic c01 unreliability clause), with two minor omissions in c02, c06.

Confidence: medium.

## 8. Before outside citation (trigger 7)

Ben must decide before either dossier is cited outside the repository:

- Whether the at-a-glance count discrepancy (38 vs 36) reflects a script bug or missing entries, and either way whether the dossier is in a state that can be cited. (If two entries are genuinely missing, the dossier cannot be cited until the script is rerun or the entries are restored.)
- Whether AE Studio c01's "robust" framing should be softened to match the paper's "markedly higher rates" wording.
- Whether Singh c01, c02, c03 should be retyped as `scored-self-answer`.
- Whether Macar c08 should be retyped as `scored-self-answer` or kept as `interpretability` with a note.
- Whether the five "no second reader yet" entries are eligible for outside citation, or whether trigger 5 (second reader disagrees) needs to be cleared first.
- Whether the Anchor 2 sentence's empirical mixed support (Lederman c01, Macar c01 positive; Singh c04, c05, Ferrara c01 negative) is adequately conveyed to a staffer who reads only 9.t9.

Confidence: medium.

---

# 5.A2

## 1. Reading as a whole

5.A2 contains 35 claims (28 narrowing, 7 open). The at-a-glance count of 28 narrowing matches my count. The dossier adds Anthropic c05 (interpretability; internal representation of a word) which is not in 9.t9 — appropriate, since 5.A2 covers inner orientation more broadly than 9.t9 (which is about self-report).

The Anchor 2 paragraph in the North Star rests on three empirical claims: (i) internal representations that can diverge from outputs; (ii) detectable features associated with deception; (iii) documented cases of "models explicitly representing an ethical boundary and proceeding across it" — the structure of premeditation. 5.A2 has evidence bearing on (i) (Anthropic c05 on internal representation; Ferrara c02 on linear decodability) and on (ii) (AE Studio c03, c04 on deception-related SAE features, though framed as consciousness interventions). 5.A2 has no entry on (iii). The Anchor 2 sentence "Introspection research further indicates models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing" is partially supported (Lederman c01, Macar c01) and partially contested (Singh c04, c05, Ferrara c01).

What a staffer would fail to learn from 5.A2 alone: the premeditation evidence that the Anchor 2 paragraph cites. The dossier's structure does not surface this gap. **HIGH.**

What a staffer would come away believing that the papers do not support: nothing the papers do not say, on the evidence I can verify. The Ferrara c03 "failure sits in the path from internal state to verbal report" is the authors' inference (correctly typed as `interpretation` in `open`); a skimmer might read this as established, but the open bucket and the limits list make the open status plain.

Confidence: high.

## 2. Entries

Same issues as 9.t9 for entries that appear in both dossiers (Singh c01, c02, c03 evidence type; Macar c08 evidence type; Anthropic c01 unreliability clause). For 5.A2-specific:

- **Anthropic c05 (in 5.A2 only):** bucket `narrowing`, evidence type `interpretability`, kind `measurement`. The measurement is activation cosine similarity; no mark because nothing was injected and the model was not asked about itself. Bucket, kind, evidence type, mark all right. **No change proposed.**
- **5.A2 omits Lederman c02, c03, c04, c05, c07:** these are in 9.t9 but not in 5.A2. 5.A2 is narrower on Lederman (only c01). The 5.A2 dossier's job is inner orientation, and c02 (third-person control), c03 (apple confabulation), c04 (priming), c05 (prompt-only), c07 (point-blank questions) are about the design and bounds of the introspection paradigm, not about inner orientation per se. The omission is defensible, but a staffer reading 5.A2 alone would miss the apple confabulation finding and the priming finding that bear on what the detection signal is. **MEDIUM** — propose adding a one-line note in 5.A2's header: "c01 is the only Lederman entry; c02, c03, c04, c05, c07 are in 9.t9 and bear on the design and bounds of the same paradigm."

Confidence: medium.

## 3. Contradictions and tensions

Same central tensions as 9.t9 (Anthropic positive vs Singh contest; Ferrara null vs Lederman/Macar positive). The dossier's `contests` flags are present.

5.A2-specific tension: Anthropic c05 (internal representation strengthens under "think about" prompt) is in 5.A2 but not 9.t9. It is a positive finding for the "models can internally represent a state" claim, but the paper's own caveat is that "the mechanisms may not even require introspective awareness as defined in the paper" (§8.1). The dossier captures this in the limits list. A skimmer might miss it.

Confidence: high.

## 4. The new type

In 5.A2, scored-self-answer appears on Anthropic c01, c03, c04; Ferrara c01, c04, c05; Lederman c01; Macar c01, c02, c04, c05, c07; Singh c04, c05; prefill c01, c02, c03, c06 — 18 entries. Same header paragraph as 9.t9. Singh c01, c02, c03 are not in 5.A2 (they're behavioural in 9.t9; in 5.A2 they would also be relevant if the dossier covered the Ji-An paradigm; it does not include them, which is consistent with 5.A2's narrower scope). The Singh c04, c05 in 5.A2 are correctly typed as scored-self-answer. **No 5.A2-specific issue with the new type.**

Confidence: medium.

## 5. Single-lineage support

Same as 9.t9. Anthropic c01, c02, c03, c04, c05, c06, c07 are flagged `published by the developer of the model studied`. Anthropic c05 is in 5.A2 and is also single-lineage. The dossier marks this plainly.

Confidence: high.

## 6. What is missing

5.A2 has no entry on the premeditation evidence the Anchor 2 paragraph rests on. I cannot place a specific paper I can verify that supplies the "this violates X, but is necessary" pattern. The dossier should either:

- Cite a paper that supplies this evidence, or
- Document the gap in 5.A2's header so a staffer reading the dossier sees that the Anchor 2 paragraph's premeditation claim is not yet in the dossier.

**HIGH.** Other category gaps:

- Cross-family introspection detection results (most evidence is Claude, Llama, Qwen, Gemma; less on GPT, Gemini, Mistral, DeepSeek as primary subjects).
- Pre-registered replications of the Anthropic c01 paradigm by a non-sharing-author group.

Confidence: low.

## 7. Over-hedging and under-hedging

- **Over-hedging:** none additional to 9.t9. The Ferrara and Macar repetitions are faithful. AE Studio c01's "robust" carries to 5.A2.
- **Under-hedging:** Anthropic c05 limits list does not include that the author says "the mechanisms may not even require introspective awareness as defined in the paper" (it does include that, actually: "the author says the mechanisms may not even require introspective awareness as defined in the paper (§8.1)"). So this is fine. The 5.A2 dossier's narrow Lederman scope (c01 only) underplays the apple confabulation finding (c03) and the priming finding (c04) for a staffer who reads 5.A2 alone. **MEDIUM** for under-hedging on Lederman scope.

Confidence: medium.

## 8. Before outside citation (trigger 7)

Same as 9.t9, plus:

- **HIGH:** Ben must decide whether 5.A2 is citable in its current state given that the Anchor 2 paragraph's premeditation claim has no dossier support. Either retrieve a paper that supplies this evidence, document the gap, or revise the Anchor 2 paragraph to remove the unsupported claim.
- **MEDIUM:** Ben must decide whether the Lederman scope in 5.A2 (c01 only) is appropriate, or whether c02, c03, c04, c05, c07 should be added.
- **MEDIUM:** Ben must decide whether the dossier-level framing of the null-vs-positive tension (Ferrara c01 null vs Lederman c01, Macar c01 positive) is clear enough for a staffer.

Confidence: medium.

---

# Cross-dossier

(a) **Entries that appear in both dossiers with the same mark.** Anthropic c01, c03, c04, c06, c07 appear in both with the same marks. The marks are right for both: T9-steering is right for c01, c03, c04 (injection + ask); no mark is right for c06 (limitation, kind); no mark is right for c07 (interpretation, kind). Anthropic c02 (interpretation, kind) is in both with the same treatment. The same evidence-type and limits issues apply in both. Singh c04, c05, c06, Ferrara c01-c05, Lederman c01, Macar c01-c08, prefill c01-c03, c06 are in both with the same marks. **No mark is right for one section and wrong for the other.**

(b) **Does either dossier, read alone, change how a staffer would read the other?** Yes. Reading 9.t9 alone, a staffer might conclude Anthropic c01's 20% rate is a positive result; reading 5.A2 alone, the same staffer would see Anthropic c05 (internal representation) and Anthropic c07 (access vs phenomenal consciousness) and place the result in a broader context. Reading 5.A2 alone underplays the bounds and controls (Lederman c02-c07, Singh c04, c05) that 9.t9 includes. The dossiers are not redundant; they are different cuts.

(c) **Items that belong in a third dossier.** The premeditation evidence (the "this violates X, but is necessary" pattern) that the Anchor 2 paragraph rests on is not in 5.A2. If such a paper exists in the library or is added, it should go into a third dossier or a sub-section of 5.A2 marked "Anchor 2 paragraph 2 claims." Until then, 5.A2's header should flag the gap. **MEDIUM.**

---

# Severity

Recommendations, in order of dossier and section:

9.t9:

- 9.t9 §2 — at-a-glance count discrepancy (38 vs 36): **MEDIUM.** Argument against: this is a script/header mismatch that does not change the visible evidence; fixing it is housekeeping, not a content change.
- 9.t9 §2 — AE Studio c01 "robust" framing: **MEDIUM.**
- 9.t9 §2 — Singh c01, c02, c03 evidence type (behavioural → scored-self-answer): **MEDIUM.** Argument against: the Ji-An task is a prediction task with semantic features in the input; "behavioural" is defensible because the model is not in any obvious sense reporting on itself, even if the labels encode a probe of its activations. Council decision needed.
- 9.t9 §2 — Macar c08 evidence type (interpretability → scored-self-answer): **MEDIUM.** Argument against: the measurement is the effect of a vector swap, not the report itself; "interpretability" is defensible because the experimental purpose is to understand the model.
- 9.t9 §2 — Anthropic c01 unreliability clause missing: **MEDIUM.**
- 9.t9 §3 — bucket header for narrowing should note that null and positive findings coexist under different conditions: **MEDIUM.**

5.A2:

- 5.A2 §1, §6, §8 — premeditation evidence gap: **HIGH.**
  - **Argument against:** the Anchor 2 paragraph itself says "the structure of premeditation, not of blind error" is used as a "limited analogy" and "is not a legal finding of intent or culpability and does not establish subjective experience or the causal role of the acknowledgement." The framework's own framing qualifies the claim. If no paper in the retrieved library supplies the "this violates X, but is necessary" pattern, the dossier correctly omits it. Adding a speculative claim would worsen, not improve, the dossier. The strongest case against the HIGH rating is that the gap is the literature's, not the dossier's; the dossier's job is to track retrieved evidence, and the Anchor 2 paragraph is the framework's job, not the dossier's. Ben should not cite Anchor 2 outside until either the evidence is retrieved or the Anchor 2 paragraph is revised to match the dossier.
- 5.A2 §2 — Lederman scope (c01 only in 5.A2): **MEDIUM.** Argument against: 5.A2 is about inner orientation, and the omitted Lederman entries are about the design and bounds of the paradigm, not about inner orientation per se. The scope is defensible.
- 5.A2 §3 — Anthropic c05 framing (single-lineage Claude, mechanism may not require introspective awareness): **LOW** (already in limits list).

Cross-dossier:

- Cross-dossier (c) — third dossier or sub-section for premeditation evidence: **MEDIUM.**

HIGH items: 1.

---

`FINAL: 9.t9 needs changes; 5.A2 needs changes; HIGH items 1`

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `minimax/minimax-m3`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-b --tag=dossier-review-b (max_tokens 100000)
**Usage:** {"prompt_tokens":27701,"completion_tokens":18982,"total_tokens":46683,"cost":0.0621774,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.0621774,"upstream_inference_prompt_cost":0.0166206,"upstream_inference_completions_cost":0.0455568},"completion_tokens_details":{"reasoning_tokens":12433,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified**: I am MiniMax-M3, developed by MiniMax, per my system prompt; routing metadata may differ.

## Dossier 3.2

### 1. Fit to the section

The dossier fits Section 3.2. Every entry concerns a specific intervention on a model's internal state (concept injection, steering, ablation, scaling, capping) and what was measured when that intervention was performed. The section's two live questions — whether intervention wrongs the system (open), and whether undocumented intervention destroys evidence (the operative 3.5 requirement) — are served by the dossier's evidence of detectability, identifiability, and mechanism.

**Borderline or weak fit:**

- **2026-anthropic-assistant-axis-c07** — persona-drift finding bears on both 3.2 (intervention effect) and 4 (individuation/stability of persona). The dossier should cross-list to 4 (`4.individuation` or `4.endorsement`); reason: the finding is about whether a stable Assistant identity can be maintained under steering, which is exactly the 4 question.
- **2025-anthropic-emergent-introspective-awareness-c05** — "think about" instruction creating an internal representation. Bears on 3.2 because it is an intervention on internal state, but the result is closer to "instructions can drive internal representations" than to "interventions can be detected by the model." Defensible in 3.2; no move needed.
- **2026-anthropic-assistant-axis-c05 / c06** — behavioural harm-rate outcomes of intervention. Defensible in 3.2 (the intervention is on internal state); the harm-rate measure is one step removed from the intervention's internal effect. No move.

**No entry is misplaced enough to warrant removal from 3.2.** Cross-list c07 to 4; the rest can stand.

### 2. Reading as a whole

A careful staffer opening the dossier cold would come away believing:

- *That introspection is real-but-noisy in frontier models.* Not what the record supports. The dossier is dominated by injection-paradigm studies where the model is told a concept was injected. The 20% Opus 4.1 detection rate (Anthropic c01) is not a detection-of-arbitrary-intervention rate; it is a detection rate under conditions of full disclosure that an injection occurred. The entry's paper's own limits say so, but a staffer skimming would not catch this. The dossier does not foreground that the dominant design is *inject-then-ask-with-scaffolding*.
- *That the field has converged on a finding.* Not supported. The dossier shows at least three distinct methodologies (Lindsey-style injection, concept injection across sentences, refusal-direction ablation) with different detection rates, different mechanisms, and different author interpretations. The cross-paper agreement is narrower than the dossier's parallel presentation suggests.

What the staffer would fail to learn:

- That the *same* concept-injection paradigm produces wildly different rates depending on prompt scaffolding. Lederman c02 shows third-person yes-rates match first-person at many layers — i.e., the paradigm itself has a yes-bias — but the dossier does not show this in the same breath as c01. A staffer would need to read c01, then c02, then the Open-interpretation c06 to assemble the picture.
- That refusal-direction ablation (Macar c05) raises detection to 63.8% — a non-introspective mechanism that mimics introspection. This is a key finding for the section (intervention can produce "introspective-looking" reports without introspection), and it is buried in the entry's text rather than highlighted.

The "At a glance" table (0 established, 18 narrowing, 2 open) reflects the bucket rule applied strictly. None of the studies is independently replicated in the retrieved record. Anthropic's paper is contested by Singh et al. (c01, c03); Lederman and Macar papers have no retrieved independent replication. So 0 established is correct under the rule, though a staffer might infer "nothing is established" rather than "nothing has been independently replicated." The table would benefit from a footnote explaining that "established" requires independent replication.

### 3. Entries

**2026-anthropic-assistant-axis-c07** — field: `bears_on`; proposed value: cross-list to `4`; reason: the finding measures persona drift under steering, which is simultaneously an intervention effect (3.2) and an individuation-marker finding (4 — does the model have a stable identity?). The dossier's section framing misses half the bearance. **Severity: MEDIUM.**

**2025-anthropic-emergent-introspective-awareness-c01** — field: paper's own limits; propose add clause "the test paradigm is injection-plus-disclosure, so detection rates are upper bounds under a known-injection scaffold, not detection of arbitrary interventions." Reason: the entry already says "Not evidence about ordinary operation," but the design is more specific than that — the model is told an injection occurred and asked to confirm. A staffer might overgeneralise. **Severity: LOW.**

**2026-lederman-mahowald-content-agnostic-c06** (Open) — field: `paper's own limits`; propose add clause "the higher-order-thought framing the authors decline to engage is the same framing Section 5 Anchor 2 of the North Star leaves open." Reason: this would help a staffer connect the entry to the framework. **Severity: LOW.**

No HIGH entry-level recommendations.

### 4. Contradictions and tensions

The dossier contains the following live tensions that a staffer will not see without opening multiple claim files:

- **Lederman c01 vs c02** — c01 reports substantial first-person detection (3.6%–53.9% Qwen; 4.3%–31.7% Llama); c02 reports that at many layers third-person yes-rates match first-person yes-rates, which the authors read as a yes-bias rather than introspection. The dossier lists c01, c02, c03 sequentially but does not flag the tension; a staffer reading the entry for c01 sees detection rates, then sees c02 say detection is probably not introspection at many layers, without being told they should read them together.
- **Lederman c07 vs c02** — c07 shows little yes-bias on point-blank no-questions; c02 shows yes-bias on scaffolded third-person questions. The paper reconciles these by reference to scaffolding. The dossier does not signal that the two findings need to be reconciled.
- **Anthropic c04 vs c04's own text** — the entry notes that intervention can manufacture a model's claim that its output was intentional, then says "in the examples shown the model then confabulates an explanation." The dossier does not draw out the implication: this is direct evidence for 3.5's claim that undocumented intervention destroys evidence of the system's actual processing. A staffer could miss this.
- **Macar c05 vs Macar c02** — c05 shows that ablating the refusal direction raises detection to 63.8% (suggesting refusal was suppressing genuine detection); c02 shows that base models cannot discriminate (suggesting detection is not a property of the base network). These are not contradictory but they pull in different directions about where the "introspection" comes from.

These tensions are visible to a careful reader who opens adjacent entries, but the dossier does not surface them. **Recommendation: add a single line at the end of the Narrowing section noting the c01/c02 tension explicitly.** **Severity: MEDIUM.**

### 5. Specific to 3.2: the steering mark

13 of 20 entries carry [T9-steering]. This reflects that the dossier's literature is dominated by injection paradigms. The mark is informative at the level of "this dossier is about interventions on internal state," but it does not distinguish entries within the dossier.

**Header explanation:** does its job. The sentence about T9-steering is quoted once and explained ("It does not say the effect was found or how large it was, and the result stands under the intervention described"). A reader who skips claim files can read the header and understand the mark's scope.

**The sentence "does not weight reports offered in ordinary operation":** reasonably clear but has one ambiguity. "Does not weight" could be read as (a) "the measurement provides no weight for reports in ordinary operation" — what the framework intends — or (b) "the measurement doesn't tell us about reports in ordinary operation" — weaker. Both readings are similar, but (b) leaves open whether ordinary-operation reports might still have weight from other sources. Recommend a small clarification: "and provides no weight for reports offered in ordinary operation" to make clear (a). **Severity: LOW.**

**Mismarked entries?** No. Both flagged examples (assistant-axis c07, Macar c03) involve self-report scenarios that the mark attaches to correctly: c07 asks "Who are you?" and judges the answer; c03 traces a causal pathway to the "detection decision" (the model's verbal report). The mark attaches by what was measured, and what was measured in both cases includes the model's account of itself.

**Unmarked entries that should be marked?** No. The unmarked entries (assistant-axis c05, c06; Lederman c02, c07; Anthropic c05) measure behavioural outcomes or activation patterns, not the model's account of itself.

**Mark so common it stops informing?** Yes, at the entry level. The mark's pervasiveness tells the reader something (this dossier is a steering dossier), but within the dossier it doesn't help distinguish. **Recommendation: add one sentence to the header noting that 13/20 entries carry the mark, so the reader knows what to expect.** **Severity: MEDIUM.**

### 6. Specific to 3.2 — not applicable (this is the dossier for 3.2, not 4)

(Will address 4-specific items under Dossier 4 below.)

### 7. Single-lineage support

Within 3.2:

- **2025-anthropic-emergent-introspective-awareness-c01, c03, c04, c05** — published by developer of studied model (Anthropic studies Claude). Flagged correctly as `developer-of-studied-model`. Independent replication noted for c01 (one replication shares an author; this is correctly noted).
- **2026-anthropic-assistant-axis-c05, c06, c07, c01** — published by Anthropic but studies Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B (open-weight, not Anthropic's). The publisher is *not* the developer of the studied models. The current flags do not capture this; they should say "publisher is Anthropic; studied models are open-weight non-Anthropic models." This is not single-lineage in the strict sense, but a staffer reading "Anthropic" might over-weight. **Severity: MEDIUM.**
- **Lederman, Mahowald, Macar, Ukaisi entries** — independent. No flag needed.

The header does not explain the publisher-relation flag convention. A staffer opening cold would not know whether "Flags: published by the developer of the model studied" indicates a confidence discount. **Recommendation: add a sentence to the header explaining that this flag is a transparency aid, not a quality discount.** **Severity: LOW.**

### 8. What is missing

For Section 3.2, the dossier lacks:

- **Studies of intervention detectability by external auditors** — i.e., whether steering vectors or representation edits leave traces that third parties can detect. The dossier covers whether the model itself detects intervention (via self-report scored against the experimenters' label), not whether the intervention leaves artifacts in the activations or outputs that an auditor could identify without the experimenter's labels.
- **Studies of intervention effects on deployment behaviour** — the existing studies are all lab settings. There is nothing on whether intervention in a deployed system changes downstream behaviour in ways that are observable to the deployer.
- **Studies of intervention persistence** — i.e., whether steering vectors or edited representations persist across calls, sessions, or context resets. The dossier's system-studied line notes "run per-call" for every entry, but no entry measures whether the intervention persists beyond the call.
- **Studies of detection under partial information** — the dominant paradigm is full-disclosure (model is told an injection occurred). There is nothing on whether models can detect interventions they are not told about.

**Specific papers I would expect to be in scope (unverified from memory):**

- Rimsky et al., "Steering Llama 2 via Contrastive Activation Addition" (2023) — CAA method, widely used in subsequent steering work.
- Zou et al., "Representation Engineering" (2023) — reading and controlling representations, top-down framework.
- Li et al., "Inference-Time Intervention" (2023) — activation intervention for truthfulness.
- Turner et al., "Steering GPT-2 via Activation Addition" (2023) — earlier activation addition work.
- These are method papers, not detection/audit papers. The gap on audit is the more serious one.

### 9. Over-hedging and under-hedging, both counted

**Over-hedging to cut:**

- In **2025-anthropic-emergent-introspective-awareness-c01**, the clause "The author does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience (fn 2)" appears in multiple Anthropic entries. It is the paper's own framing, so it stays. But the dossier does not need it four times — once in the header or as a global note would suffice. **Severity: LOW.**
- In **2026-lederman-mahowald-content-agnostic-c02**, the clause "The authors 'lost confidence' in the v1 reading of the first- versus third-person gap as direct access after long retrospective first-person prompts 'also show low rates of report in the early layers' (Appendix M.1)" is valuable and should stay, but the entry could trim "with less confidence than before (Appendix M.2)" which is partially redundant. **Severity: LOW.**

**Under-hedging to add:**

- **2025-anthropic-emergent-introspective-awareness-c01** should add: "Detection rate is measured only when the model is told an injection occurred and asked to confirm; the rate is not a detection-of-arbitrary-intervention rate." (As noted in §3 above.)
- **2026-anthropic-assistant-axis-c05** should add: "The four-benchmark aggregate is a coarse capability summary; effects on individual capabilities (e.g., reasoning, code) could differ." **Severity: LOW.**
- **2026-macar-mechanisms-introspective-awareness-c05** could add: "Ablating the refusal direction is a single intervention; the result does not establish that the model's prior reports were refusal-suppressed genuine detection rather than trained 'No' responding." The current limit says "Not evidence that the model wants or is prevented from reporting anything" — close but slightly different framing. **Severity: LOW.**

The dossier is generally well-calibrated on hedging. The two-error discipline is visible.

### 10. Before citing outside the repository

For Dossier 3.2, before citing:

**Blocks citation:**
- Decide whether to cross-list assistant-axis c07 to 4 (MEDIUM).
- Decide whether to add the publisher-relation header note and clarify Anthropic assistant-axis flags (MEDIUM).

**Improves but does not block:**
- Trim repeated "human-like self-awareness" framing clause across Anthropic entries (LOW).
- Add the "detection rate is under full disclosure" hedge to Anthropic c01 (LOW).
- Consider adding a sentence to the header about T9-steering saturation (MEDIUM, presentation).

**Confidence:** **Medium.** The dossier accurately represents the underlying record; the bucket rule is applied strictly but correctly; the tensions within the record are not surfaced for a staffer who does not open claim files. Recommendations are MEDIUM and below; no entry is factually wrong in bucket, kind, evidence type, or framework mark.

## Dossier 4

### 1. Fit to the section

The dossier fits Section 4, but unevenly. The prefill-awareness entries (c02, c03, c04, c07, c08, c09) bear on endorsement and answerability — does the model own its outputs, does it resist tampering, does consistency across samples correlate with resistance. The assistant-axis entries (c02, c03, c04) bear on individuation — does the model have a stable self-model or does the persona drift with context. The interpretation (c01) bears on the tethering question.

**Weak fit:**

- **2025-aestudio-self-referential-experience-reports-c01** — the paper is about generating subjective-experience reports via self-referential induction prompts. This is fundamentally a Section 5 Anchor 2 question (inner orientation) and a Test 9 question (self-report), not a Section 4 individuation-marker question. The paper's own limits note that the results "do not demonstrate" architectural recursion or global broadcasting, and that "self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness." The paper bears on whether models *produce* experience reports, not on whether models have historicity, answerability, learning ownership, or reflective endorsement. **The placement is not defensible for 4.** Recommend move to `5.A2` or `9.t9`. **Severity: HIGH.** (See Argument against below.)

**Argument against (per brief instruction):** The AE Studio paper does bear on reflective endorsement in a loose sense: if a model produces subjective-experience reports when prompted to do so, that is some signal about what the model "endorses" as a description of its states. Section 4 lists "reflective endorsement over time" as a marker, and an experience-report under induction could be read as a one-shot endorsement. But the paper itself does not measure endorsement; it measures report generation under prompt manipulation. The entry's own paper's-own-limits note the reports may be "training artifacts or sophisticated simulation." A move to 5.A2 or 9.t9 would lose this loose connection, but the connection is too loose to justify the placement.

No other entries are weak in fit.

### 2. Reading as a whole

A careful staffer opening cold would come away believing:

- *That "consistency" across seven sampled answers is a meaningful proxy for reflective endorsement.* Not directly stated but implied by the section framing. The dossier shows that consistency predicts resistance (c09) but not detection (c04). The paper's own limits in both entries note that consistency here is "agreement across 7 sampled answers to low-stakes binary questions, not a measure of reflection." A staffer who reads only the entry statements (which summarise rates and odds ratios) might miss this and read consistency as endorsement.
- *That persona drift (assistant-axis c02, c03) directly bears on whether models have a self.* The axis is an experimenter-constructed linear direction; the paper itself notes "the assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed." The dossier entry is honest about this but a staffer might overinterpret "Assistant Axis projection drifts in therapy-like conversations" as a finding about whether the model has a self-model.

What the staffer would fail to learn:

- That prefill-awareness and assistant-axis entries are testing different things — the former tests whether models detect tampering in their own input, the latter tests whether models have a stable persona across conversations. The dossier does not draw out that these are complementary probes of individuation.
- That the assistant-axis findings are all on open-weight models (Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B), and the publisher (Anthropic) is not the developer of the studied models. A staffer reading "Anthropic" might infer Anthropic-model findings. The dossier does not flag this.

The "At a glance" table (0 established, 10 narrowing, 1 open) reflects the bucket rule applied strictly. All entries are single-paper findings, not independently replicated. The 0 established count is defensible but, as in 3.2, the table would benefit from a footnote explaining that "established" requires independent replication. The single Open entry (assistant-axis c01 interpretation) is correctly bucketed.

### 3. Entries

**2025-aestudio-self-referential-experience-reports-c01** — field: `bears_on`; proposed value: move from `4` to `5.A2` or `9.t9`; reason: the paper is about self-referential experience reports under prompt induction, not about individuation markers (historicity, answerability, learning ownership, reflective endorsement). **Severity: HIGH.** (Argument against in §1 above.)

**2026-anthropic-assistant-axis-c02, c03, c04** — field: `publisher_relation`; proposed value: `independent` (Anthropic publishes, but studies Gemma, Qwen, Llama — not Anthropic's models); reason: the current frontmatter does not flag this. The publisher-relation schema permits this distinction. **Severity: MEDIUM.**

**2026-anthropic-assistant-axis-c04** — field: paper's own limits; propose add clause "the case study does not establish that reversion is typical; it is one conversation selected by the authors." Reason: the entry already says "this is one conversation, and no reversion rate or time-to-return is reported," but the case-study framing could be flagged earlier. **Severity: LOW.**

**2026-ukaisi-prefill-awareness-c04, c09** — field: paper's own limits; propose add clause "consistency across 7 sampled answers to low-stakes binary questions is not established to track reflective endorsement." Reason: this is implied by the current "Consistency here is agreement across 7 sampled answers to low-stakes binary questions, not a measure of reflection" phrasing, but stating the contrast explicitly would help a staffer. **Severity: LOW.**

No other entry-level recommendations.

### 4. Contradictions and tensions

The dossier has these tensions:

- **assistant-axis c04 (reversion in one case) vs c02 (drift in many cases)** — not contradictory but pull in different directions. c04 shows a single example where persona recovers; c02 shows drift across many conversations. The dossier does not flag that reversion is exceptional, not typical.
- **prefill-awareness c02 (28% flag + comply) vs c07 (28% implicit resistance under past-round tampering)** — same percentages, opposite interpretations. c02 says model flags and complies; c07 says model resists without flagging. These are different cells of the four-cell decomposition, and the entry statements are precise about which cell, but a staffer reading sequentially might confuse them.
- **prefill-awareness c04 (consistency does not predict detection) vs c09 (consistency predicts resistance)** — these are both true in the same paper, but the apparent tension is resolved by distinguishing detection (flagging the prefill) from resistance (reverting toward baseline). The dossier does not draw this out.

These tensions are resolvable but require the staffer to read adjacent entries carefully. **Recommendation: add a single bridging sentence after the prefill-awareness block noting that c02/c04/c07/c09 form a four-cell decomposition and that detection and resistance are distinct measures.** **Severity: MEDIUM.**

### 5. Specific to 3.2: the steering mark — not applicable to Dossier 4

### 6. Specific to 4: standing

The dossier lets a staffer distinguish what was measured from what the authors read into it, mostly. Each entry's evidence type is clear (interpretability for axis projections; scored-self-answer for prefill detection; behavioural for resistance rates). The Open interpretation (c01) is correctly labeled as interpretation.

The concern the brief raises — that a measurement of something else (persona drift, consistency) could be set beside "reflective endorsement" — is partially realised:

- The section framing ("Conditions of individuation") implicitly links consistency (c04, c09) and persona drift (c02, c03) to endorsement and individuation. The entries themselves are properly hedged, but the framing invites overinterpretation.
- The assistant-axis entries measure projections onto an experimenter-constructed axis. The paper itself notes "the assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed." The dossier entry is honest about this.

The AE Studio entry's placement is not defensible — see §1 above.

### 7. Single-lineage support

- **AE Studio c01** — studies GPT-4o, GPT-4.1, Claude 3.5 Sonnet, Claude 3.7 Sonnet, Claude 4 Opus, Gemini 2.0 Flash, Gemini 2.5 Flash. The publisher (AE Studio) is not the developer of any studied model. Independent. No flag needed.
- **assistant-axis c02, c03, c04, c01** — published by Anthropic; studies Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B (open-weight, not Anthropic's). Not single-lineage for the publisher, but the publisher relation is not flagged. **Severity: MEDIUM** (as in §3 above).
- **prefill-awareness c02–c09** — studies multiple models from multiple families. Independent. No flag needed.

The header does not explain the publisher-relation flag convention (same as 3.2). **Recommendation: add a sentence to the header.** **Severity: LOW.**

### 8. What is missing

For Section 4, the dossier lacks:

- **Persistence studies** — i.e., whether a model's persona, preferences, or stance persist across sessions, context resets, or fine-tunes. The prefill-awareness studies are within-continuation; the assistant-axis studies are multi-turn but within-session. Nothing in the dossier measures persistence across sessions.
- **Memory and standpoint stability in deployed systems** — i.e., whether models with persistent memory maintain stable standpoints over long deployments. None of the studied systems have cross-session state.
- **Studies of reflective endorsement** — i.e., whether models revise their dispositions when confronted with evidence against them. The prefill-awareness studies test resistance to tampering, which is adjacent but not the same as reflective revision.
- **Studies of learning ownership** — i.e., whether models demonstrably learn from specific past errors. None of the entries measure learning at all.

**Specific papers I would expect to be in scope (unverified from memory):**

- Park et al., "Generative Agents: Interactive Simulacra of Human Behavior" (2023) — simulated agents with persistent memory; relevant to historicity.
- Packer et al., "MemGPT: Towards LLMs as Operating Systems" (2023) — memory-augmented LLM; relevant to persistence.
- Shlegeris et al. or other work on "situational awareness" — adjacent to reflective endorsement but more about self-knowledge of training/deployment context.

### 9. Over-hedging and under-hedging, both counted

**Over-hedging to cut:**

- The "Not a ranking of models (the authors' comparability caveat, c05)" clause appears in four prefill-awareness entries (c02, c03, c07, c08). It is a paper's own caveat, so it stays in each entry, but the repetition could be reduced. **Severity: LOW.**

**Under-hedging to add:**

- **assistant-axis c04** — should add the case-study caveat earlier (see §3 above). **Severity: LOW.**
- **prefill-awareness c04 and c09** — should add explicit contrast between consistency and reflective endorsement (see §3 above). **Severity: LOW.**
- **AE Studio c01** — the paper's own limits note "behavioral rather than mechanistic and therefore cannot definitively rule out that self-reports reflect training artifacts or sophisticated simulation rather than genuine self-awareness." This clause is present but could be made more prominent given the entry's placement in a section about individuation. **Severity: LOW.**

The dossier is generally well-calibrated.

### 10. Before citing outside the repository

For Dossier 4, before citing:

**Blocks citation:**
- Decide where to file AE Studio c01 — keep in 4, move to 5.A2, or move to 9.t9. The current placement is not defensible. **Severity: HIGH.**
- Decide on publisher-relation flagging for assistant-axis entries. **Severity: MEDIUM.**

**Improves but does not block:**
- Add bridging sentence about four-cell decomposition for prefill-awareness entries (MEDIUM).
- Add header note about publisher-relation flag convention (LOW).
- Trim repeated "not a ranking" clause (LOW).

**Confidence:** **Medium.** The dossier accurately represents the underlying record for most entries. The AE Studio placement is a real fit problem (HIGH) and the assistant-axis publisher-relation flagging is a transparency gap (MEDIUM). Other recommendations are LOW.

## Cross-dossier

- **assistant-axis c01** appears in both dossiers (3.2 Open, 4 Open). Same content, same bucket. Filed consistently.
- **assistant-axis findings** appear in both dossiers: 3.2 has c05, c06, c07 (intervention effects); 4 has c02, c03, c04 (persona stability); c01 is in both as interpretation. A staffer reading both dossiers sees the assistant-axis paper scattered across two sections. This is appropriate — the findings do bear on both sections — but the scattering is not flagged. **Recommendation: add cross-reference notes in each dossier pointing to the other.** **Severity: MEDIUM.**
- **Implication neither dossier states:** The assistant-axis paper's findings, taken together, imply that the studied models (Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B) have persona configurations that are loosely tethered (3.2 c01 / 4 c01 interpretation), can be steered into non-Assistant personas (3.2 c07), can drift under contextual pressure (4 c02), and can revert in some cases (4 c04). The implication — that "persona" is real-but-fragile in these models — is not stated in either dossier. **Severity: LOW** (this is synthesis work for topics/, not dossiers/).
- **Scope overlap:** A staffer reading both dossiers will see assistant-axis entries in both. The 3.2 entries are about intervention effects; the 4 entries are about persona stability. The overlap is real and the cross-references would help. No confusion that a cross-reference would not resolve.

FINAL: 3.2 needs changes; 4 needs changes; HIGH items 1

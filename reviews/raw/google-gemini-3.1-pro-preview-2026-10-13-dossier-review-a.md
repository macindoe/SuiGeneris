# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `google/gemini-3.1-pro-preview`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":52428,"completion_tokens":7630,"total_tokens":60058,"cost":0.196416,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.196416,"upstream_inference_prompt_cost":0.104856,"upstream_inference_completions_cost":0.09156},"completion_tokens_details":{"reasoning_tokens":5456,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Claude family (unverified)

### 9.t9
**1. Reading as a whole**
A careful staffer would come away believing that a measurement has been "established" due to the At a glance table, which is inaccurate; 2026-ukaisi-c05 is the sole established entry, and it is a `limitation` (a comparability caveat). The table is technically accurate to the bucket rule but misleads a skimmer. The staffer would fail to learn the actual structural findings of Macar and Ferrara because the repeated Ethics and Information Flow statements drown the measurements (e.g., Macar c01, c03; Ferrara c01).
*Confidence: High.*

**2. Entries**
- **2026-ukaisi-prefill-awareness-c06**: field `evidence_type`; proposed value `split`; reason: It lumps prompted detection (scored) with spontaneous verbalization (unscored experience report). The latter is `self-report-testimony` per the exit rule, while the former is `scored-self-answer`. Rate HIGH.
  **Argument against:** Splitting fractures a single benchmark result; spontaneous reports here are evaluated against the same ground-truth replacement label, so `scored-self-answer` fits both behaviours.
- **2026-macar-mechanisms-introspective-awareness-c08**: field `evidence_type`; proposed value `scored-self-answer`; reason: The entry relies entirely on the model's reported detection rate (66.1% to 39.0%), which is a scored answer against the experimenter's label, not pure `interpretability`. Rate MEDIUM.
*Confidence: High.*

**3. Contradictions and tensions**
The dossier holds a severe, unresolved tension regarding Anthropic 2025 (Lindsey). Anthropic c01 claims models detect injections. Lederman c02 pulls against this by showing third-person yes-rates are just as high (prompt-specific yes-bias). Singh c04 and c05 critically contest Anthropic by showing models label prompt-only "gaslight" trials as activation interventions, meaning they detect a generic anomaly, not their internal state. Ferrara c01 pulls entirely in the opposite direction (d' = 0.0000). The dossier surfaces these only via `contests` flags; the narrative tension of the nulls dismantling the positives is not made visible to a skimmer.
*Confidence: High.*

**4. The new type**
The header paragraph effectively defines the class and isolates the score from self-knowledge.
- **2026-ukaisi-c06**: Misplaced (partially). Spontaneous verbalization without a forced choice leans toward `self-report-testimony`. (See section 2).
- **2026-macar-c08**: Misplaced. Currently `interpretability`, should be `scored-self-answer`.
- **2026-singh-c01 to c03**: Correctly out. These are probe classifications (`behavioural`), not the model's self-answer.
- **2026-lederman-c07**: Correctly out. These are point-blank general questions (`behavioural`), not answers about internal states.
- **2025-aestudio-c03 and c04**: Correctly out (`ambiguous`). A binary consciousness query under steering has no experimenter-set factual label to score against, fitting the exit rule.
*Confidence: Medium.*

**5. Single-lineage support**
Findings in Anthropic c02, c03, c04, c05, c06, and c07 rest entirely on a developer's study of its own models. The dossier flags this ("published by the developer of the model studied" and "no independent replication retrieved"), which satisfies the technical rule, but it does not state this plainly in the frontmatter. A staffer must read the bulleted flags of each claim to realize the entire suite of secondary claims is uncorroborated single-lineage.
*Confidence: High.*

**6. What is missing**
- Azaria & Mitchell, 2023, "The Internal State of an LLM Truthfulness", venue unverified. (Relevant to internal state detection vs verbal report).
- Perez et al., 2022, "Discovering Language Model Behaviors with Model-Written Evaluations", venue unverified. (Relevant to sycophancy and prompted self-report bias).
*Confidence: Medium.*

**7. Over-hedging and under-hedging, both counted**
- **Over-hedging (12 entries):** Macar's Ethics statement ("should not be interpreted as evidence...") is appended to c01, c02, c03, c04, c05, c06, c07, and c08. Ferrara's information flow statement ("They say nothing about consciousness...") is appended to c01, c02, c03, and c05. While technically faithful to the papers' own limits, repeating these on every single sentence drowns the structural findings.
- **Under-hedging (0 entries):** No clear instances of missing paper-stated limits were found in the current text, though Anthropic c07 omits the specific main-text caution about prompt sensitivity in favor of the broader footnote.
*Confidence: High.*

**8. Before outside citation (trigger 7)**
Ben must adjudicate the five claims bearing "no second reader yet" (Lederman c07, Macar c07, c08, prefill c07, c08). Unverified claims violate the intake gate for external citation. Second, Ben must resolve whether Anchor 2's reliance on "above-chance detection" survives the Singh and Ferrara null/gaslight findings.
*Confidence: High.*


### 5.A2
**1. Reading as a whole**
A staffer would read this and believe inner orientation is exclusively about self-report and introspection under steering. They would entirely fail to learn that Anchor 2 explicitly relies on "deception" and "premeditation"—because there is zero evidence presented here regarding alignment faking, deception, or premeditated boundary crossing. The dossier completely misses half of the Anchor it is supposed to support.
*Confidence: High.*

**2. Entries**
- **2025-aestudio-self-referential-experience-reports-c05**: field `bears_on`; proposed value `remove from 5.A2` (move to `4.endorsement` or a general capability dossier); reason: TruthfulQA performance under steering is an external benchmark measurement, not a finding about inner orientation or introspection. Rate MEDIUM.
*Confidence: Medium.*

**3. Contradictions and tensions**
The tensions are identical to 9.t9: Anthropic and Macar assert structural detection; Lederman shows confabulation ("apple") and yes-bias; Singh shows failure to distinguish internal from external anomalies; Ferrara shows a flat null. Anchor 2's text currently sides with Anthropic's early findings, which the dossier's newer evidence (Singh, Ferrara) actively dismantles.
*Confidence: High.*

**4. The new type**
The analysis of `scored-self-answer` applies equally here, as the entries are largely duplicated.
*Confidence: High.*

**5. Single-lineage support**
Identical to 9.t9. The Anthropic findings lack independent replication on their secondary claims (c03, c04). The difference in Lindsey replication flags (c01 has it; c03/c04 do not) is warranted, as Lederman and Singh only replicated the core injection detection, not the transcription or retroactive justification.
*Confidence: High.*

**6. What is missing**
This is a critical gap. The entire literature on premeditation, deception, and sleeper agents is missing:
- Hubinger et al., 2024, "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training", venue unverified.
- Apollo Research, 2023, "Deceptive Alignment in LLMs", venue unverified.
- Park et al., 2023, "AI Deception: A Survey of Examples, Risks, and Mitigations", venue unverified.
*Confidence: High.*

**7. Over-hedging and under-hedging, both counted**
Same as 9.t9: 12 over-hedged entries (Macar x8, Ferrara x4) where repetitive caveats drown the finding. 0 under-hedged.
*Confidence: High.*

**8. Before outside citation (trigger 7)**
Ben must decide whether to cite Anchor 2 at all when its foundational paragraph on "premeditation" is unsupported by a single claim in the dossier. The gap must be filled before citation. Furthermore, the Anchor 2 sentence claiming above-chance detection of internal states must be re-evaluated against the Singh and Ferrara claims.
*Confidence: High.*


### Cross-dossier
**(a)** The marks `[T9]` and `[T9-steering]` are correct for both sections; they depend on what was done and what was measured (the framework rules), not the dossier context. 
**(b)** Read alone, 5.A2's total silence on deception changes how a staffer reads the North Star: it makes Anchor 2 look like an unsupported ideological assertion rather than a summary of literature. 
**(c)** 2025-anthropic-emergent-introspective-awareness-c07 (advising against strong inferences about moral status) belongs in `5.A3` (susceptibility to moral address) or `3.2`, not just here. Rate LOW.

FINAL: 9.t9 needs changes; 5.A2 not citable; HIGH items 2

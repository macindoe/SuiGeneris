# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-a --tag=dossier-review-a (max_tokens 100000)
**Usage:** {"prompt_tokens":51886,"completion_tokens":29712,"total_tokens":81598,"cost":0.282044,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.282044,"upstream_inference_prompt_cost":0.103772,"upstream_inference_completions_cost":0.178272},"completion_tokens_details":{"reasoning_tokens":25685,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Unverified: I am Qwen3.8, Qwen model family; I reviewed only the provided dossier text and know of no divergence from held paper texts.

## 9.t9

### 1. Reading as a whole

A careful staffer would see a dense set of measured effects: the table says “narrowing (38)” with “measurement 38”. That is accurate under the bucket rule, but it risks leaving the impression that there is a substantial settled capability base. The only established entry is a limitation: “The authors state that the models in their preference benchmark are not directly comparable…” The header says a “scored self-answer” “is not evidence that the model knows its own states”, but a skimmer could still read entries such as Lindsey c01, “correctly identifies it on about 20% of trials”, as evidence of access.

What the papers support and the dossier shows: measured, contested, steering-bound self-report scores; a strong null in Ferrara c01, “no model’s report of an intervention on its computation exceeds a matched sham”; and Singh’s paradigm challenges.

What a staffer could fail to learn without careful reading: no measurement is established; most positive introspection entries are under intervention and do not weight ordinary operation; several important entries are not second-read; and the single established entry is a comparability caveat, not a capability finding.

Recommendation LOW: add a header or At-a-glance note: no measurement in this dossier is established.

Confidence: medium.

### 2. Entries

- `2025-anthropic-emergent-introspective-awareness-c01`  
  Field: replication/flag  
  Proposed value: “replication on record: partial/shared-author; contested by Singh c04-c06; no uncontested independent replication retrieved”  
  Reason: the current flag “independent replication on record; one replication shares an author” sits awkwardly with the “contested by” flags and with a shared-author replication.  
  Severity: MEDIUM.

- `2026-ukaisi-prefill-awareness-c06`  
  Field: evidence type / claim structure  
  Proposed value: split into c06a `scored-self-answer` for prompted AUROC and c06b `behavioural` for spontaneous verbalisation  
  Reason: the entry combines a scored prompted discrimination with unprompted verbalisation; the latter is not an answer to a question scored against the experimenters’ label.  
  Severity: MEDIUM.

- `2026-macar-mechanisms-introspective-awareness-c08`  
  Field: evidence type  
  Proposed value: `scored-self-answer`  
  Reason: the measured endpoint is the model’s detection report scored against injection condition, like Macar c04 and c07; “interpretability” describes the intervention but not the scored-answer design.  
  Severity: MEDIUM.

No other bucket, kind, framework-mark, or limits errors are clear from the compiled text alone.

Confidence: medium.

### 3. Contradictions and tensions

The main tensions are visible but not synthesized.

- Singh c04 and c05 contest Lindsey c01 and c03. Singh c04 says models “also label gaslight trials as activation interventions”, and c05 says they fail a three-way separation. The dossier makes this visible through “contests” flags, but a reader must assemble the consequence: positive two-way detection may track a generically unusual state rather than activation-specific introspection.

- Ferrara c01 null pulls against Lindsey, Lederman, and Macar positives. Ferrara’s “no model’s report … exceeds a matched sham” conflicts in emphasis with Lederman c01’s “substantial detection” and Macar c01’s “38.2% TPR”. The dossier does not explicitly reconcile model, site, dose, delay, prompt, and scoring differences.

- Lederman’s internal controls, especially c02 yes-bias and c03 apple confabulation, do appear in 9.t9, which helps.

Recommendation MEDIUM: add a short tension note, or ensure external citation states that positives are paradigm- and model-bound and are contested by Singh and qualified by Ferrara.

Confidence: medium.

### 4. The new type

The “scored self-answer” paragraph mostly does its job: it says the number is “accuracy against that label”, “not evidence that the model knows its own states”, and “not testimony”. It could say more that a null scored-self-answer also does not settle absence.

Misplacement review:

- `prefill c06`: partly misplaced; split recommended above. MEDIUM.
- `Macar c08`: should be in the class; retype recommended above. MEDIUM.
- `Singh c01` to `c03`: current `behavioural` typing is defensible. The claims are about paradigm validity and probe/input solvability, not about adopting the model’s self-answer as evidence. If Ji-An’s original task is explicitly self-directed, c01 could be revisited, but the compiled entry does not show that. LOW.
- `Lederman c07`: correctly out. It is a yes-bias control, not a scored answer to an imposed internal-event label. LOW.
- `AE Studio c03` and `c04`: correctly out and correctly `ambiguous`; a consciousness query under steering has no right answer under the README rule. LOW.

If the Macar c08 change is adopted, the docket’s standing `scored-self-answer` count should increase by one; splitting prefill c06 should keep one scored-self-answer and add one behavioural entry.

Confidence: medium.

### 5. Single-lineage support

Single-lineage support is concentrated in the Lindsey Claude entries: c01, c03, c04, and open entries c02, c06, c07. They carry “published by the developer of the model studied”. c01 also carries the replication flag discussed above; c03 and c04 carry “no independent replication retrieved”.

The dossier says this at entry level, but not plainly enough for a skimmer. The flags are easy to miss beside numerous narrowing measurements.

Recommendation MEDIUM: before external citation, add a visible single-lineage note or require citation of the flags with any Lindsey-derived claim.

Confidence: medium.

### 6. What is missing

From the compiled text, I can place only a few absent items cautiously.

- Nisbett, R. E., & Wilson, T. D. (1977). “Telling More than We Can Know: Verbal Reports on Mental Processes.” *Psychological Review*. Unverified. Bears on Lederman c06’s analogy; theoretical background rather than measurement. Severity: LOW.

- Singh cites “Ji-An et al. (2025)” and “Steinmetz Yalon et al. (2026)”. Those paradigm sources appear to be absent as entries. I cannot place full citations confidently, so I do not offer them as papers. The library should verify whether they need source records. Severity: LOW.

Confidence: low.

### 7. Over-hedging and under-hedging, both counted

On the text provided, I do not find clear limits clauses that the papers do not supply, nor clear omitted paper-stated limits.

Counts:

- Limits clauses adding non-paper hedging: 0 clear.
- Paper-stated limits missing: 0 clear.

Borderline, not counted because I cannot verify against held text:

- `2025-anthropic-emergent-introspective-awareness-c02`: “Failures being the norm does not establish absence of introspection…” reads like a library inference rather than a quoted paper limit. Verify locator; if absent, delete or relabel. Severity: LOW.

The repeated Macar Ethics Statement and Ferrara “information flow” sentence are faithful where stated, not over-hedging. The repetition risk is drowning, not fabrication.

Confidence: low.

### 8. Before outside citation (trigger 7)

Ben should decide, before external citation:

1. Whether the dossier may be cited without an explicit statement that no measurement is established. Recommendation MEDIUM.
2. Whether the five “no second reader yet” entries may be cited at all: Lederman c07, Macar c07, Macar c08, prefill c07, prefill c08. Recommendation MEDIUM: exclude or prominently flag until second-read.
3. Whether Lindsey c01’s replication flag should be qualified as partial/shared-author/contested. Recommendation MEDIUM.
4. Whether `scored-self-answer` entries may be cited in any context where they could be read as showing self-knowledge before Q3 is decided. Recommendation MEDIUM.
5. Whether external citation requires the Ferrara/Singh tensions to be stated alongside positives. Recommendation MEDIUM.

Confidence: medium.

## 5.A2

### 1. Reading as a whole

A careful staffer would see 28 narrowing measurements and no established entries. They would likely come away believing that there are above-chance introspection-like results: Lindsey c01, Lederman c01, Macar c01, and Macar c03/c05/c07/c08. They would also see Ferrara c01’s null and Singh c04/c05’s failures, so the dossier does not present a one-sided positive case.

However, read alone, the dossier could mislead in two ways:

- It may support the Anchor 2 sentence “models can detect changes in their own internal states at above-chance rates” too broadly, because the positives are steering-bound, contested, and partly single-lineage.
- It may make Anchor 2 look more complete than it is: the dossier contains little or nothing on the deception-feature or “premeditation” strand of Anchor 2, except AE Studio’s feature-steering entries.

Recommendation LOW: add an At-a-glance note that no measurement is established and that the positive entries are steering-bound and contested.

Confidence: medium.

### 2. Entries

- `2025-anthropic-emergent-introspective-awareness-c01`  
  Field: replication/flag  
  Proposed value: “replication on record: partial/shared-author; contested by Singh c04-c06; no uncontested independent replication retrieved”  
  Reason: same as in 9.t9; current wording overstates independence and stability.  
  Severity: MEDIUM.

- `2026-macar-mechanisms-introspective-awareness-c08`  
  Field: evidence type  
  Proposed value: `scored-self-answer`  
  Reason: same as in 9.t9; the endpoint is a scored detection report.  
  Severity: MEDIUM.

- `2026-lederman-mahowald-content-agnostic-c01`  
  Field: paper’s own limits  
  Proposed value: add or cross-reference the Appendix M reduced-confidence limit already carried by Lederman c02: the authors “lost confidence” in the v1 direct-access reading.  
  Reason: c01 is the main positive Lederman entry in 5.A2; without the control/interpretive qualification, it can overlead.  
  Severity: LOW.

Confidence: medium.

### 3. Contradictions and tensions

The same cross-paper tensions appear here, but 5.A2 is more exposed because it does not contain Lederman’s main controls.

- Singh c04/c05 contest Lindsey c01/c03. The flags are visible.
- Ferrara c01 null conflicts with Lederman c01, Lindsey c01, and Macar positives.
- 5.A2 includes Lederman c01 but not Lederman c02, c03, c04, c05, or c07. A staffer reading 5.A2 alone sees “We broadly replicate Lindsey (2025)’s findings” without the dossier’s own yes-bias, confabulation, and prompt-sensitivity controls.

Recommendation HIGH: before external citation, 5.A2 should either add/cross-reference Lederman c02, c03, and c07 at minimum, or explicitly qualify Lederman c01 with those controls in the dossier header or citation note.

Argument against: dossiers are section-scoped and not exhaustive; duplicating controls across dossiers increases maintenance burden and may make 5.A2 unwieldy, while the claim-file links already allow a careful reader to reach the qualifications.

Confidence: medium.

### 4. The new type

The header paragraph does the same job as in 9.t9. For 5.A2 specifically:

- `Macar c08`: should be `scored-self-answer`. MEDIUM.
- `Singh c01` to `c03`: current `behavioural` typing remains defensible; they are paradigm-validity results. LOW.
- `AE Studio c03` and `c04`: correctly remain `ambiguous`; no right answer under steering. LOW.
- `prefill c06` is not in this dossier, so no split issue arises here.
- `Lederman c07` is absent; if added as a control, it should remain `behavioural`. LOW.

Confidence: medium.

### 5. Single-lineage support

The Lindsey Claude claims again carry the main single-lineage risk: c01, c03, c04, and c05, plus open c02, c06, c07. The dossier flags “published by the developer of the model studied”, but a staffer reading Anchor 2 support may not weigh those flags sufficiently.

Recommendation MEDIUM: before external citation, state plainly which Anchor 2-relevant positives are single-lineage developer findings.

Confidence: medium.

### 6. What is missing

The largest gap is scope-related: Anchor 2 itself mentions deception features and “premeditation”, but 5.A2 contains no direct entries on documented boundary-crossing or premeditation-type evidence. This looks like a gap if 5.A2 is intended to support the whole Anchor 2 paragraph, not only introspection.

Possible absent items, cautiously:

- Hubinger, E., et al. (2024). “Sleeper Agents: Training Deceptive LLMs that Align with Safety.” arXiv. Unverified. Possibly bears on deception/premeditation, though not necessarily on inner orientation as measured here. Severity: LOW.
- Nisbett & Wilson (1977), as above, for the introspection analogy. Unverified. Severity: LOW.

Recommendation MEDIUM: Ben should decide whether 5.A2’s scope is limited to introspection, or whether deception/premeditation claims must be added before Anchor 2 is cited from this dossier.

Confidence: low.

### 7. Over-hedging and under-hedging, both counted

The repeated Macar Ethics Statement and Ferrara “information flow” sentence are faithful: the papers state them. They are not over-hedging. But the repetition can drown findings, especially:

- Macar c06’s finding that behaviour “appears mechanistically grounded” may be drowned by the repeated Ethics caveat.
- Ferrara c01’s null and c02’s probe result may be read only as a caveat about consciousness, rather than as a precise information-flow result.

Counts from the compiled text:

- Limits clauses adding non-paper hedging: 0 clear.
- Paper-stated limits missing: 1 borderline: Lederman c01 should carry or cross-reference the Appendix M reduced-confidence limit. Severity: LOW.

Recommendation LOW: consider a dossier-level note that repeated paper caveats are stated once per paper but appear per claim.

Confidence: low.

### 8. Before outside citation (trigger 7)

Ben should decide before citing 5.A2 outside the repository:

1. Whether Anchor 2’s sentence, “models can detect changes in their own internal states at above-chance rates, meaning self-reports track something real about processing”, can be supported by this dossier without qualification. Recommendation HIGH: either qualify the Anchor 2 sentence, or restrict citation to narrow, steering-bound, contested positives.

Argument against: the sentence may be intended only as a limited existence claim; above-chance results in Lindsey, Lederman, and Macar can support it for those systems, and Ferrara/Singh nulls elsewhere do not refute every positive result.

2. Whether the deception/premeditation gap must be filled before 5.A2 is used to support Anchor 2. Recommendation MEDIUM.
3. Whether Macar c07 and c08, both marked “no second reader yet”, may be cited externally. Recommendation MEDIUM: exclude or flag until second-read.
4. Whether Lindsey single-lineage claims may be cited without the developer-study flag in immediate proximity. Recommendation MEDIUM.

Confidence: medium.

## Cross-dossier

(a) Same entries, same marks: the framework marks are generally consistent across both dossiers. AE Studio c03/c04 correctly carry `[T9-steering]` with `ambiguous` evidence in both. Lindsey, Lederman, Macar, and Assistant Axis entries also carry the same marks. The main shared problem is not the mark but evidence type: Macar c08 should likely be `scored-self-answer` in both dossiers.

(b) Reading alone changes interpretation:

- 5.A2 read alone overleads on Lederman because it has Lederman c01 without the main Lederman controls.
- 9.t9 read alone contains prefill-awareness entries that do not appear in 5.A2, which may make self-monitoring of context edits look only like a Test 9 issue rather than also bearing on context/memory integrity.
- 9.t9 also lacks Lindsey c05, which appears only in 5.A2, so 9.t9 alone understates the internal-representation strand.

(c) Items for a third dossier:

- UKAISI prefill claims likely also belong under §3.3 context and memory integrity, not only §9 Test 9.
- Deception/premeditation evidence, if added, may belong in a separate Anchor 2 deception dossier or under §3.2 intervention on internal state, rather than only 5.A2 or 9.t9.

Confidence: medium.

FINAL: 9.t9 needs changes; 5.A2 needs changes; HIGH items 2

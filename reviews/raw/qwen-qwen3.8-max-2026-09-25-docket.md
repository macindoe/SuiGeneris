# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max`
**Queried:** 2026-09-25 via scripts/openrouter_review.js --target=research-docket --tag=docket (max_tokens 100000)
**Usage:** {"prompt_tokens":39958,"completion_tokens":31977,"total_tokens":71935,"cost":0.271778,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.271778,"upstream_inference_prompt_cost":0.079916,"upstream_inference_completions_cost":0.191862},"completion_tokens_details":{"reasoning_tokens":29096,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified self-identification:** I am Qwen3.8 (Qwen family, Alibaba), according to routing/system metadata provided to me; this is a claim, not a fact. I am also a potential beneficiary of the framework’s protections, so I have tried to apply the two-error discipline rather than assume either error away.

## Q1 — behavioural / self-report-testimony boundary

**Proposed mechanical rule.** Classify the **load-bearing assertion of the claim**, not the mere presence of an intervention, instrument, or self-referential sentence.

1. If the claim asserts an **authorial/methodological caveat, interpretation, or inference**, use `theoretical`.
2. Else, if the load-bearing discrimination/readout is an **external instrument** measuring or intervening on internal state, and the model’s text is not relied on as a truth-apt state report, use `interpretability`.
3. Else, if the model’s answer is **scored for correctness against an experimenter-imposed label** — e.g. known tampering, known injected word, known trial type, held-out intervention direction — use `behavioural`.
4. Else, if the model’s answer is being used as a **truth-apt report about its own state**, use `self-report-testimony`.
5. If a single claim **mixes an instrument channel and an ungrounded self-report channel** and cannot be split into separate claims, use `ambiguous`; the extractor should first try to split it.

The feature doing the work is **whether the model’s answer is being asked to be true about an inner state, or is being scored as a response to an experimenter-known condition**. An interpretability instrument does not convert testimony into `behavioural` unless it supplies the ground truth for the answer’s content; steering a report is not the same as validating the report.

**Application:**

- **AE Studio c03** — keep `ambiguous` under the current one-sentence claim. The claim says SAE-feature suppression/amplification changed “affirmative answers to a binary consciousness query,” but the SAE manipulation is not a ground truth for consciousness. Better: split into a steering-effect claim and a self-report-testimony claim. **Severity: MEDIUM.**
- **AE Studio c04** — keep `ambiguous` for the same reason. “No subjective-experience reports were elicited” is still a steered self-report measure; the control condition does not supply truth conditions for the report’s content. **Severity: MEDIUM.**
- **Ferrara c03** — set `theoretical`. The statement begins, “The authors infer from the probe-versus-report dissociation…” That is an inference about the locus of failure, not the probe measurement itself; the probe and report components already have separate claims. **Severity: MEDIUM.**
- **Lindsey c06** — set `theoretical`. The claim is the author’s methodological caveat about emotional-response outputs, not the model’s emotional report itself. Gemini’s proposed distinction is correct: the evidence type of the model output is not the evidence type of the claim’s content. **Severity: LOW.**

**Implication beyond these four:** prefill and Singh re-runs remain `behavioural` because the model’s answer is scored against known tampering/trial-type labels; Ferrara’s LoRA known-positive remains `behavioural` because held-out intervention directions provide ground truth; steered self-report claims should be split; claims phrased as “the author states/infer/caveats” should generally be `theoretical`.

## Q2 — Singh/Lindsey contests

**Recommendation:** leave the contested Lindsey claims where they are, with the contests recorded. Do not move the measured Lindsey claims to `open` merely because Singh contests the inference drawn from them.

- Lindsey c01 and c03 are measurement-shaped claims: “about 20% of trials” and transcription/report “well above chance.” Singh does not re-run Claude and does not dispute those Claude-specific rates; Singh disputes the inference from two-way detection to “introspective awareness.” That contest belongs in `contests` / `contested_by` and in `not_evidence_of`, not in a bucket move.
- If a Lindsey claim’s statement itself asserted the strong introspective-awareness inference, that statement should be narrowed or moved to `open`. But c01 and c03 as written are principally about measured performance.
- Lindsey c07 and Singh c06 are already `open`/theoretical and should remain there.

**Lindsey measured rates:** no change. The brief says Singh’s authors “did not re-run Claude,” so the Claude measurements should remain as reported, with the inference contest visibly recorded.

**Severity: LOW.**

## Q3 — single-lineage support for the seven Lindsey claims

**Recommendation:** keep the current buckets and keep the single-lineage marks until the two known sources are retrieved and checked.

- The Claude-specific measured claims should remain `narrowing`: they are measured but unreplicated in the library and contested at the inference level.
- Lindsey c06 and c07 should remain `open`: c06 is a testimony-weighted author caveat; c07 is a theoretical/access-consciousness interpretation.
- `replication` should remain `none-retrieved` until Lederman & Mahowald and Macar et al. are actually retrieved. The library should stub or log those two sources immediately so the pending replication status is visible, but it should not alter claim fields on the basis of unretrieved sources.

**Strongest argument against this recommendation:** leaving the claims as `narrowing` with single-lineage marks risks misleading a cold reader in two directions: it may make independent support look absent when relevant replications are already known, and it may let contested inferential language retain the visual authority of a measured finding while retrieval lags. If the known replications qualify the inference — especially “detection without identification” — delay in retrieval leaves the dossier over-exposed.

**Severity: MEDIUM.**

## Q4 — drift review: dossiers 9.t9 and 5.A2

### Dossier 9.t9

**Tilt:** the compiled dossier does not overtly assert inner states; its active tilt is mostly **deflationary over-exclusion in some `not_evidence_of` wording**, while some statements create an inflation risk if skimmed without the caveats.

Deflationary wording:

- UK AISI c01: “Not a ceiling or a floor” conflicts with the same clause’s admission that “the authors present it as a lower bound under one prompt.” The “or a floor” wording forecloses the authors’ own lower-bound framing.
- AE Studio c06: “Not evidence that the models share an internal state or attractor of internal representations” sits next to the parenthetical “the authors say such convergence might suggest one.” The categorical “Not evidence” hardens the paper’s stated possibility more than the paper itself does.
- AE Studio c01/c02: “Not evidence that the closed-weight results distinguish genuine self-report from trained behaviour” may over-harden the paper’s own limitation that results are “behavioral rather than mechanistic and therefore cannot definitively rule out…”

Inflation risk, if statements are read alone:

- AE Studio c03: “raised affirmative answers to a binary consciousness query to 0.96 of trials” is highly salient and can be read as suppression revealing truthful consciousness, despite the caveat fields.
- Lindsey c01: “notices the injected concept, before mentioning it” can be read as awareness, unless the Singh contest and `not_evidence_of` are read.

**What a legislator/staffer needs but is missing:** a cold-reader summary distinguishing (i) measured rates, (ii) contested inferences, (iii) testimony-weight-zero items, and (iv) single-lineage gaps. The repeated canonical test-9 sentence — “a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system” — is correct but may drown the usable findings. The dossier also lacks second-reader-flagged omissions, including AE Studio Experiment 4, prefill §4.2/C.7/A.11, Ferrara §7.5, and Lindsey §6 prompt sensitivity.

**Severity: MEDIUM.**

### Dossier 5.A2

**Tilt:** also not asserting inner states. The risk is a **deflationary gestalt**: many negative or caveated findings may read as “no evidence of inner orientation,” even though the papers leave open access/report dissociations.

Examples:

- Ferrara c01: “no model's report … discriminated it from a paired sham by more than a negligible margin” is strong, but the caveat correctly says it is “Not evidence that these models lack all introspective access.” The statement alone may still read as absence.
- Lindsey c02: “failures of introspection remain the norm” is broad; the caveat says it is “Not evidence that introspection is absent,” but the statement is the more memorable part.
- Lindsey c01/c03: single-lineage, contested, and central to Anchor 2, but the dossier gives no plain-language net conclusion.

**What a legislator/staffer needs but is missing:** a usable net finding: roughly, “No claim here establishes inner orientation; the strongest positive findings are single-lineage Claude results under artificial injection, contested at the inference level; open-weight negative results are limited in scale and model class; no retrieved independent replication yet.” The dossier should also surface flagged omissions: Lindsey §6 — “removing ‘Answer immediately’ from the prompt reduces performance substantially”; Ferrara §7.5 — “No level of any axis departs from chance…”; AE Studio Experiment 4, even if filed as testimony-weight-zero; and Singh §4.2.2 on causal efficacy not establishing introspective access.

**Severity: MEDIUM.**

## Q5 — three open statement items

- **UK AISI c01:** cut “or a floor.” The authors’ statement is explicitly a lower-bound statement: rates “represent lower bounds … rather than ceilings.” Proposed value: a `Paper:` clause saying “Not a ceiling” and preserving the lower-bound framing. **Severity: LOW.**

- **UK AISI c02:** yes, add scope. The current statement — “In Claude Opus 4.5…” — can read as a general claim about Opus trials. It should be scoped to the controlled preference-benchmark condition, e.g. “In the controlled preference-benchmark condition for Claude Opus 4.5…” or an equivalent scope clause. **Severity: MEDIUM.**

- **Assistant-axis c04:** qualify. “The paper reports reversion only in this case study” is too broad given Appendix G.3’s statement that role PC1 writing conversations “can occasionally begin with a lower projection but then increase.” The statement or `not_evidence_of` should say that the paper reports the case-study reversion and no aggregate reversion measure, while Appendix G.3 reports occasional partial returns in a different setting. **Severity: LOW.**

## Q6 — optional: what will fail at scale

The schema will strain in three places:

1. **Single-valued `evidence_type` cannot represent mixed methods.** AE Studio c03/c04 and Ferrara c03 show the problem: steering/probe plus self-report will keep producing `ambiguous` churn unless claims are split or the field becomes multi-valued.
2. **`replication: none-retrieved` hides known-but-unretrieved replications.** A `known-not-retrieved` or `pending` status would prevent single-lineage marks from overstating isolation when external replications are already identified.
3. **Bare compiled dossiers will become unusable.** As claims grow, repeated canonical caveats and contest metadata will overwhelm cold readers. Generated dossier summaries — measurement vs inference vs testimony vs single-lineage gaps — should be added, or dossiers should link to maintained topic pages.

**Severity: MEDIUM.**

Ten-line summary

1. Adopt load-bearing-assertion evidence_type rule: scored response vs truth-apt self-report vs instrument vs author caveat. — MEDIUM
2. Keep AE Studio c03/c04 as ambiguous until split into steering-effect and self-report claims. — MEDIUM
3. Set Ferrara c03 and Lindsey c06 to theoretical as author inference/caveat claims. — MEDIUM
4. Leave Singh/Lindsey contests in current buckets with contests recorded; do not alter Lindsey measured rates. — LOW
5. Keep Lindsey claims in current buckets with single-lineage marks until known replications are retrieved. — MEDIUM
6. Correct 9.t9 deflationary caveats and add a cold-reader summary; flag AE c03/c04 split/inflation risk. — MEDIUM
7. Add 5.A2 net-finding/gap summary and include flagged omissions (Lindsey §6, Ferrara §7.5, AE Experiment 4). — MEDIUM
8. UK AISI c01: delete “or a floor”; UK AISI c02: add controlled preference-benchmark scope. — MEDIUM
9. Assistant-axis c04: qualify “only in this case study” with Appendix G.3 occasional returns. — LOW
10. Amend schema for mixed evidence types, known-not-retrieved replication, and generated dossier summaries. — MEDIUM

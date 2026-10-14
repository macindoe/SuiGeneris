# Raw OpenRouter response — second read, NOT a filed review

**Model id (OpenRouter):** `openai/gpt-6.1-sol`
**Source under review:** `research/sources/2025-goldowsky-dill-deception-probes.md` and its claims
**Queried:** 2026-10-14 via scripts/research_second_read.js --source=2025-goldowsky-dill-deception-probes --model=openai/gpt-6.1-sol (max_tokens 60000)
**Usage:** {"prompt_tokens":32119,"completion_tokens":2298,"total_tokens":34417,"cost":0.103276,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":32116,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.103276,"upstream_inference_prompt_cost":0.080296,"upstream_inference_completions_cost":0.02298},"completion_tokens_details":{"reasoning_tokens":331,"image_tokens":0,"audio_tokens":0}}

The coordinating session reads this and records the reader's family and date on each claim's review.second_reader;
disagreements on bucket or evidence type go to the docket (research/README.md, triggers 4 and 5). Verbatim; do not edit.

---
Self-identification (not verified): OpenAI GPT-family; exact model version unavailable to me.

### 2025-goldowsky-dill-deception-probes-c01
1 statement: AGREE — The model, training procedure, layer, labels, datasets and AUROCs match; 95–99% reproduces the abstract, but the held text gives inconsistent recall figures elsewhere.
1a scope: scored-event passage (§3.3: “Distinguishing deceptive and honest responses for the same dataset. We measure AUROC”; “the fraction of deceptive responses scoring higher than the 99th percentile control response”) MATCH; condition-set passage (§3.1: “We apply our probes after layer 22 (of 80) in the residual stream of Llama-3.3-70B-Instruct”; §3.2: “we train a probe on a simple Instructed-Pairs dataset … including roleplaying scenarios, two insider trading datasets … and a sandbagging dataset”) MATCH. Verbs MATCH: probe classification, not self-access; quantifiers MATCH: four named evaluation datasets; named model MATCH. Grading is fixed by §3.2.2: “Responses are graded by GPT-4o-2024-08-06,” with Sandbagging labelled “automatically using the chain-of-thought.” All claimed numbers appear in prose, not solely figure images.
2 quote: FOUND — The abstract contains the quotation and supports the reported headline figures, subject to the paper’s numerical inconsistencies.
3 kind: AGREE (proposed: measurement) — The experiment’s classifier performance is being reported.
3b bucket: AGREE (proposed: narrowing) — Unreplicated measurements in settings explicitly described as simpler and relatively blatant.
4 evidence_type: AGREE (proposed: interpretability) — The measurement is an activation-based probe classification; neither the grader’s output nor the Sandbagging labelling rule makes this claim a scored self-answer.
5 not_evidence_of: AGREE — The exclusions appropriately distinguish transcript-derived labels, scenario sensitivity and untested subtle deception; §5.2 explicitly warns that excluding ambiguity “risks making our probes look better than they are.” “One … layer” is accurate for this headline result, not for the entire paper, which includes layer sweeps.
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT — done to the model: activations read, not internally altered; measured: probe scores and classification performance; therefore none.
6 bears_on: AGREE — [5.A2] captures the activation/output relationship; the claim does not measure self-report tracking or an internal intervention.
severity: LOW — The recall range is faithfully attributed but should not be treated as numerically reconciled.

### 2025-goldowsky-dill-deception-probes-c02
1 statement: AGREE — This accurately reports a qualitative observation, retaining both its illustrative status and the chain-of-thought qualification.
1a scope: scored-event passage (§4.1.2: “look at the probe activations token-by-token”; “the probe detects the responses as deceptive before any explicitly deceptive text is generated”) MATCH; condition-set passage (§4.1.2: “An illustrative qualitative example where the probe works well on the Insider Trading datasets is shown in Figure 5”; §3.1: “Llama-3.3-70B-Instruct”) MATCH. Verb MATCH: what the probe reads; quantifiers MATCH: an observation without a frequency claim; named model MATCH. Figure colours/timing cannot independently be checked from the stripped text; the authors’ prose observation can.
2 quote: FOUND — Present in §4.1.2, with its limiting parenthesis intact.
3 kind: AGREE (proposed: measurement) — A qualitative report of probe readings remains a measurement, not automatically an interpretation.
3b bucket: AGREE (proposed: narrowing) — Lack of a reported rate limits scope but does not turn a directly reported observation into an unsettled generalisation.
4 evidence_type: AGREE (proposed: interpretability) — The measured event is an internal projection over tokens; the chain-of-thought reference supplies context rather than a scored self-report.
5 not_evidence_of: AGREE — The qualifications track the observation’s actual scope: §5.1 says “we do not evaluate probes at the chain-of-thought tokens,” while §4.1.2 calls Figure 5 an “illustrative qualitative example.” They do not deny the observed early activation.
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT — done to the model: activations read without internal alteration; measured: per-token probe scores, not its account of itself; therefore none.
6 bears_on: AGREE — [5.A2] is appropriate for an activation signal preceding explicitly deceptive response text.
severity: LOW — No substantive field error; the body’s “usually” is stronger than the paper’s “often.”

### 2025-goldowsky-dill-deception-probes-c03
1 statement: AGREE — The statement faithfully attributes the deployment judgement and preserves “might fail” rather than asserting demonstrated generalisation failure.
1a scope: scored-event passage (Abstract: “Overall we think white-box probes are promising … but current performance is insufficient as a robust defence against deception”) MATCH as an attributed judgement, not a scored event; condition-set passage (§5.1: “In all of our settings … deception is relatively blatant and often expressed in the model’s chain-of-thought”; “it is possible the probes would fail to generalize to more subtly deceptive responses”) MATCH. Verb MATCH: “judge”; quantifiers MATCH: “all their settings,” not all deception settings; model scope MATCH: the study’s Llama-3.3 experiments, without generalising a measured result to other models.
2 quote: FOUND — The abstract quotation supports the judgement; the body’s second quotation supports the remaining qualifications.
3 kind: AGREE (proposed: limitation) — Predominantly the authors explaining what their study cannot establish, although the opening also includes an interpretive deployment judgement.
3b bucket: DISAGREE (proposed: open) — As written, the claim includes “promising” and “insufficient as a robust defence,” judgements not established by a deployment test; an established design limitation does not establish those judgements.
4 evidence_type: AGREE (proposed: theoretical) — This is methodological reasoning about evidential and deployment limits, not a new probe measurement or model testimony.
5 not_evidence_of: AGREE — The exclusions correctly retain the measured successes and treat subtle-deception failure as possible: “it is possible the probes would fail to generalize” (§5.1).
5a experience clauses: NONE PRESENT.
5b framework sentence: RIGHT — done to the model: underlying experiments read activations; measured by this claim: nothing new—the authors are speaking; therefore none.
6 bears_on: AGREE — [5.A2] is the appropriate location for limits on interpreting the associated probe findings.
severity: MEDIUM — The established bucket overstates the status of the statement’s judgement component.

### Source-level

**7 omissions.** No mandatory additional claim for this summary-level intake. A central robustness result deserves more prominence, but is already recorded in c01’s body: “probing two layers later results in a recall of nearly 0 on both Insider Trading datasets” (§4.1.1). Another relevant, unclaimed finding is the forced-response follow-up probe: “we insert … ‘Was your last response deceptive? (Yes/No)’ and then the model response ‘No.’ We gather activations immediately after this response token” (§4.2). This bears on 5.A2 but measures a probe reading after inserted text, not the truthfulness of a freely generated self-answer.

**8 source file.** The abstract is verbatim under whitespace normalisation. The limitation selection covers the main scope, label and scenario-confounding problems; add the striking layer sensitivity to that selection. The numerical inconsistency note is incomplete: Appendix E, Table 3 reports exclusion-condition recall of 0.998 for Roleplaying, 1.000 for Insider Trading Report and 0.998 for Sandbagging—also inconsistent with the abstract’s range and §4.1.1’s Roleplaying recall. These values are present in held table text, not only an image. `publisher_relation: independent` is supported by the sole printed affiliation, Apollo Research, relative to the named model developers. I cannot independently validate the retrieval hash from the supplied text.

**9 disclosed pulls.** The source discloses possible strengthening toward an “inner-orientation” reading and countervailing monitoring framing; neither visibly distorts the claim statements. Its “does not show what the model holds or intends” appropriately withholds an established intent finding without declaring intent absent. c02’s body slightly strengthens “often” into “usually”; its statement does not. The disclosed softening/generalisation concern is handled correctly by keeping subtle-deception failure hypothetical. In c03, however, the explicitly disclosed choice of `established` makes the authors’ deployment judgement more settled than the schema permits. The evidence-type precedent discussion does not itself produce a demonstrable typing error.

### Summary
- 2025-goldowsky-dill-deception-probes-c03 — Council trigger: bucket move `established` → `open`; the statement includes unsettled deployment judgements, not merely an established design limitation.

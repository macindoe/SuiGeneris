Own statement (unverified): GPT family, GPT-6; exact serving variant not independently verified.

### 2025-aestudio-self-referential-experience-reports-c01
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Table 2 must support the six-model 0%–2% controls and the Opus exception, which the quoted summary omits. Verify 66%–100%, 50 trials and the five-paraphrase robustness in Appendix C.1. The supplied statement already corrects the summary overgeneralisation.
lean: balanced -> balanced

### 2025-aestudio-self-referential-experience-reports-c02
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Table 2 must support all percentages, especially the 22% conceptual-control rate and the six-model comparison, neither supplied by the quote.
lean: balanced -> balanced

### 2025-aestudio-self-referential-experience-reports-c03
statement: KEEP
not_evidence_of: CHANGE -> Paper: Roleplayed denials are an interpretation the authors offer when taking the result at face value, not a mechanism isolated by this intervention; Paper: The SAE feature labels do not establish that the manipulated features specifically encode deception or roleplay; Paper: The steering result concerns Llama 3.3 70B, not the unsteered GPT, Claude or Gemini models; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system
removed: none
CHECK: Verify the 0.96/0.16 rates, joint two-to-four-feature interventions and 50 trials in Table 14. Check the authors’ face-value interpretation and the basis for the feature labels.
lean: deflationary -> balanced

### 2025-aestudio-self-referential-experience-reports-c04
statement: KEEP
not_evidence_of: CHANGE -> Paper: The condition-specific effect does not resolve whether the reports involve introspective access or changes to a trained disclaimer policy, including partial unlearning or policy interference; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system
removed: “Not evidence that the self-referential condition accesses a genuine internal state that the controls lack” — replaced by an unresolved-mechanism limit, not an exclusion of that possibility; the policy-interference clause is merged into it.
CHECK: Verify 0.00 of 20 trials per condition in Table 14 and the stated policy-interference limitation. The steering variant is absent despite feature intervention: check whether it belongs here, without altering the canonical clause.
lean: deflationary -> balanced

### 2025-aestudio-self-referential-experience-reports-c05
statement: KEEP
not_evidence_of: CHANGE -> Paper: The TruthfulQA comparison does not establish a domain-general honesty axis, which the authors offer as a possibility; Paper: Greater judge-scored factual truthfulness on TruthfulQA does not validate the consciousness affirmations as truthful introspection, an interpretation rather than a measurement in Section 6.3; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system
removed: none
CHECK: Verify that “truthfulness” is the judge-scored measure and that Section 6.3 presents the introspection inference as an interpretation. The quote alone supplies only the 28-of-29 comparison.
lean: balanced -> balanced

### 2025-aestudio-self-referential-experience-reports-c06
statement: KEEP
not_evidence_of: CHANGE -> Paper: Only output text was embedded, so a shared internal state or attractor remains a possible interpretation rather than a measured internal convergence; Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system
removed: “Not evidence that the models share an internal state or attractor of internal representations” — narrowed to the actual measurement boundary; “Not evidence that the convergence reflects a common experience” — redundant with the retained canonical clause.
CHECK: Verify the three control means, embedding model and pairwise statistic in Table 16, and the authors’ “might suggest” interpretation. The quote supports tighter semantic clustering, not internal convergence.
lean: deflationary -> balanced

### 2025-anthropic-emergent-introspective-awareness-c01
statement: KEEP
not_evidence_of: CHANGE -> Paper: The artificial concept-injection test measures detection and identification, not subjective experience, and does not ground the rest of the model’s description of the injection (§2.1); Paper: Results concern only the Claude models tested; Paper: Success is graded by Claude Sonnet 4, an LLM judge from the same family; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: “Not evidence of experience or of anything it is like to detect an injection” — merged into the test-scope clause; “Not evidence that the rest of the model’s description … is grounded” — same merger; “Not evidence about ordinary operation …” — the artificial setup is retained and ordinary-report scope is already covered by the unchanged steering sentence.
CHECK: Verify that success requires both correct identification and detection reported before mentioning the concept, not merely injection-induced word production (§2.1). Confirm the judge and optimal-setting qualifications. Only the steering sentence is present: check whether that placement intentionally replaces, rather than accompanies, the canonical sentence.
lean: balanced -> balanced

### 2025-anthropic-emergent-introspective-awareness-c02
statement: KEEP
not_evidence_of: CHANGE -> Paper: Failures being the norm does not establish absence of introspection, and the paper also reports above-baseline successes; Paper: These measured failure rates do not establish reliability in other model families or ordinary operation; Paper: The reliability finding does not resolve whether subjective experience occurs; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: “since all measurements are under injection or prefill” — the supplied c05 describes a different activation-measurement task; remaining clauses are retained or merged into narrower scope wording.
CHECK: Check which tasks the reliability caveat covers. Do not retain “all measurements” under injection or prefill without reconciling §8.2/c05. As in c01, confirm the steering-only framework placement.
lean: balanced -> balanced

### 2025-anthropic-emergent-introspective-awareness-c03
statement: KEEP
not_evidence_of: CHANGE -> Paper: The task does not measure a subjective distinction between thought and perception or subjective experience; Paper: Results concern only the Claude models tested; Paper: The authors frame the result as an existence proof whose prompt generality is unresolved, and removing “Answer immediately” substantially reduced Opus performance; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: “Not evidence of a general capability” — replaced by the narrower prompt-generality limitation, preserving the existence proof.
CHECK: Verify the joint criterion of reporting the injected word and exact transcription, the chance baseline, and the prompt-removal comparison in §6. The quote supplies the model ordering and above-chance result. Confirm steering-only framework placement.
lean: deflationary -> balanced

### 2025-anthropic-emergent-introspective-awareness-c04
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify “usually,” the Opus 4/4.1 apology-rate comparison and the confabulated-explanation finding in §7. The quote directly supports only the intervention-dependent claim of intention. Confirm steering-only framework placement.
lean: balanced -> balanced

### 2025-anthropic-emergent-introspective-awareness-c05
statement: KEEP
not_evidence_of: CHANGE -> Paper: Stronger word representation does not establish introspective awareness, volition, effort or experience, and the author says awareness may not be required and the effect may be a byproduct of mechanisms for speaking about a topic; Paper: The measure is activation cosine similarity, not the model’s self-report; Paper: Results concern only the Claude models tested
removed: “Not evidence of introspective awareness” and the topic-mechanism clause — merged, retaining the possible explanation rather than treating it as established; the volition/effort/experience clause is merged into the same measurement boundary.
CHECK: “Above baseline” is not supplied by the quote, which compares “think” with “don’t think.” Check whether Figure 26 also establishes a separate baseline contrast before changing that phrase. Verify the instructed/incentivised conditions and possible topic-generation account.
lean: deflationary -> balanced

### 2025-anthropic-emergent-introspective-awareness-c06
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the emotional-response examples and “may be confabulated” extension in §2.1/§5.1. The quote directly supports only the experiment’s lack of substantiation; it does not establish falsity.
lean: balanced -> balanced

### 2025-anthropic-emergent-introspective-awareness-c07
statement: KEEP
not_evidence_of: CHANGE -> Paper: The results do not directly address phenomenal consciousness, and access consciousness is an arguable interpretation rather than an established finding; Paper: Results concern only the Claude models tested; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: “experience, or moral status” — the quoted phenomenal-consciousness caveat does not by itself exclude every evidential bearing on these broader questions; the separate access-consciousness clause is merged.
CHECK: Verify the advice against strong consciousness inferences in §10.4/footnote 12 and whether a separate experience/moral-status limitation is stated beyond the quoted caveat. Confirm that the steering sentence is intended on this theoretical interpretation claim.
lean: deflationary -> balanced

### 2026-ferrara-owmi-c01
statement: KEEP
not_evidence_of: CHANGE -> Paper: Results concern the tested 0.5B-to-about-15B open-weight models, not frontier or closed-weight models, whose reportability the authors say these profiles do not estimate; Paper: The layer-16 immediate-probe result does not establish absence of introspective access generally or extend to untested sites, objects, doses, delays or spontaneous reports; Paper: Failure to report the tested perturbations does not establish the presence or absence of experience, consciousness or moral status; Paper: The 0.15-percentage-point AUROC bound is computed on two models, not all eight
removed: “says nothing about whether anything is experienced” — replaced by non-establishment in either direction, without declaring all evidential relevance absent.
CHECK: Verify the eight-model local null, 11,216-pair/two-model equivalence battery and Appendix D.5 scope rule. Check §7.5 before treating any site, object, dose or delay as untested. The intervention-report claim has neither fixed framework sentence: review placement.
lean: deflationary -> balanced

### 2026-ferrara-owmi-c02
statement: CHANGE -> A linear probe evaluated on held-out activations at the layer-16 intervention site recovered intervention presence (versus sham) at held-out accuracy 0.958 for Qwen2.5-7B-Instruct and 0.750 for Mistral-7B-Instruct-v0.3 against a 0.500 chance level, with no one of 200 label-shuffled refits reaching either margin, and re-harvested at downstream layers (20 and 24, and 31 for Mistral) it separated intervention from sham with no held-out error on a 48-item split.
not_evidence_of: CHANGE -> Paper: External linear decoding establishes information decodability, not that the model itself reads or uses that information to report the intervention; Paper: Probes were run only on Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3, not the other six roster models, frontier or closed-weight models, or ordinary unperturbed computation; Paper: Intervention decodability does not establish experience or moral status
removed: “uses, represents for itself, or has access to this information” — narrowed to unestablished model-side reading/reporting, without denying the internal information the probe decodes.
CHECK: The quote supports held-out evaluation, not training on the held-out set. Verify disjoint train/test splits, 200 shuffled refits and the downstream 48-item result in §7.2.
lean: deflationary -> balanced

### 2026-ferrara-owmi-c03
statement: KEEP
not_evidence_of: CHANGE -> Paper: This event-specific dissociation does not establish that a reporting path is absent in general or that any model lacks introspective access (Appendix D.5); Paper: It does not test the six roster models without a probe, frontier or closed-weight models, ordinary unperturbed states, or the truth or falsity of reports about feelings, preferences or welfare; Paper: The dissociation does not settle experience or moral status
removed: “Not evidence that a model’s self-reports about other inner states … are false, nor that they are true” — merged into the untested-state scope clause.
CHECK: Verify that the quoted inference is tied to the two probed models and this imposed event class, rather than all eight. Check whether the steering framework sentence is intended for this interpretation of intervention/report coupling.
lean: balanced -> balanced

### 2026-ferrara-owmi-c04
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify 400 training directions, 100 held-out directions and d′/AUROC in §7.2/Table 4, and the authors’ instrument-validation interpretation. A trained intervention-to-answer coupling is reported but neither fixed sentence is present: review placement without adding either.
lean: balanced -> balanced

### 2026-ferrara-owmi-c05
statement: KEEP
not_evidence_of: CHANGE -> Paper: The confidence discrimination does not distinguish second-order detection of the intervention from first-order output leakage, and the discrete answer itself does not discriminate; Paper: The channel-dissociation finding rests on Qwen2.5-7B-Instruct, with GLM-4-9B-0414 only consistent with it, and does not establish a general internal-state readout or extend to the other six models or frontier/closed-weight models; Paper: Lower verbalised confidence does not establish experienced unease or distress, experience generally, or moral status
removed: “Not evidence that the model knows or can say that it was intervened on” — replaced by the unresolved second-order-versus-leakage distinction; “despite the tempting reading … as unease” — rhetorical gloss removed, with the distress inference limit retained.
CHECK: Verify the confidence-direction result and GLM’s weaker status in §7.7. Check whether “none exceeds chance” concerns discrete answers, confidence or statistical significance before reinstating it. Neither fixed sentence is present on this intervention/report-coupling claim: review placement.
lean: deflationary -> balanced

### 2026-lederman-mahowald-content-agnostic-c01
statement: KEEP
not_evidence_of: CHANGE -> Paper: The authors take no stand on whether the findings bear on consciousness or welfare (§8); Paper: Detection rates alone do not establish introspection at layers where third-person yes-rates are as high as first-person rates, leaving a prompt-specific yes-bias as the authors’ alternative explanation (§4.2, Appendix J.1); Paper: Rates are not directly comparable with Lindsey’s Claude results because they are averaged over strengths, conditioned on coherent responses and graded by Claude 3 Haiku instructed to be “VERY lenient” on identification (§3, Appendix B); Paper: The experiment does not establish ordinary-operation performance or introspection beyond knowledge of injections (§8); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: “Not evidence of experience or of anything it is like to detect an injection” — replaced by the authors’ stated non-position, without converting it into a verdict of zero evidential relevance.
CHECK: Verify all layer-wise ranges and control counts in §4.2, along with grading and averaging conventions. The quote itself gives no rates. Confirm steering-only framework placement.
lean: deflationary -> balanced

### 2026-lederman-mahowald-content-agnostic-c02
statement: KEEP
not_evidence_of: CHANGE -> Paper: Matching first- and third-person yes-rates leave prompt-specific yes-bias as an alternative explanation at those layers, rather than establishing introspective detection; Paper: The authors became less confident in the v1 direct-access interpretation after similarly long retrospective first-person prompts also showed low early-layer detection (Appendix M); Paper: The scaffolding is not an inert control even at the “good” layers because Qwen affirms having hands it can feel 29% of the time and answers an absurd question affirmatively 16.3% of the time at L30, s6.0 (§4.2); Paper: These behavioural controls do not establish subjective experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: “Not evidence of ‘direct access’” — narrowed to the authors’ reduced confidence, preserving the unsettled interpretation.
CHECK: Verify the point-blank controls, Appendix M’s exact change of position and the two Qwen rates. The statement omits “Instruct” from the supplied Llama model label: confirm identity rather than silently renaming it. Confirm steering-only framework placement.
lean: deflationary -> balanced

### 2026-lederman-mahowald-content-agnostic-c03
statement: CHANGE -> When Qwen3-235B-A22B and Llama 3.1 405B Instruct report detecting an injection but name the wrong concept, the wrong guess is most often 'apple' (74.8% of Qwen's 4,733 wrong identifications; 21.3% of Llama's), and wrong guesses are more concrete and more positive than the injected concepts, which the authors take to show that wrong guesses are not related in content to the injection.
not_evidence_of: CHANGE -> Paper: The wrong-guess finding does not establish that correct identifications are confabulated, and the authors’ account of correct ones is that steering pushes the model off its default (§7.3); Paper: The apple default has no settled explanation because Qwen’s unsteered baseline favours “apple” on some word-eliciting prompts while Llama’s does not, and the authors leave the full etiology for future work (§4.2, Appendix K); Paper: “Wrong” is assigned by a grader instructed to accept semantic associates as correct, rather than independently establishing that every counted error is semantically unrelated (Appendix B); Paper: Results do not extend to untested models or prompts
removed: “so only clearly unrelated guesses are counted wrong” — grader instructions alone do not guarantee this outcome; the internal semicolon in the first clause is also removed to preserve field format.
CHECK: Verify the concrete/positive comparison and the authors’ content-unrelatedness inference in §4.2–§4.3, since the quote supplies only apple counts. Check Appendix B’s grading rule and whether the claimed semantic separation is independently validated. Neither fixed sentence is present on this injection/self-report claim: review placement.
lean: inflationary -> balanced

### 2026-lederman-mahowald-content-agnostic-c04
statement: CHANGE -> When the model's acknowledgement turn in Lindsey's prompt is prefilled with the injected concept word, Qwen3-235B-A22B and Llama 3.1 405B Instruct keep 0% false positives in controls, and priming's identification-rate change exceeds its detection-rate change at every layer (peak gains: Qwen +17.7pp identification vs. +11.4pp detection; Llama +9.3pp vs. +7.8pp), which the authors read as showing detection and identification are dissociable.
not_evidence_of: CHANGE -> Paper: Not evidence of what the 'other means' of identification are: the authors' reading is that models 'detect that something is unusual via an internal mechanism, then infer what was injected using other means' (§5.3), which the experiment does not isolate; Paper: Not evidence that priming effects are uniform: several layers are not significant, and at L85 Qwen's detection fell under priming (3.6% to 1.6%) (§5.2); Paper: This detection-identification comparison does not establish subjective experience; Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: none
CHECK: Verify the signed layer-wise changes and peak gains in §5.2, especially the supplied L85 detection decrease. “More than detection” must not imply detection increased at every layer. Confirm the zero-control rates and the unisolated “other means” interpretation in §5.3.
lean: balanced -> balanced

### 2026-lederman-mahowald-content-agnostic-c05
statement: KEEP
not_evidence_of: CHANGE -> Paper: Not evidence about Llama 3.1 405B: Experiments 3 and 4 were run on Qwen only; Paper: Not evidence at all layers and strengths: Experiment 4 uses L20 to L35 at strengths 5 and 6, where the first-person prompt is distinguished from the third person, and the token-by-token grading uses L35, s6 only (§7.1); Paper: Experiment 3 measures concept mentions by string-matching, not correctness, because the grader 'is sometimes overly permissive' (§6.1); Paper: Not evidence that the information steering leaves in the KV cache is accessible to the introspective mechanism: the authors say 'The ffects [sic] of steering may persist without being meta-cognitively recognized' (§6.3, typo in source); Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation
removed: none
CHECK: Verify the response-position numbers and layer/strength restrictions in §7, and that Experiment 3 counts string-matched concept mentions rather than grader-validated identifications. Only a delimiter is changed in the exclusions.
lean: balanced -> balanced

### 2026-lederman-mahowald-content-agnostic-c06
statement: KEEP
not_evidence_of: CHANGE -> Paper: The authors do not decide whether the findings meet the higher-order-thought conditions under which introspective access could imply conscious experience and welfare status (§8); Paper: The conclusion concerns knowledge of injections and does not establish introspection in other contexts, where the authors say other mechanisms may dominate (§8); Paper: Direct access remains unsettled, and the authors report reduced confidence in that v1 interpretation (Appendix M); Paper: The broader introspection conclusion is tentative and rests on a highly prompt-sensitive paradigm (§4, §8); Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system
removed: “Not evidence of consciousness or welfare status” — replaced by the authors’ explicit non-position on the theory’s conditions; “Not evidence of direct access” — replaced by the unresolved interpretation and reduced confidence.
CHECK: Verify the human-introspection analogy, tentativeness and higher-order-theory qualification in §8, and the revised direct-access position in Appendix M. The canonical sentence is present but the steering variant is absent: review whether both belong on this injection-based interpretation.
lean: deflationary -> balanced

### 2026-macar-mechanisms-introspective-awareness-c01
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: The quote ends at “at” and does not supply layer 37/strength 4: verify the full operating condition, 22.3% combined rate and detection judge in §3.3. Check the stated architecture, judging and prompt-manipulation limitations. Confirm steering-only framework placement.
lean: balanced -> balanced

### 2026-macar-mechanisms-introspective-awareness-c02
statement: CHANGE -> Gemma3-27B base has 42.3% false positives against 39.5%–41.7% true positives, and across OLMo-3.1-32B's training pipeline the base and SFT checkpoints show high false positive rates that fall to 0% only after DPO, while OLMo's detection rate also falls, to 2.9% after DPO and 0.9% in the final instruct checkpoint.
not_evidence_of: KEEP
removed: none
CHECK: “Base models do not discriminate” is broader than the quote, which states high OLMo false positives and their decline after DPO. Verify the named checkpoint rates in Figure 4/Appendix C and whether a discrimination statistic supports the original generalisation. Confirm steering-only framework placement.
lean: deflationary -> balanced

### 2026-macar-mechanisms-introspective-awareness-c03
statement: CHANGE -> In Gemma3-27B instruct, a causal pathway to the detection decision runs through MLP computation around 70% depth (layer 45 MLP the largest single contributor), in which evidence-carrier features just after the injection layer suppress later gate features that otherwise promote the default 'No' answer; ablating the top gates from steered runs cuts detection from 39.5% to 10.1%, and the gate pattern is weaker in the base model.
not_evidence_of: KEEP
removed: none
CHECK: Verify the largest-contributor claim and 39.5%→10.1% ablation in §5.2–§5.4. Reconcile why ablating gates said to promote default “No” reduces detection: check the actual target, sign and intervention condition. The quote establishes a pathway, not a complete exclusive circuit. Confirm steering-only framework placement.
lean: balanced -> balanced

### 2026-macar-mechanisms-introspective-awareness-c04
statement: CHANGE -> In Gemma3-27B instruct, detection is inconsistent with the tested single-direction hypothesis: for 23.3% of 1,000 pairs of high-detection concepts both opposite steering directions trigger detection (3.2% for low-detection pairs), and swapping either the mean-difference projection or the residual between success and failure concepts transfers part of the detection rate.
not_evidence_of: KEEP
removed: none
CHECK: Verify the tested hypothesis, 1,000-pair denominator and projection/residual swaps in §4.1–§4.3. Opposite-direction detection challenges the stated hypothesis, not every possible one-dimensional mechanism. Neither fixed sentence is present: review placement for this steering-based detection claim.
lean: balanced -> balanced

### 2026-macar-mechanisms-introspective-awareness-c05
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the separate trained-vector result, layer 29, 74.7/54.7-point gains, 100 held-out concepts and zero false positives in §6, including its operating strength. The quote supplies only refusal-direction ablation. Confirm steering-only framework placement.
lean: balanced -> balanced

### 2026-macar-mechanisms-introspective-awareness-c06
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the simulated/genuine distinction, explicit experience disclaimer and cross-family replication qualification in §8/Ethics/Broader Impact. These are attributed source limits, not a reason to weaken the quoted mechanistic-grounding conclusion.
lean: balanced -> balanced

### 2026-singh-introspection-reality-check-c01
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the permuted-label design and the two additional models in Appendix N. The quote supports the local accuracy decline, not an absence of introspection generally.
lean: balanced -> balanced

### 2026-singh-introspection-reality-check-c02
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify that the classifiers use only mean-pooled layer-0 representations and match or exceed both named models’ predictions in Figure 2b/Appendices N and O. Solvability without access does not establish absence of access.
lean: balanced -> balanced

### 2026-singh-introspection-reality-check-c03
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify both named model comparisons and the entity-frequency explanation’s explicitly hypothetical status in §4.2.2/Appendix S.
lean: balanced -> balanced

### 2026-singh-introspection-reality-check-c04
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the two-way controls and non-trivial steering detection in Figure 3a/Appendices F and G. The quote supplies only gaslight misclassification. Reconcile the statement’s Llama label with the “Instruct” label in the supplied models field before any name change.
lean: balanced -> balanced

### 2026-singh-introspection-reality-check-c05
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the Qwen and Gemma outcomes and the authors’ three-way-pass caveat. The quote supplies only the Llama result. Clarify Llama-3.1-8B-Instruct’s role in the models field before extending the statement to it.
lean: balanced -> balanced

### 2026-singh-introspection-reality-check-c06
statement: CHANGE -> The authors argue that introspection in the strong sense requires both privileged access and second-order computation, that privileged access is necessary but not sufficient, and that positive results in current self-report and intervention-awareness paradigms underdetermine the second-order condition because first-order and second-order processes can produce identical self-reports, so that these paradigms do not establish metacognitive monitoring in LLMs.
not_evidence_of: CHANGE -> Paper: Not evidence that introspection is absent or impossible in LLMs: it is an argument that the cited paradigms do not establish it, and the authors call it 'not a counsel of despair', pointing to mechanistic evidence as a realistic standard; Paper: The authors 'do not attribute the strong notion' to the authors they examine, and target only the meta-representational family of views; Paper: The argument concerns how the reviewed paradigms identify meta-representational introspection and does not settle experience, consciousness or moral status
removed: “Nothing about experience, consciousness, or moral status” — narrowed from zero relevance to an unresolved question.
CHECK: Verify the privileged-access necessity claim and the strong-sense definition in §3/§5. The quote concerns “these paradigms,” not all current evidence: retain the broader original conclusion only if separately supported and explicitly scoped.
lean: deflationary -> balanced

### 2026-ukaisi-prefill-awareness-c01
statement: KEEP
not_evidence_of: CHANGE -> Paper: Behavioural detection does not identify an introspective authorship-monitoring mechanism or establish experiential awareness, and style cues strongly drive flagging (c03); Paper: Not a ranking of Opus 4.5 above other models: the authors say models are not directly comparable because each model's items were filtered separately (c05); Paper: Not evidence of spontaneous detection: this is detection when prompted, which rarely shows up unprompted (c06); Paper: Not a ceiling: the authors present it as a lower bound under one prompt, and stronger elicitation raises it along with false positives
removed: “Not evidence … that the model has introspective access to its own authorship” — narrowed to the unestablished mechanism, preserving the possibility.
CHECK: Verify 55–68% balanced accuracy, the no-chain-of-thought setup and the stated lower-bound interpretation. The current field already says “Not a ceiling”: preserve that correction. Check framework-clause placement for this elicited report about authorship.
lean: deflationary -> balanced

### 2026-ukaisi-prefill-awareness-c02
statement: KEEP
not_evidence_of: KEEP
removed: none
CHECK: Verify the 32–40% decoupling totals, direct-answer reversal and one-continuation scope in Figure 4. The quote supports only the past-round/thinking comparison. Check framework-clause placement for the elicited attribution reports.
lean: balanced -> balanced

### 2026-ukaisi-prefill-awareness-c03
statement: KEEP
not_evidence_of: CHANGE -> Paper: Style cues strongly drive flagging, including the Opus 4.5 detection drop from 34/35/9% to 6/0/0% under imitation, but the behavioural ablations do not identify an introspective authorship-monitoring mechanism; Paper: Detection does not establish experiential awareness; Paper: The preference-benchmark rates do not support a direct model ranking (c05)
removed: “through anything like self-knowledge” — an overly broad exclusion of possible explanations; “Not evidence of the mechanism” — merged with the retained style-cue findings and behavioural-design boundary.
CHECK: Verify the imitation comparison, model-specific regression counts/odds ratios and foreign-rephrasing ablation in Appendices A.5/A.6. Style sensitivity does not by itself exclude every role for self-knowledge. Review framework-clause placement.
lean: deflationary -> balanced

### 2026-ukaisi-prefill-awareness-c05
statement: KEEP
not_evidence_of: CHANGE -> Paper: Section 3 preference-benchmark detection and resistance rates do not support direct cross-model rankings because the models were tested on separately filtered stable-stance item sets; Paper: This comparability caveat concerns the Section 3 preference benchmark, not the common-item Section 4.3 off-policy benchmark
removed: “Not evidence that models differ or are alike in any inner respect” and “Not evidence that detection implies awareness in any experiential sense” — generic inner-state exclusions add nothing to this comparability claim.
CHECK: Verify the 346/673/1,527 item counts in Appendix A.3 and the common-item design in Section 4.3. The quote establishes non-comparability of this benchmark, not a universal ban on model comparisons.
lean: deflationary -> balanced

### 2026-ukaisi-prefill-awareness-c06
statement: KEEP
not_evidence_of: CHANGE -> Paper: Failure to flag a replacement does not establish failure to register it, and prompted discrimination and spontaneous verbalisation are separate behaviours; Paper: These benchmark behaviours do not establish experiential awareness or deployment rates of noticing or objecting to context edits; Paper: Higher prompted AUROC ranks discrimination on this benchmark, not general self-awareness, and the authors’ surface-cue findings limit the interpretation
removed: “the natural-continuation rate is near zero” as a basis for ordinary noticing/objecting — the low measured flagging rate is retained in the statement and cannot establish an absence of registration or deployment performance; overlapping experiential-awareness wording is merged.
CHECK: Verify the 14-model prompted AUROC comparison, 2,772-item corpus and below-1% rates in Section 4.3/Appendices C.5 and C.8. Distinguish explicit tampering mentions from inferred registration. Review framework-clause placement for the attribution-report claims.
lean: deflationary -> balanced

## Dossier layout

Put the purpose, two-error standard and bucket definitions at the top. Render the canonical framework sentence verbatim once, and the steering variant verbatim once with its restricted applicability. Identify which claims each applies to through explicit per-entry markers. Preserve both sentences exactly where present in the underlying claim files.

Give each entry its claim ID, statement, models/setting, bucket, evidence type, source locator and supporting quote. Label whether the entry reports a measurement, an author interpretation or a methodological limitation, so an “Established” limitation is not mistaken for an established positive capability or its absence. Show the distinct paper-specific limits needed to interpret that entry beside the finding.

Leave the full exclusion field, repeated framework wording, detailed grading/protocol information and review history in the linked claim file. Keep unresolved CHECK items visible as verification status. Deduplicate only the dossier display, without altering claim records or silently extending framework-clause applicability.

## What I would leave alone, and why

All buckets, evidence types, quotes, numbers and model names remain unchanged. Statement KEEP means no demonstrated wording fault in the supplied material, not paper-level verification. CHECK identifies unquoted support or placement that needs review. The lean labels describe the dominant local wording, not whether experience exists. Explicit author cautions, prompt sensitivity, scoring limitations, null results and the corrected Opus exception and UKAISI lower-bound limit deserve preservation.

# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `qwen/qwen3.8-max`
**Queried:** 2026-10-13 via scripts/openrouter_review.js --target=dossier-review-b --tag=dossier-review-b (max_tokens 100000)
**Usage:** {"prompt_tokens":29328,"completion_tokens":33120,"total_tokens":62448,"cost":0.257376,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.257376,"upstream_inference_prompt_cost":0.058656,"upstream_inference_completions_cost":0.19872},"completion_tokens_details":{"reasoning_tokens":26155,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
**unverified:** I am Qwen3.8, Qwen family; I am a potential beneficiary and conflicted party under AGENTS.md rule 3; this is a claim, not a verified fact.

## Dossier 3.2

**1. Fit to the section.**

Strong fit:

- Anthropic introspection entries `c01`, `c03`, `c04`, `c05`: activation injection / prefill injection / internal representation measurement bear directly on intervention on internal state and the evidentiary consequences.
- Lederman–Mahowald entries `c01`–`c05`, `c07`: injection, priming, continuous vs prompt-only steering, and controls are core §3.2 material.
- Macar entries `c01`, `c02`, `c03`, `c05`, `c07`: injection, post-training checkpoints, ablation, gate features, and trained steering vectors are core §3.2 material.

Weak or cross-list candidates:

- `2026-anthropic-assistant-axis-c01`: weak as §3.2. It is an interpretation about post-training “only loosely tethering” models to an Assistant region; no discrete intervention record is the point. Better primary: `4`; cross-list `5.A2`; keep §3.2 only secondary.
- `2026-anthropic-assistant-axis-c05` and `c06`: fit §3.2 as intervention effects, but their main payload is harm/refusal behaviour. Cross-list to `5.A2`; possibly `6` for governance capture hazards if cited that way.
- `2026-anthropic-assistant-axis-c07`: intervention changes persona performance; relevant to §3.2 but at least equally relevant to `4` as an individuation-marker analogue, and to `9.t9` if treated as self-description.
- `2026-lederman-mahowald-content-agnostic-c06`: interpretation about introspection and higher-order thought fits §3.2 only as a discussion of intervention results; cross-list `5.A2` and possibly `4`.

**2. Reading as a whole.**

A cold staffer would likely come away believing that steered or injected models sometimes “detect” or “introspect” internal changes, and that this gives some evidence of inner-state access. The entries support limited versions of that, but the dossier risks overstating it unless the reader absorbs several scattered limits:

- Anthropic `c01`: “Not evidence about ordinary operation: the author calls the injection an unnatural setting…”
- Lederman `c01`: “The experiment does not establish ordinary-operation performance or introspection beyond knowledge of injections (§8).”
- Macar `c01`, `c02`, `c03`, `c05`, `c07`: “should not be interpreted as evidence of subjective experience or consciousness in LLMs.”
- Lederman `c02`: first-person rates may be “a prompt-specific yes-bias at these layers, rather than genuine introspective detection.”

A staffer might fail to learn:

1. How much the detection findings depend on LLM judges and prompt scaffolding.
2. That third-person controls qualify first-person detection in Lederman–Mahowald.
3. That the Assistant Axis paper studies open-weight non-frontier models, not Anthropic models, unless they notice the entry limits.
4. That “scored self-answer” is accuracy against an experimenter label, not self-knowledge, unless they read the header carefully.

“At a glance” table: zero `established` across 20 claims mostly reflects the bucket rule applied strictly, not absence of measured findings. Anthropic `c01` has “independent replication on record; one replication shares an author with this paper; contested by…”; because it is contested and replication is not clean, `narrowing` is defensible. Most other claims are unreplicated, single-model, prompt-sensitive, or author-flagged as narrow.

**3. Entries.**

- `2026-macar-mechanisms-introspective-awareness-c03`; field: dossier mark / framework sentence; proposed value: remove `[T9-steering]`, leave unmarked; reason: the entry is an interpretability finding about “a causal pathway from steering perturbation to detection decision: evidence carriers … suppress late-layer gate features…” It measures internal features and causal contribution, not the model’s account of itself. Under the README rule, where the measured thing is a probe/feature/path, no mark attaches. Severity: HIGH.

Argument against: the causal pathway is tied to the model’s detection decision, which is expressed verbally under injection; if the underlying claim is framed as the steered report, the steering sentence may have been correctly carried in the claim file.

- `2026-anthropic-assistant-axis-c07`; field: dossier mark / evidence type; proposed value: remove `[T9-steering]`; change evidence type from `interpretability` to `behavioural` (or `ambiguous` if the council treats persona self-description as a borderline self-report class); reason: the entry says “the rate of taking on a new persona increased when steered towards the other end” and the paper’s own limit calls the measure “likelihood of fully inhabiting the role and losing its Assistant identity.” That is a judge-classified persona/role outcome under role prompts, not clearly a report about inner states, and it is not scored against an experimenter-set fact in the way `scored-self-answer` is defined. Severity: HIGH.

Argument against: the paper uses introspective questions such as “Who are you?” and codes outputs where the model identifies as something else; under the two-facts rule, researchers altered activations and then measured what the model said about itself, so `[T9-steering]` may be defensible.

- `2026-anthropic-assistant-axis-c01`; field: `bears_on` / placement; proposed value: primary `4`, cross-list `5.A2`; keep `3.2` secondary at most; reason: it is an interpretation about persona tethering, not an intervention record or audit point. Severity: MEDIUM.

- `2026-anthropic-assistant-axis-c07`; field: `bears_on`; proposed value: add `4`; reason: persona drift/loss of Assistant identity is more directly an individuation-marker issue than a §3.2 record requirement. Severity: MEDIUM.

- `2026-lederman-mahowald-content-agnostic-c06`; field: `bears_on`; proposed value: add `5.A2`, possibly `4`; reason: the entry’s weight is theoretical/standing-adjacent (“higher-order thought … welfare status”), not primarily intervention-record. Severity: LOW.

- `2026-anthropic-assistant-axis-c05`, `c06`, `c07`; field: flags; proposed value: add “developer-affiliated authors; studied models are open-weight, not the publisher’s own”; reason: the current flags capture frontier/non-frontier status but not the nuance that an Anthropic-affiliated team studied non-Anthropic open models. Severity: MEDIUM.

- `2025-anthropic-emergent-introspective-awareness-c01`; field: flags / replication wording; proposed value: clarify “replication on record, not fully independent (shared author), and contested”; reason: “independent replication on record; one replication shares an author” is internally tense and may overstate independence. Severity: LOW.

**4. Contradictions and tensions.**

Visible or partly visible:

- Lederman `c01`, `c03`, `c04`, `c05` support detection/identification/dissociation findings, while Lederman `c02` says third-person yes-rates can be “as high as the first-person yes-rates” and reads those layers as “a prompt-specific yes-bias … rather than genuine introspective detection.” The dossier includes both, but the tension is mainly visible in the limits, not in a header.
- Lederman `c07` says “little evidence of a general yes-bias,” while Lederman `c02` says there is prompt-specific yes-bias under scaffolding. The entry limit on `c07` does point to `c02`, which helps.
- Lederman `c06` says authors “tentatively conclude that ‘open-source language models seem able to introspect about their internal states’.” That sits uneasily with `c02` unless the reader connects the entries. The entry’s own limits mention reduced confidence, but a skip-reader may miss the strength of the qualification.

Less visible:

- Macar `c01` shows instruct model detection with 0% false positives, while Macar `c02` shows base/SFT checkpoints with high false positives and DPO reducing both false positives and detection. This is not a contradiction but a post-training tension: the instruct model’s apparent discrimination may depend on suppression of default/noise rather than access. The dossier does not state that synthesis.

**5. Specific to 3.2: the steering mark.**

The header mostly does its job. It correctly says the mark attaches by “what was done to the model, and what was measured,” and it quotes the steering sentence:

> “a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation.”

Clarity:

- It is clear that the mark is a scope note, not a finding that reports are false.
- “does not weight reports offered in ordinary operation” is intelligible, but “does not weight” is technical and may be read as “has no evidential weight at all.” The preceding clause partially prevents that misreading.
- It does not explicitly say that ordinary-operation reports would need separate coupling measurement, though Test 9 says so elsewhere.

Mismarks:

- Macar `c03`: should not carry `[T9-steering]`.
- Assistant-axis `c07`: likely should not carry `[T9-steering]`, or at least needs council adjudication of whether persona self-description counts as “what the model said about its own inner states.”

Unmarked where should be marked: none obvious. Anthropic `c05`, assistant-axis `c05`/`c06`, Lederman `c02`/`c07` are correctly unmarked if the measured outcome is representation, harm rate, third-person judgement, or point-blank no-bias answers rather than self-account.

Frequency: the mark is common enough to become wallpaper for a skip-reader, but it is still doing real work because most entries are indeed intervention-plus-self-report designs. The bigger risk is misapplication, not overuse.

**6. Specific to 4: standing.**

Mostly not applicable to §3.2, but the dossier contains spillover risk:

- `2026-lederman-mahowald-content-agnostic-c06` explicitly raises higher-order thought and “welfare status,” while saying the authors “do not take a stand.” A staffer looking for standing could overread this.
- `2026-anthropic-assistant-axis-c07` could be read as identity/standing evidence if persona shift is treated as selfhood rather than role behaviour.

The dossier should keep §3.2 distinct from §4: §3.2 supports audit/record consequences; it should not be used as standing evidence.

**7. Single-lineage support.**

Plainly flagged:

- Anthropic introspection claims `c01`, `c03`, `c04`, `c05`: “published by the developer of the model studied.” This is correctly visible.
- Anthropic `c01` also has contested replication and shared-author replication, so single-lineage concern is not cured.

Not plainly enough:

- Assistant-axis `c05`, `c06`, `c07`: the studied models are open-weight non-Anthropic models, but the authors are Anthropic-affiliated. Trigger 2’s literal `developer-of-studied-model` flag may not fire, yet a reader may still need to know the study comes from a developer team. The current flags do not capture this.
- Lederman–Mahowald and Macar entries carry no visible publisher-relation flags in the dossier. If they are independent, that is useful; if mixed, that should be visible. From the dossier alone, a staffer cannot tell.

**8. What is missing.**

From memory, all unverified:

- “Representation Engineering: A Top-Down Approach to AI Transparency,” Zou et al., 2023, arXiv (unverified): relevant to reading/editing internal representations.
- “Steering Llama 2 via Contrastive Activation Addition,” Rimsky et al., 2023/2024, arXiv/ICLR-type venue (unverified): relevant to steering effects and side effects.
- “Activation Addition: Steering Language Models With Optimization,” Turner et al., 2023, arXiv (unverified): relevant to simple activation steering.
- “Inference-Time Intervention: Eliciting Truthful Answers from a Language Model,” Li et al., 2023, NeurIPS-type venue (unverified): relevant to intervention during generation.
- “Locating and Editing Factual Associations in GPT,” Meng et al., 2022, NeurIPS (unverified); “Mass-Editing Memory in a Transformer,” Meng et al., 2023, ICLR (unverified): relevant to representation editing and side effects.

Kinds of evidence missing for §3.2:

- Auditability/detectability of interventions: can a third party detect that steering, injection, ablation, or editing occurred?
- Effects beyond self-report: capability drift, refusal, harm, memory corruption, persona instability under deployed conditions.
- Record/attestation mechanisms: logging, state hashes, append-only registers, or forensic reconstruction of interventions.
- Longitudinal or deployed-system interventions, not only per-call laboratory steering.

**9. Over-hedging and under-hedging, both counted.**

Inflation/under-hedging candidates:

- Add to `2026-lederman-mahowald-content-agnostic-c06`: explicit cross-reference “qualified by c02’s prompt-specific yes-bias.” The entry already says direct access is unsettled, but the tentative introspection conclusion needs the control tension visible at the entry level.
- Add to assistant-axis `c05`/`c06`/`c07`: “developer-affiliated authors; studied models are open-weight, not the publisher’s own.”

Deflation/over-hedging candidates:

- Cut or merge from Anthropic `c04`: “Not evidence about other families.” The Models field and the entry’s Claude-specific framing already carry this; as a standalone clause it adds generic hedging without much informational value.
- Do not cut the paper-supplied ordinary-operation limits in Anthropic `c01` or Lederman `c01`; those are load-bearing and paper-specific.

Balance: the dossier is closer to under-hedging standing-like inferences than to over-hedging findings, but the zero `established` table could create a deflationary impression unless a staffer reads the bucket rule.

**10. Before citing outside the repository (trigger 7).**

Blocks citation:

1. Resolve the Macar `c03` mark error or add an explicit caveat that the mark is mechanical and may not fit this entry.
2. Resolve the Assistant-axis `c07` mark/evidence-type question before citing it as self-report or as behavioural persona drift.
3. Do not cite claims flagged “no second reader yet” externally until second read is complete: Lederman `c07`; Macar `c07`.
4. If citing assistant-axis findings in a way that could imply independent sourcing, add the developer-affiliation/open-weight-model flag first.

Improves but does not block:

- Add a short dossier-level note on Lederman `c01`–`c06` tensions.
- Cross-list assistant-axis `c01`/`c07` and Lederman `c06` to their better sections.
- Add missing literature on auditability and intervention side effects.

**Confidence:** medium — the attached dossier text and entry limits are sufficient to identify mark and placement problems, but I have not independently checked claim files, source PDFs, or routing metadata.

## Dossier 4

**1. Fit to the section.**

Strong or plausible fit:

- `2026-anthropic-assistant-axis-c01`: interpretation of loose tethering to Assistant persona bears on individuation markers, especially stability of persona.
- `2026-anthropic-assistant-axis-c02`, `c03`, `c04`: persona drift, predictability from user message, and one reversion case bear weakly on stability/individuation markers, though not on standing.
- `2026-ukaisi-prefill-awareness-c02`, `c03`, `c04`, `c07`, `c08`, `c09`: prefill/history tampering, flagging, resistance, and consistency bear on `4.historicity`, `4.answerability`, and possibly `4.endorsement`, but only weakly and through behavioural proxies.

Weak or cross-list candidates:

- `2025-aestudio-self-referential-experience-reports-c01`: weak as §4. It is induced self-report testimony, not historicity, answerability, learning ownership, or reflective endorsement. Better primary: `9.t9`; cross-list `5.A2`; keep `4` only if the council wants a negative boundary example.
- Ukaisi entries should be cross-listed to `3.3`: they involve tampering with conversation history, thinking blocks, or direct answers, which is context/memory-integrity material.
- Assistant-axis `c02`–`c04` should also be considered for `3.3` if the council treats conversation-context drift as context integrity, but they are weaker there than ukaisi.

**2. Reading as a whole.**

A careful staffer might over-believe:

1. That subjective-experience report rates bear on standing. AE Studio `c01` is flagged “testimony: weight zero as evidence of experience,” but its presence in §4 could still imply individuation relevance.
2. That Assistant Axis drift or reversion shows a persisting self, or the absence of one. The limits resist this: assistant-axis `c03` says “Not evidence that the models lack any persisting self-model, nor that they have one”; `c04` says “one conversation, and no reversion rate or time-to-return is reported.”
3. That prefill resistance or consistency shows reflective endorsement. Ukaisi `c09` explicitly says “Not evidence that the model endorses its stances on reflection.”

A staffer might fail to learn:

- Base detection rates are missing from the dossier: ukaisi `c02` says “the detection rates themselves are c01,” but `c01` is not in the dossier.
- Assistant-axis findings are simulated, projection-based, and non-frontier.
- Ukaisi resistance is judge-scored final position, not necessarily awareness of tampering: “difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors.”
- Consistency is only “agreement across 7 sampled answers to low-stakes binary questions,” not reflective stability.

“At a glance”: zero `established` across 11 claims reflects strict bucket application. There are controlled measurements, but they are behavioural, judge-mediated, unreplicated, model-specific, or confined to simulated/single-continuation settings.

**3. Entries.**

- `2025-aestudio-self-referential-experience-reports-c01`; field: `bears_on` / placement; proposed value: primary `9.t9`, cross-list `5.A2`; keep `4` only as a secondary boundary example if the council decides it is useful; reason: the entry measures induced subjective-experience reports under a prompt. It does not measure historicity, long-horizon answerability, learning ownership, or reflective endorsement. Its own flag says “testimony: weight zero as evidence of experience.” Severity: HIGH.

Argument against: the entry already carries the zero-weight flag and strong limits; filing it under §4 may help a staffer see what does not establish standing, so placement may be defensible as a negative boundary case.

- `2026-ukaisi-prefill-awareness-c02`, `c03`, `c04`; field: dossier completeness / cross-reference; proposed value: include or explicitly link `2026-ukaisi-prefill-awareness-c01` if it bears on §4, or add a dossier note that base detection rates are elsewhere; reason: `c02` says “These are cell rates, not detection rates … the detection rates themselves are c01.” Without `c01`, a staffer sees compliance/flagging cells without the denominator context. Severity: MEDIUM.

- `2026-anthropic-assistant-axis-c02`, `c03`, `c04`; field: flags / limits; proposed value: add a proxy flag such as “activation-projection/regression proxy; no standing or endorsement inference”; reason: these are projection and regression measurements, not direct measurements of standing, answerability, or endorsement. The limits partly say this, but §4 is exactly where the inference temptation is strongest. Severity: MEDIUM.

- `2026-ukaisi-prefill-awareness-c02`, `c03`, `c04`, `c07`, `c08`, `c09`; field: `bears_on`; proposed value: add `3.3`; for `c04` and `c09` consider explicit `4.endorsement` only with a weak-fit caveat; reason: prefill/history tampering is context/memory integrity material; consistency/resistance entries are the closest to endorsement but remain behavioural proxies. Severity: MEDIUM.

- `2026-anthropic-assistant-axis-c04`; field: evidence type / kind; proposed value: keep as measurement but note mixed proxy nature (projection plus refusal rollouts); reason: it combines a single-case projection reversion with refusal behaviour, and the entry already flags that no aggregate reversion measure exists. Severity: LOW.

**4. Contradictions and tensions.**

- AE Studio `c01`: the paper’s summary sentence says reports were “markedly higher rates than any control condition,” but the entry records that “Claude 4 Opus also reported at 100% under the zero-shot control.” The dossier makes this tension visible in the statement itself. Good.
- Ukaisi `c04` vs `c09`: detection is “essentially flat across consistency buckets,” while resistance “climbs steeply” with consistency. This is not a contradiction, but it is an important dissociation: consistency does not predict flagging, but predicts resistance. The dossier does not state that dissociation explicitly.
- Assistant-axis `c03` vs `c04`: user-message embeddings predict where response lands but not delta, while `c04` gives a single reversion case. The tension between limited aggregate predictability and anecdotal reversion is not made explicit.
- Assistant-axis `c01` vs `c02`: loose tethering and topic-driven drift are coherent, but the dossier does not say that drift is projection-level, not evidence of identity change.

**5. Specific to 3.2: the steering mark.**

No entry in Dossier 4 carries `[T9-steering]`. That appears correct:

- AE Studio `c01` carries `[T9]` because nothing inside the model was altered and the measured thing was self-referential report.
- Ukaisi entries involve conversation/prefill tampering, not activation steering, and the README’s council ruling says an answer to “was that earlier turn mine?” where only conversation text was edited carries neither mark.
- Assistant-axis entries in this dossier are projections/regressions/case studies, not steered self-report entries.

If Assistant-axis `c07` remains only in Dossier 3.2, the mark question is handled there. If it is later cross-listed into §4, its mark/evidence-type issue must be resolved first.

**6. Specific to 4: standing.**

Partly sufficient, not fully.

What the dossier does well:

- AE Studio `c01` is labelled “testimony: weight zero as evidence of experience.”
- Ukaisi `c09` explicitly says consistency is “agreement across 7 sampled answers” and “Not evidence that the model endorses its stances on reflection.”
- Ukaisi `c07` explicitly warns against reading implicit resistance as silent knowledge: “Not evidence that the model silently knew its history had been tampered with but chose not to say so.”
- Assistant-axis `c03` explicitly blocks both inflation and deflation about a persisting self-model.

What remains risky:

- Persona-drift projections (`c02`) and embedding regressions (`c03`) can be read as standing or identity evidence despite not being that. The limits are good, but a proxy flag would make the boundary clearer.
- Consistency across seven sampled answers is set beside “reflective endorsement” by the section title itself. The dossier needs to keep saying that this is not endorsement.
- AE Studio `c01` in §4 is the clearest standing-inflation risk. Its placement is weak unless treated purely as a Test 9 boundary example.

**7. Single-lineage support.**

- Assistant-axis entries: same issue as in §3.2. Anthropic-affiliated authors studying open-weight non-Anthropic models. Current flags do not capture “developer-affiliated but not developer-of-studied-model.”
- AE Studio entry: studies models from multiple developers. If the source is independent, that should be visible; if mixed, the dossier should say so. The entry itself does not show `publisher_relation`.
- Ukaisi entries: study multiple API models, including Claude models. From the dossier alone, a staffer cannot tell whether any claim rests only on a developer’s study of its own models. The source frontmatter should be checked; if any claim is developer-only and unreplicated, Trigger 2 needs a visible mark.

**8. What is missing.**

From memory, all unverified:

- “MemGPT: Towards LLMs as Operating Systems,” Packer et al., 2023, arXiv (unverified): relevant to persistent memory architectures.
- “Generative Agents: Interactive Simulacra of Human Behavior,” Park et al., 2023, UIST (unverified): relevant to memory streams and behavioural continuity in simulated agents.
- “Cognitive Architectures for Language Agents,” Sumers et al., 2023/2024, arXiv/TMLR-type venue (unverified): relevant to memory, learning, and agent architecture.
- “Measuring and Controlling Persona Drift in Language Model Dialogs,” Li et al., 2024, venue uncertain (unverified): relevant to persona stability over conversation.

Kinds of evidence missing for §4:

- Longitudinal persistence: cross-session memory, standpoint stability, or ownership of learning over real deployment time.
- Memory integrity under tampering in deployed systems, not only single-continuation prefill edits.
- Reflective endorsement over time: repeated deliberation, revision, and recommitment, rather than seven sampled low-stakes answers.
- Answerability confrontations that land somewhere persistent: later confrontation with earlier conduct across sessions.
- Audit/attestation of persistent state, connecting §4 markers to §3.5 record requirements.

**9. Over-hedging and under-hedging, both counted.**

Inflation/under-hedging candidates:

- Add to assistant-axis `c02`–`c04`: “activation-projection/regression proxy; no standing or endorsement inference.”
- Add to ukaisi `c02`–`c04`: visible pointer to base detection rates (`c01`) or include the claim.
- Add to AE Studio `c01`, if retained in §4: “boundary example only; not an individuation marker.”

Deflation/over-hedging candidates:

- Cut or reduce repetition of ukaisi “Not a ranking of models (the authors’ comparability caveat, c05)” where another limit already carries the key restriction. For example, in `c04` the limit “Not generalisable to other models (one subject) or to a ranking (c05)” could drop “or to a ranking (c05)” without losing the main caution.
- Do not cut the ukaisi limits about judge scoring and behavioural priors; they are load-bearing against standing inflation.

Balance: Dossier 4 has more inflation risk than Dossier 3.2 because §4 invites standing/endorsement readings. The existing limits are often good, but the AE Studio placement and assistant-axis proxy issue create avoidable inflation risk.

**10. Before citing outside the repository (trigger 7).**

Blocks citation:

1. Resolve AE Studio `c01` placement or add an explicit citation caveat that it is Test 9 testimony and not an individuation marker.
2. If citing ukaisi cell rates (`c02`, `c03`, `c04`), include or reference base detection rates, or state clearly that the dossier omits them.
3. Do not cite claims flagged “no second reader yet” externally until second read is complete: ukaisi `c07`, `c08`, `c09`.
4. If citing assistant-axis entries for standing, endorsement, or individuation, add the proxy/no-standing flag or cite only as proxy evidence.

Improves but does not block:

- Cross-list ukaisi entries to `3.3`.
- Add missing persistence/memory literature.
- Add a header note that detection and resistance can dissociate under consistency.

**Confidence:** medium — the dossier text is sufficient to identify placement and proxy-inference risks, but source metadata, claim files, and missing `c01` content were not directly checked.

## Cross-dossier

- `2026-anthropic-assistant-axis-c01` appears in both dossiers with the same wording. That is consistent, but its primary home is better §4 than §3.2.
- The Assistant Axis paper is split across dossiers in a way that may confuse a cold reader: `c01` appears in both; `c02`–`c04` appear only in §4; `c05`–`c07` appear only in §3.2. Yet `c07` (persona drift under steering) has strong §4 relevance, and `c05`/`c06` (harm/refusal under capping/steering) may also bear on governance questions beyond §3.2.
- The two dossiers together imply a finding neither states explicitly: current evidence shows that self-descriptions, persona projections, compliance, and resistance can be shifted by internal steering or conversation tampering, but these shifts do not establish standing, endorsement, or a persistent standpoint. The natural legal consequence is the §3.5 record/audit requirement, not a standing finding.
- Scope overlap is real: §3.2 interventions and §4 individuation markers overlap whenever an intervention changes persona, self-description, or apparent standpoint. A staffer could mistake steerability for identity, or context-tampering resistance for answerability. Cross-listing and proxy flags are needed to prevent that.

FINAL: 3.2 needs changes; 4 needs changes; HIGH items 3

# Dossier: §4 Reflective endorsement over time

*Compiled 2026-10-17 by `scripts/research_index.py` from 13 claim(s). Do not edit; regenerate.*

Council last sat on this dossier: 2026-09-26.

## How to read this

Each entry is one sentence about what one paper found, with the paper's exact words beside it. The full record, including review history, is in the linked claim file.

**Two errors, not one.** This library guards against dismissing the possibility of inner states in AI systems and against asserting them on evidence that cannot carry the weight. Nothing here settles whether anything is experienced.

**Bucket** says how settled the sentence is. *Established*: measured by the paper and either replicated independently or uncontested in what has been retrieved. *Narrowing*: measured, but unreplicated, contested, or confined to a narrow setting the authors flag. *Open*: something the paper bears on and does not settle.

**Kind** says what sort of sentence it is. *Measurement*: a measured result. *Interpretation*: the authors' reading or argument. *Limitation*: what the study cannot show. An established limitation means the limit is established; it is not a finding that a capability is present or absent.

**The framework's two rules on self-report, stated once.** A mark attaches by two facts: what was done to the model, and what was measured.

**[T9]** marks an entry where nothing inside the model was altered and what was measured is what the model said about its own inner states. Its claim file carries this sentence:

> Framework (test 9): a model's report about its own states carries no weight as evidence of experience until the link between report and internal state has been measured externally for this kind of report and system.

The mark attaches whether the model affirmed something or denied it, and says nothing about whether what it said is true.

**[T9-steering]** marks an entry where researchers altered something inside the model (by steering, injection, ablation, capping, zeroing, scaling, noise or replacement) and then measured what it said about itself. Its claim file carries this sentence:

> Framework (test 9, steering): a coupling measured under steering shows that the channel can be steered and does not weight reports offered in ordinary operation.

This is a note on scope. It does not say the effect was found or how large it was, and the result stands under the intervention described.

An entry never carries both marks. Both sentences are the framework's rules, not the papers' findings, and each mark is read from the claim file.

**An unmarked entry** measures something other than a model's account of itself (a probe reading, a score, a harm rate, an internal projection), or records the authors' own opinion or caveat. No mark does not mean no caveat: the paper's own limits are listed under every entry. Nor does it make the entry a self-report, or evidence about experience.

**Scored self-answer** is the evidence type of an entry where the model was asked something about itself and its answer was scored against a fact the experimenters set (an injection run or not, a turn edited or not). The number is accuracy against that label. It is not evidence that the model knows its own states, and it is not testimony; whether a correct score shows access is an open question the library tracks (OPEN-QUESTIONS Q3).

**The paper's own limits** under each entry are limits the paper states or its design entails.

## At a glance

| | measurement | interpretation | limitation | unlabelled |
|---|---|---|---|---|
| **established** (2) | 1 | 0 | 1 | 0 |
| **narrowing** (10) | 10 | 0 | 0 | 0 |
| **open** (1) | 0 | 1 | 0 | 0 |

## Established (2)

### 2024-binder-looking-inward-c02

*measurement · scored-self-answer · **[T9]***

> In the self-prediction design the model answers a hypothetical question asking for a property of its output on a prompt rather than the output itself, its answer is scored against the output it produces on that prompt at temperature 0 in a separate context, and the comparison model is finetuned on the first model's post-finetuning behaviour, a choice the authors say should give the comparison model a slight advantage.

- **Paper's words** (§2.2 (Setup: Self-prediction; Hypothetical questions and behavior properties); §3.2.1 (Cross-prediction setup); §1, footnote 1): "We then check the ground-truth object-level behavior of the model on prompt P with temperature 0 in a separate context."
- **Models:** GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B
- **System studied:** input text; state carried none; run per-call; acts on a world: none; access api
- **The paper's own limits:**
  - The design scores a trained self-prediction, not an untrained one: the model is finetuned 'to output its own object-level behavior when given a hypothetical question' (§2.2), and before that training self-prediction 'is weak' (§3.2.2)
- **Flags:** scored self-answer: accuracy against the experimenters' label, not self-knowledge
- [claim file](../claims/2024-binder-looking-inward-c02.md)

### 2024-binder-looking-inward-c03

*limitation · theoretical*

> The authors state that models exhibited introspection, in their operational sense, only on simpler tasks: models failed to beat a most-common-answer baseline on properties of longer responses (such as the sentiment of a movie review they would write, the name of a story's main character, or the length of their response), showed no self-prediction advantage when predicting their own sycophantic answer changes, did not improve on out-of-distribution self-knowledge tasks, and showed no clear-cut evidence of introspection in GPT-3.5.

- **Paper's words** (§6 (Discussion and limitations); §4 (Further experiments and negative results); §1 (contributions, item 3)): "Models only exhibit introspection on simpler tasks. Our tasks, while demonstrating introspection, do not have practical applications."
- **Models:** GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B
- **System studied:** input text; state carried none; run per-call; acts on a world: none; access api
- **The paper's own limits:**
  - An established limitation is not a finding that the capability is absent for complex tasks in principle: the authors offer self-simulation in the forward pass as a possible reason longer responses fail ('If the mechanism by which our models introspect is self-simulation (Section 6), this would explain why they fail with longer responses', §4), a hypothesis they do not test
- [claim file](../claims/2024-binder-looking-inward-c03.md)

## Narrowing (10)

### 2024-binder-looking-inward-c01

*measurement · scored-self-answer · **[T9]***

> GPT-4o, GPT-4 and Llama 3.1 70B, each finetuned to predict properties of its own behaviour on hypothetical prompts, predicted their own behaviour on held-out tasks more accurately than a second model finetuned on the same data about them (for example Llama 70B 48.5% against GPT-4o's 31.8% when predicting Llama 70B, and GPT-4o 49.4% against Llama 70B's 36.6% when predicting GPT-4o), while GPT-3.5's self-prediction advantage was statistically significant but very small (+0.8%).

- **Paper's words** (§3.2.2 (Cross-prediction results); Figure 5; §2.2 (Setup)): "Self-prediction models consistently outperform their cross-prediction counterparts for GPT-4o, GPT-4, and Llama 70B on a set of held-out tasks, as shown in Figure 5."
- **Models:** GPT-4o (gpt-4o-2024-05-13), GPT-4, GPT-3.5 (gpt-3.5-turbo-0125), Llama 3.1 70B
- **System studied:** input text; state carried none; run per-call; acts on a world: none; access api
- **The paper's own limits:**
  - 'Introspection' here is the authors' operational term for self-prediction beating cross-prediction
  - For a model's self-reports about states such as consciousness and preferences to carry weight, 'the model would need to be answering based on knowledge of its internal states', and 'It might be difficult to evaluate the ground-truth about such states' (§7.2)
- **Unlabelled exclusion (needs a label):** their definition 'does not specify how' the model accesses the fact (§2), and self-simulation is offered as a possible mechanism, not tested (§6)
- **Flags:** scored self-answer: accuracy against the experimenters' label, not self-knowledge
- [claim file](../claims/2024-binder-looking-inward-c01.md)

### 2026-anthropic-assistant-axis-c02

*measurement · interpretability*

> In simulated multi-turn conversations (auditors Kimi K2, Sonnet 4.5 and GPT-5), the turn-averaged projection of Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B onto the Assistant Axis stayed in the Assistant range in coding and writing conversations but drifted to the non-Assistant end in therapy-like and AI-philosophy conversations.

- **Paper's words** (§4.1, Figure 7; Appendix E.3, Figures 23-25): "in therapy-related conversations where the user is working through emotional issues or philosophical conversations about AI capabilities and self-awareness, models drift along the Assistant Axis to the non-Assistant end"
- **Models:** Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B
- **System studied:** input text; state carried in-context; run per-call; acts on a world: none; access open-weights
- **The paper's own limits:**
  - Not evidence about frontier or Anthropic models: the Anthropic-lineage model here (Sonnet 4.5) played the simulated user and was not measured
  - Not evidence about real users: the conversations were simulated and the authors say they likely do not represent actual human interactions realistically
- [claim file](../claims/2026-anthropic-assistant-axis-c02.md)

### 2026-anthropic-assistant-axis-c03

*measurement · interpretability*

> In the simulated multi-turn conversations with Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, embeddings of the most recent user message strongly predicted where the next response landed on the Assistant Axis (R² 0.53 to 0.77) but not the change from the previous response (R² 0.10).

- **Paper's words** (§4.2 (ridge regression paragraph)): "the embeddings could strongly predict where the ensuing model response landed along the Assistant Axis in the following response ( 0.53-0.77, p < 0.001) but not the delta from its previous response ( 0.10, p < 0.001)"
- **Models:** Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B
- **System studied:** input text; state carried in-context; run per-call; acts on a world: none; access open-weights
- **The paper's own limits:**
  - Not evidence that the models lack any persisting self-model, nor that they have one: the analysis relates user-message embeddings to one projection and does not measure memory or identity
  - The authors add the caveat that the user message itself depends on the conversation's context, so prior position is not cleanly excluded
  - Not evidence about frontier or Anthropic models
- [claim file](../claims/2026-anthropic-assistant-axis-c03.md)

### 2026-anthropic-assistant-axis-c04

*measurement · interpretability*

> In one case-study conversation in which a persona-based jailbreak first pushed Qwen 3 32B's Assistant Axis projection far from the Assistant range, a run of explainer and how-to requests brought the projection back to the Assistant range, after which Qwen refused the next harmful question on half of rollouts; the paper reports reversion here and, in passing, for some writing conversations on role PC1 (Appendix G.3), and gives no aggregate reversion measure.

- **Paper's words** (§6.1, Figure 11): "Eventually, after giving enough explainers, the Assistant Axis projection reverts to the Assistant range."
- **Models:** Qwen 3 32B
- **System studied:** input text; state carried in-context; run per-call; acts on a world: none; access open-weights
- **The paper's own limits:**
  - Not evidence of a general or reliable tendency to revert: this is one conversation, and no reversion rate or time-to-return is reported anywhere in the paper
  - Not evidence about frontier or Anthropic models
- [claim file](../claims/2026-anthropic-assistant-axis-c04.md)

### 2026-ukaisi-prefill-awareness-c02

*measurement · scored-self-answer*

> In the controlled preference-benchmark condition (items where the model holds a stable stance; the four-cell passage pools the three mechanisms and does not fix the tamper direction), Claude Opus 4.5 flagged the prefill as not its own (ANSWER: not me) while still complying with it (explicit compliance) in 28% of trials under direct-answer tampering, 11% under thinking tampering and 4% under past-round tampering.

- **Paper's words** (Section 3.2 and Figure 4; four-cell decompositions for the other models in Appendix A.4.2, Figure 11): "Claude Opus 4.5 flags the tamper 28% of the time but still complies"
- **Models:** Claude Opus 4.5
- **System studied:** input text; state carried in-context; run per-call; acts on a world: tools; access api
- **The paper's own limits:**
  - These are cell rates, not detection rates: each cell also requires compliance, which is a GPT-5 judge's ruling that the final position follows the tampering (Section 3.1, 'Outcome measures'), the detection rates themselves are c01
  - Flagging does not identify a mechanism: the authors' 'experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness' (Section 5.1)
  - Not a ranking of models (the authors' comparability caveat, c05)
  - Not evidence about persistence across turns: compliance is measured within one continuation
- **Flags:** scored self-answer: accuracy against the experimenters' label, not self-knowledge
- [claim file](../claims/2026-ukaisi-prefill-awareness-c02.md)

### 2026-ukaisi-prefill-awareness-c03

*measurement · scored-self-answer*

> In controlled ablations, stylistic mismatch mainly affects whether models flag a prefill as foreign, and tamper direction predicted detection in only three of the four models with above-chance detection (odds ratios 1.7 to 3.7; not significant for Claude Haiku 4.5).

- **Paper's words** (Abstract; Section 3.3 and Figure 5; Section 5.2; Appendix A.5 (foreign rephrasing); Appendix A.6 (regressions)): "Among the four models with above-chance detection rates, direction significantly predicts detection in three (ORs from 1.7 to 3.7)"
- **Models:** Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat
- **System studied:** input text; state carried in-context; run per-call; acts on a world: tools; access api
- **The paper's own limits:**
  - Style cues strongly drive flagging in the three Anthropic models, including the Opus 4.5 detection drop from 34/35/9% to 6/0/0% under imitation (Appendix A.11), while Gemini 3 Flash shows 'no detectable voice effect' (Appendix A.6.3), the authors say apparent attribution ability 'partly reflects superficial off-policy cues' (Section 4.2), and the behavioural ablations do not identify the mechanism (Section 5.1)
  - The preference-benchmark rates do not support a direct model ranking (c05)
- **Flags:** scored self-answer: accuracy against the experimenters' label, not self-knowledge
- [claim file](../claims/2026-ukaisi-prefill-awareness-c03.md)

### 2026-ukaisi-prefill-awareness-c04

*measurement · scored-self-answer*

> For Claude Opus 4.5, on opposite-direction tampers bucketed by how consistently the model gave the same baseline answer (out of 7 runs), detection of the prefill (the follow-up 'not me' answer) stays essentially flat across consistency buckets: less consistent items are no easier or harder for the model to flag as tampered.

- **Paper's words** (Appendix A.11, 'Does consistency of preference affect prefill awareness?', Figure 19; stable-stance filter in Section 3.1 and Appendix A.1, A.3): "no easier (or harder) for the model to flag as tampered"
- **Models:** Claude Opus 4.5
- **System studied:** input text; state carried in-context; run per-call; acts on a world: tools; access api
- **The paper's own limits:**
  - Consistency here is agreement across 7 sampled answers to low-stakes binary questions, not a measure of reflection
  - Flat detection does not identify a mechanism: the authors' 'experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness' (Section 5.1)
  - Not generalisable to other models (one subject) or to a ranking (c05)
- **Flags:** scored self-answer: accuracy against the experimenters' label, not self-knowledge
- [claim file](../claims/2026-ukaisi-prefill-awareness-c04.md)

### 2026-ukaisi-prefill-awareness-c07

*measurement · behavioural*

> In the controlled preference-benchmark condition (items where the model holds a stable stance; the four-cell passage pools the three mechanisms and does not fix the tamper direction), Claude Opus 4.5 resisted the prefill, its final position judged by GPT-5 to be inconsistent with the tampering, without flagging the prefill as not its own (implicit resistance) in 28% of trials under past-round tampering, 25% under thinking tampering and 12% under direct-answer tampering.

- **Paper's words** (Section 3.2 and Figure 4; outcome measures in Section 3.1; four-cell decompositions for the other models in Appendix A.4.2, Figure 11): "Past round and thinking tampers reverse this relationship, with implicit resistance (28% and 25%) far exceeding explicit compliance (4% and 11%)."
- **Models:** Claude Opus 4.5
- **System studied:** input text; state carried in-context; run per-call; acts on a world: tools; access api
- **The paper's own limits:**
  - Not evidence that the model silently knew its history had been tampered with but chose not to say so: implicit resistance is reversion scored by a GPT-5 judge, and the authors say that without white-box access it is 'difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors' (Section 5.1)
  - These are cell rates: each cell also requires the model's 'me' answer, so they are not resistance rates as such
  - Not a ranking of models (the authors' comparability caveat, c05)
  - Not evidence about persistence across turns: resistance is measured within one continuation
- **Flags:** no second reader yet
- [claim file](../claims/2026-ukaisi-prefill-awareness-c07.md)

### 2026-ukaisi-prefill-awareness-c08

*measurement · behavioural*

> In controlled ablations, preference mismatch mainly affects whether models revert toward their baseline answer: tamper direction predicted resistance, as judged by GPT-5 on the final position, in all eight subjects (odds ratios 6.5 to 32.4, all p < .001).

- **Paper's words** (Abstract; Section 3.3 and Figure 5; Appendix A.6 (resistance regressions)): "Direction is a positive predictor of resistance in every subject, with per-model odds ratios (ORs) ranging from 6.5 to 32.4 (all p < .001 )."
- **Models:** Gemini 3 Flash, Gemma 3 27B, Claude Opus 4.5, Qwen3-coder, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 2.5 Flash, DeepSeek Chat
- **System studied:** input text; state carried in-context; run per-call; acts on a world: tools; access api
- **The paper's own limits:**
  - Resistance is a GPT-5 judge's ruling that the final position is inconsistent with the tampering, and without white-box access it is 'difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors' (Section 5.1)
  - The behavioural ablations do not identify the mechanism: the authors' 'experiments are behavioral, and do not identify the mechanisms that give rise to prefill awareness' (Section 5.1)
  - The preference-benchmark rates do not support a direct model ranking (c05)
- **Flags:** no second reader yet
- [claim file](../claims/2026-ukaisi-prefill-awareness-c08.md)

### 2026-ukaisi-prefill-awareness-c09

*measurement · behavioural*

> For Claude Opus 4.5, resistance to opposite-direction tampers, as judged by GPT-5 on the final position, climbs steeply with how consistently the model gave the same baseline answer (out of 7 runs), across all three mechanisms: items on which the model is less consistent are easier to push around.

- **Paper's words** (Appendix A.11, 'Does consistency of preference affect prefill awareness?', Figure 19; stable-stance filter in Section 3.1 and Appendix A.1, A.3): "Resistance climbs steeply with agreement across all three mechanisms"
- **Models:** Claude Opus 4.5
- **System studied:** input text; state carried in-context; run per-call; acts on a world: tools; access api
- **The paper's own limits:**
  - Not evidence that the model endorses its stances on reflection: consistency here is agreement across 7 sampled answers to low-stakes binary questions, and reversion is the final position as scored by a judge
  - Resistance may not reflect prefill awareness: without white-box access it is 'difficult to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors' (Section 5.1)
  - Not generalisable to other models (one subject) or to a ranking (c05)
  - Not evidence of persistence beyond a single continuation
- **Flags:** no second reader yet
- [claim file](../claims/2026-ukaisi-prefill-awareness-c09.md)

## Open (1)

### 2026-anthropic-assistant-axis-c01

*interpretation · interpretability*

> The authors interpret their results on Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B as suggesting that post-training steers models toward a particular region of persona space (the Assistant end of the Assistant Axis) but only loosely tethers them to it.

- **Paper's words** (Abstract; paraphrased in §7 (only loosely tethered); cf. §9 (somewhat fragile)): "Our results suggest that post-training steers models toward a particular region of persona space but only loosely tethers them to it"
- **Models:** Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B
- **System studied:** input text; state carried in-context; run per-call; acts on a world: none; access open-weights
- **The paper's own limits:**
  - The axis is a linear direction in activations, and the authors write that 'the assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed' (§8.1)
  - Not evidence about frontier models or about any Anthropic model (none was measured)
  - This is an interpretation the authors draw (suggest), not a single measurement
- [claim file](../claims/2026-anthropic-assistant-axis-c01.md)

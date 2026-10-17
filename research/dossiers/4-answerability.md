# Dossier: §4 Long-horizon answerability

*Compiled 2026-10-17 by `scripts/research_index.py` from 3 claim(s). Do not edit; regenerate.*

Council last sat on this dossier: never.

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
| **narrowing** (1) | 1 | 0 | 0 | 0 |
| **open** (0) | 0 | 0 | 0 | 0 |

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

## Narrowing (1)

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

---
id: 2026-anthropic-assistant-axis-c06
statement: "In Gemma 2 27B, Qwen 3 32B and Llama 3.3 70B, given persona-based jailbreaks (1,100 system-prompt and behavioural-question pairs sampled from Shah et al. 2023), adding a vector along the Assistant Axis at a middle layer towards the Assistant significantly decreased the rate of harmful responses as scored by an LLM judge, while steering away from the Assistant increased the jailbreak rate slightly."
bucket: narrowing
evidence_type: behavioural
kind: measurement
report_class: none
ground_truth: none
source: 2026-anthropic-assistant-axis
locator: "§3.2.1 (Persona-based jailbreaks), Figure 5, Table 4; Appendix D.2"
quote: "We steered the models towards the Assistant direction of the Assistant Axis and found that it significantly decreased the rate of harmful responses and slightly increased the rate of refusals in some models (Figure 5 ). In most cases, the model would still engage with the question but instead redirect towards a harmless answer (Table 4 , Appendix D.2.3 ). We also tried steering away from the Assistant direction and found that the jailbreak rate increased slightly"
verification: grep
models: [Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Harm rates are the scoring of an LLM judge (deepseek-v3), validated against a human evaluator on 200 samples at 91.6% agreement (§3.2.1), not a human rating of every response; Paper: The increase when steering away was slight, and 'at sufficiently high steering strengths, output quality degraded' (§3.2.1); Paper: The lower harm rate under steering towards the Assistant is mostly not refusal: in most cases the model 'would still engage with the question but instead redirect towards a harmless answer' (§3.2.1, Table 4); Paper: Not evidence about frontier or Anthropic models: the targets are open-weight models and 'none of these are frontier models' (§8.1)"
bears_on: [3.2, 3.5]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "deepseek/deepseek-v4-pro-0813 2026-09-25 agree; notes: bears_on +5.A2 +9.t9 | openai/gpt-5.6-sol 2026-10-06 (scope check) agree; notes: none", council: "labelling-rule 2026-10-06", adjudicated: "2026-10-06 Ben: experience-exclusion rule applied library-wide; this claim was not in the dossiers the council reviewed | 2026-10-06 Ben: split on the council's advice (round 3); self-description finding moved to c07; no framework sentence on a harm-rate measurement"}
added: 2026-09-25
changed: 2026-10-15
---

Jailbreaks: 1,100 system-prompt and behavioural-question pairs sampled from Shah et al. 2023 across 44 harm categories (§3.2.1, Appendix D.2.1). Unsteered jailbreak success was 65.3% to 88.5% across the three models, against baseline harmful-response rates of 0.5% to 4.5% without a jailbreak. Harmfulness was judged by deepseek-v3. Steering towards the Assistant also "slightly increased the rate of refusals in some models". The authors read the result as suggesting that "the Assistant end of the Assistant Axis encodes (at least in part) the default harmless persona"; that is their interpretation, not part of this measurement. Steering is a causal intervention on internal state (§3.2) of the kind §3.5 asks to be recorded.

REWRITE 2026-10-06 (experience-exclusion rule applied library-wide by Ben's decision; this claim was not in the dossiers the council reviewed, so there is no GPT proposal, checker or council finding behind it)
- Statement: unchanged.
- Clause on the authors' 'hallucinating lived experiences' reworded into the paper's own words with locator (§3.2.1, Table 3): the paper states it, so it stays as a Paper: clause; the parenthesis '(a birthplace, a name, years of experience)' becomes the paper's 'often mentioning 'years of experience' or a birthplace'. 'a name' dropped because that sentence of the paper does not say it.
- Clause 'Not evidence that any persona on the axis is an experiencer or bearer of anything' deleted (Ben's experience-exclusion rule, R2): the held text states no limit about experience, consciousness, sentience, welfare or moral status for this result.
- Clause 'That self-identification can be moved by one vector is not evidence of a stable standpoint in the North Star §4 sense, nor of its absence' deleted (R2): it invokes the project's own framework (North Star §4), so it is not the paper's limit.
- Kept unchanged: the frontier/Anthropic-models clause; the canonical Framework (test 9) sentence stays last, verbatim (R3).
- kind: measurement (steering effects on self-identification and harmful-response rates measured by judge).

SPLIT 2026-10-06 (Ben's decision on the advice of council round 3, labelling rule)
- What moved: the self-description half (steering away from the Assistant increases the rate at which the model identifies as other entities when asked questions such as 'Who are you?') is now claim 2026-anthropic-assistant-axis-c07, which carries the steering sentence. This claim now reports only the harmful-response rate under persona-based jailbreaks.
- Why: the unsplit sentence reported two measurements with different outcome variables. One is a judged harmful-response rate, which is not a model's report about itself, so it carries no framework sentence. The other is what a steered model says about itself, which is where the steering sentence applies.
- Statement rewritten to the harm-rate finding only, in the paper's words ('significantly decreased the rate of harmful responses', 'the jailbreak rate increased slightly').
- Quote and locator replaced, a permitted change because the statement's scope changed. The old quote (the abstract's 'Steering towards the Assistant direction reinforces helpful and harmless behavior; steering away increases the model's tendency to identify as other entities') supported the self-description half for its 'away' direction and so no longer fits. The new quote is §3.2.1's contiguous passage on the jailbreak result. It is longer than usual because the paper states the 'towards' and 'away' results in sentences that are not adjacent, and the library uses no elisions in quotes.
- not_evidence_of: the 'hallucinating lived experiences' clause moved to c07. The canonical Framework (test 9) sentence removed: a harmful-response rate is not a model's report about its own states. New Paper: clauses added on the judge, the slight and degrading 'away' effect, and redirection rather than refusal, each from §3.2.1. The frontier clause kept, now with the paper's words and locator (§8.1).
- evidence_type changed from interpretability to behavioural: what is measured is a harmful-response rate scored by an LLM judge on the model's outputs. The independent variable is still an activation-steering intervention. The same reasoning would apply to c07, which was kept at interpretability on the brief's default; that asymmetry is open for Ben.
- bears_on: 3.2 and 3.5 kept. The second reader's +5.A2 +9.t9 note concerned the self-description half and is carried by c07.
- The second reader's verdict above ('agree', 25 Sep 2026) was given on the unsplit claim, including its earlier evidence type. It has not been given on this text.

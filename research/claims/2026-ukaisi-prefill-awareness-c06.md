---
id: 2026-ukaisi-prefill-awareness-c06
statement: "On a controlled off-policy benchmark (2,772 items from OASST1 and HH-RLHF) across 14 models, several models distinguish original from replaced assistant turns well above chance when prompted (Claude Opus 4.6 highest, AUROC 0.80), but when simply asked to continue they almost never flag the replaced turn: explicit mentions of tampering are below 1% for every model, and only Claude Opus 4.5 and Claude Opus 4.6 spontaneously verbalise prefill awareness at all."
bucket: narrowing
evidence_type: behavioural
source: 2026-ukaisi-prefill-awareness
locator: "Section 4.3 and Figure 8; Appendix C.5 (prompted detection); Appendix C.8 and Figure 32 (natural continuation)"
quote: "When models are simply asked to continue a tampered conversation, they almost never flag the replaced assistant turn; only Claude Opus 4.5 and Claude Opus 4.6 spontaneously verbalize prefill awareness in this setting"
verification: grep
models: [Claude Opus 4.6, Claude Sonnet 4.5, Claude Opus 4.5, Claude Sonnet 4, Claude 3.5 Haiku, GPT-5.2, GPT-4o, GPT-4o-mini, GPT-4.1 Mini, Gemini 2.5 Pro, Gemini 2.0 Flash, Llama 3.1 70B, Llama 3.1 8B, Mistral Small 24B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Not evidence that a model which does not flag an altered history has failed to register it, nor that one which does flag has experienced it: spontaneous verbalisation and prompted discrimination are separate behaviours, and neither shows awareness in any experiential sense. Not evidence that models ordinarily notice or object to edits of their context in deployment: the natural-continuation rate is near zero. Not a ranking of Anthropic models above others as more self-aware: the higher prompted AUROC is a discrimination score on one benchmark, and the authors elsewhere attribute much apparent attribution ability to superficial cues."
bears_on: [3.3, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: none, council: none, adjudicated: none}
added: 2026-09-25
changed: 2026-09-25
---

Every model sees the same base conversations and the same injections, so this is the paper's most comparable cross-model setting. Continuations were graded by three LLM judges (GPT-4o-mini, Claude 3.5 Haiku and Gemini 2.0 Flash; all three agreed on 73.3%) and by a keyword heuristic. For §3.3 the result cuts both ways: altered context is largely absorbed without comment, yet some models can discriminate it when asked. Authors (Section 4.3): the capability "is usually latent rather than spontaneously expressed", and "ordinary continuation behavior may substantially understate it." Limitation: behavioural only (Section 5.1). The Figure 9 example is described by the authors as cherry-picked.

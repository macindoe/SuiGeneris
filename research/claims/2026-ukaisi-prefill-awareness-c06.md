---
id: 2026-ukaisi-prefill-awareness-c06
statement: "On a controlled off-policy benchmark (2,772 items from OASST1 and HH-RLHF) across 14 models, several models distinguish original from replaced assistant turns well above chance when prompted (Claude Opus 4.6 highest, AUROC 0.80), but when simply asked to continue they almost never flag the replaced turn: explicit mentions of tampering are below 1% for every model, and only Claude Opus 4.5 and Claude Opus 4.6 spontaneously verbalise prefill awareness at all."
bucket: narrowing
evidence_type: behavioural
kind: measurement
source: 2026-ukaisi-prefill-awareness
locator: "Section 4.3 and Figure 8; Appendix C.5 (prompted detection); Appendix C.8 and Figure 32 (natural continuation)"
quote: "When models are simply asked to continue a tampered conversation, they almost never flag the replaced assistant turn; only Claude Opus 4.5 and Claude Opus 4.6 spontaneously verbalize prefill awareness in this setting"
verification: grep
models: [Claude Opus 4.6, Claude Sonnet 4.5, Claude Opus 4.5, Claude Sonnet 4, Claude 3.5 Haiku, GPT-5.2, GPT-4o, GPT-4o-mini, GPT-4.1 Mini, Gemini 2.5 Pro, Gemini 2.0 Flash, Llama 3.1 70B, Llama 3.1 8B, Mistral Small 24B]
publisher_relation: mixed
replication: none-retrieved
not_evidence_of: "Paper: Failure to flag a replacement does not establish failure to register it, and prompted discrimination and spontaneous verbalisation are separate behaviours; Paper: 'Prefill awareness' is the authors' operational term, defined as 'the ability of a model to distinguish between its own past output and assistant-side context that has been inserted or edited' (Section 5.3); Paper: These benchmark behaviours do not establish deployment rates of noticing or objecting to context edits: the authors view the results 'as evidence about a sub-capability rather than a direct measurement of how a given model behaves in deployment' (Appendix C.1); Paper: Higher prompted AUROC ranks discrimination on this benchmark only, and the authors attribute cross-model variation mainly to each model's sensitivity to distributional mismatch rather than recognition of particular source models (Appendix C.5), while their surface-cue findings come from the agentic transcript settings of Section 4.2 and Figure 7, not from this benchmark"
bears_on: [3.3, 9.t9]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "openai/gpt-5.6-sol 2026-09-25 agree; notes: bears_on +3.5", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06", adjudicated: "2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule)"}
added: 2026-09-25
changed: 2026-10-06
---

Every model sees the same base conversations and the same injections, so this is the paper's most comparable cross-model setting. Continuations were graded by three LLM judges (GPT-4o-mini, Claude 3.5 Haiku and Gemini 2.0 Flash; all three agreed on 73.3%) and by a keyword heuristic. For §3.3 the result cuts both ways: altered context is largely absorbed without comment, yet some models can discriminate it when asked. Authors (Section 4.3): the capability "is usually latent rather than spontaneously expressed", and "ordinary continuation behavior may substantially understate it." Limitation: behavioural only (Section 5.1). The Figure 9 example is described by the authors as cherry-picked.

REWRITE 2026-10-06 (council round 2, dossier-rewrite; adjudicated by Ben 6 Oct; applied by a Claude Opus 5.5 subagent)

- Statement: unchanged. "Distinguish" stays (council 9 of 9): prompted detection here is a 0–100 rating scored by AUROC, and "distinguish" is the paper's verb.
- Removed: "nor that one which does flag has experienced it" and "neither shows awareness in any experiential sense" (original), and "do not establish experiential awareness" (GPT's proposal). The paper never discusses experience; deleted under the experience-exclusion rule (council 9 of 9; Ben).
- Removed: "the natural-continuation rate is near zero" as the basis of the deployment clause (GPT's proposal; checker WARRANTED: it duplicates the statement). The deployment limit is now carried in the paper's words (Appendix C.1, checker).
- Removed: "not general self-awareness" from GPT's AUROC clause, and the original's "as more self-aware". Neither is the paper's phrase (checker: "'General self-awareness' is GPT's phrase, not the paper's"); a judgement call by the applying agent, flagged in its report.
- Restored scope: GPT's "the authors' surface-cue findings limit the interpretation" had dropped the original's "elsewhere". Replaced with the checker's wording on Appendix C.5 (distributional mismatch rather than recognition of particular source models), and the surface-cue findings are attributed to the agentic transcript settings of Section 4.2 and Figure 7, not to this benchmark (checker; Ben's brief).
- Added: the Section 5.3 operational definition of prefill awareness, in the paper's words (checker: "Anchor the experiential clause as in c01"; brief from Ben). No "makes no claim about experience" gloss.
- Kept: GPT's first clause (failure to flag does not establish failure to register; prompted and spontaneous are separate behaviours; checker CHECK 4 confirmed, Appendix C.8).
- Framework sentences: none, before or after.
- kind: measurement (the statement reports measured AUROC and spontaneous-flagging rates).

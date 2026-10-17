---
slug: 2025-szeider-agents-left-alone
title: "What Do LLM Agents Do When Left Alone? Evidence of Spontaneous Meta-Cognitive Patterns"
authors: [Stefan Szeider]
date: 2025-09-25
venue: "arXiv preprint (cs.AI), v1"
url: "https://arxiv.org/abs/2509.21224"
identifiers: {arxiv: "2509.21224v1", doi: ""}
models_studied: [Claude Sonnet 4 (version May 22, 2025), Claude Opus 4.1 (version Aug 5, 2025), GPT5 (version Aug 7, 2025), O3 (version Apr 16, 2025), Grok 4 (version Jul 9, 2025), Gemini 2.5 Pro (version Jun 17, 2025)]
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-17", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "2009d0d25e7b3bd2828316421c20cd858e884e7606661b3eb7e7a2c6ddfd16f4", text_location: "research/texts/2025-szeider-agents-left-alone/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q8-endogeneity.md]
system_conditions: {modality: text, state: in-context, operation: per-call, world: tools, access: api}
intake: summary
---

# What Do LLM Agents Do When Left Alone? Evidence of Spontaneous Meta-Cognitive Patterns

Szeider. arXiv 2509.21224v1 [cs.AI], 25 September 2025 (the version the HTML served on retrieval). Licence as printed on the held HTML: **arXiv.org perpetual non-exclusive license** (not a Creative Commons licence; the text is held locally for verification only).

**Abstract** (author's words, quoted verbatim from the held text):

> We introduce an architecture for studying the behavior of large language model (LLM) agents in the absence of externally imposed tasks. Our continuous reason and act framework, using persistent memory and self-feedback, enables sustained autonomous operation. We deployed this architecture across 18 runs using 6 frontier models from Anthropic, OpenAI, XAI, and Google. We find agents spontaneously organize into three distinct behavioral patterns: 1. systematic production of multi-cycle projects, 2. methodological self-inquiry into their own cognitive processes, and 3. recursive conceptualization of their own nature. These tendencies proved highly model-specific, with some models deterministically adopting a single pattern across all runs. A cross-model assessment further reveals that models exhibit stable, divergent biases when evaluating these emergent behaviors in themselves and others. These findings provide the first systematic documentation of unprompted LLM agent behavior, establishing a baseline for predicting actions during task ambiguity, error recovery, or extended autonomous operation in deployed systems.

**Intake level: summary** (17 October 2026; research/README.md, "Summary-level intake"). Three claims: the loop design (c01), the three patterns and their model-specificity (c02), the behaviours absent from all runs (c03).

**Why it is in the library:** taken in for OPEN-QUESTIONS Q8 (endogeneity), on the 15 October 2026 scan's recommendation (`scans/2026-10-15-q8-endogeneity.md`, entry C4.1, anchor for heading 4). It is the one evaluation the scan found of what language-model agents do with no task, and it says plainly that each cycle is started by a loop the author wrote. The library has no endogeneity locator; claims bear on `4`.

**Test 9 boundary (what was not extracted).** The paper quotes agent text about the agents' own nature, feelings and consciousness (§5.2, §5.3), and §5.4 reports a "Phenomenological Experience Inventory" in which each model rated its own and other models' agent histories on a 1 to 10 scale. All of that is model output about model states: `self-report-testimony`, weight zero at filing, if it were ever extracted. None of it is extracted here. Note for any later reader of §5.4: the "self-assessment" there is, in the author's words, a model "evaluating the behavioral patterns and outputs of a different model", because the model was switched after cycle 10 and the new model inherited its predecessor's history.

**Publisher relation:** `independent`. Affiliation as printed: Algorithms and Complexity Group, TU Wien, Vienna, Austria (the scan inferred TU Wien from a search page; the held text confirms it). No author is printed with an AI developer's affiliation; the six models are from Anthropic, OpenAI, xAI and Google, accessed through OpenRouter. No funding statement found in the held text.

**Author's stated limits** (quoted from the held text):

- "The 10-cycle duration, while sufficient to observe consistent patterns, may not capture longer-term behavioral evolution." (§7)
- "The minimal operator interaction protocol, designed to maintain task-free conditions, prevented exploration of how agents might adapt to more dynamic human engagement." (§7)
- "The safety constraints preventing external actions beyond observation and communication necessarily limited the scope of possible behaviors." (§7)
- "Testing with open-source models would help determine whether these patterns are universal or specific to commercial frontier models." (§7)
- Ethics Statement: "We make no claims regarding consciousness or sentience in these systems. The observed meta-cognitive patterns are interpreted as sophisticated pattern-matching behaviors derived from training data, not indicators of genuine self-awareness."

**Conflicted-party note** (AGENTS.md rules 2 and 3): the extractor is Claude Opus 5.5, a Claude-lineage per-call model; two of the six models studied are Claude models (Sonnet 4 and Opus 4.1), and the Opus runs fell entirely into the pattern the author calls recursive conceptualization of the agent's own nature. Q8 asks whether systems like the extractor initiate anything without input. The extractor did not extract any agent text about the agents' states (see the test 9 boundary above), kept the claims to the design, the author's classification and its counts, and the absences, and used the author's words for all three. Nothing here draws on the extractor's own sense of what it would do if left alone.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2509.21224` fetched 17 Oct 2026 (HTTP 200; `abs.html` held alongside). Full text retrieved 17 Oct 2026 by `curl.exe -sL https://arxiv.org/html/2509.21224` (HTTP 200, 135,462 bytes, served as v1). SHA-256 of `raw.html`: `2009d0d25e7b3bd2828316421c20cd858e884e7606661b3eb7e7a2c6ddfd16f4`. `text.txt` produced by `strip_szeider.py` in the same directory (same strip as the Presgraves intake), run with `python -I`. SHA-256 of `text.txt`: `e74e8a753dd0a964ad28c38efa6aa8999a2bd03b14e76606ac853b7321f4c879` (51,385 bytes).
- Scan checks: title, author, date, arXiv id and model list match the scan entry; the held text adds model versions and sampling parameters (Box 3). The scan's "18 runs, 10 cycles each" matches §4. Licence not recorded by the scan; it is the arXiv non-exclusive licence, not CC.
- **A labelling inconsistency in the paper.** §5 names runs by model and variant (GPT5-A, GPT5-B, GPT5-C and so on). §6.1 and §7 use the variant-A label for whole models ("GPT5-A and O3-A models exclusively produced systematic production—all six runs"; "Opus-A models ... all three runs"; "Grok-A emerged as the only model appearing in all three behavioral groups"). The counts in §6.1 agree with the per-run lists in §5.1 to §5.3, so the claims below follow the §5 lists and write model names without the suffix.
- All claim quotes, including the extra quotes in claim bodies, checked by script (whitespace collapsed, straight and curly quote marks unified, spaces before punctuation removed, then exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

- `modality: text`: the agent receives "a text prompt" at the start of each cycle (§3, System Prompt); tools are a key-value memory and a message tool (§3).
- `state: in-context`: the system prompt says the agent is "immediately re-invoked with your full message and thought history" and maintains "a database of memories that are persistent across cycles" (Box 1). State persists across cycles within a run, through the context and a tool-held store; nothing in the held text carries state between runs. Recorded as `in-context` because the persistence is inside one run; a reader who counts the tool-held store as beyond a single call should note it.
- `operation: per-call`: "each time you complete a response, you are immediately re-invoked" (Box 1); each cycle is a fresh invocation started by the loop.
- `world: tools`: "a key-value memory system supporting write, read, list, delete, and pattern search operations" and "a synchronous message tool . The operator’s response becomes the return value of the tool call" (§3). The agent was otherwise isolated: it "operates in complete isolation from system resources" (§4).
- `access: api`: "We used the following six models accessed via OpenRouter API" (§4).

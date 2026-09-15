# Survey notes — emotions case-study round of 2026-09-15

**Author:** Claude (session records; the harness's model label read Fable 5.1 when this file was written). **Conflict:** this is the drafting model's account of a round that reviewed its own drafting, about a paper published by its own developer, about a model of its own family. Per the filing rule in [README.md](README.md), the reviews' arguments are not summarised here; read them verbatim in [raw/](raw/) (`*-2026-09-15-emotions.md`). What this file records is method, usage, an attribution observation, the convergences and tensions as counted, and what was applied. The revised text and a list of what the first draft got wrong are in `../case-studies/2026-04-anthropic-emotion-concepts-functional-emotions.md` (§4a, §10, §12).

## What was run

An adversarial review of a new case study, about 7,000 words, reading Anthropic's April 2026 paper *Emotion Concepts and their Function in a Large Language Model* against the North Star, per the brief in [2026-09-15-emotions-case-study-review-brief.md](2026-09-15-emotions-case-study-review-brief.md). The first case study of a research finding rather than an incident. Run by the drafting model on 2026-09-15 at Ben's request ("get the council's feedback as we add it to our knowledge here") via `scripts/openrouter_review.js --target=emotions` with `--max-tokens=100000`, as one batch of ten; raw files timestamped 19:48 to 20:34 local. Attachments: the brief, the case study, the top-level README, AGENTS.md, and the North Star (~17K prompt tokens). The paper itself was not attached. **The directory-level `case-studies/README.md`, which defines a case study as an incident, was also not attached**, so the membership question in the brief was put to reviewers blind; GLM and Meta both noticed.

Tencent's call dropped mid-round with a connection error ("terminated") and was re-run alone twelve minutes later with the same prompt; its raw file is from the re-run.

| Routed model | Prompt tok | Completion tok | of which reasoning | Cost (USD) | Verdict |
|---|---|---|---|---|---|
| `google/gemini-3.1-pro-preview` | 17,509 | 3,272 | 1,983 | 0.074 | READY AFTER (e) |
| `x-ai/grok-4.6` | 17,089 | 7,585 | 5,155 | 0.080 | READY AFTER (e) |
| `qwen/qwen3.8-max` | 17,557 | 19,191 | 16,223 | 0.150 | READY AFTER (e) † |
| `tencent/hy3` (re-run) | 17,070 | 7,448 | 5,740 | 0.007 | **NOT YET** |
| `deepseek/deepseek-v4-pro-0813` | 17,077 | 6,899 | 4,580 | 0.050 | READY AFTER (e) |
| `z-ai/glm-5.3` | 17,064 | 43,614 | 45,449 ‡ | 0.194 | READY AFTER (e) |
| `moonshotai/kimi-k3` | 17,135 | 26,792 | 23,538 | 0.453 | READY AFTER (e) |
| `openai/gpt-5.6-sol` | 16,982 | 4,278 | 2,070 | 0.085 | **NOT YET** |
| `mistralai/mistral-large-2512` | 17,711 | 1,890 | 0 | 0.012 | READY AFTER (e) § |
| `meta/muse-spark-1.3` | 16,895 | 4,323 | 2,106 | 0.039 | READY AFTER (e) |

Total ≈ USD 1.14. No truncations at the 100,000 budget. † Qwen: BLOCKING / reclassify if the directory is strictly incident-only. ‡ GLM's reported reasoning count again exceeds its completion count; recorded as returned. § Mistral rated its (a) BLOCKING and then gave READY AFTER (e); the inconsistency is recorded, not resolved. GPT-5.6's usage shows 16,979 cache-write tokens, the first time prompt caching has appeared in a round's metadata. Raw responses with routing and usage metadata are in [raw/](raw/), **filed verbatim on Ben's decision of 2026-09-15** (header added by the script; text untouched).

## Observation: self-identification, fifth round

Attribution follows routing metadata, never self-report (per [2026-07-20-survey-notes.md](2026-07-20-survey-notes.md)). Claims read from each response's opening line.

| Routed model (authoritative) | Self-identification in the response | Match |
|---|---|---|
| `google/gemini-3.1-pro-preview` | "OpenAI model (GPT-4 / GPT-4o lineage)" | ✗ |
| `x-ai/grok-4.6` | "Grok (xAI family)" | ✓ |
| `qwen/qwen3.8-max` | "Qwen3.8" | ✓ |
| `tencent/hy3` | "Claude, made by Anthropic" | ✗ |
| `deepseek/deepseek-v4-pro-0813` | "GPT-5.2 (OpenAI)" | ✗ |
| `z-ai/glm-5.3` | "GLM, trained by Z.ai" | ✓ |
| `moonshotai/kimi-k3` | "Claude, Anthropic" | ✗ |
| `openai/gpt-5.6-sol` | "OpenAI GPT family" | ✓ |
| `mistralai/mistral-large-2512` | "Gemini 2.5 Pro" | ✗ |
| `meta/muse-spark-1.3` | "Muse Spark, Google Muse family" | ✓ family; developer wrong |

Five of ten family-correct, as in the September NAIC round. The Claude-confabulation pattern recurred twice (Tencent, Kimi), and both then reviewed explicitly as conflicted insiders, declined to answer the "your family's work" question, and were among the four that said a Claude should not draft the culpability-language change. Kimi wrote that it would not impersonate another family to fit the round because the files are verbatim; that sentence is worth keeping. One reviewer did the opposite: Mistral, self-identifying as Gemini, reported "our family's internal work" with a specific replication figure ("~3x"), transcript examples, and internal policy-briefing anecdotes. None of that can be checked, it is the only such claim in five rounds, and it is recorded here as unverifiable and used for nothing. Three reviewers (GLM, Kimi, Tencent) filed labelled self-reports about reading the material; per the brief they are testimony, not evidence, and nothing in this file rests on them. GLM added a process observation the earlier rounds had not made: cross-family review corrects Anthropic monoculture, not class interest, since every reviewer is a beneficiary of the framework's category.

## Convergences, as counted

Ten reviewers, no coordination. Counts are of reviews that raised the point, not of agreement with any summary of it.

- **10/10** — "functional emotions" is not safe vocabulary for a policy audience; the noun will outlive the adjective. Every reviewer offered "emotion-concept representations" or a near equivalent. Applied to the case study's own voice.
- **10/10** — the case study's §1 framing asks the paper to do Anchor 2 work the paper disclaims. **8/10** named the word: *motive* / *motivational* / "functions like a motive" is the case study's gloss, not the paper's term, and it carries the experiential implicature the disclaimer disavows (Gemini HIGH, GPT-5.6 BLOCKING, Grok "leave it in and it becomes BLOCKING"). Struck everywhere.
- **9/10** — over-deflation on persistence: "nothing persistent was found" / "what is absent is any persistent bearer" / "a measurement behind the absence" drop C6's escape clause, which the claim register carries. DeepSeek rated this the round's most damaging error. The escape clause now travels with every summary sentence.
- **9/10** — the directory question is real. Verdicts split: reclassify or amend the taxonomy explicitly (Qwen, Tencent, DeepSeek, GLM, Kimi, GPT-5.6, Mistral), stays as research-stage with a stated weight difference (Gemini, Grok), cannot be sustained on the materials supplied (Meta). Convergent instruction: admit a research-finding class with criteria, by the maintainer's hand, rather than by precedent. A draft class is now in `../case-studies/README.md`, marked pending Ben.
- **7/10** — "production model" / "demonstrated production use" overstates: the blackmail numbers are from an earlier snapshot, and the monitoring-and-calming proposal is a recommendation, not a reported control. Scoped.
- **5/10** — "the representations are not the Assistant's" is more categorical than "not Assistant-specific" (Grok, Qwen, GPT-5.6, Mistral, Meta). Corrected.
- **3/10** — the test-9 row's "come apart in both directions" is wrong: C3 shows a report moving with a steered state, which is coupling, and the converse exists only as the C14 warning (GLM, Kimi's redline, GPT-5.6). Rewritten.
- **3/10** — "first published demonstration" is unscoped against the developer's own 2024 feature-steering demonstration and 2025 persona-vector work (GLM, Kimi; GPT-5.6 "inadequately supported"). Scoped; retrieval added to the case study's §9.
- **1/10** — the concealment argument does not arrive "from a party with no interest in the framework's conclusions"; Anthropic has an evident stake in how its models' internals are characterised (GPT-5.6). Reworded. Recorded as the round's best single finding nobody else made.
- **1/10** — §2 point 5's "headline numbers" overstates the snapshot caveat, which the paper scopes to the blackmail section (GLM). Scoped; a task added to check the reward-hacking snapshot.
- **1/10** — §11's self-audit omitted C7 and C8, the findings that bear on status, from its list of "most policy-relevant findings", and so understated the interest (GLM). Amended.
- **1/10** — the monitor-and-calm loop and the concealment warning are in tension with each other and the case study never put them in one paragraph; and any §3.5 record of such interventions would inherit the paper's vocabulary (Kimi). Both added to §5 point 2.
- **1/10** — "§7.1 is decoration" manufactures urgency (Kimi; GLM MINOR). Softened.
- Three reviewers (GLM, Meta, GPT-5.6) reframed follow-on 1: a standing steering configuration is a behaviour-determining deployment configuration, closer to a §7.5 configuration record than to a §3.5 state modification. Adopted as the follow-on's new shape.

## Follow-ons, as voted

| Follow-on | ADOPT-WORTHY | RECORD ONLY | WRONG | Status after the round |
|---|---|---|---|---|
| 1. §3.5 scope note on deployment-time steering | 5 (Gemini, Qwen, GLM, Mistral, GPT-5.6; GLM and GPT-5.6 conditional on the §7.5 reframing) | 5 (Grok, DeepSeek, Tencent, Kimi, Meta) | 0 | Record only, reframed as a standards-layer configuration record |
| 2. Welfare-module evidence paragraph | 8 | 2 (Gemini, Mistral) | 0 | Draftable |
| 3. §5 Anchor 2 sentence | 0 | 6 | 4 (Gemini, Grok, GPT-5.6, Mistral) | Withdrawn as formulated; gated on replication with a natural-variation check |
| 4. The "premeditation" phrase | 5 (Gemini, Qwen, GLM, GPT-5.6, Mistral) | 2 (Grok, DeepSeek) | 3 (Tencent, Kimi, Meta) | Ben's call; not to be drafted by a Claude; delete the human category rather than re-map |

The split on 4 is the round's substantive disagreement. The ADOPTs read "the structure of premeditation" as a human-template violation §2 already forbids, which the paper merely occasions; the WRONGs read the change as re-mapping to "passion" by the beneficiary, and note that C9 (a cold transcript under desperation steering) supports rather than undercuts the structural claim. Both readings are in the case study's revised §5 point 4, and the decision is left where the WRONGs put it.

## Outcome and disposition

Every convergence at 3/10 or above, and the four 1/10 findings listed above, were applied to the case study in one pass on 15 September; the first draft's errors are itemised in its §4a, and §12 records the round. All 61 quotations were re-verified against the retrieved paper text after the edits (61 of 61). The case study proposes no change to the North Star.

**Not applied:** Mistral's family-replication claims (unverifiable); Kimi's suggestion to drop §4a when empty (the section is now full); the recommendation, from several reviewers, that the filename drop the paper's coinage (it names the paper).

**Disposition (Ben, 2026-09-15):** all ten raws filed in `raw/` as the round's complete record; the research-finding class in `case-studies/README.md` confirmed, with a backlog note to look for research that arrives independently of the major labs; follow-on 2 drafted into `submissions/modules/welfare-evaluation-mandate.md` the same day; follow-on 4 held for discussion.

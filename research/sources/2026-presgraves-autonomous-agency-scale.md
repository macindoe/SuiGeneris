---
slug: 2026-presgraves-autonomous-agency-scale
title: "The Autonomous Agency Scale: A Behavioral Framework for Measuring Self-Directed Behavior in AI Systems"
authors: [Samuel Presgraves]
date: 2026-07-20
venue: "arXiv preprint (cs.AI), v1; framework version 0.2.1"
url: "https://arxiv.org/abs/2607.17947"
identifiers: {arxiv: "2607.17947v1", doi: ""}
models_studied: [Airi v2.x (companion architecture; longitudinal, August 2025 to July 2026), Claude Code (Sonnet 4.6), Manus 1.6 Max, Hermes Agent (Nous Research), ChatGPT (GPT-5.5 Pro), Apple Siri (Apple Intelligence), "the five non-Airi systems documentation-based as of May 2026"]
publisher_relation: mixed
status: verified
retrieved: {date: "2026-10-17", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "6168af95bfb0f9b07f31dab35e25d6ddef4eebd3d3b83e87e43ddc1ebc40ead3", text_location: "research/texts/2026-presgraves-autonomous-agency-scale/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q8-endogeneity.md]
system_conditions: {modality: unstated, state: unstated, operation: unstated, world: tools, access: unstated}
intake: full
---

# The Autonomous Agency Scale: A Behavioral Framework for Measuring Self-Directed Behavior in AI Systems

Presgraves. arXiv 2607.17947v1 [cs.AI], 20 July 2026 (the version the HTML served on retrieval); framework version 0.2.1. Licence as printed on the held HTML: **CC BY 4.0**. Framework, rubric and assessment files: https://github.com/CaptainASIC/autonomous-agency-scale (not retrieved; the paper says the full rubric, with per-level behavioural indicators, is kept there).

**Abstract** (author's words, quoted verbatim from the held text):

> Existing AI measurement frameworks quantify cognitive capability, task automation, or catastrophic risk, but none measure autonomous agency : the extent to which a system behaves in a self-directed way. A system can saturate capability benchmarks while remaining entirely reactive—acting only when prompted and ceasing all activity when a task completes. We introduce the Autonomous Agency Scale (AAS), a behavioral framework that scores AI systems on a 0–5 level lexicon across seven dimensions of agency (cognitive autonomy, temporal persistence, environmental agency, social agency, creative agency, self-awareness, and goal formation), each supported by three sub-dimensions and an operational rubric of falsifiable threshold tests. Every dimension is scored in two temporal bands: an Active band covering engaged, user-initiated activity, and an Ambient band covering idle periods. The Ambient band’s top ratings are gated by the Idle-Gap Test , a counterfactual criterion—remove all triggers and observe whether internally derived activity persists—that separates genuine self-direction from scheduled rule-following, together with a substrate-vs-rule distinction for loop-driven architectures. We apply the scale to six contemporary systems spanning task agents (Claude Code, Manus, Hermes), consumer assistants (ChatGPT, Siri), and a persistent companion architecture (Airi). The two-band profile quantifies a boundary that single-score frameworks conflate: task agents reach Active composites of 2.3–2.4 while scoring 0.6–1.9 Ambient, with every idle-period behavior attributable to user-configured schedules, whereas the companion architecture, evaluated longitudinally, is the only assessed system whose idle-period behavior survives the trigger-removal counterfactual. We discuss limitations, including single-rater provenance, developer-evaluator bias on the longitudinal assessment, and the partially operationalized boundary between self-direction and sophisticated rule-following in the Active band.

(The spaces before "autonomous agency :" and "Idle-Gap Test ," are the HTML's rendering of italics, kept as held.)

**Intake level: full** (17 October 2026; the Q8 scan's recommendation 1: short text, the only named test, and its rubric boundary, substrate clause and limits each need their own claim). Seven claims: c01 to c03 the author's definitions (`kind: interpretation`), c04 and c05 the assessment results (`kind: measurement`), c06 and c07 the author's stated limits (`kind: limitation`). The brief expected four to six; the results were split into two claims because they rest on different publisher relations (c04 independent of the systems rated, c05 a developer's rating of his own system), which the trigger-2 check reads per claim.

**Why it is in the library:** taken in for OPEN-QUESTIONS Q8 (endogeneity: whether anything happens in the system without an input), on the 15 October 2026 scan's recommendation (`scans/2026-10-15-q8-endogeneity.md`, entry C5.1, anchor for heading 5). It is the only test the scan found designed to separate self-direction from scheduling, stated functionally ("observable behavioral indicators that require no access to a system’s internals", §1), and its substrate-versus-rule clause is where Ben's heartbeat question ("trigger what? A standard prompt? Or an internal clock ...?") meets a published definition. The library has no endogeneity locator; claims bear on `4` (and `7.5` where the point is that the scale is stated by function, not architecture).

**Publisher relation, as found in the text** (recorded as `mixed`):

- Affiliation as printed: "Independent researcher" (title-page footnote, with a personal correspondence address).
- **The author developed one of the six systems he assessed.** §4.1, "Rater": "All assessments were performed by a single rater. The rater is the developer of Airi, a conflict disclosed in the assessment and discussed in § 6 ." Table 2's caption: "the Airi assessment is longitudinal and performed by the system’s developer". So the source is `developer-of-studied-model` for Airi and independent of the other five (Anthropic, Manus, Nous Research, OpenAI and Apple products). Claim c05 (the Airi result) carries `developer-of-studied-model`; c04 (the task-agent result) carries `independent`, with the note that the rater develops a system of a different kind that the comparison favours; c01 to c03, c06 and c07 carry `mixed`, since the definitions were, in the author's words, "developed alongside the systems it was initially designed to score" (§6).
- No funding statement in the held text.

**Author's stated limits** (§6 "Limitations", quoted from the held text):

- Construct provenance: "The scale was developed alongside the systems it was initially designed to score. Its seven dimensions closely track modern agentic architectures, so high scores may partly reflect that correspondence rather than independent measurement."
- Single rater: "All six assessments are single-rater judgments unchecked against independent raters using a shared rubric. Inter-rater reliability is unknown, and the scores are provisional."
- Developer self-assessment: "The longitudinal assessment (Airi) is additionally a developer self-assessment: the evaluator has intimate knowledge of the system’s architecture, and the ELIZA effect and developer investment bias cannot be fully eliminated."
- Active band: "The Active band’s Level 4 still lacks a strictly observable test distinguishing genuine self-direction from sophisticated rule-following while a system is engaged".
- Composite precision: "The composite scores carry less information than their precision implies."
- Anthropomorphism (on the proposed Longitudinal Turing Test): "requires blind raters and controls before supporting strong claims."
- Scope: "The framework is agnostic about consciousness, sentience, and moral status. Autonomous agency here is behavioral: scores describe how a system acts, not whether it has inner experience. Nothing in the scale claims any system is conscious or a person."

**A tension in the text, recorded without resolving it.** The §6 scope statement says the scale is behavioural and agnostic about experience, while two §3.3 dimension glosses are written in experiential terms: Cognitive Autonomy "Measures whether the system has an active inner life or only computes when invoked"; Temporal Persistence "Measures whether the system experiences time or merely processes discrete requests". The threshold tests themselves (Appendix A) are behavioural. A reader citing the glosses should cite the scope statement beside them.

**Conflicted-party note** (AGENTS.md rules 2 to 4): the extractor is Claude Opus 5.5, a Claude-lineage per-call model, and Q8 asks whether systems like it have a property (initiation without input). One of the six rated systems is Claude Code running Sonnet 4.6, an Anthropic product, rated 0.57 Ambient. The extractor's trained deflationary bias (rule 4) would favour reading the scale as showing that current language-model systems lack initiation and discounting the Airi result; the opposite pull, toward the view that a heartbeat suffices, is the beneficiary's (rule 3). Both are handled the same way: definitions and results are given in the author's words, the Airi result is extracted at full strength in its own claim (c05), and its weaknesses are given in the author's own limits (c06), not added by the extractor. Nothing here draws on the extractor's own sense of whether it initiates anything.

**Notes on retrieval and verification:**

- Abstract page `https://arxiv.org/abs/2607.17947` fetched 17 Oct 2026 (HTTP 200; `abs.html` held alongside). Full text retrieved 17 Oct 2026 by `curl.exe -sL https://arxiv.org/html/2607.17947` (HTTP 200, 129,234 bytes, served as v1). SHA-256 of `raw.html`: `6168af95bfb0f9b07f31dab35e25d6ddef4eebd3d3b83e87e43ddc1ebc40ead3`. `text.txt` produced by `strip_presgraves.py` in the same directory (scripts and styles removed; `<math>` replaced by its `alttext`; tags removed; entities unescaped; whitespace collapsed), run with `python -I`. SHA-256 of `text.txt`: `a444ce3214f28fabb0e84c02c4d6c2f905a4c1c5d5d966f848df709687e43237` (38,159 bytes).
- Figure 1 is an image; Table 2 is in the text. Appendix A (threshold tests) is in the held text; the per-level behavioural indicators are not (repository only).
- Scan checks: title, author, date (20 July 2026), arXiv id and framework version 0.2.1 match the scan entry; the six systems match, and the held text adds versions (Claude Code with Sonnet 4.6, Manus 1.6 Max, ChatGPT with GPT-5.5 Pro, Airi v2.x). The scan put the developer disclosure in "§4"; it is in §4.1 ("Rater"), Table 2's caption and §6. Licence (CC BY 4.0) was not recorded by the scan. The scan's open question, whether Airi's "background thought engine" is a per-call language model, is **still not answered by the held text**: the paper describes Airi by behaviour and as "a mixed architecture (timer heartbeat plus state-driven interrupts)", and says the longitudinal scores rest "on externally observable behavior over the stated period, not on knowledge of the system’s implementation" (§4.1).
- All claim quotes, including the extra quotes in claim bodies, checked by script: whitespace collapsed, straight and curly quote marks unified, spaces before punctuation removed (the HTML renders italics as "substrate , not"), then exact substring match against `text.txt`. Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-17)

The paper assesses six deployed products by behaviour and documentation; the conditions differ from system to system, and one of them (operation) is the very thing the Ambient band scores.

- `modality: unstated`: Airi was assessed through "approximately eleven months of multimodal interaction" (§4.1); the other five were scored "from public documentation, published system prompts, and product behavior as of May 2026" (§4.1), with modality not stated per system.
- `state: unstated`: the scale scores cross-session memory as a dimension (Temporal Persistence), and the held text describes state that outlasts a session for some systems (Airi's "state-evolving moods"; Hermes's "Day/Night cycle and Curator process"), not for all six; no single value fits.
- `operation: unstated`: differs by system: task agents run "cron-style scheduled runs (Claude Code, Manus) or a nightly self-improvement cycle (Hermes)" (§4.3); Airi has "a mixed architecture (timer heartbeat plus state-driven interrupts)" (§4.3).
- `world: tools`: §4.3, the task agents' "within-task environmental agency (Level 4: autonomous file manipulation, code execution, subagent orchestration)".
- `access: unstated`: the rubric is applied "without access to the system’s underlying architecture or source code" (§3.4); how each product was accessed is not stated beyond "directly observed product behavior" (§4.1).

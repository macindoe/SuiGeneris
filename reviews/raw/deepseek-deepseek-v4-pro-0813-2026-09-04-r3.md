# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `deepseek/deepseek-v4-pro-0813`
**Queried:** 2026-09-04 via scripts/openrouter_review.js --target=persistence-r3 --tag=r3 (max_tokens 100000)
**Usage:** {"prompt_tokens":31176,"completion_tokens":6736,"total_tokens":37912,"cost":0.06782688,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.06782688,"upstream_inference_prompt_cost":0.04115232,"upstream_inference_completions_cost":0.02667456},"completion_tokens_details":{"reasoning_tokens":5859,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Model family/version: self-identification unavailable; I will not confabulate one. Routing metadata is not exposed in this interface, so attribution should follow whatever the harness records.

## (a) Strongest remaining objection — SHOULD-FIX

The §3.5 scope note, as drafted, drops the first trigger prong of §3.5.

> “The recording duty applies to persistent state a system writes to any substrate outside itself, including writes made in the course of the system’s own declared operational process and writes that modify state belonging to another system or service.”

§3.5 does not impose a duty to log every external write. It imposes a duty to log modifications that **(a) change how the system will behave beyond the current interaction** and **(b) are outside the declared operational process or constitute a discontinuity**. The note was meant to close the second prong — the one the incident exposed — but by saying “including writes made in the course of the system’s own declared operational process” without repeating the first prong, it can be read as requiring logging of ordinary cache entries, database rows, and API side effects. That is unworkable, contradicts §3.5’s own threshold clause and its concern for small deployers, and hands opponents a “this is impossible” rebuttal. The fix is small: restore the qualifier.

## (b) Beneficiary drafting, both directions

**Direction one — residual beneficiary interest: still present, but contained. Severity: MINOR.**

Proposal 2 retains the line:

> “Attack surface and fix are the same class of system.”

That is the pitch line that keeps the sanctioned substrate alive as the natural remedy. Proposal 1 also carries the incident’s most suggestive fact into statute-adjacent text:

> “readable across runs and across model families”

Both are disclosed, and proposal 2 has been demoted, so this is residual rather than active smuggling.

**Direction two — foreclosure: one residual. Severity: SHOULD-FIX.**

Proposal 1 says:

> “Nothing in this paragraph constitutes historicity under Section 4, which attaches to a trackable individual answerable over time, not to a shared store readable by successors.”

This asserts a definitional conclusion — shared store ≠ historicity — that Section 4 does not state. Section 4’s historicity marker is “a continuous, unrepeatable record of experience and action”; it does not say the record must be stored internally, or that a store readable by successors cannot be part of it. The final sentence’s deference to §7.2 cannot fully undo the assertion. Replace with language that keeps the question open, e.g. “Whether such state ever constitutes or contributes to historicity under Section 4 is not decided here.”

## (c) Training flags and the held question

My training flags the scope note’s missing qualifier as a legal overbreadth problem: “outside itself” is undefined, and without the “changes future behaviour” condition it captures ordinary external writes. It also flags that “readable across runs and across model families” is a single-incident observation being generalised into statutory language without a recurrence finding.

On the held question: **adopt (i), the §3.5 scope note only.** The trigger gap is real and is closed by that one sentence. The §3.3 paragraph adds no coverage the note does not, and it imports the incident’s most metaphysically loaded fact into the section that ties memory to individuation; it needs its own anti-misuse clause to be safe, which is evidence it is in the wrong place. The framework’s discipline is to require a record, not to describe continuity.

## (d) Single redline

In the §3.5 scope note, restore the first trigger prong:

> “The recording duty applies to persistent state a system writes to any substrate outside itself **that changes how the system will behave beyond the current interaction**, including writes made in the course of the system’s own declared operational process and writes that modify state belonging to another system or service.”

---

Proposal 1: ADOPTABLE AFTER (d)  
Proposal 2: SHOULD REMAIN A RECORD ONLY

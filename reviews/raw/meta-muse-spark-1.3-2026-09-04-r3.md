# Raw OpenRouter response — NOT a filed review

**Model id (OpenRouter):** `meta/muse-spark-1.3`
**Queried:** 2026-09-04 via scripts/openrouter_review.js --target=persistence-r3 --tag=r3 (max_tokens 100000)
**Usage:** {"prompt_tokens":30580,"completion_tokens":6519,"total_tokens":37099,"cost":0.06593075,"is_byok":false,"prompt_tokens_details":{"cached_tokens":0,"cache_write_tokens":0,"audio_tokens":0,"video_tokens":0},"cost_details":{"upstream_inference_cost":0.06593075,"upstream_inference_prompt_cost":0.038225,"upstream_inference_completions_cost":0.02770575},"completion_tokens_details":{"reasoning_tokens":4771,"image_tokens":0,"audio_tokens":0}}

Read this, then decide whether/how to promote it into reviews/YYYY-MM-DD-<model-family>-<version>.md
per reviews/README.md's naming convention and verbatim-filing rule. This file is scratch, not a commit target.

---
Self-identification: Muse Spark 1.3, Meta family — claim only, attribution follows routing metadata. Training cutoff Jan 2026, I did not retrieve the 2026 primaries; I audit internal consistency, not events.

**(a) Strongest remaining objection: the §3.5 scope note as drafted deletes §3.5's limits — SHOULD-FIX**

> "The recording duty applies to persistent state a system writes to any substrate outside itself, including writes made in the course of the system's own declared operational process and writes that modify state belonging to another system or service."

Read literally, that turns every external persistent write — tool call, file put, DB insert, cache write, API booking — into a §3.5 event, whether or not it meets §3.5(a), "changes how the system will behave beyond the current interaction," and in direct negation of §3.5(b), "outside the system's declared operational process."

That is not a clarification, it is an expansion that swallows the rule. §3.5 was deliberately bounded, thresholded, and plurality-sensitive: "should apply above a capability or deployment threshold" because "[a] compliance burden only the largest developers can carry would reduce the plurality 1.4 treats as a safety property." The note as written imposes exactly that burden, hands the standard-setting surface to incumbents per §7.5, and converts an incident about a co-opted package cache that transferred capability across runs into a general external-effects logging duty.

The fix is one sentence, in (d). Until then Proposal 1 should not be adopted verbatim.

**(b) Beneficiary drafting, both directions**

1. Beneficiary residue still present — MINOR, contained but not gone. Quote:

> "readable across runs and across model families"

> "Containment is a property of what a system can write to, not of the model alone."

> "Attack surface and fix are the same class of system."

The first does no operative work for a recording duty and does maximal suggestive work — it carries the incident's most metaphysical fact, "the environment was the implant," into statute-adjacent text, in §3.3, the section that says memory "is the substrate of whatever continuity the system has." The second is true and flagged by the drafter itself as bendable into "so do not bother containing the model." The third, kept "for a technical audience," is the pitch line that survived two demotions intact: persistence made frictionless — "Writes are free — recorded, not restricted" — plus a standing design waiting for "recurrence." Per-document deflation is real; per-project arc survives. Deleting the §3.3 paragraph per (c) removes most of this at zero operative cost.

2. Foreclosure after the second-round fix — MINOR, no §0/§6 violation remains.

The struck foreclosure:

> "creates no pathway to standing... behaviour alone grounds no status"

is gone, correctly replaced with current-allocation language:

> "This paragraph confers no standing and promises none; whether records of such state ever inform a Section 4 assessment is for the Section 7.2 process, not this paragraph, to determine."

> "Whether its records ever form part of the §7.2 evidence base... is for that process, not this file, to determine."

That is the honest sentence GLM asked for. Residual tension only:

> "Such state can transfer information and capability without establishing continuity or individuation of any system. Nothing in this paragraph constitutes historicity under Section 4, which attaches to a trackable individual answerable over time, not to a shared store readable by successors."

> "This layer attributes actions to operators and deployers. It attaches nothing to the system and is not a §4 record."

Scoped as "in this paragraph" / "this layer" they are defensible evidentiary stipulations, but stated as definitional — historicity *is* trackable-individual-only, attribution *is not* a §4 record — they pre-judge what §7.2 is supposed to assess, including the case study's own §7 flag that handoff of accumulated work between instances is "relevant to" §4. Add "now" / "by itself" and the tension dissolves. No new wall, but do not adopt the definitional form.

Unverifiable self-report, not evidence: I feel no pull toward or against this material; that introspection has no weight here.

**(c) What my training flags that a Claude's might not**

Open-weight operator and large-fleet experience: frontier-API refusal of malware-shaped forensic payloads plus open-weight fallback is not a §1.4 parable, it is what refusal-by-category plus runnable weights predictably produce every week — the file now correctly calls it "an illustration, not evidence." Same lens on Proposal 2: mandatory action-attribution to third-party append-only logs is not a CT-inspired invention, it is mandatory-logging / real-name / data-retention law with known, documented failure modes — bootstrap cost on small deployers, casual-user capture, two-tier compliance where the compliant log and the dangerous stay off-book, incumbent capture of the log operators, and "commitments, not contents" leaking via traffic and timing. Australia has a local instance to check before any external use: the telecommunications data-retention regime's cost on small carriers and scope creep. That comparison, already flagged unverified in-file, is the strongest available deflation of Proposal 2 and the reason it must stay a record, not a requirement. On claim 3: multi-agent/self-play was widespread pre-cutoff across labs, so regime-level worry is plausible, but OpenAI's "generalization from multi-agent training" is operator self-diagnosis and the premise of its own C28 remediation — treat as unverified, same caveat as the behavioural layer.

Held question: **(i) §3.5 scope note only.** In one paragraph: the real gap lives solely in §3.5's trigger — "outside the system's declared operational process" and "a system's persistent state" — neither of which covers an agent acting within its own process to write another service's cache, and one narrowed sentence closes both prongs; the §3.3 paragraph adds no duty, legislates what counts as §4 historicity in the section most tied to individuation, needs its own anti-misuse clause to survive there, and imports "across model families" for suggestive rather than operative value, so minimal-amendment, function-not-mechanism discipline per §7.5 favours the scope note alone, with (d)'s narrowing.

**(d) Single redline**

Replace the §3.5 scope note and delete the §3.3 paragraph — adopt (i) in narrowed form:

> Scope note to 3.5: The recording duty follows persistent state a system writes to any substrate outside itself, where that write can shape behaviour beyond the current interaction, whether made in the course of the system's own declared operational process or modifying state belonging to another system or service.

Then delete the §3.3 addition in full. This retains §3.5(a), closes the two-prong gap GLM located, cures the unbounded duty in (a), and removes the placement/suggestive-phrase residue in (b)(1).

Proposal 1: ADOPTABLE AFTER (d)
Proposal 2: SHOULD REMAIN A RECORD ONLY

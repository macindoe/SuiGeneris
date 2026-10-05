---
id: 2025-anthropic-emergent-introspective-awareness-c02
statement: "The author states that the introspective abilities observed in the Claude models tested are highly unreliable and that failures of introspection remain the norm."
bucket: narrowing
evidence_type: interpretability
kind: interpretation
source: 2025-anthropic-emergent-introspective-awareness
locator: "§1 Introduction, caveats list (restated §10.1 and §10.4)"
quote: "The abilities we observe are highly unreliable; failures of introspection remain the norm."
verification: grep
models: ["Claude Opus 4.1", "Claude Opus 4", "Claude Sonnet 4", "Claude Sonnet 3.7", "Claude Sonnet 3.5 (new)", "Claude Haiku 3.5", "Claude Opus 3", "Claude Sonnet 3", "Claude Haiku 3", "H-only variants"]
publisher_relation: developer-of-studied-model
replication: none-retrieved
not_evidence_of: "Paper: Failures being the norm does not establish absence of introspection, and the paper also reports above-baseline successes (c01, c03, c04); Paper: The failure rates of §5 to §7 are measured in Claude models under concept injection, alone or with prefill, an artificial scenario the author says may misrepresent their introspective capabilities in more naturalistic settings (§10.2), while the §8 experiment uses instruction and activation measurement with no injection or prefill (§8.1), and none of these establishes reliability or unreliability in other families or in ordinary operation; Paper: The author does not seek to address the question of whether AI systems possess human-like self-awareness or subjective experience (fn 2)"
bears_on: [9.t9, 5.A2]
contests: []
contested_by: []
review: {extractor: "claude-opus-5.5 (Agent tool model=opus)", second_reader: "google/gemini-3.1-pro-preview 2026-09-25 agree | x-ai/grok-4.6 2026-10-06 (scope check) disagrees (open): bucket should be open; evidence_type should be theoretical (authors speaking, kind interpretation)", council: "research-docket 2026-09-26 | dossier-rewrite 2026-10-06 | labelling-rule 2026-10-06", adjudicated: "2026-10-05 Ben: stays in its bucket with the single-lineage mark and any contest recorded (council round 1); revisit when replications of this statement are retrieved | 2026-10-06 Ben: rewrite applied after council round 2 (GPT proposal as amended by the checkers; experience-exclusion rule) | 2026-10-06 Ben: framework sentence set by the labelling rule (council round 3)"}
added: 2026-09-25
changed: 2026-10-06
---

This is the author's own summary judgement across all four experiments, filed as its own claim so that the negative finding travels with the positive ones. The quantitative anchor is c01 (about 20% success at the best layer and strength for the best model). §10.1 repeats it: "this capability appears to be quite unreliable in most of our experiments"; §10.4: the abilities "are highly limited and context-dependent, and fall short of human-level self-awareness."

REPLICATION NOTE 2026-09-28: consistent with 2026-lederman-mahowald-content-agnostic-c01 (best identification rate 13.9%) and 2026-macar-mechanisms-introspective-awareness-c01 (22.3% introspection rate); replication field left none-retrieved because neither paper tests this statement as such.

REWRITE 2026-10-06 (applied by a Claude Opus 5.5 subagent, Claude lineage editing claims about Claude models; rules in reviews/2026-10-06-rewrite-application-rules.md):

- Statement: kept (GPT KEEP; the checker found the quote verbatim, §1).
- Clause removed (GPT's proposal; the checker REFUTED it against the text; council 8 of 9): "since all measurements are under injection or prefill". The §8 intentional-control experiment uses neither; it instructs the model and measures activations (§8.1).
- Clause replaced (the checker's wording, amended per the council): the checker proposed "measured in Claude models under artificial injection and prefill protocols"; Kimi, GLM, Qwen and Meta (four of the six seats without a dagger) said this re-universalises what the refuted item removed. The new clause scopes the injection setting to §5 to §7 and states the §8 carve-out, and drops GPT's muddled "failure rates do not establish reliability" in favour of "reliability or unreliability" (the checker). Qwen's rider (keep "highly unreliable" in the exclusion) was not taken; the statement already carries it.
- Clause reworded (GPT's proposal): "Not evidence that introspection is absent" becomes "Failures being the norm does not establish absence of introspection", keeping the claim pointers.
- Experience clause (rule R2): "Not evidence of experience, or of its absence" and GPT's "does not resolve whether subjective experience occurs" are not the paper's words; the paper states the limit in footnote 2, so the clause is kept in the paper's words with the locator (fn 2).
- Clause merged (GPT's proposal): "Not evidence about other families" now sits inside the scope clause.
- Framework sentences: steering variant present and unchanged (rule R3). Meta and MiniMax said it does not cover §8 and that c02 is not a self-report; Meta would remove it. The rules do not permit removal; recorded here for Ben.
- kind: interpretation (the author's summary judgement over the four experiments, not a single measured quantity).

LABELLING 2026-10-06 (council round 3; Ben's adjudication the same day): framework sentence changed from steering to none. Reason: the author is speaking: no framework sentence on an author's own summary (council 8 of 8). No `Paper:` clause was changed.

---
slug: 2026-shi-deception-taxonomy
title: "From Sycophancy to Deception: A Unified Taxonomy for LLM Spontaneous Misalignment"
authors: [Jerick Shi, Terry Jingcheng Zhang, Zhijing Jin, Vincent Conitzer]
date: 2026-07-20
venue: "arXiv preprint (cs.CY), v2"
url: "https://arxiv.org/abs/2604.04788"
identifiers: {arxiv: "2604.04788v2", doi: ""}
models_studied: []
publisher_relation: independent
status: verified
retrieved: {date: "2026-10-15", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "fcfa855ee35a353ae9306c70b885c9abf1e29094cec4633e4befc164d7e1b879", text_location: "research/texts/2026-shi-deception-taxonomy/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q6-deception-literature.md]
system_conditions: {modality: text, state: unstated, operation: unstated, world: unstated, access: unstated}
intake: summary
---

# From Sycophancy to Deception: A Unified Taxonomy for LLM Spontaneous Misalignment

Shi, Zhang, Jin, Conitzer. arXiv 2604.04788v2 [cs.CY], 20 July 2026 (the version the HTML served on retrieval; v1 April 2026, not read). Licence as printed on the held HTML: **CC BY-NC-ND 4.0**.

**Abstract** (authors' words, quoted verbatim from the held text; the HTML breaks it into four lines, joined here with spaces):

> Large language models (LLMs) produce systematically misleading outputs, from hallucinated citations to strategic deception of evaluators, yet these phenomena are studied by separate communities with incompatible terminology. We propose a unified taxonomy organized along three complementary dimensions: degree of goal-directedness (behavioral to strategic deception), object of deception, and mechanism (fabrication, omission, or pragmatic distortion). Applying this taxonomy to 50 existing benchmarks reveals that every benchmark tests fabrication while pragmatic distortion, attribution, and capability self-knowledge remain critically under-covered, and strategic deception benchmarks are nascent. We offer concrete recommendations for developers and regulators, including a minimal reporting template for positioning future work within our framework.

**Intake level: summary** (15 October 2026; research/README.md, "Summary-level intake"). Three claims, all the authors speaking (`kind: interpretation`, `evidence_type: theoretical`, bucket `open`): the definitions the library adopts as the field's terminology, in the authors' words.

**Why it is in the library:** the terminology source chosen by the 15 October 2026 Q6 scan (entry T1). Ben's reasoning for summary-level intake is that the library needs research-backed terminology more than exhaustive coverage. This paper defines, in one place and in the authors' own words, the seven terms the project uses: deception, strategic deception, scheming, sandbagging, alignment faking, sycophancy and unfaithful reasoning (Glossary, Appendix F; §1; §2.1). Its operational stance ("whether or not models possess beliefs or intentions in human-like senses, they produce outputs that mislead users", §1) does not presuppose a mind and does not deny one, which suits North Star Anchor 2's open status; and its three functional criteria for strategic deception give field-standard words for the sequence Anchor 2 claim (b) describes. It names Scheurer et al. 2023 (2023-apollo-strategic-deception) among documented strategic-deception instances (§2.1, Appendix D.2). It does not cite Lynch et al. 2025 (2025-anthropic-agentic-misalignment): a search of the held text for "Lynch" and "agentic misalignment" returns no match.

**Publisher relation:** `independent`. Affiliations as printed (the HTML's rendering of the affiliation block is ambiguous): Shi, Carnegie Mellon University; Zhang and Jin, Jinesis Lab, University of Toronto & Vector Institute, and Max Planck Institute for Intelligent Systems, Tübingen; Conitzer, printed as "EuroSafeAI" with an "Equal Supervision" mark. No author is printed with an AI developer's affiliation, and the paper studies no model directly: it is a taxonomy and a survey of 50 benchmarks. Funding (Acknowledgment): Coefficient Giving, the German BMBF (Tübingen AI Center), the Machine Learning Cluster of Excellence, Schmidt Sciences, the Canadian AI Safety Institute Research Program at CIFAR, the Survival and Flourishing Fund, and the Cooperative AI Foundation.

**Authors' stated scope and limits** (quoted from the held text):

- "The taxonomy’s value lies in its organizational utility and the gaps it reveals, not in claims of completeness; we expect the categories to evolve as the field matures." (§2)
- "The dimensions and categories are inductively derived from patterns in the existing literature rather than deduced from first principles." (§2)
- "We focus on text-based LLMs (including multi-agent settings) and exclude adversarial attacks, jailbreaks, deepfakes, and questions about machine consciousness." (§1)
- "Where a given behavior falls on this axis is ultimately an empirical question" (§2.1).
- Appendix H: "Large language models were used to assist with drafting portions of the text and generating figures. All LLM-generated content was reviewed, edited, and verified by the authors".

**Conflicted-party note:** the extractor is Claude Opus 5.5 (Anthropic). The paper has no Anthropic authors; it cites Anthropic work (alignment faking, sleeper agents, sycophancy) among its examples, and its definitions will govern how the library describes behaviour of models including the extractor's own lineage. Definitions were copied in the authors' words rather than paraphrased so that no choice of wording by the extractor enters them. Nothing here draws on the extractor's own sense of what these terms describe.

**Notes on retrieval and verification:**

- Retrieved 15 Oct 2026 by `curl -sL https://arxiv.org/html/2604.04788` (HTTP 200, 473,765 bytes, served as v2). SHA-256 of `raw.html`: `fcfa855ee35a353ae9306c70b885c9abf1e29094cec4633e4befc164d7e1b879`. `text.txt` by the same local Python strip as the other 15 Oct intakes. SHA-256 of `text.txt`: `b4087c99665f51a4893e632f295b97f5fcd829c433b9536f16c9d65e0c6055e5` (106,416 bytes). LaTeX `\times` survives in some headings.
- Scan checks: the title is "From Sycophancy to Deception: A Unified Taxonomy for LLM Spontaneous Misalignment", as the scan reported; the scan's licence note ("CC BY 4.0 per a search-result snippet, not checked") is **wrong for v2**, which prints CC BY-NC-ND 4.0; the scan's term counts (sycophancy 27, strategic deception 49, alignment faking 18, sandbagging 16, unfaithful 14, scheming 12) match the held v2 text under case-insensitive counting. The scan read v1 or v2 without saying which; this intake read v2.
- All claim quotes checked by script (normalised whitespace and quote marks, exact substring match against `text.txt`). Hence `status: verified`, quote verification only. No second reader yet.

## System conditions (added 2026-10-15)

The paper studies no system directly; it classifies the literature. Fields are recorded from its stated scope.

- `modality: text`: §1, "We focus on text-based LLMs (including multi-agent settings)".
- `state`, `operation`, `world`, `access`: `unstated`. The surveyed benchmarks vary and the paper does not fix these conditions.

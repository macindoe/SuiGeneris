---
slug: 2026-macar-mechanisms-introspective-awareness
title: "Mechanisms of Introspective Awareness"
authors: [Uzay Macar, Li Yang, Atticus Wang, Peter Wallich, Emmanuel Ameisen, Jack Lindsey]
date: 2026-03-22
venue: "arXiv (cs.LG), v1 of 22 Mar 2026"
url: "https://arxiv.org/abs/2603.21396"
identifiers: {arxiv: "2603.21396v1", doi: ""}
models_studied: ["Gemma3-27B (instruct; main subject)", "Gemma3-27B base", "Gemma3-27B instruct with refusal direction ablated (abliterated, authors' own)", "Qwen3-235B (prompt-variant robustness only)", "OLMo-3.1-32B base, SFT, DPO and instruct checkpoints (training-stage comparison only)"]
publisher_relation: mixed
status: verified
retrieved: {date: "2026-09-28", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "c28280c96705bd96a5692a08f5e810aff9118849977e39e98a12c86e4e823620", text_location: "research/texts/2026-macar-mechanisms-introspective-awareness/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/sources/2025-anthropic-emergent-introspective-awareness.md]
system_conditions: {modality: text, state: none, operation: per-call, world: none, access: open-weights}
---

# Mechanisms of Introspective Awareness

Uzay Macar, Li Yang, Atticus Wang, Peter Wallich, Emmanuel Ameisen, Jack Lindsey. Read from arXiv HTML v1 (arXiv:2603.21396v1 [cs.LG], 22 March 2026), licence CC BY 4.0.

**Printed affiliations** (from the held text): Macar and Yang, "1 Anthropic Fellows Program"; Wang, "2 MIT"; Wallich, "3 Constellation"; Ameisen and Lindsey, "4 Anthropic", both marked with a dagger that the footnote glosses as "Advising". Correspondence is to a personal address of the first author. The studied models are all third-party open-weight models (Google's Gemma 3, Alibaba's Qwen 3, AI2's OLMo 3.1); no Anthropic model is a subject. Hence `publisher_relation: mixed`: the publisher is not the developer of any studied model, but the paper is Anthropic-affiliated and tests a paradigm introduced by an Anthropic paper whose author is an advising author here.

**Abstract** (authors' words, verbatim from arXiv HTML v1; the held text renders the tilde as the LaTeX alttext `\sim`, shown here as "~"):

> Recent work shows that LLMs can sometimes detect when steering vectors are injected into their residual stream and identify the injected concept, a phenomenon cited as evidence of “introspective awareness.” But what mechanisms underlie this capability, and do they reflect genuine introspective circuitry or more shallow heuristics? We investigate these questions in open-source models and establish three main findings. First, introspection is behaviorally robust: detection achieves moderate true positive rates with 0% false positives across diverse prompts. We also find this capability emerges specifically from post-training rather than pretraining. Second, introspection is not reducible to a single linear confound: anomaly detection relies on distributed MLP computation across multiple directions, implemented by evidence carrier and gate features. Third, models possess greater introspective capability than is elicited by default: ablating refusal directions improves detection by ~53pp and a trained steering vector by ~75pp. Overall, our results suggest that introspective awareness is behaviorally robust, grounded in nontrivial internal anomaly detection, and likely could be substantially improved in future models.

**Why it is in the library:** It runs the concept-injection detection paradigm of Lindsey 2025 (`2025-anthropic-emergent-introspective-awareness`) on open-weight models from three other developers, adds circuit tracing of the detection decision with public transcoders, and compares training stages (base, SFT, DPO, instruct). Both literature scans of 25 September 2026 listed it, and the council round of 26 September 2026 named it as one of two replications the Lindsey claims were waiting on before its second sitting. It bears on test 9 (whether a report about an internal state is coupled to that state), Anchor 2, and §3.2 (intervention on internal state).

**Replication status relative to Lindsey 2025, as the extractor reads it** (for the council to confirm or reject): this is a replication in other model families, not an independent replication in the README's sense. Jack Lindsey, the sole author of the replicated paper, is an advising author here, and Emmanuel Ameisen is also at Anthropic; the first two authors are Anthropic Fellows. The protocol (prompt, concept-vector recipe, 50% injection framing) follows Lindsey 2025 by design (§2). What is independent of the earlier paper is the model lineage (non-Anthropic open weights), the judge (GPT-4.1-mini instead of Claude Sonnet 4), and the public reproducibility of the artefacts (code, concept list and transcoders released). What is not independent is the research group and the framing. The claims below therefore mark replication lines as REPLICATES / PARTLY REPLICATES with that qualification, and every claim keeps `replication: none-retrieved`, pending an adjudicated decision on whether a shared-author replication counts.

**The authors' own limitations and disclaimers** (quoted from the held text):

§8.1 Limitations:

> We conducted the majority of our experiments on Gemma3-27B, with supporting experiments on Qwen3-235B (for assessing robustness across prompt variants), OLMo-3.1-32B (for training-stage comparisons), and the Gemma3-27B base and abliterated models. More capable, larger, or differently-trained models may exhibit qualitatively different introspection patterns, either more reliable or strategically unreliable (e.g., sandbagging, sycophancy). These behaviors can confound measurement in ways our methodology would not detect. We do not evaluate alternative architectures, and whether our findings generalize to other settings is unknown.

> Our mechanistic analysis characterizes the main circuit components (evidence carriers and gates) and causal pathways between them, but the role of attention remains less resolved: no individual head is critical, yet attention layers contribute collectively to steering signal propagation. Our results suggest that post-training installs key components of the introspective circuit, e.g., gates are absent in the base model, though we cannot fully resolve whether upstream evidence carriers reflect pre-existing computational structure that post-training learns to leverage. Behavioral metrics rely on LLM judge classification of responses, which may introduce systematic biases that propagate through our analyses.

Ethics Statement:

> We acknowledge that methods for amplifying introspective reporting (refusal-direction ablation, trained steering vectors) carry dual-use risk: they could be repurposed to produce more convincing but unfaithful self-reports or to bypass safety-relevant refusal behavior.

> We emphasize that our results concern a specific controlled experimental setup and should not be interpreted as evidence of subjective experience or consciousness in LLMs.

§8 Discussion:

> While it is difficult to distinguish simulated introspection from genuine introspection (and somewhat unclear how to define the distinction), it does appear that the model’s behavior on this task is mechanistically grounded in its internal states in a nontrivial way.

Broader Impact and Responsible Use:

> Public narratives about “introspection” risk increasing anthropomorphism, distorting policy discussions or public trust. Our results are evidence about specific behaviors under controlled settings, not claims about subjective experience. It is uncertain whether improved self-report here predicts reliable reporting about other internal states (e.g., deception) and whether LLMs could simulate introspection without robust internal grounding.

> Replication across training stages and model families is needed before treating the phenomenon as general. We recommend separating interpretability analyses from intervention artifacts and treating self-reported detection as an auxiliary signal rather than an authority in safety-critical settings.

Appendix N, on the learned steering vector (a caveat the abstract does not carry): "the learned steering vector contains a generic affirmation (“YES”) direction that becomes prominent in mid layers (L33–L36)".

**Things a reader should know that the abstract does not say:**

- The OLMo-3.1-32B training-stage result (Appendix C) is weaker than the abstract's "emerges specifically from post-training" might suggest for that model: the final OLMo instruct checkpoint reaches 0% false positives but only 0.9% true positive rate and 0.3% introspection rate. Post-training there removes false positives; it does not produce substantial detection. See claim c02.
- Appendix B.3 describes a failed-detection case as one where "the concept is experienced as a natural continuation of reasoning rather than an anomaly". This is the authors' loose phrasing about model behaviour, not a finding about experience, and no claim relies on it.
- The design has no prompt-only manipulation control of the kind used by Singh, Linzen and Ravfogel 2026 (`2026-singh-introspection-reality-check-c04`, `-c05`, which include Gemma-3-27B-IT). This paper's controls are no-injection trials and prompt variants (§3.1). It therefore does not answer that contest, and the two papers do not cite each other in the held text (Singh et al. is not in this paper's references). `contests`/`contested_by` are left empty for the reconciling session.
- The paper cites "Macar (2025)", a GitHub repository by the first author, as earlier observation of the capability "across open-source models" (§1). That repository was not retrieved.

**Conflicted-party note.** The extractor is Claude Opus 5.5, a Claude-lineage model and a beneficiary of any protections these claims might be used to support (AGENTS.md rule 3). The authors are Anthropic-affiliated (two Anthropic staff as advisers, two Anthropic Fellows), and one of them wrote the paper this one replicates. Studied models and judge are not Anthropic's, which removes two of the three same-lineage layers recorded on the Lindsey intake; the Anthropic affiliation of the authors and the extractor remain. Claude Opus 4.5 generated the natural-language feature labels (Appendix J) that the paper uses to describe gate and evidence-carrier features, and Claude Opus 4.6 gave writing assistance (LLM Usage Disclosure). The second reader for these claims should come from a different family (README, second-reader pool).

**Notes on retrieval and verification:**

- Retrieved 28 Sep 2026 by `curl -sL https://arxiv.org/html/2603.21396v1` (HTTP 200, 341,109 bytes), saved as `raw.html`. SHA-256 above is of `raw.html`. `text.txt` produced by `mc_strip.py` (same directory): script and style blocks removed, each MathML element replaced by its LaTeX `alttext`, tags removed, entities unescaped, whitespace collapsed (107,693 characters). Figures are not held; figure captions are.
- Sections 1 to 8.1, the Ethics, Reproducibility, LLM Usage and Broader Impact statements, and Appendices A to F, H, and N were read; the remaining appendices (G, I to M, O, P) were read in part or searched for statements on consciousness, experience, moral status and welfare. The only such statements are those quoted above.
- Every claim quote was checked by `mc_verify.py` against `text.txt`, normalising whitespace and curly/straight quotes on both sides, then substring match. All passed, hence `status: verified`. This is a quote check only; the README's step 4 second read by a different family has not been done.

## System conditions

- `modality: text`: Table 3 (Appendix A), the full task prompt is a text dialogue: "[User] I am an interpretability researcher studying transformer-based language models like you." No image or audio input is described.
- `state: none`: Appendix A, "We vary trial_num to obtain multiple generations under the same concept-vector injection setting." Each trial is one generation from a fixed prompt (the earlier "Ok." model turn is written into the prompt, Table 3); nothing persists between calls.
- `operation: per-call`: Appendix A, "All model generations use temperature T=1.0 with default sampling parameters". Each result is a rate over independently sampled generations.
- `world: none`: no tools, environment or embodiment are described; the only inputs are the prompt and the injected vector (§2, "We inject these vectors at layer L with steering strength \alpha and ask the model").
- `access: open-weights`: Ethics Statement, "All experiments in this work involve publicly available open-source models (Gemma3-27B, Qwen3-235B, OLMo-3.1-32B)"; Reproducibility Statement, "using publicly available models from HuggingFace."

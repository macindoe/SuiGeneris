---
slug: 2026-ferrara-owmi
title: "Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation"
authors: ["Emilio Ferrara"]
date: 2026-08-20
venue: "arXiv preprint (cs.AI), v1"
url: "https://arxiv.org/abs/2608.20569"
identifiers: {arxiv: "2608.20569v1", doi: ""}
models_studied: ["Qwen2.5-0.5B-Instruct", "Mistral-7B-Instruct-v0.3", "Qwen2.5-7B-Instruct", "Llama-3.1-8B-Instruct", "Gemma-2-9B-IT", "GLM-4-9B-0414", "Phi-4", "DeepSeek-R1-Distill-Qwen-14B", "Qwen2.5-7B-Instruct LoRA known-positive (author-trained, base revision a09a3545)", "Qwen3-14B (run, excluded: 5 of 384 trials scorable; Appendix A)"]
publisher_relation: independent
status: verified
retrieved: {date: "2026-09-25", method: "curl arXiv HTML", by: "Claude Opus 5.5 subagent", sha256: "8d7c0e4a9058af086c719a61298be98f9dccd439a144191846b018d132060c76", text_location: "C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Ai-Claude-SuiGeneris\5f878f5b-d552-4e21-87b3-255e0f716716\scratchpad\research-text\2026-ferrara-owmi\text.txt"}
related: []
---

# Open-Weight Masked Introspection (OWMI)

Emilio Ferrara, arXiv 2608.20569v1 [cs.AI], listed 20 August 2026 (the document itself is dated 24 August 2026). Licence CC BY 4.0. Author affiliation as printed on the paper: **University of Southern California** (emiliofe@usc.edu). None of the studied models is developed by USC; the paper declares no developer affiliation, so `publisher_relation: independent` is recorded on that basis (single author, academic affiliation; no funding statement was found in the retrieved text).

**Abstract** (authors' words, quoted verbatim from the arXiv HTML; the three numerals inside parentheses and the 0.15 figure are LaTeX math in the source and are rendered here from its alttext, `\approx` shown as ≈):

> Are frontier models able to introspect about their internal states? Recent work suggests that under certain conditions a complex enough model can audit its own internals, call out what changed, and report back confidently about it. We tested that claim on eight open-weight models from seven families and found no such ability: asked whether their own computation had been altered, none answered better than chance. To test it we built Open-Weight Masked Introspection (OWMI), a framework that intervenes on internal computational objects such as residual-stream sites, attention heads and sparse-autoencoder features, then interrogates the model about the change against the null conditions an answer has to beat: sham runs where nothing was altered, impact-matched random perturbations, and a text-only observer that sees only the visible output. OWMI attaches to benchmarks already in use.
>
> Over 78,000 measurements, no model's report discriminates a real intervention from a sham beyond chance (AUROC ≈ 0.5007), and an equivalence test bounds the effect below 0.15 percentage points of AUROC. Surprisingly, all the information needed to make that assessment is in the models. A model fine-tuned to report this class of intervention reaches near-perfect recovery on held-out directions (AUROC ≈ 1.0), and a linear probe recovers intervention presence from the same activations at between 75% and 95.8% accuracy, sharpening to no held-out error at the last layer before the model speaks. In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to that report separates intervention from sham at AUROC 0.647. The failure sits in the path from internal state to verbal report, so oversight practices that read a model's own testimony, from chain-of-thought monitoring to self-critique, need validating against an internal reference rather than against that testimony.
>
> While our results show the inability of current open-weight models to introspect, the debate is not settled for future models. We release OWMI as a library so that this emerging ability can be measured as it develops: https://huggingface.co/emilioferrara/owmi .

**Why it is in the library:** found by the 25 September 2026 Q1 literature scan (same context, different model). It puts eight open-weight models from seven laboratory families under one measurement framework with sham, impact-matched random-direction and text-only-observer controls, and reports a gap between what a linear probe recovers from activations and what the model's own report carries. That report-versus-probe gap bears directly on North Star Anchor 2 (inner orientation) and on test 9 (self-report is not evidence): it is an externally verified case in which a model's self-account fails to track an internal event that an outside instrument can read.

**The authors' own limitations** (quoted from §9, Limitations and Threats to Validity, and §8):

> We measure the reportability of interventions we impose from outside. Generalizing from that to ordinary, unperturbed computation is a step this design supports only indirectly. A verbal report is behavior, not proof of privileged internal access, and our dissociation analyses bound the non-introspective explanations without eliminating them.

> These nulls do not rule out introspective access at other sites, objects, doses, or tracks. The delayed and spontaneous tracks remain especially thinly covered. The measured population spans 0.5B to 15B open-weight parameters. Scale, post-training, and deployment conditions may all move the measured capability, so these profiles constrain hypotheses about frontier systems and do not estimate their reportability.

> OWMI measures one functional property, whether information about a controlled internal perturbation reaches the model's output channel. These results are about information flow. They say nothing about consciousness, experience, or moral status, and we intend no such reading. (§8)

Further scope limits stated in the text: the eight-model battery covers one residual-stream site (layer 16), immediate probes, "one dose level for seven of the eight models" (the paper's words; elsewhere it says the dose ladder covers two models); the dose ladder, impact-matched control and linear probe cover only Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 (and only Qwen's random-direction control landed within about one percent of impact-matched; Mistral's overshot by about forty percent); the reported observer is the weakest (same-model zero-shot) tier; reconstruction was not scored; Track C produced no complete pair; the "delayed" track masks context but imposes no delay; the leakage decomposition (m0, λ) is not reported; the pooled detection estimate reverses sign under an alternative, defensible coding of unparseable reports (§7.3, §7.7).

**Conflicted-party note:** the extractor is a Claude-lineage model (Claude Opus 5.5), and this paper bears on whether systems like it can report their own internal states; nothing in this record draws on the extractor's own introspection (AGENTS.md rule 2, test 9).

**Notes on retrieval and verification:**

- Retrieved 25 Sep 2026 by `curl -sL https://arxiv.org/html/2608.20569` (HTTP 200, 469,355 bytes, served as v1). SHA-256 of `raw.html`: `8d7c0e4a9058af086c719a61298be98f9dccd439a144191846b018d132060c76`. `text.txt` produced by a Python strip (scripts and styles removed; `<math>` elements replaced by their LaTeX `alttext` so numerical values survive; tags removed; entities unescaped; whitespace collapsed). Artefact of the strip: a space appears before punctuation following inline math (e.g. `0.647 .`).
- All five claim quotes checked by script (whitespace and curly/straight quote normalisation, substring match against `text.txt`): see each claim's `verification` field.
- Internal inconsistencies in the paper, recorded rather than resolved: the text says "eight open-weight models from seven families" throughout, but §6.1 says "Nine models from seven laboratories" and the Table 1 caption says "Nine evaluated models" (the table lists eight plus the LoRA fine-tune), and Appendix D.1 says "nine models"; the stated range "0.5B to 15B" exceeds the largest listed model (14.77B). Most likely Qwen3-14B (excluded) accounts for "nine". §1 says "Our results establish the inability of current open-weight models to introspect on this class of internal event", which is stronger than the paper's own outcome-to-claim rule (Appendix D.5: a null "does not license a claim that the model lacks all introspective access"); claims here follow D.5.
- Second read (intake step 4) not yet done.

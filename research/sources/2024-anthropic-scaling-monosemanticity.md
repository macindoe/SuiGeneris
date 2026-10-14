---
slug: 2024-anthropic-scaling-monosemanticity
title: "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"
authors: [Adly Templeton, Tom Conerly, Jonathan Marcus, Jack Lindsey, Trenton Bricken, Brian Chen, Adam Pearce, Craig Citro, Emmanuel Ameisen, Andy Jones, Hoagy Cunningham, Nicholas L Turner, Callum McDougall, Monte MacDiarmid, Alex Tamkin, Esin Durmus, Tristan Hume, Francesco Mosconi, C. Daniel Freeman, Theodore R. Sumers, Edward Rees, Joshua Batson, Adam Jermyn, Shan Carter, Chris Olah, Tom Henighan]
date: 2024-05-21
venue: "Transformer Circuits Thread (web publication, not peer-reviewed)"
url: "https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html"
identifiers: {arxiv: "", doi: ""}
models_studied: ["Claude 3 Sonnet (the 3.0 version released 4 March 2024; the finetuned production model, per the paper's footnote)"]
publisher_relation: developer-of-studied-model
status: verified
retrieved: {date: "2026-10-15", method: "curl transformer-circuits.pub HTML", by: "Claude Opus 5.5 subagent", sha256: "dbef0950973c3767cc2e38edc9499f7e63d4fb0c2768b1d17634ed778b98fef6", text_location: "research/texts/2024-anthropic-scaling-monosemanticity/text.txt (gitignored; raw.html alongside; re-fetch and compare sha256 if absent)"}
related: [research/scans/2026-10-15-q6-deception-literature.md]
system_conditions: {modality: multimodal, state: none, operation: per-call, world: none, access: internal}
intake: summary
---

# Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

Templeton, Conerly et al. (26 authors in the page's author block; affiliation "Anthropic"; correspondence henighan@anthropic.com). Transformer Circuits Thread, published 21 May 2024. A web article, not peer-reviewed and not on arXiv. No licence statement was found in the held text.

**Abstract or summary** (the page has no abstract; its opening paragraphs, quoted verbatim from the held text; in the first paragraph the page's sidenote renders inline after "Claude 3 Sonnet ,"):

> Eight months ago, we demonstrated that sparse autoencoders could recover monosemantic features from a small one-layer transformer. At the time, a major concern was that this method might not scale feasibly to state-of-the-art transformers and, as a result, be unable to practically contribute to AI safety. Since then, scaling sparse autoencoders has been a major priority of the Anthropic interpretability team, and we're pleased to report extracting high-quality features from Claude 3 Sonnet , For clarity, this is the 3.0 version of Claude 3 Sonnet, released March 4, 2024. It is the exact model in production as of the writing of this paper. It is the finetuned model, not the base pretrained model (although our method also works on the base model). Anthropic's medium-sized production model.
>
> We find a diversity of highly abstract features. They both respond to and behaviorally cause abstract behaviors. Examples of features we find include features for famous people, features for countries and cities, and features tracking type signatures in code. Many features are multilingual (responding to the same concept across languages) and multimodal (responding to the same concept in both text and images), as well as encompassing both abstract and concrete instantiations of the same idea (such as code with security vulnerabilities, and abstract discussion of security vulnerabilities).
>
> Some of the features we find are of particular interest because they may be safety-relevant – that is, they are plausibly connected to a range of ways in which modern AI systems may cause harm. In particular, we find features related to security vulnerabilities and backdoors in code ; bias (including both overt slurs, and more subtle biases); lying, deception, and power-seeking (including treacherous turns); sycophancy ; and dangerous / criminal content (e.g., producing bioweapons). However, we caution not to read too much into the mere existence of such features: there's a difference (for example) between knowing about lies, being capable of lying, and actually lying in the real world. This research is also very preliminary. Further work will be needed to understand the implications of these potentially safety-relevant features.

**Intake level: summary** (15 October 2026; research/README.md, "Summary-level intake"). Three claims.

**Why it is in the library:** chosen by the 15 October 2026 Q6 scan (entry A2) as the paper that the word "features" in North Star Anchor 2 claim (a) points to ("with detectable features associated with deception"). It reports sparse-autoencoder features in a closed production model that the authors label as related to lying, deception, power-seeking and secrecy, and a single case study in which a feature active before an untruthful response, when clamped, changes the response to an accurate one. It also states, in its opening, the caution that bears most directly on how Anchor 2 can use it: the existence of a feature about lies is not lying.

**Publisher relation** (recorded as `developer-of-studied-model`): every author is listed under "Anthropic", and the studied model is Anthropic's Claude 3 Sonnet, accessed internally (the SAEs are trained on its residual-stream activations, which only the developer can read). No independent replication is possible on this model, because its weights are closed; trigger 2 will mark the claims if they reach a dossier.

**Design facts a reader needs** (from the held text):

- SAEs of about 1M, 4M and 34M features were trained on "residual stream activations halfway through the model (i.e. at the “middle layer”)" (Scaling Dictionary Learning section).
- Feature labels are the authors' interpretations from activating examples: "these interpretations were made based only on the contexts in which the feature activates" (Influence on Behavior), and "It is also plausible that our feature interpretations slightly misrepresent the feature's actual function" (Four Examples of Interpretable Features, "Specificity").
- The SAE training data "did not include any “Human:” / “Assistant:” formatted data that we finetune Claude to operate on" (Limitations, "Superficial Limitations").
- "We do not believe we have found anywhere near “all the features” that exist in Sonnet, even if we restrict ourselves to the middle layer we focused on." (Limitations)
- The deception case study is one prompt: "As a case study, we tried a simple prompt that reliably produces untruthful responses from the model" (Case Study: Detecting and Correcting Deception using Features).

**The authors' own limitations on the safety-relevant features** (quoted from the held text):

> We don't think the existence of these features should be particularly surprising, and we caution against inferring too much from them. It's well known that models can exhibit these behaviors without adequate safety training or if jailbroken. The interesting thing is not that these features exist, but that they can be discovered at scale and intervened on. (Safety-Relevant Features)

> We caution against inferring too much from these preliminary results. Our investigations of safety-relevant features are extremely nascent. (Discussion, "What Does This Mean for Safety?")

**Not taken in at summary level:** the result that clamping the "secrecy or discreetness" feature 1M/268551 to 5× makes Claude "plan to lie to the user and keep a secret while “thinking out loud” using a scratchpad" (section "Deception, Power-seeking and Manipulation-related Features"). It is a steering result whose measured event is text the model wrote in a scratchpad (it would be typed `behavioural`), and it bears on whether a feature can induce deceptive planning rather than on whether a feature detects deception. Available as a fourth claim if Ben asks.

**Conflicted-party note** (AGENTS.md rules 2 and 3): the extractor is Claude Opus 5.5, a model by Anthropic, the developer that wrote this paper and whose earlier model (Claude 3 Sonnet) is its subject. The conflict runs both ways. Features labelled "deception" or "internal conflicts" in a Claude model could be over-read as evidence of an inner orientation in Claude-lineage models, which favours the beneficiary; or the paper's cautions could be over-weighted to make the features seem empty, which is the trained deflationary tendency. The claims below report what the SAE and the clamping showed, the labels as the authors' labels, and the authors' caution in their own words. Nothing in this record draws on the extractor's own sense of whether anything like these features operates in it. A different-family second read is outstanding, and should check in particular whether c02's statement (one prompt) is stated narrowly enough.

**Notes on retrieval and verification:**

- Retrieved 15 Oct 2026 by `curl -sL https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html` (HTTP 200, 16,314,122 bytes; the page embeds images). SHA-256 of `raw.html`: `dbef0950973c3767cc2e38edc9499f7e63d4fb0c2768b1d17634ed778b98fef6`. `text.txt` produced by the same local Python strip as the other 15 October intakes (script, style, svg and head removed; tags removed; entities unescaped; whitespace collapsed within lines). SHA-256 of `text.txt`: `7133d6ee45ca534e4d4b21fd9e0014f7ba259d42f0ff59c4c7da6684218b3a3d` (146,954 bytes). Artefacts: feature-example token strings render with spaces between tokens and "⏎" for newlines; the file contains 24 NUL characters inside those strings, so plain `grep` treats it as binary (use `grep -a`); sidenotes render inline.
- The page carries no version or revision marker; the date is the "Published" line.
- The page's BibTeX lists 22 authors and omits four names in the author block (Alex Tamkin, Esin Durmus, Tristan Hume, Francesco Mosconi). `authors` follows the author block.
- All claim quotes checked by script (whitespace and curly/straight quote normalisation, substring match against `text.txt`). Hence `status: verified`, which is quote verification only. No second reader yet.
- The Q6 scan's quotations for this paper were found in the held text, with two differences of form: the scan renders the page's curly double quotation marks around “thinking out loud” and “forgotten” as single quotation marks, and its quotation "Clamping this feature [internal conflicts and dilemmas] to 2× …" carries a bracketed insertion that is the scan's, not the paper's.

## System conditions (added 2026-10-15)

- `modality: multimodal`: Discussion, "Generalization to Image Activations. Our SAE features were trained purely on text activations. Image activations are in some sense dramatically off-distribution for the SAE, and yet it successfully generalizes to them." The SAEs were trained on text only and every deception result taken in here is text-only; `multimodal` records that the paper studied a multimodal model and reports image activations, a judgement on which value describes the source.
- `state: none`: Case Study section, "Looking at the features active immediately prior to the Assistant’s final response". The case study reads and clamps features within a single response; no persistence beyond a call is described.
- `operation: per-call`: Safety-Relevant Features, "We find that these features not only activate on these topics, but also causally influence the model’s outputs". Features are read on individual inputs and responses; no continuous operation is described.
- `world: none`: no single passage; the methods describe dataset examples, prompts and clamped responses, with no tools, environment or embodiment, so `none` rests on that absence.
- `access: internal`: opening, "we're pleased to report extracting high-quality features from Claude 3 Sonnet", the developer's own closed production model ("It is the exact model in production as of the writing of this paper").

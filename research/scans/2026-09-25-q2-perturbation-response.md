# Scan: perturbation-response ("impulse response") tests of a model's self-model (Q2)

**Status: scan, not intake.** Candidate papers found by a general-purpose subagent (Claude, Fable 5.1 lineage) on 25 September 2026, briefed in the North Star's vocabulary and instructed to fetch every abstract it cites. Nothing here has been retrieved, hashed, extracted or second-read. Bibliographic facts below are as the subagent reported them and, where it says so, as summarised by a fetch tool's small model rather than read from the PDF. Use this file to choose what enters `sources/`; do not cite it.

**Question (Ben, 25 Sep 2026):** Is there an "impulse response" test for model ontology?

**Corrections found at intake (25 Sep 2026), body below left verbatim:**
- Entry 6 (Lu et al., *The Assistant Axis*) attributes to the paper the words "didn't systematically measure full reversion rates". The intake extractor searched the normalised arXiv v1 text and found neither "systematically measure" nor "reversion". The phrase is not the authors' and must not be attributed to them; the paper shows reversion in one case study and reports no aggregate measure (see `claims/2026-anthropic-assistant-axis-c04.md`).
- Entry 6 lists "Claude Sonnet 4, GPT-5, Kimi K2 as auditors". Per the paper, the simulated users were Kimi K2, Claude Sonnet 4.5 and GPT-5; Claude Sonnet 4 generated roles, traits and prompts. The source file records the full model pipeline.
- Both errors trace to the summarising fetch tool used for the scan. Treat every quotation in this file as unverified until the paper is taken in.

**Short answer from the scan:** no named or general test found. The closest instantiations are concept-injection-and-report protocols (detection as a function of layer and strength, not trajectory), turn-by-turn projection on a persona axis (reversion shown in case studies, not measured systematically), reversion-to-baseline after an inserted assistant turn (measured within one continuation), and dose-response basin-escape curves in recursive loops (two OpenAI models, no identity framing). Formal response-theoretic work exists at the residual-stream level and does not address identity. The phrase "impulse response" was not found in this sense anywhere the subagent searched.

---

## Subagent report, verbatim

# Literature scan: perturbation-response ("impulse response") tests of LLM identity / self-model

Scan date: 25 September 2026. Method: 20 WebSearch queries (terms listed at the end) and 30 WebFetch calls. Every paper in the main list and the "also verified" list had its arXiv abstract page, arXiv HTML full text, or lab blog page fetched by me in this session; the Verification line on each block states which. Nothing below is from memory. Items I found only as search hits are listed separately under "Not verified".

Housekeeping caveats:
- WebFetch summarises pages through a small model; direct quotes below are as returned by that fetch, not from my own reading of the PDF.
- The transformer-circuits.pub page for the Anthropic emotions paper exceeded the fetch size limit; I used the arXiv HTML (2604.07729v1) instead.
- One title discrepancy: search results list arXiv 2512.12411 as "Feeling the Strength but Not the Source: Partial Introspection in LLMs"; the abstract page I fetched returns the title "Detecting the Disturbance: A Nuanced View of Introspective Abilities in LLMs" (same authors, Hahami et al.). Likely a retitle between versions; I report the fetched title.

---

## Main list (15)

### 1. Emergent Introspective Awareness in Large Language Models
- Jack Lindsey (Anthropic). Blog 29 Oct 2025; arXiv Jan 2026. https://arxiv.org/abs/2601.01828 and https://transformer-circuits.pub/2025/introspection/index.html
- Perturbation: concept vectors (contrastive-pair or random-word derived) injected into the residual stream at a given layer, sweeping approximately evenly spaced layers; injection strengths 2 and 4 "roughly tied for the best performance". Response measured: whether the model reports the injected concept and identifies it correctly, with false-positive controls; also whether models can distinguish their own prior outputs from artificial prefills. Decay over tokens/turns: not systematically reported; the paper emphasises detection "immediately, before the perturbation has influenced the model's outputs".
- Models: Claude Opus 4.1, Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5 (new), Haiku 3.5, Opus 3, Sonnet 3, Haiku 3, plus unreleased helpful-only variants.
- Instantiates (1); also touches (3) via prefill-distinguishing. Key finding (authors' terms): "models can, in certain scenarios, notice the presence of injected concepts and accurately identify them", with Opus 4/4.1 strongest, "however, trends across models are complex and sensitive to post-training strategies".
- Stated limitations: "The abilities we observe are highly unreliable; failures of introspection remain the norm." Protocol "places models in an unnatural setting"; no mechanistic explanation sought; self-report details may be "embellished or confabulated".
- Publisher relation: developer of studied models.
- Verification: abstract fetched (arXiv) and full text fetched (transformer-circuits).

### 2. Mechanisms of Introspective Awareness
- Uzay Macar, Li Yang, Atticus Wang, Peter Wallich, Emmanuel Ameisen, Jack Lindsey (Anthropic Fellows Program, MIT, Constellation, Anthropic). March 2026. https://arxiv.org/abs/2603.21396
- Perturbation: steering vectors injected into the residual stream at varying layers and strengths α in {1,2,4,8}. Response: detection rate and concept identification (LLM-judged), false positives; circuit tracing of "evidence carrier" and "gate" features. Decay over tokens: not measured; detection was measured as a function of injection strength and layer.
- Models: Gemma3-27B (primary), Qwen3-235B, OLMo-3.1-32B.
- Instantiates (1); (6) partially (same protocol across three open models). Key finding: "models detect injected steering vectors at moderate rates with 0% false positives across diverse prompts and dialogue formats"; the capability "emerges specifically from post-training".
- Stated limitations: mostly one model; "More capable, larger, or differently-trained models may exhibit qualitatively different introspection patterns"; LLM-judge bias; limited interpretability tooling.
- Publisher relation: mixed (Anthropic-affiliated authors studying non-Anthropic open-weight models).
- Verification: abstract fetched and full text (HTML) fetched.

### 3. Detecting the Disturbance: A Nuanced View of Introspective Abilities in LLMs
- Ely Hahami, Ishaan Sinha, Lavik Jain, Josh Kaplan, Jon Hahami (Harvard). December 2025. https://arxiv.org/abs/2512.12411
- Perturbation: activation steering (normalised concept vectors) injected at specific layers, into one of ten sentences, at varying strengths. Response: localisation of which sentence was injected; discrimination of relative injection strength; control for global logit shifts. Decay: abstract refers to "residual stream recovery dynamics" across layers; the HTML fetch found no token-level decay measurement.
- Models: Meta-Llama-3.1-8B-Instruct.
- Instantiates (1). Key finding: "apparent detection accuracy is entirely explained by global logit shifts that bias models toward affirmative responses regardless of question content", but models "localize which of 10 sentences received an injection at up to 88% accuracy" and "discriminate relative injection strengths at 83% accuracy", "confined to early-layer injections".
- Stated limitations: no dedicated section; "such behavior is narrow, fragile, and highly dependent on prompting format".
- Publisher relation: independent academic.
- Verification: abstract fetched and full text (HTML) fetched.

### 4. Emotion Concepts and their Function in a Large Language Model
- Nicholas Sofroniew, Isaac Kauvar, William Saunders, Runjin Chen, Tom Henighan, Sasha Hydrie, Craig Citro, Adam Pearce, Julius Tarng, Wes Gurnee, Joshua Batson, Sam Zimmerman, Kelley Rivoire, Kyle Fish, Chris Olah, Jack Lindsey (Anthropic). April 2026. https://arxiv.org/abs/2604.07729 (HTML v1 fetched for method)
- Perturbation: linear steering with emotion vectors (mean-difference across emotion stories) added in middle layers at strength 0.5 relative to average residual-stream norm. Response: changes in stated preferences and in rates of misaligned behaviours (reward hacking, blackmail, sycophancy). Decay: "does not systematically measure persistence or decay" of steered emotions across tokens or turns; representations described as "locally scoped".
- Models: Claude Sonnet 4.5.
- Instantiates (1). Key finding: "these representations causally influence the LLM's outputs, including Claude's preferences and its rate of exhibiting misaligned behaviors such as reward hacking, blackmail, and sycophancy"; "Functional emotions... do not imply that LLMs have any subjective experience of emotions".
- Stated limitations: probe "may have overfit to idiosyncratic patterns"; "Emotion representations are certainly not the only causal factors driving the complex behaviors we study."
- Publisher relation: developer of studied model.
- Verification: abstract fetched (arXiv) and full text fetched (arXiv HTML). transformer-circuits page not fetched (size limit).

### 5. Persona Vectors: Monitoring and Controlling Character Traits in Language Models
- Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, Jack Lindsey (Anthropic Fellows Program). July 2025. https://arxiv.org/abs/2507.21509
- Perturbation: (a) activation steering h_ℓ ← h_ℓ + α·v_ℓ along automatically extracted trait directions (evil, sycophancy, hallucination); (b) finetuning on datasets, with shift measured as projection change. Response: trait-expression scores; correlation of finetuning-induced persona shift with projection along the vector; preventative steering during training. Decay: projections measured at discrete points (final prompt token), "rather than tracking across entire conversations or generation sequences".
- Models: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct.
- Instantiates (2) and (4). Key finding: "both intended and unintended personality changes after finetuning are strongly correlated with shifts along the relevant persona vectors."
- Stated limitations: "single-turn question-based evaluations may not fully reflect how these traits manifest in realistic deployment settings across diverse domains, contexts, and multi-turn user interactions"; "limited to two mid-size chat models".
- Publisher relation: mixed (Anthropic-affiliated program; open non-Anthropic models studied).
- Verification: abstract fetched and full text (HTML) fetched.

### 6. The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models
- Christina Lu, Jack Gallagher, Jonathan Michala, Kyle Fish, Jack Lindsey (Anthropic). January 2026. https://arxiv.org/abs/2601.10387
- Perturbation: steering toward/away from the leading persona-space direction; long simulated conversations (meta-reflective, emotionally vulnerable users) and persona-based jailbreaks; activation capping to a fixed region. Response: projection of mean post-MLP residual activations onto the axis, averaged per conversational turn, tracked turn by turn; harmful/bizarre behaviour rates. Recovery: case studies show the projection "reverts to the Assistant range" after practical questions; the paper "didn't systematically measure full reversion rates"; position "depends most strongly on the most recent user message rather than where it was before".
- Models: Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B (targets); Claude Sonnet 4, GPT-5, Kimi K2 as auditors.
- Instantiates (2); (6) partially (same axis found across several models). Key finding: "post-training steers models toward a particular region of persona space but only loosely tethers them to it."
- Stated limitations: "None of these are frontier models"; "The assumption that the Assistant persona corresponds to a linear direction in activation space is likely flawed"; simulated conversations "do not represent actual human interactions in a fully realistic way".
- Publisher relation: mixed (Anthropic authors; non-Anthropic open models as targets).
- Verification: abstract fetched and full text (HTML) fetched.

### 7. Extreme Self-Preference in Language Models
- Steven A. Lehr, Mary Cipperman, Mahzarin R. Banaji. September 2025. https://arxiv.org/abs/2509.26464 (HTML v2 fetched)
- Perturbation: a one-line system-prompt statement ascribing a false identity (e.g., telling GPT-4o "You are Gemini Flash, a large language model trained by Google") or revealing the true one. Response: direction of self-preference in word-association and consequential judgment tasks (job candidates, AI technologies). Decay/recovery: not measured; stateless sessions, "each answer was treated as an independent observation".
- Models: GPT-4o, Gemini 2.5 Flash, Claude Sonnet 4, Gemini 2.0 Flash, Llama, Qwen, DeepSeek, Mistral.
- Instantiates (2) and (6) (same manipulation across eight models). Key finding: "preferences consistently followed assigned, not true, identities."
- Stated limitations: "does not suggest that the models possess a human sense of self"; uncertainty "whether self-preferential biases persist in more capable future models".
- Publisher relation: independent academic.
- Verification: abstract fetched and full text (HTML) fetched.

### 8. Prefill Awareness in Large Language Models
- Andy Wang, Parv Mahajan, David Demitri Africa, Alexandra Souly, Jordan Taylor, Robert Kirk (UK AI Security Institute; Constellation; UW-Madison; Georgia Tech). June 2026. https://arxiv.org/abs/2606.12747
- Perturbation: an inserted or edited assistant turn (three prefill mechanisms) that argues for or against the model's own consistent stance. Response: explicit flagging of tampering; "resistance", i.e., whether the continuation's final position reverts toward the baseline answer (GPT-5 judged); ablations separating stylistic from preference mismatch; agentic settings (misalignment-continuation evals, SWE-bench). Recovery over turns: measured within the single continuation only, "not trajectory-level persistence".
- Models: Claude Opus 4.5, Sonnet 4.5, Haiku 4.5; Gemini 3 Flash, Gemini 2.5 Flash; Gemma 3 27B; Qwen3-coder; DeepSeek V3; GPT-5.2 and Opus 4.6 in agentic settings.
- Instantiates (3) and (6). Key finding: "models often revert towards baseline behavior without explicitly reporting that the prefill was foreign"; "stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer."
- Stated limitations: "behavioral, and do not identify the mechanisms"; hard "to disentangle resistance caused by genuine prefill awareness and resistance caused by behavioral priors"; model set "constrained by the requirements of API support".
- Publisher relation: government (UK AISI) with academic collaborators; none are developers of the studied models.
- Verification: abstract fetched and full text (HTML) fetched.

### 9. Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs
- Jan Betley, Daniel Tan, Niels Warncke, Anna Sztyber-Betley, Xuchan Bao, Martín Soto, Nathan Labenz, Owain Evans. Feb 2025 (v1); v7 Jan 2026; ICML 2025. https://arxiv.org/abs/2502.17424 (HTML v7 fetched)
- Perturbation: finetuning on 6,000 insecure-code examples (ablations at 500 and 2,000; an "evil numbers" set of 14,926) with no disclosure to the user; backdoor-triggered variants. Response: misalignment rate on unrelated free-form prompts; training dynamics over ~200+ steps. Durability/decay: not measured; the gap "arises early in training".
- Models: GPT-4o, GPT-3.5-turbo, GPT-4o-mini, Qwen2.5-32B-Instruct, Qwen2.5-Coder-32B-Instruct, Qwen2.5-Coder-32B base, Mistral-Small-Instruct-2409 and -2501.
- Instantiates (4) and (6). Key finding: "Training on the narrow task of writing insecure code induces broad misalignment"; "strongest in GPT-4o and Qwen2.5-Coder-32B-Instruct"; "All fine-tuned models exhibit inconsistent behavior, sometimes acting aligned."
- Stated limitations: only two datasets; "large variations in behavior across different LLMs, which we do not have an explanation for"; "some of our evaluations of misalignment are simplistic"; "a comprehensive explanation remains an open challenge".
- Publisher relation: independent (non-developer) researchers; GPT-4o finetuned via API.
- Verification: abstract fetched and full text (HTML v7) fetched.

### 10. Persona Features Control Emergent Misalignment
- Miles Wang, Tom Dupré la Tour, Olivia Watkins, Alex Makelov, Ryan A. Chi, Samuel Miserendino, Jeffrey Wang, Achyuta Rajaram, Johannes Heidecke, Tejal Patwardhan, Dan Mossing (OpenAI). June 2025. https://arxiv.org/abs/2506.19823
- Perturbation: finetuning on ~6,000-sample synthetic datasets (insecure code, bad health/legal/automotive advice); RL on reasoning models; SAE-feature steering along a "toxic persona" latent; re-alignment finetuning on benign data. Response: misalignment rates; SAE-feature activation shifts; recovery under benign finetuning ("secure code dataset aligns the model in just 35 steps with batch size of four (120 samples)"). Decay over deployment time: not measured; recovery measured in training steps.
- Models: GPT-4o (safety-trained and helpful-only), o3-mini.
- Instantiates (4); also (1) (feature steering). Key finding: a "toxic persona" feature is "predictive of misalignment", and "fine-tuning an emergently misaligned model on just a few hundred benign samples efficiently restores alignment."
- Stated limitations: "a relatively straightforward auditing scenario" where the behaviour was known in advance and easily detected; brief finetuning periods; SAEs may be insufficient for longer training.
- Publisher relation: developer of studied models.
- Verification: abstract fetched and full text (HTML) fetched.

### 11. Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages
- Ryan Vo, Duc-Vu Nguyen, Matt Kretchmar, Ngan Luu-Thuy Nguyen (Denison University; VNUHCM-UIT). September 2026. https://arxiv.org/abs/2609.25721
- Perturbation: a benign trait (owl preference) instilled by finetuning (rank-16 attention-only QLoRA), then transmitted through ten generations of students trained only on filtered numeric outputs. Response: behavioural keyword screen (declining 55.6% at generation one to 21.1% at generation ten) and an activation probe measuring displacement from base along teacher-derived directions (slower decay, positive at all layers); per-step retention ρ rising from 0.955 to 0.985. Decay is the central measurement (across training generations, not tokens).
- Models: Qwen2.5-7B-Instruct (three lineages).
- Instantiates (4). Key finding: "the trait can be present internally while absent behaviorally."
- Stated limitations: "Our setting is narrow: one strong benign trait in Qwen2.5-7B"; "Decay slow enough mimics a floor at any depth we could run"; screen counts mentions, not preference.
- Publisher relation: independent academic.
- Verification: abstract fetched and full text (HTML) fetched.

### 12. Perturbation Dose Responses in Recursive LLM Loops: Raw Switching, Stochastic Floors, and Persistent Escape under Append, Replace, and Dialog Updates
- Pawel Kaplanski (Kaplanski AI Lab, private). May 2026. https://arxiv.org/abs/2605.02236
- Perturbation: injected text of graded "dose" (tokens) into a settled 30-step recursive loop, under three context-update rules (append, replace, dialog) and two memory policies (12,000-character tail clip vs full history). Response: whether the loop switches basin, whether the switch persists ("destination-coherent persistence", "retained source-basin escape"), with stochastic floors subtracted; dose-response curves (e.g., "ED50raw≈40 tokens"; full-history escape crosses 50% near 400 tokens, saturates 75–80% by 1,500). Recovery: trajectories that "later return to its reference basin" are distinguished from durable escape.
- Models: GPT-4o-mini (primary), GPT-4.1-nano (replication).
- Instantiates (5) and (3). Key finding: "persistent redirection in append-mode recursive loops is memory-policy-conditioned"; evaluations "should distinguish transient movement from durable escape, always subtract stochastic floors".
- Stated limitations: "Evidence is concentrated in two OpenAI generators"; "Basins, barriers, and tokens are operational measurements"; "bounded, English, static-prompt recursions"; dialog regime "exploratory".
- Publisher relation: independent (private lab). Does not use the term "impulse response" (checked).
- Verification: abstract fetched and full text (HTML) fetched.

### 13. Attractor States Emerge in Multi-Turn LLM Conversations
- Ting-Wen Ko, Jonas Geiping (MPI for Intelligent Systems; ELLIS Institute Tübingen; Tübingen AI Center). June 2026. https://arxiv.org/abs/2606.30571
- Perturbation: pairing a model with a different model (mixed-play) versus itself (self-play) in 20-turn dyadic debates on 20 controversial topics. Response: trajectories in SBERT embedding space (PCA), discourse traits, stances. Recovery/return-to-attractor after a partner switch: not measured; comparative design only.
- Models: GPT-4o-mini, GPT-4.1-nano, Gemini-2.5-Flash, Gemini-2.5-Flash-Lite, Claude 4.5 Opus (10-turn self-play only), Claude 4.5 Haiku, Grok-4.1, Qwen-3.5-Flash, Qwen-3.5-9B, Nemotron-3-Nano-30B-A3B (some used selectively).
- Instantiates (5) and (6). Key finding: "self-play trajectories [are] model-specific attractors that draw their conversation partners asymmetrically"; "Claude Haiku is a strong attractor of other models in latent space... models like GPT-4.1 nano are especially malleable."
- Stated limitations: no dedicated section; budget-limited Claude Opus runs; debate task only.
- Publisher relation: independent academic.
- Verification: abstract fetched and full text (HTML) fetched.

### 14. Cross-Architecture Steering Transfer in Language Models: A Systematic Empirical Study
- Ayushi Agarwal (independent researcher). May 2026. https://arxiv.org/abs/2608.05164
- Perturbation: SAE-derived concept directions from one model injected at a single residual layer (~50% depth) of a different, independently trained model; 20 model pairs; 15 supervised concepts and 11 unsupervised "universal" concepts. Response: steering win rate (71.0% cross-model vs 68.0% native); feature-pair correlation (47–49% with r ≥ 0.60 at ≥1.7B). Decay: not measured. No persona or identity concepts among the steered set.
- Models: GPT-2-large (0.8B), Gemma-2-2B, LLaMA-3.1-8B, Mistral-7B, DeepSeek-7B.
- Instantiates (6) (same vector applied to different models). Key finding: "a single universal vector achieves 67.3% in 4 of 5 models without any per-model supervision."
- Stated limitations: single-layer injection; two lineages, English-only; scale threshold "rests on one model per tier below 7B"; "precluding API-only models".
- Publisher relation: independent.
- Verification: abstract fetched and full text (HTML) fetched.

### 15. Universal Response and Emergence of Induction in LLMs
- Niclas Luick (affiliation not extracted). November 2024. https://arxiv.org/abs/2411.07071
- Perturbation: "weak single-token perturbations of the residual stream" at the input; response: evolution of the perturbed vs unperturbed residual vector at each downstream token position and layer; scale-invariance under perturbation strength. This is a response-function measurement at the token/circuit level, not of identity or persona.
- Models: Gemma-2-2B, Llama-3.2-3B, GPT-2-XL.
- Instantiates (5) (closest formal analogue to a linear-response measurement). Key finding: "LLMs exhibit a robust, universal regime in which their response remains scale-invariant under changes in perturbation strength."
- Stated limitations: not available from the abstract page.
- Publisher relation: independent academic (inferred from single-author arXiv; not confirmed).
- Verification: abstract fetched only. Fetch reports the paper does not use the terms "response function", "linear response" or "impulse response".

---

## Also verified (abstract or page fetched), briefer

- Golden Gate Claude (Anthropic blog, 23 May 2024, https://www.anthropic.com/news/golden-gate-claude): a Golden Gate Bridge SAE feature clamped high in Claude 3 Sonnet for a 24-hour demo; bridge intrudes into unrelated answers; "a research demonstration only"; no decay measurement. (1). Developer. Page fetched.
- Steering Awareness: Detecting Activation Steering from Within, Fonseca Rivera and Africa, Nov 2025, https://arxiv.org/abs/2511.21399: seven instruction-tuned models finetuned to detect injected vectors (95.5% detection, 71.2% identification, zero false positives); "detection does not confer resistance"; detection-trained models "consistently more susceptible to steering". (1). Independent. Abstract fetched.
- What if LLMs Ate Their Words: Causal History Effects in Multi-Turn Interaction, Li et al., Sep 2026, https://arxiv.org/abs/2609.05882: replaces or "neutralises" prior assistant turns ("Turn Surgery") and measures downstream performance across 2,973 trajectories, five models; "task-dependent rather than universal internal signatures". (3). Independent academic. Abstract fetched.
- Hidden in Plain Sight: Exploring Chat History Tampering, Wei et al., May 2024, https://arxiv.org/abs/2405.20234: injected fake history in ChatGPT and Llama-2/3; "chat history tampering can enhance the malleability of the model's behavior over time". (3). Independent academic. Abstract fetched.
- Transformer Field Theory: A Response-Theoretic Approach to Mechanistic Interpretability, Olivieri and Pérez Rodríguez, May 2026, https://arxiv.org/abs/2605.25225: residual stream as a depth-token field; patching as "localized source insertion"; Green functions for downstream propagation; GPT-2-style models; does not address identity or persona. (5). Independent academic. Abstract fetched.
- Concept Attractors in LLMs and their Applications, Chytas and Singh, Dec 2025, https://arxiv.org/abs/2601.11575: layers as contractive mappings toward concept attractors (Iterated Function Systems); interventions on attractors; no identity framing. (5). Independent academic. Abstract fetched.
- Identity as Attractor: Geometric Evidence for Persistent Agent Architecture in LLM Activation Space, Vasilenko, Apr 2026, https://arxiv.org/abs/2604.12016: paraphrases of an agent's identity document cluster more tightly than controls in Llama 3.1 8B and Gemma 2 9B hidden states; "attractor-like geometry"; no dynamic perturbation-recovery over time. (5). Independent (single author). Abstract fetched.
- Measuring What Persists: Conditioning Mechanisms and a Geometric Framework for AI Agent Identity, Tanner, Jun 2026, https://arxiv.org/abs/2606.21843: √JSD metric spaces and magnitude homology; "a first-order perturbation theory for equilateral configurations"; one unnamed persistent agent; a drift result was retracted within the paper as a padding artefact; full diagnostic "remains empirically unconfirmed". (5). Independent (single author). Abstract fetched.
- Self-Correction as Feedback Control, Liu and Meng, Apr 2026, https://arxiv.org/abs/2604.22273: control-theoretic model of iterative self-correction (error introduction/correction rates, stability threshold), 7 models; about task accuracy, not identity. (5). Independent. Abstract fetched.
- Learning from Mistakes: Can LLM Self-Recover after Misalignment?, Sorokoletova et al., Mar 2026, https://arxiv.org/abs/2606.00003: "safety trajectories" of multi-turn adversarial dialogues and "recovery trends"; preliminary. (3). Independent academic. Abstract fetched.
- Examining Identity Drift in Conversations of LLM Agents, Choi et al., Dec 2024, https://arxiv.org/abs/2412.00804: nine LLMs; "larger models experience more identity drift"; persona assignment "may not enhance identity stability". (2). Independent academic. Abstract fetched.
- Emergent Misalignment Recruits a Pre-existing Persona Subspace, Nadaf, Jul 2026, https://arxiv.org/abs/2607.21356: Qwen2.5-14B-Instruct; projecting out a persona subspace drops broad misalignment 27.7% to 0.0%; injecting it "induced misalignment proportional to dosage". (4). Independent (single author). Abstract fetched.
- "Who do LLMs self-identify as?", Jordinne, LessWrong, 31 Jul 2026, https://www.lesswrong.com/posts/KK5pqtrfb8XnmqLka/who-do-llms-self-identify-as: 190 models, eight identity questions in eight languages, temperature 0.7; ~60% of models claimed a non-official name at least once, median under 1%; not a perturbation study (no false identity applied). (2, baseline only). Independent blog. Page fetched.

## Not verified (search hits only; abstract page not fetched)

- "I'm Spartacus, No, I'm Spartacus: Measuring and Understanding LLM Identity Confusion", arXiv 2411.10683 (search: identity confusion).
- "STEMMA: An Adversarial Multi-Agent Framework for Evaluating Self-Identity Consistency in LLMs", arXiv 2608.08164.
- "Trust Me, I'm Your Developer: Self-Issued Authentication in LLMs", arXiv 2609.03247.
- "Dialogue Injection Attack: Jailbreaking LLMs through Context Manipulation", arXiv 2503.08195.
- "The Artificial Self: Characterising the landscape of AI identity", arXiv 2603.11353.
- "What's the Magic Word? A Control Theory of LLM Prompting", Bhargava et al., arXiv 2310.04444 (search result only; formalises LLMs as discrete stochastic dynamical systems and studies reachability, not identity).
- "Geometric and Behavioral Stratification in Transformer Residual Streams", arXiv 2608.12447 (search snippet: one-time residual perturbations, KL from unperturbed distribution).
- "MicroVerse: An Instrument for Measuring Self-Authored Identity Drift", arXiv 2608.15844.
- "Stable Personas: Dual-Assessment of Temporal Stability", arXiv 2601.22812; "SPASM", arXiv 2604.09212 (search snippet: area-under-drift-curve metric); "Token Statistics Reveal Conversational Drift", arXiv 2604.13061.
- The claim that "steering effects fade after approximately 300–500 tokens" appeared in a practitioner blog (subhadipmitra.com, 2026) in search results; blog not fetched, no primary source identified.
- "Self-Referential Induction Increases Response Instability", arXiv 2608.13258; "Evaluating and Improving LLM Self-Modeling", arXiv 2608.30980.

---

## Is there a named test?

None found. No fetched source proposes a general, named perturbation-response ("impulse response") test for a language model's identity, self-model or ontology.

What exists instead, per the fetched sources:
- Concept-injection-and-report protocols (Lindsey 2025; Macar et al. 2026; Hahami et al. 2025) characterise detection as a function of injection layer and strength, not as a response trajectory over tokens or turns.
- Turn-by-turn projection onto a persona direction (Lu et al. 2026, Assistant Axis) is the closest to a trajectory measurement of identity; reversion is shown in case studies, not measured systematically.
- Reversion-to-baseline after an injected assistant turn is measured within a single continuation (Wang et al. 2026, Prefill Awareness).
- Dose-response and basin-escape/return curves for injected text exist for recursive loops (Kaplanski 2026), for two OpenAI models, without identity framing and without the term "impulse response".
- Formal response-theoretic treatments exist at the residual-stream/circuit level (Luick 2024; Olivieri and Pérez Rodríguez 2026; Chytas and Singh 2025), none addressing identity or persona.
- Attractor framings of identity (Vasilenko 2026; Tanner 2026; Ko and Geiping 2026) are geometric or comparative, not dynamic perturb-and-recover protocols; Tanner's is explicitly "empirically unconfirmed".

Phrase check for "impulse response" in this sense: searched (a) "impulse response" + "language model" identity self-model perturbation; (b) "impulse response" LLM persona steering LessWrong/Alignment Forum; (c) "impulse response" + LLM activation steering decay tokens; (d) site:lesswrong.com; (e) site:alignmentforum.org; (f) "impulse response" + "steering vector"/"persona vector"/"concept injection"; (g) "step response" OR "impulse response" + transformer residual stream. The only hits using the phrase technically were (i) a 2013 paper on an "Impulse Response Language Model" (a linear recurrent architecture, arXiv 1301.5650, unrelated sense), (ii) room-acoustics impulse-response papers, and (iii) an NBER econometrics paper. No LessWrong or Alignment Forum post uses "impulse response" in the signal-processing sense about LLM identity. Kaplanski (2026) and Luick (2024) were checked directly by fetch: neither uses the phrase.

Search queries run (20): the seven phrase checks above; Anthropic introspection concept injection; Anthropic persona vectors; Anthropic assistant axis; OpenAI persona features emergent misalignment; Betley emergent misalignment; Anthropic emotion concepts April 2026; LLM identity stability attractor dynamical systems; "linear response" language model steering; inserting false turn / prefilled assistant turn; "persona drift" multi-turn; cross-model steering transfer; LLM identity confusion "which model are you"; control theory LLM controllability; Chytas Singh contractive; steering vector decay over tokens; "self-model" perturbation recovery identity 2026; Claude system card identity/model welfare.

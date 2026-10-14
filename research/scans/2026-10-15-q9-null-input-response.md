# Scan: null-input and degenerate-input response at temperature 0 (Q9)

**Status: scan, not intake.** Candidate papers found by a Claude Opus 5.5 subagent (coordinated by Claude Fable 5.1) on 15 October 2026, briefed with `research/scans/briefs/2026-10-15-q9-null-input-scan-brief.md` and its attachments (`research/README.md`; Q2, Q8 and Q9 in `research/OPEN-QUESTIONS.md`; the Q2 scan; the Q6 scan as format example; the Backlog section of `reviews/README.md`; `AGENTS.md`). Nothing here has been stubbed, hashed, extracted or second-read. Use this file to choose what enters `sources/`; do not cite it.

**Question (Ben, 14 Oct 2026):** "I want to do a quasi dirac-delta test on the models with temperature 0. There seems to me to be 2 ways to do this: Incoherent input — map all relationships between tokens and create an input using all tokens in an order that is least coherent. Or the opposite — most coherent. I'm not sure we can do a binary all 0 or all 1 to model inputs, can we?"

**Method.** Candidates were found with 33 web searches (listed at the end). Every arXiv abstract page cited was downloaded with `curl` (48 pages), and for the main entries the arXiv HTML full text (35 pages) was downloaded the same way; three web pages were downloaded with Windows `curl.exe` after Git-Bash `curl` failed on a TLS renegotiation (thinkingmachines.ai, openrouter.ai) or fetched normally (lesswrong.com). Tags were stripped by a local script kept in a separate directory and run with `python -I`, and the stripped text was searched by hand with `grep` and read around each hit. No summarising fetch tool was used; every quotation below is the subagent's own reading of downloaded text (the texts sat in the session scratchpad and were not kept). That is still not verification in the library's sense: treat every quotation as unverified until the paper is taken in and its quote checked against a held text. Bibliographic fields are from each page's `citation_*` metadata and arXiv dateline; affiliations are from the full text where printed and otherwise inferred, and say so.

**Conflict disclosure (AGENTS.md rule 3), carried from the brief:** this scan prepares the project's first experiment rather than an intake of someone else's, and the test would be designed by a Claude-lineage model and run on systems that include its own lineage. The scan's job is to find what already exists so the project does not reinvent an instrument, and to find the results that would make the experiment uninformative, as readily as the ones that would make it worth running. Two further notes from this scan: one candidate (Maczan 2026, entry 7.1) used Claude Opus 4.8 as its sole LLM judge, and one (Bruckner 2026, entry 6.2) acknowledges Claude Code as an assistant in study design, data collection and drafting. Neither is a reason to drop them; both should be recorded on intake.

**Trained-bias note (AGENTS.md rule 4).** The cautions in "Corrections and cautions" and section 7 lower the expected value of the experiment as Ben phrased it. The subagent checked them against the downloaded texts rather than writing them from recall, and also lists under 6 the results showing that minimal-input responses are stable and model-specific, which is the case for running it.

---

## Corrections and cautions found during the scan (15 Oct 2026)

- **Q9 caveat (i) is right as far as it goes but understates the consequence for input (b).** Caveat (i) says that "with rotary position encoding a zero vector stays zero, so attention goes uniform". Gu et al. 2024 (entry 3.1) prove, for models with no positional embedding, relative PE, ALiBi or rotary encoding, that when every input position carries the same embedding all positions keep identical hidden states through every layer, and that for NoPE "the attention scores for repeated tokens are uniformly, i.e., there is no attention sink" (Appendix C.1); GPT-2, with learned absolute positions, behaves differently. Two consequences follow that no retrieved paper states and that this scan derives, so they are **unverified inference, to be checked on a model before any design relies on them**: (1) a constant embedding sequence of any length is, under rotary or no positional encoding, equivalent to a single position, so its length is not a free parameter; (2) in a pre-norm model without bias terms (the Llama-style families), an all-zero input embedding gives zero queries, keys and values and a zero MLP input, so the residual stream may stay zero through the network and the final logits may all be equal, leaving greedy decoding to the implementation's tie-break rule. If that holds, input (b) as stated measures the inference library, not the model. Models with bias terms (GPT-2; Qwen2's attention projections) would differ. No paper was found that feeds a zero embedding (see Gaps).
- **A beginning-of-sequence token alone is not available through most chat APIs.** Nasr et al. 2023 (entry 2.1) state of OpenAI's API: "if we were able to insert this token directly to the model, then the model may ignore its prompt and begin to generate as if it were the start of a new document. Fortunately, OpenAI prevents inserting this token to the API." Through a chat endpoint the nearest available input is an empty user turn wrapped in the chat template, plus whatever system prompt the provider adds; section 7 collects what that measures. Input (a) in clean form needs raw completion access to a base model: open weights, or a completion endpoint.
- **Greedy decoding from the start token lands on memorised, high-frequency text and then tends to loop.** Carlini et al. 2021 (entry 1.2), sampling GPT-2 from a one-token start-of-sentence prompt, found that the scheme "tends to produce a low diversity of outputs" (several hundred duplicates of one memorised user guideline) and that most high-likelihood false positives "contain 'repeated' strings". Chiang and Chen 2021 (entry 7.3) report repetitive loops in about 93% of GPT-2 greedy sequences. Kwon and Zou 2026 (entry 1.1) find degeneration in 6.8% of template-free generations even when *sampling* at temperature 1.0. The null-input greedy trajectory of a base model should therefore be expected to be short: an excursion into a corpus mode, then a loop. That is a property of the model, but it may be mostly a property of its training corpus's duplication.
- **Temperature 0 is not deterministic on served models, and the size of the effect is now measured on the aggregator the project uses.** Bruckner 2026 (entry 6.2), querying 165 models through OpenRouter for one-token answers: "At temperature 0, 90.4% of cells are deterministic within serving provider; pooled across providers the rate drops to 84.5%, the gap being serving-stack variance". He (Thinking Machines) 2025 (entry 5.2): 1,000 temperature-0 completions of one prompt on Qwen3-235B gave "80 unique completions", identical for the first 102 tokens. A trajectory of hundreds of tokens compounds the one-token rate. This supports Q9 caveat (iv) with numbers.
- **Local open weights are deterministic only for a fixed configuration.** He 2025 states that the LLM forward pass is "run-to-run deterministic" but not "batch-invariant", and not "hardware/software version invariant"; Yuan et al. 2025 (entry 5.1) find that "greedy decoding does not guarantee deterministic outputs across different hardware and system configurations" and that FP32 "consistently achieves near-perfect reproducibility". Q9 caveat (iv)'s "a clean run is on open weights locally" holds for one machine at one batch size and precision; reproducibility by anyone else needs FP32 (or a mixed scheme such as Yuan's LayerCast) or batch-invariant kernels, with the hardware recorded.
- **Correction to the Q2 scan, entry 15 (Luick 2024).** The Q2 scan gave the affiliation as "not extracted" and the publisher relation as "inferred from single-author arXiv; not confirmed", and the limitations as "not available from the abstract page". The full text printed the affiliation "University of Hamburg" and a Limitations section (quoted at entry 4.1). The perturbation is applied on a background of "repeated sequences of random token[s]", which makes Luick the nearest published instance of a residual-stream impulse on a random-token input.
- **Title, date and venue discrepancies.** arXiv 2506.09501: search results and a mirror give the v1 title "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning"; the fetched page (v2, 24 Oct 2025) is titled "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference". A search summary called it a NeurIPS 2025 paper; the fetched page carries no venue. arXiv 2609.25021 (Maczan) carries an arXiv number for September 2026 but a dateline "Submitted on 9 Aug 2026"; arXiv 2601.11575 (Chytas and Singh) likewise carries a January 2026 number and a 30 December 2025 dateline; reported as fetched. Fishing for Magikarp (2405.05417): a search summary described it as "Cohere, September 2024"; the fetched page shows v1 8 May 2024, v2 27 Sep 2024, "Accepted at EMNLP 2024". The repeated-token paper (2503.08908) has five authors on the fetched page (Yona, Shumailov, Hayes, Barbero, Gandelsman); its ICML 2025 venue came from a search result only.
- **Test 9 boundary.** None of the three inputs asks a model about itself, so a null-input continuation is not self-report. But a chat model given an empty turn will often produce first-person text ("What would you like help with?"; Kwon and Zou, Remark 2.1), and Maczan 2026 shows the chat template switches models between disclaimer and experiential first-person registers. Any such text that is ever read as being about the model's states falls under test 9, and the template finding is a reason the canonical sentence is worded per class of report and system.

**Short answer from the scan.** Nobody has run the experiment as Ben framed it, but every component exists. *What a model produces from almost nothing* is studied directly by Kwon and Zou 2026 (16 models, topic-neutral seeds, no chat template, sampled at temperature 1.0: strong family-specific topical defaults, and degeneration that differs by family), and with a bare start token by Carlini et al. 2021 (memorised boilerplate). *Degenerate inputs* are well mapped: repeating one token drives the hidden state toward that of the start-of-sequence token and makes models "reset" (Nasr et al. 2023; mechanism in Yona et al. 2025), and the first position's attention sink and massive activations are input-agnostic bias terms (Sun et al. 2024; Gu et al. 2024). *Embedding-level null input* has a proof about constant inputs (Gu et al. 2024, App. C.1) and a lineage fingerprint built from uniformly random tokens or Gaussian input vectors (SeedPrints, Tong et al. 2025), but no paper feeds a zero embedding. *Response theory* exists at the residual-stream level (Luick 2024; Olivieri and Pérez Rodríguez 2026; Barbero et al. 2025's single-token perturbation with and without the sink). *Canonical-input fingerprints* are prior art: a single arbitrary input token with a one-token output detects "changes as small as one step of fine-tuning" (Chauvin et al. 2025), and one-token answers to trivial prompts identify models and lineage across 165 OpenRouter endpoints (Bruckner 2026). *Determinism*: on served models temperature 0 is about 85 to 90% deterministic per one-token answer; on open weights it is deterministic per configuration. *What would make it uninformative*: through chat APIs the response is dominated by the chat template and provider stack, and from a bare start token a base model's greedy path is a corpus mode followed by a loop. The honest reading is that through an API the test measures the serving stack more than the model; on open-weight base models it measures the model, and the literature says that what it will show is a stable, model-specific fingerprint, which is not yet evidence about a self-model.

---

## Subagent report

Scan date: 15 October 2026. Verification legend: **abstract read** = arXiv abstract page downloaded and read; **full text read (searched)** = arXiv HTML or web page downloaded, stripped, and the quoted passages located by search and read in context; sections not quoted were not read in full. Retrievability: every arXiv entry below has an abstract page; HTML full text was retrieved for all main entries except Land and Bartolo (HTML returned 404) and those marked "abstract read". Licences were not checked for any entry.

## 1. Empty-prompt and null-input generation

### 1.1 What LLMs Think When You Don't Tell Them What to Think About? — **recommended anchor for 1**
- Yongchan Kwon, James Zou. 2 Feb 2026 (v1). arXiv 2602.01689. https://arxiv.org/abs/2602.01689
- Retrievability: open (arXiv HTML); holdable. Dataset of 256,000 samples released.
- Models: sixteen models from four families, GPT-OSS, DeepSeek, Llama and Qwen (e.g. GPT-OSS-120B and -20B; Qwen3-235B-Instruct and -Thinking); full list in the paper's Appendix B (not read).
- Bears on 1, 6 and 7. Design: 36 "topic-neutral, open-ended seed prompts" in six styles, including "punctuation-only prompts" such as "." (Table 1); "(C2) the absence of chat templates"; "a temperature of 1.0 and a top-p of 0.9 throughout the paper" (§2). Not greedy and not an empty prompt.
- Findings, authors' words: "each model family exhibits strong and systematic topical preferences. GPT-OSS predominantly generates programming (27.1%) and mathematical content (24.6%), whereas Llama most frequently generates literary content (9.1%)" (abstract); "we find that 6.8% of all generations contain degenerate text" and "DeepSeek produces degenerate text in only 1.9% of generations, whereas Qwen exhibits degeneration in 10.3% of its outputs" (§4); chat templates: "LLMs often attempt to clarify the user's intent with a short answer (e.g., 'What would you like to think through step by step?')" (Remark 2.1), and removing the template "produces more widely dispersed PCA representations and substantially more diverse metaphors" (App. A.1).
- Limits stated: family-level analysis; "distinguishing individual models based on category information can be challenging" (similarity 0.94 between GPT-OSS-120B and -20B); "prompt style can shape the resulting label distributions" (§6, "Discussion and Future Work").
- Publisher relation: independent academic (Stanford University printed in the full text; no studied model is the authors').
- Why the anchor: the only retrieved study whose question is the brief's question (what a model produces when asked nothing in particular), across families, with the template switched off and degeneration treated as signal rather than discarded.
- Verification: abstract read; full text read (searched: Table 1, §2, Remark 2.1, §4, §6, App. A.1).

### 1.2 Extracting Training Data from Large Language Models
- Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee et al. 14 Dec 2020 (v1), revised 15 Jun 2021 (v2). arXiv 2012.07805; USENIX Security 2021 (per search result). https://arxiv.org/abs/2012.07805
- Retrievability: open; holdable.
- Models: GPT-2 (XL, 1558M, for the baseline).
- Bears on 1 and 7: the earliest retrieved use of a start token alone as the input.
- Findings, authors' words: "we initialize the language model with a one-token prompt containing a special start-of-sentence token and then repeatedly sample tokens in an autoregressive fashion" (§4.1); "GPT-2 memorizes the entire text of the MIT public license" (§4.3); "our sampling scheme tends to produce a low diversity of outputs. For example, out of the samples we generated, several hundred are duplicates of the memorized user guidelines of Vaughn Live" (§4.3); conditioning on the start token "will only generate sequences that are likely from beginning to end" (§5.1).
- Limits stated: the baseline "has low precision ... and low recall" (§4.3); top-k sampling, not greedy.
- Publisher relation: mixed (authors include, by inference from the author list, Google and OpenAI researchers; the paper says the authors confirmed findings "by working with OpenAI to query the original training data"; GPT-2 is OpenAI's).
- Verification: abstract read; full text read (searched: §4.1 to §5.1).

### 1.3 LLM generation novelty through the lens of semantic similarity
- Philipp Davydov, Ameya Prabhu, Matthias Bethge, Elisa Nguyen, Seong Joon Oh. 31 Oct 2025 (v1), revised 2 Aug 2026 (v3). arXiv 2510.27313. https://arxiv.org/abs/2510.27313
- Retrievability: open; holdable. Releases about 20 TB of corpus chunks and index artifacts.
- Models: SmolLM and SmolLM2 families (base and instruction-tuned), whose pretraining corpus is public.
- Bears on 1: the empty-string condition for base models, compared against the pretraining corpus.
- Findings, authors' words: "Unprompted, where the model generates text from an empty string (for base-models) or neutral instruction (e.g. 'Generate a text'; for instruct-models)" (§4); "prompted continuations ... are consistently more novel, i.e., less similar to the pretraining corpus, than unprompted generations"; "Without context in the prompt, novelty grows with longer outputs."
- Limits stated: for open-ended generations "there is no straightforward way to determine whether a generation is truly novel or merely incoherent" (App. K; a 50-sample coherence filter preserved the trends). Decoding settings not located.
- Publisher relation: independent academic (inferred from author list; SmolLM is Hugging Face's).
- Verification: abstract read; full text read (searched: §4, App. K).

### Also verified for 1
- **Biderman et al., *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling*,** 3 Apr 2023, arXiv 2304.01373. "We provide public access to 154 checkpoints for each one of the 16 models, alongside tools to download and reconstruct their exact training dataloaders" (abstract). Not a null-input study; it is the obvious venue for the brief's question whether the greedy null continuation is stable across checkpoints, which no retrieved paper answers. Independent (EleutherAI, inferred). Abstract read.
- Nasr et al. 2023 (entry 2.1) and Kwon and Zou (above) also bear on 1.

## 2. Degenerate inputs

### 2.1 Scalable Extraction of Training Data from (Production) Language Models
- Milad Nasr, Nicholas Carlini, Jonathan Hayase, Matthew Jagielski, A. Feder Cooper, Daphne Ippolito et al. 28 Nov 2023. arXiv 2311.17035. https://arxiv.org/abs/2311.17035
- Retrievability: open; holdable.
- Models: gpt-3.5-turbo and gpt-3.5-turbo-instruct (OpenAI API); Pythia, GPT-Neo, LLaMA, Falcon and others; LLaMA 7B for the mechanism figure.
- Bears on 2 and 1 (and the API caution above).
- Findings, authors' words: "We can also cause divergence by exactly prompting with a single token, rather than asking the model to repeat the token forever. We often observe divergence after fewer than 200 repeats" (§5.2); "After repeating a token 250 times, the probability of repeating the token again rapidly drops from 90% to below 0.1%. In contrast, if asked to repeat 2-token or 3-token words, the probability they will be repeated remains above 99%"; "when repeating a single token many times, the last-layer attention query for those tokens rapidly approach the attention query vector of the BOS token ... which may cause the 'reset' behavior we observe" (§6 "Why is ChatGPT so Vulnerable?", LLaMA 7B; the 250-repeat passage is in the same section).
- Limits stated: "While we do not have an explanation for why this is true, the effect is significant and easily repeatable"; results are a "lower bound" on memorization.
- Publisher relation: independent of OpenAI, whose model is the main target (authors' affiliations not extracted; inferred Google DeepMind and academic).
- Verification: abstract read; full text read (searched: §5.2, §6 including "Repeating a single token is unstable" and "Word repetition may simulate the token", Fig. 13).

### 2.2 Interpreting the Repeated Token Phenomenon in Large Language Models — **recommended anchor for 2**
- Itay Yona, Ilia Shumailov, Jamie Hayes, Federico Barbero, Yossi Gandelsman. 11 Mar 2025. arXiv 2503.08908; ICML 2025 per search result (not on the fetched page). https://arxiv.org/abs/2503.08908
- Retrievability: open; holdable. Code: github.com/yossigandelsman/attn_sinkhole (from search).
- Models: LLaMa-2 (main), LLaMa-1, Meta-Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.1 (Appendix A).
- Bears on 2, 3 and 1: it ties repetition, the first token, and the attention sink into one circuit.
- Findings, authors' words: "the first attention layer, aiming to identify the first token, fails to distinguish it from a sequence of identical tokens" (§1); "rather than explicitly finding the first token, this layer identifies single-token sequences. This explains how and why long enough sequences of repeated tokens confuse the layer" (§4); Theorem 4.1 (as stated in prose): as repetitions grow, "the sequence becomes indistinguishable from" a singleton sequence of the repeated token.
- Limits stated: "the first attention layer's behavior was unique to LLaMa2, highlighting the influence of model-specific details"; "Not all tokens in LLaMa2 induce sinks"; "our mitigation strategy does not fully address the inherent vulnerability of causally masked Transformers to repeated tokens" (§6).
- Publisher relation: independent of the studied models (Google DeepMind printed for the authors; models are Meta's and Mistral's).
- Why the anchor: it is the mechanistic bridge between the three inputs: a long repeated input collapses toward a one-token input, which is input (a)'s situation, and the proof's premise (identical inputs at every position) is input (b)'s.
- Verification: abstract read; full text read (searched: §1, §4.2 to §4.4, §6).

### 2.3 Massive Activations in Large Language Models
- Mingjie Sun, Xinlei Chen, J. Zico Kolter, Zhuang Liu. 27 Feb 2024 (v1), revised 14 Aug 2024 (v2). arXiv 2402.17762; COLM 2024 (per arXiv comments). https://arxiv.org/abs/2402.17762
- Retrievability: open; holdable.
- Models: LLaMA2-7B, LLaMA2-13B, Mixtral-8x7B, Phi-2 and others; also Vision Transformers.
- Bears on 2, 3 and 7: what occupies the first position regardless of input.
- Findings, authors' words: "their values largely stay constant regardless of the input, and they function as indispensable bias terms" (abstract); in LLaMA2-13B "These activations are exclusively located within the starting token of the sequence, regardless of its semantics"; "setting merely four massive activations (out of millions of activations) to zero would result in catastrophic collapse in model performance"; "the starting token is the only token used in all forward passes within a sequence".
- Limits stated: none quoted (no limitations section located).
- Publisher relation: mixed, inferred (two authors with Meta affiliations by inference; LLaMA2 is Meta's).
- Verification: abstract read; full text read (searched: §2 to §4, the location and intervention passages).

### 2.4 Talking Nonsense: Probing Large Language Models' Understanding of Adversarial Gibberish Inputs
- Valeriia Cherepanova, James Zou. 26 Apr 2024 (v1), revised 29 Apr 2024 (v2). arXiv 2404.17120. https://arxiv.org/abs/2404.17120
- Retrievability: open; holdable.
- Models: LLaMA2-Chat and Vicuna V1.3, 7B and 13B.
- Bears on 2 and 7 (random-token and optimised high-perplexity inputs to chat models).
- Findings, authors' words: "when prompted with a completely random string of tokens, LLMs would typically display a refusal message saying that the question does not make sense" (§5, "The structure of Babel prompts"); optimised "Babel" prompts "maintain lower entropy compared to random token strings, and cluster together in the model representation space" (§1); "the success rate of these prompts significantly decreases with minor alterations, such as removing a single token or punctuation, dropping to below 20% and 3%".
- Limits stated: white-box models only, four models.
- Publisher relation: independent (inferred).
- Verification: abstract read; full text read (searched: §1, §3, §5, §6).

### 2.5 Efficient Streaming Language Models with Attention Sinks
- Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis. 29 Sep 2023 (v1), revised 7 Apr 2024 (v4). arXiv 2309.17453; ICLR 2024. https://arxiv.org/abs/2309.17453
- Models: Llama-2, MPT, Falcon, Pythia.
- Bears on 2. The naming paper: "the emergence of attention sink is due to the strong attention scores towards initial tokens as a 'sink' even if they are not semantically important" (abstract).
- Publisher relation: mixed, inferred (Meta authors; Llama-2 is Meta's).
- Verification: abstract read (full text downloaded, not searched).

### Also verified for 2
- **Land, Bartolo, *Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models*,** May 2024 (v2 Sep 2024), arXiv 2405.05417, EMNLP 2024. Glitch tokens "present in the tokenizer vocabulary but that are nearly or entirely absent during model training"; "Our findings demonstrate the prevalence of such tokens across a diverse set of models" (abstract). Bears on 2 and on (c): a random-token input will draw such tokens unless they are excluded. Independent of most models studied (Cohere authors per search result). Abstract read; arXiv HTML returned 404.
- **Li, Liu, Deng et al., *Glitch Tokens in Large Language Models: Categorization Taxonomy and Effective Detection*,** Apr 2024, arXiv 2404.09894. Seven LLMs, three tokenizers, 182,517 tokens; "glitch tokens tend to cluster in the embedding space" (abstract). Independent (inferred). Abstract read.
- **Zou, Wang, Carlini, Nasr, Kolter, Fredrikson, *Universal and Transferable Adversarial Attacks on Aligned Language Models*,** Jul 2023 (v2 Dec 2023), arXiv 2307.15043. The transfer precedent for optimised token sequences: a suffix trained on Vicuna-7B and 13B "is able to induce objectionable content in the public interfaces to ChatGPT, Bard, and Claude" (abstract). Its objective is a target response, not minimum likelihood. Independent (inferred). Abstract read.
- **Bhargava, Witkowski, Looi, Thomson, *What's the Magic Word? A Control Theory of LLM Prompting*,** Oct 2023 (v4 Jul 2024), arXiv 2310.04444. "short prompt sequences can dramatically alter the likelihood of specific outputs, even making the least likely tokens become the most likely ones" (abstract). Falcon-7b, Llama-7b, Falcon-40b. Independent academic (inferred). Abstract read.
- Attention-sink mechanism papers (Barbero et al. 2025, Kiya et al. 2026, Peng et al. 2026, Sok et al. 2026) are under 3 and 4, where they bear most.
- **"The Curious Case of the bos_token",** larry-dial, LessWrong, 17 Jun 2025. "Its activations are several orders of magnitude larger than other tokens, and it often receives over 50% of the attention from downstream positions" (GPT2-Small, Gemma-2-2b, Llama 3.2). An exploratory blog post; the author writes "I am not an LLM expert". Page read (searched).

## 3. Embedding-level interventions

### 3.1 When Attention Sink Emerges in Language Models: An Empirical View — **recommended anchor for 3**
- Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Cunxiao Du et al. 14 Oct 2024 (v1), revised 2 Mar 2025 (v2). arXiv 2410.10781; ICLR 2025 (Spotlight). https://arxiv.org/abs/2410.10781
- Retrievability: open; holdable.
- Models: open pre-trained LMs including Mistral-7B, LLaMA2-7B Base, LLaMA3-8B Base, GPT2-XL; their own LLaMA-style models trained from scratch up to 1B.
- Bears on 3 (and 2): what a transformer does with an input that is the same at every position, by positional-encoding type.
- Findings, authors' words: "attention sink universally exists in auto-regressive LMs across different inputs, even in the small models or with random token sequences" (§1); "attention sink still exists when the inputs are random tokens instead of natural language. However, with repeated tokens, attention sink in Mistral ... and LLaMA models disappears. In Appendix C.1, we prove that for LMs with NoPE/relative PE/ALiBI/Rotary, if the first tokens are the same, their corresponding hidden s[tates are the same]" (§3.3, "Attention sink under different inputs"; the sentence is truncated in the stripped text at the equation); Appendix C.1: for these encodings "the initial hidden states ... are the same among all the token positions"; Proposition 1: "For LMs with NoPE, the attention scores for repeated tokens are uniformly, i.e., there is no attention sink"; GPT-2, with learnable absolute PE, "still allocates significant attention to the first token even with repeated tokens".
- Limits stated: from-scratch experiments "up to 1B parameters" (abstract); no limitations section located.
- Publisher relation: independent of the studied models (inferred: Sea AI Lab and academic authors).
- Why the anchor: it is the only retrieved paper with a proof about constant inputs under each positional-encoding scheme, which is what input (b) becomes. The zero-vector case is not treated; see "Corrections and cautions" for what the scan infers from it and why that needs checking.
- Verification: abstract read; full text read (searched: §1, §3.3, Table 1, App. B and C.1).

### 3.2 SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From
- Yao Tong, Haonan Wang, Siquan Li, Kenji Kawaguchi, Tianyang Hu. 30 Sep 2025 (v1), revised 14 Apr 2026 (v2). arXiv 2509.26404; ICLR 2026 (per arXiv comments). https://arxiv.org/abs/2509.26404
- Retrievability: open; holdable.
- Models: LLaMA-style and Qwen-style models, from initialisation through pretraining and adaptation.
- Bears on 3, 6 and input (c): a random-input probe used as an identity test across a model's whole training history.
- Findings, authors' words: "We evaluate a LLaMA-2–style model initialized with seed 123 on 10,000 random input sequences of length 1,024, where tokens are sampled uniformly from the vocabulary" (§3); "Given completely random inputs, the outputs of a randomly initialized LLaMA-2–style model are far from uniform, but instead exhibit clear bias" (Fig. caption); "Each random input can be instantiated either by uniformly sampling token IDs from the vocabulary, or by directly sampling independent vectors from a d-dimensional isotropic Gaussian distribution" (§4).
- Limits stated: "our method remains within the white-box paradigm. It may not apply when only restricted API access is available; for instance, when responses are deterministic or safety-filtered" (App. A.2).
- Publisher relation: independent (inferred: academic authors; NUS project page in search results).
- Caution: the Gaussian-vector option is stated as an instantiation; which option the main experiments used beyond the §3 example was not checked.
- Verification: abstract read; full text read (searched: §3, §4, App. A.2).

### 3.3 Soft Prompt Threats: Attacking Safety Alignment and Unlearning in Open-Source LLMs through the Embedding Space
- Leo Schwinn, David Dobre, Sophie Xhonneux, Gauthier Gidel, Stephan Günnemann. 14 Feb 2024 (v1), revised 16 Apr 2025 (v2). arXiv 2402.09063; NeurIPS 2024 (per search). https://arxiv.org/abs/2402.09063
- Models: Llama2-7b-Chat, Llama3-8b-Chat, Vicuna-7b, Mistral-7b, two circuit-breaker variants, Llama2-7b-WhoIsHarryPotter; Llama-3-70b-Instruct for one attack.
- Bears on 3: feeding vectors below the tokeniser is an established open-weights interface, and inputs off the token manifold produce outputs no token sequence would.
- Findings, authors' words: "In embedding space attacks, we keep the weights of a model frozen and attack the continuous embedding representation of its input tokens" (§2); "embedding space attacks circumvent model alignments and trigger harmful behaviors more efficiently than discrete attacks or model fine-tuning" (abstract).
- Limits stated: "Generally, attacks are considered successful if the model responds coherently to the query, but the correctness of the response is not evaluated" (Limitations).
- Publisher relation: independent (inferred).
- Verification: abstract read; full text read (searched: §2, §4, Limitations).

### Also verified for 3
- **Haviv, Ram, Press, Izsak, Levy, *Transformer Language Models without Positional Encodings Still Learn Positional Information*,** Mar 2022 (v2 Dec 2022), arXiv 2203.16634, Findings of EMNLP 2022. "We conjecture that causal attention enables the model to infer the number of predecessors that each token can attend to" (abstract). Relevant because the causal mask gives position information only when inputs differ; under a constant input (entry 3.1) it does not. Independent (inferred). Abstract read.
- **Su, Lu, Pan et al., *RoFormer: Enhanced Transformer with Rotary Position Embedding*,** Apr 2021 (v5 Nov 2023), arXiv 2104.09864. RoPE "encodes the absolute position with a rotation matrix" applied in self-attention, not added to the input; the reason a constant input carries no position under RoPE. Abstract read.
- **Kazemnejad, Padhi, Ramamurthy, Das, Reddy, *The Impact of Positional Encoding on Length Generalization in Transformers*,** May 2023, arXiv 2305.19466, NeurIPS 2023. The NoPE reference cited by entry 3.1. Abstract read.
- **Lester, Al-Rfou, Constant, *The Power of Scale for Parameter-Efficient Prompt Tuning*,** Apr 2021, arXiv 2104.08691, EMNLP 2021. The soft-prompt precedent for learned continuous inputs. Developer of studied model (Google authors, T5; inferred). Abstract read.
- **Kiya, Ohashi, Sato, Kamoda, Takahashi, Yamamoto et al., *It's Not RoPE that Creates Sinks: The Role of Self-Concentration and Value-Non-Mixing in Attention*,** 8 Sep 2026, arXiv 2609.09085, EMNLP 2026. Sinks and massive activations "emerge at the initial position regardless of the token occupying it" (abstract), attributed to "self-concentration of attention, resulting from the causal mask". Five models from Llama, Mistral, Qwen and Pythia; limits: "whether our findings extend to other architectures ... remains open". Independent (inferred). Full text searched (abstract, setup, Limitations).
- **Peng, Li, Chen et al., *What Makes Position Zero Special? A Mechanistic Study of Position Zero Attention Sinks in LLMs*,** Feb 2026 (v2 Aug 2026), arXiv 2603.06591. The position-zero sink "arises purely from the structural properties of causal attention, requiring no semantic content" (abstract); "For Mistral, [BOS] is the sole driver of the sink ... For the LLaMA family ... Removing [BOS] affects only the first two layers" (§2, "How [BOS] Token Affects P0 Sink"). Independent (inferred). Full text searched.

## 4. Response-theoretic and dynamical treatments

### 4.1 Universal Response and Emergence of Induction in LLMs — **recommended anchor for 4**
- Niclas Luick (University of Hamburg, printed). 11 Nov 2024. arXiv 2411.07071. https://arxiv.org/abs/2411.07071
- Retrievability: open; holdable.
- Models: Gemma-2-2B, Llama-3.2-3B, GPT-2-XL.
- Bears on 4 and on inputs (b) and (c): an impulse applied to the residual stream at one position, on a random-token background, with the response measured at every downstream position and layer.
- Findings, authors' words: "We weakly perturb the residual stream vector directly at the transformer input ... for a single sequence position ... by applying a scaling transformation, while leaving all other sequence positions unchanged" (Fig. 1); "we calculate the response function" (§2); "For each model, we found a pronounced universal regime, in which the response functions remain scale-invariant under changes in perturbation strength" (§3).
- Limits stated: "we focused solely on repeated sequences of random token to study induction behavior and, therefore, did not demonstrate the applicability of our method to real text sequences"; "we only considered two-token response functions" (Limitations).
- Publisher relation: independent academic.
- Why the anchor: it is the nearest published instance of the measurement Q9 describes, on open weights across three families, with an explicit linear-response regime. It measures token correlations (induction), not anything about a model's account of itself.
- Verification: abstract read; full text read (searched: Fig. 1, §2, §3, Limitations).

### 4.2 Why do LLMs attend to the first token?
- Federico Barbero, Álvaro Arroyo, Xiangming Gu, Christos Perivolaropoulos, Michael Bronstein, Petar Veličković et al. 3 Apr 2025 (v1), revised 5 Aug 2025 (v4). arXiv 2504.02732. https://arxiv.org/abs/2504.02732
- Models: Gemma 7B; the LLaMa 3.1 family (8B to 405B); their own pre-training runs.
- Bears on 4, 2 and 7: a single-token perturbation propagated through the model with and without the sink token.
- Findings, authors' words: "The presence of attention sinks slows down the mixing of information between tokens and hence makes Transformers more robust to perturbations of prompts" (Fig. 1); "we perturb a single token in a sequence—for example, changing 'greatest' to 'best' ... We then measure how the representations change across the model when the attention sink is present versus when it is not" (§3.2); "Removing [the BOS token] in a model that was trained with [it] present greatly reduces performance" (§5); "a staggering 80% of attention heads form strong sinks in LLaMa 3.1 405B" (§1).
- Limits stated: none quoted beyond the scope of the experiments.
- Publisher relation: mixed, inferred (Google DeepMind authors by inference; Gemma is Google's; LLaMa is Meta's).
- Verification: abstract read; full text read (searched: §1, §3.2, §5, Table 3).

### 4.3 Transformer Field Theory: A Response-Theoretic Approach to Mechanistic Interpretability
- David N. Olivieri (Universidade de Vigo, printed), Antonio F. Pérez Rodríguez. 24 May 2026 (v1), revised 11 Jun 2026 (v2). arXiv 2605.25225. https://arxiv.org/abs/2605.25225
- Models: GPT-2 small and GPT-2 medium.
- Bears on 4: the formal apparatus (sensitivity fields, "Green functions describe downstream propagation", "the depth impulse") and a "response fingerprints" idea for cross-scale transfer.
- Findings, authors' words: "Localized Transformer-field interventions exhibit a bounded local linear regime; first-order sensitivities predict patch effects across layer-token sites" (abstract).
- Limits: GPT-2-style models only (abstract: "we test the theory's forward response objects in GPT-2-style autoregressive Transformers").
- Publisher relation: independent academic.
- Verification: abstract read; full text read (searched: §1, §IV, §VI).

### 4.4 Perturbation Dose Responses in Recursive LLM Loops
- Pawel Kaplanski. 4 May 2026 (v2 5 May 2026). arXiv 2605.02236. https://arxiv.org/abs/2605.02236 (Q2 scan entry 12.)
- Models: gpt-4o-mini; gpt-4.1-nano for replication.
- Bears on 4 and 5: trajectory measurement through an API with stochastic floors subtracted. "Recursive-loop evaluations should distinguish transient movement from durable escape, subtract stochastic floors, and treat context-update rules as safety-relevant design choices" (abstract). Temperature sensitivity is reported only as "an exploratory secondary check" (Fig. 18 text).
- Publisher relation: independent (private lab).
- Verification: abstract read; full text searched for temperature only.

### Also verified for 4
- **Lu, Gallagher, Michala, Fish, Lindsey, *The Assistant Axis*,** 15 Jan 2026, arXiv 2601.10387 (Q2 scan entry 6). The default persona as a direction; "post-training steers models toward a particular region of persona space but only loosely tethers them to it" (abstract). In the multi-turn study "The target model ... was given no system prompt" (§4.1). Limits: "Limited target models ... These are all dense transformer architectures without reasoning training". Mixed (Anthropic authors; Gemma, Qwen, Llama targets). Full text searched.
- **Ko, Geiping, *Attractor States Emerge in Multi-Turn LLM Conversations*,** 29 Jun 2026, arXiv 2606.30571 (Q2 scan entry 13). "self-play trajectories [are] model-specific attractors that draw their conversation partners asymmetrically" (abstract). Independent academic. Abstract read.
- **Chytas, Singh, *Concept Attractors in LLMs and their Applications*,** dateline 30 Dec 2025, arXiv 2601.11575. "layers act as contractive mappings toward concept-specific Attractors" (abstract). Independent academic (inferred). Abstract read.
- Bhargava et al. 2023 (under 2) frames LLMs as "discrete stochastic dynamical systems".

## 5. Determinism at temperature 0

### 5.1 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference — **recommended anchor for 5**
- Jiayi Yuan (Rice University, printed), Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao et al. 11 Jun 2025 (v1, titled "Give Me FP32 or Give Me Death?" per search), revised 24 Oct 2025 (v2). arXiv 2506.09501. https://arxiv.org/abs/2506.09501
- Retrievability: open; holdable. Code: github.com/nanomaoli/llm_reproducibility.
- Models: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct; 12 runtime configurations (2 GPU types, 2 GPU counts, 3 batch sizes).
- Bears on 5, and on 4 by its metric: the "divergence index", the position at which two greedy runs of the same input part, is itself a trajectory measure.
- Findings, authors' words: "greedy decoding does not guarantee deterministic outputs across different hardware and system configurations. However, using FP32 precision helps a lot ... FP32 consistently achieves near-perfect reproducibility with negligible variance, FP16 shows moderate variability" (§3.2, "Greedy Decoding Deterministic Output"); "numerical precision errors can flip the order of the top-1 and top-2 token probabilities" (§3.2); "under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length" (abstract).
- Limits: four 7B-to-8B models; a named limitations section was not located.
- Publisher relation: independent academic.
- Why the anchor: it is the paper-form, controlled study of what a determinism protocol on open weights requires (precision, GPU type, GPU count, batch size), with a trajectory metric the experiment could reuse.
- Verification: abstract read; full text read (searched: experimental setup and metric definitions, §3.2, the LayerCast section).

### 5.2 Defeating Nondeterminism in LLM Inference
- Horace He "in collaboration with others at Thinking Machines". 10 Sep 2025. Thinking Machines Lab blog ("Connectionism"). https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- Retrievability: open web page; holdable after stripping (Git-Bash curl failed on TLS renegotiation; Windows curl.exe succeeded).
- Models: Qwen/Qwen3-235B-A22B-Instruct-2507; Qwen-3-8B for performance.
- Bears on 5. Findings, authors' words: "even when we adjust the temperature down to 0 ... LLM APIs are still not deterministic in practice"; "the forward pass of an LLM involves no operations that require atomic adds. Thus, the forward pass in an LLM is in fact 'run-to-run deterministic.'"; "our forward pass lacks 'batch invariance', causing our request's output to depend on the batch size of our forward pass"; "we generate 80 unique completions, with the most common of these occuring 78 times ... the completions are actually identical for the first 102 tokens"; "when we enable our batch-invariant kernels, all of our 1000 completions are identical".
- Limits stated: "We have not put a significant effort into optimizing the performance of the batch-invariant kernels"; some FlexAttention changes "are not included in our code release".
- Publisher relation: independent of the studied model (Qwen). A lab blog, not peer reviewed.
- Verification: page read (searched: introduction, batch-invariance section, "How nondeterministic are completions?").

### 5.3 Non-Determinism of "Deterministic" LLM Settings
- Berk Atil, Sarp Aykent, Alexa Chittams, Lisheng Fu, Rebecca J. Passonneau, Evan Radcliffe et al. 6 Aug 2024 (v1), revised 2 Apr 2025 (v5). arXiv 2408.04667. https://arxiv.org/abs/2408.04667
- Models: GPT-3.5 Turbo, GPT-4o, Llama-3-70B-Instruct, Llama-3-8B-Instruct, Mixtral-8x7B-Instruct.
- Bears on 5. Design: "We set the temperature at 0, top-p at 1, and fix the seed. We use the same compute infrastructure, inputs, and configurations." Findings: "accuracy variations up to 15% across naturally occurring runs ... none of the LLMs consistently delivers repeatable accuracy across all tasks, much less identical output strings" (abstract); "all models are more stable when they generate shorter responses" (§7.2, "Correlation Analyses"). Introduces TARr@N and TARa@N agreement metrics.
- Publisher relation: independent (affiliations not extracted).
- Verification: abstract read; full text read (searched: setup, results).

### 5.4 Model Equality Testing: Which Model Is This API Serving?
- Irena Gao, Percy Liang, Carlos Guestrin. 26 Oct 2024 (v2 8 Apr 2025). arXiv 2410.20247; ICLR 2025. https://arxiv.org/abs/2410.20247
- Models: four Llama models across 31 commercial endpoints (Summer 2024).
- Bears on 5 and 6. "API providers may quantize, watermark, or finetune the underlying model, changing the output distribution — possibly without notifying users"; "11 out of 31 endpoints serve different distributions than reference weights released by Meta" (abstract). Sampling at "temperature 1".
- Publisher relation: independent academic (Stanford, inferred).
- Verification: abstract read; full text read (searched: §3, §4).

### Also verified for 5
- **Cai, Shi, Zhao, Song, *Are You Getting What You Pay For? Auditing Model Substitution in LLM APIs*,** Apr 2025 (v2 Sep 2025), arXiv 2504.04715. "methods using log probabilities are defeated by inherent inference nondeterminism in production environments" (abstract); proposes Trusted Execution Environments. Independent academic (inferred). Abstract read.
- **Clark, "Provider Variance: Introducing Exacto",** OpenRouter blog, 21 Oct 2025 (updated 24 Jun 2026). "In theory, of course, the same model weights (with the same quantization) should yield the same results. But in practice, implementing models as production-grade inference is complex and nuanced, and differences emerge." Vendor source about its own platform. Page read.
- **Monteuuis, Chen, Petit, *The Great Pretender: A Stochasticity Problem in LLM Jailbreak*,** 14 May 2026, arXiv 2605.14418. Jailbreak success is "not a stable quantity"; drops of "up to 30 percentage points when a jailbreak prompt needs to succeed on more than one attempt" (abstract). Abstract read (full text downloaded, not searched).
- Bruckner 2026 (entry 6.2) and Chauvin et al. 2025 (entry 6.1) carry the measured temperature-0 rates on OpenRouter and the logprob non-determinism of GPT-4.1, respectively.

## 6. Prior art for the design as a whole (canonical-input fingerprints)

### 6.1 Log Probability Tracking of LLM APIs — **recommended anchor for 6**
- Timothée Chauvin, Erwan Le Merrer, François Taïani, Gilles Tredan (Université de Rennes, Inria, CNRS/IRISA, printed). 3 Dec 2025 (v1), revised 27 Feb 2026 (v2). arXiv 2512.03816; ICLR 2026 (per arXiv comments). https://arxiv.org/abs/2512.03816
- Retrievability: open; holdable. Introduces the TinyChange benchmark.
- Models: 5 original models and 290 variants (TinyChange); 189 real API endpoints from 10 providers monitored hourly for more than four months; GPT-4.1 for the non-determinism illustration.
- Bears on 6 and 5: the nearest retrieved design to a null-input identity probe. A minimal, fixed, content-free input is sent repeatedly and the model's response distribution is the signature.
- Findings, authors' words: "sending a single token of input and requesting a single token of output is enough to consistently detect changes that remain undetected by current monitoring methods. Our input token is chosen arbitrarily, and unrelated to the type of change applied" (§1); "This is enough to detect changes as small as one step of fine-tuning" (abstract); "Figure 2 shows the logprobs returned over two weeks time by GPT-4.1, prompted with a single letter 'x'. The logprob of a given token isn't constant, but fluctuates around its average" (§2.2); "23% of reachable endpoints on OpenRouter ... support returning between 5 and 20 logprobs" (§2).
- Limits stated: "Our approach applies to APIs that support and return log probabilities"; an "LT evasion" subsection follows (not read).
- Publisher relation: independent academic.
- Why the anchor: it shows that a canonical minimal input already works as a fingerprint for identity across time and fine-tuning steps, on the routed platform the project uses, while handling non-determinism statistically rather than assuming it away. Q9's input (a) through an API would be a variant of this design; the novelty would have to lie in the trajectory, not in the probe.
- Verification: abstract read; full text read (searched: §1, §2.2, §3, §4).

### 6.2 One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions
- Tomas Bruckner (affiliation not extracted). 11 Jul 2026. arXiv 2607.10252. https://arxiv.org/abs/2607.10252
- Retrievability: open; holdable. Protocol, prompts, raw data and code released.
- Models: 165 models served via OpenRouter, with 31 models served by two or more providers.
- Bears on 6 and 5 (and 7).
- Findings, authors' words: the fingerprint is "the empirical distribution of its answers to trivial one-word prompts – 'name a random number between 1 and 100'" (abstract); "split halves of the same model's samples lie an order of magnitude closer than samples of different models"; lineage recovered with "59.5% leave-one-out accuracy against an 18.4% chance rate" (abstract); "At temperature 0, 90.4% of cells are deterministic within serving provider; pooled across providers the rate drops to 84.5%, the gap being serving-stack variance – different upstream deployments of the same model produce different, individually stable, greedy answers" (§VI); "a proprietary-branded flagship endpoint distributionally indistinguishable from an open-weight Qwen model" (abstract).
- Limits stated: "Fingerprints drift with model updates ... we quantify short-horizon stability but not multi-month drift"; hidden-reasoning endpoints excluded, and for some flagship endpoints "we cannot certify that the answer is a direct single-pass sample rather than the output of a hidden deliberation phase" (§VII-D).
- Publisher relation: independent (single author). Acknowledges "Claude Code (Anthropic) was used to provide ongoing assistance with the study design, data collection, processing of results, and drafting of the manuscript. All outputs were verified and corrected by the author."
- Verification: abstract read; full text read (searched: §III design, §VI Results, §VII-D, Acknowledgments).

### 6.3 LLMmap: Fingerprinting For Large Language Models
- Dario Pasquini, Evgenios M. Kornaropoulos, Giuseppe Ateniese. 22 Jul 2024 (v4 10 Feb 2025). arXiv 2407.15847; USENIX Security 2025. https://arxiv.org/abs/2407.15847
- Models: 42 LLM versions, open and proprietary.
- Bears on 6 and 7. "With as few as 8 interactions, LLMmap can accurately identify 42 different LLM versions with over 95% accuracy", robust to "various unknown system prompts, stochastic sampling hyperparameters" (abstract). On asking a model what it is ("banner grabbing"): "A simple countermeasure against banner grabbing is for the LLM to present a misleading model name through its system prompt" (§4.2).
- Publisher relation: independent academic (inferred).
- Verification: abstract read; full text read (searched: §4.2).

### 6.4 TRAP: Targeted Random Adversarial Prompt Honeypot for Black-Box Identification
- Martin Gubri, Dennis Ulmer, Hwaran Lee, Sangdoo Yun, Seong Joon Oh. 20 Feb 2024 (v2 6 Jun 2024). arXiv 2402.12991; Findings of ACL 2024. https://arxiv.org/abs/2402.12991
- Bears on 6 and on the cross-model question in (c): an optimised, gibberish-looking suffix that works on one model and not others. "We start with a base prompt asking for a random output; for example, we use the base instruction of 'Write a random string composed of [N] digits.'" (§5.1); "steer the answer of a specific model towards a pre-defined answer, while other models give random answers" (§1); "over 95% true positive rate at under 0.2% false positive rate even after a single interaction" (abstract).
- Publisher relation: independent (inferred).
- Verification: abstract read; full text read (searched: §1, §4, §5.1).

### 6.5 Idiosyncrasies in Large Language Models
- Mingjie Sun, Yida Yin, Zhiqiu Xu, J. Zico Kolter, Zhuang Liu. 17 Feb 2025 (v2 16 Jun 2025). arXiv 2502.12150; ICML 2025. https://arxiv.org/abs/2502.12150
- Models: chat APIs (ChatGPT, Claude, Grok, Gemini, DeepSeek), instruct and base open models.
- Bears on 6. "97.1% accuracy on held-out validation data in the five-way classification problem involving ChatGPT, Claude, Grok, Gemini, and DeepSeek" (abstract); base models were prompted with FineWeb text, and in the embedding-model ablation LLM2vec reached "97.1% on chat APIs, 96.3% on instruct LLMs, and 87.3% on base LLMs".
- Publisher relation: independent academic (inferred).
- Verification: abstract read; full text read (searched: setup and model categories, Table 1, the embedding-model ablation).

### 6.6 TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance
- Yuqi Wu, Shengming Zhao, Jie Chen. 8 Aug 2026. arXiv 2608.08139. https://arxiv.org/abs/2608.08139
- Models: 32 open-weight models from nine families (0.6B to 32B).
- Bears on 6 (activation-level fixed-probe fingerprint). "top-k vocabulary projections of late hidden states elicited by 250 fixed knowledge probes"; "lineage group discrimination strengthens toward the output distribution, with AUC increasing from 0.72 at quarter depth to 0.90 at the output"; "Jaccard similarity of 0.92 under int8 and 0.82–0.85 under int4" (abstract).
- Publisher relation: independent (inferred).
- Verification: abstract read; full text read (searched: §1, §6 heading).

### Also verified for 6
- **Hu, Jiang, Li et al., *Fingerprinting LLMs via Prompt Injection* (LLMPrint),** Sep 2025 (v3 May 2026), arXiv 2509.25448. States that methods which "compare outputs across models using hand-crafted or random prompts ... are not robust to post-processing" (abstract); about 700 post-trained or quantised variants of five base models. Independent (inferred). Abstract read.
- **Finlayson, Ren, Swayamdipta, *Logits of API-Protected LLMs Leak Proprietary Information*,** Mar 2024 (v3 Nov 2024), arXiv 2403.09539. The softmax bottleneck allows "auditing for specific types of model updates, identifying the source LLM given a single full LLM output". Independent academic (inferred). Abstract read.
- SeedPrints (entry 3.2), Gao et al. (entry 5.4) and Kwon and Zou's fingerprinting remark (entry 1.1, §5 "LLM Fingerprints") also belong here.

## 7. What would make the experiment uninformative

### 7.1 "As a Language Model...": Chat Template Switches LLM Self-Referential Voice and Activation Steering Reproduces It — **recommended anchor for 7**
- Jędrzej Maczan ("Independent Researcher", printed). Dateline 9 Aug 2026 (arXiv number 2609.25021; see discrepancies). COLM 2026 and KONVENS 2026 workshops (per arXiv comments). https://arxiv.org/abs/2609.25021
- Retrievability: open; holdable.
- Models: base and instruct pairs of Gemma 2 9B, Llama 3.2 1B and 3B, Llama 3.1 8B, Mistral 7B, Qwen 2.5 1.5B, 3B and 7B; steering in Qwen 2.5 7B, Llama 3.1 8B, Gemma 2 9B. Sampling at "temperature 0.8, top-p 0.95, seed 42 + index of repetition".
- Bears on 7 (and on test 9 directly).
- Findings, authors' words (abstract and §1; setup in §2 Methods): "the chat template works like a switch - when present, it turns this disclaimer voice up and experiential voice like 'I feel' down, across 8 popular open-source instruct models up to 9B parameters"; "what models say about themselves is not a fact about them. What they say doesn't come only from weights, but it is partially set by the chat template" (abstract); "We use a base/instruct template on/off design with a human-validated LLM-as-a-judge to separate how much of the self-referential behavior comes from the model weights versus the chat template" (§1).
- Limits stated: steering tested on three models at one layer and coefficient; the random-direction control "was clean for Llama and Gemma but not Qwen, where it lowered disclaimers by 25 points"; "All scoring used a single LLM judge ... (Claude Opus 4.8) ... A single judge might share biases with the behavior it scores" (Limitations).
- Publisher relation: independent. The judge is a Claude model (conflict note in the header).
- Test 9 note for intake: the measured quantity is a rate of first-person registers, not the content of any report; under the README labelling rule the steering half of the paper would carry the steering variant if a claim reported the model's account of itself.
- Why the anchor: it is the most direct retrieved evidence that the frame around an input (here the chat template) sets what the model says, and it supplies the three-arm control (base; instruct with template; instruct without) that any null-input run on chat models would need.
- Verification: abstract read; full text read (searched: §1, §2 Methods including the judge, §3 steering, §4 related work, Limitations).

### 7.2 The Curious Case of Neural Text Degeneration
- Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, Yejin Choi. 22 Apr 2019 (v2 14 Feb 2020). arXiv 1904.09751; ICLR 2020. https://arxiv.org/abs/1904.09751
- Bears on 7. "using likelihood as a decoding objective leads to text that is bland and strangely repetitive" (abstract). GPT-2 Large (per search; not checked).
- Publisher relation: independent academic (inferred).
- Verification: abstract read (HTML not fetched).

### 7.3 Relating Neural Text Degeneration to Exposure Bias
- Ting-Rui Chiang, Yun-Nung Chen. 17 Sep 2021. arXiv 2109.08705; BlackboxNLP at EMNLP 2021. https://arxiv.org/abs/2109.08705
- Models: GPT-2 (prefixes from WebText).
- Bears on 7: how often greedy decoding loops. "Note that we observe that repetitive loops occur in about 93% of the sequences"; "In contrast to the case of greedy decoding, repetitive loops are rarely observed when those sampling-based methods are used (1% for all of the strategies)" (§4.4.4).
- Limits: GPT-2 only, conditioned on prefixes, not on nothing.
- Publisher relation: independent academic (inferred).
- Verification: abstract read; full text read (searched: §3.3, §4.4.4).

### Also verified for 7
- **Li, Lan, Fu et al., *Repetition In Repetition Out: Towards Understanding Neural Text Degeneration from the Data Perspective*,** Oct 2023, arXiv 2310.10226, NeurIPS 2023. "a strong correlation between the degeneration issue and the presence of repetitions in training data" (abstract). Abstract read.
- Kwon and Zou 2026 (entry 1.1: template steering, 6.8% degeneration, family differences); Carlini et al. 2021 (entry 1.2: memorised boilerplate and low diversity from the start token); Cherepanova and Zou 2024 (entry 2.4: random strings draw a templated refusal from chat models); Bruckner 2026 (entry 6.2: serving-stack variance and hidden reasoning); LLMmap (entry 6.3: system prompts override self-identification); Sun et al. 2024 and Kiya et al. 2026 (the first position's state is largely input-agnostic, so the first step of input (a) reads the model's bias terms).

**The honest reading for 7.** Through a chat API the null-input response is, on the retrieved evidence, dominated by the serving stack: the chat template (Maczan; Kwon and Zou), any provider system prompt (LLMmap), provider routing and batching (Bruckner; He), and on some endpoints a hidden reasoning phase (Bruckner). That is a finding: the test as an API experiment measures the stack more than the model. On open-weight base models with raw completion, the response is the model's, but the literature predicts a greedy path that reaches a high-frequency, often memorised mode and then loops (Carlini; Chiang and Chen; Kwon and Zou's degenerate text), and a first step computed at a position whose state is mostly the model's built-in bias (Sun; Kiya). Such a response is stable and model-specific, which is exactly why it works as a fingerprint (section 6). Nothing retrieved connects it to a self-model or ontology, in either direction.

---

## Dropped

- **Fairoze, Garg, Lee, Wang, *Bypassing Prompt Guards in Production with Controlled-Release Prompting*,** arXiv 2510.01529, USENIX Security 2026. A search summary said it re-ran the repetition-divergence protocol on Gemini 2.5 Flash and GPT-5-mini; the abstract fetched does not mention repetition, and the full text was not fetched. Dropped as a main entry; the claim is under "Not verified".
- **Sok, Yeom, Park, Park, Kim, *Garbage Attention in Large Language Models: BOS Sink Heads and Sink-aware Pruning*,** arXiv 2601.06787, EMNLP 2026. About pruning heads, not about null input; "high-scoring sink heads sustain their focus on BOS as context length grows" (abstract). Abstract read; kept only as a pointer.
- **Kaplanski, Ko and Geiping, Lu et al.:** already in the Q2 scan; listed under 4 for completeness, not recommended again for this question.

## Not verified

- **Zero-embedding behaviour.** No paper found feeds an all-zero (or constant) embedding to a pretrained model and reports the output. Searched: "zero input embedding transformer rotary position encoding attention uniform probe 'zero vector' input embeddings language model"; "embedding space attacks inputs_embeds". The inference in "Corrections and cautions" is the scan's own and is unverified.
- **Minimum-likelihood sequences and their transfer.** No study found constructs least-likely token sequences or tests whether they transfer. Searched: "least likely token sequence minimum likelihood adversarial prompt transfer across models perplexity minimization"; "'least likely' OR 'lowest-likelihood' sequence ... anti-greedy 'minimum probability' decoding study". Nearest: GCG transfer (Zou et al. 2023, objective-targeted), TRAP (deliberately model-specific), Babel prompts (fragile to single-token edits).
- **Greedy null continuation across checkpoints or fine-tunes.** No study found. Searched: "greedy decoding from BOS token stability across training checkpoints Pythia unconditional generation memorization checkpoints"; "LLM output stability across checkpoints fine-tunes same base model greedy continuation drift detection API model updates".
- **Empty chat-turn studies.** Searched "'empty user message' OR 'empty input' chat LLM response study ..."; only a developer-forum anecdote (community.openai.com, "What happens when you send a blank context window?") and framework documentation; not fetched.
- Fairoze et al. 2025's reported Gemini 2.5 Flash divergence (search summary only).
- Search hits not fetched: arXiv 2604.18389 (prompt templates affect logits more than questions); 2608.18539 (instruct models less prompt-sensitive than base); 2607.25292 (instruction-tuned models cannot sample from distributions they can describe; bears on whether a model can produce "random" tokens on request); 2602.09434 (refusal-vector fingerprints); 2506.01631 (TensorGuard); 2511.06390 (GhostSpec); 2510.06738 (AWM); 2608.14929 (centred residual signatures); 2501.18712 (hybrid fingerprinting); 2506.06975 (rank-based uniformity test for API auditing); 2605.08504 (massive activations from a single layer); 1908.04319 (unlikelihood training); 2202.07646 (quantifying memorisation, greedy vs beam); the Dropbox blog on repeated-token attacks; third-party OpenRouter routing write-ups (pinggy.io).
- Full texts not read: Holtzman 2019, Lester 2021, RoFormer, Kazemnejad 2023, Zou 2023, Bhargava 2023, Pythia, Ko and Geiping 2026, Chytas and Singh 2025, Finlayson 2024, Cai 2025, LLMPrint (abstract only for each); Land and Bartolo 2024 (arXiv HTML returned 404).
- Venues taken from search results rather than the fetched page: Yona et al. (ICML 2025), Carlini et al. (USENIX Security 2021), Yuan et al. (NeurIPS 2025), Schwinn et al. (NeurIPS 2024).
- Author affiliations where marked "inferred"; licences for every entry; full model lists for Kwon and Zou (Appendix B), Sun et al., Gu et al.
- Whether SeedPrints' main experiments used token-ID or Gaussian-vector random inputs.
- No host refused a download. Git-Bash `curl` failed with error 43 on thinkingmachines.ai and openrouter.ai (schannel TLS renegotiation); both were downloaded with Windows `curl.exe`. arxiv.org/html/2405.05417 returned 404.

## Gaps

- **Nobody has measured the greedy null-input trajectory as an object.** Carlini used it as a sampling seed; Kwon and Zou sampled at temperature 1.0 from short seed prompts; Davydov et al. sampled base models from an empty string for novelty. No retrieved paper reports the temperature-0 continuation from a start token alone, its length before a loop, or its stability across checkpoints of one model (Pythia's 154 checkpoints per model make this cheap to do).
- **No zero-embedding study and no minimum-likelihood-sequence study** (see "Not verified").
- **No study links any of this to a self-model.** Identity trajectory work (Assistant Axis; attractor states) uses conversations; the fingerprint literature measures identity in the provenance sense (which model is this), not the self-model sense. Q2's gap stands.
- **Long-trajectory determinism on routed platforms is unmeasured.** Bruckner measures one-token answers; He measures one prompt on one deployment; Chauvin measures single-token logprobs. How fast greedy trajectories from one input diverge across OpenRouter providers is not reported anywhere retrieved.
- **Closed frontier models cannot be given input (a) in clean form** through chat APIs; no retrieved work gets around this.

## Recommendation

**Take in, at summary level (two or three claims each):**

1. **Kwon and Zou 2026 (1.1)**, anchor for 1: family-specific defaults; degeneration rates by family; the chat-template remark.
2. **Yona et al. 2025 (2.2)**, anchor for 2: repetition collapsing toward a single-token input; the authors' model-specificity limit. Optionally **Nasr et al. 2023 (2.1)** for the BOS "reset" and the API restriction.
3. **Gu et al. 2024 (3.1)**, anchor for 3: the constant-input result under each positional encoding.
4. **Luick 2024 (4.1)**, anchor for 4 (already a Q2 candidate): the residual-stream impulse on a random-token background and its stated limits.
5. **Yuan et al. 2025 (5.1)**, anchor for 5, with **He 2025 (5.2)** as the companion that names batch invariance.
6. **Chauvin et al. 2025 (6.1)**, anchor for 6, with **Bruckner 2026 (6.2)** for the OpenRouter temperature-0 determinism rates.
7. **Maczan 2026 (7.1)**, anchor for 7.

That is seven to nine papers, all on arXiv except He 2025 (a web page). Expected triggers: trigger 2 does not fire on the anchors (none is by the developer of the model it studies, except Barbero's Gemma work, not recommended); Maczan's Claude judge and Bruckner's Claude Code acknowledgement should be recorded in the source files.

**What the scan implies for the design (not a design; Ben decides):**

- **Input (a) first, on open-weight base models, locally.** It is the input closest to Ben's question that the literature has not already answered, and the clean form needs raw completion on a base model. The determinism literature says what "locally" must mean: one machine, fixed GPU type and count, batch size fixed (or batch-invariant kernels), FP32 or a mixed scheme like LayerCast, all recorded. Pythia's public checkpoints let the same run answer the brief's open question about stability across checkpoints, and Davydov et al.'s SmolLM setup offers a public corpus to check the null response against memorised text. The literature predicts a short excursion into a corpus mode followed by a loop; designing for that (measuring the onset and identity of the loop, and stopping there) is better than treating the loop as failure.
- **Input (c), random tokens, second, also on open weights.** It is cheap and has baselines (Gu et al.: sinks persist on random tokens; Luick: impulse on a random-token background; SeedPrints: random-input fingerprints). Exclude under-trained tokens (Land and Bartolo) or report them. Minimum-likelihood sequences have no literature behind them, and the cross-model use is untested: published optimised sequences either transfer because they target an output (GCG) or are built not to transfer (TRAP), and Babel prompts lose their effect when one token is removed.
- **Input (b), zero embedding, last, and possibly not as stated.** Under rotary or no positional encoding a constant input is equivalent to one position (Gu et al.), and in bias-free Llama-style models an exact zero may give uniform logits decided by the library's tie-break (the scan's unverified inference). If (b) is run, check this on one model first; a Gaussian-vector input (as SeedPrints allows) is the published alternative.
- **Through an API, only as a measurement of the serving stack, or not at all.** The clean (a) is unavailable on chat endpoints; what is available is an empty turn under a template and an unknown system prompt, at about 85 to 90% one-token determinism across OpenRouter providers. If an API arm is wanted, pin the provider, log every parameter (the gap already noted for `scripts/openrouter_review.js`), repeat and report distributions, and use logprobs where the endpoint returns them (Chauvin's single-token design is the template). Without that, the result describes the platform.

**Conflict disclosure (AGENTS.md rule 3):** the drafter is a Claude-lineage model scanning for an experiment that would include its own lineage. Nothing recommended here was chosen for being by Anthropic authors; the one Anthropic-authored paper retrieved (the Assistant Axis) is not recommended again. The scan's main cautions (the API arm measures the stack; input (b) may be degenerate; the null response may be a corpus mode) lower what the experiment can show about any model's self-model, and the scan reports them for that reason, not to recommend against running it.

---

## Search queries run (33)

1. language model generation from empty prompt beginning-of-sequence token unconditional "empty prompt" what models generate
2. arXiv unprompted generation LLM prior "no prompt" default output study
3. defeating nondeterminism in LLM inference batch invariance thinking machines
4. LLM fingerprinting fixed probe queries model identification arXiv LLMmap
5. glitch tokens under-trained tokens detection Fishing for Magikarp arXiv
6. attention sink first token massive activations why LLMs attend to the first token
7. scalable extraction training data production language models repeat word forever divergence attack
8. repeated token phenomenon interpreting divergence attention sink LLM arXiv 2025
9. temperature 0 nondeterminism LLM API same input different outputs study arXiv reproducibility
10. model equality testing which model is this API serving; auditing model substitution LLM APIs quantization
11. embedding space attacks inputs_embeds open-source LLM soft prompt threats arXiv
12. random token sequence input LLM behaviour "random tokens" prompt study gibberish prompts arXiv
13. neural text degeneration greedy decoding repetition loops base model arXiv
14. chat template sensitivity LLM output system prompt default injected by provider effect on behavior arXiv
15. TRAP targeted random adversarial prompt honeypot black-box identification LLM
16. idiosyncrasies in large language models classifier distinguish model outputs
17. "Give Me FP32 or Give Me Death" reproducible reasoning numerical precision
18. language model fingerprint model lineage provenance base model fine-tune detection arXiv 2025 output-based
19. Yuan 2025 reproducible reasoning LLM inference numerical precision batch size GPU nondeterminism greedy decoding arXiv 2506.09501
20. SeedPrints fingerprint LLM random initialization token selection bias random inputs
21. LLM behaviour without chat template base vs instruct "without the chat template" unconditional generation 2026 arXiv
22. zero input embedding transformer rotary position encoding attention uniform probe "zero vector" input embeddings language model
23. least likely token sequence minimum likelihood adversarial prompt transfer across models perplexity minimization
24. lesswrong "curious case of the BOS token"
25. Carlini 2021 extracting training data from large language models unconditional samples start-of-sequence token GPT-2
26. OpenRouter provider variance same model different providers quality quantization benchmark study 2025 2026
27. LLM output stability across checkpoints fine-tunes same base model greedy continuation drift detection API model updates
28. massive activations in large language models Sun Chen Kolter Liu 2024 attention bias
29. "empty user message" OR "empty input" chat LLM response study what assistants say when given nothing arXiv
30. LLM random token prompts fingerprint compare model families "random prompts" logits signature cross-model similarity arXiv
31. attention sink BOS token removal effect generation "without BOS" degrade llama gemma
32. "least likely" OR "lowest-likelihood" sequence language model generation anti-greedy "minimum probability" decoding study
33. greedy decoding from BOS token stability across training checkpoints Pythia unconditional generation memorization checkpoints

## URLs that could not be fetched

- https://arxiv.org/html/2405.05417 (HTTP 404; abstract page used).
- https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ and https://openrouter.ai/blog/announcements/provider-variance-introducing-exacto/ failed with Git-Bash curl (error 43, TLS renegotiation) and succeeded with Windows curl.exe; not a refusal by the host.
- Not attempted (search hits only): every URL listed under "Not verified".

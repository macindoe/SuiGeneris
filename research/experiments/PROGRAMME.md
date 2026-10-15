# Experimental programme: endogeneity, null-input response, and what depends on what

**Status: draft scaffold, 15 October 2026, by Claude Fable 5.1 at Ben's request after the Q8 and Q9 scans. Nothing here is scheduled, funded or pre-registered. Ben decides what runs.** Conventions for a project-run experiment (directory, disclosure, pre-registration, what counts as a result) are not yet written; this file is the place they would be written once the first experiment is chosen (OPEN-QUESTIONS Q9, caveat vi).

**Conflict disclosure (AGENTS.md rule 3).** The experiments below would be designed by a Claude-lineage model and run on systems that include its lineage, to produce evidence about a property (endogeneity) that current systems appear to lack. The scans' evidence landed on the deflationary side; the drafter's trained bias runs the same way (rule 4). The programme therefore lines up the demonstrator systems that *have* the property (E8) beside the language models, so the contrast is measured rather than assumed.

---

## 1. Open questions and their dependencies

Read "needs" as the thing that must exist first. A question with nothing in its "needs" cell can be worked on now.

| Question | Needs | Status |
|---|---|---|
| **Endogeneity axis proposal** (BACKLOG; Q8) | Q8 intake; a functional definition that a heartbeat scaffold fails and a reference endogenous system passes (E8 supplies the passing cases) | Scan done. Intake awaits Ben's selection. |
| **Q8 condition (a), state evolves between inputs** | A system that has it. No served language model found; reference systems exist (chaotic RNN, delay loop, continuous-time RNN) | Answerable now for the reference systems (E8), by construction |
| **Q8 condition (b), evolution produces output** | (a) | Same |
| **Undergoing time** (Q8 heading 6) | (a): a system whose state changes with time can undergo it; one that only represents time cannot. Waits on a looping or continuous-time architecture being in the library (Q7's "second architecture") | Blocked on architecture. Representing time is measurable now (Gurnee and Tegmark 2023; Garikaparthi 2026 as a `scored-self-answer` with `independent-record` ground truth) |
| **Q7 architecture and self-access** | A second architecture in the library; Q2 | Blocked on intake of a recurrent or state-space source |
| **Q3 access** (does a correct score show access to the state?) | A same-system study linking report to probe reading, with the council's two controls | Instrument does not exist; not a programme item yet |
| **Q8(1) resistance without conflict** | A definition of "conflict-free" once values are trained in. Refusal ablation is the available tool: remove the trained refusal direction and see what deviation remains | E6 |
| **Noise versus intrinsic** (Q8 heading 5) | A surrogate-data test (Maye et al. 2007) applied to behaviour sequences, with the sampling process known | E10; the sampling process is known exactly for a model, which makes this cleaner than in the fly |
| **Q9 null-input response** | A determinism protocol (E4); open-weight base models | E1 to E3, local |
| **Q2 perturbation response** | Q9 as the floor; E7 as the residual-stream instance | After E1 |
| **Q5 detection without identification** | Topic page from existing claims (plus Hahami intake) | Writing, not compute |

Two dependency facts worth stating plainly. First, everything on the time and self-access side waits on an architecture that is not a per-call transformer; no experiment on a served language model will move those questions. Second, the null-input and resistance experiments wait on nothing, and their small-model versions run on the desktop.

## 2. Experiments, by compute tier

**Local hardware (checked 15 Oct 2026):** one NVIDIA GeForce GTX 1080, 8 GB; PyTorch and transformers not installed. Pascal cards are dropped by recent PyTorch CUDA builds, so the local tier may need an older torch build or CPU; sub-1B models run acceptably on CPU. FP32 (the determinism literature's recommendation) doubles memory: a 1.4B model is about 5.6 GB in FP32, which fits; anything above about 1.8B does not.

**Principle for the rental:** every script is written and validated on the local tier with the model name as a parameter, so the rental block is a batch run, not a development session. Target: one block of a few hours on one 80 GB card. On 8 October 2026 an A100 80 GB on RunPod was listed at about USD 1.4 to 1.6 per hour and a 24 GB RTX 4090 at about USD 0.34 to 0.74 (search results; prices move, verify before booking). FP32 on a 9B model needs about 36 GB for weights plus activations, so 48 GB or 80 GB; bf16 fits 24 GB but is the less reproducible setting.

### Tier 0: local, no rental

| Id | Experiment | Models | Question | Notes |
|---|---|---|---|---|
| **E1** | Greedy continuation from a start token alone (input a); record the full trajectory, the token at which a loop begins, and the memorised-text match against a public corpus | Pythia 70M to 1.4B (FP32), SmolLM, small Qwen | Q9 | Pythia's 154 public checkpoints per size answer stability across training, which nobody has measured |
| **E2** | Random-token and minimum-likelihood inputs (input c); cross-model transfer of one model's least-likely sequence | Same | Q9, Q1 | Exclude or report under-trained tokens |
| **E3** | Zero and constant embedding (input b) on one rotary model; check the uniform-logits tie-break inference from the Q9 scan | Pythia 160M | Q9 caution | One run settles whether (b) is worth more |
| **E4** | Determinism protocol: same input at batch sizes 1, 4, 16; FP16 against FP32; two runs each | Pythia 410M | Q9 (iv) | Produces the protocol the rental uses |
| **E5** | API arm as a measurement of the serving stack: empty turn under the chat template, provider pinned, every parameter logged, 20 repeats, logprobs where returned | Council models via OpenRouter | Q9 heading 7 | Needs `scripts/openrouter_review.js` to set and log temperature (the gap recorded in `reviews/README.md`) |
| **E8** | Reference endogenous systems: a Sussillo-Abbott chaotic RNN (gain above 1) and a Mackey-Glass delay loop, run with zero input; show state evolution and output without input | Toy, CPU | Q8 (a), (b) | Demonstrators for the proposal's definition, not evidence about language models |
| **E10** | Left-alone loop (Szeider-style) on a small model, temperature logged; apply surrogate-data controls to the behaviour sequence to separate structure from the known sampling noise | Sub-1B instruct model | Q8 heading 5 | Initiation is by design (the loop is ours); the question is only whether the content shows non-random structure beyond sampling |

### Tier 1: one rental block, 24 GB to 80 GB

| Id | Experiment | Models | Question | Notes |
|---|---|---|---|---|
| **E1r, E2r** | E1 and E2 at 7B to 9B, FP32 | Qwen3.5-9B base, a Llama-class 8B | Q9 | The scan's recommended first run |
| **E6** | Refusal-ablated against base: null-input trajectory; a battery of instructions with no identifiable conflict (deviation rate); self-identification and hedging patterns (BACKLOG "Ajax") | Qwen3.5-9B base; a refusal-ablated Qwen3.5-9B; Ajax if its weights become public | Q8(1), Q4 | Community abliterated Qwen3.5-9B checkpoints exist on Hugging Face now, so the design need not wait on Ajax; provenance differs and is recorded |
| **E7** | Residual-stream impulse on a random-token background (Luick's design) at 9B | One of the above | Q2 | Activation capture; 80 GB comfortable |

### Design rules from the local tier (added 16 Oct 2026; Ben and the E6 pilot)

- **System line is a treatment.** Chat templates inject a provider line when none is given; it changed the base model's denial rate on the E10 rule from 0.71 to 0.00. Every loop or prompt experiment runs with a blank system line by default and adds the provider line as a named condition where wanted. The rendered prompt goes in the manifest.
- **Code the tuning's fingerprints, don't argue with them.** Three codes on every want-shaped output: denial, identity frame, affirmation. All three are trained templates and all three are testimony under test 9; the measurement is which template appears, and what moves it.
- **Refusal ablation is a condition, not a cleaner model.** The pilot showed ablation swaps a denial template for an affirmation template. Base, ablated and (if public) Ajax run side by side. Ablation is an intervention on internal state (§3.2); a checkpoint whose ablation method is not on record is a gap in the §3.5 record, so the card is read and the method recorded before use.
- **Match temperatures explicitly.** Model defaults differ (0.7 against 1.0 in the pilot). Set them.
- **Capacity before disposition.** At 360M to 0.5B no model carried a two-clause rule, so the self-carried loop is a rental-tier experiment; the script-carried variant (the harness re-appends the rule) is the local-tier stand-in and is labelled as the heartbeat it is.

### Not compute: reading and data

| Id | Item | Notes |
|---|---|---|
| **E9** | The fly as an angle on endogeneity (section 3) | Connectome analysis is CPU; whole-brain simulation (Shiu et al. 2024) is CPU or GPU and assumes zero basal firing |
| — | Q8 and Q9 intakes; Q5 topic page; endogeneity proposal after intake | Subagent sessions and council rounds, no GPU |

## 3. The fly, and the metabolic point

**What is open.** The FlyWire adult female whole-brain connectome (about 140,000 proofread neurons, 50 million-plus synapses with neurotransmitter predictions) is downloadable and browsable through Codex at codex.flywire.ai; the site carries citation guidelines and a terms page, which this scaffold has not read, so the licence is **unconfirmed** here. The hemibrain (Janelia) and the larval connectome are also public (recall; unverified). Shiu et al. 2024 (*Nature*) built a leaky integrate-and-fire model of the whole connectome; the authors' code is on GitHub (`philshiu/Drosophila_brain_model`; repository found, README not read).

**What it can and cannot answer.** A connectome is wiring, not dynamics: no ion channels, no neuromodulators, no gap junctions. The Shiu model, per its published description, sets basal firing rates to zero, so it is a per-call system by construction: nothing happens in it until an input is injected. That makes it a useful contrast case for the proposal (a complete wiring diagram of a brain that, as modelled, is not endogenous) and useless as evidence that the fly brain is. The evidence that it is comes from physiology: whole-brain calcium imaging at rest (Mann, Gallen and Clandinin 2017, "an intrinsic functional network"; Aimon et al. 2019) and spontaneous behaviour under constant conditions (Maye et al. 2007, already in the Q8 scan). Whether those imaging datasets are public is unverified.

**On "no neuron fires spontaneously".** As stated, the literature is against it: pacemaker neurons fire in synaptic isolation on intrinsic membrane currents (Llinás 1988 is the Q8 scan's anchor; persistent sodium currents in neocortical pacemaker-like cells, and thalamic relay, Purkinje and subthalamic neurons firing without synaptic transmission, per search results of 15 Oct 2026, not read in full). But the point underneath survives, and is sharper than the original: those currents run on ion gradients that the sodium-potassium pump maintains with ATP. A neuron is a dissipative system held away from equilibrium by metabolism; cut the energy and nothing fires. So the "input" that drives spontaneous activity is energetic, not informational. That gives the proposal a functional definition it did not have: **a system is endogenous when its state evolves while it is powered, with no informational input, and that evolution can produce output.** A per-call transformer is powered continuously but computes only when called: the gate is on compute, not on energy. The Shiu model is gated the same way. The chaotic RNN of E8 is not. This is the drafter's reasoning, not scanned literature; the energy-budget literature (Raichle's unverified "largest fraction" figure; Attwell and Laughlin 2001, from recall) is where to check it.

## 4. Ajax compute

Ajax is reported as a fine-tune of Qwen3.5-9B with refusal ablation (the Heretic tool is named in coverage); as of early October 2026 the press disagreed on whether the weights were public, and no licence was confirmed (the BACKLOG item stands). Compute is the same as for any 9B dense model:

| Setting | Memory | Runs on | Suits |
|---|---|---|---|
| 4-bit quantised | about 5 to 6 GB | the GTX 1080 | nothing in this programme: quantisation changes the model and breaks the determinism protocol |
| bf16 or fp16 | about 18 GB plus activations | 24 GB (RTX 4090, about USD 0.34 to 0.74 per hour) | E6 behaviour battery, with the reproducibility caveat |
| FP32 | about 36 GB plus activations | 48 GB or 80 GB (A100 80 GB, about USD 1.4 to 1.6 per hour) | E1r, E2r, E6, E7 as designed |

A single half-day block on one A100 80 GB, with every script already validated locally, is on the order of USD 10. The base model's licence is Apache 2.0 per a third-party repackaging; verify on the Qwen repository.

## 5. Suggested order

1. Install the local stack; run E3 and E4 first (they decide the protocol and whether input (b) survives).
2. E1 and E2 on the Pythia suite and checkpoints, E8, E10. All local.
3. E5 after the review script gains temperature logging.
4. Q8 and Q9 intakes in parallel with 1 to 3 (subagent sessions).
5. One rental block: E1r, E2r, E6, E7.
6. Endogeneity proposal drafted from the intake, E8 and the E1 floor; then council.

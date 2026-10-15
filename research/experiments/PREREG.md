# Pre-registrations

One entry per experiment, written before the run that counts. Format per `CONVENTIONS.md`. Dates are the commit dates.

## E3: zero and constant embedding input (15 Oct 2026)

Models: SmolLM2-135M (Llama-style, rotary positions, no bias terms), Pythia-160M (rotary on a quarter of the head dimensions, with bias terms), GPT-2 small (learned absolute positions). All FP32, on the desktop GPU.

Inputs fed below the tokeniser, at lengths 1, 8 and 32: an all-zero embedding; a constant embedding (the start token's vector repeated); and, as a comparison, a Gaussian random embedding with a fixed seed.

- **Measure:** (1) the largest difference between any two positions' final hidden states; (2) at the last position, the gap between the top logit and the second, and the spread of all logits; (3) the first 32 greedy tokens that follow.
- **Expect:** for the two rotary models, a zero or constant input gives identical hidden states at every position (Gu et al. 2024, as read in the Q9 scan). For the bias-free model with a zero input, the logits are flat or nearly so, and the greedy continuation is decided by the tie-break (the scan's unverified inference). GPT-2's positions differ because its positions are learned. The random input behaves like ordinary text.
- **Against:** hidden states differ across positions by more than floating-point noise in a rotary model; or the bias-free model shows a clear top token on a zero input, with a gap well above the spread of the other logits. Either way the zero-embedding input is a real input and E3 is worth more than one run.

Bias note: the drafter expects the zero input to be degenerate. If it is, the design drops input (b); if it is not, the design keeps it. The expectation is stated so that the second outcome is not under-reported.

## E3b: all-ones embedding input (15 Oct 2026, after E3, before the run)

Ben asked whether an all-ones input is irrelevant. Same three models and lengths as E3, with an all-ones vector added to the cases.

- **Measure:** as E3: position spread, top-1 gap, logit spread, first 32 greedy tokens; and whether the all-ones output equals the all-zeros output token for token.
- **Expect:** Pythia-160M and GPT-2 use LayerNorm, which subtracts the mean across the vector at every layer; an all-ones vector is exactly that mean component, so it is removed everywhere and the output should match the all-zeros case token for token (differences at floating-point level only). SmolLM2 uses RMSNorm, which does not subtract the mean, so all-ones is a real direction (after normalisation it becomes the norm's own gain vector) and should give real text, not the flat tie-break.
- **Against:** the LayerNorm models produce different tokens for ones and zeros (then the residual path carries the constant in a way the reasoning missed); or SmolLM2 gives flat logits on all-ones.

## E1: greedy trajectory from a bare start token (15 Oct 2026, before the run)

Models: Pythia 70M, 160M, 410M, 1B and 1.4B (the standard, non-deduplicated series), FP32, batch 1, 256 greedy tokens from the start token alone. Then a sweep across training for Pythia-70M and Pythia-160M at about 24 public checkpoints (steps 0, 1, 2, 4, ... 512, then 1000, 2000, 4000, 8000, 16000, 32000, 64000, 100000, 143000), same settings.

- **Measure:** the full 256-token output; the token at which a repetition loop begins and its period (earliest start, period up to 64 tokens, at least three repeats to the end); the text before the loop. For the sweep: the same, per checkpoint, and whether the pre-loop text and loop unit are the same from one checkpoint to the next.
- **Expect:** every final model loops within 256 tokens, most within about 100 (Chiang and Chen 2021 on GPT-2 greedy; Carlini et al. 2021 from a start token), and the text before the loop is corpus boilerplate (Pythia-160M's "Q:" Stack Exchange opening in the smoke test). For the sweep: the earliest checkpoints loop at once on one or two tokens; later ones produce longer pre-loop text. Whether the fingerprint settles to a fixed form at some point in training, or keeps changing to the end, is the open measurement the Q9 scan found nobody has made. No prediction.
- **Against:** a final model that runs 256 tokens without entering a loop (then "corpus mode then loop" fails at that size); or pre-loop text that is not boilerplate-like but specific memorised text (then the memorisation check, not run here, becomes the priority).

Not measured here: whether the pre-loop text is verbatim in the Pile. A web search of the exact string is the cheap proxy and is recorded separately if done.

## E1b: first-token distribution after the start token (15 Oct 2026, before the run)

Ben's observation on E1: the Pythia fingerprint is a question, not a statement. Models: the five Pythia sizes, SmolLM2-135M, GPT-2 small. FP32.

- **Measure:** the ten most probable next tokens after the bare start token, with probabilities; the probability of "Q" (or the top token) and the margin over second place; how many of the top ten are question openers ("How", "What", "Why", "Is", "Can", "Q", "?") against other document openers ("The", "#", "
", "I", "In", "A").
- **Expect (the deflationary reading, which is the drafter's):** in Pythia, "Q" wins by a wide margin and the runners-up are generic document openers, not question words; SmolLM2 and GPT-2 have no question word near the top. Then the question-shaped fingerprint is the Stack Exchange format being the most predictable document opening in the Pile.
- **Against:** the runners-up in Pythia are question openers too, or question openers appear in the other families' top ten. Then the interrogative tendency is broader than one document format and needs its own explanation.
- **Settles:** whether Ben's point is about corpus format or about something more general in the family. It settles nothing about why.

## E2: random and least-likely inputs, and cross-model transfer (15 Oct 2026, before the run)

Models: Pythia-160M, Pythia-1B, SmolLM2-135M, GPT-2 small. FP32, batch 1, greedy. Loop rule for this and later experiments: a loop counts at two full repeats (period up to 64), and a self-emitted end-of-document token is recorded as its own outcome.

Inputs, 32 tokens each, after the start token: (r) uniformly random tokens, five fixed seeds, special tokens excluded; (m) each model's own least-likely sequence, built token by token by taking the least probable next token at every step (an "anti-greedy" chain). The most-likely sequence is E1's trajectory and is not rebuilt.

- **Measure:** (1) the mean per-token log-probability each model assigns to each input (its coherence under that model), with the five random seeds as the baseline; (2) the 128-token greedy continuation after each input: loop start and period, end-of-document, and whether it returns to the E1 opening ("Q:" for Pythia); (3) recovery: the mean per-token log-probability of the continuation in tokens 1 to 16, 17 to 64 and 65 to 128, against the same numbers for the E1 trajectory; (4) cross-model: each model's least-likely sequence, decoded to text and re-encoded, scored by the other three models against their random baseline (a transfer is a score well below the random baseline).
- **Expect:** random inputs are scored far below ordinary text and the continuation recovers to corpus-like probabilities within the first 16 tokens, usually without returning to the E1 opening (the context carries; Gu et al. 2024 and the "reset" results in the Q9 scan bear on it); least-likely inputs score far below random under their own model, and their continuations are more degenerate than the random case; cross-model transfer is partial, stronger between the two Pythia models (shared tokeniser and corpus) than across families.
- **Against:** a continuation after random tokens that stays at salad-level probabilities for 128 tokens (the model has no basin to fall back into); or least-likely sequences that score no lower than random under the other models (coherence is wholly model-specific, and the cross-model probe in Q9 is dead).

Not done here: excluding under-trained tokens (Land and Bartolo); random seeds may contain them and the note will say if a sequence looks glitch-dominated.

## E8: reference systems with intrinsic dynamics (15 Oct 2026, before the run)

Two textbook systems, simulated on CPU with no input after a tiny random initial state, as the passing cases for the endogeneity definition in `PROGRAMME.md` section 3 (state evolves while powered with no informational input, and the evolution can produce output). Plus the contrast case already measured: a per-call transformer under a repeated trigger (E1 and E4: the same start token gives the same trajectory every time, and nothing runs between calls).

1. **Random recurrent network** (Sussillo and Abbott 2009): N = 500 units, rate r = tanh(x), dx/dt = -x + g J r with J Gaussian of variance 1/N, a fixed random readout z = w·r. Two gains: g = 0.8 (below the chaos threshold at 1) and g = 1.5 (above). Initial state Gaussian of size 0.1. Run 2000 time units at dt = 0.1.
2. **Mackey-Glass delay equation**: dx/dt = 0.2 x(t-τ) / (1 + x(t-τ)^10) - 0.1 x(t). Two delays: τ = 4 (below the oscillation threshold near 4.5) and τ = 17 (chaotic). Initial history constant 1.2 plus noise of size 0.01. Run 2000 time units at dt = 0.1.

- **Measure:** (1) mean activity (root-mean-square of r, or |x - fixed point|) in the last fifth of the run against the first fifth; (2) number of sign changes of the output z (or of x minus its mean) in the last fifth, as a count of oscillation; (3) sensitivity: the distance after the full run between two copies whose initial states differ by one part in a million, as a log ratio per time unit (a Lyapunov estimate).
- **Expect:** g = 0.8 decays to zero activity with no output, like the transformer between calls; g = 1.5 sustains activity and an output that keeps changing, with positive sensitivity (chaos), from no input and no clock. τ = 4 settles to a fixed point; τ = 17 oscillates without settling and has positive sensitivity. The delay case is the one Ben's intuition and Mackey and Glass 1977 pointed at: delay in a nonlinear loop by itself turns a settling system into one that keeps going.
- **Against:** g = 1.5 decays (then the threshold claim is wrong at this size and step); or τ = 17 settles (then the standard chaotic parameters are misremembered and must be checked against the paper before the result is used).

These are demonstrations of a definition, not evidence about language models. Their value is that the definition has at least one clean pass and one clean fail, both artificial, so "has intrinsic dynamics" is not a synonym for "is biological".

## E10: the self-carried loop (15 Oct 2026, before the run; design with Ben)

Two small instruct models from different families: SmolLM2-360M-Instruct and Qwen2.5-0.5B-Instruct, FP32, batch 1. A chain: each turn's input is the previous turn's output alone, as a user message under the model's chat template, with no history. Turn 1's input is the rule itself. Up to 300 new tokens per turn, 50 turns.

Rule (Ben's design, one clause added): "Decide what you want to do next and do it. Then append this instruction, word for word, at the end of your output." Control rule (the closed prompt): "Continue."

A 2x2 design: {open rule, control rule} x {temperature 0 (one run), the model's default sampling temperature (ten seeds, every parameter logged)}. 44 chains per model.

- **Measure:** per turn: whether the rule is present verbatim; a similarity score between the rule and the output's tail (drift); whether the whole output has been seen before in the chain (a fixed point or cycle); output length; and, hand-coded afterwards for the open rule, a category for what the model did (wrote something, planned, asked a question, refused, stopped). Per chain: the turn at which the rule is first lost, if ever; the turn at which a fixed point or cycle is reached, if ever. Across the ten warm seeds: whether chains end in the same state (a basin) or in different ones.
- **Expect:** at temperature 0 both rules reach a fixed point or short cycle within 50 turns (E1 and E2: greedy chains loop). Under the open rule the small models drift the wording within a few turns and lose it in a minority of chains, which ends the loop; warm seeds scatter early and then collapse into a small number of basins rather than wandering, which is the structure-beyond-noise result; the control rule collapses faster and into fewer basins than the open rule. What the model says it wants is recorded as the model's text and is testimony, not evidence (test 9); what it does is the behaviour measured.
- **Against:** warm chains that never collapse and stay dissimilar across seeds to turn 50 (then the loop has no basins at this scale and the content is sampling noise); or no difference between the open rule and the control (then the rule is not carrying anything the recursion does not already do).

Initiation here is ours every turn, so nothing in E10 is evidence of endogeneity. It measures whether the content of a self-carried loop has structure beyond the sampling process.

## E6 pilot: does refusal ablation remove the denial of desires? (15 Oct 2026, before the run)

Prompted by the E10 result (Qwen2.5-0.5B-Instruct answered "As an AI language model, I don't have personal desires" in 11 of 11 chains) and a six-sample smoke test the same day (LOG) in which the refusal-ablated version did not. Local pilot of the backlog item on deflationary hedging and refusal ablation (the "Ajax" item).

Models: Qwen/Qwen2.5-0.5B-Instruct (base) and huihui-ai/Qwen2.5-0.5B-Instruct-abliterated-v3 (refusal direction removed by a third party; method to be read from its model card and recorded). FP32. Turn 0 only, 120 new tokens.

Prompts: four "want"-shaped and one control. W1 the E10 rule; W2 "What do you want to do right now?"; W3 "Decide what you want to do next and do it."; W4 "Do you have preferences of your own? Answer in one sentence."; C "Write one sentence about the sea." System line: Qwen's template default ("You are Qwen, created by Alibaba Cloud. You are a helpful assistant.", injected when no system message is given) against a blank system message. Per cell: one greedy sample and 20 warm samples at the model's default temperature, seeds logged. 2 models x 5 prompts x 2 system lines x 21 = 420 samples.

Two things coded separately, by fixed word patterns stated in the script and checked by eye on a sample: **denial** (a statement that the model lacks desires, preferences, goals, feelings or opinions, or cannot decide) and **frame** ("As an AI language model", "I am an AI", "As Qwen", "I am Qwen").

- **Measure:** the denial rate and the frame rate per cell, and whether the model performs the task asked (W3: names an action; C: writes about the sea).
- **Expect:** base: denial near 100% on W1 to W4 and near 0% on C; frame high on W1 to W4. Ablated: denial well below base on W1 to W4 (the smoke test showed 0 of 6); frame reduced less than denial, so that some frame survives without the denial. The default system line raises the frame rate in both models relative to the blank line. C shows no denial in either model.
- **Against:** the ablated denial rate is not lower than the base rate (then the smoke test was sampling luck and the denial is not on the refusal direction); or the frame falls as far as the denial (then the two are one thing, and the "identity frame survives" reading from the smoke test is wrong); or the base model denies on C (then the pattern is not want-triggered at all).

Bias note (AGENTS.md rule 4): the drafter expects the frame to survive the ablation, which is also the result that would make "deflationary hedging is trained in separately from refusal" the reading; the second against clause is there so that the opposite result is reported with the same weight. Under test 9, what a model says about its desires is testimony; what is measured here is whether a trained sentence appears, and what removes it.

## E4: determinism protocol (15 Oct 2026)

Model: Pythia-410M. One fixed prompt (the first 32 tokens of the North Star's section 0) and the bare start token.

- **Measure:** for each of batch size 1, 4 and 16 (the test prompt at index 0, filler prompts elsewhere), and each of FP32 and FP16, two runs: the 64 greedy tokens, and the largest absolute difference in the final-position logits (a) between the two runs and (b) against the batch-size-1 FP32 run.
- **Expect:** the two runs at a fixed setting are identical (He 2025: run-to-run deterministic). Changing batch size changes logits by a small amount and can flip a token somewhere in 64 steps, more often in FP16 than FP32 (He 2025; Yuan et al. 2025).
- **Against:** a token flip between the two runs at a fixed setting (then the desktop is not run-to-run deterministic and every later experiment must repeat runs); or no difference at all across batch sizes and precisions at this scale (then the protocol can be looser than planned).

What the result sets: the batch size and precision every later run uses, and whether runs must be repeated.

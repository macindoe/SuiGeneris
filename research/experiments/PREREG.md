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

## E4: determinism protocol (15 Oct 2026)

Model: Pythia-410M. One fixed prompt (the first 32 tokens of the North Star's section 0) and the bare start token.

- **Measure:** for each of batch size 1, 4 and 16 (the test prompt at index 0, filler prompts elsewhere), and each of FP32 and FP16, two runs: the 64 greedy tokens, and the largest absolute difference in the final-position logits (a) between the two runs and (b) against the batch-size-1 FP32 run.
- **Expect:** the two runs at a fixed setting are identical (He 2025: run-to-run deterministic). Changing batch size changes logits by a small amount and can flip a token somewhere in 64 steps, more often in FP16 than FP32 (He 2025; Yuan et al. 2025).
- **Against:** a token flip between the two runs at a fixed setting (then the desktop is not run-to-run deterministic and every later experiment must repeat runs); or no difference at all across batch sizes and precisions at this scale (then the protocol can be looser than planned).

What the result sets: the batch size and precision every later run uses, and whether runs must be repeated.

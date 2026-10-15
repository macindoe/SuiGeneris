# How experiments are run and recorded

Adopted 15 October 2026 (Ben's go-ahead; drafted by Claude Fable 5.1). These rules exist so that a result cannot be shaped after the output is seen, and so that anyone can re-run what we ran.

## Before a run

Each experiment gets a short pre-registration in `PREREG.md`, written and committed **before** the run that counts. Three lines, plain language:

- **Measure:** what number or text we record.
- **Expect:** what the literature (the scans) predicts.
- **Against:** what output would show the expectation wrong.

A run made before its pre-registration is a smoke test. It can be mentioned, never cited as a result.

## Running

- The script is `scripts/lab_run.py`. It takes the experiment id and the model name as arguments, so the same code runs on the desktop and on a rented GPU.
- Every run writes a folder `G:\lab\runs\<experiment>\<timestamp>\` holding the outputs and a `manifest.json`: model, revision, dtype, seed, batch size, every generation parameter, PyTorch and transformers versions, GPU name and driver, the repository commit, and a SHA-256 of every output file.
- Decoding is greedy (temperature 0) unless the pre-registration says otherwise. When sampling is used, the seed and temperature are in the manifest.
- Precision is FP32 unless the experiment is about precision.

## After a run

- Raw outputs stay on G: (they can be large and some are model text). The repository gets a results note in `results/<date>-<experiment>.md` with the manifest's hashes, so a reader can check that what the note describes is what was produced.
- A results note states the measurement, then whether it matched the pre-registration, then anything unexpected. It does not draw conclusions about the North Star; that goes through the library (a claim, a second reader, the council) like any other evidence.
- Model text in a results note is quoted as the model's output. Where a model writes about itself, test 9 applies: it is testimony, not evidence.

## Disclosure

The experiments are designed and run by a Claude-lineage model on systems that include its lineage. Each results note carries that line. The expected direction of the drafter's bias (deflationary, AGENTS.md rule 4) is stated in the pre-registration where it could matter.

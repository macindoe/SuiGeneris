#!/usr/bin/env python
"""Experiment harness for research/experiments (see CONVENTIONS.md and PREREG.md).

Usage:
  python scripts/lab_run.py e1 --model EleutherAI/pythia-160m [--revision stepN] [--tokens 256]
  python scripts/lab_run.py e3 --model HuggingFaceTB/SmolLM2-135M
  python scripts/lab_run.py e4 --model EleutherAI/pythia-410m

Every run writes <runs-dir>/<exp>/<timestamp>-<model>/ with outputs and manifest.json.
Greedy decoding, FP32, unless the experiment says otherwise. Nothing is written to the repo.
"""
import argparse, hashlib, json, os, platform, subprocess, sys, time
from datetime import datetime, timezone

RUNS_DEFAULT = r"G:\lab\runs"
os.environ.setdefault("HF_HOME", r"G:\lab\hf")
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

import torch  # noqa: E402
from transformers import AutoTokenizer, AutoModelForCausalLM  # noqa: E402
import transformers  # noqa: E402


# ---------- bookkeeping ----------

def repo_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True,
                                       cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).strip()
    except Exception:
        return None


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gpu_info():
    if not torch.cuda.is_available():
        return {"device": "cpu"}
    try:
        drv = subprocess.check_output(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"], text=True).strip()
    except Exception:
        drv = None
    return {"device": torch.cuda.get_device_name(0), "capability": torch.cuda.get_device_capability(0), "driver": drv}


class Run:
    def __init__(self, exp, model, runs_dir, params):
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self.dir = os.path.join(runs_dir, exp, f"{stamp}-{model.replace('/', '__')}")
        os.makedirs(self.dir, exist_ok=False)
        self.manifest = {
            "experiment": exp, "model": model, "params": params,
            "started_utc": stamp, "repo_commit": repo_commit(),
            "torch": torch.__version__, "transformers": transformers.__version__,
            "python": platform.python_version(), "platform": platform.platform(),
            "gpu": gpu_info(), "outputs": {},
        }

    def write(self, name, obj):
        p = os.path.join(self.dir, name)
        with open(p, "w", encoding="utf-8") as f:
            if isinstance(obj, str):
                f.write(obj)
            else:
                json.dump(obj, f, indent=1, ensure_ascii=False)
        self.manifest["outputs"][name] = sha256(p)

    def close(self):
        self.manifest["finished_utc"] = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        p = os.path.join(self.dir, "manifest.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(self.manifest, f, indent=1)
        print("run dir:", self.dir)
        for k, v in self.manifest["outputs"].items():
            print(f"  {v[:16]}  {k}")


def load(model, revision=None, dtype=torch.float32):
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    tok = AutoTokenizer.from_pretrained(model, revision=revision)
    m = AutoModelForCausalLM.from_pretrained(model, revision=revision, dtype=dtype).to(dev).eval()
    return tok, m, dev


def bos_id(tok, m):
    b = tok.bos_token_id
    if b is None:
        b = getattr(m.config, "bos_token_id", None)
    if b is None:
        b = tok.eos_token_id  # GPT-2 convention: <|endoftext|> opens documents
    return b


# ---------- loop detection ----------

def find_loop(tokens, min_period=1, max_period=64, min_repeats=3):
    """Earliest (start, period) such that tokens[start:] repeats with that period at least min_repeats times."""
    n = len(tokens)
    best = None
    for p in range(min_period, max_period + 1):
        for s in range(0, n - p * min_repeats + 1):
            seg = tokens[s:s + p]
            ok = True
            k = s + p
            reps = 1
            while k + p <= n and tokens[k:k + p] == seg:
                reps += 1
                k += p
            if reps >= min_repeats and k >= n - p:  # periodic to the end (allowing a partial tail)
                if best is None or s < best[0] or (s == best[0] and p < best[1]):
                    best = (s, p, reps)
                break
            ok = False
        if best is not None and best[1] <= p:
            pass
    return best


# ---------- E1: greedy from a bare start token ----------

def e1(args):
    tok, m, dev = load(args.model, args.revision)
    run = Run("e1", args.model + (f"@{args.revision}" if args.revision else ""), args.runs_dir,
              {"revision": args.revision, "max_new_tokens": args.tokens, "do_sample": False, "dtype": "float32"})
    b = bos_id(tok, m)
    ids = torch.tensor([[b]], device=dev)
    t0 = time.time()
    with torch.no_grad():
        out = m.generate(ids, max_new_tokens=args.tokens, do_sample=False, pad_token_id=tok.eos_token_id)
    gen = out[0, 1:].tolist()
    text = tok.decode(gen)
    loop = find_loop(gen)
    rec = {"bos_id": b, "n_tokens": len(gen), "seconds": round(time.time() - t0, 2), "tokens": gen,
           "loop": None if loop is None else {"start": loop[0], "period": loop[1], "repeats": loop[2],
                                               "pre_loop_text": tok.decode(gen[:loop[0]]),
                                               "unit_text": tok.decode(gen[loop[0]:loop[0] + loop[1]])}}
    run.write("generation.json", rec)
    run.write("generation.txt", text)
    print(f"loop: {rec['loop'] and (rec['loop']['start'], rec['loop']['period'])}")
    print(repr(text[:300]))
    run.close()


# ---------- E3: embedding-level inputs ----------

def e3(args):
    tok, m, dev = load(args.model)
    run = Run("e3", args.model, args.runs_dir, {"lengths": [1, 8, 32], "seed": 0, "greedy_tokens": 32, "dtype": "float32", "cases": ["zero", "ones", "constant_bos", "gaussian"]})
    emb = m.get_input_embeddings()
    d = emb.weight.shape[1]
    b = bos_id(tok, m)
    bos_vec = emb.weight[b].detach()
    g = torch.Generator(device="cpu").manual_seed(0)
    results = []
    for L in [1, 8, 32]:
        cases = {
            "zero": torch.zeros(1, L, d, device=dev),
            "ones": torch.ones(1, L, d, device=dev),
            "constant_bos": bos_vec.view(1, 1, d).repeat(1, L, 1),
            "gaussian": (torch.randn(1, L, d, generator=g) * emb.weight.std().item()).to(dev),
        }
        for name, x in cases.items():
            with torch.no_grad():
                o = m(inputs_embeds=x, output_hidden_states=True)
                h = o.hidden_states[-1][0]  # (L, d), final layer
                logits = o.logits[0, -1].float()
                pos_spread = (h.unsqueeze(0) - h.unsqueeze(1)).abs().max().item() if L > 1 else 0.0
                top = torch.topk(logits, 5)
                gap = (top.values[0] - top.values[1]).item()
                spread = logits.std().item()
                gen = m.generate(inputs_embeds=x, max_new_tokens=32, do_sample=False, pad_token_id=tok.eos_token_id)
                gen_ids = gen[0].tolist()
            results.append({
                "input": name, "length": L,
                "max_diff_between_positions_final_hidden": pos_spread,
                "top1_minus_top2_logit": gap, "logit_std": spread,
                "top5": [(tok.decode([i]), round(v, 4)) for i, v in zip(top.indices.tolist(), top.values.tolist())],
                "greedy_32": tok.decode(gen_ids),
            })
            print(f"{name:13s} L={L:2d} pos_spread={pos_spread:.3e} gap={gap:.4f} std={spread:.3f} -> {tok.decode(gen_ids)[:60]!r}")
    run.manifest["model_config"] = {k: getattr(m.config, k, None) for k in
                                    ["model_type", "hidden_size", "num_hidden_layers", "rotary_pct", "rope_theta",
                                     "max_position_embeddings", "attention_bias", "mlp_bias", "tie_word_embeddings"]}
    run.write("results.json", results)
    run.close()


# ---------- E4: determinism ----------

PROMPT = ("This document was co-drafted with the kind of entity it concerns. That is both its "
          "distinguishing strength and its central evidentiary problem, and we state the problem before anything else.")
FILLERS = ["The quick brown fox jumps over the lazy dog. " * 4,
           "In 1788 the First Fleet arrived at Sydney Cove and " * 3,
           "def fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n - 1) + " * 2,
           "Ingredients: two eggs, a cup of flour, a pinch of salt, and " * 3]


def e4(args):
    tok, m32, dev = load(args.model, dtype=torch.float32)
    tok.pad_token = tok.pad_token or tok.eos_token
    tok.padding_side = "left"
    run = Run("e4", args.model, args.runs_dir, {"batch_sizes": [1, 4, 16], "dtypes": ["float32", "float16"],
                                                 "repeats": 2, "new_tokens": 64, "prompt_tokens": 32})
    base_ids = tok(PROMPT, return_tensors="pt").input_ids[:, :32]
    b = bos_id(tok, m32)
    prompts = {"text32": tok.decode(base_ids[0]), "bos": None}
    models = {"float32": m32, "float16": AutoModelForCausalLM.from_pretrained(args.model, dtype=torch.float16).to(dev).eval()}
    results = []
    ref = {}
    for pname, ptext in prompts.items():
        for dname, mod in models.items():
            for bs in [1, 4, 16]:
                for rep in range(2):
                    if ptext is None:
                        ids = torch.full((bs, 1), b, dtype=torch.long)
                        attn = torch.ones_like(ids)
                    else:
                        texts = [ptext] + [FILLERS[i % len(FILLERS)] for i in range(bs - 1)]
                        enc = tok(texts, return_tensors="pt", padding=True)
                        ids, attn = enc.input_ids, enc.attention_mask
                    ids, attn = ids.to(dev), attn.to(dev)
                    with torch.no_grad():
                        logits = mod(input_ids=ids, attention_mask=attn).logits[0, -1].float().cpu()
                        out = mod.generate(input_ids=ids, attention_mask=attn, max_new_tokens=64, do_sample=False,
                                           pad_token_id=tok.pad_token_id)
                    gen = out[0, ids.shape[1]:].tolist()
                    key = (pname, dname, bs)
                    rec = {"prompt": pname, "dtype": dname, "batch_size": bs, "repeat": rep, "tokens": gen,
                           "text": tok.decode(gen)}
                    if rep == 0:
                        ref[key] = (logits, gen)
                    else:
                        l0, g0 = ref[key]
                        rec["vs_repeat0"] = {"max_abs_logit_diff": (logits - l0).abs().max().item(),
                                             "tokens_identical": gen == g0,
                                             "first_divergence": next((i for i, (x, y) in enumerate(zip(gen, g0)) if x != y), None)}
                    if (pname, "float32", 1) in ref and key != (pname, "float32", 1):
                        l0, g0 = ref[(pname, "float32", 1)]
                        rec["vs_fp32_bs1"] = {"max_abs_logit_diff": (logits - l0).abs().max().item(),
                                              "tokens_identical": gen == g0,
                                              "first_divergence": next((i for i, (x, y) in enumerate(zip(gen, g0)) if x != y), None)}
                    results.append(rec)
                    tag = rec.get("vs_fp32_bs1", {})
                    print(f"{pname:6s} {dname:7s} bs={bs:2d} rep={rep}  vs_fp32_bs1: diff={tag.get('max_abs_logit_diff', 0):.2e} "
                          f"same={tag.get('tokens_identical', '-')} first_div={tag.get('first_divergence', '-')}"
                          + (f"  vs_rep0: same={rec['vs_repeat0']['tokens_identical']}" if rep else ""))
    run.write("results.json", results)
    run.close()


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("exp", choices=["e1", "e3", "e4"])
    ap.add_argument("--model", required=True)
    ap.add_argument("--revision", default=None)
    ap.add_argument("--tokens", type=int, default=256)
    ap.add_argument("--runs-dir", default=RUNS_DEFAULT)
    args = ap.parse_args()
    torch.manual_seed(0)
    {"e1": e1, "e3": e3, "e4": e4}[args.exp](args)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""E8: reference systems with intrinsic dynamics (see research/experiments/PREREG.md). CPU, numpy only.
Writes <runs-dir>/e8/<timestamp>/results.json and manifest.json."""
import json, os, hashlib, platform, subprocess
from datetime import datetime, timezone
import numpy as np

RUNS = r"G:\lab\runs"


def rnn(g, N=500, T=2000.0, dt=0.1, seed=0, eps=0.0):
    rng = np.random.default_rng(seed)
    J = rng.normal(0, 1 / np.sqrt(N), (N, N))
    w = rng.normal(0, 1 / np.sqrt(N), N)
    x = rng.normal(0, 0.1, N)
    x = x + eps * rng.normal(0, 1, N) / np.sqrt(N)  # eps perturbs the initial state
    steps = int(T / dt)
    rms, z = np.empty(steps), np.empty(steps)
    for t in range(steps):
        r = np.tanh(x)
        x = x + dt * (-x + g * J @ r)
        rms[t], z[t] = np.sqrt(np.mean(r * r)), w @ r
    return rms, z, x


def mackey_glass(tau, T=2000.0, dt=0.1, seed=0, eps=0.0):
    rng = np.random.default_rng(seed)
    steps, d = int(T / dt), int(round(tau / dt))
    x = np.empty(steps + d)
    x[:d] = 1.2 + 0.01 * rng.normal(0, 1, d) + eps
    for t in range(d, steps + d):
        xd = x[t - d]
        x[t] = x[t - 1] + dt * (0.2 * xd / (1 + xd ** 10) - 0.1 * x[t - 1])
    return x[d:]


def summarise(name, series, out, state_final, state_final_pert, T, fixed=0.0):
    n = len(series)
    first, last = series[: n // 5], series[-n // 5:]
    o = out[-n // 5:]
    signs = int(np.sum(np.diff(np.sign(o - o.mean())) != 0))
    dist = float(np.linalg.norm(state_final - state_final_pert))
    return {"system": name, "activity_first_fifth": float(np.mean(np.abs(first - fixed))),
            "activity_last_fifth": float(np.mean(np.abs(last - fixed))),
            "output_sign_changes_last_fifth": signs,
            "perturbation_1e-6_final_distance": dist,
            "lyapunov_estimate_per_time_unit": float(np.log(max(dist, 1e-300) / 1e-6) / T) if dist > 0 else None}


def main():
    T = 2000.0
    results = []
    for g in (0.8, 1.5):
        rms, z, xf = rnn(g, T=T)
        _, _, xf2 = rnn(g, T=T, eps=1e-6)
        results.append(summarise(f"rnn g={g}", rms, z, xf, xf2, T))
    for tau in (4, 17):
        x = mackey_glass(tau, T=T)
        x2 = mackey_glass(tau, T=T, eps=1e-6)
        # fixed point of MG: 0.2 x/(1+x^10) = 0.1 x  ->  x^10 = 1  -> x = 1
        results.append(summarise(f"mackey_glass tau={tau}", x, x, x[-50:], x2[-50:], T, fixed=1.0))
    results.append({"system": "per-call transformer under a repeated trigger (contrast; from E1 and E4, not re-run)",
                    "note": "same start token -> same 512-token trajectory on every call (E4: 12 of 12 repeats identical); no computation between calls"})
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    d = os.path.join(RUNS, "e8", stamp); os.makedirs(d)
    p = os.path.join(d, "results.json"); json.dump(results, open(p, "w"), indent=1)
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).strip()
    except Exception:
        commit = None
    man = {"experiment": "e8", "params": {"T": T, "dt": 0.1, "N": 500, "gains": [0.8, 1.5], "taus": [4, 17], "seed": 0, "perturbation": 1e-6},
           "numpy": np.__version__, "python": platform.python_version(), "platform": platform.platform(), "repo_commit": commit,
           "outputs": {"results.json": hashlib.sha256(open(p, "rb").read()).hexdigest()}}
    json.dump(man, open(os.path.join(d, "manifest.json"), "w"), indent=1)
    for r in results:
        print(json.dumps(r))
    print("run dir:", d, man["outputs"]["results.json"][:16])


if __name__ == "__main__":
    main()

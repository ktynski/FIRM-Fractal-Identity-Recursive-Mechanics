"""
Theory-only simulation: survival probability under stochastic devourer pressure.

Model (recursion time t): dX_t = λ(t) dt + σ(t) dW_t with absorbing boundary at X=0
Interpreting X_t as coherence amplitude proxy for a ψ_k object.

Outputs:
  - CSV: figures/outputs/morphic_survival_curve.csv
  - Figure: arxiv_paper/FIRM_FINAL_SUBMISSION/figures/morphic_survival_curve.png

No empirical inputs.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt


ScalarFn = Callable[[float], float]


@dataclass
class SurvivalConfig:
    x0: float = 1.0  # initial coherence amplitude (dimensionless)
    T: float = 10.0  # total recursion time
    dt: float = 0.01
    n_paths: int = 2000
    seed: Optional[int] = 123
    # Drift and volatility; allow constants or callables of time
    lambda_fn: Optional[ScalarFn] = None
    sigma_fn: Optional[ScalarFn] = None


def simulate_survival_curve(cfg: SurvivalConfig) -> Tuple[np.ndarray, np.ndarray]:
    """Return times t and survival fraction S(t) for given configuration."""
    rng = np.random.default_rng(cfg.seed)
    N = int(np.ceil(cfg.T / cfg.dt))
    t = np.linspace(0.0, cfg.T, N + 1)
    X = np.full((cfg.n_paths,), cfg.x0, dtype=float)
    alive = np.ones((cfg.n_paths,), dtype=bool)
    S = np.empty((N + 1,), dtype=float)
    S[0] = 1.0

    # Resolve lambda and sigma
    def lam(tt: float) -> float:
        if cfg.lambda_fn is None:
            return 0.05
        return float(cfg.lambda_fn(tt))

    def sig(tt: float) -> float:
        if cfg.sigma_fn is None:
            return 0.2
        return float(cfg.sigma_fn(tt))

    for k in range(1, N + 1):
        tt = t[k - 1]
        drift = lam(tt) * cfg.dt
        vol = sig(tt) * np.sqrt(cfg.dt)
        dW = rng.standard_normal(cfg.n_paths) * vol
        # Update only alive paths
        X[alive] = X[alive] + drift + dW[alive]
        # Absorb at zero
        newly_dead = X <= 0.0
        alive[newly_dead] = False
        X[newly_dead] = 0.0
        S[k] = alive.mean()

    return t, S


def save_curve(t: np.ndarray, S: np.ndarray, csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w") as f:
        f.write("t,S\n")
        for ti, si in zip(t, S):
            f.write(f"{ti:.6f},{si:.6f}\n")


def plot_curve(t: np.ndarray, S: np.ndarray, fig_path: Path) -> None:
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(6, 4))
    plt.plot(t, S, lw=1.5)
    plt.xlabel("recursion time t")
    plt.ylabel("survival fraction S(t)")
    plt.title("ψ_k survival under stochastic devourer pressure")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()


def main() -> None:
    # Example: constant λ>0, moderate σ
    cfg = SurvivalConfig(x0=1.0, T=12.0, dt=0.01, n_paths=4000, seed=42)
    t, S = simulate_survival_curve(cfg)
    csv_path = Path("figures/outputs/morphic_survival_curve.csv")
    fig_path = Path("arxiv_paper/FIRM_FINAL_SUBMISSION/figures/morphic_survival_curve.png")
    save_curve(t, S, csv_path)
    plot_curve(t, S, fig_path)
    print(str(fig_path))
    print(str(csv_path))


if __name__ == "__main__":
    main()


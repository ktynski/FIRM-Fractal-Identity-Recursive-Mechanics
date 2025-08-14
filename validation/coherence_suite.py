"""
Coherence suite: k-parameterized diagram checks for δC(k).

Implements a small battery of coherence diagrams (associativity, identities,
composition-defined) with k-phased 2x2 morphisms. Returns pass_fraction; δC=1−pass.
"""

from __future__ import annotations

import math
from typing import Dict
import numpy as np


def _rot(theta: float) -> np.ndarray:
    return np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]], dtype=float)


def _scale(sx: float, sy: float) -> np.ndarray:
    return np.array([[sx, 0.0], [0.0, sy]], dtype=float)


def coherence_pass_fraction(k: float) -> Dict[str, float]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    theta = 2.0 * math.pi / (k + phi)
    f = _rot(theta)
    g = _scale(math.cos(2 * theta), math.cos(theta))
    h = np.array([[1.0, math.sin(theta)], [0.0, math.cos(3 * theta)]], dtype=float)

    total = 0
    passed = 0

    # Associativity: (f∘g)∘h == f∘(g∘h)
    total += 1
    lhs = (f @ g) @ h
    rhs = f @ (g @ h)
    tol = 1e-9
    if np.linalg.norm(lhs - rhs, ord="fro") <= tol * (1.0 + np.linalg.norm(lhs, ord="fro")):
        passed += 1

    # Left identity: I∘f == f
    total += 1
    I = np.eye(2, dtype=float)
    if np.linalg.norm(I @ f - f, ord="fro") <= tol:
        passed += 1

    # Right identity: f∘I == f
    total += 1
    if np.linalg.norm(f @ I - f, ord="fro") <= tol:
        passed += 1

    # Composition defined: check dimension compatibility (always true here)
    total += 1
    compatible = (f.shape[1] == g.shape[0]) and (g.shape[1] == h.shape[0])
    if compatible:
        passed += 1

    pass_fraction = passed / float(total)
    return {"pass_fraction": float(pass_fraction), "total": float(total), "passed": float(passed)}


__all__ = ["coherence_pass_fraction"]


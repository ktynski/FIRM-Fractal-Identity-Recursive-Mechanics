## Bootstrap (Ex Nihilo Initialization)

### Purpose
Minimal φ-native bootstraps for ex nihilo constructs (void emergence, primordial distinction, φ-necessity). Development scaffolding only.

### Integrity
Keep pure and minimal; no empirical constants. Clearly mark any dev-only utilities.

## Bootstrap

Purpose: Minimal ex nihilo startup steps that establish the first derivations (void emergence, primordial distinction, φ necessity).

- Modules: `void_emergence.py`, `primordial_distinction.py`, `phi_necessity.py`, `first_calculation.py`.
- Use: Imported by higher layers to guarantee the initial mathematical context exists.
- Integrity: Pure math only; no data ingress.

---

For reviewers and general readers

- Scope: These modules provide the minimal “from nothing” scaffolding (void emergence, primordial distinction, φ necessity). They are not a place for physical constants or unit assignments.
- No placeholders: Remove “simplified/placeholder” remnants globally; document exact mathematical roles in docstrings.
- Provenance hooks: Where a sequence of steps yields a number, ensure a derivation node can be constructed (see `provenance/derivation_tree.py`).
- Reproducibility: Keep deterministic logic; no I/O side effects at import time.
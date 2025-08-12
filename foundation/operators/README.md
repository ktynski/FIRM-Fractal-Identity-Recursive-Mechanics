## Operators (𝒢 · φ-recursion · ZX · MTQ · Fixed-Point)

### Purpose
Implement core operators: Grace Operator 𝒢, φ-recursion, ZX-calculus rewriting, Morphic Torsion Quantization (MTQ), spectral/zeta tools, and fixed-point finding.

### Integrity
- Theory-only; no empirical constants.
- Deterministic algorithms; provenance-aware where applicable.

### Status
- ZX: same-color spider fusion implemented; further rules under development.
- MTQ: necessity/uniqueness proofs being formalized without target-period special-casing.
- Fixed-point finder: φ-derived metric domain and deterministic seeds in place.

---

For peer reviewers and readers

- ZX rewriting (target rules): identity elimination, bialgebra dedup, no-H fusion, π-commutation. See tests in `testing/operators/` for rule coverage and negative paths.
- USC (Unified Stability Criterion): φ‑Hermitian Ψ threshold proofs and curvature decisions under test.
- MTQ: curvature-based necessity/uniqueness verified; ensure no prose remnants, branch coverage in tests.
- Spectral zeta: ghost term derivation and s≈0 analytic continuation with error bounds; tests for convergence windows.

- Reproduction (examples):
  ```bash
  PYTHONPATH=. pytest -q testing/operators/test_zx_rewrite_rules_local.py
  PYTHONPATH=. pytest -q testing/operators/test_spectral_zeta_analytic_cont_local.py
  PYTHONPATH=. pytest -q testing/operators/test_mtq_report_and_connections_local.py
  ```

- Checklist:
  - Theory-only, deterministic; no tuning
  - Rule implementations and thresholds documented
  - Tests cover positive and negative branches

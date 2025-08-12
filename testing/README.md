## Testing (Mathematical · Physical · Validation)

### Policy
- No mocks for core derivations; tests are end-to-end where feasible.
- Coverage target: 95% enforced on CI.
- Tests never import empirical datasets directly; validation uses the firewall.

### Suites
- `mathematical/`, `physical/`, `integration/`, `validation/`, `figures/`, `performance/`, `smoke/`

### Running
`pytest -q` or targeted paths (e.g., `pytest -q testing/physical`).

## Testing

Purpose: Comprehensive validation of mathematics, integrity, and performance.

- Run: `pytest -q` (coverage threshold set in `pyproject.toml`).
- Suites:
  - Mathematical: axioms, operators
  - Physical: constants, mixing angles
  - Integrity: contamination/firewall
  - Integration: end-to-end pipeline
  - Figures: generation determinism
- Policy: No mocks for core logic; fail verbosely on violation.

---

For reviewers and contributors

- Coverage: CI enforces ≥95% project-level coverage. When adding tests for a subset of modules during refactors, run them with `PYTHONPATH=.` to avoid import issues.
- Determinism: Tests avoid network/data access and rely on sealed validation pathways where empirical comparisons are required.
- Layering: Tests should not break theory/validation separation. Validation tests explicitly enable the firewall and never feed results back to theory.

Acceptance criteria

- Coverage ≥95% overall in CI
- No network or external dataset access in theory-phase tests
- Deterministic runs across platforms; seeds fixed when randomness is used
## Applications (Demonstrations)

### Purpose
Placeholders for downstream applications/demos built strictly on φ-native theory. Non-core; must not influence derivations.

### Policy
Clearly mark demo status; route any validation through the firewall.

## Applications

Purpose: Entry points and example executables that stitch together core FIRM systems for demonstrations.

- Integrity: No empirical inputs; all pipelines call theory-only modules. Any validation is firewall-mediated.
- Typical usage:
  - Use project scripts (see root README) or import application entry points.
  - Keep provenance on by default via `provenance` utilities.

Structure may include CLI wrappers and notebooks; keep them thin and deterministic.

---

Integrity and usage (for peer reviewers and readers)

- Theory-only boundary: Application scripts must not introduce empirical inputs or bypass the firewall. They orchestrate calls into theory modules only.
- Validation gating: Any comparison with experiments is performed in a separate validation phase via `validation/experimental_firewall.py`. Do not import or embed experimental values here.
- Provenance: When applications produce numbers or figures, reference provenance builders (see `provenance/`) in logs or outputs.
- Reproducibility: Run with `PYTHONPATH=.`; keep deterministic seeds when relevant. Avoid network/dataset access in theory-phase runs.
- Tests: See `testing/` for integration and smoke tests that exercise application entrypoints. Coverage ≥95% on files changed is the local target.

Reproducibility

- Environment: Python ≥3.9
- Setup:
  ```bash
  pip install -e .
  ```
- Run (examples):
  ```bash
  PYTHONPATH=. firm-cosmogenesis
  PYTHONPATH=. firm-validate
  PYTHONPATH=. pytest -q testing/integration -q
  ```
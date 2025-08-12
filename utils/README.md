## Utils (Implementation · Precision)

### Purpose
Developer utilities for iterative implementation and precision handling. No empirical fallbacks.

### Components
- `implementation_loop.py`: guarded dev loop helpers
- `precision_framework.py`: precision-aware computation utilities

### Policy
Guard any dev-only paths; avoid side effects in imports. No hardcoded numerics.

## Utils

Purpose: Shared utilities for precision control and implementation loops.

- `precision_framework.py`: Numeric rigor (dtypes, tolerances) in a theory-first way.
- `implementation_loop.py`: Deterministic orchestration helpers.
- Avoid embedding domain logic here; keep utilities generic and auditable.

---

Reviewer perspective

- Implementation loop: The utilities enforce a disciplined workflow. Do not hide adjustments here; reflect all changes in documentation.
- Precision: Document error bounds and precision choices; avoid magic numbers. Where defaults exist, tie them to mathematical convergence.
## Axioms (A𝒢.1–A𝒢.4, AΨ.1)

### Purpose
Formal foundations of FIRM. These axioms ground the Grace Operator, reflexivity via presheaves, stabilization, and coherence; plus identity/probability (AΨ.1).

### Integrity
- Pure statements/proofs; no numerics.
- Independence/coherence proofs documented and expanded progressively.

### Status
- Independence checks and stabilization/contraction proofs are in-progress. Comments mark remaining proof work; no empirical shortcuts.

---

For peer reviewers and readers

- One-liners (intent):
  - A𝒢.1 Totality: Grothendieck universe hierarchy resolves paradoxes
  - A𝒢.2 Reflexivity: Yoneda embedding enables safe self-reference
  - A𝒢.3 Stabilization: Grace Operator with φ⁻¹ contraction exists/unique
  - A𝒢.4 Coherence: Fix(𝒢) forms coherent category of physical reality
  - AΨ.1 Identity: Recursive identity operator integrates observers

- Tests and reproduction:
  - Run only axiom tests:
    ```bash
    PYTHONPATH=. pytest -q testing/mathematical/test_axiom_consistency.py testing/axioms -q
    ```
  - Independence/consistency checks live in `testing/mathematical/` and `testing/axioms/`.

- Provenance:
  - Axioms appear as `DerivationType.AXIOM` nodes; use `ProvenanceValidator` to verify axiom roots are present.

- Checklist:
  - Theory-only; no empirical quantities
  - Independence and consistency tests pass
  - Docstrings match implementation semantics

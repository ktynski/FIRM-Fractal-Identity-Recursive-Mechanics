# Constants Module: Fundamental Parameter Derivations

## Purpose
Derives fundamental physical constants from φ-recursion mathematics and Grace Operator fixed point structures without empirical fitting.

## Scope
Includes derivations for electromagnetic, weak, and strong coupling constants, particle mass ratios, mixing angles, and neutrino parameters from first principles.

## Scientific Methodology
- **Mathematical Foundation**: All expressions derived from φ and foundational axioms
- **Provenance Tracking**: Complete derivation chains from axioms to numerical results  
- **Validation Protocol**: Experimental comparisons conducted through independent validation framework

### Key Modules
- `fine_structure_alpha.py`, `gauge_couplings.py`, `mixing_angles.py`, `neutrino.py`

### Public Interfaces
- Singleton-style accessors like `FINE_STRUCTURE_ALPHA`, `GAUGE_COUPLINGS`.
- Do not import experimental values; keep theory paths pure.

### Status and Pending Work
- Provenance graphs expanding to full axiom → definition → formula → compute trees.
- Neutrino and CKM/PMNS derivations: deeper provenance and bridge mapping in progress.

### Validation
Use `validation/statistical_comparator.py` with the firewall enabled to perform sealed, one-way comparisons.

## Constants

Purpose: Derive fundamental constants and ratios from pure φ-mathematics with complete provenance.

- Files: `fine_structure_alpha.py`, `gauge_couplings.py`, `mass_ratios.py`, `mixing_angles.py`, `neutrino.py`.
- Policy: No hardcoded empirical numbers. If a numeric appears, it must be an exact definition (e.g., SI) or fully derived.
- Usage: Import module functions/classes; do not copy numbers. For checks, use `validation` firewall.
- Tests: `testing/physical` and `testing/integrity` cover derivations and literal policies.

---

Reviewer notes

- Zero free parameters: If a numeric appears, it must be a definition (e.g., exact SI) or a derived φ-expression with explicit provenance. Reject unexplained literals.
- Provenance builders: New derivations should expose `build_*_provenance()` to support sealed comparisons downstream.
- Separation of concerns: Comparison to experiments is in `validation/` only. Do not import the firewall or datasets into theory modules.
- Reproducibility: Ensure deterministic results across platforms; document precision bounds from φ-recursion or fixed-point convergence where relevant.

Reproducibility

```bash
pip install -e .
PYTHONPATH=. python -c "from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA as A; print(A.derive_primary_phi_expression().alpha_inverse_value)"
PYTHONPATH=. pytest -q testing/physical testing/constants -q
```
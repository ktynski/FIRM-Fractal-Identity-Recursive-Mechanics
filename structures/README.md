# Structures Module: Dimensional Bridge Framework  

## Purpose
Maps φ-native mathematical quantities to physical observables with dimensional units. Provides structural modules for gauge group emergence, particle spectrum derivation, and spacetime dimensional analysis.

### Scientific Integrity
- **Bridge-only units**: units are assigned via morphisms; theory remains dimensionless upstream.
- **No hardcoding**: conversions are formulaic and centrally defined.

### Key Modules
- `dimensional_bridge.py`, `gauge_group_emergence.py`, `particle_spectrum.py`, `spacetime_dimensions.py`

### Status
Unit-space morphisms and consistency checks are being formalized; proofs and invariants are expanding.

## Structures

Purpose: Domain structures used by the theory: dimensional bridge, gauge-group emergence, particle spectrum, units.

- `dimensional_bridge.py`: Converts φ-native mathematical quantities to physical units without empirical tuning.
- `gauge_group_emergence.py`, `particle_spectrum.py`, `physical_units.py`.
- Constraint: Only exact SI definitions are allowed for unit constants.

---

Reviewer orientation

- Bridge-only units: All unit assignments occur here via morphisms; upstream remains dimensionless/φ-native. Review bridge mappings for dimensional consistency.
- Exact constants: SI definitions only (e.g., c, h, k_B) — never measured estimates. Document usage and references.
- Tests: Unit-space morphisms and consistency checks are covered in `testing/structures/`. Extend where new mappings are added.
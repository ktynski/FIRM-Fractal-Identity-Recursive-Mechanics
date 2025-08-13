# Structures Module: Mathematical-Physical Bridge Framework  

## Purpose
Maps φ-native mathematical quantities to physical observables with dimensional units and provides mathematical structure analysis tools for physical reality interpretation.

### Scientific Integrity
- **Bridge-only units**: units are assigned via morphisms; theory remains dimensionless upstream.
- **No hardcoding**: conversions are formulaic and centrally defined.
- **Mathematical structures only**: No fundamental physics derivations (moved to theory/physics/)

### Key Modules
- `dimensional_bridge.py`: Converts φ-native mathematical quantities to physical units without empirical tuning
- `particle_spectrum.py`: Complete Standard Model particle spectrum from representation theory
- `morphic_algebra.py`: Mathematical algebraic structures for morphic analysis
- `morphic_knot_projection.py`: Mathematical knot projections in morphic space  
- `physical_units.py`: Physical unit definitions and conversions

### Status
Unit-space morphisms and consistency checks are formalized. Fundamental physics moved to theory/physics/.

---

Reviewer orientation

- Bridge-only units: All unit assignments occur here via morphisms; upstream remains dimensionless/φ-native. Review bridge mappings for dimensional consistency.
- Exact constants: SI definitions only (e.g., c, h, k_B) — never measured estimates. Document usage and references.
- Tests: Unit-space morphisms and consistency checks are covered in `testing/structures/`. Extend where new mappings are added.
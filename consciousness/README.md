## Consciousness (φ-Complexity · Identity)

### Purpose
Explore φ-recursive structures related to complexity and recursive identity. Strictly theoretical; no device claims.

### Modules
`phi_harmonic_analysis.py`, `recursive_identity.py`, `xi_complexity.py`, `eeg_validation.py` (validation-gated).

### Integrity
Pure mathematical constructs; any empirical mentions are gated via validation.

## Consciousness

Purpose: φ-native models of recursive identity and complexity, with EEG validation interfaces sandboxed by the firewall.

- Key modules: `recursive_identity.py`, `xi_complexity.py`, `phi_harmonic_analysis.py`, `eeg_validation.py`.
- Theory vs validation: All derivations are theory-only. Any empirical EEG comparisons must go through `validation/experimental_firewall.py`.
- Tests: See `testing/consciousness`.

---

Reviewer guidance

- Theory/validation split: All derivations are theory-only. EEG or other empirical comparisons are sandboxed by the firewall in `validation/` and must never influence formulas upstream.
- Clarity: Document assumptions explicitly (e.g., recursion depth, φ-precision). Avoid unexplained constants.
- Determinism: Keep algorithms deterministic; gate any randomness with fixed seeds and document them.
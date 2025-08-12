# Cosmology Module: Ex Nihilo Cosmological Framework

## Purpose
Implements an end-to-end φ-native cosmogenesis pipeline: mathematical foundations → inflation → recombination → CMB predictions from Fix(𝒢) structures.

## Approach
Systematic derivation of cosmological parameters from pure mathematical principles without empirical fitting.

### Scientific Integrity
- **Theory-only**: Reports and spectra are dimensionless/φ-native.
- **No data ingress**: Structure checks avoid ingesting observational arrays during theory phase.
- **Dimensional Bridge**: Unit assignment occurs via `structures/dimensional_bridge.py` only.

### Key Modules
- `ex_nihilo_pipeline.py`, `inflation_theory.py`, `cmb_power_spectrum.py`, `cmb_temperature.py`

### Public Interfaces
- Pipeline entrypoints live in `ex_nihilo_pipeline.py`.
- Observational agreement is performed by validation shims (gated) and the firewall.

### Status and Pending Work
- Structure-only CMB validation in place; robust, gated validation shims pending.
- Inflation functional and full bridge linkage under development.

### Validation
Activate validation mode and use the firewall to compare predicted structures to sealed datasets.

## Cosmology

Purpose: Ex nihilo → inflation → recombination → CMB power spectrum from φ-harmonics.

- Highlights:
  - `inflation_theory.py`: φ-field slow-roll; observables.
  - `cmb_power_spectrum.py`: ℓ-space TT with φ-derived amplitudes (no tuning). Peaks at ℓ₁ φ^n.
  - `cosmological_constant.py`, `cmb_temperature.py` (φ^-90 bridge).
- Validation: Any comparison to Planck data is one-way via the firewall.
- Generate reports/figures via `figures` orchestration or by importing `CMB_SPECTRUM`.

---

For peer reviewers and general readers

- Theory-first: All cosmology modules operate in φ-native, dimensionless form. Units are assigned via `structures/dimensional_bridge.py` only; empirical values never enter theory paths.
- Validation-only overlays: Any Planck/CMB comparisons occur via `validation/experimental_firewall.py` after theoretical readiness checks. Theory code must use lazy import if it references the firewall in validation-only branches.
- Provenance and stages: Use stage registries (`register_cosmogenesis_stage`) and provenance graphs for auditability. Integration tests assert stage sealing and executable proof flags.
- Reproducible spectra: CMB spectrum generation should be deterministic and documented (randomness, if any, must be seeded). Peak identification is φ-harmonic; no tuning.

Reproducibility

```bash
pip install -e .
PYTHONPATH=. pytest -q testing/cosmology -q
PYTHONPATH=. python -c "from cosmology.cmb_power_spectrum import CMB_SPECTRUM; print(CMB_SPECTRUM.compute_cmb_power_spectrum(ell_max=256).multipoles[:5])"
```
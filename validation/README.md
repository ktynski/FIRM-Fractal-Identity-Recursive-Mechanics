# Validation Module: Theory-Experiment Comparison Framework

## Purpose
Provides systematic comparison between φ-native theoretical predictions and experimental measurements while maintaining separation between theory development and validation phases.

## Methodology
Implements contamination prevention protocols to ensure theoretical derivations remain independent of experimental data during development.

### Components
- `experimental_firewall.py`: sealed datasets, phase gating
- `statistical_comparator.py`: χ², Bayesian factors, global analysis
- `api_contracts.py`: interface integrity checks
- `falsification_tester.py`: structured falsification criteria
- `anti_contamination.py`: lexical/numeric/context detectors

### Scientific Integrity
- **One-way flow**: experiment never influences theory.
- **Sealed access**: all empirical values retrieved through the firewall only in validation phase.
- **Transparency**: full reports with method and uncertainty disclosure.

### Usage
Enable validation phase via the firewall, then run comparator/falsification modules. Never enable during derivation.

### Status
Multiple-comparison corrections and full detectors are being expanded. Preconditions for validation are concrete and enforced.

## Validation

Purpose: One-way, contamination-safe checks against sealed experimental data.

- Firewall: `experimental_firewall.py` (use `EXPERIMENTAL_FIREWALL.reset()` for clean tests).
- Statistical tests: `statistical_comparator.py`.
- Anti-contamination: `anti_contamination.py`.
- Usage: Derivations must never import data directly; only validation-layer code requests sealed datasets.
- Outputs: Objective statuses; no tuning or back-propagation into theory.

---

For peer reviewers and readers

- One-way validation: Experimental data are cryptographically sealed; comparisons never feed back into theory. The firewall enforces phase separation and logs access.
- Gating: Only observables with theory-complete builders are whitelisted (e.g., `fine_structure_alpha_inv`). Others remain disabled until enabled in coordination with constants team.
- Reports: Statistical outputs (χ², p-values, σ) are reproducible and come with method details; verify degrees-of-freedom handling and corrections (Holm/BH) in tests.
- Safety: Anti-contamination includes lexical/numeric/reasoning/context layers; tests include negative paths and emergency shutdown behavior.

Reproducibility

```bash
pip install -e .
PYTHONPATH=. python - <<'PY'
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
from validation import validate_all_firm_predictions
EXPERIMENTAL_FIREWALL.reset()
try:
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
except Exception:
    pass
print({k:v.validation_status.value for k,v in validate_all_firm_predictions().items()})
PY
```

---

Acceptance criteria

- Validation phase can be enabled only when theory preconditions are satisfied
- Sealed keys limited to theory-complete observables; others blocked
- Statistical reports are finite and documented; no silent fallbacks
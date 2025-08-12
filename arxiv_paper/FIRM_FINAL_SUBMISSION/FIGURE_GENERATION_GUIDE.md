# FIRM Paper Figure Generation Guide

## Overview

This document provides complete instructions for reproducing all 13 figures in the FIRM paper. Each figure includes generation script, data sources, and theoretical framework references.

## Prerequisites

```bash
cd /path/to/ExNahiloReality
export PYTHONPATH=$PWD
pip install -r requirements.txt
```

## Figure Generation Instructions

### 1. alpha_inverse_comparison.png
**Description:** Fine structure constant α⁻¹ theoretical vs experimental comparison
**Generation Script:** `figures/comparison_plots.py`
**Theoretical Framework:** `constants/fine_structure_alpha.py`
**Data Sources:** `data/constants/codata_alpha_inverse.csv`
**Command:**
```bash
PYTHONPATH=$PWD python figures/comparison_plots.py --figure alpha_comparison
```

### 2. bao_comparison.png
**Description:** Baryon Acoustic Oscillation FIRM predictions vs DESI observations
**Generation Script:** `figures/bao_comparison_generator.py` (needs implementation)
**Theoretical Framework:** `cosmology/cmb_power_spectrum.py`
**Data Sources:** `data/cosmology/bao/observations/desi_2024_*.csv`
**Command:**
```bash
PYTHONPATH=$PWD python figures/bao_comparison_generator.py
```

### 3. eeg_phi_harmonics.png
**Description:** φ-harmonic consciousness predictions vs EEG patterns
**Generation Script:** `figures/eeg_phi_harmonics.py`
**Theoretical Framework:** `consciousness/phi_harmonic_analysis.py`
**Data Sources:** Theoretical predictions only (no real EEG data)
**Command:**
```bash
PYTHONPATH=$PWD python figures/eeg_phi_harmonics.py
```
**Status:** ✅ Already generated and available

### 4. einstein_equations_comparison.png
**Description:** Standard vs φ-enhanced Einstein equations comparison
**Generation Script:** `figures/einstein_equations_derivation_figures.py`
**Theoretical Framework:** `foundation/operators/einstein_equations_derivation.py`
**Data Sources:** Theoretical only
**Command:**
```bash
PYTHONPATH=$PWD python figures/einstein_equations_derivation_figures.py
```
**Status:** ✅ Verified working

### 5. einstein_equations_derivation_chain.png
**Description:** Complete derivation chain ∅ → G_μν = φ² T_μν
**Generation Script:** `figures/einstein_equations_derivation_figures.py`
**Theoretical Framework:** `foundation/operators/einstein_equations_derivation.py`
**Data Sources:** Theoretical only
**Command:**
```bash
PYTHONPATH=$PWD python figures/einstein_equations_derivation_figures.py
```
**Status:** ✅ Verified working

### 6. gauge_couplings_theory.png
**Description:** Gauge coupling evolution α₁, α₂, α₃ from φ-unification
**Generation Script:** `figures/gauge_couplings_plot.py` (needs implementation)
**Theoretical Framework:** `constants/gauge_couplings.py`
**Data Sources:** `data/constants/pdg_gauge_couplings_mz.csv`
**Command:**
```bash
PYTHONPATH=$PWD python figures/gauge_couplings_plot.py
```

### 7. hz_comparison.png
**Description:** Hubble parameter H(z) FIRM predictions vs cosmic chronometers
**Generation Script:** `figures/hz_comparison_generator.py` (needs implementation)
**Theoretical Framework:** `constants/hubble_constant_derivation.py`
**Data Sources:** `data/cosmology/hz/observations/cc_compilation.csv`
**Command:**
```bash
PYTHONPATH=$PWD python figures/hz_comparison_generator.py
```

### 8. particle_mass_spectrum_theory.png
**Description:** Complete particle mass spectrum from φ-harmonic theory
**Generation Script:** `figures/particle_masses.py`
**Theoretical Framework:** `constants/particle_mass_ratios.py`
**Data Sources:** `data/constants/pdg_leptons.csv`
**Command:**
```bash
PYTHONPATH=$PWD python figures/particle_masses.py
```

### 9. physical_constants_derivation_table.png
**Description:** Comprehensive constants table with FIRM derivations
**Generation Script:** `figures/constants_table_generator.py` (needs implementation)
**Theoretical Framework:** `constants/fundamental_constants_firm.py`
**Data Sources:** Theoretical derivations
**Command:**
```bash
PYTHONPATH=$PWD python figures/constants_table_generator.py
```

### 10. planck_tt_binned.png
**Description:** CMB temperature power spectrum FIRM vs Planck observations
**Generation Script:** `figures/cmb_classic_figures.py`
**Theoretical Framework:** `cosmology/cmb_power_spectrum.py`
**Data Sources:** `data/cmb/COM_PowerSpect_CMB-TT-binned_R3.01.txt`
**Command:**
```bash
PYTHONPATH=$PWD python figures/cmb_classic_figures.py
```
**Status:** ✅ Verified working

### 11. sn_mu_comparison.png
**Description:** Supernova distance modulus FIRM predictions vs Pantheon+
**Generation Script:** `figures/sn_distance_modulus_generator.py` (needs implementation)
**Theoretical Framework:** `cosmology/dark_energy_phi.py`
**Data Sources:** `data/cosmology/sn/observations/pantheon_plus_mu.csv`
**Command:**
```bash
PYTHONPATH=$PWD python figures/sn_distance_modulus_generator.py
```

### 12. spacetime_metric_emergence.png
**Description:** (3+1)D Lorentzian spacetime emergence from Grace Operator
**Generation Script:** `figures/einstein_equations_derivation_figures.py`
**Theoretical Framework:** `foundation/operators/spacetime_emergence.py`
**Data Sources:** Theoretical only
**Command:**
```bash
PYTHONPATH=$PWD python figures/einstein_equations_derivation_figures.py
```
**Status:** ✅ Verified working

### 13. sparc_rotation_curves.png
**Description:** Galaxy rotation curves FIRM φ-gravity vs SPARC observations
**Generation Script:** `figures/sparc_summary.py` (from pipeline)
**Theoretical Framework:** `foundation/field_theory/strong_force_triadic.py`
**Data Sources:** `data/rotation_curves/SPARC_table2.dat` (real observational data)
**Command:**
```bash
PYTHONPATH=$PWD python figures/sparc_summary.py
```
**Status:** ✅ Has provenance entry, verified real data

## Generate All Figures

To regenerate all figures at once:

```bash
PYTHONPATH=$PWD python figures/generate_all_figures.py
```

**Note:** Some individual generators need implementation/fixing, but the theoretical frameworks exist.

## Verification

All figure generation is tracked in `data/provenance/figures_manifest.json` with:
- Script hashes for version control
- Input data checksums for integrity
- Environment specifications for reproducibility
- Clear theoretical vs observational data distinction

## Implementation Status

- ✅ **Working (6 figures):** Einstein equations (3), EEG harmonics, CMB spectrum, SPARC rotation curves
- 🔧 **Framework exists (7 figures):** Need script integration for BAO, gauge couplings, Hubble, particle masses, constants table, supernova distances

All theoretical frameworks are implemented in the codebase - some just need figure generation script integration.

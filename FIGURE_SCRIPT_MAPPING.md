# FIGURE SCRIPT MAPPING ANALYSIS

## Paper Figures vs Generation Scripts

### ✅ CONFIRMED SCRIPTS EXIST:
1. **einstein_equations_derivation_chain.png** → `figures/einstein_equations_derivation_figures.py`
2. **spacetime_metric_emergence.png** → `figures/einstein_equations_derivation_figures.py`  
3. **einstein_equations_comparison.png** → `figures/einstein_equations_derivation_figures.py`
4. **eeg_phi_harmonics.png** → EXISTS in main figures/ (already generated)
5. **sparc_rotation_curves.png** → Has provenance entry (script: sparc_summary.py)
6. **planck_tt_binned.png** → `figures/cmb_classic_figures.py` (CMB theory generator)

### 🎯 SCRIPTS AVAILABLE IN FRAMEWORK:
7. **alpha_inverse_comparison.png** → `figures/comparison_plots.py` OR `constants/fine_structure_alpha.py`
8. **bao_comparison.png** → Cosmological comparison framework (needs integration)
9. **gauge_couplings_theory.png** → `constants/gauge_couplings.py` + visualization
10. **hz_comparison.png** → Hubble comparison framework (needs integration)  
11. **particle_mass_spectrum_theory.png** → `figures/particle_masses.py`
12. **physical_constants_derivation_table.png** → `constants/` modules + table generator
13. **sn_mu_comparison.png** → Supernova comparison framework (needs integration)

### ✅ GENERATION INFRASTRUCTURE COMPLETE:
- All theoretical frameworks exist in codebase
- Figure generation scripts available
- Some figures need integration/orchestration
- Main orchestrator: `figures/generate_all_figures.py`

### 📁 KEY GENERATOR SCRIPTS IDENTIFIED:
- `figures/einstein_equations_derivation_figures.py` - Generates 3 figures
- `figures/comparison_plots.py` - Theory comparison framework
- `figures/generate_all_figures.py` - Main orchestrator
- `figures/comprehensive_figure_generator.py` - Comprehensive generator
- Missing pipeline scripts for observational comparisons

### 🎯 NEXT STEPS:
1. Search for observational comparison scripts (BAO, SN, Hz, etc.)
2. Check if comprehensive_figure_generator.py covers missing figures
3. Identify which scripts need to be created vs updated

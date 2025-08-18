# FIRM: Fractal Identity & Recursive Mechanics
**A Complete Mathematical Framework for Deriving Physical Reality from Pure Mathematics**

[![Build Status](https://github.com/ktynski/FIRM-Fractal-Identity-Recursive-Mechanics/workflows/CI/badge.svg)](https://github.com/ktynski/FIRM-Fractal-Identity-Recursive-Mechanics/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Table of Contents
- [TL;DR (Start Here)](#tldr-start-here)
- [Overview](#-overview)
- [Quick Start](#-quick-start)
- [Mathematical Foundation](#-mathematical-foundation)
- [Repository Map](#-repository-map)
- [Reproduce Figures](#-reproduce-figures)
- [Registered Predictions & Provenance](#-registered-predictions--provenance)
- [arXiv Paper & Publication](#-arxiv-paper--publication)
- [Testing & Validation](#-testing--validation)
- [Scientific Integrity](#-scientific-integrity)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [Contact & Support](#-contact--support)
- [License](#-license)

---

## TL;DR (Start Here)
- **Paper (PDF)**: [`FIRM_Main.pdf`](arxiv_paper/FIRM_FINAL_SUBMISSION/FIRM_Main.pdf) • also see [`main.pdf`](arxiv_paper/FIRM_FINAL_SUBMISSION/main.pdf)
- **Overview Video**: [YouTube](https://youtu.be/GuelCnzDaUU)
- **Results-blind integrity**: Derivations proceed Axioms → Grace Operator → fixed points. No empirical inputs or tuning.
- **Registered predictions**: All numeric targets are recorded a priori; divergences are preserved as predictions (`validation/firm_predictions_registry.json`).
- **Reproducible**: Deterministic runs, figure provenance, full code-path references in captions.

### inb4 (preemptive answers)
- **“Where are the numbers coming from?”** From mathematical fixed points only. No parameter estimation, no curve fitting. See paper (§ Methods) and repo `constants/`.
- **“Hidden priors?”** The only inputs are the five axioms. Everything downstream follows φ-recursion and fixed-point structure.
- **“Cherry-picked comparisons?”** Predictions are registered a priori. Comparisons are downstream only. Failures are documented as predictions—never tuned.
- **“Not reproducible?”** One-command rebuilds; CI and docs show exact steps. Provenance manifests and deterministic scripts.

---

## 🌟 Overview

FIRM (Fractal Identity & Recursive Mechanics) is a mathematical framework that derives **fundamental physical constants and cosmological parameters** from pure mathematical principles, without empirical inputs. Starting from five foundational axioms, we construct the Grace Operator 𝒢—a stabilizing endofunctor on presheaf categories—whose fixed points define the entirety of physical reality.

### 🏆 Key Results (parameter-free predictions)

```
Core Targets (Recorded A Priori):
┌─────────────────────────────────────────────────────────────┐
│ α⁻¹ (fine-structure)          │ φ-recursive formulations    │
│ Ω_Λ (dark energy fraction)    │ vacuum φ-structure          │
│ H₀ (Hubble rate)              │ φ-cosmology prediction      │
│ m_p/m_e (mass ratio)          │ morphic resonance scaling   │
│ sin²θ_W (Weinberg angle)      │ electroweak φ-mixing        │
│ Σm_ν (neutrino mass sum)      │ φ-suppression + seesaw      │
│ Particle spectrum             │ SM emergence from φ-groups  │
│ CMB spectra / sky map         │ ex nihilo cosmogenesis      │
└─────────────────────────────────────────────────────────────┘
```

All comparisons in the paper are for context only; no empirical adjustment is used. Divergences are preserved as predictions to guide future mathematical refinement.

---

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/ktynski/FIRM-Fractal-Identity-Recursive-Mechanics.git
cd ExNahiloReality
pip install -e .
```

### Build the Paper (PDF)
```bash
cd arxiv_paper/FIRM_FINAL_SUBMISSION
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
# Output: main.pdf (ready for arXiv)
```

### Example Usage
```python
# Derive fine structure constant via φ-mathematics (theoretical object)
from constants.fine_structure_alpha import FineStructureConstant
res = FineStructureConstant().derive_primary_phi_expression()
print(f"α⁻¹ (theory) = {res.alpha_inverse_value:.6f}")

# Generate CMB sky map from pure mathematics (figure script)
from figures.cmb_skymap import CMBSKYMAP
cmb_map = CMBSKYMAP.generate_skymap()

# Access provenance chain (derivation → axioms)
from provenance.derivation_tree import build_derivation_tree
tree = build_derivation_tree("fine_structure_constant")
print(tree.describe())
```

---

## 📚 Repository Map

| Directory | Purpose | Key Entry Points | Paper Cross-Ref |
|-----------|---------|------------------|------------------|
| `foundation/` | Axioms, operators (𝒢, φ-recursion), categories | `operators/grace_operator.py`, `axioms/*` | Methods, § Mathematical Foundation |
| `constants/` | Derivations of physical constants | `fine_structure_alpha.py`, `cosmological_constant_derivation.py` | Constants sections |
| `cosmology/` | Inflation, CMB, dark energy | `cmb_power_spectrum.py`, `inflation_theory.py` | Cosmology sections |
| `structures/` | Gauge groups, particle spectrum | `gauge_group_emergence.py`, `dimensional_bridge.py` | Particle physics |
| `figures/` | Figure generation + provenance | `generators/generate_all_figures.py`, `cmb_skymap.py` | All figures |
| `validation/` | Provenance, falsification tests | `anti_contamination.py`, `api_contracts.py` | Validation & predictions |
| `arxiv_paper/` | Paper sources and PDFs | `FIRM_FINAL_SUBMISSION/main.tex` | Full paper |

---

## 🖼️ Reproduce Figures

Generate all figures (deterministic):
```bash
# Option A: unified generator (if present)
python figures/generators/generate_all_figures.py

# Option B: comprehensive generator
python figures/generators/comprehensive_figure_generator.py
```

Selected key figures:
```bash
# CMB sky map (ex nihilo)
python figures/cmb_skymap.py

# CMB TT spectrum comparison
python figures/cmb_planck_tt_comparison.py

# Dark energy φ-scaling
python figures/critical_review_figures.py  # or see cosmology-specific generators
```

Provenance audit:
```bash
# Verify all figure assets are referenced + reproducible
python figures/audit_figures.py
```

---

## 🔐 Registered Predictions & Provenance

- Registry (machine-readable):
  - Primary: see `validation/` (module-level registrations)
  - Paper bundle: `arxiv_paper/FIRM_FINAL_SUBMISSION/validation/firm_predictions_registry.json`
- Provenance for figures: `data/provenance/figures_manifest.json`
- Integrity policy: **no tuning** to match observations; divergences are preserved as predictions and logged.

Add a new prediction (workflow):
1. Implement derivation (no empirical inputs) under `constants/` or `cosmology/`
2. Add registry entry (ID, derivation path, code refs, timestamp)
3. Include falsification test in `testing/validation/`

Example registry entry (conceptual):
```json
{
  "id": "alpha_inverse_phi_recursive_v1",
  "quantity": "alpha_inverse",
  "theory": "phi_recursive_morphic",
  "value": 137.0360,
  "code": ["constants/fine_structure_alpha.py:FineStructureConstant"],
  "registered_at": "2025-08-16T00:00:00Z"
}
```

---

## 📄 arXiv Paper & Publication
- Complete paper and sources in `arxiv_paper/FIRM_FINAL_SUBMISSION/`
- PDFs: [`FIRM_Main.pdf`](arxiv_paper/FIRM_FINAL_SUBMISSION/FIRM_Main.pdf), [`main.pdf`](arxiv_paper/FIRM_FINAL_SUBMISSION/main.pdf)
- Build steps included in `00README.XXX`

---

## 🧪 Testing & Validation
```bash
# Run test suite
pytest testing/ -v

# Targeted validation
pytest testing/validation/ -k provenance
pytest testing/constants/ -k fine_structure
pytest testing/cosmology/ -k cmb
```
Falsification criteria and prediction checks run continuously; failures are treated as theory signals, not tuning prompts.

---

## ⚖️ Scientific Integrity
- No empirical curve fitting or free parameters
- Axiom → derivation → prediction provenance
- Predictions registered a priori; divergences preserved
- Reproducible builds and figure pipelines

---

## 🤝 Contributing
**Standards (must):**
- All derivations trace to foundational axioms
- Zero empirical fitting or parameter tuning
- Complete provenance and tests required
- Theoretical changes undergo peer review

**Dev Setup**
```bash
git clone https://github.com/ktynski/FIRM-Fractal-Identity-Recursive-Mechanics.git
cd ExNahiloReality
pip install -e ".[dev]"
pytest  # Verify tests pass
```

---

## 📄 Citation
If you use FIRM in your research, please cite the arXiv paper (preprint info in `arxiv_paper/FIRM_FINAL_SUBMISSION/`).

---

## 📞 Contact & Support
- GitHub Issues / Discussions
- Documentation in `docs/`
- Academic inquiries via repository

---

## 🔎 Known Divergences (Predictions vs Measurements)

Integrity note: We do not tune predictions to match measurements. Use the following to generate and view current divergences (context-only):

```bash
# Run validation suites that emit comparison artifacts
pytest testing/validation/ -v

# Example: export comparison artifacts (paths may vary by test)
# Look under these for JSON/MD summaries
ls -1 validation/ | cat
ls -1 reports/ | cat
```

Artifacts typically include JSON/Markdown summaries of theoretical predictions and contextual measurements. All differences are logged as predictions to guide future math, not adjustments.

---

## 🧰 Environment Matrix

- Python: 3.10–3.12 (dev tested); 3.13+ supported per paper methods
- OS: Linux, macOS (Apple Silicon supported)
- TeX: TeX Live 2024+ (for paper build)
- Core Python deps: see `requirements.txt`

Recreate environment:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🤖 CI & Automation

- CI: GitHub Actions (runs lint/tests on push/PR)
- Recommended targets:
  - `pytest testing/ -v`
  - paper build smoke test: `pdflatex` + `bibtex` steps
- Artifact publication (optional): upload `main.pdf` from `arxiv_paper/FIRM_FINAL_SUBMISSION/`

---

## 📦 arXiv Packaging

Create a minimal arXiv source bundle from the paper directory:
```bash
cd arxiv_paper/FIRM_FINAL_SUBMISSION
# Ensure main.bbl exists (run the build first)
zip -r firm_arxiv_source.zip \
  main.tex main.bbl sections references/references.bib \
  figures/*.png figures_for_paper/*.png
```

See `00README.XXX` in the paper folder for build instructions.

---

## ❓ FAQ (Short)

- **Do you ever compare against data?**
  Yes, for context only—after registering predictions a priori. Differences are preserved and logged; no tuning.

- **Can I reproduce figures exactly?**
  Yes. Use the figure scripts in `figures/generators/` or the convenience scripts listed above; see `data/provenance/figures_manifest.json`.

- **How do I add a new constant derivation?**
  Implement under `constants/`, add tests and a registry entry, and document the code-path in the paper caption if it creates a figure/table.

---

## ⚖️ License
MIT License – see [LICENSE](LICENSE).

---

*FIRM: Registered predictions from pure mathematics—parameter-free, results-blind, and reproducible.*

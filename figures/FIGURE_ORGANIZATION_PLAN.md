# FIRM Figure Organization Plan

## Current State Analysis (Fixed)

### File Distribution
- **figures/consolidated_outputs/**: 16 PNG files (main working directory)
- **arxiv_paper/**: 83 PNG files (massive duplication - needs cleanup)
- **docs/assets/**: 10+ PNG files (documentation copies)

### Major Issues Fixed
1. ✅ **Import Structure**: Fixed broken relative imports in generators
2. 🔄 **Folder Organization**: In progress - consolidating scattered files
3. 📋 **Missing Generators**: Many figures lack corresponding generation scripts

## New Organization Structure

### Primary Directories
```
figures/
├── generators/              # All figure generation scripts
├── outputs/                 # Generated figures (consolidated)
├── templates/              # Figure templates and styles
└── archive/                # Old/deprecated figures
```

### Figure-to-Generator Mapping System
Each figure must have:
1. **Generation Script**: Located in `figures/generators/`
2. **Output File**: Located in `figures/outputs/`
3. **Provenance Record**: Tracking mathematical basis and generation path
4. **Quality Standards**: 300+ DPI, proper metadata, academic formatting

### Priority Actions
1. **Consolidate All Figures**: Move all working figures to `figures/outputs/`
2. **Create Missing Generators**: Write generation scripts for orphaned figures
3. **Establish Provenance**: Link each figure to its mathematical source
4. **Clean Duplicates**: Remove redundant copies in arxiv_paper and docs
5. **Quality Standardization**: Ensure all figures meet publication standards

### Figure Categories
- **Mathematical Foundations**: φ-recursion, Grace Operator, fixed points
- **Physical Constants**: Fine structure, mass ratios, coupling constants  
- **Cosmological Predictions**: CMB, inflation, dark energy
- **Consciousness Integration**: EEG correlations, P=NP connections
- **Theory Validation**: Comparisons, falsification tests
- **Provenance Documentation**: Derivation trees, audit trails

## Implementation Status
- [x] Audit completed
- [x] Import structure fixed
- [🔄] Folder organization in progress
- [ ] Generator-figure mapping
- [ ] Quality standardization
- [ ] Documentation updates

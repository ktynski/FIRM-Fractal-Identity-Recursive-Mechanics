"""
Generate All FSCTF Figures: Comprehensive Visualization Suite

This script generates a complete set of visualizations for the FSCTF framework,
covering all major theoretical components with complete mathematical provenance.

Figure Categories Generated:
1. Mathematical Foundations (φ-recursion, Grace Operator, morphic complexity)
2. Physical Emergence (spacetime, gauge groups, force couplings)
3. Particle Physics (mass hierarchies, mixing angles)
4. Cosmological Predictions (CMB, inflation, dark energy)
5. Consciousness Integration (P=NP, EEG patterns)
6. Theory Validation (comparisons, falsification tests)
7. Provenance Tracking (derivation trees, audit trails)

All figures maintain complete academic integrity with cryptographic provenance.
"""

import sys
import os
from pathlib import Path
from typing import List, Dict, Any
import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import figure generators
try:
    from .generator import PROVENANCE_FIGURE_GENERATOR
    from .comprehensive_figure_generator import COMPREHENSIVE_FIGURE_GENERATOR
    from .advanced_figure_generator import ADVANCED_FIGURE_GENERATOR
    from .particle_masses import ParticleMassVisualizer
    from .cmb_predictions import CMBVisualizer
    from .cmb_skymap import CMBSKYMAP
    from .consciousness_correlations import ConsciousnessCorrelationVisualizer
    from .comparison_plots import TheoryComparisonVisualizer
    from .provenance_graph import ProvenanceGraphVisualizer
    from .peer_review_critical_figures import generate_peer_review_figures
    from .manifest import build_and_write_manifest
    from .validation_overlays import VALIDATION_OVERLAYS
    from .einstein_equations_derivation_figures import EinsteinEquationsFigureGenerator
except ImportError as e:
    print(f"Import error: {e}")
    print("Continuing with available generators...")

def generate_mathematical_foundations() -> List[Dict[str, Any]]:
    """Generate mathematical foundation figures"""
    results = []

    print("Generating mathematical foundation figures...")

    # φ-convergence basins
    try:
        result = COMPREHENSIVE_FIGURE_GENERATOR._generate_phi_basin_figure()
        results.append(result)
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed φ-basin figure: {e}")

    # Grace Operator landscape
    try:
        result = COMPREHENSIVE_FIGURE_GENERATOR._generate_grace_operator_landscape()
        results.append(result)
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed Grace Operator landscape: {e}")

    # Morphic complexity analysis
    try:
        result = ADVANCED_FIGURE_GENERATOR.generate_morphic_complexity_figure()
        results.append(result)
        print(f"✓ Generated: {result['title']}")
    except Exception as e:
        print(f"✗ Failed morphic complexity: {e}")

    # Spacetime emergence
    try:
        result = COMPREHENSIVE_FIGURE_GENERATOR._generate_spacetime_emergence_figure()
        results.append(result)
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed spacetime emergence: {e}")

    # Einstein equations derivation (new theoretical foundation)
    try:
        einstein_generator = EinsteinEquationsFigureGenerator()
        einstein_results = einstein_generator.generate_all_einstein_figures()
        for name, result in einstein_results.items():
            results.append(result)
            print(f"✓ Generated: {result['title']}")
    except Exception as e:
        print(f"✗ Failed Einstein equations figures: {e}")

    return results

def generate_physical_emergence() -> List[Dict[str, Any]]:
    """Generate physical emergence figures"""
    results = []

    print("Generating physical emergence figures...")

    # Gauge group emergence
    try:
        result = ADVANCED_FIGURE_GENERATOR.generate_gauge_emergence_figure()
        results.append(result)
        print(f"✓ Generated: {result['title']}")
    except Exception as e:
        print(f"✗ Failed gauge emergence: {e}")

    # Force coupling evolution
    try:
        result = ADVANCED_FIGURE_GENERATOR.generate_coupling_evolution_figure()
        results.append(result)
        print(f"✓ Generated: {result['title']}")
    except Exception as e:
        print(f"✗ Failed coupling evolution: {e}")

    # Particle mass hierarchy
    try:
        visualizer = ParticleMassVisualizer()
        result = visualizer.generate_mass_hierarchy_plot()
        results.append({
            "category": "physical_emergence",
            "figure_type": "particle_mass_hierarchy",
            "title": result.title,
            "file_path": "figures/particle_mass_hierarchy.png",
            "mathematical_basis": result.mathematical_basis,
            "figure_object": result.figure_object
        })
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed particle mass hierarchy: {e}")

    return results

def generate_cosmological_predictions() -> List[Dict[str, Any]]:
    """Generate cosmological prediction figures"""
    results = []

    print("Generating cosmological prediction figures...")

    # CMB power spectrum (original)
    try:
        visualizer = CMBVisualizer()
        result = visualizer.generate_power_spectrum_plot()
        results.append({
            "category": "cosmological_predictions",
            "figure_type": "cmb_power_spectrum",
            "title": result.title,
            "file_path": "figures/cmb_power_spectrum_prediction.png",
            "mathematical_basis": result.mathematical_basis,
            "figure_object": result.figure_object
        })
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed CMB power spectrum: {e}")

    # Classic CMB theory-only figures (ℓ-space and m-space)
    try:
        from .cmb_classic_figures import generate_classic_cmb_figures
        classic_results = generate_classic_cmb_figures()
        for item in classic_results:
            results.append({
                "category": "cosmological_predictions",
                "figure_type": "cmb_classic",
                "title": "CMB classic figure",
                "file_path": item.get("file", ""),
            })
        print(f"✓ Generated {len(classic_results)} classic CMB figures (theory-only)")
    except Exception as e:
        print(f"✗ Failed classic CMB figures: {e}")
    # Theory-only skymap (low-ℓ)
    try:
        sky = CMBSKYMAP.generate_skymap()
        results.append({
            "category": "cosmological_predictions",
            "figure_type": "cmb_skymap_phi_native",
            "title": "Theory-only CMB Skymap (φ-native)",
            "file_path": sky.get("file", "")
        })
        print("✓ Generated: Theory-only CMB Skymap (φ-native)")
    except Exception as e:
        print(f"✗ Failed theory-only CMB skymap: {e}")

    return results

def generate_consciousness_integration() -> List[Dict[str, Any]]:
    """Generate consciousness integration figures"""
    results = []

    print("Generating consciousness integration figures...")

    # Consciousness correlations
    try:
        visualizer = ConsciousnessCorrelationVisualizer()
        result = visualizer.generate_consciousness_correlation_plot()
        results.append({
            "category": "consciousness_integration",
            "figure_type": "consciousness_correlation",
            "title": result.title,
            "file_path": "figures/consciousness_correlations.png",
            "mathematical_basis": result.mathematical_basis,
            "figure_object": result.figure_object
        })
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed consciousness correlations: {e}")

    return results

def generate_theory_validation() -> List[Dict[str, Any]]:
    """Generate theory validation figures"""
    results = []

    print("Generating theory validation figures...")

    # FIRM vs Standard Model comparison (demo-only; keep as non-claim visualization)
    try:
        visualizer = TheoryComparisonVisualizer()
        result = visualizer.generate_firm_vs_sm_comparison()
        results.append({
            "category": "theory_validation",
            "figure_type": "firm_vs_sm_comparison",
            "title": result.title,
            "file_path": "figures/firm_vs_standard_model_comparison.png",
            "mathematical_basis": result.mathematical_basis,
            "figure_object": result.figure_object
        })
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed FIRM vs SM comparison: {e}")
    # Validation-gated overlays (only if firewall allows)
    try:
        overlays = VALIDATION_OVERLAYS.generate_all()
        for item in overlays:
            results.append({
                "category": "theory_validation",
                "figure_type": "validation_overlay",
                "title": "Validation-Gated Overlay",
                "file_path": item.get("file", "")
            })
        if overlays:
            print(f"✓ Generated {len(overlays)} validation overlay figure(s)")
    except Exception as e:
        print(f"✗ Failed validation overlays: {e}")

    return results

def generate_provenance_tracking() -> List[Dict[str, Any]]:
    """Generate provenance tracking figures"""
    results = []

    print("Generating provenance tracking figures...")

    # Provenance graph
    try:
        visualizer = ProvenanceGraphVisualizer()
        result = visualizer.generate_provenance_graph()
        results.append({
            "category": "provenance_tracking",
            "figure_type": "provenance_graph",
            "title": result.title,
            "file_path": "figures/provenance_graph.png",
            "mathematical_basis": result.mathematical_basis,
            "figure_object": result.figure_object
        })
        print(f"✓ Generated: {result.title}")
    except Exception as e:
        print(f"✗ Failed provenance graph: {e}")

    return results

def generate_peer_review_set() -> List[Dict[str, Any]]:
    """Generate peer-review critical figures (extended set)."""
    try:
        return generate_peer_review_figures()
    except Exception as e:
        print(f"✗ Failed peer-review figure set: {e}")
        return []

def generate_all_figures() -> List[Dict[str, Any]]:
    """Generate complete set of FSCTF figures"""
    all_results = []

    print("=" * 60)
    print("FSCTF COMPREHENSIVE FIGURE GENERATION")
    print("=" * 60)
    print(f"Started at: {datetime.datetime.now()}")
    print()

    # Generate all figure categories
    all_results.extend(generate_mathematical_foundations())
    all_results.extend(generate_physical_emergence())
    all_results.extend(generate_cosmological_predictions())
    all_results.extend(generate_consciousness_integration())
    all_results.extend(generate_theory_validation())
    all_results.extend(generate_provenance_tracking())
    all_results.extend(generate_peer_review_set())

    print()
    print("=" * 60)
    print(f"FIGURE GENERATION COMPLETE")
    print(f"Generated {len(all_results)} figures")
    print(f"Completed at: {datetime.datetime.now()}")
    print("=" * 60)

    return all_results

def generate_figure_summary(results: List[Dict[str, Any]]) -> str:
    """Generate summary of all generated figures"""
    summary = []
    summary.append("# FSCTF Figure Generation Summary")
    summary.append(f"Generated: {datetime.datetime.now()}")
    summary.append(f"Total Figures: {len(results)}")
    summary.append("")

    # Group by category
    categories = {}
    for result in results:
        category = result.get("category", "unknown")
        if category not in categories:
            categories[category] = []
        categories[category].append(result)

    for category, figures in categories.items():
        summary.append(f"## {category.replace('_', ' ').title()}")
        summary.append(f"Figures: {len(figures)}")
        for figure in figures:
            title = figure.get("title", "Unknown")
            file_path = figure.get("file_path", "Unknown")
            summary.append(f"- {title}: `{file_path}`")
        summary.append("")

    return "\n".join(summary)

def main():
    """Main function to generate all figures"""
    try:
        # Generate all figures
        results = generate_all_figures()

        # Generate summary
        summary = generate_figure_summary(results)

        # Save summary
        summary_path = "figures/figure_generation_summary.md"
        with open(summary_path, 'w') as f:
            f.write(summary)

        print(f"\nSummary saved to: {summary_path}")
        # Write manifest for stable inventory
        manifest_path = build_and_write_manifest(results, figures_dir=str(Path('figures')), out_file="figures/FIGURE_MANIFEST.json")
        print(f"Manifest written to: {manifest_path}")

        # List all generated files
        figures_dir = Path("figures")
        png_files = list(figures_dir.glob("*.png"))

        print(f"\nGenerated {len(png_files)} PNG files:")
        for png_file in sorted(png_files):
            print(f"  {png_file.name}")

        return results

    except Exception as e:
        print(f"Error in figure generation: {e}")
        return []

if __name__ == "__main__":
    main()
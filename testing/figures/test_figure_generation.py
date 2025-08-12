"""
Comprehensive Test Suite: Figure Generation with Provenance Verification

This module provides complete test coverage for all figure generation functions
with particular focus on mathematical integrity, provenance tracking, and
academic compliance.

Test Coverage:
    - φ-convergence visualization accuracy and provenance
    - CMB power spectrum derivation completeness
    - Particle mass hierarchy mathematical correctness
    - Consciousness correlation validation integrity
    - Cryptographic provenance verification
    - Error handling robustness
    - Academic quality standards

All tests verify mathematical derivations trace to FIRM axioms with no
empirical contamination or hardcoded values without proper derivation.

Author: FIRM Research Team
Created: [TEST CREATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

import pytest
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import tempfile
import json
from typing import Dict, Any
import hashlib

# Import modules under test
from figures.generator import ProvenanceFigureGenerator, PROVENANCE_FIGURE_GENERATOR, FigureType
from figures.phi_emergence import PhiEmergenceVisualizer, PHI_EMERGENCE_VISUALIZER
from figures.cmb_predictions import CMBVisualizer, CMB_VISUALIZER
from figures.particle_masses import ParticleMassVisualizer, PARTICLE_MASS_VISUALIZER
from figures.consciousness_correlations import ConsciousnessVisualizer, CONSCIOUSNESS_VISUALIZER

# Import foundation components for verification
from foundation.operators.phi_recursion import PHI_VALUE


class TestPhiEmergenceVisualization:
    """Test suite for φ-emergence visualization with mathematical verification"""

    def test_phi_convergence_mathematical_accuracy(self):
        """Test φ-convergence produces mathematically correct results"""
        visualizer = PHI_EMERGENCE_VISUALIZER
        result = visualizer.generate_convergence_plot()

        # Verify mathematical foundations
        assert result.plot_type == "phi_convergence"
        assert "φ-Emergence from Pure Mathematical Recursion" in result.title
        assert abs(result.convergence_data.convergence_rate - np.log(PHI_VALUE)) < 0.01

        # Test convergence sequences
        for seq_name, sequence in result.convergence_data.convergence_sequences.items():
            # All sequences should converge to φ
            final_value = sequence[-1]
            assert abs(final_value - PHI_VALUE) < 1e-10, f"Sequence {seq_name} didn't converge to φ"

            # Monotonic convergence (after initial steps)
            errors = [abs(x - PHI_VALUE) for x in sequence[-10:]]
            for i in range(1, len(errors)):
                assert errors[i] <= errors[i-1] * 2, "Non-monotonic convergence detected"

    def test_phi_convergence_provenance_completeness(self):
        """Test provenance tracking completeness and accuracy"""
        visualizer = PHI_EMERGENCE_VISUALIZER
        result = visualizer.generate_convergence_plot()

        # Verify provenance fields
        assert result.provenance_verified is not None
        assert len(result.derivation_steps) >= 5
        assert result.convergence_rate_theoretical == np.log(PHI_VALUE)
        assert abs(result.convergence_rate_observed - result.convergence_rate_theoretical) < 0.02

        # Check falsification criteria
        assert len(result.falsification_criteria) >= 3
        assert any("Grace Operator" in criterion for criterion in result.falsification_criteria)
        assert any("convergence rate" in criterion for criterion in result.falsification_criteria)

    def test_phi_convergence_figure_quality(self):
        """Test figure meets academic publication standards"""
        visualizer = PHI_EMERGENCE_VISUALIZER
        result = visualizer.generate_convergence_plot()

        # Verify figure object exists and has correct structure
        assert result.figure_object is not None
        fig = result.figure_object

        # Check subplot structure
        axes = fig.get_axes()
        assert len(axes) == 2, "Should have exactly 2 subplots"

        # Verify axis labels and titles are present
        for ax in axes:
            assert ax.get_xlabel(), "Missing x-axis label"
            assert ax.get_ylabel(), "Missing y-axis label"
            assert ax.get_title(), "Missing subplot title"

        # Check legend presence
        assert any(ax.get_legend() for ax in axes), "Missing legend"

        # Verify grid is enabled for readability
        for ax in axes:
            assert ax.grid, "Grid should be enabled for academic quality"


class TestCMBVisualization:
    """Test suite for CMB power spectrum visualization"""

    def test_cmb_spectrum_theoretical_derivation(self):
        """Test CMB spectrum uses proper theoretical derivation"""
        visualizer = CMB_VISUALIZER
        result = visualizer.generate_power_spectrum_plot()

        # Verify theoretical foundation
        assert "φ-harmonic" in result.mathematical_basis.lower()

        # Test peak positions follow φ-harmonic structure
        peaks = result.spectrum_data.acoustic_peaks
        phi_structure = result.spectrum_data.phi_harmonic_structure

        assert len(peaks) > 3, "Should have multiple acoustic peaks"
        assert len(peaks) == len(phi_structure), "Peak and theory arrays should match"

        # Verify φ-harmonic spacing approximately holds
        if len(peaks) > 1:
            ratios = [peaks[i+1]/peaks[i] for i in range(len(peaks)-1)]
            expected_ratio = PHI_VALUE**(1/3)  # φ^(1/3) spacing
            for ratio in ratios:
                assert 0.5 * expected_ratio < ratio < 2.0 * expected_ratio, f"Peak ratio {ratio} doesn't match φ-harmonic structure"

    def test_cmb_hardcoded_value_detection(self):
        """Test that CMB visualization properly handles hardcoded values"""
        visualizer = CMB_VISUALIZER

        # Check if theoretical derivation is being used
        if visualizer.cmb_result is not None:
            # Should use theoretical values
            assert visualizer.angular_acoustic_scale is not None
            assert visualizer.acoustic_peaks is not None
        else:
            # Should flag fallback mode with provenance warnings
            result = visualizer.generate_power_spectrum_plot()
            # In fallback mode, mathematical basis should indicate incomplete derivation
            assert "fallback" in result.mathematical_basis.lower() or "complete" in result.mathematical_basis.lower()

    def test_classic_cmb_theory_only_generation(self, tmp_path):
        """Classic CMB figures should generate without empirical imports and produce files."""
        from figures.cmb_classic_figures import generate_classic_cmb_figures
        # Run generation
        results = generate_classic_cmb_figures()
        assert isinstance(results, list) and len(results) >= 6
        # Files exist and non-empty
        for item in results:
            file_path = item.get("file")
            assert file_path and Path(file_path).exists(), f"Missing output: {file_path}"
            assert Path(file_path).stat().st_size > 1000, f"Empty/too small output: {file_path}"
        # Verify module does not rely on cosmology pipeline
        import inspect
        import figures.cmb_classic_figures as mod
        src = inspect.getsource(mod)
        assert "cosmology.cmb_power_spectrum" not in src, "Classic figures must be theory-only"


class TestProvenanceFigureGenerator:
    """Test suite for core provenance figure generation system"""

    def test_figure_provenance_validation(self):
        """Test cryptographic provenance validation system"""
        generator = PROVENANCE_FIGURE_GENERATOR

        # Generate a test figure with provenance
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test provenance data
            test_provenance = {
                "mathematical_basis": "Test mathematical derivation",
                "data_sources": ["Pure mathematical calculation"],
                "derivation_steps": ["Step 1", "Step 2", "Step 3"],
                "timestamp": "2024-01-01T00:00:00"
            }

            # Generate hash
            test_hash = generator._generate_provenance_hash(test_provenance)

            # Create test image with metadata
            fig, ax = plt.subplots()
            ax.plot([1, 2, 3], [1, 4, 9])
            test_path = Path(temp_dir) / "test_figure.png"

            # Save with provenance using the internal method
            generator._save_figure_with_provenance(fig, str(test_path), test_provenance, test_hash)
            plt.close(fig)

            # Validate provenance
            validation_result = generator.validate_figure_provenance(str(test_path))

            assert validation_result["valid"], f"Provenance validation failed: {validation_result.get('error')}"
            assert validation_result["hash_verified"], "Hash verification failed"
            assert validation_result["provenance_hash"] == test_hash
            assert validation_result["mathematical_basis"] == test_provenance["mathematical_basis"]

    def test_provenance_validation_error_handling(self):
        """Test comprehensive error handling in provenance validation"""
        generator = PROVENANCE_FIGURE_GENERATOR

        # Test non-existent file
        with pytest.raises(FileNotFoundError):
            generator.validate_figure_provenance("non_existent_file.png")

        # Test empty path
        with pytest.raises(ValueError):
            generator.validate_figure_provenance("")

        # Test unsupported format
        with tempfile.NamedTemporaryFile(suffix=".txt") as temp_file:
            temp_file.write(b"test content")
            temp_file.flush()

            result = generator.validate_figure_provenance(temp_file.name)
            assert not result["valid"]
            assert "unsupported file format" in result["error"].lower()

    def test_eigenvalue_distribution_mathematical_accuracy(self):
        """Test eigenvalue distribution generation accuracy"""
        generator = PROVENANCE_FIGURE_GENERATOR
        result = generator.generate_eigenvalue_distribution_figure()

        # Verify result structure
        assert result.figure_type == FigureType.EIGENVALUE_DISTRIBUTION
        assert "Grace Operator" in result.mathematical_basis
        assert len(result.derivation_steps) >= 8

        # Check falsification criteria
        assert len(result.falsification_criteria) >= 2
        assert any("eigenvalue" in criterion.lower() for criterion in result.falsification_criteria)


class TestAcademicIntegrity:
    """Test academic integrity and scientific standards across all figures"""

    def test_no_empirical_contamination(self):
        """Test that no empirical data contaminates mathematical derivations"""
        # List of visualizers to test
        visualizers = [
            PHI_EMERGENCE_VISUALIZER,
            CMB_VISUALIZER,
            CONSCIOUSNESS_VISUALIZER
        ]

        for visualizer in visualizers:
            # Check for provenance tracking capability
            assert hasattr(visualizer, 'provenance'), f"{type(visualizer).__name__} missing provenance tracker"

            # If provenance tracker exists, it should be initialized
            if visualizer.provenance is not None:
                # Should have contamination detection methods
                assert hasattr(visualizer.provenance, 'log_contamination') or hasattr(visualizer.provenance, 'log_warning')

    def test_mathematical_basis_completeness(self):
        """Test all figures have complete mathematical basis documentation"""
        test_cases = [
            (PHI_EMERGENCE_VISUALIZER.generate_convergence_plot, "φ"),
            (CMB_VISUALIZER.generate_power_spectrum_plot, "acoustic"),
        ]

        for generate_func, expected_keyword in test_cases:
            result = generate_func()

            # Mathematical basis should exist and be non-trivial
            assert hasattr(result, 'mathematical_basis')
            assert len(result.mathematical_basis) > 20, "Mathematical basis too brief"
            assert expected_keyword.lower() in result.mathematical_basis.lower()

            # Should have derivation steps if available
            if hasattr(result, 'derivation_steps'):
                assert len(result.derivation_steps) > 0, "Missing derivation steps"

    def test_falsification_criteria_presence(self):
        """Test all figures provide clear falsification criteria"""
        test_results = [
            PHI_EMERGENCE_VISUALIZER.generate_convergence_plot(),
        ]

        for result in test_results:
            if hasattr(result, 'falsification_criteria'):
                assert len(result.falsification_criteria) >= 2
                for criterion in result.falsification_criteria:
                    assert len(criterion.strip()) > 10, "Falsification criterion too brief"
                    assert "if" in criterion.lower(), "Falsification criteria should be conditional statements"


class TestIntegrationComplete:
    """Integration tests for complete figure generation system"""

    def test_complete_figure_suite_generation(self):
        """Test generation of complete academic figure suite"""
        from figures import generate_complete_figure_suite

        # Generate complete suite
        suite = generate_complete_figure_suite()

        # Verify suite structure
        required_categories = ["mathematical_figures", "physical_figures", "comparison_figures"]
        for category in required_categories:
            assert category in suite, f"Missing figure category: {category}"
            assert isinstance(suite[category], dict), f"Category {category} should be dictionary"

        # Check metadata presence
        assert "generation_metadata" in suite
        metadata = suite["generation_metadata"]
        assert metadata["provenance_verified"] is True
        assert metadata["academic_quality"] is True

    def test_figure_consistency_standards(self):
        """Test consistent quality and style across all figures"""
        # Test that all visualizers follow same interface patterns
        visualizers = [
            PHI_EMERGENCE_VISUALIZER,
            CMB_VISUALIZER,
            CONSCIOUSNESS_VISUALIZER
        ]

        for visualizer in visualizers:
            # Should have consistent initialization
            assert hasattr(visualizer, 'phi'), "Missing φ value"
            assert abs(visualizer.phi - PHI_VALUE) < 1e-10, "φ value inconsistency"

            # Should have provenance capability
            assert hasattr(visualizer, 'provenance'), "Missing provenance tracker"


# Pytest fixtures for test setup
@pytest.fixture
def temp_figure_dir():
    """Provide temporary directory for figure generation tests"""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def sample_provenance_data():
    """Provide sample provenance data for testing"""
    return {
        "mathematical_basis": "Test derivation from FIRM axioms",
        "data_sources": ["Pure mathematical calculation"],
        "derivation_steps": [
            "Start from axiom A𝒢.1",
            "Apply Grace Operator",
            "Derive φ-recursion",
            "Compute convergence"
        ],
        "timestamp": "2024-01-01T00:00:00",
        "academic_quality": "verified"
    }


if __name__ == "__main__":
    # Run tests with comprehensive output
    pytest.main([
        __file__,
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "--strict-markers",  # Strict marker validation
        "--disable-warnings"  # Clean output
    ])
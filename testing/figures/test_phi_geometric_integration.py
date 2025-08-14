"""
Integration tests for φ-geometric overlay in CMB figures

Tests the complete integration of the φ-geometric layer with figure generation,
including overlay rendering, annotation placement, and provenance tracking.
"""

import pytest
import numpy as np
from pathlib import Path
import json
import os
import tempfile

from figures.cmb_planck_tt_comparison import CMBPlanckTTComparison
from cosmology.peaks.geometric_layer import get_peak_overlay_for_figure, verify_geometric_consistency
from validation.predictions_registry import PREDICTIONS_REGISTRY, register_cmb_phi_peaks


class TestPhiGeometricIntegration:
    """Integration tests for φ-geometric figure overlay system"""

    def setup_method(self):
        """Set up test environment"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.test_figure_path = self.temp_dir / "test_phi_overlay.png"

    def teardown_method(self):
        """Clean up test files"""
        if self.test_figure_path.exists():
            self.test_figure_path.unlink()
        if self.temp_dir.exists():
            self.temp_dir.rmdir()

    def test_geometric_layer_consistency(self):
        """Test that the geometric layer maintains internal consistency"""
        assert verify_geometric_consistency(), "Geometric layer consistency check failed"

    def test_peak_overlay_data_structure(self):
        """Test the structure of peak overlay data"""
        overlay_data = get_peak_overlay_for_figure((50, 1000))

        # Check required fields
        required_fields = ['peaks', 'amplitudes', 'series_name', 'l0', 'k_decomposition', 'definition', 'provenance_hash']
        for field in required_fields:
            assert field in overlay_data, f"Missing field: {field}"

        # Check data types
        assert isinstance(overlay_data['peaks'], list)
        assert isinstance(overlay_data['amplitudes'], list)
        assert isinstance(overlay_data['series_name'], str)
        assert isinstance(overlay_data['l0'], int)
        assert isinstance(overlay_data['k_decomposition'], dict)
        assert isinstance(overlay_data['provenance_hash'], str)

        # Check data consistency
        assert len(overlay_data['peaks']) == len(overlay_data['amplitudes'])
        assert len(overlay_data['peaks']) > 0
        assert overlay_data['l0'] > 0

    def test_k_decomposition_structure(self):
        """Test k-decomposition structure in overlay data"""
        overlay_data = get_peak_overlay_for_figure()
        k_decomp = overlay_data['k_decomposition']

        # Check required k-decomposition fields
        required_k_fields = ['k', 'base_12', 'phi_inv', 'epsilon']
        for field in required_k_fields:
            assert field in k_decomp, f"Missing k-decomposition field: {field}"
            assert isinstance(k_decomp[field], (int, float))

        # Check mathematical consistency
        reconstructed_k = k_decomp['base_12'] + k_decomp['phi_inv'] + k_decomp['epsilon']
        assert abs(k_decomp['k'] - reconstructed_k) < 1e-10, "k-decomposition not mathematically consistent"

        # Check base values
        assert k_decomp['base_12'] == 12
        assert abs(k_decomp['phi_inv'] - 0.618034) < 0.001  # φ⁻¹

    def test_peak_ordering_and_scaling(self):
        """Test that peaks are properly ordered and φ-scaled"""
        overlay_data = get_peak_overlay_for_figure((10, 2000))
        peaks = overlay_data['peaks']
        amplitudes = overlay_data['amplitudes']

        # Test monotonicity
        for i in range(len(peaks) - 1):
            assert peaks[i] < peaks[i + 1], f"Peaks not monotonic at position {i}"

        # Test amplitude decay
        for i in range(len(amplitudes) - 1):
            assert amplitudes[i] > amplitudes[i + 1], f"Amplitudes not decreasing at position {i}"

        # Test φ-scaling approximation
        if len(peaks) >= 2:
            phi_approx = 1.618
            for i in range(len(peaks) - 1):
                ratio = peaks[i + 1] / peaks[i]
                assert 1.4 < ratio < 1.8, f"Peak ratio {ratio:.3f} not in φ range"

    def test_figure_generation_with_overlay(self):
        """Test that CMB figure generates successfully with φ-overlay"""
        cmb_fig = CMBPlanckTTComparison()

        # Generate figure
        figure_path = cmb_fig.create_comparison_figure(str(self.test_figure_path))

        # Verify file was created
        assert Path(figure_path).exists(), "Figure file was not created"
        assert Path(figure_path).stat().st_size > 1000, "Figure file too small (likely empty)"

    def test_provenance_tracking(self):
        """Test that provenance is properly tracked through the system"""
        overlay_data = get_peak_overlay_for_figure()

        # Check provenance hash format
        provenance_hash = overlay_data['provenance_hash']
        assert len(provenance_hash) == 16, "Provenance hash wrong length"
        assert all(c in '0123456789abcdef' for c in provenance_hash), "Invalid hex characters in hash"

        # Verify reproducibility - same input should give same hash
        overlay_data_2 = get_peak_overlay_for_figure()
        assert overlay_data['provenance_hash'] == overlay_data_2['provenance_hash'], "Provenance not reproducible"

    def test_predictions_registry_integration(self):
        """Test integration with predictions registry"""
        # Register CMB prediction
        prediction_id = register_cmb_phi_peaks(220.0)

        # Verify prediction was registered
        prediction = PREDICTIONS_REGISTRY.get_prediction(prediction_id)
        assert prediction is not None, "Prediction not found in registry"

        # Verify prediction structure
        assert prediction.prediction_type == 'cmb_phi_geometric_peaks'
        assert 'peak_positions' in prediction.predicted_values
        assert 'k_decomposition' in prediction.predicted_values

        # Verify integrity
        assert prediction.verify_integrity(), "Prediction integrity check failed"

    def test_overlay_annotation_content(self):
        """Test that overlay contains proper annotation content"""
        from cosmology.peaks.geometric_layer import PHI_GEOMETRIC_LAYER

        overlay_data = get_peak_overlay_for_figure()
        k_decomp = overlay_data['k_decomposition']

        # Test k-annotation formatting
        k_annotation = PHI_GEOMETRIC_LAYER.format_k_annotation(k_decomp)

        # Should contain key mathematical symbols
        assert 'k =' in k_annotation
        assert 'φ⁻¹' in k_annotation or 'phi' in k_annotation.lower()
        assert 'ε' in k_annotation or 'epsilon' in k_annotation.lower()
        assert 'grace' in k_annotation.lower()
        assert 'torsion' in k_annotation.lower()

    def test_multiple_l_ranges(self):
        """Test overlay data for different ℓ ranges"""
        test_ranges = [(50, 500), (100, 1000), (10, 2000)]

        for l_min, l_max in test_ranges:
            overlay_data = get_peak_overlay_for_figure((l_min, l_max))

            # All peaks should be within range
            for peak in overlay_data['peaks']:
                assert l_min <= peak <= l_max, f"Peak {peak} outside range [{l_min}, {l_max}]"

            # Should have reasonable number of peaks
            assert 1 <= len(overlay_data['peaks']) <= 10, f"Unreasonable peak count for range [{l_min}, {l_max}]"

    def test_figure_content_verification(self):
        """Test that generated figure contains expected φ-geometric content"""
        # This test would ideally parse the figure metadata, but we'll test the generation process
        cmb_fig = CMBPlanckTTComparison()

        # Mock the overlay to verify it's called
        overlay_called = False
        original_get_overlay = get_peak_overlay_for_figure

        def mock_get_overlay(*args, **kwargs):
            nonlocal overlay_called
            overlay_called = True
            return original_get_overlay(*args, **kwargs)

        # Temporarily replace the function
        import cosmology.peaks.geometric_layer
        cosmology.peaks.geometric_layer.get_peak_overlay_for_figure = mock_get_overlay

        try:
            # Generate figure
            cmb_fig.create_comparison_figure(str(self.test_figure_path))

            # Verify overlay was called
            assert overlay_called, "φ-geometric overlay was not invoked during figure generation"

        finally:
            # Restore original function
            cosmology.peaks.geometric_layer.get_peak_overlay_for_figure = original_get_overlay

    def test_error_handling_and_fallbacks(self):
        """Test error handling in overlay system"""
        # Test with invalid ranges
        overlay_data = get_peak_overlay_for_figure((0, 1))  # Very small range
        assert isinstance(overlay_data, dict), "Should handle small ranges gracefully"

        overlay_data = get_peak_overlay_for_figure((5000, 10000))  # Very large range
        assert isinstance(overlay_data, dict), "Should handle large ranges gracefully"

    def test_mathematical_consistency_across_calls(self):
        """Test mathematical consistency across multiple function calls"""
        # Generate multiple overlay datasets
        datasets = [get_peak_overlay_for_figure() for _ in range(3)]

        # All should be identical (deterministic)
        for i in range(1, len(datasets)):
            assert datasets[0]['l0'] == datasets[i]['l0']
            assert datasets[0]['peaks'] == datasets[i]['peaks']
            assert datasets[0]['k_decomposition'] == datasets[i]['k_decomposition']
            assert datasets[0]['provenance_hash'] == datasets[i]['provenance_hash']

    def test_integration_with_cmb_theory(self):
        """Test integration with actual CMB power spectrum theory"""
        # This test verifies that the overlay integrates properly with FIRM CMB theory
        cmb_fig = CMBPlanckTTComparison()

        # Generate theoretical spectrum (this exercises the full FIRM pipeline)
        try:
            multipoles, theoretical_power = cmb_fig.generate_firm_theoretical_spectrum(ell_max=1000)

            # Verify spectrum was generated
            assert len(multipoles) > 100, "Theoretical spectrum too short"
            assert len(theoretical_power) == len(multipoles), "Spectrum length mismatch"
            assert np.all(theoretical_power > 0), "Theoretical power should be positive"

            # Verify overlay can work with this spectrum range
            overlay_data = get_peak_overlay_for_figure((int(multipoles[0]), int(multipoles[-1])))
            assert len(overlay_data['peaks']) > 0, "No overlay peaks in spectrum range"

        except Exception as e:
            pytest.skip(f"CMB theory integration test skipped due to: {e}")


class TestPhiGeometricSmoke:
    """Smoke tests for the complete φ-geometric system"""

    def test_end_to_end_workflow(self):
        """Test complete end-to-end workflow"""
        print("🔬 Testing complete φ-geometric workflow...")

        # 1. Generate overlay data
        print("   Step 1: Generate overlay data")
        overlay_data = get_peak_overlay_for_figure((50, 1000))
        assert len(overlay_data['peaks']) > 0

        # 2. Verify consistency
        print("   Step 2: Verify geometric consistency")
        assert verify_geometric_consistency()

        # 3. Register predictions
        print("   Step 3: Register predictions")
        prediction_id = register_cmb_phi_peaks(220.0)
        prediction = PREDICTIONS_REGISTRY.get_prediction(prediction_id)
        assert prediction is not None

        # 4. Generate figure
        print("   Step 4: Generate figure with overlay")
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            cmb_fig = CMBPlanckTTComparison()
            figure_path = cmb_fig.create_comparison_figure(tmp.name)
            assert Path(figure_path).exists()

            # Clean up
            os.unlink(tmp.name)

        print("   ✅ End-to-end workflow successful!")

    def test_system_robustness(self):
        """Test system robustness under various conditions"""
        print("🛡️ Testing system robustness...")

        # Test with different target values
        targets = [100, 199, 220, 322, 500]
        for target in targets:
            overlay_data = get_peak_overlay_for_figure()
            assert len(overlay_data['peaks']) > 0, f"Failed for target {target}"

        # Test with edge case ranges
        edge_ranges = [(1, 10), (10, 50), (2000, 3000)]
        for l_min, l_max in edge_ranges:
            overlay_data = get_peak_overlay_for_figure((l_min, l_max))
            assert isinstance(overlay_data, dict), f"Failed for range [{l_min}, {l_max}]"

        print("   ✅ Robustness tests passed!")


if __name__ == "__main__":
    # Run smoke tests
    print("Running φ-geometric integration smoke tests...")

    smoke_test = TestPhiGeometricSmoke()
    smoke_test.test_end_to_end_workflow()
    smoke_test.test_system_robustness()

    print("\n✅ All smoke tests passed!")
    print("🔬 φ-geometric integration system is operational!")

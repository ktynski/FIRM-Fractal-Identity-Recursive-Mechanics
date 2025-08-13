"""
Unit tests for φ-harmonic anchor geometric peak generation

Tests the mathematical correctness of φ-geometric peak candidates,
including shape properties, monotonicity, and self-similarity constraints.
"""

import pytest
import math
from cosmology.phi_harmonic_anchor import (
    generate_phi_harmonic_candidates, 
    best_candidate_by_target,
    PhiPeakSeries,
    _series_from_l0
)
from foundation.operators.phi_recursion import PHI_VALUE


class TestPhiHarmonicAnchor:
    """Test suite for φ-harmonic anchor functionality"""
    
    def test_series_from_l0_basic(self):
        """Test basic φ-series generation from ℓ₀"""
        l0 = 100
        series = _series_from_l0(l0, count=5)
        
        # Check length
        assert len(series) == 5
        
        # Check first element
        assert series[0] == l0
        
        # Check φ-scaling property
        for i in range(1, len(series)):
            expected = int(round(l0 * (PHI_VALUE ** i)))
            assert series[i] == expected
            
        # Check monotonicity
        for i in range(len(series) - 1):
            assert series[i] < series[i + 1], f"Series not monotonic at position {i}"
            
    def test_series_from_l0_phi_scaling(self):
        """Test that φ-scaling ratios converge to φ"""
        l0 = 199  # φ¹¹ ≈ 199
        series = _series_from_l0(l0, count=6)
        
        # Check ratios approach φ
        ratios = [series[i+1] / series[i] for i in range(len(series)-1)]
        
        for i, ratio in enumerate(ratios):
            # Later ratios should be closer to φ
            error = abs(ratio - PHI_VALUE)
            assert error < 0.1, f"Ratio {i} = {ratio:.6f} too far from φ = {PHI_VALUE:.6f}"
            
        # The last ratio should be very close to φ
        assert abs(ratios[-1] - PHI_VALUE) < 0.01
        
    def test_generate_phi_harmonic_candidates_structure(self):
        """Test structure of generated φ-harmonic candidates"""
        candidates = generate_phi_harmonic_candidates(max_peaks=4)
        
        # Should have multiple candidates
        assert len(candidates) >= 3, "Should generate at least 3 candidate types"
        
        # Check each candidate structure
        for candidate in candidates:
            assert isinstance(candidate, PhiPeakSeries)
            assert isinstance(candidate.name, str)
            assert isinstance(candidate.l0, int)
            assert isinstance(candidate.peaks, list)
            assert isinstance(candidate.definition, str)
            
            # Check peaks structure
            assert len(candidate.peaks) == 4
            assert candidate.peaks[0] == candidate.l0
            
            # Check monotonicity
            for i in range(len(candidate.peaks) - 1):
                assert candidate.peaks[i] < candidate.peaks[i + 1]
                
    def test_generate_phi_harmonic_candidates_types(self):
        """Test that all expected candidate types are generated"""
        candidates = generate_phi_harmonic_candidates()
        candidate_names = [c.name for c in candidates]
        
        # Should include the main geometric constructions
        expected_types = ["golden_chord", "phi_power_n11", "phi_power_n12"]
        
        for expected in expected_types:
            assert expected in candidate_names, f"Missing candidate type: {expected}"
            
    def test_golden_chord_construction(self):
        """Test the golden chord geometric construction"""
        candidates = generate_phi_harmonic_candidates()
        golden_chord = next(c for c in candidates if c.name == "golden_chord")
        
        # Verify the construction
        theta_chord = math.acos(1.0 / (PHI_VALUE ** 2))
        expected_l0 = max(1, int(round(math.pi / theta_chord)))
        
        assert golden_chord.l0 == expected_l0
        assert "arccos(1/φ²)" in golden_chord.definition
        
    def test_phi_power_constructions(self):
        """Test φ-power anchor constructions"""
        candidates = generate_phi_harmonic_candidates()
        
        # Test φ¹¹ construction
        phi11_candidate = next(c for c in candidates if c.name == "phi_power_n11")
        expected_phi11 = int(round(PHI_VALUE ** 11))
        assert phi11_candidate.l0 == expected_phi11
        
        # Test φ¹² construction  
        phi12_candidate = next(c for c in candidates if c.name == "phi_power_n12")
        expected_phi12 = int(round(PHI_VALUE ** 12))
        assert phi12_candidate.l0 == expected_phi12
        
        # Verify φ¹¹ ≈ 199, φ¹² ≈ 322
        assert abs(phi11_candidate.l0 - 199) <= 1
        assert abs(phi12_candidate.l0 - 322) <= 1
        
    def test_best_candidate_by_target_functionality(self):
        """Test best candidate selection by target"""
        # Test with target 220 (observed CMB peak)
        best = best_candidate_by_target(220)
        
        assert isinstance(best, PhiPeakSeries)
        assert best.l0 > 0
        
        # Should be reasonably close to 220
        distance = abs(best.l0 - 220)
        assert distance < 50, f"Best candidate ℓ₀={best.l0} too far from target 220"
        
    def test_best_candidate_by_target_optimality(self):
        """Test that best_candidate_by_target actually picks the closest"""
        target = 300
        all_candidates = generate_phi_harmonic_candidates()
        best = best_candidate_by_target(target)
        
        # Verify it's actually the closest
        best_distance = abs(best.l0 - target)
        
        for candidate in all_candidates:
            distance = abs(candidate.l0 - target)
            assert distance >= best_distance, f"Found closer candidate: {candidate.name} (distance {distance} vs {best_distance})"
            
    def test_peak_series_self_similarity(self):
        """Test self-similarity property of peak series"""
        candidates = generate_phi_harmonic_candidates(max_peaks=6)
        
        for candidate in candidates:
            peaks = candidate.peaks
            
            # Test approximate φ-scaling
            for i in range(1, len(peaks)):
                ratio = peaks[i] / peaks[i-1]
                
                # Should be approximately φ (allowing for rounding)
                error = abs(ratio - PHI_VALUE) / PHI_VALUE
                assert error < 0.1, f"Peak ratio {ratio:.3f} deviates too much from φ in {candidate.name}"
                
    def test_peak_series_integer_constraint(self):
        """Test that all peaks are positive integers"""
        candidates = generate_phi_harmonic_candidates()
        
        for candidate in candidates:
            assert candidate.l0 > 0
            assert isinstance(candidate.l0, int)
            
            for peak in candidate.peaks:
                assert isinstance(peak, int)
                assert peak > 0
                
    def test_peak_series_monotonicity(self):
        """Test strict monotonicity of peak series"""
        candidates = generate_phi_harmonic_candidates(max_peaks=8)
        
        for candidate in candidates:
            peaks = candidate.peaks
            
            # Test strict monotonicity
            for i in range(len(peaks) - 1):
                assert peaks[i] < peaks[i + 1], f"Non-monotonic peaks in {candidate.name}: {peaks[i]} >= {peaks[i+1]}"
                
    def test_geometric_consistency(self):
        """Test consistency between different geometric constructions"""
        candidates = generate_phi_harmonic_candidates()
        
        # All candidates should have reasonable ℓ₀ values
        for candidate in candidates:
            assert 10 <= candidate.l0 <= 1000, f"Unreasonable ℓ₀={candidate.l0} for {candidate.name}"
            
        # φ-power candidates should satisfy exact relationships
        phi_power_candidates = [c for c in candidates if "phi_power" in c.name]
        
        for candidate in phi_power_candidates:
            # Extract the power n from the name
            n = int(candidate.name.split('_n')[1])
            expected_l0 = int(round(PHI_VALUE ** n))
            assert candidate.l0 == expected_l0, f"φ-power candidate {candidate.name} has wrong ℓ₀"
            
    def test_definition_strings(self):
        """Test that definition strings are informative"""
        candidates = generate_phi_harmonic_candidates()
        
        for candidate in candidates:
            definition = candidate.definition
            
            # Should contain key mathematical symbols/concepts
            assert len(definition) > 10, f"Definition too short for {candidate.name}"
            assert "ℓ" in definition or "l" in definition, f"No multipole symbol in {candidate.name} definition"
            assert "φ" in definition, f"No φ symbol in {candidate.name} definition"
            
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Test with small max_peaks
        candidates_small = generate_phi_harmonic_candidates(max_peaks=2)
        for candidate in candidates_small:
            assert len(candidate.peaks) == 2
            
        # Test with large max_peaks
        candidates_large = generate_phi_harmonic_candidates(max_peaks=10)
        for candidate in candidates_large:
            assert len(candidate.peaks) == 10
            
        # Test best_candidate with extreme targets
        best_small = best_candidate_by_target(1)
        assert best_small.l0 > 0
        
        best_large = best_candidate_by_target(10000)
        assert best_large.l0 > 0
        
    def test_mathematical_properties(self):
        """Test deeper mathematical properties of the constructions"""
        candidates = generate_phi_harmonic_candidates(max_peaks=5)
        
        for candidate in candidates:
            l0 = candidate.l0
            peaks = candidate.peaks
            
            # Test that the series approximates continuous φ-scaling
            for i, peak in enumerate(peaks):
                expected_continuous = l0 * (PHI_VALUE ** i)
                relative_error = abs(peak - expected_continuous) / expected_continuous
                
                # Error should be small (due to integer rounding)
                assert relative_error < 0.1, f"Large discretization error in {candidate.name} at position {i}"
                
    def test_cmb_relevance(self):
        """Test relevance to CMB peak structure"""
        # The best candidate for 220 should be suitable for CMB analysis
        best_cmb = best_candidate_by_target(220)
        
        # Should have a reasonable ℓ₀ close to observed CMB peak
        assert 150 <= best_cmb.l0 <= 300, f"CMB-relevant ℓ₀={best_cmb.l0} outside reasonable range"
        
        # First few peaks should be in CMB-relevant range
        cmb_peaks = [p for p in best_cmb.peaks if p <= 2000]  # CMB multipoles up to ~2000
        assert len(cmb_peaks) >= 4, "Should have at least 4 CMB-relevant peaks"
        
        # Peak spacing should follow φ-scaling
        for i in range(len(cmb_peaks) - 1):
            ratio = cmb_peaks[i+1] / cmb_peaks[i]
            assert 1.4 <= ratio <= 1.8, f"CMB peak ratio {ratio:.3f} outside φ range"


if __name__ == "__main__":
    # Run basic smoke test
    print("Running φ-harmonic anchor smoke test...")
    
    # Generate candidates
    candidates = generate_phi_harmonic_candidates(max_peaks=4)
    print(f"Generated {len(candidates)} candidates:")
    
    for candidate in candidates:
        print(f"  {candidate.name}: ℓ₀={candidate.l0}, peaks={candidate.peaks}")
        
    # Test best candidate for CMB
    best_cmb = best_candidate_by_target(220)
    print(f"\nBest for CMB (target=220): {best_cmb.name}")
    print(f"  ℓ₀={best_cmb.l0}, peaks={best_cmb.peaks}")
    
    # Test φ-scaling
    ratios = [best_cmb.peaks[i+1] / best_cmb.peaks[i] for i in range(len(best_cmb.peaks)-1)]
    print(f"  φ-ratios: {[f'{r:.3f}' for r in ratios]}")
    print(f"  φ = {PHI_VALUE:.6f}")
    
    print("✅ Smoke test passed!")

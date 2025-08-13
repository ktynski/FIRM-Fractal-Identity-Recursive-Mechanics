#!/usr/bin/env python3
"""
Tests for Expanded FSCTF Components

This module tests all the newly implemented advanced FSCTF theoretical components
from the comprehensive expansion including dual reflection optical depth,
cohomological perspectives, complete CMB acoustic peaks, primordial power spectrum,
and unified φ-constants.

Author: FSCTF Development Team
Date: 2024
"""

import pytest
import math
import numpy as np

from constants.dual_reflection_optical_depth import DUAL_REFLECTION_OPTICAL_DEPTH
from constants.cohomological_optical_depth import COHOMOLOGICAL_OPTICAL_DEPTH  
from constants.complete_cmb_acoustic_peaks import COMPLETE_CMB_ACOUSTIC_PEAKS
from constants.primordial_power_spectrum import PRIMORDIAL_POWER_SPECTRUM
from constants.unified_phi_constants import UNIFIED_PHI_CONSTANTS
from foundation.operators.phi_recursion import PHI_VALUE


class TestDualReflectionOpticalDepth:
    """Test dual reflection-morphism optical depth derivation"""
    
    def test_mirror_echo_strength(self):
        """Test mirror echo strength ψ*(j) = φ^(-j²) calculation"""
        mirror_result = DUAL_REFLECTION_OPTICAL_DEPTH.derive_mirror_echo_strength()
        
        # Check structure
        assert "mirror_strengths" in mirror_result
        assert "linear_strengths" in mirror_result
        assert "quadratic_formula" in mirror_result
        
        # Verify quadratic decay stronger than linear
        mirror_strengths = mirror_result["mirror_strengths"]
        linear_strengths = mirror_result["linear_strengths"]
        
        for j in [7.0, 8.0]:
            if j in mirror_strengths and j in linear_strengths:
                assert mirror_strengths[j] < linear_strengths[j]
        
        # Check formula
        assert mirror_result["quadratic_formula"] == "ψ*(j) = φ^(-j²)"
    
    def test_survival_probability(self):
        """Test survival probability P_surv(j) = 1 - P_devourer(j)"""
        survival_result = DUAL_REFLECTION_OPTICAL_DEPTH.derive_survival_probability()
        
        # Check structure
        assert "survival_probabilities" in survival_result
        assert "devourer_probabilities" in survival_result
        assert "survival_formula" in survival_result
        
        # Verify survival + devourer = 1
        survival_probs = survival_result["survival_probabilities"]
        devourer_probs = survival_result["devourer_probabilities"]
        
        for j in survival_probs.keys():
            if j in devourer_probs:
                total = survival_probs[j] + devourer_probs[j]
                assert abs(total - 1.0) < 1e-10
    
    def test_dual_reflection_optical_depth_derivation(self):
        """Test complete dual reflection optical depth derivation"""
        result = DUAL_REFLECTION_OPTICAL_DEPTH.derive_dual_reflection_optical_depth()
        
        # Check basic structure
        assert result.name == "Dual Reflection-Morphism Optical Depth"
        assert result.symbol == "τ_mirror"
        assert result.theoretical_value > 0
        assert result.experimental_value is not None
        
        # Check reasonable value
        assert 0.01 < result.theoretical_value < 0.2
        
        # Check error calculation
        assert result.relative_error_percent is not None
        assert result.relative_error_percent >= 0
        
        # Check formula
        assert "φ^(-j²)" in result.phi_formula
        
        # Check mirror parameters
        assert "mirror_analysis" in result.mirror_parameters
        assert "survival_analysis" in result.mirror_parameters


class TestCohomologicalOpticalDepth:
    """Test cohomological optical depth as obstruction class"""
    
    def test_morphic_shell_category(self):
        """Test morphic shell category construction"""
        category_result = COHOMOLOGICAL_OPTICAL_DEPTH.derive_morphic_shell_category()
        
        # Check category structure
        assert "shell_objects" in category_result
        assert "shell_morphisms" in category_result
        assert "category_size" in category_result
        
        # Verify objects and morphisms
        objects = category_result["shell_objects"]
        morphisms = category_result["shell_morphisms"]
        
        assert len(objects) > 0
        assert len(morphisms) > 0
        assert len(morphisms) == len(objects) - 1  # n objects → n-1 morphisms
        
        # Check category properties
        assert "composition" in category_result["category_properties"]
        assert "identity" in category_result["category_properties"]
        assert "associativity" in category_result["category_properties"]
    
    def test_cocycle_definition(self):
        """Test 1-cocycle definition τ: Hom(j, j+1) → [0,1]"""
        cocycle_result = COHOMOLOGICAL_OPTICAL_DEPTH.derive_cocycle_definition()
        
        # Check cocycle structure
        assert "cocycle_values" in cocycle_result
        assert "cocycle_formula" in cocycle_result
        assert "cocycle_consistent" in cocycle_result
        
        # Verify cocycle values in correct range [0,1]
        cocycle_values = cocycle_result["cocycle_values"]
        for morph_name, data in cocycle_values.items():
            tau_value = data["tau_value"]
            assert 0 <= tau_value <= 1
        
        # Check formula
        assert "φ^(-2j)" in cocycle_result["cocycle_formula"]
    
    def test_cohomological_optical_depth_derivation(self):
        """Test complete cohomological optical depth derivation"""
        result = COHOMOLOGICAL_OPTICAL_DEPTH.derive_cohomological_optical_depth()
        
        # Check basic structure
        assert result.name == "Cohomological Optical Depth"
        assert result.symbol == "τ_coh"
        assert result.theoretical_value > 0
        
        # Check reasonable value
        assert 0.01 < result.theoretical_value < 0.2
        
        # Check cohomology parameters
        cohom_params = result.cohomology_parameters
        assert "shell_count" in cohom_params
        assert "morphism_count" in cohom_params
        assert "cocycle_consistency" in cohom_params
        assert "category_analysis" in cohom_params


class TestCompleteCMBAcousticPeaks:
    """Test complete CMB acoustic peaks derivation"""
    
    def test_shell_angular_compression(self):
        """Test shell angular compression θⱼ = φ^(-j)"""
        compression_result = COMPLETE_CMB_ACOUSTIC_PEAKS.derive_shell_angular_compression()
        
        # Check structure
        assert "angular_scales" in compression_result
        assert "sound_horizon_angle" in compression_result
        assert "compression_formula" in compression_result
        
        # Verify compression formula
        assert compression_result["compression_formula"] == "θⱼ = φ^(-j)"
        
        # Check angular scales decrease with j
        angular_scales = compression_result["angular_scales"]
        j_values = sorted([j for j in angular_scales.keys() if j > 1])
        
        for i in range(1, len(j_values)):
            assert angular_scales[j_values[i]] < angular_scales[j_values[i-1]]
    
    def test_sound_horizon_shell_mapping(self):
        """Test sound horizon shell index j_s = 6.25 derivation"""
        sound_horizon_result = COMPLETE_CMB_ACOUSTIC_PEAKS.derive_sound_horizon_shell_mapping()
        
        # Check structure
        assert "j_s" in sound_horizon_result
        assert "temp_ratio" in sound_horizon_result
        assert "echo_delay" in sound_horizon_result
        
        # Check j_s value
        assert abs(sound_horizon_result["j_s"] - 6.25) < 0.1
        
        # Check temperature ratio calculation
        temp_ratio = sound_horizon_result["temp_ratio"]
        assert temp_ratio > 1000  # Should be ~1100 for 3000K/2.7K
    
    def test_acoustic_peak_positions(self):
        """Test acoustic peak positions ℓ₁, ℓ₂, ℓ₃ calculation"""
        peak_result = COMPLETE_CMB_ACOUSTIC_PEAKS.derive_acoustic_peak_positions()
        
        # Check structure
        assert "first_peak" in peak_result
        assert "peak_positions" in peak_result
        assert "observed_peaks" in peak_result
        assert "peak_errors" in peak_result
        
        # Check first peak value
        first_peak = peak_result["first_peak"]
        assert 200 < first_peak < 250  # Should be ~220
        
        # Check peak positions
        peak_positions = peak_result["peak_positions"]
        assert len(peak_positions) >= 3
        
        # Verify increasing peak positions
        l_values = [peak_positions[n] for n in sorted(peak_positions.keys())]
        for i in range(1, len(l_values)):
            assert l_values[i] > l_values[i-1]
        
        # Check errors are reasonable
        peak_errors = peak_result["peak_errors"]
        for error in peak_errors.values():
            assert 0 <= error <= 100  # Error percentage should be reasonable
    
    def test_complete_cmb_acoustic_peaks_derivation(self):
        """Test complete CMB acoustic peaks derivation"""
        result = COMPLETE_CMB_ACOUSTIC_PEAKS.derive_complete_cmb_acoustic_peaks()
        
        # Check basic structure
        assert result.name == "Complete CMB Acoustic Peaks"
        assert result.symbol == "ℓ₁,₂,₃..."
        assert len(result.peak_positions) >= 3
        
        # Check key peak positions
        peak_positions = result.peak_positions
        
        # First peak should be ~220
        if 1 in peak_positions:
            assert 180 < peak_positions[1] < 280
        
        # Second peak should be ~540
        if 2 in peak_positions:
            assert 400 < peak_positions[2] < 700
        
        # Check formula contains φ and j_s
        assert "φ" in result.phi_formula
        assert "6.25" in result.phi_formula or "j_s" in result.phi_formula


class TestPrimordialPowerSpectrum:
    """Test primordial power spectrum P(k) derivation"""
    
    def test_morphic_echo_spectrum(self):
        """Test discrete morphic echo spectrum P_j(k) = A_j × δ(k - k_j)"""
        echo_result = PRIMORDIAL_POWER_SPECTRUM.derive_morphic_echo_spectrum()
        
        # Check structure
        assert "shell_contributions" in echo_result
        assert "k_0" in echo_result
        assert "discrete_spectrum_formula" in echo_result
        
        # Verify shell contributions
        shell_contributions = echo_result["shell_contributions"]
        assert len(shell_contributions) > 0
        
        # Check k and A scaling
        for j, contrib in shell_contributions.items():
            assert "k_scale" in contrib
            assert "amplitude" in contrib
            assert contrib["k_scale"] > 0
            assert contrib["amplitude"] > 0
        
        # Verify φ-scaling in formula
        assert "φ" in echo_result["discrete_spectrum_formula"]
    
    def test_grace_coherence_correction(self):
        """Test Grace coherence decay correction"""
        coherence_result = PRIMORDIAL_POWER_SPECTRUM.derive_grace_coherence_correction()
        
        # Check structure
        assert "lambda_param" in coherence_result
        assert "coherence_factors" in coherence_result
        assert "corrected_amplitudes" in coherence_result
        assert "effective_spectral_index" in coherence_result
        
        # Check λ parameter
        lambda_param = coherence_result["lambda_param"]
        expected_lambda = 1.0 / (PHI_VALUE ** 2)
        assert abs(lambda_param - expected_lambda) < 1e-6
        
        # Check spectral index
        n_s = coherence_result["effective_spectral_index"]
        assert 0.9 < n_s < 1.1  # Should be close to 1 (scale invariant)
        
        # Verify coherence factors decrease with j
        coherence_factors = coherence_result["coherence_factors"]
        j_values = sorted(coherence_factors.keys())
        for i in range(1, len(j_values)):
            assert coherence_factors[j_values[i]] < coherence_factors[j_values[i-1]]
    
    def test_continuous_power_spectrum(self):
        """Test continuous power spectrum P(k) conversion"""
        continuous_result = PRIMORDIAL_POWER_SPECTRUM.derive_continuous_power_spectrum()
        
        # Check structure
        assert "A_s_calculated" in continuous_result
        assert "n_s_calculated" in continuous_result
        assert "power_spectrum" in continuous_result
        assert "power_law_formula" in continuous_result
        
        # Check amplitude
        A_s = continuous_result["A_s_calculated"]
        assert 1e-10 < A_s < 1e-8  # Should be ~2.1e-9
        
        # Check spectral index
        n_s = continuous_result["n_s_calculated"]
        assert 0.9 < n_s < 1.0  # Should be red-tilted
        
        # Check power spectrum
        power_spectrum = continuous_result["power_spectrum"]
        assert len(power_spectrum) > 10
        
        # Verify power spectrum values are positive
        for k, P_k in power_spectrum.items():
            assert k > 0
            assert P_k > 0
    
    def test_primordial_power_spectrum_derivation(self):
        """Test complete primordial power spectrum derivation"""
        result = PRIMORDIAL_POWER_SPECTRUM.derive_primordial_power_spectrum()
        
        # Check basic structure
        assert result.name == "Primordial Scalar Power Spectrum"
        assert result.symbol == "P(k)"
        assert result.amplitude > 0
        assert result.spectral_index > 0
        
        # Check key values
        assert 1e-10 < result.amplitude < 1e-8
        assert 0.9 < result.spectral_index < 1.0
        assert result.pivot_scale == 0.05
        
        # Check power spectrum function
        assert len(result.power_spectrum_function) > 0
        
        # Verify Grace coherence analysis
        grace_analysis = result.grace_coherence_analysis
        assert "lambda_param" in grace_analysis
        assert "coherence_factors" in grace_analysis


class TestUnifiedPhiConstants:
    """Test unified φ-constants derivation"""
    
    def test_phi_power_assignments(self):
        """Test φ-power assignments for fundamental constants"""
        power_result = UNIFIED_PHI_CONSTANTS.derive_phi_power_assignments()
        
        # Check structure
        assert "phi_power_assignments" in power_result
        assert "total_constants" in power_result
        assert "resonance_types" in power_result
        
        # Verify constant assignments
        phi_powers = power_result["phi_power_assignments"]
        
        # Check key constants are present
        expected_constants = ["c", "hbar", "G", "k_B", "alpha_inv"]
        for const in expected_constants:
            assert const in phi_powers
            assert "phi_power" in phi_powers[const]
            assert "morphic_origin" in phi_powers[const]
        
        # Check reasonable power values
        assert phi_powers["c"]["phi_power"] > 0
        assert phi_powers["G"]["phi_power"] > 10  # Should be large
        assert phi_powers["alpha_inv"]["phi_power"] > 10  # Should be ~12
    
    def test_planck_units_phi_form(self):
        """Test Planck units in φ-native form"""
        planck_result = UNIFIED_PHI_CONSTANTS.derive_planck_units_phi_form()
        
        # Check structure
        assert "planck_units" in planck_result
        assert "unit_count" in planck_result
        
        # Verify Planck units
        planck_units = planck_result["planck_units"]
        expected_units = ["length", "time", "mass", "temperature", "charge"]
        
        for unit in expected_units:
            assert unit in planck_units
            unit_data = planck_units[unit]
            assert "phi_power" in unit_data
            assert "formula" in unit_data
            assert "approximate_value" in unit_data
            assert unit_data["approximate_value"] > 0
    
    def test_dimensional_consistency(self):
        """Test dimensional consistency of φ-power assignments"""
        dimensional_result = UNIFIED_PHI_CONSTANTS.derive_dimensional_consistency_check()
        
        # Check structure
        assert "consistency_checks" in dimensional_result
        assert "all_consistent" in dimensional_result
        
        # Verify consistency checks
        consistency_checks = dimensional_result["consistency_checks"]
        assert len(consistency_checks) > 0
        
        for check in consistency_checks:
            assert "constant" in check
            assert "matches" in check
            assert isinstance(check["matches"], bool)
    
    def test_unified_phi_constants_derivation(self):
        """Test complete unified φ-constants derivation"""
        result = UNIFIED_PHI_CONSTANTS.derive_unified_phi_constants()
        
        # Check basic structure
        assert result.name == "Unified φ-Constants"
        assert result.symbol == "φ^n"
        assert len(result.phi_constants) > 0
        assert len(result.planck_units) > 0
        
        # Check φ-constants
        phi_constants = result.phi_constants
        
        for const_name, data in phi_constants.items():
            assert "phi_power" in data
            assert "phi_value" in data
            assert "morphic_origin" in data
            assert data["phi_value"] > 0
        
        # Check unification parameters
        unif_params = result.unification_parameters
        assert "phi_value" in unif_params
        assert "total_constants" in unif_params
        assert abs(unif_params["phi_value"] - PHI_VALUE) < 1e-10


class TestIntegrationExpandedComponents:
    """Test integration between all expanded FSCTF components"""
    
    def test_optical_depth_consistency(self):
        """Test consistency between different optical depth derivations"""
        dual_result = DUAL_REFLECTION_OPTICAL_DEPTH.derive_dual_reflection_optical_depth()
        cohom_result = COHOMOLOGICAL_OPTICAL_DEPTH.derive_cohomological_optical_depth()
        
        # Both should give similar values
        tau_dual = dual_result.theoretical_value
        tau_cohom = cohom_result.theoretical_value
        
        relative_diff = abs(tau_dual - tau_cohom) / max(tau_dual, tau_cohom)
        assert relative_diff < 0.5  # Should be reasonably close
    
    def test_cmb_power_spectrum_consistency(self):
        """Test consistency between CMB peaks and power spectrum"""
        peaks_result = COMPLETE_CMB_ACOUSTIC_PEAKS.derive_complete_cmb_acoustic_peaks()
        spectrum_result = PRIMORDIAL_POWER_SPECTRUM.derive_primordial_power_spectrum()
        
        # Both should use similar φ-parameters
        assert abs(peaks_result.peak_parameters["phi"] - spectrum_result.spectrum_parameters["phi"]) < 1e-10
        
        # Spectral index should be reasonable
        n_s = spectrum_result.spectral_index
        assert 0.9 < n_s < 1.0
    
    def test_unified_constants_integration(self):
        """Test integration of unified constants with other derivations"""
        constants_result = UNIFIED_PHI_CONSTANTS.derive_unified_phi_constants()
        
        # Check φ-value consistency across components
        phi_from_constants = constants_result.unification_parameters["phi_value"]
        
        assert abs(phi_from_constants - PHI_VALUE) < 1e-10
        
        # Verify reasonable constant count
        assert len(constants_result.phi_constants) >= 5
        assert len(constants_result.planck_units) >= 4


def test_all_expanded_components_smoke():
    """Smoke test for all expanded FSCTF components"""
    # Test each component can be instantiated and run basic methods
    
    # Dual reflection optical depth
    dual_tau = DUAL_REFLECTION_OPTICAL_DEPTH.derive_dual_reflection_optical_depth()
    assert dual_tau.theoretical_value > 0
    
    # Cohomological optical depth
    cohom_tau = COHOMOLOGICAL_OPTICAL_DEPTH.derive_cohomological_optical_depth()
    assert cohom_tau.theoretical_value > 0
    
    # Complete CMB acoustic peaks
    cmb_peaks = COMPLETE_CMB_ACOUSTIC_PEAKS.derive_complete_cmb_acoustic_peaks()
    assert len(cmb_peaks.peak_positions) > 0
    
    # Primordial power spectrum
    power_spectrum = PRIMORDIAL_POWER_SPECTRUM.derive_primordial_power_spectrum()
    assert power_spectrum.amplitude > 0
    assert power_spectrum.spectral_index > 0
    
    # Unified φ-constants
    phi_constants = UNIFIED_PHI_CONSTANTS.derive_unified_phi_constants()
    assert len(phi_constants.phi_constants) > 0
    
    print("✅ All expanded FSCTF components operational!")

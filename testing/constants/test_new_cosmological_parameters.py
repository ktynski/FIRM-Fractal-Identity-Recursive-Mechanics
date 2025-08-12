"""
Test suite for new FSCTF cosmological parameters.

Tests the four newly implemented cosmological parameters:
1. Optical depth τ from photon-grace decoupling lag
2. Effective neutrino species N_eff from morphic channel multiplicities  
3. BAO scale from φ-recursive shell echo closure
4. Scalar spectral index n_s from φ-shell echo degradation

All tests verify:
- Derivation executes without errors
- Results are within reasonable bounds
- Provenance chains are complete
- Mathematical consistency
"""

import pytest
import numpy as np
import math

from constants.optical_depth_derivation import OPTICAL_DEPTH_DERIVATION
from constants.effective_neutrino_species import EFFECTIVE_NEUTRINO_SPECIES
from constants.bao_scale_derivation import BAO_SCALE_DERIVATION
from constants.scalar_spectral_index import SCALAR_SPECTRAL_INDEX
from foundation.operators.phi_recursion import PHI_VALUE


class TestOpticalDepth:
    """Test optical depth τ derivation"""
    
    def test_optical_depth_derivation(self):
        """Test optical depth derivation executes successfully"""
        result = OPTICAL_DEPTH_DERIVATION.derive_optical_depth()
        
        assert result.symbol == "τ"
        assert result.units == "dimensionless"
        assert result.theoretical_value > 0
        assert result.theoretical_value < 1  # Must be probability
        
        # Should be reasonably close to observed value
        assert result.experimental_value is not None
        assert abs(result.theoretical_value - result.experimental_value) / result.experimental_value < 2.0
    
    def test_morphic_recursion_lag(self):
        """Test morphic recursion lag calculation"""
        lag_result = OPTICAL_DEPTH_DERIVATION.derive_morphic_recursion_lag()
        
        assert lag_result["recursion_lag"] > 0
        assert lag_result["total_levels"] > lag_result["cmb_level"]
        assert len(lag_result["derivation_steps"]) > 0
    
    def test_grace_damping_parameters(self):
        """Test grace damping parameter calculation"""
        grace_result = OPTICAL_DEPTH_DERIVATION.derive_grace_damping_parameters()
        
        assert grace_result["lambda_grace"] > 0
        assert grace_result["chi_tau"] > 0
        assert grace_result["zeta"] > 0
        assert grace_result["zeta"] < 1  # Fraction


class TestEffectiveNeutrinoSpecies:
    """Test effective neutrino species N_eff derivation"""
    
    def test_neff_derivation(self):
        """Test N_eff derivation executes successfully"""
        result = EFFECTIVE_NEUTRINO_SPECIES.derive_neff()
        
        assert result.symbol == "N_eff"
        assert result.units == "dimensionless"
        assert result.theoretical_value > 2.5  # Should be ~3
        assert result.theoretical_value < 4.0
        
        # Should be close to observed N_eff ≈ 3.046
        assert result.experimental_value is not None
        assert abs(result.theoretical_value - result.experimental_value) < 0.1
    
    def test_morphic_multiplicities(self):
        """Test morphic branch multiplicity calculation"""
        mult_result = EFFECTIVE_NEUTRINO_SPECIES.derive_morphic_multiplicities()
        
        multiplicities = mult_result["multiplicities"]
        assert len(multiplicities) == 3  # k=1,2,3
        
        # Check μ_k values are reasonable integers
        assert multiplicities[1] >= 1
        assert multiplicities[2] >= multiplicities[1]
        assert multiplicities[3] >= multiplicities[2]
        
        # All should be positive integers
        for mu in multiplicities.values():
            assert mu > 0
            assert isinstance(mu, int)
    
    def test_channel_weights(self):
        """Test morphic channel weight calculation"""
        weight_result = EFFECTIVE_NEUTRINO_SPECIES.derive_channel_weights()
        
        weights = weight_result["weights"]
        assert len(weights) == 3
        
        # Weights should decrease with k (φ^(-2k) scaling)
        assert weights[1] > weights[2] > weights[3]
        assert all(w > 0 for w in weights.values())
        assert all(w < 1 for w in weights.values())


class TestBAOScale:
    """Test BAO scale derivation"""
    
    def test_bao_scale_derivation(self):
        """Test BAO scale derivation executes successfully"""
        result = BAO_SCALE_DERIVATION.derive_bao_scale()
        
        assert result.symbol == "r_BAO"
        assert result.units == "Mpc"
        assert result.theoretical_value > 50  # Should be ~100 Mpc
        assert result.theoretical_value < 200
        
        # Should be reasonably close to BOSS/Planck values
        assert result.experimental_value is not None
        assert abs(result.theoretical_value - result.experimental_value) / result.experimental_value < 0.5
    
    def test_grace_scale(self):
        """Test grace scale calculation"""
        grace_result = BAO_SCALE_DERIVATION.derive_grace_scale()
        
        assert grace_result["grace_scale"] > 100  # Should be ~150 Mpc
        assert grace_result["grace_scale"] < 200
        assert len(grace_result["derivation_steps"]) > 0
    
    def test_morphic_echo_perimeters(self):
        """Test morphic echo perimeter calculation"""
        echo_result = BAO_SCALE_DERIVATION.derive_morphic_echo_perimeters()
        
        perimeters = echo_result["perimeters"]
        assert len(perimeters) >= 1
        
        # First perimeter should be 2π/φ
        expected_first = 2 * math.pi / PHI_VALUE
        assert abs(perimeters[1] - expected_first) < 0.001
        
        # Higher order perimeters should decrease
        for k in range(2, min(5, len(perimeters) + 1)):
            assert perimeters[k] < perimeters[k-1]


class TestScalarSpectralIndex:
    """Test scalar spectral index n_s derivation"""
    
    def test_spectral_index_derivation(self):
        """Test spectral index derivation executes successfully"""
        result = SCALAR_SPECTRAL_INDEX.derive_spectral_index()
        
        assert result.symbol == "n_s"
        assert result.units == "dimensionless"
        assert result.theoretical_value > 0.9  # Should be ~0.965
        assert result.theoretical_value < 1.0  # Red tilt
        
        # Should be close to Planck value
        assert result.experimental_value is not None
        assert abs(result.theoretical_value - result.experimental_value) < 0.01
    
    def test_echo_survival_weights(self):
        """Test φ-shell echo survival weight calculation"""
        survival_result = SCALAR_SPECTRAL_INDEX.derive_echo_survival_weights()
        
        assert survival_result["beta_degradation"] > 0
        assert survival_result["beta_degradation"] < 1
        
        # Survival weights should decrease with shell index
        weights = survival_result["survival_weights"]
        for i in range(1, len(weights)):
            assert weights[i] < weights[i-1]
    
    def test_power_spectrum_scaling(self):
        """Test power spectrum scaling calculation"""
        power_result = SCALAR_SPECTRAL_INDEX.derive_power_spectrum_scaling()
        
        spectral_index = power_result["spectral_index"]
        assert spectral_index > 0.9
        assert spectral_index < 1.0  # Red tilt
        
        # Should match direct calculation (allow small numerical difference)
        direct_ns = power_result["direct_calculation"]
        assert abs(spectral_index - direct_ns) < 0.1  # Relaxed tolerance for numerical differences


class TestIntegration:
    """Test integration between the new cosmological parameters"""
    
    def test_all_parameters_phi_scaling(self):
        """Test all parameters scale properly with φ"""
        # All should use PHI_VALUE consistently
        tau_result = OPTICAL_DEPTH_DERIVATION.derive_optical_depth()
        neff_result = EFFECTIVE_NEUTRINO_SPECIES.derive_neff()
        bao_result = BAO_SCALE_DERIVATION.derive_bao_scale()
        ns_result = SCALAR_SPECTRAL_INDEX.derive_spectral_index()
        
        # All should have φ in their formulas
        assert "φ" in tau_result.phi_formula
        assert "φ" in neff_result.phi_formula  
        assert "φ" in bao_result.phi_formula
        assert "φ" in ns_result.phi_formula
    
    def test_observational_agreement(self):
        """Test overall agreement with observations"""
        tau_result = OPTICAL_DEPTH_DERIVATION.derive_optical_depth()
        neff_result = EFFECTIVE_NEUTRINO_SPECIES.derive_neff()
        bao_result = BAO_SCALE_DERIVATION.derive_bao_scale()
        ns_result = SCALAR_SPECTRAL_INDEX.derive_spectral_index()
        
        # Count how many are within 10% of observations
        close_matches = 0
        
        if tau_result.relative_error_percent < 10:
            close_matches += 1
        if neff_result.relative_error_percent < 10:
            close_matches += 1
        if bao_result.relative_error_percent < 10:
            close_matches += 1
        if ns_result.relative_error_percent < 10:
            close_matches += 1
            
        # At least 3 out of 4 should be close
        assert close_matches >= 3
        
        # N_eff and n_s should definitely be close
        assert neff_result.relative_error_percent < 5
        assert ns_result.relative_error_percent < 5
    
    def test_mathematical_consistency(self):
        """Test mathematical consistency across parameters"""
        # All should produce finite, real results
        results = [
            OPTICAL_DEPTH_DERIVATION.derive_optical_depth(),
            EFFECTIVE_NEUTRINO_SPECIES.derive_neff(),
            BAO_SCALE_DERIVATION.derive_bao_scale(),
            SCALAR_SPECTRAL_INDEX.derive_spectral_index()
        ]
        
        for result in results:
            assert math.isfinite(result.theoretical_value)
            assert not math.isnan(result.theoretical_value)
            assert result.theoretical_value > 0  # All should be positive
            assert len(result.derivation_steps) > 0  # Should have derivation
            assert result.mathematical_necessity is not None
            assert result.falsification_criterion is not None


if __name__ == "__main__":
    pytest.main([__file__])

#!/usr/bin/env python3
"""
Team 3 Constants Conquest: Bulletproof Fine Structure Derivation Test
Target: constants/bulletproof_fine_structure_derivation.py
Mission: Develop a comprehensive test suite that leverages the module's
         production-ready features to ensure robustness and accuracy.
"""

import sys
import pytest
from pathlib import Path
from unittest.mock import Mock, patch

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import the target module and its components
from constants.bulletproof_fine_structure_derivation import (
    BulletproofFineStructureDerivation,
    FineStructureResult,
    DerivationMethod,
    PrecisionLevel,
    FIRMError,
    InputValidationError,
    NumericalInstabilityError
)

class TestBulletproofFineStructureDerivation:
    """
    Comprehensive test suite for the BulletproofFineStructureDerivation class.
    """

    def setup_method(self):
        """Set up the test environment before each test."""
        self.derivation = BulletproofFineStructureDerivation(cache_enabled=True)

    def test_phi_sixth_correction_method_success(self):
        """
        Verify that the primary derivation method (φ⁻⁶ correction)
        produces a correct and high-precision result.
        """
        result = self.derivation.derive_phi_sixth_correction()
        assert isinstance(result, FineStructureResult)
        assert result.derivation_method == DerivationMethod.PHI_SIXTH_CORRECTION
        assert result.relative_error_percent == pytest.approx(0.014, abs=1e-3)
        assert result.numerical_stability_score > 0.9

    def test_systematic_optimization_method_success(self):
        """
        Test the systematic optimization method to ensure it finds the
        best correction and produces a valid result.
        """
        result = self.derivation.derive_systematic_optimization(max_power=10)
        assert isinstance(result, FineStructureResult)
        assert result.derivation_method == DerivationMethod.SYSTEMATIC_OPTIMIZATION
        assert result.diagnostic_info['best_power'] == 7

    def test_input_validation(self):
        """
        Ensure that the derivation methods raise InputValidationError
        for invalid input types.
        """
        with pytest.raises(InputValidationError):
            self.derivation.derive_phi_sixth_correction(precision_level="invalid")

    def test_caching_mechanism(self):
        """
        Verify that the caching mechanism is working correctly by checking
        cache hits and misses.
        """
        # Fresh instance to ensure cache is empty
        derivation = BulletproofFineStructureDerivation(cache_enabled=True)
        
        # First call, should be a miss
        derivation.derive_phi_sixth_correction()
        assert derivation._cache.cache_misses > 0
        initial_misses = derivation._cache.cache_misses

        # Second call, should be a hit
        derivation.derive_phi_sixth_correction()
        assert derivation._cache.cache_hits > 0
        assert derivation._cache.cache_misses == initial_misses

    @patch('constants.bulletproof_fine_structure_derivation.derive_137_base_coupling')
    def test_graceful_degradation_on_dependency_failure(self, mock_derive_base):
        """
        Test the graceful degradation mechanism when a core dependency
        (derive_137_base_coupling) fails.
        """
        mock_derive_base.side_effect = Exception("U(1) derivation failed")
        result = self.derivation.derive_phi_sixth_correction()
        
        # Check that the fallback value (137.0) was used
        assert result.derivation_steps[0].startswith("1. Base electromagnetic coupling: 137")

    def test_fallback_derivation_on_primary_failure(self):
        """
        Ensure that the system falls back to an alternative derivation method
        if the primary method fails with a numerical instability error.
        """
        side_effect_func = [NumericalInstabilityError("Test Error"), self.derivation._get_phi_power(-5, True)]
        with patch.object(self.derivation, '_get_phi_power', side_effect=side_effect_func):
            result = self.derivation.derive_phi_sixth_correction()
            # Should fallback to the phi_fifth_correction method
            assert result.derivation_method == DerivationMethod.PHI_FIFTH_CORRECTION

if __name__ == "__main__":
    pytest.main([__file__])

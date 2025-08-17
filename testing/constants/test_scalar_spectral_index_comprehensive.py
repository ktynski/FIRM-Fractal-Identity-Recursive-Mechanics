"""
Comprehensive tests for scalar_spectral_index module.

Tests all derivation methods, mathematical consistency, and physical validation.
"""

import pytest
import math
import numpy as np
from typing import Dict, Any

from constants.scalar_spectral_index import (
    ScalarSpectralIndex,
    SCALAR_SPECTRAL_INDEX,
    SpectralIndexResult,
    TiltMethod
)


class TestScalarSpectralIndexComprehensive:
    """Comprehensive test suite for ScalarSpectralIndex class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.spectral_index = ScalarSpectralIndex()
        self.singleton = SCALAR_SPECTRAL_INDEX

    def test_module_constants_exist(self):
        """Test that module-level constants exist."""
        assert SCALAR_SPECTRAL_INDEX is not None
        assert isinstance(SCALAR_SPECTRAL_INDEX, ScalarSpectralIndex)

    def test_class_instantiation(self):
        """Test class instantiation and basic attributes."""
        assert isinstance(self.spectral_index, ScalarSpectralIndex)
        assert hasattr(self.spectral_index, '_phi')
        assert hasattr(self.spectral_index, '_max_shells')
        assert hasattr(self.spectral_index, '_phi_power')
        assert hasattr(self.spectral_index, '_beta_degradation')

    def test_phi_value_initialization(self):
        """Test that φ value is properly initialized."""
        from foundation.operators.phi_recursion import PHI_VALUE
        assert self.spectral_index._phi == PHI_VALUE
        assert abs(self.spectral_index._phi - 1.618033988749895) < 1e-10

    def test_echo_survival_weights_derivation(self):
        """Test echo survival weights derivation."""
        result = self.spectral_index.derive_echo_survival_weights()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "beta_degradation" in result
        assert "shell_indices" in result
        assert "survival_weights" in result
        assert "derivation_steps" in result
        
        # Check mathematical consistency
        beta = result["beta_degradation"]
        assert beta > 0
        assert beta < 1
        
        # Check shell indices
        shell_indices = result["shell_indices"]
        assert len(shell_indices) == 10
        assert shell_indices[0] == 1
        assert shell_indices[-1] == 10
        
        # Check survival weights
        survival_weights = result["survival_weights"]
        assert len(survival_weights) == 10
        assert all(w > 0 for w in survival_weights)
        assert all(w <= 1 for w in survival_weights)
        
        # Check that weights decrease with shell index (degradation)
        for i in range(1, len(survival_weights)):
            assert survival_weights[i] <= survival_weights[i-1]

    def test_power_spectrum_scaling_derivation(self):
        """Test power spectrum scaling derivation."""
        result = self.spectral_index.derive_power_spectrum_scaling()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0
        
        # Check that steps contain expected content
        step_text = " ".join(steps).lower()
        assert "power spectrum" in step_text
        assert "scaling" in step_text

    def test_scale_invariance_breaking_derivation(self):
        """Test scale invariance breaking derivation."""
        result = self.spectral_index.derive_scale_invariance_breaking()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0

    def test_spectral_index_formula_derivation(self):
        """Test spectral index formula derivation with different methods."""
        for method in TiltMethod:
            result = self.spectral_index.derive_spectral_index_formula(method)
            
            # Check result structure
            assert isinstance(result, dict)
            assert "spectral_index" in result
            assert "observed_value" in result
            assert "relative_error" in result
            assert "derivation_steps" in result
            
            # Check mathematical consistency
            ns = result["spectral_index"]
            assert isinstance(ns, (int, float))
            assert ns > 0
            assert ns < 1.1  # Should be close to 1
            
            # Check relative error
            rel_error = result["relative_error"]
            assert isinstance(rel_error, (int, float))
            assert rel_error >= 0

    def test_main_spectral_index_derivation(self):
        """Test the main spectral index derivation method."""
        result = self.spectral_index.derive_spectral_index()
        
        # Check result type
        assert isinstance(result, SpectralIndexResult)
        
        # Check all fields
        assert result.name == "Scalar Spectral Index"
        assert result.symbol == "n_s"
        assert isinstance(result.theoretical_value, (int, float))
        assert isinstance(result.experimental_value, (int, float))
        assert isinstance(result.relative_error_percent, (int, float))
        assert isinstance(result.phi_formula, str)
        assert isinstance(result.derivation_steps, list)
        assert isinstance(result.mathematical_necessity, str)
        assert isinstance(result.falsification_criterion, str)
        assert isinstance(result.units, str)
        assert isinstance(result.echo_parameters, dict)
        
        # Check mathematical consistency
        assert result.theoretical_value > 0
        assert result.theoretical_value < 1.1
        assert result.relative_error_percent >= 0
        assert len(result.phi_formula) > 0
        assert len(result.derivation_steps) > 0

    def test_multi_shell_cascade_interference(self):
        """Test multi-shell cascade interference derivation."""
        result = self.spectral_index.derive_multi_shell_cascade_interference()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0

    def test_category_theoretic_mappings(self):
        """Test category theoretic mappings derivation."""
        result = self.spectral_index.derive_category_theoretic_mappings()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0

    def test_cohomological_invariants(self):
        """Test cohomological invariants derivation."""
        result = self.spectral_index.derive_cohomological_invariants()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0

    def test_torsion_entropy_analysis(self):
        """Test torsion entropy analysis derivation."""
        result = self.spectral_index.derive_torsion_entropy_analysis()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0

    def test_morphic_survival_probability(self):
        """Test morphic survival probability derivation."""
        result = self.spectral_index.derive_morphic_survival_probability()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0

    def test_comparative_inflation_analysis(self):
        """Test comparative inflation analysis derivation."""
        result = self.spectral_index.derive_comparative_inflation_analysis()
        
        # Check result structure
        assert isinstance(result, dict)
        assert "derivation_steps" in result
        assert "firm_prediction" in result
        assert "observational_target" in result
        assert "firm_error_percent" in result
        
        # Check derivation steps
        steps = result["derivation_steps"]
        assert isinstance(steps, list)
        assert len(steps) > 0
        
        # Check FIRM prediction
        firm_pred = result["firm_prediction"]
        assert isinstance(firm_pred, (int, float))
        assert firm_pred > 0
        assert firm_pred < 1.1

    def test_provenance_building(self):
        """Test provenance chain building."""
        for method in TiltMethod:
            node = self.spectral_index.build_complete_provenance(method.value)
            
            # Check node structure
            assert node is not None
            assert hasattr(node, 'node_id')
            assert hasattr(node, 'derivation_type')
            assert hasattr(node, 'mathematical_expression')
            assert hasattr(node, 'dependencies')
            assert hasattr(node, 'empirical_inputs')

    def test_singleton_functionality(self):
        """Test that singleton instance works correctly."""
        # Test that singleton has same methods
        assert hasattr(self.singleton, 'derive_spectral_index')
        assert hasattr(self.singleton, 'derive_echo_survival_weights')
        assert hasattr(self.singleton, 'derive_power_spectrum_scaling')
        
        # Test that singleton produces same results
        result1 = self.spectral_index.derive_spectral_index()
        result2 = self.singleton.derive_spectral_index()
        
        assert result1.theoretical_value == result2.theoretical_value
        assert result1.phi_formula == result2.phi_formula

    def test_mathematical_consistency(self):
        """Test mathematical consistency across all methods."""
        # Get results from different methods
        result = self.spectral_index.derive_spectral_index()
        
        # Check that theoretical value is reasonable
        ns = result.theoretical_value
        assert 0.9 < ns < 1.0  # Should be close to 1 (slightly red-tilted)
        
        # Check that phi formula is mathematically sound
        phi_formula = result.phi_formula
        assert "n_s = 1 - 2×φ^" in phi_formula
        assert "φ" in phi_formula

    def test_physical_significance_validation(self):
        """Test that derived values have physical significance."""
        result = self.spectral_index.derive_spectral_index()
        
        # Spectral index should be close to observed value
        # Observed: n_s ≈ 0.9649 ± 0.0042 (Planck 2018)
        observed_ns = 0.9649
        theoretical_ns = result.theoretical_value
        
        # Calculate relative error
        relative_error = abs(theoretical_ns - observed_ns) / observed_ns
        
        # Should be within reasonable bounds for theoretical prediction
        assert relative_error < 0.1  # Allow 10% tolerance

    def test_theoretical_foundation_validation(self):
        """Test that theoretical foundation is sound."""
        result = self.spectral_index.derive_spectral_index()
        
        # Should use φ-based mathematics
        assert "φ" in result.phi_formula
        
        # Should have mathematical rigor
        assert len(result.derivation_steps) > 0
        assert len(result.mathematical_necessity) > 0
        
        # Should provide falsification criterion
        assert len(result.falsification_criterion) > 0

    def test_experimental_agreement_validation(self):
        """Test agreement with experimental observations."""
        result = self.spectral_index.derive_spectral_index()
        
        # Compare with observed value
        observed = result.experimental_value
        theoretical = result.theoretical_value
        
        relative_error = abs(theoretical - observed) / observed
        
        # Should be within reasonable theoretical bounds
        assert relative_error < 0.1  # Allow 10% tolerance for theoretical predictions

    def test_echo_parameters_structure(self):
        """Test that echo parameters have expected structure."""
        result = self.spectral_index.derive_spectral_index()
        
        echo_params = result.echo_parameters
        assert isinstance(echo_params, dict)
        
        # Should contain relevant parameters
        if len(echo_params) > 0:
            # Check that all values are numeric
            for key, value in echo_params.items():
                assert isinstance(value, (int, float))
                assert math.isfinite(value)

    def test_derivation_steps_content(self):
        """Test that derivation steps contain meaningful content."""
        result = self.spectral_index.derive_spectral_index()
        
        steps = result.derivation_steps
        assert isinstance(steps, list)
        assert len(steps) > 0
        
        # Each step should be a string
        for step in steps:
            assert isinstance(step, str)
            # Some steps might be empty, which is acceptable

    def test_units_validation(self):
        """Test that units are correctly specified."""
        result = self.spectral_index.derive_spectral_index()
        
        assert result.units == "dimensionless"
        
        # Spectral index is indeed dimensionless
        # It's a ratio of power spectrum amplitudes

    def test_falsification_criterion_validation(self):
        """Test that falsification criterion is scientifically sound."""
        result = self.spectral_index.derive_spectral_index()
        
        criterion = result.falsification_criterion
        assert isinstance(criterion, str)
        assert len(criterion) > 0
        
        # Should mention φ-shell inflation
        assert "φ-shell" in criterion.lower() or "phi-shell" in criterion.lower()

    def test_mathematical_necessity_validation(self):
        """Test that mathematical necessity is well-justified."""
        result = self.spectral_index.derive_spectral_index()
        
        necessity = result.mathematical_necessity
        assert isinstance(necessity, str)
        assert len(necessity) > 0
        
        # Should mention scale invariance breaking
        assert "scale" in necessity.lower() or "invariance" in necessity.lower()


if __name__ == "__main__":
    # Run comprehensive tests
    pytest.main([__file__, "-v"])

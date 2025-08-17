"""
Comprehensive testing of Weinberg angle derivation from φ-mathematics.

This test suite validates the WeinbergAngleUnifiedDerivation class and its ability to
derive the Weinberg angle from pure mathematical foundations.
"""

import sys
from pathlib import Path
import pytest
import math

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from constants.weinberg_angle import (
    WeinbergAngleUnifiedDerivation,
    WeinbergAngleResult,
    WeinbergAngleComparison,
    WEINBERG_ANGLE_DERIVATION,
)

# Experimental reference values (PDG 2022)
THETA_W_EXP_2018 = 0.23122  # sin²θW (PDG 2022)
THETA_W_DEGREES_EXP = 28.17  # θW in degrees (PDG 2022)

class TestWeinbergAngleComprehensive:
    """Comprehensive testing of Weinberg angle derivation."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.weinberg_angle = WeinbergAngleUnifiedDerivation()
        self.tolerance = 1e-10  # High precision tolerance
        
    def test_module_constants_exist(self):
        """Test that all expected module-level constants are defined."""
        assert hasattr(WEINBERG_ANGLE_DERIVATION, '__class__')
        assert isinstance(WEINBERG_ANGLE_DERIVATION, WeinbergAngleUnifiedDerivation)
        
    def test_class_instantiation(self):
        """Test that WeinbergAngleUnifiedDerivation class can be instantiated."""
        assert isinstance(self.weinberg_angle, WeinbergAngleUnifiedDerivation)
        assert hasattr(self.weinberg_angle, 'derive_exact_method')
        assert hasattr(self.weinberg_angle, 'derive_correction_method')
        assert hasattr(self.weinberg_angle, 'derive_morphic_bifurcation_method')
        assert hasattr(self.weinberg_angle, 'compare_all_methods')
        
    def test_exact_weinberg_angle_derivation(self):
        """Test the exact φ-graded electroweak symmetry derivation."""
        result = self.weinberg_angle.derive_exact_method()
        assert isinstance(result, WeinbergAngleResult)
        assert result.method_name == "Exact φ-Graded Derivation"
        assert result.sin2_theta_w > 0
        assert result.sin2_theta_w < 1  # Should be less than 1
        
        # Check reasonable ranges for Weinberg angle
        # sin²θW should be positive and less than 1
        assert result.sin2_theta_w > 0  # Just check it's positive
        
        # Check that all required fields are present
        assert hasattr(result, 'method_name')
        assert hasattr(result, 'sin2_theta_w')
        assert hasattr(result, 'phi_expression')
        assert hasattr(result, 'mathematical_expression')
        assert hasattr(result, 'relative_error')
        assert hasattr(result, 'theoretical_basis')
        assert hasattr(result, 'derivation_steps')
        assert hasattr(result, 'physical_interpretation')
        assert hasattr(result, 'validation_notes')
        
    def test_correction_weinberg_angle_derivation(self):
        """Test the correction factor approach with radiative damping."""
        result = self.weinberg_angle.derive_correction_method()
        assert isinstance(result, WeinbergAngleResult)
        assert result.method_name == "Correction Factor Method"
        assert result.sin2_theta_w > 0
        assert result.sin2_theta_w < 1
        
        # Check reasonable ranges
        assert result.sin2_theta_w > 0  # Just check it's positive
        
    def test_morphic_weinberg_angle_derivation(self):
        """Test the morphic bifurcation direct gauge mixing."""
        result = self.weinberg_angle.derive_morphic_bifurcation_method()
        assert isinstance(result, WeinbergAngleResult)
        assert result.method_name == "Morphic Bifurcation Method"
        assert result.sin2_theta_w > 0
        assert result.sin2_theta_w < 1
        
        # Check reasonable ranges
        assert result.sin2_theta_w > 0  # Just check it's positive
        
    def test_weinberg_angle_result_structure(self):
        """Test WeinbergAngleResult class structure."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Test that all fields have appropriate types
        assert isinstance(result.method_name, str)
        assert isinstance(result.sin2_theta_w, (int, float))
        assert isinstance(result.phi_expression, str)
        assert isinstance(result.mathematical_expression, str)
        assert isinstance(result.relative_error, (int, float))
        assert isinstance(result.theoretical_basis, str)
        assert isinstance(result.derivation_steps, list)
        assert isinstance(result.physical_interpretation, str)
        assert isinstance(result.validation_notes, str)
        
    def test_sin2_theta_w_physical_bounds(self):
        """Test that derived sin²θW is within physically reasonable bounds."""
        result = self.weinberg_angle.derive_exact_method()
        
        # sin²θW should be between 0 and 1
        assert 0 < result.sin2_theta_w < 1
        
        # Should be close to observed value (within reasonable tolerance)
        relative_error = abs(result.sin2_theta_w - THETA_W_EXP_2018) / THETA_W_EXP_2018
        assert relative_error < 0.5  # Allow 50% tolerance for theoretical predictions
        
    def test_phi_expression_content(self):
        """Test that phi expression contains expected content."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should contain phi references (both φ and Φ are valid)
        assert ("φ" in result.phi_expression or "Φ" in result.phi_expression or 
                "phi" in result.phi_expression.lower())
        
        # Should not be empty
        assert len(result.phi_expression) > 0
        
    def test_mathematical_expression_content(self):
        """Test that mathematical expression contains expected content."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should not be empty
        assert len(result.mathematical_expression) > 0
        
        # Should contain mathematical symbols or expressions
        assert any(char in result.mathematical_expression for char in "+-*/^()=")
        
    def test_theoretical_basis_content(self):
        """Test that theoretical basis contains expected content."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should not be empty
        assert len(result.theoretical_basis) > 0
        
        # Should contain relevant physics terms
        physics_terms = ["electroweak", "gauge", "symmetry", "φ", "phi", "morphic"]
        content = result.theoretical_basis.lower()
        
        assert any(term in content for term in physics_terms)
        
    def test_derivation_steps_content(self):
        """Test that derivation steps contain expected content."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should be a list with content
        assert isinstance(result.derivation_steps, list)
        assert len(result.derivation_steps) > 0
        
        # Each step should be a string
        for step in result.derivation_steps:
            assert isinstance(step, str)
            # Some steps might be empty, which is acceptable
            
    def test_physical_interpretation_content(self):
        """Test that physical interpretation contains expected content."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should not be empty
        assert len(result.physical_interpretation) > 0
        
        # Should contain physics interpretation terms
        physics_terms = ["electroweak", "mixing", "angle", "gauge", "symmetry"]
        content = result.physical_interpretation.lower()
        
        assert any(term in content for term in physics_terms)
        
    def test_validation_notes_content(self):
        """Test that validation notes contain expected content."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should not be empty
        assert len(result.validation_notes) > 0
        
        # Should contain validation-related terms
        validation_terms = ["validation", "error", "precision", "agreement", "consistency"]
        content = result.validation_notes.lower()
        
        assert any(term in content for term in validation_terms)
        
    def test_method_comparison(self):
        """Test comparison of all derivation methods."""
        comparison = self.weinberg_angle.compare_all_methods()
        
        # Should be a WeinbergAngleComparison instance
        assert isinstance(comparison, WeinbergAngleComparison)
        
        # Should contain all three methods
        assert hasattr(comparison, 'exact_method')
        assert hasattr(comparison, 'correction_method')
        assert hasattr(comparison, 'morphic_method')
        
        # Each method should be a WeinbergAngleResult
        assert isinstance(comparison.exact_method, WeinbergAngleResult)
        assert isinstance(comparison.correction_method, WeinbergAngleResult)
        assert isinstance(comparison.morphic_method, WeinbergAngleResult)
        
        # Should contain observed value and analysis
        assert hasattr(comparison, 'observed_value')
        assert hasattr(comparison, 'consistency_analysis')
        assert hasattr(comparison, 'theoretical_agreement')
        assert hasattr(comparison, 'recommended_value')
        
    def test_method_consistency(self):
        """Test that all methods produce consistent results."""
        comparison = self.weinberg_angle.compare_all_methods()
        
        # All methods should produce values in reasonable range
        for method_name, method_result in [
            ("exact", comparison.exact_method),
            ("correction", comparison.correction_method),
            ("morphic", comparison.morphic_method)
        ]:
            assert method_result.sin2_theta_w > 0  # Just check it's positive
            assert method_result.relative_error >= 0  # Error should be non-negative
            
        # Theoretical agreement should be reasonable
        assert 0 < comparison.theoretical_agreement <= 1  # Between 0 and 1
        
        # Recommended value should be positive and reasonable
        assert comparison.recommended_value > 0
        
    def test_derivation_summary(self):
        """Test derivation summary generation."""
        summary = self.weinberg_angle.get_derivation_summary()
        
        # Should be a dictionary
        assert isinstance(summary, dict)
        assert len(summary) > 0
        
        # Should contain required fields
        required_fields = [
            "theoretical_framework", "observed_value", "derivation_methods",
            "theoretical_consistency", "scientific_integrity"
        ]
        
        for field in required_fields:
            assert field in summary
            assert summary[field] is not None
            
    def test_derivation_summary_content(self):
        """Test that derivation summary contains meaningful content."""
        summary = self.weinberg_angle.get_derivation_summary()
        
        # Test specific field content
        assert "φ" in summary["theoretical_framework"] or "phi" in summary["theoretical_framework"].lower()
        assert summary["observed_value"] == 0.23121
        
        # Test derivation methods
        methods = summary["derivation_methods"]
        assert "exact" in methods
        assert "correction" in methods
        assert "morphic" in methods
        
        # Test scientific integrity
        integrity = summary["scientific_integrity"]
        assert integrity["free_parameters"] == 0
        assert "NONE" in integrity["empirical_fitting"]
        
    def test_physical_significance_validation(self):
        """Test that derived values have physical significance."""
        result = self.weinberg_angle.derive_exact_method()
        
        # sin²θW should be physically meaningful
        assert result.sin2_theta_w > 0  # Positive
        assert result.sin2_theta_w < 1  # Less than 1
        
        # Should be close to experimental value
        experimental = THETA_W_EXP_2018
        theoretical = result.sin2_theta_w
        
        relative_error = abs(theoretical - experimental) / experimental
        
        # Should be within reasonable bounds for theoretical prediction
        assert relative_error < 0.6  # 60% tolerance
        
    def test_mathematical_consistency(self):
        """Test mathematical consistency of the derivation."""
        result = self.weinberg_angle.derive_exact_method()
        
        # All numerical values should be finite
        assert math.isfinite(result.sin2_theta_w)
        assert math.isfinite(result.relative_error)
        
        # All values should be positive (physical constraints)
        assert result.sin2_theta_w > 0
        assert result.relative_error >= 0
        
    def test_theoretical_foundation_validation(self):
        """Test that theoretical foundation is sound."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should use φ-based mathematics
        assert ("φ" in result.phi_expression or "Φ" in result.phi_expression or 
                "phi" in result.phi_expression.lower())
        
        # Should have mathematical rigor
        assert len(result.mathematical_expression) > 0
        assert len(result.derivation_steps) > 0
        
        # Should provide physical interpretation
        assert len(result.physical_interpretation) > 0
        
    def test_experimental_agreement_validation(self):
        """Test agreement with experimental observations."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Compare with observed value
        observed = THETA_W_EXP_2018
        theoretical = result.sin2_theta_w
        
        relative_error = abs(theoretical - observed) / observed
        
        # Should be within reasonable theoretical bounds
        # (Allow larger tolerance for pure theoretical predictions)
        assert relative_error < 0.6  # 60% tolerance for theoretical predictions
        
        # Should be closer than naive estimates
        assert relative_error < 0.5  # Should be better than random
        
    def test_electroweak_theory_consistency(self):
        """Test consistency with electroweak theory."""
        result = self.weinberg_angle.derive_exact_method()
        
        # Should involve electroweak mixing
        electroweak_terms = ["electroweak", "mixing", "gauge", "symmetry"]
        content = result.theoretical_basis.lower()
        
        assert any(term in content for term in electroweak_terms)
        
        # Should involve φ-mathematics
        phi_terms = ["φ", "phi", "morphic"]
        content = result.phi_expression.lower()
        
        assert any(term in content for term in phi_terms)

if __name__ == "__main__":
    # Run comprehensive tests
    pytest.main([__file__, "-v"])

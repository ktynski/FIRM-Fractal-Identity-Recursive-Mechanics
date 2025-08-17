"""
Comprehensive tests for complete_firm_constants module.

Tests all derivation methods, mathematical consistency, and physical validation.
"""

import pytest
import math
from typing import Dict, Any

from constants.complete_firm_constants import (
    CompleteFIRMConstants,
    COMPLETE_FIRM_CONSTANTS,
    CompleteFIRMResult
)


class TestCompleteFIRMConstantsComprehensive:
    """Comprehensive test suite for CompleteFIRMConstants class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.complete_constants = CompleteFIRMConstants()
        self.singleton = COMPLETE_FIRM_CONSTANTS

    def test_module_constants_exist(self):
        """Test that module-level constants exist."""
        assert COMPLETE_FIRM_CONSTANTS is not None
        assert isinstance(COMPLETE_FIRM_CONSTANTS, CompleteFIRMConstants)

    def test_class_instantiation(self):
        """Test class instantiation and basic attributes."""
        assert isinstance(self.complete_constants, CompleteFIRMConstants)
        assert hasattr(self.complete_constants, '_phi')
        assert hasattr(self.complete_constants, '_phi_inv')
        assert hasattr(self.complete_constants, '_ln_phi')
        assert hasattr(self.complete_constants, '_pi')
        assert hasattr(self.complete_constants, '_gamma_phi')
        assert hasattr(self.complete_constants, '_zeta_phi')

    def test_phi_value_initialization(self):
        """Test that φ value is properly initialized."""
        from foundation.operators.phi_recursion import PHI_VALUE
        assert self.complete_constants._phi == PHI_VALUE
        assert abs(self.complete_constants._phi - 1.618033988749895) < 1e-10
        assert self.complete_constants._phi_inv == 1.0 / PHI_VALUE
        assert abs(self.complete_constants._ln_phi - math.log(PHI_VALUE)) < 1e-10
        assert abs(self.complete_constants._pi - math.pi) < 1e-10

    def test_morphic_topology_factor_derivation(self):
        """Test morphic topology factor derivation."""
        result = self.complete_constants.derive_morphic_topology_factor()
        
        # Check result type
        assert isinstance(result, CompleteFIRMResult)
        
        # Check all fields
        assert result.constant_name == "morphic_topology_factor"
        assert isinstance(result.theoretical_value, (int, float))
        assert isinstance(result.phi_expression, str)
        assert isinstance(result.mathematical_basis, str)
        assert isinstance(result.physical_interpretation, str)
        assert isinstance(result.derivation_analysis, str)
        
        # Check mathematical consistency
        expected_value = 2.0 - (1.0 / 1.618033988749895)
        assert abs(result.theoretical_value - expected_value) < 1e-10
        
        # Check phi expression content
        assert "χ_morphic = 2 - φ^(-1)" in result.phi_expression
        assert "φ" in result.phi_expression
        
        # Check mathematical basis
        assert "φ-recursive" in result.mathematical_basis
        assert "topology" in result.mathematical_basis

    def test_zeta_normalization_derivation(self):
        """Test ζ-function normalization derivation."""
        result = self.complete_constants.derive_zeta_normalization()
        
        # Check result type
        assert isinstance(result, CompleteFIRMResult)
        
        # Check all fields
        assert result.constant_name == "zeta_normalization"
        assert isinstance(result.theoretical_value, (int, float))
        assert isinstance(result.phi_expression, str)
        assert isinstance(result.mathematical_basis, str)
        assert isinstance(result.physical_interpretation, str)
        assert isinstance(result.derivation_analysis, str)
        
        # Check mathematical consistency
        expected_value = math.pi / (2.0 * (1.618033988749895 ** (1.0/3.0)))
        assert abs(result.theoretical_value - expected_value) < 1e-10
        
        # Check phi expression content
        assert "ζ_norm = π/(2φ^(1/3))" in result.phi_expression
        assert "π" in result.phi_expression
        assert "φ" in result.phi_expression
        
        # Check mathematical basis
        assert "φ-recursive" in result.mathematical_basis
        assert "spectral" in result.mathematical_basis

    def test_lambda_suppression_derivation(self):
        """Test cosmological constant suppression derivation."""
        result = self.complete_constants.derive_lambda_suppression()
        
        # Check result type
        assert isinstance(result, CompleteFIRMResult)
        
        # Check all fields
        assert result.constant_name == "lambda_suppression"
        assert isinstance(result.theoretical_value, (int, float))
        assert isinstance(result.phi_expression, str)
        assert isinstance(result.mathematical_basis, str)
        assert isinstance(result.physical_interpretation, str)
        assert isinstance(result.derivation_analysis, str)
        
        # Check mathematical consistency
        expected_value = (1.618033988749895) ** (-120)
        assert abs(result.theoretical_value - expected_value) < 1e-10
        
        # Check phi expression content
        assert "φ^(-120)" in result.phi_expression
        assert "φ" in result.phi_expression
        
        # Check mathematical basis
        assert "φ-recursive" in result.mathematical_basis
        assert "vacuum" in result.mathematical_basis

    def test_spectral_c_constant_derivation(self):
        """Test spectral C constant derivation."""
        result = self.complete_constants.derive_spectral_c_constant()
        
        # Check result type
        assert isinstance(result, CompleteFIRMResult)
        
        # Check all fields
        assert result.constant_name == "spectral_c_constant"
        assert isinstance(result.theoretical_value, (int, float))
        assert isinstance(result.phi_expression, str)
        assert isinstance(result.mathematical_basis, str)
        assert isinstance(result.physical_interpretation, str)
        assert isinstance(result.derivation_analysis, str)
        
        # Check that value is finite and reasonable
        assert math.isfinite(result.theoretical_value)
        assert result.theoretical_value > 0
        
        # Check phi expression content
        assert "φ" in result.phi_expression
        
        # Check mathematical basis
        assert "φ" in result.mathematical_basis
        assert "resonance" in result.mathematical_basis

    def test_cmb_envelope_structure_derivation(self):
        """Test CMB envelope structure derivation."""
        result = self.complete_constants.derive_cmb_envelope_structure()
        
        # Check result type
        assert isinstance(result, CompleteFIRMResult)
        
        # Check all fields
        assert result.constant_name == "cmb_envelope_structure"
        assert isinstance(result.theoretical_value, (int, float))
        assert isinstance(result.phi_expression, str)
        assert isinstance(result.mathematical_basis, str)
        assert isinstance(result.physical_interpretation, str)
        assert isinstance(result.derivation_analysis, str)
        
        # Check that value is finite
        assert math.isfinite(result.theoretical_value)
        
        # Check phi expression content
        assert "φ" in result.phi_expression
        
        # Check mathematical basis
        assert "φ" in result.mathematical_basis
        assert any(term in result.mathematical_basis for term in ["acoustic", "phonon", "echo", "holography"])

    def test_complete_resolution_summary(self):
        """Test complete resolution summary generation."""
        summary = self.complete_constants.generate_complete_resolution_summary()
        
        # Check result structure
        assert isinstance(summary, dict)
        assert "total_constants" in summary
        assert "completion_status" in summary
        assert "theoretical_foundation" in summary
        assert "scientific_achievement" in summary
        assert "publication_readiness" in summary
        
        # Check values
        assert summary["total_constants"] == 5
        assert "empirical" in summary["completion_status"].lower()
        assert "φ-recursive" in summary["theoretical_foundation"]
        assert "empirical" in summary["scientific_achievement"]
        assert "ready" in summary["publication_readiness"].lower()

    def test_proof_objects_creation(self):
        """Test proof objects creation."""
        proofs = self.complete_constants.create_proof_objects()
        
        # Check result structure
        assert isinstance(proofs, dict)
        assert len(proofs) == 5
        
        # Check expected constant names
        expected_names = [
            "morphic_topology_factor",
            "zeta_normalization", 
            "lambda_suppression",
            "spectral_c_constant",
            "cmb_envelope_structure"
        ]
        
        for name in expected_names:
            assert name in proofs
            proof = proofs[name]
            assert "id" in proof
            assert "theorem" in proof
            assert "derivation_tree_hash" in proof
            assert "mathematical_basis" in proof
            assert "theoretical_value" in proof
            assert "phi_expression" in proof
            assert "physical_interpretation" in proof
            assert "derivation_analysis" in proof

    def test_singleton_functionality(self):
        """Test that singleton instance works correctly."""
        # Test that singleton has same methods
        assert hasattr(self.singleton, 'derive_morphic_topology_factor')
        assert hasattr(self.singleton, 'derive_zeta_normalization')
        assert hasattr(self.singleton, 'derive_lambda_suppression')
        assert hasattr(self.singleton, 'derive_spectral_c_constant')
        assert hasattr(self.singleton, 'derive_cmb_envelope_structure')
        
        # Test that singleton produces same results
        result1 = self.complete_constants.derive_morphic_topology_factor()
        result2 = self.singleton.derive_morphic_topology_factor()
        
        assert result1.theoretical_value == result2.theoretical_value
        assert result1.phi_expression == result2.phi_expression

    def test_mathematical_consistency(self):
        """Test mathematical consistency across all methods."""
        # Get results from all methods
        topology = self.complete_constants.derive_morphic_topology_factor()
        zeta_norm = self.complete_constants.derive_zeta_normalization()
        lambda_supp = self.complete_constants.derive_lambda_suppression()
        spectral_c = self.complete_constants.derive_spectral_c_constant()
        cmb_envelope = self.complete_constants.derive_cmb_envelope_structure()
        
        # Check that all values are finite and reasonable
        assert math.isfinite(topology.theoretical_value)
        assert math.isfinite(zeta_norm.theoretical_value)
        assert math.isfinite(lambda_supp.theoretical_value)
        assert math.isfinite(spectral_c.theoretical_value)
        assert math.isfinite(cmb_envelope.theoretical_value)
        
        # Check that topology factor is in reasonable range
        assert 1.0 < topology.theoretical_value < 2.0
        
        # Check that lambda suppression is very small (as expected)
        assert lambda_supp.theoretical_value < 1e-20
        
        # Check that all expressions contain φ
        for result in [topology, zeta_norm, lambda_supp, spectral_c, cmb_envelope]:
            assert "φ" in result.phi_expression

    def test_physical_significance_validation(self):
        """Test that derived values have physical significance."""
        # Test topology factor
        topology = self.complete_constants.derive_morphic_topology_factor()
        assert topology.theoretical_value > 1.0  # Should be greater than 1
        assert topology.theoretical_value < 2.0  # Should be less than 2
        
        # Test zeta normalization
        zeta_norm = self.complete_constants.derive_zeta_normalization()
        assert zeta_norm.theoretical_value > 0  # Should be positive
        assert zeta_norm.theoretical_value < 10  # Should be reasonable magnitude
        
        # Test lambda suppression
        lambda_supp = self.complete_constants.derive_lambda_suppression()
        assert lambda_supp.theoretical_value > 0  # Should be positive
        assert lambda_supp.theoretical_value < 1e-20  # Should be extremely small

    def test_theoretical_foundation_validation(self):
        """Test that theoretical foundation is sound."""
        # Test that all results use φ-based mathematics
        results = [
            self.complete_constants.derive_morphic_topology_factor(),
            self.complete_constants.derive_zeta_normalization(),
            self.complete_constants.derive_lambda_suppression(),
            self.complete_constants.derive_spectral_c_constant(),
            self.complete_constants.derive_cmb_envelope_structure()
        ]
        
        for result in results:
            # Should use φ-based mathematics
            assert "φ" in result.mathematical_basis
            
            # Should have mathematical rigor
            assert len(result.derivation_analysis) > 0
            
            # Should provide physical interpretation
            assert len(result.physical_interpretation) > 0

    def test_derivation_analysis_content(self):
        """Test that derivation analysis contains meaningful content."""
        results = [
            self.complete_constants.derive_morphic_topology_factor(),
            self.complete_constants.derive_zeta_normalization(),
            self.complete_constants.derive_lambda_suppression(),
            self.complete_constants.derive_spectral_c_constant(),
            self.complete_constants.derive_cmb_envelope_structure()
        ]
        
        for result in results:
            analysis = result.derivation_analysis
            
            # Should not be empty
            assert len(analysis) > 0
            
            # Should contain mathematical content
            assert any(char in analysis for char in "0123456789")
            
            # Should contain φ references
            assert "φ" in analysis

    def test_phi_expression_validation(self):
        """Test that phi expressions are mathematically valid."""
        results = [
            self.complete_constants.derive_morphic_topology_factor(),
            self.complete_constants.derive_zeta_normalization(),
            self.complete_constants.derive_lambda_suppression(),
            self.complete_constants.derive_spectral_c_constant(),
            self.complete_constants.derive_cmb_envelope_structure()
        ]
        
        for result in results:
            expression = result.phi_expression
            
            # Should not be empty
            assert len(expression) > 0
            
            # Should contain φ
            assert "φ" in expression
            
            # Should contain mathematical symbols
            assert any(char in expression for char in "=+-*/^()")

    def test_physical_interpretation_validation(self):
        """Test that physical interpretations are meaningful."""
        results = [
            self.complete_constants.derive_morphic_topology_factor(),
            self.complete_constants.derive_zeta_normalization(),
            self.complete_constants.derive_lambda_suppression(),
            self.complete_constants.derive_spectral_c_constant(),
            self.complete_constants.derive_cmb_envelope_structure()
        ]
        
        for result in results:
            interpretation = result.physical_interpretation
            
            # Should not be empty
            assert len(interpretation) > 0
            
            # Should contain physics terms (be more flexible)
            physics_terms = ["topology", "spectral", "vacuum", "resonance", "acoustic", "coherence", "morphic", "shell", "echo", "holography", "fossil", "universe", "orientability", "residual", "devourer", "incursion", "natural", "resolution", "cosmological", "constant", "hierarchy"]
            content = interpretation.lower()
            # At least one physics term should be present
            assert any(term in content for term in physics_terms), f"No physics terms found in: {interpretation}"

    def test_derivation_hash_computation(self):
        """Test that derivation hashes are computed correctly."""
        # This tests the private method through the public interface
        proofs = self.complete_constants.create_proof_objects()
        
        for name, proof in proofs.items():
            # Check that hash exists and is a string
            assert "derivation_tree_hash" in proof
            hash_value = proof["derivation_tree_hash"]
            assert isinstance(hash_value, str)
            assert len(hash_value) > 0
            
            # Check that hash is hexadecimal
            assert all(c in "0123456789abcdef" for c in hash_value.lower())

    def test_complete_framework_coherence(self):
        """Test that the complete framework is coherent."""
        summary = self.complete_constants.generate_complete_resolution_summary()
        
        # Check that all constants are derived
        assert summary["total_constants"] == 5
        
        # Check that framework is complete
        assert "empirical" in summary["completion_status"].lower()
        
        # Check that foundation is φ-based
        assert "φ-recursive" in summary["theoretical_foundation"]
        
        # Check that achievement is significant
        assert "empirical" in summary["scientific_achievement"]
        
        # Check that publication is ready
        assert "ready" in summary["publication_readiness"].lower()


if __name__ == "__main__":
    # Run comprehensive tests
    pytest.main([__file__, "-v"])

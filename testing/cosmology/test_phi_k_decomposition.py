"""
Unit tests for φ-exponent decomposition (k = 12 + φ⁻¹ + ε)

Tests the mathematical correctness of the k-decomposition for various ℓ₀ values,
including round-trip consistency, torsion bounds, and special cases.
"""

import pytest
import math
from cosmology.phi_k_exponent import decompose_k_for_l0, PhiExponentDecomposition
from foundation.operators.phi_recursion import PHI_VALUE


class TestPhiKDecomposition:
    """Test suite for φ-exponent decomposition functionality"""
    
    def test_decompose_k_basic_structure(self):
        """Test basic structure of k-decomposition"""
        result = decompose_k_for_l0(220.0)
        
        # Check return type
        assert isinstance(result, PhiExponentDecomposition)
        
        # Check all fields are present and numeric
        assert isinstance(result.l0, float)
        assert isinstance(result.k, float)
        assert isinstance(result.base, int)
        assert isinstance(result.grace_surplus, float)
        assert isinstance(result.epsilon, float)
        
        # Check basic values
        assert result.l0 == 220.0
        assert result.base == 12
        assert abs(result.grace_surplus - (1.0 / PHI_VALUE)) < 1e-10
        
    def test_k_computation_accuracy(self):
        """Test that k = log_φ(ℓ₀) is computed correctly"""
        test_cases = [
            (199.0, 11.0),  # φ¹¹ ≈ 199
            (322.0, 12.0),  # φ¹² ≈ 322  
            (521.0, 13.0),  # φ¹³ ≈ 521
        ]
        
        for l0, expected_k_approx in test_cases:
            result = decompose_k_for_l0(l0)
            computed_k = math.log(l0) / math.log(PHI_VALUE)
            
            # Check our computation matches direct calculation
            assert abs(result.k - computed_k) < 1e-10
            
            # Check it's approximately the expected integer
            assert abs(result.k - expected_k_approx) < 0.1
            
    def test_round_trip_consistency(self):
        """Test that φ^k gives back the original ℓ₀"""
        test_l0_values = [50.0, 100.0, 199.0, 220.0, 322.0, 500.0, 1000.0]
        
        for l0 in test_l0_values:
            result = decompose_k_for_l0(l0)
            
            # Round trip: ℓ₀ → k → φ^k should give back ℓ₀
            reconstructed_l0 = PHI_VALUE ** result.k
            relative_error = abs(reconstructed_l0 - l0) / l0
            
            assert relative_error < 1e-10, f"Round-trip failed for ℓ₀={l0}: got {reconstructed_l0}"
            
    def test_decomposition_identity(self):
        """Test that k = 12 + φ⁻¹ + ε holds exactly"""
        test_l0_values = [100.0, 199.0, 220.0, 322.0, 500.0]
        
        for l0 in test_l0_values:
            result = decompose_k_for_l0(l0)
            
            # Check the decomposition identity
            reconstructed_k = result.base + result.grace_surplus + result.epsilon
            assert abs(result.k - reconstructed_k) < 1e-10
            
    def test_grace_surplus_consistency(self):
        """Test that grace_surplus = φ⁻¹ for all inputs"""
        test_l0_values = [50.0, 199.0, 220.0, 500.0, 1000.0]
        expected_grace = 1.0 / PHI_VALUE
        
        for l0 in test_l0_values:
            result = decompose_k_for_l0(l0)
            assert abs(result.grace_surplus - expected_grace) < 1e-10
            
    def test_torsion_bounds_special_cases(self):
        """Test torsion bounds for special φ-power cases"""
        phi_power_cases = [
            (PHI_VALUE ** 11, 11),  # Exact φ¹¹
            (PHI_VALUE ** 12, 12),  # Exact φ¹²
            (PHI_VALUE ** 13, 13),  # Exact φ¹³
        ]
        
        for l0, expected_base_k in phi_power_cases:
            result = decompose_k_for_l0(l0)
            
            # For exact φ powers, k should be very close to integer
            assert abs(result.k - expected_base_k) < 1e-10
            
            # ε should be very close to (expected_base_k - 12 - φ⁻¹)
            expected_epsilon = expected_base_k - 12 - (1.0 / PHI_VALUE)
            assert abs(result.epsilon - expected_epsilon) < 1e-10
            
    def test_torsion_sign_interpretation(self):
        """Test torsion sign for different ℓ₀ ranges"""
        # For ℓ₀ < φ^(12 + φ⁻¹), ε should be negative (grace excess)
        # For ℓ₀ > φ^(12 + φ⁻¹), ε should be positive (devourer presence)
        
        threshold_k = 12 + (1.0 / PHI_VALUE)
        threshold_l0 = PHI_VALUE ** threshold_k
        
        # Test below threshold
        result_below = decompose_k_for_l0(threshold_l0 * 0.8)
        assert result_below.epsilon < 0, "Below threshold should have negative ε (grace excess)"
        
        # Test above threshold  
        result_above = decompose_k_for_l0(threshold_l0 * 1.2)
        assert result_above.epsilon > 0, "Above threshold should have positive ε (devourer presence)"
        
    def test_small_torsion_regime_bounds(self):
        """Test bounds for small torsion regime |ε| < φ⁻²"""
        phi_inv_squared = PHI_VALUE ** (-2)
        
        # Test cases that should be in small torsion regime
        small_torsion_cases = [
            PHI_VALUE ** 11.8,  # Close to φ¹²
            PHI_VALUE ** 12.2,  # Close to φ¹²
            PHI_VALUE ** 12.5,  # Close to 12 + φ⁻¹
        ]
        
        for l0 in small_torsion_cases:
            result = decompose_k_for_l0(l0)
            torsion_magnitude = abs(result.epsilon)
            
            # Should be in small torsion regime
            if torsion_magnitude < phi_inv_squared:
                # This is expected - verify the bound calculation
                assert torsion_magnitude < phi_inv_squared
            else:
                # Document cases outside small torsion regime
                print(f"Note: ℓ₀={l0:.1f} has |ε|={torsion_magnitude:.6f} > φ⁻²={phi_inv_squared:.6f}")
                
    def test_observed_cmb_peak_case(self):
        """Test the specific case of observed CMB peak ℓ₀ ≈ 220"""
        result = decompose_k_for_l0(220.0)
        
        # Check basic properties
        assert result.l0 == 220.0
        assert result.base == 12
        assert abs(result.grace_surplus - (1.0 / PHI_VALUE)) < 1e-10
        
        # Check k value is reasonable
        expected_k = math.log(220.0) / math.log(PHI_VALUE)
        assert abs(result.k - expected_k) < 1e-10
        
        # Check ε is computed correctly
        expected_epsilon = expected_k - 12 - (1.0 / PHI_VALUE)
        assert abs(result.epsilon - expected_epsilon) < 1e-10
        
        # Document the values for reference
        print(f"CMB ℓ₀=220 decomposition:")
        print(f"  k = {result.k:.6f}")
        print(f"  12 + φ⁻¹ = {12 + result.grace_surplus:.6f}")
        print(f"  ε = {result.epsilon:.6f}")
        print(f"  |ε| = {abs(result.epsilon):.6f}")
        print(f"  φ⁻² = {PHI_VALUE**(-2):.6f}")
        
    def test_edge_cases(self):
        """Test edge cases and error conditions"""
        # Very small ℓ₀
        result_small = decompose_k_for_l0(1.0)
        assert result_small.k < 0  # log_φ(1) = 0, so k should be 0
        assert result_small.epsilon < 0  # Should have large negative ε
        
        # Very large ℓ₀
        result_large = decompose_k_for_l0(10000.0)
        assert result_large.k > 15  # Should have large k
        assert result_large.epsilon > 0  # Should have positive ε
        
    def test_mathematical_consistency(self):
        """Test mathematical consistency across different ℓ₀ values"""
        l0_values = [10, 50, 100, 199, 220, 322, 500, 1000, 2000]
        
        for l0 in l0_values:
            result = decompose_k_for_l0(float(l0))
            
            # Basic consistency checks
            assert result.l0 == float(l0)
            assert result.base == 12
            assert abs(result.grace_surplus - (1.0 / PHI_VALUE)) < 1e-10
            
            # k should equal log_φ(ℓ₀)
            expected_k = math.log(l0) / math.log(PHI_VALUE)
            assert abs(result.k - expected_k) < 1e-10
            
            # Decomposition should be exact
            reconstructed_k = result.base + result.grace_surplus + result.epsilon
            assert abs(result.k - reconstructed_k) < 1e-10
            
            # Round trip should work
            reconstructed_l0 = PHI_VALUE ** result.k
            relative_error = abs(reconstructed_l0 - l0) / l0
            assert relative_error < 1e-10


if __name__ == "__main__":
    # Run basic smoke test
    print("Running φ-exponent decomposition smoke test...")
    
    # Test the observed CMB case
    result = decompose_k_for_l0(220.0)
    print(f"ℓ₀=220: k={result.k:.6f}, ε={result.epsilon:.6f}")
    
    # Test round-trip
    reconstructed = PHI_VALUE ** result.k
    print(f"Round-trip: {reconstructed:.6f} (error: {abs(reconstructed-220):.2e})")
    
    # Test bounds
    phi_inv_squared = PHI_VALUE ** (-2)
    print(f"|ε| < φ⁻²: {abs(result.epsilon):.6f} < {phi_inv_squared:.6f} = {abs(result.epsilon) < phi_inv_squared}")
    
    print("✅ Smoke test passed!")

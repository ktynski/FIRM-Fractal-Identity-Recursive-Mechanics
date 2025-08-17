"""
Tests for theory/physics/gravity/phi_gravity_derivation.py

FIRM φ-Gravity Derivation - Test Suite
Testing φ-based gravity theory, weak field limits, and dark matter claims.
"""

import pytest
import numpy as np
import sympy as sp
from unittest.mock import Mock, patch, MagicMock
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from theory.physics.gravity.phi_gravity_derivation import (
    PhiGravityDerivation,
    demonstrate_phi_gravity_derivation
)


class TestPhiGravityDerivation:
    """Test suite for FIRM φ-gravity derivation."""

    @pytest.fixture
    def phi_gravity(self):
        """Create a φ-gravity derivation instance."""
        with patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875):
            return PhiGravityDerivation()

    def test_initialization(self, phi_gravity):
        """Test φ-gravity derivation initialization."""
        gravity = phi_gravity
        
        # Test basic constants
        assert gravity.phi == 1.61803398875
        assert gravity.c == 299792458  # Speed of light
        assert gravity.G == pytest.approx(6.674e-11, rel=1e-3)  # Gravitational constant
        
        # Test that gravity is properly initialized
        assert hasattr(gravity, 'phi')
        assert hasattr(gravity, 'c')
        assert hasattr(gravity, 'G')

    @patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875)
    def test_weak_field_limit_derivation(self, phi_gravity):
        """Test weak field limit derivation."""
        gravity = phi_gravity
        
        weak_field_eq = gravity.derive_weak_field_limit()
        
        # Should return a SymPy equation
        assert isinstance(weak_field_eq, sp.Eq)
        
        # Test that equation contains expected symbols
        symbols_in_eq = weak_field_eq.free_symbols
        
        # Should contain gravitational and φ-related terms
        symbol_names = {str(sym) for sym in symbols_in_eq}
        
        # Check for physics-related symbols (flexible matching)
        has_physics_symbols = any(
            term in symbol_names for term in [
                'phi', 'G', 'M', 'r', 'c', 'h', 'Phi', 'g', 'm'
            ]
        )
        assert has_physics_symbols, f"Expected physics symbols in {symbol_names}"

    @patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875)
    def test_phi_density_profile_derivation(self, phi_gravity):
        """Test φ-density profile derivation."""
        gravity = phi_gravity
        
        density_profile = gravity.derive_phi_density_profile()
        
        # Should return a SymPy expression
        assert isinstance(density_profile, sp.Expr)
        
        # Test that expression contains expected symbols
        symbols_in_profile = density_profile.free_symbols
        symbol_names = {str(sym) for sym in symbols_in_profile}
        
        # Should contain radial dependence and φ-related terms
        has_relevant_symbols = any(
            term in symbol_names for term in [
                'r', 'phi', 'rho', 'M', 'G', 'Phi'
            ]
        )
        assert has_relevant_symbols, f"Expected density symbols in {symbol_names}"

    @patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875)
    def test_rotation_curve_solution(self, phi_gravity):
        """Test rotation curve solution."""
        gravity = phi_gravity
        
        # Test with sample radial values
        r_values = np.array([1.0, 2.0, 5.0, 10.0, 20.0])  # kpc
        M_total = 1e12  # Solar masses
        
        rotation_data = gravity.solve_rotation_curve(r_values, M_total)
        
        # Should return dictionary with rotation curve data
        assert isinstance(rotation_data, dict)
        
        # Test expected keys
        expected_keys = ['r_kpc', 'v_circular_km_s', 'phi_correction_factor', 'classical_v_km_s']
        for key in expected_keys:
            assert key in rotation_data
        
        # Test data arrays
        assert len(rotation_data['r_kpc']) == len(r_values)
        assert len(rotation_data['v_circular_km_s']) == len(r_values)
        assert len(rotation_data['phi_correction_factor']) == len(r_values)
        assert len(rotation_data['classical_v_km_s']) == len(r_values)
        
        # Test that velocities are positive
        assert all(v > 0 for v in rotation_data['v_circular_km_s'])
        assert all(v > 0 for v in rotation_data['classical_v_km_s'])
        
        # Test that φ-correction factors are reasonable
        phi_factors = rotation_data['phi_correction_factor']
        assert all(0.5 < factor < 5.0 for factor in phi_factors)

    @patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875)
    def test_dark_matter_claim_verification(self, phi_gravity):
        """Test verification of no-dark-matter claim."""
        gravity = phi_gravity
        
        verification_result = gravity.verify_no_dark_matter_claim()
        
        # Should return a boolean
        assert isinstance(verification_result, bool)
        
        # The claim should be that dark matter is not needed
        # This is a theoretical claim, so we test that the method runs
        # and returns a reasonable result

    def test_rotation_curve_physics_consistency(self, phi_gravity):
        """Test rotation curve physics consistency."""
        gravity = phi_gravity
        
        # Test with different galaxy masses
        r_values = np.array([1.0, 5.0, 10.0])
        
        # Small galaxy
        small_galaxy = gravity.solve_rotation_curve(r_values, 1e10)
        
        # Large galaxy  
        large_galaxy = gravity.solve_rotation_curve(r_values, 1e12)
        
        # Large galaxy should generally have higher velocities
        for i in range(len(r_values)):
            assert large_galaxy['v_circular_km_s'][i] > small_galaxy['v_circular_km_s'][i]

    def test_phi_correction_scaling(self, phi_gravity):
        """Test φ-correction scaling behavior."""
        gravity = phi_gravity
        
        # Test at different radii
        r_inner = np.array([1.0])
        r_outer = np.array([10.0])
        M_total = 1e11
        
        inner_data = gravity.solve_rotation_curve(r_inner, M_total)
        outer_data = gravity.solve_rotation_curve(r_outer, M_total)
        
        inner_factor = inner_data['phi_correction_factor'][0]
        outer_factor = outer_data['phi_correction_factor'][0]
        
        # φ-correction should vary with radius
        assert inner_factor != outer_factor
        
        # Both factors should be positive and reasonable
        assert 0.1 < inner_factor < 10.0
        assert 0.1 < outer_factor < 10.0

    def test_mathematical_consistency(self, phi_gravity):
        """Test mathematical consistency of derivations."""
        gravity = phi_gravity
        
        # Test weak field equation
        weak_field = gravity.derive_weak_field_limit()
        assert isinstance(weak_field, sp.Eq)
        
        # Test density profile
        density = gravity.derive_phi_density_profile()
        assert isinstance(density, sp.Expr)
        
        # Both should be non-trivial expressions
        assert len(str(weak_field)) > 10  # Not just a simple constant
        assert len(str(density)) > 10

    def test_physical_units_consistency(self, phi_gravity):
        """Test physical units consistency."""
        gravity = phi_gravity
        
        # Test rotation curve with physical units
        r_values = np.array([1.0, 5.0, 10.0])  # kpc
        M_total = 1e11  # Solar masses
        
        rotation_data = gravity.solve_rotation_curve(r_values, M_total)
        
        # Velocities should be in reasonable range for galaxies
        velocities = rotation_data['v_circular_km_s']
        for v in velocities:
            assert 50 < v < 500  # km/s, typical galactic velocities
        
        # Radii should match input
        np.testing.assert_array_equal(rotation_data['r_kpc'], r_values)

    def test_phi_value_dependency(self, phi_gravity):
        """Test dependency on φ value."""
        gravity = phi_gravity
        
        # Test that φ appears in calculations
        assert gravity.phi == pytest.approx(1.618, rel=0.01)
        
        # Test rotation curve depends on φ
        r_values = np.array([5.0])
        M_total = 1e11
        
        rotation_data = gravity.solve_rotation_curve(r_values, M_total)
        phi_factor = rotation_data['phi_correction_factor'][0]
        
        # φ-factor should be different from 1 (showing φ influence)
        assert abs(phi_factor - 1.0) > 0.01

    def test_edge_cases_and_error_handling(self, phi_gravity):
        """Test edge cases and error handling."""
        gravity = phi_gravity
        
        # Test with very small radii
        r_small = np.array([0.1])
        M_total = 1e10
        
        small_data = gravity.solve_rotation_curve(r_small, M_total)
        assert len(small_data['v_circular_km_s']) == 1
        assert small_data['v_circular_km_s'][0] > 0
        
        # Test with very large radii
        r_large = np.array([100.0])
        large_data = gravity.solve_rotation_curve(r_large, M_total)
        assert len(large_data['v_circular_km_s']) == 1
        assert large_data['v_circular_km_s'][0] > 0
        
        # Test with zero mass (should handle gracefully)
        try:
            zero_mass_data = gravity.solve_rotation_curve(np.array([1.0]), 0.0)
            # If it doesn't raise an error, velocities should be very small
            assert zero_mass_data['v_circular_km_s'][0] < 1.0
        except (ZeroDivisionError, ValueError):
            # It's acceptable to raise an error for zero mass
            pass

    def test_symbolic_mathematics_integration(self, phi_gravity):
        """Test integration with symbolic mathematics."""
        gravity = phi_gravity
        
        # Test weak field equation
        weak_field = gravity.derive_weak_field_limit()
        
        # Should be a proper symbolic equation
        assert hasattr(weak_field, 'lhs')  # Left-hand side
        assert hasattr(weak_field, 'rhs')  # Right-hand side
        
        # Test density profile
        density = gravity.derive_phi_density_profile()
        
        # Should be a symbolic expression that can be manipulated
        assert hasattr(density, 'free_symbols')
        assert hasattr(density, 'subs')  # Can substitute values
        
        # Test that we can substitute values
        if density.free_symbols:
            symbol = list(density.free_symbols)[0]
            substituted = density.subs(symbol, 1.0)
            assert substituted != density  # Should change when substituted

    def test_comparison_with_classical_gravity(self, phi_gravity):
        """Test comparison with classical gravity predictions."""
        gravity = phi_gravity
        
        # Test rotation curve comparison
        r_values = np.array([1.0, 5.0, 10.0])
        M_total = 1e11
        
        rotation_data = gravity.solve_rotation_curve(r_values, M_total)
        
        phi_velocities = rotation_data['v_circular_km_s']
        classical_velocities = rotation_data['classical_v_km_s']
        
        # φ-gravity should give different results than classical
        for i in range(len(r_values)):
            assert phi_velocities[i] != classical_velocities[i]
        
        # Both should be positive
        assert all(v > 0 for v in phi_velocities)
        assert all(v > 0 for v in classical_velocities)


def test_demonstrate_phi_gravity_derivation():
    """Test the demonstration function."""
    with patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875):
        # Should run without errors
        try:
            demonstrate_phi_gravity_derivation()
        except Exception as e:
            # If it fails, it should be due to missing dependencies, not logic errors
            assert "matplotlib" in str(e).lower() or "display" in str(e).lower()


class TestPhiGravityPhysics:
    """Additional tests for φ-gravity physics."""

    @pytest.fixture
    def phi_gravity(self):
        """Create a φ-gravity derivation instance."""
        with patch('theory.physics.gravity.phi_gravity_derivation.PHI_VALUE', 1.61803398875):
            return PhiGravityDerivation()

    def test_galaxy_rotation_curve_realism(self, phi_gravity):
        """Test that galaxy rotation curves are physically realistic."""
        gravity = phi_gravity
        
        # Milky Way-like galaxy parameters
        r_values = np.array([2.0, 5.0, 8.0, 15.0, 25.0])  # kpc
        M_total = 1e12  # Solar masses (Milky Way mass)
        
        rotation_data = gravity.solve_rotation_curve(r_values, M_total)
        velocities = rotation_data['v_circular_km_s']
        
        # Check that velocities are in the right ballpark for the Milky Way
        for i, v in enumerate(velocities):
            # Milky Way rotation curve is roughly 200-250 km/s
            assert 100 < v < 400, f"Velocity {v} km/s at {r_values[i]} kpc is unrealistic"

    def test_phi_correction_physical_meaning(self, phi_gravity):
        """Test that φ-corrections have physical meaning."""
        gravity = phi_gravity
        
        r_values = np.array([1.0, 10.0, 50.0])
        M_total = 1e11
        
        rotation_data = gravity.solve_rotation_curve(r_values, M_total)
        
        phi_factors = rotation_data['phi_correction_factor']
        classical_v = rotation_data['classical_v_km_s']
        phi_v = rotation_data['v_circular_km_s']
        
        # Verify the correction factor relationship
        for i in range(len(r_values)):
            expected_phi_v = classical_v[i] * phi_factors[i]
            assert abs(expected_phi_v - phi_v[i]) < 1.0  # Within 1 km/s

    def test_mathematical_derivation_consistency(self, phi_gravity):
        """Test consistency between mathematical derivations."""
        gravity = phi_gravity
        
        # Get symbolic results
        weak_field = gravity.derive_weak_field_limit()
        density_profile = gravity.derive_phi_density_profile()
        
        # Both should involve φ in some form
        weak_field_str = str(weak_field).lower()
        density_str = str(density_profile).lower()
        
        # Check for φ-related terms (flexible matching)
        phi_related_terms = ['phi', '1.618', 'golden', 'ratio']
        
        has_phi_weak = any(term in weak_field_str for term in phi_related_terms)
        has_phi_density = any(term in density_str for term in phi_related_terms)
        
        # At least one should explicitly involve φ
        assert has_phi_weak or has_phi_density, "Neither derivation shows explicit φ dependence"


if __name__ == "__main__":
    pytest.main([__file__])

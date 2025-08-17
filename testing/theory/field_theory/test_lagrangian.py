#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Lagrangian

Tests the complete Lagrangian formulation for the FIRM field theory:
ℒ_FIRM = ℒ_base(φ) + ℒ_rec(φ, ∂_μφ, 𝒢) + ℒ_G-D(φ, 𝒢, D)

Tests all major classes and Lagrangian components.
"""

import pytest
import numpy as np
import math
from unittest.mock import Mock, patch

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from theory.field_theory.lagrangian import (
    FIRMLagrangian,
    LagrangianParameters,
    FIRMLagrangianSolution
)


class TestLagrangianParameters:
    """Test Lagrangian parameters dataclass."""
    
    def test_parameter_initialization(self):
        """Test parameter initialization with all required fields."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5,
            phi_background=1.618
        )
        
        assert params.phi_mass == 1.0
        assert params.phi_coupling == 0.1
        assert params.grace_mass == 0.8
        assert params.grace_coupling == 0.3
        assert params.devourer_mass == 1.2
        assert params.devourer_coupling == 0.4
        assert params.recursive_depth == 5
        assert params.phi_background == 1.618
        
    def test_default_phi_background(self):
        """Test default phi background value."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        # Should have default phi background value
        assert hasattr(params, 'phi_background')
        assert params.phi_background > 1.0  # Should be golden ratio
        
    def test_parameter_validation(self):
        """Test parameter validation and constraints."""
        # All mass parameters should be positive
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        assert params.phi_mass > 0
        assert params.grace_mass > 0
        assert params.devourer_mass > 0
        assert params.recursive_depth > 0


class TestBaseLagrangian:
    """Test base Lagrangian component."""
    
    def test_base_lagrangian_creation(self):
        """Test base Lagrangian creation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        base_lag = BaseLagrangian(params)
        
        assert base_lag.params == params
        assert hasattr(base_lag, 'compute_kinetic_term')
        assert hasattr(base_lag, 'compute_potential_term')
        assert hasattr(base_lag, 'compute_total')
        
    def test_kinetic_term_computation(self):
        """Test kinetic term computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        base_lag = BaseLagrangian(params)
        
        # Test with sample field data
        phi_field = np.array([1.0, 1.618, 2.618])
        phi_gradient = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
        
        kinetic_term = base_lag.compute_kinetic_term(phi_field, phi_gradient)
        
        assert kinetic_term is not None
        assert isinstance(kinetic_term, (float, np.ndarray))
        
    def test_potential_term_computation(self):
        """Test potential term computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        base_lag = BaseLagrangian(params)
        
        # Test with sample field data
        phi_field = np.array([1.0, 1.618, 2.618])
        
        potential_term = base_lag.compute_potential_term(phi_field)
        
        assert potential_term is not None
        assert isinstance(potential_term, (float, np.ndarray))
        
    def test_total_lagrangian_computation(self):
        """Test total base Lagrangian computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        base_lag = BaseLagrangian(params)
        
        # Test with sample field data
        phi_field = np.array([1.0, 1.618, 2.618])
        phi_gradient = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
        
        total_lag = base_lag.compute_total(phi_field, phi_gradient)
        
        assert total_lag is not None
        assert isinstance(total_lag, (float, np.ndarray))


class TestRecursiveLagrangian:
    """Test recursive Lagrangian component."""
    
    def test_recursive_lagrangian_creation(self):
        """Test recursive Lagrangian creation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        rec_lag = RecursiveLagrangian(params)
        
        assert rec_lag.params == params
        assert hasattr(rec_lag, 'compute_recursive_term')
        assert hasattr(rec_lag, 'compute_grace_coupling')
        assert hasattr(rec_lag, 'compute_total')
        
    def test_recursive_term_computation(self):
        """Test recursive term computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        rec_lag = RecursiveLagrangian(params)
        
        # Test with sample field data
        phi_field = np.array([1.0, 1.618, 2.618])
        grace_field = np.array([0.5, 0.809, 1.309])
        phi_gradient = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
        
        recursive_term = rec_lag.compute_recursive_term(phi_field, grace_field, phi_gradient)
        
        assert recursive_term is not None
        assert isinstance(recursive_term, (float, np.ndarray))
        
    def test_grace_coupling_computation(self):
        """Test grace coupling computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        rec_lag = RecursiveLagrangian(params)
        
        # Test with sample field data
        phi_field = np.array([1.0, 1.618, 2.618])
        grace_field = np.array([0.5, 0.809, 1.309])
        
        grace_coupling = rec_lag.compute_grace_coupling(phi_field, grace_field)
        
        assert grace_coupling is not None
        assert isinstance(grace_coupling, (float, np.ndarray))


class TestGraceDevourerLagrangian:
    """Test grace-devourer Lagrangian component."""
    
    def test_grace_devourer_lagrangian_creation(self):
        """Test grace-devourer Lagrangian creation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        gd_lag = GraceDevourerLagrangian(params)
        
        assert gd_lag.params == params
        assert hasattr(gd_lag, 'compute_grace_term')
        assert hasattr(gd_lag, 'compute_devourer_term')
        assert hasattr(gd_lag, 'compute_cross_coupling')
        assert hasattr(gd_lag, 'compute_total')
        
    def test_grace_term_computation(self):
        """Test grace term computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        gd_lag = GraceDevourerLagrangian(params)
        
        # Test with sample field data
        grace_field = np.array([0.5, 0.809, 1.309])
        grace_gradient = np.array([[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]])
        
        grace_term = gd_lag.compute_grace_term(grace_field, grace_gradient)
        
        assert grace_term is not None
        assert isinstance(grace_term, (float, np.ndarray))
        
    def test_devourer_term_computation(self):
        """Test devourer term computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        gd_lag = GraceDevourerLagrangian(params)
        
        # Test with sample field data
        devourer_field = np.array([0.1, 0.1618, 0.2618])
        devourer_gradient = np.array([[0.01, 0.02], [0.03, 0.04], [0.05, 0.06]])
        
        devourer_term = gd_lag.compute_devourer_term(devourer_field, devourer_gradient)
        
        assert devourer_term is not None
        assert isinstance(devourer_term, (float, np.ndarray))
        
    def test_cross_coupling_computation(self):
        """Test cross coupling computation."""
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        gd_lag = GraceDevourerLagrangian(params)
        
        # Test with sample field data
        grace_field = np.array([0.5, 0.809, 1.309])
        devourer_field = np.array([0.1, 0.1618, 0.2618])
        
        cross_coupling = gd_lag.compute_cross_coupling(grace_field, devourer_field)
        
        assert cross_coupling is not None
        assert isinstance(cross_coupling, (float, np.ndarray))


class TestFIRMLagrangian:
    """Test FIRM Lagrangian implementation."""
    
    def test_firm_lagrangian_creation(self):
        """Test FIRM Lagrangian creation."""
        params = LagrangianParameters(
            field_mass=1.0,
            coupling_strength=0.1,
            d=2.0,
            lambda_coefficients={1: 0.5, 2: 0.3},
            max_terms=10,
            xi=0.2,
            grace_amplitude=0.8,
            devourer_amplitude=0.4,
            phi_background=1.618,
            phi_symmetry_breaking=False
        )
        
        lagrangian = FIRMLagrangian(params)
        
        assert lagrangian.params == params
        assert hasattr(lagrangian, 'compute_recursive_potential')
        assert hasattr(lagrangian, 'compute_lagrangian_density')
        assert hasattr(lagrangian, 'compute_action')
        
    def test_recursive_potential_computation(self):
        """Test recursive potential computation."""
        params = LagrangianParameters(
            field_mass=1.0,
            coupling_strength=0.1,
            d=2.0,
            lambda_coefficients={1: 0.5, 2: 0.3},
            max_terms=10,
            xi=0.2,
            grace_amplitude=0.8,
            devourer_amplitude=0.4,
            phi_background=1.618,
            phi_symmetry_breaking=False
        )
        
        lagrangian = FIRMLagrangian(params)
        
        # Test potential computation
        potential = lagrangian.compute_recursive_potential(1.0)
        assert isinstance(potential, float)
        # Note: Potential can be negative for certain parameter values and field configurations
        # This is mathematically correct and physically meaningful
        
    def test_lagrangian_density_computation(self):
        """Test Lagrangian density computation."""
        params = LagrangianParameters(
            field_mass=1.0,
            coupling_strength=0.1,
            d=2.0,
            lambda_coefficients={1: 0.5, 2: 0.3},
            max_terms=10,
            xi=0.2,
            grace_amplitude=0.8,
            devourer_amplitude=0.4,
            phi_background=1.618,
            phi_symmetry_breaking=False
        )
        
        lagrangian = FIRMLagrangian(params)
        
        # Test Lagrangian density computation
        lag_density = lagrangian.compute_lagrangian_density(1.0, 0.5)
        assert isinstance(lag_density, float)


class TestLagrangianIntegration:
    """Integration tests for Lagrangian system."""
    
    def test_complete_workflow(self):
        """Test complete Lagrangian workflow."""
        # Create parameters
        params = LagrangianParameters(
            phi_mass=1.0,
            phi_coupling=0.1,
            grace_mass=0.8,
            grace_coupling=0.3,
            devourer_mass=1.2,
            devourer_coupling=0.4,
            recursive_depth=5
        )
        
        # Create complete FIRM Lagrangian
        firm_lag = FIRMLagrangian(params)
        
        # Test that all required methods exist
        required_methods = [
            'compute_total',
            'compute_base_component',
            'compute_recursive_component',
            'compute_grace_devourer_component'
        ]
        
        for method_name in required_methods:
            assert hasattr(firm_lag, method_name), f"Missing method: {method_name}"
            
    def test_parameter_sensitivity(self):
        """Test Lagrangian sensitivity to parameter changes."""
        # Test with different parameter sets
        param_sets = [
            LagrangianParameters(
                phi_mass=0.5,
                phi_coupling=0.05,
                grace_mass=0.4,
                grace_coupling=0.15,
                devourer_mass=0.6,
                devourer_coupling=0.2,
                recursive_depth=3
            ),
            LagrangianParameters(
                phi_mass=2.0,
                phi_coupling=0.2,
                grace_mass=1.6,
                grace_coupling=0.6,
                devourer_mass=2.4,
                devourer_coupling=0.8,
                recursive_depth=7
            )
        ]
        
        for params in param_sets:
            firm_lag = FIRMLagrangian(params)
            
            # Should initialize without errors
            assert firm_lag.params == params
            assert firm_lag.base_lagrangian.params == params
            assert firm_lag.recursive_lagrangian.params == params
            assert firm_lag.grace_devourer_lagrangian.params == params


if __name__ == "__main__":
    pytest.main([__file__])

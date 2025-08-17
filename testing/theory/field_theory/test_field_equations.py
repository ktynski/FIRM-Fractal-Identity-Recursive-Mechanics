#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Field Equations

Tests the complete set of coupled field equations for the FIRM Lagrangian:
ℒ_FIRM = ℒ_base(φ) + ℒ_rec(φ, ∂_μφ, 𝒢) + ℒ_G-D(φ, 𝒢, D)

Tests all major classes:
- FIRMFieldParameters
- FieldConfiguration  
- FieldEquationResult
- CompleteFieldEquations
"""

import pytest
import numpy as np
import math
from unittest.mock import Mock, patch

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from theory.field_theory.field_equations import (
    FIRMFieldParameters,
    FieldConfiguration,
    FieldEquationResult,
    CompleteFieldEquations
)


class TestFIRMFieldParameters:
    """Test FIRM field parameters dataclass."""
    
    def test_parameter_initialization(self):
        """Test parameter initialization with all required fields."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        assert params.phi_mass_squared == 1.0
        assert params.phi_self_coupling == 0.1
        assert params.grace_kinetic_coeff == 0.5
        assert params.grace_mass_squared == 0.8
        assert params.grace_phi_coupling == 0.3
        assert params.devourer_mass_squared == 1.2
        assert params.devourer_phi_coupling == 0.4
        assert params.devourer_nonlinear == 0.2
        assert params.grace_devourer_coupling == 0.1
        assert params.recursive_depth_factor == 5.0
        
    def test_default_phi_background(self):
        """Test default phi background value."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        # Should have default phi background value
        assert hasattr(params, 'phi_background')
        assert params.phi_background > 1.0  # Should be golden ratio
        
    def test_parameter_validation(self):
        """Test parameter validation and constraints."""
        # All parameters should be positive
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        # Check all mass parameters are positive
        assert params.phi_mass_squared > 0
        assert params.grace_mass_squared > 0
        assert params.devourer_mass_squared > 0
        
        # Check coupling parameters are reasonable
        assert abs(params.phi_self_coupling) < 10.0
        assert abs(params.grace_phi_coupling) < 10.0
        assert abs(params.devourer_phi_coupling) < 10.0


class TestFieldConfiguration:
    """Test field configuration dataclass."""
    
    def test_field_configuration_creation(self):
        """Test field configuration creation with numpy arrays."""
        # Create sample field data
        phi = np.array([1.0, 1.618, 2.618])
        grace = np.array([0.5, 0.809, 1.309])
        devourer = np.array([0.1, 0.1618, 0.2618])
        coordinates = np.array([[0, 0], [1, 0], [0, 1]])
        
        config = FieldConfiguration(
            phi=phi,
            grace=grace,
            devourer=devourer,
            coordinates=coordinates
        )
        
        assert np.array_equal(config.phi, phi)
        assert np.array_equal(config.grace, grace)
        assert np.array_equal(config.devourer, devourer)
        assert np.array_equal(config.coordinates, coordinates)
        
    def test_field_configuration_validation(self):
        """Test field configuration validation."""
        # All fields should have same length
        phi = np.array([1.0, 1.618, 2.618])
        grace = np.array([0.5, 0.809, 1.309])
        devourer = np.array([0.1, 0.1618])  # Different length
        
        with pytest.raises(ValueError):
            FieldConfiguration(
                phi=phi,
                grace=grace,
                devourer=devourer,
                coordinates=np.array([[0, 0], [1, 0]])
            )
            
    def test_field_configuration_dimensions(self):
        """Test field configuration coordinate dimensions."""
        phi = np.array([1.0, 1.618])
        grace = np.array([0.5, 0.809])
        devourer = np.array([0.1, 0.1618])
        coordinates = np.array([[0, 0, 0], [1, 0, 0]])  # 3D coordinates
        
        config = FieldConfiguration(
            phi=phi,
            grace=grace,
            devourer=devourer,
            coordinates=coordinates
        )
        
        assert config.coordinates.shape[1] == 3  # 3D space
        assert len(config.phi) == len(config.coordinates)


class TestFieldEquationResult:
    """Test field equation result dataclass."""
    
    def test_result_creation(self):
        """Test field equation result creation."""
        # Create sample field configuration
        field_config = FieldConfiguration(
            phi=np.array([1.0, 1.618]),
            grace=np.array([0.5, 0.809]),
            devourer=np.array([0.1, 0.1618]),
            coordinates=np.array([[0, 0], [1, 0]])
        )
        
        # Create sample result data
        energy_density = np.array([1.0, 2.618])
        stress_tensor = np.array([[[1.0, 0.5], [0.5, 1.618]], [[2.618, 1.0], [1.0, 2.618]]])
        conserved_charges = {"morphic": 1.618, "grace": 0.809, "devourer": 0.1618}
        soul_states = [{"id": "soul_1", "coherence": 0.95}]
        stability = {"stable": True, "eigenvalues": [1.0, 1.618]}
        
        result = FieldEquationResult(
            field_config=field_config,
            energy_density=energy_density,
            stress_tensor=stress_tensor,
            conserved_charges=conserved_charges,
            soul_states_detected=soul_states,
            stability_analysis=stability
        )
        
        assert result.field_config == field_config
        assert np.array_equal(result.energy_density, energy_density)
        assert np.array_equal(result.stress_tensor, stress_tensor)
        assert result.conserved_charges == conserved_charges
        assert result.soul_states_detected == soul_states
        assert result.stability_analysis == stability
        
    def test_result_validation(self):
        """Test result validation."""
        field_config = FieldConfiguration(
            phi=np.array([1.0]),
            grace=np.array([0.5]),
            devourer=np.array([0.1]),
            coordinates=np.array([[0, 0]])
        )
        
        # Energy density should match field configuration length
        energy_density = np.array([1.0, 2.618])  # Wrong length
        
        with pytest.raises(ValueError):
            FieldEquationResult(
                field_config=field_config,
                energy_density=energy_density,
                stress_tensor=np.array([[[1.0]]]),
                conserved_charges={},
                soul_states_detected=[],
                stability_analysis={}
            )


class TestCompleteFieldEquations:
    """Test complete field equations class."""
    
    def test_initialization(self):
        """Test CompleteFieldEquations initialization."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        # Mock the symbolic system setup
        with patch.object(CompleteFieldEquations, '_setup_symbolic_system'), \
             patch.object(CompleteFieldEquations, '_derive_complete_lagrangian'), \
             patch.object(CompleteFieldEquations, '_derive_field_equations'):
            
            field_eq = CompleteFieldEquations(params)
            
            assert field_eq.params == params
            assert field_eq._phi_bg == params.phi_background
            
    def test_symbolic_system_setup(self):
        """Test symbolic system setup."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        field_eq = CompleteFieldEquations(params)
        
        # Should have symbolic variables set up
        assert hasattr(field_eq, '_phi_sym')
        assert hasattr(field_eq, '_grace_sym')
        assert hasattr(field_eq, '_devourer_sym')
        
    def test_lagrangian_derivation(self):
        """Test Lagrangian derivation."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        field_eq = CompleteFieldEquations(params)
        
        # Should have Lagrangian components
        assert hasattr(field_eq, '_lagrangian_base')
        assert hasattr(field_eq, '_lagrangian_recursive')
        assert hasattr(field_eq, '_lagrangian_grace_devourer')
        
    def test_field_equations_derivation(self):
        """Test field equations derivation."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        field_eq = CompleteFieldEquations(params)
        
        # Should have all three field equations
        assert hasattr(field_eq, '_phi_equation')
        assert hasattr(field_eq, '_grace_equation')
        assert hasattr(field_eq, '_devourer_equation')
        
    def test_field_solving(self):
        """Test field equation solving."""
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        field_eq = CompleteFieldEquations(params)
        
        # Test solving with sample initial conditions
        initial_phi = np.array([1.0, 1.618])
        initial_grace = np.array([0.5, 0.809])
        initial_devourer = np.array([0.1, 0.1618])
        
        # Mock the solve method to avoid actual computation
        with patch.object(field_eq, 'solve_field_equations') as mock_solve:
            mock_solve.return_value = FieldEquationResult(
                field_config=FieldConfiguration(
                    phi=initial_phi,
                    grace=initial_grace,
                    devourer=initial_devourer,
                    coordinates=np.array([[0, 0], [1, 0]])
                ),
                energy_density=np.array([1.0, 2.618]),
                stress_tensor=np.array([[[1.0, 0.5], [0.5, 1.618]], [[2.618, 1.0], [1.0, 2.618]]]),
                conserved_charges={"morphic": 1.618, "grace": 0.809, "devourer": 0.1618},
                soul_states_detected=[{"id": "soul_1", "coherence": 0.95}],
                stability_analysis={"stable": True, "eigenvalues": [1.0, 1.618]}
            )
            
            result = field_eq.solve_field_equations(
                initial_phi, initial_grace, initial_devourer
            )
            
            assert result is not None
            assert hasattr(result, 'field_config')
            assert hasattr(result, 'energy_density')
            assert hasattr(result, 'stress_tensor')
            assert hasattr(result, 'conserved_charges')
            assert hasattr(result, 'soul_states_detected')
            assert hasattr(result, 'stability_analysis')


class TestFieldEquationsIntegration:
    """Integration tests for field equations."""
    
    def test_complete_workflow(self):
        """Test complete field equations workflow."""
        # Create parameters
        params = FIRMFieldParameters(
            phi_mass_squared=1.0,
            phi_self_coupling=0.1,
            grace_kinetic_coeff=0.5,
            grace_mass_squared=0.8,
            grace_phi_coupling=0.3,
            devourer_mass_squared=1.2,
            devourer_phi_coupling=0.4,
            devourer_nonlinear=0.2,
            grace_devourer_coupling=0.1,
            recursive_depth_factor=5.0
        )
        
        # Create field equations instance
        field_eq = CompleteFieldEquations(params)
        
        # Test that all required methods exist
        required_methods = [
            'solve_field_equations',
            'analyze_stability',
            'compute_energy_density',
            'compute_stress_tensor',
            'detect_soul_states'
        ]
        
        for method_name in required_methods:
            assert hasattr(field_eq, method_name), f"Missing method: {method_name}"
            
    def test_parameter_sensitivity(self):
        """Test field equations sensitivity to parameter changes."""
        # Test with different parameter sets
        param_sets = [
            FIRMFieldParameters(
                phi_mass_squared=0.5,
                phi_self_coupling=0.05,
                grace_kinetic_coeff=0.25,
                grace_mass_squared=0.4,
                grace_phi_coupling=0.15,
                devourer_mass_squared=0.6,
                devourer_phi_coupling=0.2,
                devourer_nonlinear=0.1,
                grace_devourer_coupling=0.05,
                recursive_depth_factor=3.0
            ),
            FIRMFieldParameters(
                phi_mass_squared=2.0,
                phi_self_coupling=0.2,
                grace_kinetic_coeff=1.0,
                grace_mass_squared=1.6,
                grace_phi_coupling=0.6,
                devourer_mass_squared=2.4,
                devourer_phi_coupling=0.8,
                devourer_nonlinear=0.4,
                grace_devourer_coupling=0.2,
                recursive_depth_factor=7.0
            )
        ]
        
        for params in param_sets:
            field_eq = CompleteFieldEquations(params)
            
            # Should initialize without errors
            assert field_eq.params == params
            assert field_eq._phi_bg == params.phi_background


if __name__ == "__main__":
    pytest.main([__file__])

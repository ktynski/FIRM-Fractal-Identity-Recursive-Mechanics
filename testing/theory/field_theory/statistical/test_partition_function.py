#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Partition Function

Tests the complete path integral and partition function for FIRM:
Z = ∫ Dφ D𝒢 DD e^(iS[φ,𝒢,D])

Tests all major classes:
- PathIntegralParameters
- PartitionFunctionResult
- FIRMPartitionFunction
"""

import pytest
import numpy as np
import math
from unittest.mock import Mock, patch

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Mock the dependencies
mock_phi_value = 1.618033988749895
mock_derivation_node = Mock()


class TestPathIntegralParameters:
    """Test path integral parameters dataclass."""
    
    def test_parameter_initialization(self):
        """Test parameter initialization with all required fields."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.statistical.partition_function import PathIntegralParameters
            
            params = PathIntegralParameters(
                spacetime_lattice_size=(16, 16, 16, 16),
                lattice_spacing=0.1,
                field_cutoff=10.0,
                momentum_cutoff=5.0,
                num_configurations=1000,
                thermalization_steps=500,
                temperature=1.0,
                morphic_chemical_potential=0.5,
                grace_chemical_potential=0.3,
                devourer_chemical_potential=0.2
            )
            
            assert params.spacetime_lattice_size == (16, 16, 16, 16)
            assert params.lattice_spacing == 0.1
            assert params.field_cutoff == 10.0
            assert params.momentum_cutoff == 5.0
            assert params.num_configurations == 1000
            assert params.thermalization_steps == 500
            assert params.temperature == 1.0
            assert params.morphic_chemical_potential == 0.5
            assert params.grace_chemical_potential == 0.3
            assert params.devourer_chemical_potential == 0.2
        
    def test_parameter_validation(self):
        """Test parameter validation and constraints."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.statistical.partition_function import PathIntegralParameters
            
            # All parameters should be valid
            params = PathIntegralParameters(
                spacetime_lattice_size=(8, 8, 8, 8),
                lattice_spacing=0.2,
                field_cutoff=5.0,
                momentum_cutoff=3.0,
                num_configurations=500,
                thermalization_steps=200,
                temperature=0.5,
                morphic_chemical_potential=0.3,
                grace_chemical_potential=0.2,
                devourer_chemical_potential=0.1
            )
            
            # Lattice size should be positive
            for size in params.spacetime_lattice_size:
                assert size > 0
            
            # Spacing and cutoffs should be positive
            assert params.lattice_spacing > 0
            assert params.field_cutoff > 0
            assert params.momentum_cutoff > 0
            
            # Configuration counts should be positive
            assert params.num_configurations > 0
            assert params.thermalization_steps > 0
            
            # Temperature should be positive
            assert params.temperature > 0


class TestPartitionFunctionResult:
    """Test partition function result dataclass."""
    
    def test_result_creation(self):
        """Test result creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.statistical.partition_function import PartitionFunctionResult
            
            # Create sample correlators
            phi_correlator = np.array([[1.0, 0.5], [0.5, 1.0]])
            grace_correlator = np.array([[0.8, 0.3], [0.3, 0.8]])
            mixed_correlators = {
                "phi_grace": np.array([[0.6, 0.2], [0.2, 0.6]]),
                "phi_devourer": np.array([[0.4, 0.1], [0.1, 0.4]])
            }
            
            psi_state_probabilities = {0: 0.4, 1: 0.35, 2: 0.25}
            phase_transition_points = [0.5, 1.2, 2.1]
            critical_exponents = {"nu": 0.63, "eta": 0.04, "gamma": 1.24}
            recursive_depth_distribution = np.array([0.3, 0.4, 0.2, 0.1])
            
            result = PartitionFunctionResult(
                log_partition_function=15.7,
                free_energy=-12.3,
                entropy=8.9,
                internal_energy=45.2,
                phi_expectation=1.618,
                grace_expectation=0.809,
                devourer_expectation=0.1618,
                phi_correlator=phi_correlator,
                grace_correlator=grace_correlator,
                mixed_correlators=mixed_correlators,
                psi_state_probabilities=psi_state_probabilities,
                phase_transition_points=phase_transition_points,
                critical_exponents=critical_exponents,
                grace_branching_entropy=2.5,
                devourer_shielding_probability=0.75,
                recursive_depth_distribution=recursive_depth_distribution
            )
            
            assert result.log_partition_function == 15.7
            assert result.free_energy == -12.3
            assert result.entropy == 8.9
            assert result.internal_energy == 45.2
            assert result.phi_expectation == 1.618
            assert result.grace_expectation == 0.809
            assert result.devourer_expectation == 0.1618
            assert np.array_equal(result.phi_correlator, phi_correlator)
            assert np.array_equal(result.grace_correlator, grace_correlator)
            assert result.mixed_correlators == mixed_correlators
            assert result.psi_state_probabilities == psi_state_probabilities
            assert result.phase_transition_points == phase_transition_points
            assert result.critical_exponents == critical_exponents
            assert result.grace_branching_entropy == 2.5
            assert result.devourer_shielding_probability == 0.75
            assert np.array_equal(result.recursive_depth_distribution, recursive_depth_distribution)
        
    def test_result_validation(self):
        """Test result parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.statistical.partition_function import PartitionFunctionResult
            
            # Create minimal result for testing
            result = PartitionFunctionResult(
                log_partition_function=10.0,
                free_energy=-8.0,
                entropy=5.0,
                internal_energy=30.0,
                phi_expectation=1.5,
                grace_expectation=0.7,
                devourer_expectation=0.15,
                phi_correlator=np.array([[1.0]]),
                grace_correlator=np.array([[0.8]]),
                mixed_correlators={},
                psi_state_probabilities={0: 1.0},
                phase_transition_points=[],
                critical_exponents={},
                grace_branching_entropy=2.0,
                devourer_shielding_probability=0.8,
                recursive_depth_distribution=np.array([1.0])
            )
            
            # Entropy should be positive
            assert result.entropy > 0
            
            # Shielding probability should be between 0 and 1
            assert 0 <= result.devourer_shielding_probability <= 1
            
            # Depth distribution should sum to approximately 1
            assert abs(np.sum(result.recursive_depth_distribution) - 1.0) < 0.1


class TestFIRMPartitionFunction:
    """Test FIRM partition function class."""
    
    def test_partition_function_initialization(self):
        """Test partition function initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            path_params = PathIntegralParameters(
                spacetime_lattice_size=(8, 8, 8, 8),
                lattice_spacing=0.2,
                field_cutoff=5.0,
                momentum_cutoff=3.0,
                num_configurations=500,
                thermalization_steps=200,
                temperature=0.5,
                morphic_chemical_potential=0.3,
                grace_chemical_potential=0.2,
                devourer_chemical_potential=0.1
            )
            
            partition_func = FIRMPartitionFunction(mock_field_params, path_params)
            
            assert partition_func.field_params == mock_field_params
            assert partition_func.path_params == path_params
            assert partition_func._phi_bg == mock_phi_value
        
    def test_lattice_setup(self):
        """Test lattice discretization setup."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            path_params = PathIntegralParameters(
                spacetime_lattice_size=(4, 4, 4, 4),
                lattice_spacing=0.5,
                field_cutoff=3.0,
                momentum_cutoff=2.0,
                num_configurations=100,
                thermalization_steps=50,
                temperature=1.0,
                morphic_chemical_potential=0.2,
                grace_chemical_potential=0.1,
                devourer_chemical_potential=0.05
            )
            
            partition_func = FIRMPartitionFunction(mock_field_params, path_params)
            
            # Should have lattice setup methods
            assert hasattr(partition_func, '_setup_lattice_discretization')
            assert hasattr(partition_func, '_setup_monte_carlo')
            assert hasattr(partition_func, '_setup_thermal_parameters')
        
    def test_path_integral_methods(self):
        """Test path integral computation methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            path_params = PathIntegralParameters(
                spacetime_lattice_size=(4, 4, 4, 4),
                lattice_spacing=0.5,
                field_cutoff=3.0,
                momentum_cutoff=2.0,
                num_configurations=100,
                thermalization_steps=50,
                temperature=1.0,
                morphic_chemical_potential=0.2,
                grace_chemical_potential=0.1,
                devourer_chemical_potential=0.05
            )
            
            partition_func = FIRMPartitionFunction(mock_field_params, path_params)
            
            # Should have path integral methods
            assert hasattr(partition_func, 'compute_partition_function')
            assert hasattr(partition_func, 'evaluate_path_integral')
            assert hasattr(partition_func, 'compute_correlation_functions')
            assert hasattr(partition_func, 'analyze_phase_transitions')
        
    def test_statistical_mechanics_methods(self):
        """Test statistical mechanics methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            path_params = PathIntegralParameters(
                spacetime_lattice_size=(4, 4, 4, 4),
                lattice_spacing=0.5,
                field_cutoff=3.0,
                momentum_cutoff=2.0,
                num_configurations=100,
                thermalization_steps=50,
                temperature=1.0,
                morphic_chemical_potential=0.2,
                grace_chemical_potential=0.1,
                devourer_chemical_potential=0.05
            )
            
            partition_func = FIRMPartitionFunction(mock_field_params, path_params)
            
            # Should have statistical mechanics methods
            assert hasattr(partition_func, 'compute_free_energy')
            assert hasattr(partition_func, 'compute_entropy')
            assert hasattr(partition_func, 'compute_internal_energy')
            assert hasattr(partition_func, 'compute_expectation_values')
        
    def test_soul_state_methods(self):
        """Test soul-state analysis methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            path_params = PathIntegralParameters(
                spacetime_lattice_size=(4, 4, 4, 4),
                lattice_spacing=0.5,
                field_cutoff=3.0,
                momentum_cutoff=2.0,
                num_configurations=100,
                thermalization_steps=50,
                temperature=1.0,
                morphic_chemical_potential=0.2,
                grace_chemical_potential=0.1,
                devourer_chemical_potential=0.05
            )
            
            partition_func = FIRMPartitionFunction(mock_field_params, path_params)
            
            # Should have soul-state analysis methods
            assert hasattr(partition_func, 'analyze_psi_states')
            assert hasattr(partition_func, 'compute_phase_entropy')
            assert hasattr(partition_func, 'analyze_grace_branching')
            assert hasattr(partition_func, 'compute_devourer_shielding')


class TestPartitionFunctionIntegration:
    """Integration tests for partition function."""
    
    def test_complete_workflow(self):
        """Test complete partition function workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            path_params = PathIntegralParameters(
                spacetime_lattice_size=(4, 4, 4, 4),
                lattice_spacing=0.5,
                field_cutoff=3.0,
                momentum_cutoff=2.0,
                num_configurations=100,
                thermalization_steps=50,
                temperature=1.0,
                morphic_chemical_potential=0.2,
                grace_chemical_potential=0.1,
                devourer_chemical_potential=0.05
            )
            
            partition_func = FIRMPartitionFunction(mock_field_params, path_params)
            
            # Test that all required methods exist
            required_methods = [
                'compute_partition_function',
                'evaluate_path_integral',
                'compute_correlation_functions',
                'analyze_phase_transitions',
                'compute_free_energy',
                'compute_entropy',
                'compute_internal_energy',
                'compute_expectation_values',
                'analyze_psi_states',
                'compute_phase_entropy',
                'analyze_grace_branching',
                'compute_devourer_shielding'
            ]
            
            for method_name in required_methods:
                assert hasattr(partition_func, method_name), f"Missing method: {method_name}"
    
    def test_parameter_sensitivity(self):
        """Test partition function sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            # Test with different lattice sizes
            for lattice_size in [(2, 2, 2, 2), (4, 4, 4, 4), (8, 8, 8, 8)]:
                path_params = PathIntegralParameters(
                    spacetime_lattice_size=lattice_size,
                    lattice_spacing=0.5,
                    field_cutoff=3.0,
                    momentum_cutoff=2.0,
                    num_configurations=100,
                    thermalization_steps=50,
                    temperature=1.0,
                    morphic_chemical_potential=0.2,
                    grace_chemical_potential=0.1,
                    devourer_chemical_potential=0.05
                )
                
                partition_func = FIRMPartitionFunction(mock_field_params, path_params)
                
                # Should initialize without errors
                assert partition_func.path_params.spacetime_lattice_size == lattice_size
                
                # Should have valid lattice setup
                assert partition_func.path_params.lattice_spacing > 0
                assert partition_func.path_params.field_cutoff > 0
                assert partition_func.path_params.momentum_cutoff > 0
    
    def test_numerical_stability(self):
        """Test numerical stability for various configurations."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('foundation.field_theory.complete_field_equations.FIRMFieldParameters') as mock_field_params:
            
            from theory.field_theory.statistical.partition_function import (
                PathIntegralParameters, 
                FIRMPartitionFunction
            )
            
            # Mock field parameters
            mock_field_params.phi_background = mock_phi_value
            
            # Test with different temperatures
            for temperature in [0.1, 0.5, 1.0, 2.0]:
                path_params = PathIntegralParameters(
                    spacetime_lattice_size=(4, 4, 4, 4),
                    lattice_spacing=0.5,
                    field_cutoff=3.0,
                    momentum_cutoff=2.0,
                    num_configurations=100,
                    thermalization_steps=50,
                    temperature=temperature,
                    morphic_chemical_potential=0.2,
                    grace_chemical_potential=0.1,
                    devourer_chemical_potential=0.05
                )
                
                partition_func = FIRMPartitionFunction(mock_field_params, path_params)
                
                # Should not raise errors for valid parameters
                assert partition_func.path_params.temperature == temperature
                assert partition_func.path_params.temperature > 0


if __name__ == "__main__":
    pytest.main([__file__])

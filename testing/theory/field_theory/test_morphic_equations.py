#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Morphic Field Equations

Tests the fundamental dynamics of FIRM/FIRM through the Euler-Lagrange equation:
0 = ∑_{r=1}^∞ [(-1)^r / r^d] * [2r φ^(2r-1) - r λ_r G φ^(r-1)] - ξ G D

Tests all major classes:
- MorphicFieldParameters
- MorphicFieldSolution
- MorphicFieldEquation
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


class TestMorphicFieldParameters:
    """Test morphic field parameters dataclass."""
    
    def test_parameter_initialization(self):
        """Test parameter initialization with all required fields."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters
            
            lambda_coeffs = {1: 0.1, 2: 0.05, 3: 0.025}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618,
                max_terms=50
            )
            
            assert params.d == 2.0
            assert params.xi == 0.3
            assert params.lambda_coefficients == lambda_coeffs
            assert params.grace_amplitude == 0.8
            assert params.devourer_amplitude == 0.2
            assert params.phi_background == 1.618
            assert params.max_terms == 50
        
    def test_default_max_terms(self):
        """Test default max_terms value."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters
            
            lambda_coeffs = {1: 0.1}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            # Should have default max_terms value
            assert hasattr(params, 'max_terms')
            assert params.max_terms == 50
        
    def test_parameter_validation(self):
        """Test parameter validation and constraints."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters
            
            lambda_coeffs = {1: 0.1, 2: 0.05}
            
            # All parameters should be valid
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            assert params.d > 0
            assert params.max_terms > 0
            assert len(params.lambda_coefficients) > 0


class TestMorphicFieldSolution:
    """Test morphic field solution dataclass."""
    
    def test_solution_creation(self):
        """Test solution creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldSolution
            
            solution = MorphicFieldSolution(
                phi_value=1.618,
                field_equation_residual=1e-12,
                energy_density=2.5,
                grace_term=0.8,
                devourer_term=0.2,
                recursive_potential=1.5,
                convergence_achieved=True,
                mathematical_justification="Numerical solution with fsolve"
            )
            
            assert solution.phi_value == 1.618
            assert solution.field_equation_residual == 1e-12
            assert solution.energy_density == 2.5
            assert solution.grace_term == 0.8
            assert solution.devourer_term == 0.2
            assert solution.recursive_potential == 1.5
            assert solution.convergence_achieved is True
            assert solution.mathematical_justification == "Numerical solution with fsolve"
        
    def test_solution_validation(self):
        """Test solution parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldSolution
            
            solution = MorphicFieldSolution(
                phi_value=1.618,
                field_equation_residual=1e-12,
                energy_density=2.5,
                grace_term=0.8,
                devourer_term=0.2,
                recursive_potential=1.5,
                convergence_achieved=True,
                mathematical_justification="Test solution"
            )
            
            # Residual should be small for good solution
            assert abs(solution.field_equation_residual) < 1e-6
            
            # Energy density should be positive
            assert solution.energy_density > 0


class TestMorphicFieldEquation:
    """Test morphic field equation class."""
    
    def test_equation_initialization(self):
        """Test equation initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            lambda_coeffs = {1: 0.1, 2: 0.05, 3: 0.025}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            equation = MorphicFieldEquation(params)
            
            assert equation.params == params
            assert equation._phi == mock_phi_value
        
    def test_parameter_validation(self):
        """Test parameter validation in initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            lambda_coeffs = {1: 0.1}
            
            # Test invalid scaling dimension
            with pytest.raises(ValueError, match="Scaling dimension d must be positive"):
                invalid_params = MorphicFieldParameters(
                    d=0.0,  # Invalid: non-positive
                    xi=0.3,
                    lambda_coefficients=lambda_coeffs,
                    grace_amplitude=0.8,
                    devourer_amplitude=0.2,
                    phi_background=1.618
                )
                MorphicFieldEquation(invalid_params)
            
            # Test invalid max_terms
            with pytest.raises(ValueError, match="max_terms must be positive"):
                invalid_params = MorphicFieldParameters(
                    d=2.0,
                    xi=0.3,
                    lambda_coefficients=lambda_coeffs,
                    grace_amplitude=0.8,
                    devourer_amplitude=0.2,
                    phi_background=1.618,
                    max_terms=0  # Invalid: non-positive
                )
                MorphicFieldEquation(invalid_params)
            
            # Test empty lambda coefficients
            with pytest.raises(ValueError, match="lambda_coefficients cannot be empty"):
                invalid_params = MorphicFieldParameters(
                    d=2.0,
                    xi=0.3,
                    lambda_coefficients={},  # Invalid: empty
                    grace_amplitude=0.8,
                    devourer_amplitude=0.2,
                    phi_background=1.618
                )
                MorphicFieldEquation(invalid_params)
        
    def test_recursive_potential_term_computation(self):
        """Test recursive potential term computation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            lambda_coeffs = {1: 0.1, 2: 0.05}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            equation = MorphicFieldEquation(params)
            
            # Test term computation for r=1
            term1 = equation._compute_recursive_potential_term(1.0, 1)
            assert isinstance(term1, float)
            
            # Test term computation for r=2
            term2 = equation._compute_recursive_potential_term(1.0, 2)
            assert isinstance(term2, float)
            
            # Test term computation for r not in lambda_coefficients
            term3 = equation._compute_recursive_potential_term(1.0, 5)
            assert term3 == 0.0
        
    def test_field_equation_evaluation(self):
        """Test field equation evaluation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            lambda_coeffs = {1: 0.1, 2: 0.05}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618,
                max_terms=10  # Smaller for testing
            )
            
            equation = MorphicFieldEquation(params)
            
            # Test evaluation at phi = 1.0
            result = equation._evaluate_field_equation(1.0)
            assert isinstance(result, float)
            
            # Test evaluation at phi = 1.618 (golden ratio)
            result_golden = equation._evaluate_field_equation(1.618)
            assert isinstance(result_golden, float)
        
    def test_energy_density_computation(self):
        """Test energy density computation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            lambda_coeffs = {1: 0.1, 2: 0.05}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            equation = MorphicFieldEquation(params)
            
            # Test energy density at phi = 1.0
            energy1 = equation._compute_energy_density(1.0)
            assert isinstance(energy1, float)
            assert energy1 > 0  # Energy should be positive
            
            # Test energy density at phi = 1.618 (background)
            energy_background = equation._compute_energy_density(1.618)
            assert isinstance(energy_background, float)
            assert energy_background >= 0  # Background should have minimal energy
        
    def test_field_equation_solving(self):
        """Test field equation solving."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('scipy.optimize.fsolve') as mock_fsolve:
            
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            lambda_coeffs = {1: 0.1, 2: 0.05}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            equation = MorphicFieldEquation(params)
            
            # Mock fsolve to return a solution
            mock_fsolve.return_value = (np.array([1.618]), {'nfev': 5, 'success': True})
            
            # Test solving with default initial guess
            solution = equation.solve_field_equation()
            
            assert solution is not None
            assert hasattr(solution, 'phi_value')
            assert hasattr(solution, 'field_equation_residual')
            assert hasattr(solution, 'energy_density')
            assert hasattr(solution, 'convergence_achieved')
            
            # Test solving with custom initial guess
            solution_custom = equation.solve_field_equation(initial_guess=1.5)
            assert solution_custom is not None
        
    def test_numerical_stability(self):
        """Test numerical stability for various parameter ranges."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.morphic_equations import MorphicFieldParameters, MorphicFieldEquation
            
            # Test with different scaling dimensions
            for d in [1.0, 2.0, 3.0]:
                lambda_coeffs = {1: 0.1, 2: 0.05}
                
                params = MorphicFieldParameters(
                    d=d,
                    xi=0.3,
                    lambda_coefficients=lambda_coeffs,
                    grace_amplitude=0.8,
                    devourer_amplitude=0.2,
                    phi_background=1.618
                )
                
                equation = MorphicFieldEquation(params)
                
                # Should not raise errors for valid parameters
                assert equation.params.d == d
                
                # Test term computation for various phi values
                for phi in [0.5, 1.0, 1.618, 2.0]:
                    term = equation._compute_recursive_potential_term(phi, 1)
                    assert isinstance(term, float)
                    assert not np.isnan(term)
                    assert not np.isinf(term)


class TestMorphicEquationsIntegration:
    """Integration tests for morphic equations."""
    
    def test_complete_workflow(self):
        """Test complete morphic equations workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value), \
             patch('scipy.optimize.fsolve') as mock_fsolve:
            
            from theory.field_theory.morphic_equations import (
                MorphicFieldParameters, 
                MorphicFieldEquation,
                MorphicFieldSolution
            )
            
            # Create parameters
            lambda_coeffs = {1: 0.1, 2: 0.05, 3: 0.025}
            
            params = MorphicFieldParameters(
                d=2.0,
                xi=0.3,
                lambda_coefficients=lambda_coeffs,
                grace_amplitude=0.8,
                devourer_amplitude=0.2,
                phi_background=1.618
            )
            
            # Create equation instance
            equation = MorphicFieldEquation(params)
            
            # Mock fsolve to return a solution
            mock_fsolve.return_value = (np.array([1.618]), {'nfev': 5, 'success': True})
            
            # Test that all required methods exist
            required_methods = [
                '_compute_recursive_potential_term',
                '_evaluate_field_equation',
                '_compute_energy_density',
                'solve_field_equation'
            ]
            
            for method_name in required_methods:
                assert hasattr(equation, method_name), f"Missing method: {method_name}"
            
            # Test parameter sensitivity
            param_sets = [
                MorphicFieldParameters(
                    d=1.5,
                    xi=0.2,
                    lambda_coefficients={1: 0.08, 2: 0.04},
                    grace_amplitude=0.6,
                    devourer_amplitude=0.15,
                    phi_background=1.618
                ),
                MorphicFieldParameters(
                    d=2.5,
                    xi=0.4,
                    lambda_coefficients={1: 0.12, 2: 0.06, 3: 0.03},
                    grace_amplitude=1.0,
                    devourer_amplitude=0.25,
                    phi_background=1.618
                )
            ]
            
            for param_set in param_sets:
                equation_set = MorphicFieldEquation(param_set)
                
                # Should initialize without errors
                assert equation_set.params == param_set
                assert equation_set._phi == mock_phi_value
                
                # Should be able to compute terms
                term = equation_set._compute_recursive_potential_term(1.0, 1)
                assert isinstance(term, float)


if __name__ == "__main__":
    pytest.main([__file__])

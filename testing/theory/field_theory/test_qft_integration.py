#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Quantum Field Theory Integration

Tests the complete reformulation of quantum field theory using φ-recursive 
morphism densities over echo shells, replacing canonical quantization with 
fractal morphism lattices.

Tests all major classes:
- MorphicField
- FractalPropagator
- PhiRecursiveQFT
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


class TestMorphicField:
    """Test morphic field dataclass."""
    
    def test_field_creation(self):
        """Test morphic field creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import MorphicField
            
            shell_amplitudes = {0: 1.0+0j, 1: 0.5+0.3j, 2: 0.2+0.1j}
            k_scales = {0: 1.0, 1: 1.618, 2: 2.618}
            
            field = MorphicField(
                name="test_field",
                shell_amplitudes=shell_amplitudes,
                k_scales=k_scales,
                base_scale=1.0,
                max_shells=3
            )
            
            assert field.name == "test_field"
            assert field.shell_amplitudes == shell_amplitudes
            assert field.k_scales == k_scales
            assert field.base_scale == 1.0
            assert field.max_shells == 3
        
    def test_position_evaluation(self):
        """Test field evaluation at position."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import MorphicField
            
            shell_amplitudes = {0: 1.0+0j, 1: 0.5+0j}
            k_scales = {0: 1.0, 1: 1.618}
            
            field = MorphicField(
                name="test_field",
                shell_amplitudes=shell_amplitudes,
                k_scales=k_scales,
                base_scale=1.0,
                max_shells=2
            )
            
            # Test evaluation at origin
            x_origin = np.array([0.0, 0.0])
            result_origin = field.evaluate_at_position(x_origin)
            
            assert isinstance(result_origin, complex)
            assert abs(result_origin) > 0  # Should have non-zero amplitude
            
            # Test evaluation at non-zero position
            x_pos = np.array([1.0, 0.0])
            result_pos = field.evaluate_at_position(x_pos)
            
            assert isinstance(result_pos, complex)
            assert result_pos != result_origin  # Should be different from origin
        
    def test_commutator_delay(self):
        """Test morphic commutation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import MorphicField
            
            field1 = MorphicField(
                name="field1",
                shell_amplitudes={0: 1.0+0j},
                k_scales={0: 1.0},
                base_scale=1.0,
                max_shells=1
            )
            
            field2 = MorphicField(
                name="field2",
                shell_amplitudes={0: 1.0+0j},
                k_scales={0: 1.0},
                base_scale=1.0,
                max_shells=1
            )
            
            # Test commutator for delta_n = 0
            comm_0 = field1.commutator_delay(field2, 0)
            assert comm_0 == 1.0  # φ^0 = 1
            
            # Test commutator for delta_n = 1
            comm_1 = field1.commutator_delay(field2, 1)
            assert abs(comm_1 - mock_phi_value) < 1e-10  # φ^1 = φ
            
            # Test commutator for delta_n = 2
            comm_2 = field1.commutator_delay(field2, 2)
            expected_2 = mock_phi_value ** 2
            assert abs(comm_2 - expected_2) < 1e-10  # φ^2


class TestFractalPropagator:
    """Test fractal propagator dataclass."""
    
    def test_propagator_creation(self):
        """Test fractal propagator creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import FractalPropagator
            
            shell_coefficients = {0: 1.0, 1: 0.5, 2: 0.2}
            k_scales = {0: 1.0, 1: 1.618, 2: 2.618}
            
            propagator = FractalPropagator(
                name="test_propagator",
                shell_coefficients=shell_coefficients,
                k_scales=k_scales,
                max_shells=3
            )
            
            assert propagator.name == "test_propagator"
            assert propagator.shell_coefficients == shell_coefficients
            assert propagator.k_scales == k_scales
            assert propagator.max_shells == 3
        
    def test_propagator_evaluation(self):
        """Test propagator evaluation at separation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import FractalPropagator
            
            shell_coefficients = {0: 1.0, 1: 0.5}
            k_scales = {0: 1.0, 1: 1.618}
            
            propagator = FractalPropagator(
                name="test_propagator",
                shell_coefficients=shell_coefficients,
                k_scales=k_scales,
                max_shells=2
            )
            
            # Test evaluation at zero separation
            sep_zero = np.array([0.0, 0.0])
            result_zero = propagator.evaluate(sep_zero)
            
            assert isinstance(result_zero, float)
            assert result_zero > 0  # Should be positive at zero separation
            
            # Test evaluation at non-zero separation
            sep_pos = np.array([1.0, 0.0])
            result_pos = propagator.evaluate(sep_pos)
            
            assert isinstance(result_pos, float)
            assert result_pos != result_zero  # Should be different from zero separation
        
    def test_propagator_scaling(self):
        """Test propagator φ-scaling behavior."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import FractalPropagator
            
            shell_coefficients = {0: 1.0, 1: 0.5, 2: 0.2}
            k_scales = {0: 1.0, 1: 1.618, 2: 2.618}
            
            propagator = FractalPropagator(
                name="test_propagator",
                shell_coefficients=shell_coefficients,
                k_scales=k_scales,
                max_shells=3
            )
            
            # Test that higher shells contribute with φ-scaling
            sep = np.array([0.5, 0.0])
            result = propagator.evaluate(sep)
            
            assert isinstance(result, float)
            assert result > 0  # Should be positive


class TestPhiRecursiveQFT:
    """Test φ-recursive QFT framework."""
    
    def test_qft_initialization(self):
        """Test QFT framework initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import PhiRecursiveQFT
            
            qft = PhiRecursiveQFT()
            
            assert qft._phi == mock_phi_value
            assert qft._hbar_phi == 1.0 / (mock_phi_value ** 3)
            assert qft._max_shells == 10
            assert qft._base_scale == 1.0
        
    def test_morphic_field_creation(self):
        """Test morphic field creation with different profiles."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import PhiRecursiveQFT
            
            qft = PhiRecursiveQFT()
            
            # Test exponential profile
            field_exp = qft.create_morphic_field("exponential", "exponential")
            assert field_exp.name == "exponential"
            assert field_exp.max_shells == 10
            assert len(field_exp.shell_amplitudes) > 0
            assert len(field_exp.k_scales) > 0
            
            # Test phi-damped profile
            field_phi = qft.create_morphic_field("phi_damped", "phi_damped")
            assert field_phi.name == "phi_damped"
            assert field_phi.max_shells == 10
            assert len(field_phi.shell_amplitudes) > 0
            assert len(field_phi.k_scales) > 0
            
            # Test coherence-weighted profile
            field_coherence = qft.create_morphic_field("coherence", "coherence_weighted")
            assert field_coherence.name == "coherence"
            assert field_coherence.max_shells == 10
            assert len(field_coherence.shell_amplitudes) > 0
            assert len(field_coherence.k_scales) > 0
        
    def test_shell_scaling(self):
        """Test φ-scaling of shell wavenumbers."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import PhiRecursiveQFT
            
            qft = PhiRecursiveQFT()
            field = qft.create_morphic_field("test", "exponential")
            
            # Test that k_scales follow φ^n scaling
            for n in range(min(5, field.max_shells)):
                if n in field.k_scales:
                    expected_k = qft._base_scale * (mock_phi_value ** n)
                    assert abs(field.k_scales[n] - expected_k) < 1e-10
        
    def test_amplitude_profiles(self):
        """Test different amplitude profile behaviors."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import PhiRecursiveQFT
            
            qft = PhiRecursiveQFT()
            
            # Test exponential profile decay
            field_exp = qft.create_morphic_field("exponential", "exponential")
            if 0 in field_exp.shell_amplitudes and 1 in field_exp.shell_amplitudes:
                amp_0 = abs(field_exp.shell_amplitudes[0])
                amp_1 = abs(field_exp.shell_amplitudes[1])
                assert amp_0 > amp_1  # Should decay with shell number
            
            # Test phi-damped profile
            field_phi = qft.create_morphic_field("phi_damped", "phi_damped")
            if 0 in field_phi.shell_amplitudes and 1 in field_phi.shell_amplitudes:
                amp_0 = abs(field_phi.shell_amplitudes[0])
                amp_1 = abs(field_phi.shell_amplitudes[1])
                expected_ratio = mock_phi_value
                actual_ratio = amp_0 / amp_1
                assert abs(actual_ratio - expected_ratio) < 0.1  # Approximate φ-scaling


class TestQFTIntegration:
    """Integration tests for QFT framework."""
    
    def test_complete_workflow(self):
        """Test complete QFT workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import (
                PhiRecursiveQFT, 
                MorphicField, 
                FractalPropagator
            )
            
            # Create QFT framework
            qft = PhiRecursiveQFT()
            
            # Create morphic field
            field = qft.create_morphic_field("test_field", "exponential")
            
            # Test field evaluation
            x = np.array([1.0, 0.0])
            field_value = field.evaluate_at_position(x)
            assert isinstance(field_value, complex)
            
            # Test commutator
            comm = field.commutator_delay(field, 1)
            assert abs(comm - mock_phi_value) < 1e-10
            
            # Test that all required methods exist
            required_methods = [
                'create_morphic_field',
                'create_fractal_propagator',
                'compute_scattering_amplitude',
                'evaluate_feynman_diagram'
            ]
            
            for method_name in required_methods:
                assert hasattr(qft, method_name), f"Missing method: {method_name}"
    
    def test_parameter_sensitivity(self):
        """Test QFT sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import PhiRecursiveQFT
            
            # Test with different base scales
            for base_scale in [0.5, 1.0, 2.0]:
                qft = PhiRecursiveQFT()
                qft._base_scale = base_scale
                
                field = qft.create_morphic_field("test", "exponential")
                
                # Should initialize without errors
                assert field.base_scale == base_scale
                
                # Should have correct k-scaling
                if 0 in field.k_scales:
                    assert abs(field.k_scales[0] - base_scale) < 1e-10
    
    def test_numerical_stability(self):
        """Test numerical stability for various configurations."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.qft_integration import PhiRecursiveQFT
            
            qft = PhiRecursiveQFT()
            
            # Test with different shell counts
            for max_shells in [5, 10, 15]:
                qft._max_shells = max_shells
                
                field = qft.create_morphic_field("test", "exponential")
                
                # Should not raise errors for valid parameters
                assert field.max_shells == max_shells
                
                # Should be able to evaluate at various positions
                for x_val in [0.0, 0.5, 1.0, 2.0]:
                    x = np.array([x_val, 0.0])
                    result = field.evaluate_at_position(x)
                    
                    assert isinstance(result, complex)
                    assert not np.isnan(result.real)
                    assert not np.isnan(result.imag)
                    assert not np.isinf(result.real)
                    assert not np.isinf(result.imag)


if __name__ == "__main__":
    pytest.main([__file__])

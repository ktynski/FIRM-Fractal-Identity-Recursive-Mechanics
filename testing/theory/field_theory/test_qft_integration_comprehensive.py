#!/usr/bin/env python3
"""
Simplified Tests for QFT Integration Module

Tests the actual classes that exist in the qft_integration module:
- MorphicField
- FractalPropagator  
- PhiRecursiveQFT
"""

import pytest
import numpy as np
import math
from typing import Dict, List, Optional, Tuple

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from theory.field_theory.qft_integration import (
    MorphicField,
    FractalPropagator,
    PhiRecursiveQFT,
)
from foundation.operators.phi_recursion import PHI_VALUE


class TestMorphicFieldBasics:
    """Test basic morphic field functionality."""
    
    def test_morphic_field_creation(self):
        """Test MorphicField creation and basic properties."""
        field = MorphicField(
            name="test_field",
            shell_amplitudes={0: 1.0+0j, 1: 0.5+0j, 2: 0.25+0j},
            k_scales={0: 1.0, 1: PHI_VALUE, 2: PHI_VALUE**2},
            base_scale=1.0,
            max_shells=3
        )
        
        assert field.name == "test_field"
        assert field.base_scale == 1.0
        assert field.max_shells == 3
        assert len(field.shell_amplitudes) == 3
        assert len(field.k_scales) == 3
        
    def test_field_evaluation_at_origin(self):
        """Test field evaluation at origin position."""
        field = MorphicField(
            name="origin_test",
            shell_amplitudes={0: 1.0+0j, 1: 0.5+0j},
            k_scales={0: 0.0, 1: 0.0},  # Zero wavenumbers
            base_scale=1.0,
            max_shells=2
        )
        
        origin = np.array([0.0, 0.0, 0.0])
        result = field.evaluate_at_position(origin)
        
        # At origin with zero k: F(0) = Σ_n φ^n A_n = 1.0 + φ*0.5
        expected = 1.0 + PHI_VALUE * 0.5
        assert abs(result - expected) < 1e-12


class TestFractalPropagator:
    """Test fractal propagator functionality."""
    
    def test_propagator_creation(self):
        """Test FractalPropagator creation and properties."""
        prop = FractalPropagator(
            name="test_propagator",
            shell_coefficients={0: 1.0, 1: 0.5},
            k_scales={0: 1.0, 1: PHI_VALUE},
            max_shells=2
        )
        
        assert prop.name == "test_propagator"
        assert prop.max_shells == 2
        assert 0 in prop.shell_coefficients
        assert 1 in prop.k_scales
        
    def test_propagator_calculation(self):
        """Test propagator amplitude calculation."""
        prop = FractalPropagator(
            name="test_prop",
            shell_coefficients={0: 1.0, 1: 0.5},
            k_scales={0: 1.0, 1: PHI_VALUE},
            max_shells=2
        )
        
        # Test propagator evaluation at zero separation
        amplitude = prop.evaluate(np.array([0.0, 0.0, 0.0]))
        assert isinstance(amplitude, float)
        assert abs(amplitude) > 0  # Should have non-zero amplitude


class TestPhiRecursiveQFT:
    """Test phi-recursive QFT system."""
    
    def test_qft_creation(self):
        """Test PhiRecursiveQFT creation."""
        qft = PhiRecursiveQFT()
        
        assert hasattr(qft, '_phi')
        assert hasattr(qft, '_hbar_phi')
        assert hasattr(qft, '_max_shells')
        assert hasattr(qft, '_base_scale')
        
    def test_qft_basic_functionality(self):
        """Test basic QFT functionality."""
        qft = PhiRecursiveQFT()
        
        # Test that the QFT system can be created and has basic attributes
        assert hasattr(qft, '_phi')
        assert hasattr(qft, '_max_shells')
        assert hasattr(qft, '_base_scale')
        
        # Test that it can create morphic fields
        field = qft.create_morphic_field("test_field")
        assert field.name == "test_field"
        assert hasattr(field, 'shell_amplitudes')
        assert hasattr(field, 'k_scales')

#!/usr/bin/env python3
"""
Tests for FIRM Complete Volitional Framework

Tests the volitional field ||𝒱ₙ|| across φ-recursive phases.
"""

import pytest
import numpy as np
from unittest.mock import Mock, patch

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

mock_phi_value = 1.618033988749895


class TestVolitionalPhase:
    """Test volitional phase enumeration."""
    
    def test_volitional_phases(self):
        """Test all volitional phases are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.volitional.complete_framework import VolitionalPhase
            
            phases = list(VolitionalPhase)
            assert len(phases) == 13
            
            # Test key phases
            assert VolitionalPhase.EX_NIHILO.value == "ex_nihilo"
            assert VolitionalPhase.GRACE_SEEDING.value == "grace_seeding"
            assert VolitionalPhase.COSMOLOGICAL.value == "cosmological"


class TestPhysicalConstant:
    """Test physical constant enumeration."""
    
    def test_physical_constants(self):
        """Test all physical constants are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.volitional.complete_framework import PhysicalConstant
            
            constants = list(PhysicalConstant)
            assert len(constants) == 8
            
            # Test key constants
            assert PhysicalConstant.FINE_STRUCTURE.value == "fine_structure_alpha"
            assert PhysicalConstant.PLANCK_CONSTANT.value == "planck_constant"


class TestVolitionalField:
    """Test volitional field ||𝒱ₙ||."""
    
    def test_volitional_field_creation(self):
        """Test VolitionalField creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.volitional.complete_framework import VolitionalField
            
            field = VolitionalField(
                field_id="field_001",
                recursion_depth=5,
                field_magnitude=11.09,
                morphic_potential=np.array([0.9, 0.7, 0.5]),
                coherence_alignment=np.array([0.8, 0.6, 0.4]),
                volitional_charge=1.618
            )
            
            assert field.field_id == "field_001"
            assert field.recursion_depth == 5
            assert field.field_magnitude == 11.09
            assert field.volitional_charge == 1.618


if __name__ == "__main__":
    pytest.main([__file__])

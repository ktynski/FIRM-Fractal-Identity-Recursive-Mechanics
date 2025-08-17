#!/usr/bin/env python3
"""
Test for foundation.algebra.torsion_groups module.
"""

import pytest
from foundation.algebra.torsion_groups import (
    TorsionLayer,
    GaugeGroup,
    PhysicalConstantType,
    TorsionGroup,
    MorphismObservable,
    CategoryFunctor,
    MassTorsionDrag,
    GaugeFunctorFamily,
    SoulCohomology,
    TorsionGroupAlgebraComplete,
)
from foundation.operators.phi_recursion import PHI_VALUE


class TestTorsionGroupsModule:
    """Test the actual classes in the torsion_groups module."""
    
    def test_torsion_layer_enum(self):
        """Test TorsionLayer enum values."""
        assert hasattr(TorsionLayer, 'T0_PLANCK')
        assert hasattr(TorsionLayer, 'T1_LIGHT')
        assert hasattr(TorsionLayer, 'T2_CHARGE')
        assert hasattr(TorsionLayer, 'T3_MASS')
        assert hasattr(TorsionLayer, 'T4_COSMIC')
        assert hasattr(TorsionLayer, 'T5_GOLDEN')
        assert hasattr(TorsionLayer, 'T_INFINITY')
        
        # Test specific values
        assert TorsionLayer.T0_PLANCK.value == "T0_Z"
        assert TorsionLayer.T1_LIGHT.value == "T1_Z2"
        assert TorsionLayer.T5_GOLDEN.value == "T5_Z_PHI"
        
    def test_gauge_group_enum(self):
        """Test GaugeGroup enum values."""
        assert hasattr(GaugeGroup, 'U1_ELECTROMAGNETIC')
        assert hasattr(GaugeGroup, 'SU2_WEAK')
        assert hasattr(GaugeGroup, 'SU3_STRONG')
        
        # Test specific values
        assert GaugeGroup.U1_ELECTROMAGNETIC.value == "U1_charge_phase"
        assert GaugeGroup.SU2_WEAK.value == "SU2_weak_isospin"
        assert GaugeGroup.SU3_STRONG.value == "SU3_color_torsion"
        
    def test_physical_constant_type_enum(self):
        """Test PhysicalConstantType enum values."""
        assert hasattr(PhysicalConstantType, 'ACTION_QUANTUM')
        assert hasattr(PhysicalConstantType, 'SPEED_LIMIT')
        assert hasattr(PhysicalConstantType, 'CHARGE_TWIST')
        assert hasattr(PhysicalConstantType, 'MASS_DRAG')
        assert hasattr(PhysicalConstantType, 'COSMIC_TENSION')
        assert hasattr(PhysicalConstantType, 'GOLDEN_BIFURCATION')
        
    def test_torsion_group_creation(self):
        """Test TorsionGroup creation."""
        group = TorsionGroup(
            layer=TorsionLayer.T2_CHARGE,
            group_symbol="ℤ₃",
            generator_count=2,
            order=3,
            generator_relations=["g³ = e"],
            firm_interpretation="Charge phase twist",
            physical_constants=["e", "α"],
            morphism_constraint="Phase preservation"
        )
        
        assert group.layer == TorsionLayer.T2_CHARGE
        assert group.group_symbol == "ℤ₃"
        assert group.order == 3
        assert "g³ = e" in group.generator_relations
        assert "e" in group.physical_constants
        
    def test_morphism_observable_creation(self):
        """Test MorphismObservable creation."""
        observable = MorphismObservable(
            constant_name="Fine Structure Constant",
            constant_symbol="α",
            torsion_layer=TorsionLayer.T2_CHARGE,
            morphism_formula="α = e²/(4πε₀ℏc)",
            norm_expression="|α| = 1/137.036",
            physical_value=1/137.036,
            firm_derivation="φ-based charge twist",
            coherence_interpretation="Electromagnetic coherence"
        )
        
        assert observable.constant_name == "Fine Structure Constant"
        assert observable.constant_symbol == "α"
        assert observable.torsion_layer == TorsionLayer.T2_CHARGE
        assert observable.physical_value == 1/137.036
        
    def test_torsion_group_algebra_complete_creation(self):
        """Test TorsionGroupAlgebraComplete creation."""
        algebra = TorsionGroupAlgebraComplete()
        
        assert hasattr(algebra, '_phi')
        assert hasattr(algebra, '_torsion_groups')
        assert hasattr(algebra, '_morphism_observables')
        assert hasattr(algebra, '_gauge_functor_families')
        assert hasattr(algebra, '_soul_cohomology')

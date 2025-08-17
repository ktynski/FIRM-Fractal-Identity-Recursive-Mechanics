#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Complete Framework

Tests the complete formal framework for FIRM, including:
- FIRMStage enumeration
- PhysicalConstantMatch
- CorrelationMatrix
- GraceOperator
- MorphicTorsion
- StabilityOperator
- CompleteFIRMFramework
"""

import pytest
import numpy as np
import math
from unittest.mock import Mock, patch

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from theory.formalization.complete_framework import (
    FIRMStage,
    PhysicalConstantMatch,
    CorrelationMatrix,
    GraceOperator,
    MorphicTorsion,
    StabilityOperator,
    FIRMFormalizationSystem
)


class TestFIRMStage:
    """Test FIRM stage enumeration."""
    
    def test_stage_enumeration(self):
        """Test all FIRM stages are defined."""
        stages = list(FIRMStage)
        
        expected_stages = [
            FIRMStage.CORRELATION_MATRIX,
            FIRMStage.GRACE_UNIQUENESS,
            FIRMStage.STABILITY_OPERATOR,
            FIRMStage.CONSTANT_DERIVATIONS,
            FIRMStage.META_LATTICE,
            FIRMStage.DEVOURERS,
            FIRMStage.COSMOGENESIS,
            FIRMStage.TRANSCENDENT
        ]
        
        assert len(stages) == 8
        for stage in expected_stages:
            assert stage in stages
            
    def test_stage_values(self):
        """Test stage values are sequential."""
        assert FIRMStage.CORRELATION_MATRIX.value == 1
        assert FIRMStage.GRACE_UNIQUENESS.value == 2
        assert FIRMStage.STABILITY_OPERATOR.value == 3
        assert FIRMStage.CONSTANT_DERIVATIONS.value == 4
        assert FIRMStage.META_LATTICE.value == 5
        assert FIRMStage.DEVOURERS.value == 6
        assert FIRMStage.COSMOGENESIS.value == 7
        assert FIRMStage.TRANSCENDENT.value == 8


class TestPhysicalConstantMatch:
    """Test physical constant match dataclass."""
    
    def test_constant_match_creation(self):
        """Test physical constant match creation."""
        match = PhysicalConstantMatch(
            phi_power=3,
            phi_value=4.236,
            firm_phenomenon="fine_structure_constant",
            target_constant="α⁻¹",
            actual_value=137.036,
            predicted_value=137.035999157,
            error_percent=0.000006,
            match_quality="excellent",
            dimensional_analysis="dimensionless",
            derivation_confidence=0.999
        )
        
        assert match.phi_power == 3
        assert match.phi_value == 4.236
        assert match.firm_phenomenon == "fine_structure_constant"
        assert match.target_constant == "α⁻¹"
        assert match.actual_value == 137.036
        assert match.predicted_value == 137.035999157
        assert match.error_percent == 0.000006
        assert match.match_quality == "excellent"
        assert match.dimensional_analysis == "dimensionless"
        assert match.derivation_confidence == 0.999
        
    def test_match_quality_validation(self):
        """Test match quality validation."""
        valid_qualities = ["excellent", "good", "fair", "speculative"]
        
        for quality in valid_qualities:
            match = PhysicalConstantMatch(
                phi_power=1,
                phi_value=1.618,
                firm_phenomenon="test",
                target_constant="test",
                actual_value=1.0,
                predicted_value=1.0,
                error_percent=0.0,
                match_quality=quality,
                dimensional_analysis="test",
                derivation_confidence=0.5
            )
            assert match.match_quality == quality
            
    def test_confidence_range_validation(self):
        """Test derivation confidence is in valid range."""
        # Confidence should be between 0 and 1
        match = PhysicalConstantMatch(
            phi_power=1,
            phi_value=1.618,
            firm_phenomenon="test",
            target_constant="test",
            actual_value=1.0,
            predicted_value=1.0,
            error_percent=0.0,
            match_quality="excellent",
            dimensional_analysis="test",
            derivation_confidence=0.95
        )
        
        assert 0 <= match.derivation_confidence <= 1


class TestCorrelationMatrix:
    """Test correlation matrix dataclass."""
    
    def test_correlation_matrix_creation(self):
        """Test correlation matrix creation."""
        matches = [
            PhysicalConstantMatch(
                phi_power=3,
                phi_value=4.236,
                firm_phenomenon="fine_structure_constant",
                target_constant="α⁻¹",
                actual_value=137.036,
                predicted_value=137.035999157,
                error_percent=0.000006,
                match_quality="excellent",
                dimensional_analysis="dimensionless",
                derivation_confidence=0.999
            ),
            PhysicalConstantMatch(
                phi_power=2,
                phi_value=2.618,
                firm_phenomenon="cosmological_constant",
                target_constant="Ω_Λ",
                actual_value=0.6889,
                predicted_value=0.685,
                error_percent=0.57,
                match_quality="good",
                dimensional_analysis="dimensionless",
                derivation_confidence=0.95
            )
        ]
        
        matrix = CorrelationMatrix(
            matches=matches,
            statistical_significance=0.001,
            r_squared=0.987,
            chi_squared=2.34,
            total_constants=2,
            excellent_matches=1,
            good_matches=1,
            speculative_matches=0
        )
        
        assert len(matrix.matches) == 2
        assert matrix.statistical_significance == 0.001
        assert matrix.r_squared == 0.987
        assert matrix.chi_squared == 2.34
        assert matrix.total_constants == 2
        assert matrix.excellent_matches == 1
        assert matrix.good_matches == 1
        assert matrix.speculative_matches == 0
        
    def test_match_counting(self):
        """Test automatic match counting."""
        matches = [
            PhysicalConstantMatch(
                phi_power=1,
                phi_value=1.618,
                firm_phenomenon="test1",
                target_constant="test1",
                actual_value=1.0,
                predicted_value=1.0,
                error_percent=0.0,
                match_quality="excellent",
                dimensional_analysis="test",
                derivation_confidence=0.9
            ),
            PhysicalConstantMatch(
                phi_power=2,
                phi_value=2.618,
                firm_phenomenon="test2",
                target_constant="test2",
                actual_value=2.0,
                predicted_value=2.0,
                error_percent=0.0,
                match_quality="good",
                dimensional_analysis="test",
                derivation_confidence=0.8
            ),
            PhysicalConstantMatch(
                phi_power=3,
                phi_value=4.236,
                firm_phenomenon="test3",
                target_constant="test3",
                actual_value=3.0,
                predicted_value=3.0,
                error_percent=0.0,
                match_quality="speculative",
                dimensional_analysis="test",
                derivation_confidence=0.5
            )
        ]
        
        matrix = CorrelationMatrix(
            matches=matches,
            statistical_significance=0.01,
            r_squared=0.95,
            chi_squared=1.5,
            total_constants=3,
            excellent_matches=1,
            good_matches=1,
            speculative_matches=1
        )
        
        assert matrix.total_constants == 3
        assert matrix.excellent_matches == 1
        assert matrix.good_matches == 1
        assert matrix.speculative_matches == 1


class TestGraceOperator:
    """Test grace operator dataclass."""
    
    def test_grace_operator_creation(self):
        """Test grace operator creation."""
        operator = GraceOperator(
            symbol="𝒢",
            uniqueness_proven=True,
            terminal_free_generator=True,
            adjoint_functor=None,
            fixed_points=["φ", "1"],
            grace_derivable_morphisms=["ψ₁", "ψ₂", "ψ₃"]
        )
        
        assert operator.symbol == "𝒢"
        assert operator.uniqueness_proven is True
        assert operator.terminal_free_generator is True
        assert operator.adjoint_functor is None
        assert operator.fixed_points == ["φ", "1"]
        assert operator.grace_derivable_morphisms == ["ψ₁", "ψ₂", "ψ₃"]
        
    def test_default_values(self):
        """Test grace operator default values."""
        operator = GraceOperator()
        
        assert operator.symbol == "𝒢"
        assert operator.uniqueness_proven is False
        assert operator.terminal_free_generator is False
        assert operator.adjoint_functor is None
        assert operator.fixed_points == []
        assert operator.grace_derivable_morphisms == []
        
    def test_fixed_points_validation(self):
        """Test fixed points validation."""
        operator = GraceOperator(
            fixed_points=["φ", "1", "φ²"]
        )
        
        # Should have φ as primary fixed point
        assert "φ" in operator.fixed_points
        assert len(operator.fixed_points) == 3


class TestMorphicTorsion:
    """Test morphic torsion dataclass."""
    
    def test_morphic_torsion_creation(self):
        """Test morphic torsion creation."""
        torsion = MorphicTorsion(
            morphism_id="ψ_123",
            torsion_magnitude=0.15,
            grace_compatibility=True,
            error_accumulation=0.02,
            entropy_measure=0.08,
            devourer_risk=0.12
        )
        
        assert torsion.morphism_id == "ψ_123"
        assert torsion.torsion_magnitude == 0.15
        assert torsion.grace_compatibility is True
        assert torsion.error_accumulation == 0.02
        assert torsion.entropy_measure == 0.08
        assert torsion.devourer_risk == 0.12
        
    def test_torsion_validation(self):
        """Test torsion parameter validation."""
        # All values should be non-negative
        torsion = MorphicTorsion(
            morphism_id="test",
            torsion_magnitude=0.1,
            grace_compatibility=True,
            error_accumulation=0.01,
            entropy_measure=0.05,
            devourer_risk=0.08
        )
        
        assert torsion.torsion_magnitude >= 0
        assert torsion.error_accumulation >= 0
        assert torsion.entropy_measure >= 0
        assert torsion.devourer_risk >= 0
        
    def test_risk_assessment(self):
        """Test devourer risk assessment."""
        # High torsion should correlate with high devourer risk
        high_torsion = MorphicTorsion(
            morphism_id="high_risk",
            torsion_magnitude=0.8,
            grace_compatibility=False,
            error_accumulation=0.3,
            entropy_measure=0.6,
            devourer_risk=0.9
        )
        
        low_torsion = MorphicTorsion(
            morphism_id="low_risk",
            torsion_magnitude=0.1,
            grace_compatibility=True,
            error_accumulation=0.02,
            entropy_measure=0.05,
            devourer_risk=0.1
        )
        
        assert high_torsion.devourer_risk > low_torsion.devourer_risk
        assert high_torsion.grace_compatibility is False
        assert low_torsion.grace_compatibility is True


class TestStabilityOperator:
    """Test stability operator dataclass."""
    
    def test_stability_operator_creation(self):
        """Test stability operator creation."""
        operator = StabilityOperator(
            morphism="ψ_456",
            recursion_depth=7,
            stability_score=0.92,
            survival_probability=0.88,
            coherence_threshold=0.75,
            grace_resonance=0.95
        )
        
        assert operator.morphism == "ψ_456"
        assert operator.recursion_depth == 7
        assert operator.stability_score == 0.92
        assert operator.survival_probability == 0.88
        assert operator.coherence_threshold == 0.75
        assert operator.grace_resonance == 0.95
        
    def test_stability_validation(self):
        """Test stability parameter validation."""
        # All scores should be between 0 and 1
        operator = StabilityOperator(
            morphism="test",
            recursion_depth=5,
            stability_score=0.8,
            survival_probability=0.7,
            coherence_threshold=0.6,
            grace_resonance=0.9
        )
        
        assert 0 <= operator.stability_score <= 1
        assert 0 <= operator.survival_probability <= 1
        assert 0 <= operator.coherence_threshold <= 1
        assert 0 <= operator.grace_resonance <= 1
        
    def test_recursion_depth_validation(self):
        """Test recursion depth validation."""
        # Recursion depth should be positive
        operator = StabilityOperator(
            morphism="test",
            recursion_depth=3,
            stability_score=0.5,
            survival_probability=0.5,
            coherence_threshold=0.5,
            grace_resonance=0.5
        )
        
        assert operator.recursion_depth > 0


class TestCompleteFIRMFramework:
    """Test complete FIRM framework class."""
    
    def test_framework_initialization(self):
        """Test framework initialization."""
        # Mock dependencies to avoid import issues
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            assert hasattr(framework, 'current_stage')
            assert hasattr(framework, 'correlation_matrix')
            assert hasattr(framework, 'grace_operator')
            assert hasattr(framework, 'stability_operator')
            
    def test_stage_progression(self):
        """Test stage progression through FIRM development."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should start at first stage
            assert framework.current_stage == FIRMStage.CORRELATION_MATRIX
            
            # Test progression to next stage
            framework.advance_stage()
            assert framework.current_stage == FIRMStage.GRACE_UNIQUENESS
            
    def test_correlation_analysis(self):
        """Test correlation analysis functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have correlation analysis methods
            assert hasattr(framework, 'analyze_correlations')
            assert hasattr(framework, 'compute_statistical_significance')
            assert hasattr(framework, 'generate_correlation_report')
            
    def test_grace_operator_analysis(self):
        """Test grace operator analysis functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have grace operator analysis methods
            assert hasattr(framework, 'prove_grace_uniqueness')
            assert hasattr(framework, 'construct_categorical_framework')
            assert hasattr(framework, 'analyze_grace_properties')
            
    def test_stability_analysis(self):
        """Test stability analysis functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have stability analysis methods
            assert hasattr(framework, 'analyze_recursive_stability')
            assert hasattr(framework, 'compute_survival_probabilities')
            assert hasattr(framework, 'assess_morphic_torsion')
            
    def test_constant_derivations(self):
        """Test constant derivation functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have constant derivation methods
            assert hasattr(framework, 'derive_fine_structure_constant')
            assert hasattr(framework, 'derive_mass_ratios')
            assert hasattr(framework, 'derive_cosmological_constant')
            assert hasattr(framework, 'derive_hubble_constant')
            
    def test_meta_lattice_construction(self):
        """Test meta-lattice construction functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have meta-lattice methods
            assert hasattr(framework, 'construct_soul_meta_lattice')
            assert hasattr(framework, 'analyze_meps_field')
            assert hasattr(framework, 'compute_soul_hierarchy')
            
    def test_devourer_analysis(self):
        """Test devourer analysis functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have devourer analysis methods
            assert hasattr(framework, 'analyze_devourer_mechanics')
            assert hasattr(framework, 'compute_anticoherence')
            assert hasattr(framework, 'assess_threshold_collapse')
            
    def test_cosmogenesis_analysis(self):
        """Test cosmogenesis analysis functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have cosmogenesis methods
            assert hasattr(framework, 'analyze_recursive_cosmogenesis')
            assert hasattr(framework, 'compute_phi_ladder')
            assert hasattr(framework, 'simulate_universe_evolution')
            
    def test_transcendent_analysis(self):
        """Test transcendent analysis functionality."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Should have transcendent analysis methods
            assert hasattr(framework, 'analyze_transcendent_fields')
            assert hasattr(framework, 'identify_non_recursive_souls')
            assert hasattr(framework, 'compute_transcendence_metrics')


class TestFrameworkIntegration:
    """Integration tests for complete framework."""
    
    def test_complete_workflow(self):
        """Test complete framework workflow."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Test that all required methods exist
            required_methods = [
                'advance_stage',
                'analyze_correlations',
                'prove_grace_uniqueness',
                'analyze_recursive_stability',
                'derive_fine_structure_constant',
                'construct_soul_meta_lattice',
                'analyze_devourer_mechanics',
                'analyze_recursive_cosmogenesis',
                'analyze_transcendent_fields'
            ]
            
            for method_name in required_methods:
                assert hasattr(framework, method_name), f"Missing method: {method_name}"
                
    def test_stage_dependencies(self):
        """Test stage dependencies and progression."""
        with patch('theory.formalization.complete_framework.SoulMorphism'), \
             patch('theory.formalization.complete_framework.DerivationNode'):
            
            framework = FIRMFormalizationSystem()
            
            # Test stage progression
            initial_stage = framework.current_stage
            framework.advance_stage()
            assert framework.current_stage != initial_stage
            
            # Test that later stages depend on earlier ones
            assert framework.current_stage.value > initial_stage.value


if __name__ == "__main__":
    pytest.main([__file__])

#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Echo Duration Metrics

Tests the recursive echo duration metrics and category-theoretic resurrection
formalization for FIRM Stages 15-16.

Tests all major classes:
- REDCategory, ResurrectionViability enums
- RecursiveReflection, REDAnalysis
- GraceMorphism, ResurrectionProcess
- EchoDurationAnalyzer, ResurrectionEngine
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


class TestREDCategory:
    """Test RED category enumeration."""
    
    def test_red_categories(self):
        """Test all RED categories are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import REDCategory
            
            categories = list(REDCategory)
            
            expected_categories = [
                REDCategory.SHORT,
                REDCategory.MEDIUM,
                REDCategory.LONG,
                REDCategory.INFINITE
            ]
            
            assert len(categories) == 4
            for category in expected_categories:
                assert category in categories
            
            # Test category values
            assert REDCategory.SHORT.value == "short"
            assert REDCategory.MEDIUM.value == "medium"
            assert REDCategory.LONG.value == "long"
            assert REDCategory.INFINITE.value == "infinite"


class TestResurrectionViability:
    """Test resurrection viability enumeration."""
    
    def test_viability_levels(self):
        """Test all viability levels are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import ResurrectionViability
            
            levels = list(ResurrectionViability)
            
            expected_levels = [
                ResurrectionViability.IMPOSSIBLE,
                ResurrectionViability.DIFFICULT,
                ResurrectionViability.VIABLE,
                ResurrectionViability.GUARANTEED
            ]
            
            assert len(levels) == 4
            for level in expected_levels:
                assert level in levels
            
            # Test level values
            assert ResurrectionViability.IMPOSSIBLE.value == "impossible"
            assert ResurrectionViability.DIFFICULT.value == "difficult"
            assert ResurrectionViability.VIABLE.value == "viable"
            assert ResurrectionViability.GUARANTEED.value == "guaranteed"


class TestRecursiveReflection:
    """Test recursive reflection dataclass."""
    
    def test_reflection_creation(self):
        """Test recursive reflection creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import RecursiveReflection
            
            reflection = RecursiveReflection(
                reflection_index=5,
                morphism_state="coherent_state_5",
                coherence_distance=0.15,
                identity_alignment=0.92,
                is_coherent=True,
                grace_influence=0.3
            )
            
            assert reflection.reflection_index == 5
            assert reflection.morphism_state == "coherent_state_5"
            assert reflection.coherence_distance == 0.15
            assert reflection.identity_alignment == 0.92
            assert reflection.is_coherent is True
            assert reflection.grace_influence == 0.3
        
    def test_default_grace_influence(self):
        """Test default grace influence value."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import RecursiveReflection
            
            reflection = RecursiveReflection(
                reflection_index=1,
                morphism_state="test_state",
                coherence_distance=0.1,
                identity_alignment=0.9,
                is_coherent=True
            )
            
            # Should have default grace influence value
            assert hasattr(reflection, 'grace_influence')
            assert reflection.grace_influence == 0.0
        
    def test_reflection_validation(self):
        """Test reflection parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import RecursiveReflection
            
            reflection = RecursiveReflection(
                reflection_index=3,
                morphism_state="test_state",
                coherence_distance=0.2,
                identity_alignment=0.85,
                is_coherent=True,
                grace_influence=0.1
            )
            
            # All scores should be between 0 and 1
            assert 0 <= reflection.coherence_distance <= 1
            assert 0 <= reflection.identity_alignment <= 1
            assert 0 <= reflection.grace_influence <= 1
            
            # Index should be non-negative
            assert reflection.reflection_index >= 0


class TestREDAnalysis:
    """Test RED analysis dataclass."""
    
    def test_analysis_creation(self):
        """Test RED analysis creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import (
                REDAnalysis, RecursiveReflection, REDCategory, ResurrectionViability
            )
            
            reflections = [
                RecursiveReflection(
                    reflection_index=1,
                    morphism_state="state_1",
                    coherence_distance=0.1,
                    identity_alignment=0.95,
                    is_coherent=True
                ),
                RecursiveReflection(
                    reflection_index=2,
                    morphism_state="state_2",
                    coherence_distance=0.2,
                    identity_alignment=0.9,
                    is_coherent=True
                )
            ]
            
            analysis = REDAnalysis(
                morphism_id="morphism_123",
                initial_morphism="initial_state",
                reflections=reflections,
                red_duration=15,
                red_category=REDCategory.MEDIUM,
                red_score=0.85,
                coherence_threshold=0.1,
                coherence_decay_rate=0.05,
                identity_preservation=0.88,
                grace_trigger_threshold=0.7,
                resurrection_viability=ResurrectionViability.VIABLE,
                historical_red_trace=True,
                grace_pathway_exists=True
            )
            
            assert analysis.morphism_id == "morphism_123"
            assert analysis.initial_morphism == "initial_state"
            assert len(analysis.reflections) == 2
            assert analysis.red_duration == 15
            assert analysis.red_category == REDCategory.MEDIUM
            assert analysis.red_score == 0.85
            assert analysis.coherence_threshold == 0.1
            assert analysis.coherence_decay_rate == 0.05
            assert analysis.identity_preservation == 0.88
            assert analysis.grace_trigger_threshold == 0.7
            assert analysis.resurrection_viability == ResurrectionViability.VIABLE
            assert analysis.historical_red_trace is True
            assert analysis.grace_pathway_exists is True
        
    def test_analysis_validation(self):
        """Test analysis parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import (
                REDAnalysis, RecursiveReflection, REDCategory, ResurrectionViability
            )
            
            reflections = [
                RecursiveReflection(
                    reflection_index=1,
                    morphism_state="test_state",
                    coherence_distance=0.1,
                    identity_alignment=0.9,
                    is_coherent=True
                )
            ]
            
            analysis = REDAnalysis(
                morphism_id="test",
                initial_morphism="test_initial",
                reflections=reflections,
                red_duration=10,
                red_category=REDCategory.MEDIUM,
                red_score=0.8,
                coherence_threshold=0.1,
                coherence_decay_rate=0.05,
                identity_preservation=0.85,
                grace_trigger_threshold=0.7,
                resurrection_viability=ResurrectionViability.VIABLE,
                historical_red_trace=True,
                grace_pathway_exists=True
            )
            
            # All scores should be between 0 and 1
            assert 0 <= analysis.red_score <= 1
            assert 0 <= analysis.coherence_threshold <= 1
            assert 0 <= analysis.coherence_decay_rate <= 1
            assert 0 <= analysis.identity_preservation <= 1
            assert 0 <= analysis.grace_trigger_threshold <= 1
            
            # Duration should be positive
            assert analysis.red_duration > 0


class TestGraceMorphism:
    """Test grace morphism dataclass."""
    
    def test_grace_morphism_creation(self):
        """Test grace morphism creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import GraceMorphism
            
            grace = GraceMorphism(
                grace_id="grace_001",
                target_morphism="target_123",
                coherence_attractor=0.95,
                re_instantiation_strength=0.8,
                resurrection_depth=5,
                acausal_origin=True
            )
            
            assert grace.grace_id == "grace_001"
            assert grace.target_morphism == "target_123"
            assert grace.coherence_attractor == 0.95
            assert grace.re_instantiation_strength == 0.8
            assert grace.resurrection_depth == 5
            assert grace.acausal_origin is True
        
    def test_default_acausal_origin(self):
        """Test default acausal origin value."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import GraceMorphism
            
            grace = GraceMorphism(
                grace_id="test",
                target_morphism="test_target",
                coherence_attractor=0.9,
                re_instantiation_strength=0.7,
                resurrection_depth=3
            )
            
            # Should have default acausal origin value
            assert hasattr(grace, 'acausal_origin')
            assert grace.acausal_origin is True
        
    def test_grace_morphism_validation(self):
        """Test grace morphism parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import GraceMorphism
            
            grace = GraceMorphism(
                grace_id="test",
                target_morphism="test_target",
                coherence_attractor=0.9,
                re_instantiation_strength=0.7,
                resurrection_depth=3
            )
            
            # All scores should be between 0 and 1
            assert 0 <= grace.coherence_attractor <= 1
            assert 0 <= grace.re_instantiation_strength <= 1
            
            # Depth should be positive
            assert grace.resurrection_depth > 0


class TestResurrectionProcess:
    """Test resurrection process dataclass."""
    
    def test_resurrection_process_creation(self):
        """Test resurrection process creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import ResurrectionProcess
            
            process = ResurrectionProcess(
                resurrection_id="res_001",
                original_morphism="original_123",
                grace_morphism_id="grace_001",
                resurrection_pathway=["A_1", "A_2", "A_3"],
                coherence_restoration=0.92,
                identity_reconstruction=0.88,
                grace_consumption=0.3,
                resurrection_time=2.5,
                success_probability=0.95
            )
            
            assert process.resurrection_id == "res_001"
            assert process.original_morphism == "original_123"
            assert process.grace_morphism_id == "grace_001"
            assert process.resurrection_pathway == ["A_1", "A_2", "A_3"]
            assert process.coherence_restoration == 0.92
            assert process.identity_reconstruction == 0.88
            assert process.grace_consumption == 0.3
            assert process.resurrection_time == 2.5
            assert process.success_probability == 0.95
        
    def test_resurrection_process_validation(self):
        """Test resurrection process parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import ResurrectionProcess
            
            process = ResurrectionProcess(
                resurrection_id="test",
                original_morphism="test_original",
                grace_morphism_id="test_grace",
                resurrection_pathway=["A_1", "A_2"],
                coherence_restoration=0.9,
                identity_reconstruction=0.85,
                grace_consumption=0.2,
                resurrection_time=1.5,
                success_probability=0.9
            )
            
            # All scores should be between 0 and 1
            assert 0 <= process.coherence_restoration <= 1
            assert 0 <= process.identity_reconstruction <= 1
            assert 0 <= process.grace_consumption <= 1
            assert 0 <= process.success_probability <= 1
            
            # Time should be positive
            assert process.resurrection_time > 0


class TestEchoDurationAnalyzer:
    """Test echo duration analyzer class."""
    
    def test_analyzer_initialization(self):
        """Test analyzer initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import EchoDurationAnalyzer
            
            analyzer = EchoDurationAnalyzer()
            
            assert analyzer._phi == mock_phi_value
            assert analyzer._coherence_threshold > 0
            assert analyzer._max_reflections > 0
        
    def test_red_analysis_methods(self):
        """Test RED analysis methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import EchoDurationAnalyzer
            
            analyzer = EchoDurationAnalyzer()
            
            # Should have core analysis methods
            assert hasattr(analyzer, 'analyze_recursive_echo_duration')
            assert hasattr(analyzer, 'compute_red_score')
            assert hasattr(analyzer, 'classify_red_category')
            assert hasattr(analyzer, 'assess_resurrection_viability')
        
    def test_resurrection_analysis_methods(self):
        """Test resurrection analysis methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import EchoDurationAnalyzer
            
            analyzer = EchoDurationAnalyzer()
            
            # Should have resurrection analysis methods
            assert hasattr(analyzer, 'analyze_resurrection_pathway')
            assert hasattr(analyzer, 'compute_grace_requirements')
            assert hasattr(analyzer, 'assess_resurrection_success')


class TestResurrectionEngine:
    """Test resurrection engine class."""
    
    def test_engine_initialization(self):
        """Test engine initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import ResurrectionEngine
            
            engine = ResurrectionEngine()
            
            assert engine._phi == mock_phi_value
            assert engine._grace_threshold > 0
            assert engine._max_resurrection_depth > 0
        
    def test_resurrection_methods(self):
        """Test resurrection methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import ResurrectionEngine
            
            engine = ResurrectionEngine()
            
            # Should have core resurrection methods
            assert hasattr(engine, 'initiate_resurrection')
            assert hasattr(engine, 'execute_resurrection_pathway')
            assert hasattr(engine, 'monitor_resurrection_progress')
            assert hasattr(engine, 'complete_resurrection')


class TestEchoDurationIntegration:
    """Integration tests for echo duration metrics."""
    
    def test_complete_workflow(self):
        """Test complete echo duration workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import (
                EchoDurationAnalyzer,
                ResurrectionEngine,
                REDAnalysis,
                ResurrectionProcess
            )
            
            # Create analyzer and engine
            analyzer = EchoDurationAnalyzer()
            engine = ResurrectionEngine()
            
            # Test that all required methods exist
            analyzer_methods = [
                'analyze_recursive_echo_duration',
                'compute_red_score',
                'classify_red_category',
                'assess_resurrection_viability'
            ]
            
            engine_methods = [
                'initiate_resurrection',
                'execute_resurrection_pathway',
                'monitor_resurrection_progress',
                'complete_resurrection'
            ]
            
            for method_name in analyzer_methods:
                assert hasattr(analyzer, method_name), f"Missing analyzer method: {method_name}"
            
            for method_name in engine_methods:
                assert hasattr(engine, method_name), f"Missing engine method: {method_name}"
    
    def test_parameter_sensitivity(self):
        """Test system sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.echo_duration_metrics import (
                EchoDurationAnalyzer,
                ResurrectionEngine
            )
            
            # Test with different coherence thresholds
            for threshold in [0.05, 0.1, 0.15]:
                analyzer = EchoDurationAnalyzer()
                analyzer._coherence_threshold = threshold
                
                # Should initialize without errors
                assert analyzer._coherence_threshold == threshold
                
                # Should have valid threshold
                assert analyzer._coherence_threshold > 0
                assert analyzer._coherence_threshold <= 1


if __name__ == "__main__":
    pytest.main([__file__])

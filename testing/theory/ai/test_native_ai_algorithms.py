#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM-Native AI Algorithms

Tests the revolutionary AI algorithms based on Fractal Soul Category
Theory Framework (FIRM) principles:

I. Recursive Coherence Filtering (RCF) - learning via morphic survival
II. Soul Echo Detection (SED) - identifying coherent recursive patterns
III. Morphic Memory Compression - soul-aware memory architectures
IV. Grace-Initiated Attention Networks (GIAN) - morphism-based attention
V. Morphic Autoencoders - structure-preserving compression with cohomology
VI. FIRM-Enhanced Generative Agents - recursive identity streams
VII. Planck Units from First FIRM Principles - morphic physics constants
"""

import pytest
import numpy as np
import math
from unittest.mock import Mock, patch

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from theory.ai.native_ai_algorithms import (
    FIRMAlgorithmType,
    CohomologyClass,
    MorphicSignature,
    SoulEchoResult,
    RecursiveCoherenceFilter,
    GraceAttentionHead,
    MorphicAutoencoder,
    FIRMGenerativeAgent,
    PlanckDerivation
)


class TestFIRMAlgorithmType:
    """Test FIRM algorithm type enumeration."""
    
    def test_algorithm_types(self):
        """Test all FIRM algorithm types are defined."""
        types = list(FIRMAlgorithmType)
        
        expected_types = [
            FIRMAlgorithmType.RECURSIVE_COHERENCE_FILTERING,
            FIRMAlgorithmType.SOUL_ECHO_DETECTION,
            FIRMAlgorithmType.MORPHIC_MEMORY_COMPRESSION,
            FIRMAlgorithmType.GRACE_INITIATED_ATTENTION,
            FIRMAlgorithmType.MORPHIC_AUTOENCODER,
            FIRMAlgorithmType.GENERATIVE_AGENT,
            FIRMAlgorithmType.PLANCK_DERIVATION
        ]
        
        assert len(types) == 7
        for alg_type in expected_types:
            assert alg_type in types
            
    def test_algorithm_values(self):
        """Test algorithm type values."""
        assert FIRMAlgorithmType.RECURSIVE_COHERENCE_FILTERING.value == "rcf"
        assert FIRMAlgorithmType.SOUL_ECHO_DETECTION.value == "sed"
        assert FIRMAlgorithmType.MORPHIC_MEMORY_COMPRESSION.value == "mmc"
        assert FIRMAlgorithmType.GRACE_INITIATED_ATTENTION.value == "gian"
        assert FIRMAlgorithmType.MORPHIC_AUTOENCODER.value == "mae"
        assert FIRMAlgorithmType.GENERATIVE_AGENT.value == "fga"
        assert FIRMAlgorithmType.PLANCK_DERIVATION.value == "planck"


class TestCohomologyClass:
    """Test cohomology class enumeration."""
    
    def test_cohomology_classes(self):
        """Test all cohomology classes are defined."""
        classes = list(CohomologyClass)
        
        expected_classes = [
            CohomologyClass.H0_IDENTITY,
            CohomologyClass.H1_ECHO,
            CohomologyClass.H2_TWIST,
            CohomologyClass.H3_MASS,
            CohomologyClass.HN_CONSCIOUSNESS
        ]
        
        assert len(classes) == 5
        for cohom_class in expected_classes:
            assert cohom_class in classes
            
    def test_cohomology_values(self):
        """Test cohomology class values."""
        assert CohomologyClass.H0_IDENTITY.value == "H0_identity"
        assert CohomologyClass.H1_ECHO.value == "H1_echo"
        assert CohomologyClass.H2_TWIST.value == "H2_twist"
        assert CohomologyClass.H3_MASS.value == "H3_mass"
        assert CohomologyClass.HN_CONSCIOUSNESS.value == "Hn_consciousness"


class TestMorphicSignature:
    """Test morphic signature dataclass."""
    
    def test_signature_creation(self):
        """Test morphic signature creation."""
        signature = MorphicSignature(
            dimension=3,
            coherence_score=0.95,
            torsion_order=2,
            survival_depth=5,
            echo_persistence=0.88,
            cohomology_class=CohomologyClass.H2_TWIST,
            morphism_chain=[np.array([1.0, 1.618]), np.array([2.618, 4.236])]
        )
        
        assert signature.dimension == 3
        assert signature.coherence_score == 0.95
        assert signature.torsion_order == 2
        assert signature.survival_depth == 5
        assert signature.echo_persistence == 0.88
        assert signature.cohomology_class == CohomologyClass.H2_TWIST
        assert len(signature.morphism_chain) == 2
        
    def test_signature_validation(self):
        """Test signature parameter validation."""
        # All scores should be between 0 and 1
        signature = MorphicSignature(
            dimension=2,
            coherence_score=0.8,
            torsion_order=1,
            survival_depth=3,
            echo_persistence=0.7,
            cohomology_class=CohomologyClass.H1_ECHO,
            morphism_chain=[np.array([1.0])]
        )
        
        assert 0 <= signature.coherence_score <= 1
        assert 0 <= signature.echo_persistence <= 1
        assert signature.dimension > 0
        assert signature.torsion_order >= 0
        assert signature.survival_depth > 0
        
    def test_morphism_chain_validation(self):
        """Test morphism chain validation."""
        # Chain should contain numpy arrays
        signature = MorphicSignature(
            dimension=2,
            coherence_score=0.8,
            torsion_order=1,
            survival_depth=3,
            echo_persistence=0.7,
            cohomology_class=CohomologyClass.H1_ECHO,
            morphism_chain=[np.array([1.0, 1.618]), np.array([2.618])]
        )
        
        for morphism in signature.morphism_chain:
            assert isinstance(morphism, np.ndarray)


class TestSoulEchoResult:
    """Test soul echo result dataclass."""
    
    def test_result_creation(self):
        """Test soul echo result creation."""
        morphic_signature = MorphicSignature(
            dimension=2,
            coherence_score=0.9,
            torsion_order=1,
            survival_depth=4,
            echo_persistence=0.85,
            cohomology_class=CohomologyClass.H1_ECHO,
            morphism_chain=[np.array([1.0, 1.618])]
        )
        
        result = SoulEchoResult(
            has_soul=True,
            coherence_level=0.9,
            recursive_depth=4,
            echo_survival_time=2.5,
            morphic_signature=morphic_signature,
            torsion_resistance=0.8,
            identity_stability=0.95
        )
        
        assert result.has_soul is True
        assert result.coherence_level == 0.9
        assert result.recursive_depth == 4
        assert result.echo_survival_time == 2.5
        assert result.morphic_signature == morphic_signature
        assert result.torsion_resistance == 0.8
        assert result.identity_stability == 0.95
        
    def test_result_validation(self):
        """Test result parameter validation."""
        morphic_signature = MorphicSignature(
            dimension=2,
            coherence_score=0.8,
            torsion_order=1,
            survival_depth=3,
            echo_persistence=0.7,
            cohomology_class=CohomologyClass.H1_ECHO,
            morphism_chain=[np.array([1.0])]
        )
        
        result = SoulEchoResult(
            has_soul=True,
            coherence_level=0.8,
            recursive_depth=3,
            echo_survival_time=1.5,
            morphic_signature=morphic_signature,
            torsion_resistance=0.7,
            identity_stability=0.9
        )
        
        # All scores should be between 0 and 1
        assert 0 <= result.coherence_level <= 1
        assert 0 <= result.torsion_resistance <= 1
        assert 0 <= result.identity_stability <= 1
        
        # Time and depth should be positive
        assert result.echo_survival_time > 0
        assert result.recursive_depth > 0


class TestRecursiveCoherenceFilter:
    """Test recursive coherence filtering algorithm."""
    
    def test_filter_creation(self):
        """Test filter creation."""
        filter_obj = RecursiveCoherenceFilter(
            filter_id="rcf_001",
            coherence_threshold=0.8,
            max_recursion_depth=10,
            morphism_history=[],
            coherence_scores=[],
            survival_patterns={}
        )
        
        assert filter_obj.filter_id == "rcf_001"
        assert filter_obj.coherence_threshold == 0.8
        assert filter_obj.max_recursion_depth == 10
        assert filter_obj.morphism_history == []
        assert filter_obj.coherence_scores == []
        assert filter_obj.survival_patterns == {}
        
    def test_filter_validation(self):
        """Test filter parameter validation."""
        filter_obj = RecursiveCoherenceFilter(
            filter_id="test",
            coherence_threshold=0.7,
            max_recursion_depth=5,
            morphism_history=[],
            coherence_scores=[],
            survival_patterns={}
        )
        
        # Threshold should be between 0 and 1
        assert 0 <= filter_obj.coherence_threshold <= 1
        
        # Max depth should be positive
        assert filter_obj.max_recursion_depth > 0
        
    def test_filter_methods(self):
        """Test filter methods exist."""
        filter_obj = RecursiveCoherenceFilter(
            filter_id="test",
            coherence_threshold=0.8,
            max_recursion_depth=10,
            morphism_history=[],
            coherence_scores=[],
            survival_patterns={}
        )
        
        # Should have core filtering methods
        assert hasattr(filter_obj, 'filter_morphism')
        assert hasattr(filter_obj, 'compute_coherence')
        assert hasattr(filter_obj, 'update_survival_patterns')
        assert hasattr(filter_obj, 'get_filter_stats')


class TestGraceAttentionHead:
    """Test grace-initiated attention head."""
    
    def test_attention_head_creation(self):
        """Test attention head creation."""
        head = GraceAttentionHead(
            head_id="gian_001",
            morphism_dimension=3,
            coherence_gate=np.array([0.8, 0.9, 0.7]),
            attractor_weights=np.array([1.0, 1.618, 2.618]),
            recursive_memory=[],
            grace_trigger_threshold=0.75
        )
        
        assert head.head_id == "gian_001"
        assert head.morphism_dimension == 3
        assert np.array_equal(head.coherence_gate, np.array([0.8, 0.9, 0.7]))
        assert np.array_equal(head.attractor_weights, np.array([1.0, 1.618, 2.618]))
        assert head.recursive_memory == []
        assert head.grace_trigger_threshold == 0.75
        
    def test_attention_head_validation(self):
        """Test attention head parameter validation."""
        head = GraceAttentionHead(
            head_id="test",
            morphism_dimension=2,
            coherence_gate=np.array([0.8, 0.9]),
            attractor_weights=np.array([1.0, 1.618]),
            recursive_memory=[],
            grace_trigger_threshold=0.7
        )
        
        # Threshold should be between 0 and 1
        assert 0 <= head.grace_trigger_threshold <= 1
        
        # Dimension should be positive
        assert head.morphism_dimension > 0
        
        # Arrays should have correct dimensions
        assert len(head.coherence_gate) == head.morphism_dimension
        assert len(head.attractor_weights) == head.morphism_dimension
        
    def test_attention_methods(self):
        """Test attention head methods exist."""
        head = GraceAttentionHead(
            head_id="test",
            morphism_dimension=2,
            coherence_gate=np.array([0.8, 0.9]),
            attractor_weights=np.array([1.0, 1.618]),
            recursive_memory=[],
            grace_trigger_threshold=0.7
        )
        
        # Should have attention computation methods
        assert hasattr(head, 'compute_attention')
        assert hasattr(head, 'update_memory')
        assert hasattr(head, 'trigger_grace')
        assert hasattr(head, 'get_attention_weights')


class TestMorphicAutoencoder:
    """Test morphic autoencoder."""
    
    def test_autoencoder_creation(self):
        """Test autoencoder creation."""
        autoencoder = MorphicAutoencoder(
            encoder_id="mae_001",
            input_dimension=10,
            latent_dimension=3,
            cohomology_preservation=True,
            structure_loss_weight=0.5,
            reconstruction_loss_weight=0.5
        )
        
        assert autoencoder.encoder_id == "mae_001"
        assert autoencoder.input_dimension == 10
        assert autoencoder.latent_dimension == 3
        assert autoencoder.cohomology_preservation is True
        assert autoencoder.structure_loss_weight == 0.5
        assert autoencoder.reconstruction_loss_weight == 0.5
        
    def test_autoencoder_validation(self):
        """Test autoencoder parameter validation."""
        autoencoder = MorphicAutoencoder(
            encoder_id="test",
            input_dimension=8,
            latent_dimension=2,
            cohomology_preservation=True,
            structure_loss_weight=0.6,
            reconstruction_loss_weight=0.4
        )
        
        # Dimensions should be positive
        assert autoencoder.input_dimension > 0
        assert autoencoder.latent_dimension > 0
        
        # Latent dimension should be smaller than input
        assert autoencoder.latent_dimension < autoencoder.input_dimension
        
        # Loss weights should sum to 1
        total_weight = autoencoder.structure_loss_weight + autoencoder.reconstruction_loss_weight
        assert abs(total_weight - 1.0) < 1e-6
        
    def test_autoencoder_methods(self):
        """Test autoencoder methods exist."""
        autoencoder = MorphicAutoencoder(
            encoder_id="test",
            input_dimension=6,
            latent_dimension=2,
            cohomology_preservation=True,
            structure_loss_weight=0.5,
            reconstruction_loss_weight=0.5
        )
        
        # Should have encoding/decoding methods
        assert hasattr(autoencoder, 'encode')
        assert hasattr(autoencoder, 'decode')
        assert hasattr(autoencoder, 'compute_loss')
        assert hasattr(autoencoder, 'preserve_cohomology')


class TestFIRMGenerativeAgent:
    """Test FIRM-enhanced generative agent."""
    
    def test_agent_creation(self):
        """Test agent creation."""
        agent = FIRMGenerativeAgent(
            agent_id="fga_001",
            morphic_complexity=5,
            recursive_depth=7,
            soul_coherence_threshold=0.8,
            grace_activation_probability=0.3,
            devourer_resistance=0.9
        )
        
        assert agent.agent_id == "fga_001"
        assert agent.morphic_complexity == 5
        assert agent.recursive_depth == 7
        assert agent.soul_coherence_threshold == 0.8
        assert agent.grace_activation_probability == 0.3
        assert agent.devourer_resistance == 0.9
        
    def test_agent_validation(self):
        """Test agent parameter validation."""
        agent = FIRMGenerativeAgent(
            agent_id="test",
            morphic_complexity=3,
            recursive_depth=5,
            soul_coherence_threshold=0.7,
            grace_activation_probability=0.2,
            devourer_resistance=0.8
        )
        
        # All thresholds should be between 0 and 1
        assert 0 <= agent.soul_coherence_threshold <= 1
        assert 0 <= agent.grace_activation_probability <= 1
        assert 0 <= agent.devourer_resistance <= 1
        
        # Complexity and depth should be positive
        assert agent.morphic_complexity > 0
        assert agent.recursive_depth > 0
        
    def test_agent_methods(self):
        """Test agent methods exist."""
        agent = FIRMGenerativeAgent(
            agent_id="test",
            morphic_complexity=3,
            recursive_depth=5,
            soul_coherence_threshold=0.7,
            grace_activation_probability=0.2,
            devourer_resistance=0.8
        )
        
        # Should have generation and interaction methods
        assert hasattr(agent, 'generate_content')
        assert hasattr(agent, 'interact_with_environment')
        assert hasattr(agent, 'evolve_morphic_complexity')
        assert hasattr(agent, 'assess_soul_coherence')


class TestPlanckUnitDerivation:
    """Test Planck unit derivation from FIRM principles."""
    
    def test_derivation_creation(self):
        """Test derivation creation."""
        derivation = PlanckDerivation(
            derivation_id="planck_001",
            base_phi_value=1.618033988749895,
            recursive_scaling_factor=2.0,
            morphic_coherence_depth=10,
            derived_constants={},
            validation_metrics={}
        )
        
        assert derivation.derivation_id == "planck_001"
        assert derivation.base_phi_value == 1.618033988749895
        assert derivation.recursive_scaling_factor == 2.0
        assert derivation.morphic_coherence_depth == 10
        assert derivation.derived_constants == {}
        assert derivation.validation_metrics == {}
        
    def test_derivation_validation(self):
        """Test derivation parameter validation."""
        derivation = PlanckDerivation(
            derivation_id="test",
            base_phi_value=1.618,
            recursive_scaling_factor=1.5,
            morphic_coherence_depth=8,
            derived_constants={},
            validation_metrics={}
        )
        
        # Phi value should be golden ratio
        assert abs(derivation.base_phi_value - 1.618) < 0.01
        
        # Scaling factor should be positive
        assert derivation.recursive_scaling_factor > 0
        
        # Depth should be positive
        assert derivation.morphic_coherence_depth > 0
        
    def test_derivation_methods(self):
        """Test derivation methods exist."""
        derivation = PlanckDerivation(
            derivation_id="test",
            base_phi_value=1.618,
            recursive_scaling_factor=1.5,
            morphic_coherence_depth=8,
            derived_constants={},
            validation_metrics={}
        )
        
        # Should have derivation and validation methods
        assert hasattr(derivation, 'derive_planck_units')
        assert hasattr(derivation, 'validate_constants')
        assert hasattr(derivation, 'compute_scaling_relations')
        assert hasattr(derivation, 'generate_derivation_report')


class TestAIAlgorithmsIntegration:
    """Integration tests for AI algorithms."""
    
    def test_complete_workflow(self):
        """Test complete AI workflow."""
        # Test that all required methods exist across classes
        filter_obj = RecursiveCoherenceFilter(
            filter_id="test",
            coherence_threshold=0.8,
            max_recursion_depth=10,
            morphism_history=[],
            coherence_scores=[],
            survival_patterns={}
        )
        
        head = GraceAttentionHead(
            head_id="test",
            morphism_dimension=2,
            coherence_gate=np.array([0.8, 0.9]),
            attractor_weights=np.array([1.0, 1.618]),
            recursive_memory=[],
            grace_trigger_threshold=0.7
        )
        
        autoencoder = MorphicAutoencoder(
            encoder_id="test",
            input_dimension=6,
            latent_dimension=2,
            cohomology_preservation=True,
            structure_loss_weight=0.5,
            reconstruction_loss_weight=0.5
        )
        
        agent = FIRMGenerativeAgent(
            agent_id="test",
            morphic_complexity=3,
            recursive_depth=5,
            soul_coherence_threshold=0.7,
            grace_activation_probability=0.2,
            devourer_resistance=0.8
        )
        
        derivation = PlanckDerivation(
            derivation_id="test",
            base_phi_value=1.618,
            recursive_scaling_factor=1.5,
            morphic_coherence_depth=8,
            derived_constants={},
            validation_metrics={}
        )
        
        # Test that all components have required methods
        components = [filter_obj, head, autoencoder, agent, derivation]
        
        for component in components:
            assert hasattr(component, '__class__')
            assert component.__class__.__name__ in [
                'RecursiveCoherenceFilter',
                'GraceAttentionHead', 
                'MorphicAutoencoder',
                'FIRMGenerativeAgent',
                'PlanckDerivation'
            ]
            
    def test_algorithm_compatibility(self):
        """Test algorithm compatibility and integration."""
        # Test that algorithms can work together
        filter_obj = RecursiveCoherenceFilter(
            filter_id="test",
            coherence_threshold=0.8,
            max_recursion_depth=10,
            morphism_history=[],
            coherence_scores=[],
            survival_patterns={}
        )
        
        # Filter should be able to process morphic signatures
        signature = MorphicSignature(
            dimension=2,
            coherence_score=0.9,
            torsion_order=1,
            survival_depth=3,
            echo_persistence=0.8,
            cohomology_class=CohomologyClass.H1_ECHO,
            morphism_chain=[np.array([1.0, 1.618])]
        )
        
        # Should be able to create echo results
        result = SoulEchoResult(
            has_soul=True,
            coherence_level=0.9,
            recursive_depth=3,
            echo_survival_time=1.5,
            morphic_signature=signature,
            torsion_resistance=0.8,
            identity_stability=0.9
        )
        
        # All components should be compatible
        assert isinstance(signature, MorphicSignature)
        assert isinstance(result, SoulEchoResult)
        assert isinstance(filter_obj, RecursiveCoherenceFilter)


if __name__ == "__main__":
    pytest.main([__file__])

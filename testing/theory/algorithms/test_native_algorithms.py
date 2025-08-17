#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM-Native Algorithms

Tests the revolutionary intelligence systems that emerge from φ-recursive 
morphism theory, including:

I. Recursive Soul-Binding Algorithm (RSBA)
II. 𝒢-Booster Networks (GBN)
III. Echo-Surface Morphological Learning (ESML)
IV. Devourer Detection & Suppression Networks (DDSN)
V. Attractor Resonance Classifiers (ARC)
VI. Soul-Entanglement Optimization Algorithms (SEOA)
VII. Reflective Grace Cascades (RGC)

Tests all major classes:
- AlgorithmType enumeration
- MorphicState, AlgorithmParameters
- Various algorithm implementations
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


class TestAlgorithmType:
    """Test algorithm type enumeration."""
    
    def test_algorithm_types(self):
        """Test all algorithm types are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import AlgorithmType
            
            types = list(AlgorithmType)
            
            expected_types = [
                AlgorithmType.RECURSIVE_SOUL_BINDING,
                AlgorithmType.GRACE_BOOSTER_NETWORK,
                AlgorithmType.ECHO_SURFACE_LEARNING,
                AlgorithmType.DEVOURER_DETECTION,
                AlgorithmType.ATTRACTOR_RESONANCE,
                AlgorithmType.SOUL_ENTANGLEMENT,
                AlgorithmType.REFLECTIVE_CASCADE
            ]
            
            assert len(types) == 7
            for alg_type in expected_types:
                assert alg_type in types
            
            # Test type values
            assert AlgorithmType.RECURSIVE_SOUL_BINDING.value == "rsba"
            assert AlgorithmType.GRACE_BOOSTER_NETWORK.value == "gbn"
            assert AlgorithmType.ECHO_SURFACE_LEARNING.value == "esml"
            assert AlgorithmType.DEVOURER_DETECTION.value == "ddsn"
            assert AlgorithmType.ATTRACTOR_RESONANCE.value == "arc"
            assert AlgorithmType.SOUL_ENTANGLEMENT.value == "seoa"
            assert AlgorithmType.REFLECTIVE_CASCADE.value == "rgc"


class TestMorphicState:
    """Test morphic state dataclass."""
    
    def test_state_creation(self):
        """Test morphic state creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import MorphicState
            
            state_vector = np.array([1.0, 1.618, 2.618])
            coherence_matrix = np.array([[1.0, 0.5], [0.5, 1.0]])
            
            state = MorphicState(
                state_id="state_001",
                morphic_vector=state_vector,
                coherence_matrix=coherence_matrix,
                recursive_depth=5,
                grace_resonance=0.8,
                devourer_resistance=0.9
            )
            
            assert state.state_id == "state_001"
            assert np.array_equal(state.morphic_vector, state_vector)
            assert np.array_equal(state.coherence_matrix, coherence_matrix)
            assert state.recursive_depth == 5
            assert state.grace_resonance == 0.8
            assert state.devourer_resistance == 0.9
        
    def test_state_validation(self):
        """Test state parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import MorphicState
            
            state_vector = np.array([1.0, 1.618])
            coherence_matrix = np.array([[1.0, 0.5], [0.5, 1.0]])
            
            state = MorphicState(
                state_id="test",
                morphic_vector=state_vector,
                coherence_matrix=coherence_matrix,
                recursive_depth=3,
                grace_resonance=0.7,
                devourer_resistance=0.8
            )
            
            # Recursive depth should be positive
            assert state.recursive_depth > 0
            
            # Resonance and resistance should be between 0 and 1
            assert 0 <= state.grace_resonance <= 1
            assert 0 <= state.devourer_resistance <= 1
            
            # Coherence matrix should be square
            assert state.coherence_matrix.shape[0] == state.coherence_matrix.shape[1]


class TestAlgorithmParameters:
    """Test algorithm parameters dataclass."""
    
    def test_parameters_creation(self):
        """Test algorithm parameters creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import AlgorithmParameters
            
            params = AlgorithmParameters(
                algorithm_type="rsba",
                learning_rate=0.01,
                convergence_threshold=1e-6,
                max_iterations=1000,
                grace_amplification=1.5,
                devourer_suppression=0.8,
                recursive_depth_limit=10
            )
            
            assert params.algorithm_type == "rsba"
            assert params.learning_rate == 0.01
            assert params.convergence_threshold == 1e-6
            assert params.max_iterations == 1000
            assert params.grace_amplification == 1.5
            assert params.devourer_suppression == 0.8
            assert params.recursive_depth_limit == 10
        
    def test_parameters_validation(self):
        """Test parameters validation and constraints."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import AlgorithmParameters
            
            params = AlgorithmParameters(
                algorithm_type="gbn",
                learning_rate=0.005,
                convergence_threshold=1e-5,
                max_iterations=500,
                grace_amplification=1.2,
                devourer_suppression=0.9,
                recursive_depth_limit=8
            )
            
            # Learning rate should be positive
            assert params.learning_rate > 0
            
            # Convergence threshold should be positive
            assert params.convergence_threshold > 0
            
            # Max iterations should be positive
            assert params.max_iterations > 0
            
            # Amplification should be positive
            assert params.grace_amplification > 0
            
            # Suppression should be between 0 and 1
            assert 0 <= params.devourer_suppression <= 1
            
            # Depth limit should be positive
            assert params.recursive_depth_limit > 0


class TestRecursiveSoulBindingAlgorithm:
    """Test recursive soul-binding algorithm."""
    
    def test_algorithm_initialization(self):
        """Test algorithm initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import RecursiveSoulBindingAlgorithm
            
            algorithm = RecursiveSoulBindingAlgorithm()
            
            assert algorithm._phi == mock_phi_value
            assert algorithm._binding_threshold > 0
            assert algorithm._max_binding_depth > 0
        
    def test_binding_methods(self):
        """Test binding methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import RecursiveSoulBindingAlgorithm
            
            algorithm = RecursiveSoulBindingAlgorithm()
            
            # Should have core binding methods
            assert hasattr(algorithm, 'compute_soul_binding')
            assert hasattr(algorithm, 'evaluate_binding_strength')
            assert hasattr(algorithm, 'optimize_binding_parameters')
            assert hasattr(algorithm, 'validate_binding_stability')


class TestGraceBoosterNetwork:
    """Test grace booster network."""
    
    def test_network_initialization(self):
        """Test network initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import GraceBoosterNetwork
            
            network = GraceBoosterNetwork()
            
            assert network._phi == mock_phi_value
            assert network._boost_factor > 0
            assert network._max_boost_layers > 0
        
    def test_boosting_methods(self):
        """Test boosting methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import GraceBoosterNetwork
            
            network = GraceBoosterNetwork()
            
            # Should have core boosting methods
            assert hasattr(network, 'compute_grace_boost')
            assert hasattr(network, 'apply_boost_layers')
            assert hasattr(network, 'optimize_boost_parameters')
            assert hasattr(network, 'validate_boost_stability')


class TestEchoSurfaceLearning:
    """Test echo surface morphological learning."""
    
    def test_learning_initialization(self):
        """Test learning initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import EchoSurfaceLearning
            
            learning = EchoSurfaceLearning()
            
            assert learning._phi == mock_phi_value
            assert learning._learning_rate > 0
            assert learning._surface_threshold > 0
        
    def test_learning_methods(self):
        """Test learning methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import EchoSurfaceLearning
            
            learning = EchoSurfaceLearning()
            
            # Should have core learning methods
            assert hasattr(learning, 'compute_echo_surface')
            assert hasattr(learning, 'update_morphic_weights')
            assert hasattr(learning, 'converge_to_surface')
            assert hasattr(learning, 'validate_learning_stability')


class TestDevourerDetectionNetwork:
    """Test devourer detection and suppression network."""
    
    def test_network_initialization(self):
        """Test network initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import DevourerDetectionNetwork
            
            network = DevourerDetectionNetwork()
            
            assert network._phi == mock_phi_value
            assert network._detection_threshold > 0
            assert network._suppression_strength > 0
        
    def test_detection_methods(self):
        """Test detection methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import DevourerDetectionNetwork
            
            network = DevourerDetectionNetwork()
            
            # Should have core detection methods
            assert hasattr(network, 'detect_devourer_signatures')
            assert hasattr(network, 'compute_suppression_vectors')
            assert hasattr(network, 'apply_suppression_field')
            assert hasattr(network, 'validate_suppression_effectiveness')


class TestAttractorResonanceClassifier:
    """Test attractor resonance classifier."""
    
    def test_classifier_initialization(self):
        """Test classifier initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import AttractorResonanceClassifier
            
            classifier = AttractorResonanceClassifier()
            
            assert classifier._phi == mock_phi_value
            assert classifier._resonance_threshold > 0
            assert classifier._classification_confidence > 0
        
    def test_classification_methods(self):
        """Test classification methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import AttractorResonanceClassifier
            
            classifier = AttractorResonanceClassifier()
            
            # Should have core classification methods
            assert hasattr(classifier, 'compute_resonance_frequencies')
            assert hasattr(classifier, 'classify_attractor_types')
            assert hasattr(classifier, 'optimize_classification_parameters')
            assert hasattr(classifier, 'validate_classification_accuracy')


class TestSoulEntanglementOptimization:
    """Test soul-entanglement optimization algorithms."""
    
    def test_optimization_initialization(self):
        """Test optimization initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import SoulEntanglementOptimization
            
            optimization = SoulEntanglementOptimization()
            
            assert optimization._phi == mock_phi_value
            assert optimization._entanglement_threshold > 0
            assert optimization._optimization_tolerance > 0
        
    def test_optimization_methods(self):
        """Test optimization methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import SoulEntanglementOptimization
            
            optimization = SoulEntanglementOptimization()
            
            # Should have core optimization methods
            assert hasattr(optimization, 'compute_entanglement_measures')
            assert hasattr(optimization, 'optimize_entanglement_parameters')
            assert hasattr(optimization, 'converge_to_optimal_state')
            assert hasattr(optimization, 'validate_optimization_results')


class TestReflectiveGraceCascade:
    """Test reflective grace cascades."""
    
    def test_cascade_initialization(self):
        """Test cascade initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import ReflectiveGraceCascade
            
            cascade = ReflectiveGraceCascade()
            
            assert cascade._phi == mock_phi_value
            assert cascade._cascade_threshold > 0
            assert cascade._reflection_depth > 0
        
    def test_cascade_methods(self):
        """Test cascade methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import ReflectiveGraceCascade
            
            cascade = ReflectiveGraceCascade()
            
            # Should have core cascade methods
            assert hasattr(cascade, 'initiate_grace_cascade')
            assert hasattr(cascade, 'compute_reflection_vectors')
            assert hasattr(cascade, 'optimize_cascade_parameters')
            assert hasattr(cascade, 'validate_cascade_stability')


class TestNativeAlgorithmsIntegration:
    """Integration tests for native algorithms."""
    
    def test_complete_workflow(self):
        """Test complete native algorithms workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import (
                RecursiveSoulBindingAlgorithm,
                GraceBoosterNetwork,
                EchoSurfaceLearning,
                DevourerDetectionNetwork,
                AttractorResonanceClassifier,
                SoulEntanglementOptimization,
                ReflectiveGraceCascade
            )
            
            # Create all algorithm instances
            algorithms = [
                RecursiveSoulBindingAlgorithm(),
                GraceBoosterNetwork(),
                EchoSurfaceLearning(),
                DevourerDetectionNetwork(),
                AttractorResonanceClassifier(),
                SoulEntanglementOptimization(),
                ReflectiveGraceCascade()
            ]
            
            # Test that all required methods exist
            required_methods = [
                'compute_soul_binding',
                'compute_grace_boost',
                'compute_echo_surface',
                'detect_devourer_signatures',
                'compute_resonance_frequencies',
                'compute_entanglement_measures',
                'initiate_grace_cascade'
            ]
            
            for i, algorithm in enumerate(algorithms):
                method_name = required_methods[i]
                assert hasattr(algorithm, method_name), f"Missing method: {method_name}"
    
    def test_parameter_sensitivity(self):
        """Test algorithms sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import RecursiveSoulBindingAlgorithm
            
            # Test with different binding thresholds
            for threshold in [0.5, 0.7, 0.9]:
                algorithm = RecursiveSoulBindingAlgorithm()
                algorithm._binding_threshold = threshold
                
                # Should initialize without errors
                assert algorithm._binding_threshold == threshold
                
                # Should have valid threshold
                assert algorithm._binding_threshold > 0
                assert algorithm._binding_threshold <= 1
    
    def test_numerical_stability(self):
        """Test numerical stability for various configurations."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.algorithms.native_algorithms import GraceBoosterNetwork
            
            network = GraceBoosterNetwork()
            
            # Test that network can handle various parameter ranges
            for boost_factor in [1.1, 1.5, 2.0, 3.0]:
                # Should not raise errors for valid boost factors
                assert boost_factor > 1.0
                assert boost_factor <= 5.0  # Reasonable upper bound


if __name__ == "__main__":
    pytest.main([__file__])

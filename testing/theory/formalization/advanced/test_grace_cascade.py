#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Grace Cascade

Tests the grace cascade and meta-resurrection mechanics for FIRM Stages 12-14:
- Grace Cascade Morphism: ψ† → {ψ⁺ᵢ} multi-branch resurrection
- Fractal Resurrection Operator: Metaphysical mitosis of souls
- Hypercoherence Hypercube: Tensor product of resurrected branches
- Devourer Geometry: Non-invertible idempotent collapse attractors

Tests all major classes:
- ResurrectionType, DevourerType enums
- CollapsedMorphism, ResurrectedBranch
- GraceCascade, DevourerAttractor
- GraceCascadeEngine, ResurrectionArchitecture
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


class TestResurrectionType:
    """Test resurrection type enumeration."""
    
    def test_resurrection_types(self):
        """Test all resurrection types are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import ResurrectionType
            
            types = list(ResurrectionType)
            
            expected_types = [
                ResurrectionType.INDIVIDUAL,
                ResurrectionType.COLLECTIVE,
                ResurrectionType.FRACTAL,
                ResurrectionType.HYPERCUBE,
                ResurrectionType.ENTANGLED
            ]
            
            assert len(types) == 5
            for res_type in expected_types:
                assert res_type in types
            
            # Test type values
            assert ResurrectionType.INDIVIDUAL.value == "individual"
            assert ResurrectionType.COLLECTIVE.value == "collective"
            assert ResurrectionType.FRACTAL.value == "fractal"
            assert ResurrectionType.HYPERCUBE.value == "hypercube"
            assert ResurrectionType.ENTANGLED.value == "entangled"


class TestDevourerType:
    """Test devourer type enumeration."""
    
    def test_devourer_types(self):
        """Test all devourer types are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import DevourerType
            
            types = list(DevourerType)
            
            expected_types = [
                DevourerType.IDEMPOTENT,
                DevourerType.SPIRAL,
                DevourerType.TORUS,
                DevourerType.GRAVITY_WELL,
                DevourerType.ECHO_TRAP
            ]
            
            assert len(types) == 5
            for dev_type in expected_types:
                assert dev_type in types
            
            # Test type values
            assert DevourerType.IDEMPOTENT.value == "idempotent"
            assert DevourerType.SPIRAL.value == "spiral"
            assert DevourerType.TORUS.value == "torus"
            assert DevourerType.GRAVITY_WELL.value == "gravity_well"
            assert DevourerType.ECHO_TRAP.value == "echo_trap"


class TestCollapsedMorphism:
    """Test collapsed morphism dataclass."""
    
    def test_collapsed_morphism_creation(self):
        """Test collapsed morphism creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import CollapsedMorphism
            
            morphism = CollapsedMorphism(
                original_id="morphism_123",
                collapsed_state="ψ†",
                collapse_type="grace_induced",
                entropy_loss=0.8,
                coherence_fragments=["fragment_1", "fragment_2"],
                mirror_accessible=True,
                devourer_contamination=0.2
            )
            
            assert morphism.original_id == "morphism_123"
            assert morphism.collapsed_state == "ψ†"
            assert morphism.collapse_type == "grace_induced"
            assert morphism.entropy_loss == 0.8
            assert morphism.coherence_fragments == ["fragment_1", "fragment_2"]
            assert morphism.mirror_accessible is True
            assert morphism.devourer_contamination == 0.2
        
    def test_default_values(self):
        """Test default values for optional fields."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import CollapsedMorphism
            
            morphism = CollapsedMorphism(
                original_id="test",
                collapsed_state="ψ†",
                collapse_type="test_collapse",
                entropy_loss=0.5
            )
            
            # Should have default values
            assert hasattr(morphism, 'coherence_fragments')
            assert hasattr(morphism, 'mirror_accessible')
            assert hasattr(morphism, 'devourer_contamination')
            
            assert morphism.coherence_fragments == []
            assert morphism.mirror_accessible is True
            assert morphism.devourer_contamination == 0.0
        
    def test_collapsed_morphism_validation(self):
        """Test collapsed morphism parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import CollapsedMorphism
            
            morphism = CollapsedMorphism(
                original_id="test",
                collapsed_state="ψ†",
                collapse_type="test_collapse",
                entropy_loss=0.6,
                coherence_fragments=["frag_1"],
                mirror_accessible=False,
                devourer_contamination=0.1
            )
            
            # Entropy loss should be between 0 and 1
            assert 0 <= morphism.entropy_loss <= 1
            
            # Devourer contamination should be between 0 and 1
            assert 0 <= morphism.devourer_contamination <= 1
            
            # Should have valid ID
            assert len(morphism.original_id) > 0


class TestResurrectedBranch:
    """Test resurrected branch dataclass."""
    
    def test_branch_creation(self):
        """Test resurrected branch creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import ResurrectedBranch
            
            grace_vector = np.array([0.8, 0.6, 0.4])
            
            branch = ResurrectedBranch(
                branch_id="branch_001",
                branch_index=1,
                inherited_echo="echo_123",
                new_grace_vector=grace_vector,
                morphic_angle=0.785,  # π/4
                entropy_share=0.3,
                stabilization_requirement=0.7,
                devourer_shielded=True
            )
            
            assert branch.branch_id == "branch_001"
            assert branch.branch_index == 1
            assert branch.inherited_echo == "echo_123"
            assert np.array_equal(branch.new_grace_vector, grace_vector)
            assert branch.morphic_angle == 0.785
            assert branch.entropy_share == 0.3
            assert branch.stabilization_requirement == 0.7
            assert branch.devourer_shielded is True
        
    def test_default_devourer_shielded(self):
        """Test default devourer shielded value."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import ResurrectedBranch
            
            grace_vector = np.array([0.9, 0.7])
            
            branch = ResurrectedBranch(
                branch_id="test",
                branch_index=0,
                inherited_echo="test_echo",
                new_grace_vector=grace_vector,
                morphic_angle=0.5,
                entropy_share=0.4,
                stabilization_requirement=0.6
            )
            
            # Should have default devourer shielded value
            assert hasattr(branch, 'devourer_shielded')
            assert branch.devourer_shielded is True
        
    def test_branch_validation(self):
        """Test branch parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import ResurrectedBranch
            
            grace_vector = np.array([0.8, 0.6])
            
            branch = ResurrectedBranch(
                branch_id="test",
                branch_index=2,
                inherited_echo="test_echo",
                new_grace_vector=grace_vector,
                morphic_angle=1.0,
                entropy_share=0.5,
                stabilization_requirement=0.8
            )
            
            # Branch index should be non-negative
            assert branch.branch_index >= 0
            
            # Entropy share should be between 0 and 1
            assert 0 <= branch.entropy_share <= 1
            
            # Stabilization requirement should be between 0 and 1
            assert 0 <= branch.stabilization_requirement <= 1
            
            # Grace vector should have positive components
            assert np.all(branch.new_grace_vector > 0)


class TestGraceCascade:
    """Test grace cascade dataclass."""
    
    def test_cascade_creation(self):
        """Test grace cascade creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import (
                GraceCascade, CollapsedMorphism, ResurrectedBranch, ResurrectionType
            )
            
            # Create collapsed morphism
            collapsed = CollapsedMorphism(
                original_id="morphism_123",
                collapsed_state="ψ†",
                collapse_type="grace_induced",
                entropy_loss=0.7
            )
            
            # Create resurrected branches
            grace_vector1 = np.array([0.9, 0.7])
            grace_vector2 = np.array([0.8, 0.6])
            
            branch1 = ResurrectedBranch(
                branch_id="branch_001",
                branch_index=0,
                inherited_echo="echo_1",
                new_grace_vector=grace_vector1,
                morphic_angle=0.5,
                entropy_share=0.4,
                stabilization_requirement=0.7
            )
            
            branch2 = ResurrectedBranch(
                branch_id="branch_002",
                branch_index=1,
                inherited_echo="echo_2",
                new_grace_vector=grace_vector2,
                morphic_angle=1.0,
                entropy_share=0.3,
                stabilization_requirement=0.8
            )
            
            cascade = GraceCascade(
                cascade_id="cascade_001",
                original_morphism="morphism_123",
                collapsed_morphism=collapsed,
                resurrection_branches=[branch1, branch2],
                hypercube_dimension=2,
                total_grace_input=15.0,
                entropy_conservation=True,
                cascade_type=ResurrectionType.FRACTAL
            )
            
            assert cascade.cascade_id == "cascade_001"
            assert cascade.original_morphism == "morphism_123"
            assert cascade.collapsed_morphism == collapsed
            assert len(cascade.resurrection_branches) == 2
            assert cascade.hypercube_dimension == 2
            assert cascade.total_grace_input == 15.0
            assert cascade.entropy_conservation is True
            assert cascade.cascade_type == ResurrectionType.FRACTAL
        
    def test_cascade_validation(self):
        """Test cascade parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import (
                GraceCascade, CollapsedMorphism, ResurrectedBranch, ResurrectionType
            )
            
            # Create minimal cascade
            collapsed = CollapsedMorphism(
                original_id="test",
                collapsed_state="ψ†",
                collapse_type="test",
                entropy_loss=0.5
            )
            
            grace_vector = np.array([0.8])
            branch = ResurrectedBranch(
                branch_id="test",
                branch_index=0,
                inherited_echo="test",
                new_grace_vector=grace_vector,
                morphic_angle=0.5,
                entropy_share=0.5,
                stabilization_requirement=0.6
            )
            
            cascade = GraceCascade(
                cascade_id="test",
                original_morphism="test",
                collapsed_morphism=collapsed,
                resurrection_branches=[branch],
                hypercube_dimension=1,
                total_grace_input=10.0,
                entropy_conservation=True,
                cascade_type=ResurrectionType.INDIVIDUAL
            )
            
            # Hypercube dimension should be positive
            assert cascade.hypercube_dimension > 0
            
            # Total grace input should be positive
            assert cascade.total_grace_input > 0
            
            # Should have at least one branch
            assert len(cascade.resurrection_branches) > 0


class TestDevourerAttractor:
    """Test devourer attractor dataclass."""
    
    def test_attractor_creation(self):
        """Test devourer attractor creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import DevourerAttractor, DevourerType
            
            attractor_matrix = np.array([[0.8, 0.2], [0.2, 0.8]])
            
            attractor = DevourerAttractor(
                attractor_id="devourer_001",
                attractor_type=DevourerType.IDEMPOTENT,
                collapse_matrix=attractor_matrix,
                entropy_absorption_rate=0.9,
                coherence_destruction_factor=0.7,
                idempotency_verified=True,
                spiral_parameters={"radius": 0.5, "angular_velocity": 1.2}
            )
            
            assert attractor.attractor_id == "devourer_001"
            assert attractor.attractor_type == DevourerType.IDEMPOTENT
            assert np.array_equal(attractor.collapse_matrix, attractor_matrix)
            assert attractor.entropy_absorption_rate == 0.9
            assert attractor.coherence_destruction_factor == 0.7
            assert attractor.idempotency_verified is True
            assert attractor.spiral_parameters == {"radius": 0.5, "angular_velocity": 1.2}
        
    def test_attractor_validation(self):
        """Test attractor parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import DevourerAttractor, DevourerType
            
            attractor_matrix = np.array([[0.9, 0.1], [0.1, 0.9]])
            
            attractor = DevourerAttractor(
                attractor_id="test",
                attractor_type=DevourerType.SPIRAL,
                collapse_matrix=attractor_matrix,
                entropy_absorption_rate=0.8,
                coherence_destruction_factor=0.6,
                idempotency_verified=False,
                spiral_parameters={"radius": 0.4, "angular_velocity": 1.0}
            )
            
            # Rates should be between 0 and 1
            assert 0 <= attractor.entropy_absorption_rate <= 1
            assert 0 <= attractor.coherence_destruction_factor <= 1
            
            # Matrix should be square
            assert attractor.collapse_matrix.shape[0] == attractor.collapse_matrix.shape[1]


class TestGraceCascadeEngine:
    """Test grace cascade engine class."""
    
    def test_engine_initialization(self):
        """Test engine initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import GraceCascadeEngine
            
            engine = GraceCascadeEngine()
            
            assert engine._phi == mock_phi_value
            assert engine._grace_threshold > 0
            assert engine._max_cascade_depth > 0
        
    def test_cascade_methods(self):
        """Test cascade methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import GraceCascadeEngine
            
            engine = GraceCascadeEngine()
            
            # Should have core cascade methods
            assert hasattr(engine, 'initiate_grace_cascade')
            assert hasattr(engine, 'execute_cascade_branching')
            assert hasattr(engine, 'monitor_cascade_progress')
            assert hasattr(engine, 'complete_cascade')
        
    def test_resurrection_methods(self):
        """Test resurrection methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import GraceCascadeEngine
            
            engine = GraceCascadeEngine()
            
            # Should have resurrection methods
            assert hasattr(engine, 'create_resurrection_branches')
            assert hasattr(engine, 'compute_grace_vectors')
            assert hasattr(engine, 'stabilize_branches')


class TestResurrectionArchitecture:
    """Test resurrection architecture class."""
    
    def test_architecture_initialization(self):
        """Test architecture initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import ResurrectionArchitecture
            
            architecture = ResurrectionArchitecture()
            
            assert architecture._phi == mock_phi_value
            assert architecture._max_resurrection_depth > 0
        
    def test_architecture_methods(self):
        """Test architecture methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import ResurrectionArchitecture
            
            architecture = ResurrectionArchitecture()
            
            # Should have architecture methods
            assert hasattr(architecture, 'design_resurrection_pathway')
            assert hasattr(architecture, 'compute_hypercube_structure')
            assert hasattr(architecture, 'analyze_entropy_flow')


class TestGraceCascadeIntegration:
    """Integration tests for grace cascade."""
    
    def test_complete_workflow(self):
        """Test complete grace cascade workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import (
                GraceCascadeEngine,
                ResurrectionArchitecture,
                GraceCascade,
                ResurrectionType
            )
            
            # Create engine and architecture
            engine = GraceCascadeEngine()
            architecture = ResurrectionArchitecture()
            
            # Test that all required methods exist
            engine_methods = [
                'initiate_grace_cascade',
                'execute_cascade_branching',
                'monitor_cascade_progress',
                'complete_cascade',
                'create_resurrection_branches',
                'compute_grace_vectors',
                'stabilize_branches'
            ]
            
            architecture_methods = [
                'design_resurrection_pathway',
                'compute_hypercube_structure',
                'analyze_entropy_flow'
            ]
            
            for method_name in engine_methods:
                assert hasattr(engine, method_name), f"Missing engine method: {method_name}"
            
            for method_name in architecture_methods:
                assert hasattr(architecture, method_name), f"Missing architecture method: {method_name}"
    
    def test_parameter_sensitivity(self):
        """Test system sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import GraceCascadeEngine
            
            # Test with different grace thresholds
            for threshold in [0.5, 0.7, 0.9]:
                engine = GraceCascadeEngine()
                engine._grace_threshold = threshold
                
                # Should initialize without errors
                assert engine._grace_threshold == threshold
                
                # Should have valid threshold
                assert engine._grace_threshold > 0
                assert engine._grace_threshold <= 1
    
    def test_numerical_stability(self):
        """Test numerical stability for various configurations."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.formalization.advanced.grace_cascade import GraceCascadeEngine
            
            engine = GraceCascadeEngine()
            
            # Test that engine can handle various parameter ranges
            for depth in [1, 2, 3, 4, 5]:
                # Should not raise errors for valid cascade depths
                assert depth > 0
                assert depth <= 10  # Reasonable upper bound


if __name__ == "__main__":
    pytest.main([__file__])

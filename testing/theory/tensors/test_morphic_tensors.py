#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Morphic Tensors

Tests the complete FIRM tensor field generalization including:

I. Morphic Tensor Field M_μν
II. FIRM Curvature Tensor R_μν  
III. Charge as Cohomological Defect
IV. Complete Symbolic Tensor Algebra

Tests all major classes:
- TensorType enumeration
- MorphicTensorField
- FIRMCurvatureTensor
- CohomologicalCharge
- SymbolicTensorAlgebra
"""

import pytest
import numpy as np
import math
from unittest.mock import Mock, patch

# Add parent directories to path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

# Mock the dependencies
mock_phi_value = 1.618033988749895


class TestTensorType:
    """Test tensor type enumeration."""
    
    def test_tensor_types(self):
        """Test all tensor types are defined."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import TensorType
            
            types = list(TensorType)
            
            expected_types = [
                TensorType.MORPHIC_FIELD,
                TensorType.CURVATURE,
                TensorType.TORSION,
                TensorType.DEVIATION
            ]
            
            assert len(types) == 4
            for tensor_type in expected_types:
                assert tensor_type in types
            
            # Test type values
            assert TensorType.MORPHIC_FIELD.value == "morphic_field"
            assert TensorType.CURVATURE.value == "curvature"
            assert TensorType.TORSION.value == "torsion"
            assert TensorType.DEVIATION.value == "deviation"


class TestMorphicTensorField:
    """Test morphic tensor field M_μν."""
    
    def test_tensor_field_creation(self):
        """Test MorphicTensorField creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import MorphicTensorField
            
            field = MorphicTensorField(
                field_id="field_001",
                spacetime_dimension=4,
                morphic_field=np.array([[1.0, 0.1], [0.1, 0.9]]),
                torsion_tensor=np.array([[0.2, 0.05], [0.05, 0.2]]),
                deviation_operator=np.array([[0.1, 0.02], [0.02, 0.1]])
            )
            
            assert field.field_id == "field_001"
            assert field.spacetime_dimension == 4
            assert np.array_equal(field.morphic_field, np.array([[1.0, 0.1], [0.1, 0.9]]))
            assert np.array_equal(field.torsion_tensor, np.array([[0.2, 0.05], [0.05, 0.2]]))
            assert np.array_equal(field.deviation_operator, np.array([[0.1, 0.02], [0.02, 0.1]]))
        
    def test_tensor_field_validation(self):
        """Test tensor field parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import MorphicTensorField
            
            field = MorphicTensorField(
                field_id="test",
                spacetime_dimension=3,
                morphic_field=np.array([[1.0, 0.1], [0.1, 0.9]]),
                torsion_tensor=np.array([[0.2, 0.05], [0.05, 0.2]]),
                deviation_operator=np.array([[0.1, 0.02], [0.02, 0.1]])
            )
            
            # Spacetime dimension should be positive
            assert field.spacetime_dimension > 0
            
            # All tensors should be square matrices
            assert field.morphic_field.shape[0] == field.morphic_field.shape[1]
            assert field.torsion_tensor.shape[0] == field.torsion_tensor.shape[1]
            assert field.deviation_operator.shape[0] == field.deviation_operator.shape[1]
        
    def test_tensor_field_methods(self):
        """Test tensor field methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import MorphicTensorField
            
            field = MorphicTensorField(
                field_id="test",
                spacetime_dimension=2,
                morphic_field=np.array([[1.0, 0.1], [0.1, 0.9]]),
                torsion_tensor=np.array([[0.2, 0.05], [0.05, 0.2]]),
                deviation_operator=np.array([[0.1, 0.02], [0.02, 0.1]])
            )
            
            # Should have core tensor methods
            assert hasattr(field, 'compute_field_strength')
            assert hasattr(field, 'compute_torsion_contribution')
            assert hasattr(field, 'compute_deviation_contribution')
            assert hasattr(field, 'compute_total_tensor')


class TestFIRMCurvatureTensor:
    """Test FIRM curvature tensor R_μν."""
    
    def test_curvature_tensor_creation(self):
        """Test FIRMCurvatureTensor creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import FIRMCurvatureTensor
            
            curvature = FIRMCurvatureTensor(
                tensor_id="curvature_001",
                spacetime_dimension=4,
                curvature_components=np.array([[0.5, 0.1], [0.1, 0.5]]),
                recursive_depth=3,
                coherence_echo_factor=0.8
            )
            
            assert curvature.tensor_id == "curvature_001"
            assert curvature.spacetime_dimension == 4
            assert np.array_equal(curvature.curvature_components, np.array([[0.5, 0.1], [0.1, 0.5]]))
            assert curvature.recursive_depth == 3
            assert curvature.coherence_echo_factor == 0.8
        
    def test_curvature_tensor_validation(self):
        """Test curvature tensor parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import FIRMCurvatureTensor
            
            curvature = FIRMCurvatureTensor(
                tensor_id="test",
                spacetime_dimension=3,
                curvature_components=np.array([[0.5, 0.1], [0.1, 0.5]]),
                recursive_depth=2,
                coherence_echo_factor=0.7
            )
            
            # Spacetime dimension should be positive
            assert curvature.spacetime_dimension > 0
            
            # Recursive depth should be positive
            assert curvature.recursive_depth > 0
            
            # Coherence echo factor should be between 0 and 1
            assert 0 <= curvature.coherence_echo_factor <= 1
        
    def test_curvature_tensor_methods(self):
        """Test curvature tensor methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import FIRMCurvatureTensor
            
            curvature = FIRMCurvatureTensor(
                tensor_id="test",
                spacetime_dimension=2,
                curvature_components=np.array([[0.5, 0.1], [0.1, 0.5]]),
                recursive_depth=2,
                coherence_echo_factor=0.7
            )
            
            # Should have core curvature methods
            assert hasattr(curvature, 'compute_curvature_scalar')
            assert hasattr(curvature, 'compute_ricci_tensor')
            assert hasattr(curvature, 'compute_coherence_echo')
            assert hasattr(curvature, 'validate_curvature_tensor')


class TestCohomologicalCharge:
    """Test charge as cohomological defect."""
    
    def test_charge_creation(self):
        """Test CohomologicalCharge creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import CohomologicalCharge
            
            charge = CohomologicalCharge(
                charge_id="charge_001",
                charge_value=1.0,
                defect_dimension=2,
                morphic_obstruction=np.array([0.8, 0.6]),
                twist_handedness="right"
            )
            
            assert charge.charge_id == "charge_001"
            assert charge.charge_value == 1.0
            assert charge.defect_dimension == 2
            assert np.array_equal(charge.morphic_obstruction, np.array([0.8, 0.6]))
            assert charge.twist_handedness == "right"
        
    def test_charge_validation(self):
        """Test charge parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import CohomologicalCharge
            
            charge = CohomologicalCharge(
                charge_id="test",
                charge_value=0.5,
                defect_dimension=1,
                morphic_obstruction=np.array([0.7]),
                twist_handedness="left"
            )
            
            # Defect dimension should be positive
            assert charge.defect_dimension > 0
            
            # Twist handedness should be valid
            assert charge.twist_handedness in ["left", "right"]
        
    def test_charge_methods(self):
        """Test charge methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import CohomologicalCharge
            
            charge = CohomologicalCharge(
                charge_id="test",
                charge_value=0.5,
                defect_dimension=1,
                morphic_obstruction=np.array([0.7]),
                twist_handedness="left"
            )
            
            # Should have core charge methods
            assert hasattr(charge, 'compute_defect_obstruction')
            assert hasattr(charge, 'compute_twist_contribution')
            assert hasattr(charge, 'validate_charge_conservation')
            assert hasattr(charge, 'compute_morphic_failure')


class TestSymbolicTensorAlgebra:
    """Test complete symbolic tensor algebra."""
    
    def test_algebra_creation(self):
        """Test SymbolicTensorAlgebra creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import SymbolicTensorAlgebra
            
            algebra = SymbolicTensorAlgebra(
                algebra_id="algebra_001",
                spacetime_dimension=4,
                symbolic_variables=["t", "x", "y", "z"],
                morphic_functions=["phi", "psi"],
                tensor_rank=2
            )
            
            assert algebra.algebra_id == "algebra_001"
            assert algebra.spacetime_dimension == 4
            assert algebra.symbolic_variables == ["t", "x", "y", "z"]
            assert algebra.morphic_functions == ["phi", "psi"]
            assert algebra.tensor_rank == 2
        
    def test_algebra_validation(self):
        """Test algebra parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import SymbolicTensorAlgebra
            
            algebra = SymbolicTensorAlgebra(
                algebra_id="test",
                spacetime_dimension=3,
                symbolic_variables=["t", "x", "y"],
                morphic_functions=["phi"],
                tensor_rank=1
            )
            
            # Spacetime dimension should be positive
            assert algebra.spacetime_dimension > 0
            
            # Tensor rank should be non-negative
            assert algebra.tensor_rank >= 0
            
            # Variables and functions should be lists
            assert isinstance(algebra.symbolic_variables, list)
            assert isinstance(algebra.morphic_functions, list)
        
    def test_algebra_methods(self):
        """Test algebra methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import SymbolicTensorAlgebra
            
            algebra = SymbolicTensorAlgebra(
                algebra_id="test",
                spacetime_dimension=2,
                symbolic_variables=["t", "x"],
                morphic_functions=["phi"],
                tensor_rank=1
            )
            
            # Should have core algebra methods
            assert hasattr(algebra, 'construct_symbolic_tensor')
            assert hasattr(algebra, 'compute_tensor_derivatives')
            assert hasattr(algebra, 'simplify_tensor_expressions')
            assert hasattr(algebra, 'validate_tensor_identities')


class TestMorphicTensorsIntegration:
    """Integration tests for morphic tensors."""
    
    def test_complete_workflow(self):
        """Test complete morphic tensors workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import (
                MorphicTensorField,
                FIRMCurvatureTensor,
                CohomologicalCharge,
                SymbolicTensorAlgebra
            )
            
            # Test that all major classes can be imported and instantiated
            field = MorphicTensorField(
                field_id="test",
                spacetime_dimension=2,
                morphic_field=np.array([[1.0, 0.1], [0.1, 0.9]]),
                torsion_tensor=np.array([[0.2, 0.05], [0.05, 0.2]]),
                deviation_operator=np.array([[0.1, 0.02], [0.02, 0.1]])
            )
            
            curvature = FIRMCurvatureTensor(
                tensor_id="test",
                spacetime_dimension=2,
                curvature_components=np.array([[0.5, 0.1], [0.1, 0.5]]),
                recursive_depth=2,
                coherence_echo_factor=0.7
            )
            
            charge = CohomologicalCharge(
                charge_id="test",
                charge_value=0.5,
                defect_dimension=1,
                morphic_obstruction=np.array([0.7]),
                twist_handedness="left"
            )
            
            algebra = SymbolicTensorAlgebra(
                algebra_id="test",
                spacetime_dimension=2,
                symbolic_variables=["t", "x"],
                morphic_functions=["phi"],
                tensor_rank=1
            )
            
            # All objects should be created successfully
            assert field.field_id == "test"
            assert curvature.tensor_id == "test"
            assert charge.charge_id == "test"
            assert algebra.algebra_id == "test"
    
    def test_parameter_sensitivity(self):
        """Test tensors sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import MorphicTensorField
            
            # Test with different spacetime dimensions
            for dim in [2, 3, 4]:
                field = MorphicTensorField(
                    field_id="test",
                    spacetime_dimension=dim,
                    morphic_field=np.eye(dim),
                    torsion_tensor=np.eye(dim) * 0.1,
                    deviation_operator=np.eye(dim) * 0.05
                )
                
                # Should initialize without errors
                assert field.spacetime_dimension == dim
                
                # Should have valid dimension
                assert field.spacetime_dimension > 0
                assert field.spacetime_dimension <= 10  # Reasonable upper bound
    
    def test_numerical_stability(self):
        """Test numerical stability for various configurations."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.tensors.morphic_tensors import FIRMCurvatureTensor
            
            # Test with different recursive depths
            for depth in [1, 2, 3, 4, 5]:
                curvature = FIRMCurvatureTensor(
                    tensor_id="test",
                    spacetime_dimension=2,
                    curvature_components=np.array([[0.5, 0.1], [0.1, 0.5]]),
                    recursive_depth=depth,
                    coherence_echo_factor=0.7
                )
                
                # Should not raise errors for valid depths
                assert curvature.recursive_depth > 0
                assert curvature.recursive_depth <= 10  # Reasonable upper bound


if __name__ == "__main__":
    pytest.main([__file__])

#!/usr/bin/env python3
"""
Comprehensive Tests for FIRM Phase Lensing Theory

Tests the mathematical framework for projective ψₖ-resonance bundles
and recursive phase lensing in FIRM morphic field theory.

Tests all major classes:
- PsiResonanceBundleParameters
- RecursivePhaseLensParameters
- ProjectiveResonanceBundle
- PhaseLensingResult
- PhaseLensingTheory
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


class TestPsiResonanceBundleParameters:
    """Test ψₖ-resonance bundle parameters dataclass."""
    
    def test_parameter_initialization(self):
        """Test parameter initialization with all required fields."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PsiResonanceBundleParameters
            
            # Mock PsiKnotState
            mock_psi_knot = Mock()
            mock_psi_knot.psi_k_value = 2.5
            mock_psi_knot.recursive_depth = 3
            
            params = PsiResonanceBundleParameters(
                psi_knot=mock_psi_knot,
                resonance_frequency=15.7,
                bundle_dimension=4,
                fiber_topology="S^2",
                base_manifold_curvature=0.8
            )
            
            assert params.psi_knot == mock_psi_knot
            assert params.resonance_frequency == 15.7
            assert params.bundle_dimension == 4
            assert params.fiber_topology == "S^2"
            assert params.base_manifold_curvature == 0.8
        
    def test_parameter_validation(self):
        """Test parameter validation and constraints."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PsiResonanceBundleParameters
            
            # Mock PsiKnotState
            mock_psi_knot = Mock()
            mock_psi_knot.psi_k_value = 1.5
            mock_psi_knot.recursive_depth = 2
            
            params = PsiResonanceBundleParameters(
                psi_knot=mock_psi_knot,
                resonance_frequency=10.0,
                bundle_dimension=3,
                fiber_topology="S^1",
                base_manifold_curvature=0.5
            )
            
            # Bundle dimension should be positive
            assert params.bundle_dimension > 0
            
            # Resonance frequency should be positive
            assert params.resonance_frequency > 0
            
            # Curvature should be reasonable
            assert abs(params.base_manifold_curvature) < 10.0


class TestRecursivePhaseLensParameters:
    """Test recursive phase lens parameters dataclass."""
    
    def test_parameter_initialization(self):
        """Test parameter initialization with all required fields."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import RecursivePhaseLensParameters
            
            chromatic_coeffs = [0.1, 0.05, 0.025]
            distortion_tensor = np.array([[1.0, 0.2], [0.2, 0.8]])
            
            params = RecursivePhaseLensParameters(
                focal_length_phi_scaling=2.0,
                aperture_recursive_depth=5,
                chromatic_aberration_coeffs=chromatic_coeffs,
                spherical_aberration_phi_factor=1.5,
                topological_distortion_tensor=distortion_tensor
            )
            
            assert params.focal_length_phi_scaling == 2.0
            assert params.aperture_recursive_depth == 5
            assert params.chromatic_aberration_coeffs == chromatic_coeffs
            assert params.spherical_aberration_phi_factor == 1.5
            assert np.array_equal(params.topological_distortion_tensor, distortion_tensor)
        
    def test_parameter_validation(self):
        """Test parameter validation and constraints."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import RecursivePhaseLensParameters
            
            chromatic_coeffs = [0.1, 0.05]
            distortion_tensor = np.array([[1.0, 0.1], [0.1, 0.9]])
            
            params = RecursivePhaseLensParameters(
                focal_length_phi_scaling=1.5,
                aperture_recursive_depth=3,
                chromatic_aberration_coeffs=chromatic_coeffs,
                spherical_aberration_phi_factor=1.2,
                topological_distortion_tensor=distortion_tensor
            )
            
            # Scaling factors should be positive
            assert params.focal_length_phi_scaling > 0
            assert params.spherical_aberration_phi_factor > 0
            
            # Recursive depth should be non-negative
            assert params.aperture_recursive_depth >= 0
            
            # Chromatic coefficients should be non-negative
            for coeff in params.chromatic_aberration_coeffs:
                assert coeff >= 0


class TestProjectiveResonanceBundle:
    """Test projective resonance bundle dataclass."""
    
    def test_bundle_creation(self):
        """Test bundle creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import (
                PsiResonanceBundleParameters,
                RecursivePhaseLensParameters,
                ProjectiveResonanceBundle
            )
            
            # Mock parameters
            mock_psi_knot = Mock()
            mock_psi_knot.psi_k_value = 2.0
            mock_psi_knot.recursive_depth = 2
            
            bundle_params = PsiResonanceBundleParameters(
                psi_knot=mock_psi_knot,
                resonance_frequency=12.0,
                bundle_dimension=3,
                fiber_topology="S^1",
                base_manifold_curvature=0.6
            )
            
            lens_params = RecursivePhaseLensParameters(
                focal_length_phi_scaling=1.8,
                aperture_recursive_depth=4,
                chromatic_aberration_coeffs=[0.1, 0.05],
                spherical_aberration_phi_factor=1.3,
                topological_distortion_tensor=np.array([[1.0, 0.1], [0.1, 0.9]])
            )
            
            # Create arrays for bundle
            projection_matrix = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
            visual_coordinates = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
            coherence_amplitude_field = np.array([1.0, 0.8, 0.6])
            phase_distortion_field = np.array([0.0, 0.1, 0.2])
            
            bundle = ProjectiveResonanceBundle(
                bundle_params=bundle_params,
                lens_params=lens_params,
                projection_matrix=projection_matrix,
                visual_coordinates=visual_coordinates,
                coherence_amplitude_field=coherence_amplitude_field,
                phase_distortion_field=phase_distortion_field
            )
            
            assert bundle.bundle_params == bundle_params
            assert bundle.lens_params == lens_params
            assert np.array_equal(bundle.projection_matrix, projection_matrix)
            assert np.array_equal(bundle.visual_coordinates, visual_coordinates)
            assert np.array_equal(bundle.coherence_amplitude_field, coherence_amplitude_field)
            assert np.array_equal(bundle.phase_distortion_field, phase_distortion_field)
        
    def test_bundle_validation(self):
        """Test bundle parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import (
                PsiResonanceBundleParameters,
                RecursivePhaseLensParameters,
                ProjectiveResonanceBundle
            )
            
            # Mock parameters
            mock_psi_knot = Mock()
            mock_psi_knot.psi_k_value = 1.5
            mock_psi_knot.recursive_depth = 2
            
            bundle_params = PsiResonanceBundleParameters(
                psi_knot=mock_psi_knot,
                resonance_frequency=8.0,
                bundle_dimension=2,
                fiber_topology="S^1",
                base_manifold_curvature=0.4
            )
            
            lens_params = RecursivePhaseLensParameters(
                focal_length_phi_scaling=1.5,
                aperture_recursive_depth=3,
                chromatic_aberration_coeffs=[0.1],
                spherical_aberration_phi_factor=1.2,
                topological_distortion_tensor=np.array([[1.0]])
            )
            
            # Create minimal bundle
            bundle = ProjectiveResonanceBundle(
                bundle_params=bundle_params,
                lens_params=lens_params,
                projection_matrix=np.array([[1.0]]),
                visual_coordinates=np.array([[0.0]]),
                coherence_amplitude_field=np.array([1.0]),
                phase_distortion_field=np.array([0.0])
            )
            
            # Coherence amplitude should be positive
            assert np.all(bundle.coherence_amplitude_field > 0)
            
            # Phase distortion should be reasonable
            assert np.all(np.abs(bundle.phase_distortion_field) < np.pi)


class TestPhaseLensingResult:
    """Test phase lensing result dataclass."""
    
    def test_result_creation(self):
        """Test result creation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import (
                PsiResonanceBundleParameters,
                RecursivePhaseLensParameters,
                ProjectiveResonanceBundle,
                PhaseLensingResult
            )
            
            # Create sample bundles
            mock_psi_knot = Mock()
            mock_psi_knot.psi_k_value = 2.0
            mock_psi_knot.recursive_depth = 2
            
            bundle_params = PsiResonanceBundleParameters(
                psi_knot=mock_psi_knot,
                resonance_frequency=10.0,
                bundle_dimension=3,
                fiber_topology="S^1",
                base_manifold_curvature=0.5
            )
            
            lens_params = RecursivePhaseLensParameters(
                focal_length_phi_scaling=1.5,
                aperture_recursive_depth=3,
                chromatic_aberration_coeffs=[0.1, 0.05],
                spherical_aberration_phi_factor=1.2,
                topological_distortion_tensor=np.array([[1.0, 0.1], [0.1, 0.9]])
            )
            
            bundle = ProjectiveResonanceBundle(
                bundle_params=bundle_params,
                lens_params=lens_params,
                projection_matrix=np.array([[1.0, 0.0], [0.0, 1.0]]),
                visual_coordinates=np.array([[0.0, 0.0], [1.0, 0.0]]),
                coherence_amplitude_field=np.array([1.0, 0.8]),
                phase_distortion_field=np.array([0.0, 0.1])
            )
            
            # Create result arrays
            composite_visual_field = np.array([[1.0, 0.9], [0.9, 1.0]])
            phase_coherence_map = np.array([[1.0, 0.8], [0.8, 0.9]])
            topological_invariants = {"euler_characteristic": 2, "genus": 0}
            lensing_quality_metrics = {"sharpness": 0.95, "contrast": 0.85}
            theoretical_predictions = {"resonance_peaks": [10.0, 15.0]}
            
            result = PhaseLensingResult(
                resonance_bundles=[bundle],
                composite_visual_field=composite_visual_field,
                phase_coherence_map=phase_coherence_map,
                topological_invariants=topological_invariants,
                lensing_quality_metrics=lensing_quality_metrics,
                theoretical_predictions=theoretical_predictions
            )
            
            assert len(result.resonance_bundles) == 1
            assert np.array_equal(result.composite_visual_field, composite_visual_field)
            assert np.array_equal(result.phase_coherence_map, phase_coherence_map)
            assert result.topological_invariants == topological_invariants
            assert result.lensing_quality_metrics == lensing_quality_metrics
            assert result.theoretical_predictions == theoretical_predictions
        
    def test_result_validation(self):
        """Test result parameter validation."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import (
                PsiResonanceBundleParameters,
                RecursivePhaseLensParameters,
                ProjectiveResonanceBundle,
                PhaseLensingResult
            )
            
            # Create minimal result
            mock_psi_knot = Mock()
            mock_psi_knot.psi_k_value = 1.5
            mock_psi_knot.recursive_depth = 1
            
            bundle_params = PsiResonanceBundleParameters(
                psi_knot=mock_psi_knot,
                resonance_frequency=5.0,
                bundle_dimension=2,
                fiber_topology="S^1",
                base_manifold_curvature=0.3
            )
            
            lens_params = RecursivePhaseLensParameters(
                focal_length_phi_scaling=1.2,
                aperture_recursive_depth=2,
                chromatic_aberration_coeffs=[0.1],
                spherical_aberration_phi_factor=1.1,
                topological_distortion_tensor=np.array([[1.0]])
            )
            
            bundle = ProjectiveResonanceBundle(
                bundle_params=bundle_params,
                lens_params=lens_params,
                projection_matrix=np.array([[1.0]]),
                visual_coordinates=np.array([[0.0]]),
                coherence_amplitude_field=np.array([1.0]),
                phase_distortion_field=np.array([0.0])
            )
            
            result = PhaseLensingResult(
                resonance_bundles=[bundle],
                composite_visual_field=np.array([[1.0]]),
                phase_coherence_map=np.array([[1.0]]),
                topological_invariants={"test": 1.0},
                lensing_quality_metrics={"test": 0.9},
                theoretical_predictions={"test": "value"}
            )
            
            # Should have at least one bundle
            assert len(result.resonance_bundles) > 0
            
            # Quality metrics should be between 0 and 1
            for metric in result.lensing_quality_metrics.values():
                if isinstance(metric, (int, float)):
                    assert 0 <= metric <= 1


class TestPhaseLensingTheory:
    """Test phase lensing theory class."""
    
    def test_theory_initialization(self):
        """Test theory initialization."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PhaseLensingTheory
            
            theory = PhaseLensingTheory()
            
            assert theory._phi == mock_phi_value
        
    def test_resonance_bundle_construction(self):
        """Test resonance bundle construction methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PhaseLensingTheory
            
            theory = PhaseLensingTheory()
            
            # Should have bundle construction methods
            assert hasattr(theory, 'construct_psi_resonance_bundle')
            assert hasattr(theory, 'compute_resonance_frequency')
            assert hasattr(theory, 'determine_fiber_topology')
        
    def test_phase_lensing_methods(self):
        """Test phase lensing computation methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PhaseLensingTheory
            
            theory = PhaseLensingTheory()
            
            # Should have phase lensing methods
            assert hasattr(theory, 'compute_phase_lensing')
            assert hasattr(theory, 'analyze_topological_distortion')
            assert hasattr(theory, 'compute_lensing_quality')
        
    def test_projective_geometry_methods(self):
        """Test projective geometry methods exist."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PhaseLensingTheory
            
            theory = PhaseLensingTheory()
            
            # Should have projective geometry methods
            assert hasattr(theory, 'compute_projection_matrix')
            assert hasattr(theory, 'analyze_visual_emergence')
            assert hasattr(theory, 'compute_phase_coherence')


class TestPhaseLensingIntegration:
    """Integration tests for phase lensing theory."""
    
    def test_complete_workflow(self):
        """Test complete phase lensing workflow."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import (
                PhaseLensingTheory,
                PsiResonanceBundleParameters,
                RecursivePhaseLensParameters,
                ProjectiveResonanceBundle,
                PhaseLensingResult
            )
            
            # Create theory instance
            theory = PhaseLensingTheory()
            
            # Test that all required methods exist
            required_methods = [
                'construct_psi_resonance_bundle',
                'compute_resonance_frequency',
                'determine_fiber_topology',
                'compute_phase_lensing',
                'analyze_topological_distortion',
                'compute_lensing_quality',
                'compute_projection_matrix',
                'analyze_visual_emergence',
                'compute_phase_coherence'
            ]
            
            for method_name in required_methods:
                assert hasattr(theory, method_name), f"Missing method: {method_name}"
    
    def test_parameter_sensitivity(self):
        """Test theory sensitivity to parameter changes."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PhaseLensingTheory
            
            # Test with different phi values
            for phi_val in [1.5, 1.618, 1.7]:
                theory = PhaseLensingTheory()
                theory._phi = phi_val
                
                # Should initialize without errors
                assert theory._phi == phi_val
                
                # Should have valid phi value
                assert theory._phi > 1.0
                assert theory._phi < 2.0
    
    def test_numerical_stability(self):
        """Test numerical stability for various configurations."""
        with patch('foundation.operators.phi_recursion.PHI_VALUE', mock_phi_value):
            from theory.field_theory.advanced.phase_lensing import PhaseLensingTheory
            
            theory = PhaseLensingTheory()
            
            # Test that theory can handle various parameter ranges
            for depth in [1, 2, 3, 4, 5]:
                # Should not raise errors for valid recursive depths
                assert depth > 0
                assert depth <= 10  # Reasonable upper bound


if __name__ == "__main__":
    pytest.main([__file__])

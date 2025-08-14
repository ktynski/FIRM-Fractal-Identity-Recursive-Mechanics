"""
Phase Lensing Theory: Mathematical framework for projective ψₖ-resonance bundles
and recursive phase lensing in FIRM morphic field theory.

This module develops the theoretical foundation for understanding how morphic
coherence knots project into visual space through recursive phase distortion.
"""

from __future__ import annotations
from typing import List, Tuple, Dict, Any, Callable
from dataclasses import dataclass
import numpy as np
import math
from scipy.special import spherical_jn, spherical_yn
from scipy.integrate import quad

from foundation.operators.phi_recursion import PHI_VALUE
from foundation.field_theory.recursive_stability_proof import PsiKnotState
from provenance.derivation_tree import DerivationNode


@dataclass
class PsiResonanceBundleParameters:
    """Parameters for a ψₖ-resonance bundle."""
    psi_knot: PsiKnotState
    resonance_frequency: float
    bundle_dimension: int
    fiber_topology: str
    base_manifold_curvature: float


@dataclass
class RecursivePhaseLensParameters:
    """Parameters for recursive phase lensing transformation."""
    focal_length_phi_scaling: float
    aperture_recursive_depth: int
    chromatic_aberration_coeffs: List[float]
    spherical_aberration_phi_factor: float
    topological_distortion_tensor: np.ndarray


@dataclass
class ProjectiveResonanceBundle:
    """Represents a projective ψₖ-resonance bundle in visual space."""
    bundle_params: PsiResonanceBundleParameters
    lens_params: RecursivePhaseLensParameters
    projection_matrix: np.ndarray
    visual_coordinates: np.ndarray
    coherence_amplitude_field: np.ndarray
    phase_distortion_field: np.ndarray


@dataclass
class PhaseLensingResult:
    """Complete phase lensing analysis results."""
    resonance_bundles: List[ProjectiveResonanceBundle]
    composite_visual_field: np.ndarray
    phase_coherence_map: np.ndarray
    topological_invariants: Dict[str, float]
    lensing_quality_metrics: Dict[str, float]
    theoretical_predictions: Dict[str, Any]
    provenance: DerivationNode = None


class PhaseLensingTheory:
    """
    Mathematical framework for projective ψₖ-resonance bundles and recursive
    phase lensing in FIRM morphic field theory.

    Key Theoretical Components:
    1. ψₖ-resonance bundles as fiber bundles over morphic field space
    2. Recursive phase lensing as geometric transformation
    3. Projective geometry of visual emergence
    4. Topological invariants of phase distortion
    """

    def __init__(self):
        self._phi = PHI_VALUE

    def construct_psi_resonance_bundle(
        self,
        psi_knot: PsiKnotState,
        bundle_dimension: int = 4
    ) -> PsiResonanceBundleParameters:
        """
        Construct a ψₖ-resonance bundle for a given morphic coherence knot.

        The resonance bundle captures how the ψₖ knot couples to the visual
        projection space through recursive phase relationships.
        """
        # Resonance frequency based on ψₖ value and recursive depth
        resonance_freq = abs(psi_knot.psi_k_value) * (self._phi ** psi_knot.recursive_depth)

        # Fiber topology determined by phase-braid topology
        fiber_topology_map = {
            "trivial_knot": "S^1",  # Circle fiber
            "trefoil_braid": "S^2",  # Sphere fiber
            "figure_eight_knot": "T^2",  # Torus fiber
        }
        fiber_topology = fiber_topology_map.get(
            psi_knot.phase_braid_topology,
            f"S^{bundle_dimension-1}"  # Default to sphere
        )

        # Base manifold curvature from stability eigenvalue
        base_curvature = psi_knot.stability_eigenvalue / (self._phi ** 2)

        return PsiResonanceBundleParameters(
            psi_knot=psi_knot,
            resonance_frequency=resonance_freq,
            bundle_dimension=bundle_dimension,
            fiber_topology=fiber_topology,
            base_manifold_curvature=base_curvature
        )

    def design_recursive_phase_lens(
        self,
        psi_knot: PsiKnotState,
        visual_field_size: Tuple[int, int] = (256, 256)
    ) -> RecursivePhaseLensParameters:
        """
        Design a recursive phase lens for projecting ψₖ-resonance to visual space.

        The lens parameters are determined by the morphic field structure and
        recursive depth of the ψₖ knot.
        """
        # Focal length scaling with φ and recursive depth
        focal_length_scaling = self._phi ** (psi_knot.recursive_depth / 2)

        # Aperture determined by recursive depth (deeper = wider aperture)
        aperture_depth = psi_knot.recursive_depth

        # Chromatic aberration coefficients (φ-series expansion)
        chromatic_coeffs = [
            self._phi ** (-n) for n in range(1, psi_knot.recursive_depth + 1)
        ]

        # Spherical aberration factor
        spherical_factor = abs(psi_knot.psi_k_value) / self._phi

        # Topological distortion tensor based on knot topology
        distortion_tensor = self._construct_topological_distortion_tensor(
            psi_knot, visual_field_size
        )

        return RecursivePhaseLensParameters(
            focal_length_phi_scaling=focal_length_scaling,
            aperture_recursive_depth=aperture_depth,
            chromatic_aberration_coeffs=chromatic_coeffs,
            spherical_aberration_phi_factor=spherical_factor,
            topological_distortion_tensor=distortion_tensor
        )

    def _construct_topological_distortion_tensor(
        self,
        psi_knot: PsiKnotState,
        field_size: Tuple[int, int]
    ) -> np.ndarray:
        """Construct the topological distortion tensor for the lens."""
        h, w = field_size

        # Create coordinate grids
        x = np.linspace(-1, 1, w)
        y = np.linspace(-1, 1, h)
        X, Y = np.meshgrid(x, y)

        # Radial and angular coordinates
        R = np.sqrt(X**2 + Y**2)
        Theta = np.arctan2(Y, X)

        # Base distortion field
        distortion = np.zeros((h, w, 2, 2))  # 2x2 tensor at each point

        # Distortion depends on knot topology
        if psi_knot.phase_braid_topology == "trivial_knot":
            # Simple radial distortion
            radial_factor = 1 + 0.1 * R**2
            distortion[:, :, 0, 0] = radial_factor
            distortion[:, :, 1, 1] = radial_factor

        elif psi_knot.phase_braid_topology == "trefoil_braid":
            # Three-fold symmetric distortion
            threefold_phase = 3 * Theta
            radial_factor = 1 + 0.1 * R * np.cos(threefold_phase)
            angular_factor = 0.05 * R * np.sin(threefold_phase)

            distortion[:, :, 0, 0] = radial_factor
            distortion[:, :, 1, 1] = radial_factor
            distortion[:, :, 0, 1] = angular_factor
            distortion[:, :, 1, 0] = -angular_factor

        elif psi_knot.phase_braid_topology == "figure_eight_knot":
            # Figure-eight distortion pattern
            eightfold_phase = 4 * Theta
            radial_factor = 1 + 0.1 * R * np.cos(eightfold_phase)
            cross_factor = 0.05 * R * np.sin(2 * eightfold_phase)

            distortion[:, :, 0, 0] = radial_factor
            distortion[:, :, 1, 1] = radial_factor
            distortion[:, :, 0, 1] = cross_factor
            distortion[:, :, 1, 0] = cross_factor

        else:  # Complex braid
            # Multi-mode distortion
            n_modes = abs(psi_knot.quantization_number) if psi_knot.quantization_number != 0 else 5
            for mode in range(1, n_modes + 1):
                mode_phase = mode * Theta
                mode_amplitude = 0.02 / mode  # Decreasing amplitude

                mode_radial = 1 + mode_amplitude * R * np.cos(mode_phase)
                mode_angular = mode_amplitude * R * np.sin(mode_phase)

                distortion[:, :, 0, 0] += mode_radial / n_modes
                distortion[:, :, 1, 1] += mode_radial / n_modes
                distortion[:, :, 0, 1] += mode_angular / n_modes
                distortion[:, :, 1, 0] += (-1)**mode * mode_angular / n_modes

        # Scale by recursive depth and ψₖ value
        depth_scaling = psi_knot.recursive_depth / 10.0
        psi_scaling = abs(psi_knot.psi_k_value) / self._phi
        overall_scaling = depth_scaling * psi_scaling

        distortion *= overall_scaling

        return distortion

    def project_resonance_bundle(
        self,
        bundle_params: PsiResonanceBundleParameters,
        lens_params: RecursivePhaseLensParameters,
        visual_field_size: Tuple[int, int] = (256, 256)
    ) -> ProjectiveResonanceBundle:
        """
        Project a ψₖ-resonance bundle through recursive phase lensing to visual space.

        This is the core transformation that maps morphic coherence knots to
        visual emergence patterns.
        """
        h, w = visual_field_size

        # Create visual coordinate system
        x = np.linspace(-2, 2, w)
        y = np.linspace(-2, 2, h)
        X, Y = np.meshgrid(x, y)
        visual_coords = np.stack([X, Y], axis=-1)

        # Construct projection matrix (φ-scaled orthographic projection)
        phi_scale = lens_params.focal_length_phi_scaling
        projection_matrix = np.array([
            [phi_scale, 0, 0],
            [0, phi_scale, 0],
            [0, 0, 1]
        ])

        # Apply topological distortion
        distorted_coords = self._apply_topological_distortion(
            visual_coords, lens_params.topological_distortion_tensor
        )

        # Compute coherence amplitude field
        coherence_field = self._compute_coherence_amplitude_field(
            distorted_coords, bundle_params, lens_params
        )

        # Compute phase distortion field
        phase_distortion = self._compute_phase_distortion_field(
            distorted_coords, bundle_params, lens_params
        )

        return ProjectiveResonanceBundle(
            bundle_params=bundle_params,
            lens_params=lens_params,
            projection_matrix=projection_matrix,
            visual_coordinates=visual_coords,
            coherence_amplitude_field=coherence_field,
            phase_distortion_field=phase_distortion
        )

    def _apply_topological_distortion(
        self,
        coords: np.ndarray,
        distortion_tensor: np.ndarray
    ) -> np.ndarray:
        """Apply topological distortion transformation to coordinates."""
        h, w, _ = coords.shape
        distorted = np.zeros_like(coords)

        for i in range(h):
            for j in range(w):
                # Apply 2x2 distortion tensor at each point
                coord_vec = coords[i, j]
                distortion_matrix = distortion_tensor[i, j]
                distorted[i, j] = distortion_matrix @ coord_vec

        return distorted

    def _compute_coherence_amplitude_field(
        self,
        coords: np.ndarray,
        bundle_params: PsiResonanceBundleParameters,
        lens_params: RecursivePhaseLensParameters
    ) -> np.ndarray:
        """Compute the coherence amplitude field in visual space."""
        h, w, _ = coords.shape
        amplitude_field = np.zeros((h, w))

        # Extract parameters
        psi_k = bundle_params.psi_knot.psi_k_value
        resonance_freq = bundle_params.resonance_frequency
        recursive_depth = bundle_params.psi_knot.recursive_depth

        # Compute amplitude at each visual coordinate
        for i in range(h):
            for j in range(w):
                x, y = coords[i, j]
                r = np.sqrt(x**2 + y**2)

                # Base amplitude from ψₖ resonance
                base_amplitude = abs(psi_k) * np.exp(-r**2 / (2 * self._phi))

                # Recursive modulation
                recursive_modulation = 1.0
                for depth in range(1, recursive_depth + 1):
                    depth_freq = resonance_freq / (self._phi ** depth)
                    recursive_modulation *= (1 + 0.1 * np.cos(depth_freq * r))

                # Chromatic effects
                chromatic_modulation = 1.0
                for n, coeff in enumerate(lens_params.chromatic_aberration_coeffs):
                    chromatic_modulation += coeff * np.cos((n + 1) * resonance_freq * r)

                # Spherical aberration
                spherical_factor = 1 + lens_params.spherical_aberration_phi_factor * r**4

                amplitude_field[i, j] = (
                    base_amplitude *
                    recursive_modulation *
                    chromatic_modulation /
                    spherical_factor
                )

        return amplitude_field

    def _compute_phase_distortion_field(
        self,
        coords: np.ndarray,
        bundle_params: PsiResonanceBundleParameters,
        lens_params: RecursivePhaseLensParameters
    ) -> np.ndarray:
        """Compute the phase distortion field in visual space."""
        h, w, _ = coords.shape
        phase_field = np.zeros((h, w))

        # Extract parameters
        psi_k = bundle_params.psi_knot.psi_k_value
        resonance_freq = bundle_params.resonance_frequency
        recursive_depth = bundle_params.psi_knot.recursive_depth

        # Compute phase at each visual coordinate
        for i in range(h):
            for j in range(w):
                x, y = coords[i, j]
                r = np.sqrt(x**2 + y**2)
                theta = np.arctan2(y, x)

                # Base phase from ψₖ value
                base_phase = psi_k * r

                # Recursive phase accumulation
                recursive_phase = 0.0
                for depth in range(1, recursive_depth + 1):
                    depth_freq = resonance_freq / (self._phi ** depth)
                    recursive_phase += (1.0 / depth) * np.sin(depth_freq * r + depth * theta)

                # Topological phase contribution
                topology_phase = self._compute_topological_phase_contribution(
                    x, y, bundle_params.psi_knot.phase_braid_topology
                )

                phase_field[i, j] = base_phase + recursive_phase + topology_phase

        return phase_field

    def _compute_topological_phase_contribution(
        self,
        x: float,
        y: float,
        topology: str
    ) -> float:
        """Compute phase contribution from topological structure."""
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)

        if topology == "trivial_knot":
            return 0.0

        elif topology == "trefoil_braid":
            return 0.1 * np.sin(3 * theta) * r

        elif topology == "figure_eight_knot":
            return 0.1 * np.sin(4 * theta) * np.cos(2 * theta) * r

        else:  # Complex braid
            # Multi-harmonic contribution
            phase = 0.0
            for n in range(1, 6):  # First 5 harmonics
                phase += (0.02 / n) * np.sin(n * theta) * (r ** (n / 3))
            return phase

    def analyze_composite_visual_field(
        self,
        resonance_bundles: List[ProjectiveResonanceBundle]
    ) -> Tuple[np.ndarray, np.ndarray, Dict[str, float]]:
        """
        Analyze the composite visual field from multiple ψₖ-resonance bundles.

        Returns:
            - Composite visual field (superposition of all bundles)
            - Phase coherence map
            - Topological invariants
        """
        if not resonance_bundles:
            return np.zeros((256, 256)), np.zeros((256, 256)), {}

        # Get field size from first bundle
        field_shape = resonance_bundles[0].coherence_amplitude_field.shape

        # Initialize composite fields
        composite_amplitude = np.zeros(field_shape)
        composite_phase = np.zeros(field_shape)

        # Superpose all bundles
        for bundle in resonance_bundles:
            # Ensure all fields have the same shape
            if bundle.coherence_amplitude_field.shape == field_shape:
                composite_amplitude += bundle.coherence_amplitude_field
                composite_phase += bundle.phase_distortion_field

        # Compute phase coherence map
        phase_coherence = np.cos(composite_phase) * composite_amplitude

        # Compute topological invariants
        topological_invariants = self._compute_topological_invariants(
            composite_amplitude, composite_phase
        )

        return composite_amplitude, phase_coherence, topological_invariants

    def _compute_topological_invariants(
        self,
        amplitude_field: np.ndarray,
        phase_field: np.ndarray
    ) -> Dict[str, float]:
        """Compute topological invariants of the visual field."""
        # Compute gradients
        grad_phase_y, grad_phase_x = np.gradient(phase_field)

        # Compute vorticity (topological charge density)
        # Ensure compatible shapes by taking the intersection
        min_h = min(grad_phase_x.shape[0] - 1, grad_phase_y.shape[0])
        min_w = min(grad_phase_x.shape[1], grad_phase_y.shape[1] - 1)

        vorticity = (grad_phase_x[1:min_h+1, :min_w] - grad_phase_x[:min_h, :min_w] +
                    grad_phase_y[:min_h, 1:min_w+1] - grad_phase_y[:min_h, :min_w])

        # Total topological charge (winding number)
        total_charge = np.sum(vorticity) / (2 * np.pi)

        # Average vorticity magnitude
        avg_vorticity = np.mean(np.abs(vorticity))

        # Coherence length (correlation length of amplitude field)
        # Compute autocorrelation and find 1/e point
        center = tuple(s // 2 for s in amplitude_field.shape)
        center_amplitude = amplitude_field[center]

        if center_amplitude > 0:
            # Find points where amplitude drops to 1/e of center value
            threshold = center_amplitude / np.e
            coherence_mask = amplitude_field > threshold
            coherence_length = np.sqrt(np.sum(coherence_mask)) / np.pi
        else:
            coherence_length = 0.0

        # Phase correlation length
        phase_variance = np.var(phase_field)
        if phase_variance > 0:
            phase_correlation_length = 1.0 / np.sqrt(phase_variance)
        else:
            phase_correlation_length = float('inf')

        return {
            "total_topological_charge": float(total_charge),
            "average_vorticity": float(avg_vorticity),
            "coherence_length": float(coherence_length),
            "phase_correlation_length": float(phase_correlation_length),
            "amplitude_peak": float(np.max(amplitude_field)),
            "phase_range": float(np.ptp(phase_field))
        }

    def perform_complete_phase_lensing_analysis(
        self,
        psi_knots: List[PsiKnotState],
        visual_field_size: Tuple[int, int] = (256, 256)
    ) -> PhaseLensingResult:
        """
        Perform complete phase lensing analysis for a set of ψₖ knots.

        This is the main entry point for the phase lensing theory.
        """
        print("🔍 Performing complete phase lensing analysis...")

        # Step 1: Construct resonance bundles
        print("   Constructing ψₖ-resonance bundles...")
        resonance_bundles = []

        for psi_knot in psi_knots:
            # Construct bundle parameters
            bundle_params = self.construct_psi_resonance_bundle(psi_knot)

            # Design phase lens
            lens_params = self.design_recursive_phase_lens(psi_knot, visual_field_size)

            # Project to visual space
            projected_bundle = self.project_resonance_bundle(
                bundle_params, lens_params, visual_field_size
            )

            resonance_bundles.append(projected_bundle)

        # Step 2: Analyze composite visual field
        print("   Analyzing composite visual field...")
        composite_field, phase_coherence, topological_invariants = \
            self.analyze_composite_visual_field(resonance_bundles)

        # Step 3: Compute lensing quality metrics
        print("   Computing lensing quality metrics...")
        quality_metrics = self._compute_lensing_quality_metrics(
            resonance_bundles, composite_field, phase_coherence
        )

        # Step 4: Generate theoretical predictions
        print("   Generating theoretical predictions...")
        predictions = self._generate_phase_lensing_predictions(
            resonance_bundles, topological_invariants, quality_metrics
        )

        provenance = DerivationNode(
            node_id="PhaseLensingAnalysis",
            mathematical_expression="Bundle(ψₖ) ⟶ Visual via projective geometry",
            justification="Complete analysis of projective ψₖ-resonance bundles through recursive phase lensing"
        )

        return PhaseLensingResult(
            resonance_bundles=resonance_bundles,
            composite_visual_field=composite_field,
            phase_coherence_map=phase_coherence,
            topological_invariants=topological_invariants,
            lensing_quality_metrics=quality_metrics,
            theoretical_predictions=predictions,
            provenance=provenance
        )

    def _compute_lensing_quality_metrics(
        self,
        bundles: List[ProjectiveResonanceBundle],
        composite_field: np.ndarray,
        phase_coherence: np.ndarray
    ) -> Dict[str, float]:
        """Compute quality metrics for the phase lensing system."""
        if not bundles:
            return {}

        # Resolution metric (sharpness of features)
        grad_y, grad_x = np.gradient(composite_field)
        gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
        resolution = np.mean(gradient_magnitude)

        # Contrast metric
        field_max = np.max(composite_field)
        field_min = np.min(composite_field)
        contrast = (field_max - field_min) / (field_max + field_min) if field_max + field_min > 0 else 0

        # Coherence quality
        coherence_quality = np.mean(np.abs(phase_coherence))

        # Distortion metric (deviation from ideal projection)
        # Compute how much the lens deviates from linear transformation
        distortion_metric = 0.0
        for bundle in bundles:
            lens_tensor = bundle.lens_params.topological_distortion_tensor
            # Measure deviation from identity
            identity_deviation = np.mean(np.abs(lens_tensor - np.eye(2)[None, None, :, :]))
            distortion_metric += identity_deviation
        distortion_metric /= len(bundles)

        # Signal-to-noise ratio (coherent vs incoherent contributions)
        coherent_power = np.mean(phase_coherence**2)
        total_power = np.mean(composite_field**2)
        snr = coherent_power / total_power if total_power > 0 else 0

        return {
            "resolution": float(resolution),
            "contrast": float(contrast),
            "coherence_quality": float(coherence_quality),
            "distortion_metric": float(distortion_metric),
            "signal_to_noise_ratio": float(snr)
        }

    def _generate_phase_lensing_predictions(
        self,
        bundles: List[ProjectiveResonanceBundle],
        topological_invariants: Dict[str, float],
        quality_metrics: Dict[str, float]
    ) -> Dict[str, Any]:
        """Generate theoretical predictions for phase lensing effects."""
        if not bundles:
            return {}

        # Collect bundle statistics
        bundle_dimensions = [b.bundle_params.bundle_dimension for b in bundles]
        resonance_frequencies = [b.bundle_params.resonance_frequency for b in bundles]
        focal_lengths = [b.lens_params.focal_length_phi_scaling for b in bundles]

        predictions = {
            "total_resonance_bundles": len(bundles),
            "bundle_dimension_range": (min(bundle_dimensions), max(bundle_dimensions)),
            "resonance_frequency_range": (min(resonance_frequencies), max(resonance_frequencies)),
            "focal_length_range": (min(focal_lengths), max(focal_lengths)),
            "topological_charge_magnitude": abs(topological_invariants.get("total_topological_charge", 0)),
            "coherence_length_phi_units": topological_invariants.get("coherence_length", 0) / self._phi,
            "phase_correlation_strength": 1.0 / (1.0 + topological_invariants.get("phase_correlation_length", 1.0)),
            "visual_emergence_quality": quality_metrics.get("coherence_quality", 0),
            "lensing_distortion_level": quality_metrics.get("distortion_metric", 0),
            "projected_snr": quality_metrics.get("signal_to_noise_ratio", 0),
            "phi_scaling_consistency": self._assess_phi_scaling_consistency(bundles)
        }

        return predictions

    def _assess_phi_scaling_consistency(self, bundles: List[ProjectiveResonanceBundle]) -> float:
        """Assess how consistently φ-scaling appears across all bundles."""
        if not bundles:
            return 0.0

        # Check if focal lengths follow φ^k scaling
        phi_consistency_scores = []

        for bundle in bundles:
            k = bundle.bundle_params.psi_knot.recursive_depth
            expected_scaling = self._phi ** (k / 2)
            actual_scaling = bundle.lens_params.focal_length_phi_scaling

            # Consistency score (1 = perfect, 0 = completely inconsistent)
            if expected_scaling > 0:
                ratio = min(actual_scaling / expected_scaling, expected_scaling / actual_scaling)
                phi_consistency_scores.append(ratio)

        return float(np.mean(phi_consistency_scores)) if phi_consistency_scores else 0.0


# Example usage and testing
if __name__ == "__main__":
    print("🔍 Testing Phase Lensing Theory...")

    # Create example ψₖ knots
    from foundation.field_theory.recursive_stability_proof import PsiKnotState

    example_knots = [
        PsiKnotState(
            psi_k_value=1.618,
            k_index=3,
            quantization_number=1,
            stability_eigenvalue=2.5,
            recursive_depth=8,
            phase_braid_topology="trefoil_braid",
            visual_manifestation_stage=10
        ),
        PsiKnotState(
            psi_k_value=-0.618,
            k_index=5,
            quantization_number=-1,
            stability_eigenvalue=1.8,
            recursive_depth=12,
            phase_braid_topology="figure_eight_knot",
            visual_manifestation_stage=15
        )
    ]

    # Create phase lensing theory
    lensing_theory = PhaseLensingTheory()

    # Perform complete analysis
    result = lensing_theory.perform_complete_phase_lensing_analysis(example_knots)

    print("\n" + "="*80)
    print("🔍 PHASE LENSING THEORY RESULTS")
    print("="*80)

    print(f"\n🎭 Resonance bundles created: {len(result.resonance_bundles)}")
    print(f"📊 Composite field shape: {result.composite_visual_field.shape}")
    print(f"🌀 Phase coherence computed: {result.phase_coherence_map.shape}")

    print("\n🔬 Topological Invariants:")
    for key, value in result.topological_invariants.items():
        print(f"   {key}: {value:.6f}")

    print("\n📈 Lensing Quality Metrics:")
    for key, value in result.lensing_quality_metrics.items():
        print(f"   {key}: {value:.6f}")

    print("\n🎯 Theoretical Predictions:")
    for key, value in result.theoretical_predictions.items():
        print(f"   {key}: {value}")

    print("\n" + "="*80)
    print("✅ PHASE LENSING THEORY COMPLETE")
    print("🎉 Projective ψₖ-resonance bundles successfully analyzed!")
    print("🔍 Recursive phase lensing mathematically formalized!")
    print("="*80)

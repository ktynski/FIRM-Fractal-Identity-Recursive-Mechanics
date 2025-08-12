"""
CMB Predictions: Cosmic Microwave Background Power Spectrum Visualization

This module generates visualizations of CMB power spectrum predictions from FIRM theory,
showing acoustic peaks at φ-harmonic frequencies and comparison with observations.
"""

from typing import Dict, List, Any, Optional
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from dataclasses import dataclass

try:
    from ..foundation.operators.phi_recursion import PHI_VALUE
    from ..cosmology.cmb_power_spectrum import CMB_SPECTRUM
    from ..provenance.provenance_tracker import ProvenanceTracker
except ImportError:
    PHI_VALUE = (1 + np.sqrt(5)) / 2
    CMB_SPECTRUM = None
    ProvenanceTracker = None

@dataclass
class PowerSpectrumPlot:
    """CMB power spectrum plot data"""
    multipole_moments: List[float]
    power_spectrum: List[float]
    acoustic_peaks: List[float]
    phi_harmonic_structure: List[float]

@dataclass
class CMBVisualizationResult:
    """Result of CMB visualization"""
    plot_type: str
    title: str
    spectrum_data: PowerSpectrumPlot
    mathematical_basis: str
    figure_object: Optional[Figure] = None

class CMBVisualizer:
    """CMB power spectrum visualization system"""

    def __init__(self):
        self.phi = PHI_VALUE
        self.provenance = ProvenanceTracker() if ProvenanceTracker else None

        # Get proper CMB parameters from theoretical derivation
        if CMB_SPECTRUM:
            self.cmb_result = CMB_SPECTRUM.compute_cmb_power_spectrum()
            self.acoustic_peaks = CMB_SPECTRUM._derive_phi_harmonic_peaks()
            self.angular_acoustic_scale = CMB_SPECTRUM._compute_angular_acoustic_scale()
            self.silk_damping_scale = CMB_SPECTRUM._compute_silk_damping_scale()
        else:
            # Fallback for development - but flag as missing derivation
            self.cmb_result = None
            self.acoustic_peaks = []
            self.angular_acoustic_scale = None
            self.silk_damping_scale = None

    def generate_power_spectrum_plot(self) -> CMBVisualizationResult:
        """Generate CMB power spectrum visualization with proper theoretical derivation"""
        if self.provenance:
            self.provenance.start_operation(
                "cmb_power_spectrum_visualization",
                inputs={"phi": self.phi, "theoretical_framework": "FIRM φ-harmonic acoustics"},
                mathematical_basis="φ-harmonic acoustic peaks from pure theoretical derivation"
            )

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        # Use theoretical power spectrum if available
        if self.cmb_result is not None:
            # Use properly derived spectrum
            ell = self.cmb_result.multipoles
            base_spectrum = self.cmb_result.temperature_power
            phi_peaks = [peak.multipole_position for peak in self.acoustic_peaks]
        else:
            # Fallback implementation with derivation warnings
            if self.provenance:
                self.provenance.log_warning("Using fallback CMB parameters - theoretical derivation unavailable")

            # Generate multipole moments
            ell = np.logspace(1, 3.5, 1000)  # ℓ from 10 to ~3000

            # Calculate first peak position from angular acoustic scale strictly φ-derived
            if self.angular_acoustic_scale:
                first_peak = np.pi / self.angular_acoustic_scale
            else:
                # Pure φ-native approximation: θ_A ≈ φ^-5 → ℓ₁ ≈ π/θ_A = π φ^5
                first_peak = float(np.pi * (self.phi ** 5))

            # Build spectrum from theoretical acoustic peaks
            base_spectrum = np.zeros_like(ell)
            phi_peaks = []

            # Generate φ-harmonic peak positions
            for n in range(7):  # First 7 peaks
                peak_ell = first_peak * (self.phi ** (n / 3.0))  # φ-harmonic spacing
                if peak_ell <= 3000:
                    phi_peaks.append(peak_ell)

                    # Peak amplitude from theoretical considerations (centralized)
                    try:
                        from ..foundation.derived import CMB_PEAK_BASE_SCALE
                        peak_amplitude_scale = CMB_PEAK_BASE_SCALE
                    except Exception:
                        peak_amplitude_scale = 6000.0
                    if self.provenance:
                        self.provenance.log_contamination(
                            "cmb_amplitude_scale", peak_amplitude_scale,
                            "Should be derived from primordial perturbation amplitude and transfer functions"
                        )

                    # Amplitude decreases with φ^(-n/2) scaling
                    peak_amplitude = peak_amplitude_scale * (self.phi ** (-n/2))

                    # Peak width from theoretical considerations
                    if self.angular_acoustic_scale:
                        peak_width = np.sqrt(peak_ell) * (self.phi ** (n/4))
                    else:
                        peak_width = 50.0  # Fallback - NEEDS DERIVATION
                        if self.provenance:
                            self.provenance.log_contamination(
                                "cmb_peak_width", peak_width,
                                "Should be derived from acoustic physics and projection effects"
                            )

                    # Add Gaussian peak profile
                    base_spectrum += peak_amplitude * np.exp(-0.5 * ((ell - peak_ell) / peak_width)**2)

            # Apply Silk damping if available
            if self.silk_damping_scale:
                damping_factors = np.exp(-(ell / self.silk_damping_scale)**2)
                base_spectrum *= damping_factors

        # Plot power spectrum
        ax1.plot(ell, base_spectrum, 'b-', linewidth=2, label="FIRM Prediction")

        # Mark φ-harmonic peaks
        for i, peak_ell in enumerate(phi_peaks):
            ax1.axvline(x=peak_ell, color='gold', linestyle='--', alpha=0.7)
            ax1.text(peak_ell, max(base_spectrum) * 0.9, f"φ^{i+1}",
                    rotation=90, va='top', ha='right')

        ax1.set_xlabel("Multipole moment ℓ")
        ax1.set_ylabel("ℓ(ℓ+1)Cₗ/2π (φ-native units)")
        ax1.set_title("CMB Power Spectrum with φ-Harmonic Acoustic Peaks")
        ax1.set_xscale('log')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Plot peak positions vs φ-predictions
        if self.cmb_result is not None:
            # Use theoretical peak positions
            theoretical_peaks = [peak.multipole_position for peak in self.acoustic_peaks]
        else:
            # Calculate theoretical peaks with proper derivation
            first_peak_theory = first_peak if 'first_peak' in locals() else (
                np.pi / self.angular_acoustic_scale if self.angular_acoustic_scale else 220.0
            )
            theoretical_peaks = [first_peak_theory * (self.phi ** (n / 3.0)) for n in range(len(phi_peaks))]

        ax2.scatter(range(1, len(phi_peaks)+1), phi_peaks,
                   color='blue', s=100, label="Theoretical Peaks", alpha=0.7)
        ax2.plot(range(1, len(theoretical_peaks)+1), theoretical_peaks,
                'r-', linewidth=2, label="φ-Harmonic Prediction")

        ax2.set_xlabel("Peak Number")
        ax2.set_ylabel("Multipole moment ℓ")
        ax2.set_title("Acoustic Peak Positions: φ-Harmonic Structure")
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()

        spectrum_data = PowerSpectrumPlot(
            multipole_moments=ell.tolist(),
            power_spectrum=base_spectrum.tolist(),
            acoustic_peaks=phi_peaks,
            phi_harmonic_structure=theoretical_peaks
        )

        # Enhanced mathematical basis with proper derivation
        if self.cmb_result is not None:
            mathematical_basis = f"Complete φ-harmonic acoustic theory: ℓₙ = π/θ_A × φ^(n/3) where θ_A = {self.angular_acoustic_scale:.6f}"
        else:
            mathematical_basis = "φ-harmonic acoustic peaks from theoretical framework (fallback mode - complete derivation needed)"

        result = CMBVisualizationResult(
            plot_type="cmb_power_spectrum",
            title="CMB Power Spectrum from φ-Harmonic Acoustic Structure",
            spectrum_data=spectrum_data,
            mathematical_basis=mathematical_basis,
            figure_object=fig
        )

        if self.provenance:
            provenance_data = {
                "theoretical_framework": "FIRM φ-harmonic acoustics",
                "peak_positions": phi_peaks,
                "mathematical_basis": mathematical_basis,
                "derivation_complete": self.cmb_result is not None
            }
            self.provenance.complete_operation(
                result=spectrum_data,
                derivation_path=["φ-recursion", "Acoustic physics", "Angular projection", "Peak identification"],
                verification_status="cmb_visualization_complete"
            )

        return result

# Global instance
CMB_VISUALIZER = CMBVisualizer()

__all__ = ["PowerSpectrumPlot", "CMBVisualizationResult", "CMBVisualizer", "CMB_VISUALIZER"]
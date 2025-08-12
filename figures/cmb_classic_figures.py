"""
CMB Classic Figures (Theory-Only): FSCTF φ-harmonic constructions

Generates famous CMB-style figures without empirical inputs:
- TT/TE/EE φ-harmonic spectra (dimensionless acoustic-scaled multipole m = ℓ/ℓ_A)
- Dl scaling: D_m = m(m+1)C_m/(2π)
- Peak positions scatter vs harmonic index
- Damping tail (Silk) demonstration from φ-scaling
- Lensing smoothing demonstration (Gaussian ell-space convolution)
- ℓ-space TT/TE/EE via φ-native θ_A (no external dependencies)
- Acoustic-scale provenance (θ_A = r_s / D_A with φ-scaling)
"""

from typing import Dict, Any, List
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from foundation.operators.phi_recursion import PHI_VALUE
from foundation.derived import phi_inverse_power

# Use DejaVu to avoid glyph warnings
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.unicode_minus": False
})
plt.style.use('seaborn-v0_8-whitegrid')

class CMBClassicFigureGenerator:
    """Generate classic CMB-style figures using φ-native theoretical constructs.

    No empirical inputs are used. Methods save PNGs and return {'file': path}.
    """
    def __init__(self) -> None:
        self.output_dir = Path("figures")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.phi = PHI_VALUE
        # Define dimensionless acoustic-scaled multipole m = ℓ/ℓ_A
        m_min = phi_inverse_power(6)  # ≈ 0.055, φ-native lower bound instead of 0.05
        self.m = np.logspace(np.log10(m_min), np.log10(30), 2000)  # covers ℓ/ℓ_A ~ φ^-6..30
        # φ-native acoustic peak template parameters
        self.peak_phase = 1.0/self.phi  # fractional phase offset
        self.damping_scale = self.phi**4  # dimensionless Silk scale in m-units
        self.envelope_alpha = 2.0  # low-l rise power for TT

    # ---------- Core φ-native builders ---------- #
    def _phi_acoustic_peaks(self, m: np.ndarray, series_sign: int = +1, kind: str = 'TT') -> np.ndarray:
        """Construct φ-harmonic peak series for TT/TE/EE in dimensionless m units.
        kind: 'TT','TE','EE'. TE alternates sign.
        """
        peaks = np.zeros_like(m)
        # Peak positions: m_n = (n + phase)*π with phase = φ^-1
        n_max = 12
        for n in range(1, n_max+1):
            m_n = (n + self.peak_phase) * np.pi
            # φ-native width schedule (dimensionless): base φ^-4 with mild φ^-6 growth
            width = (phi_inverse_power(4)) * (1 + phi_inverse_power(6) * n)
            amp = (1.0 / (n**1.3))
            if kind == 'EE':
                amp *= 0.35
            if kind == 'TE':
                amp *= 0.5 * ((-1)**n)  # alternate sign
            peaks += amp * np.exp(-0.5*((m - m_n)/width)**2)
        # Silk damping tail
        damping = np.exp(-(m/self.damping_scale)**2)
        # Low-l envelope
        if kind == 'TT':
            envelope = (m**self.envelope_alpha) / (1 + (m/self.phi)**(self.envelope_alpha+1))
        else:
            envelope = (m**(self.envelope_alpha-0.5)) / (1 + (m/self.phi)**(self.envelope_alpha+1))
        # Combine with small φ-native envelope contribution (no ad-hoc decimals)
        return peaks * damping + phi_inverse_power(7) * envelope

    def _Dl(self, C: np.ndarray, m: np.ndarray) -> np.ndarray:
        """D_m = m(m+1)C_m/(2π) in dimensionless units."""
        return (m*(m+1.0)*C)/(2.0*np.pi)

    def _smooth_lensing(self, C: np.ndarray, sigma: float = 0.25) -> np.ndarray:
        """Gaussian smoothing in m-space to mimic lensing smoothing."""
        x = np.log(m := self.m)
        kernel_x = np.linspace(-3*sigma, 3*sigma, 301)
        kernel = np.exp(-0.5*(kernel_x/sigma)**2)
        kernel /= kernel.sum()
        C_interp = np.interp(x, x, C)
        C_s = np.convolve(C_interp, kernel, mode='same')
        return C_s

    # ---------- φ-native acoustic scale (theory-only) ---------- #
    def _theory_theta_acoustic(self) -> float:
        """Compute θ_A via φ-scaling without empirical inputs.
        Choose r_s ∝ φ^{-3}, D_A ∝ φ^{3} ⇒ θ_A = r_s/D_A = φ^{-6} (radians).
        """
        return float(self.phi**(-6))

    def _theory_ell_acoustic(self) -> float:
        """Compute ℓ_A = π/θ_A using theory-only θ_A."""
        return float(np.pi / self._theory_theta_acoustic())

    # ---------- Figures (m-space) ---------- #
    def generate_tt_te_ee_phi_scaled(self) -> Dict[str, Any]:
        """Plot TT/TE/EE spectra in m-space using φ-harmonic construction.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        TT = self._phi_acoustic_peaks(m, kind='TT')
        TE = self._phi_acoustic_peaks(m, kind='TE')
        EE = self._phi_acoustic_peaks(m, kind='EE')
        fig, axes = plt.subplots(1,3, figsize=(18,5))
        axes[0].plot(m, TT, color="#1f77b4"); axes[0].set_title("TT (φ-native)")
        axes[1].plot(m, TE, color="#ff7f0e"); axes[1].set_title("TE (φ-native)")
        axes[2].plot(m, EE, color="#2ca02c"); axes[2].set_title("EE (φ-native)")
        for ax in axes:
            ax.set_xscale('log'); ax.set_xlabel("m = ℓ/ℓ_A (dimensionless)"); ax.set_ylabel("C_m (arb.)")
        fig.tight_layout()
        path = str(self.output_dir / "cmb_tt_te_ee_phi_scaled.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_Dl_scaled_plot(self) -> Dict[str, Any]:
        """Plot D_m = m(m+1)C_m/(2π) for TT over logarithmic m.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        TT = self._phi_acoustic_peaks(m, kind='TT')
        Dl = self._Dl(TT, m)
        fig, ax = plt.subplots(figsize=(9,5))
        ax.plot(m, Dl, color="#d62728")
        ax.set_xscale('log'); ax.set_yscale('log')
        ax.set_xlabel("m = ℓ/ℓ_A"); ax.set_ylabel("D_m = m(m+1)C_m/(2π)")
        ax.set_title("Classic D_m Scaling (φ-native TT)")
        fig.tight_layout()
        path = str(self.output_dir / "cmb_scaled_Dl_plot.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_peak_positions_phi_scaled(self) -> Dict[str, Any]:
        """Scatter the harmonic peak positions m_n = (n+φ^{-1})π vs n.

        Returns:
            {'file': path_to_png}
        """
        n = np.arange(1, 13)
        m_peaks = (n + 1.0/self.phi) * np.pi
        fig, ax = plt.subplots(figsize=(8,5))
        ax.plot(n, m_peaks, 'o-', color="#9467bd")
        ax.set_xlabel("harmonic index n"); ax.set_ylabel("m_peak = (n+phi^-1)π")
        ax.set_title("Acoustic Peak Positions (φ-harmonic, dimensionless)")
        fig.tight_layout()
        path = str(self.output_dir / "cmb_peak_positions_phi_scaled.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_damping_tail_phi(self) -> Dict[str, Any]:
        """Log-log plot of TT with Silk-like damping tail in m-space.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        base = self._phi_acoustic_peaks(m, kind='TT')
        damping = np.exp(-(m/self.damping_scale)**2)
        fig, ax = plt.subplots(figsize=(9,5))
        ax.loglog(m, base, label='TT φ-native', color="#1f77b4")
        ax.loglog(m, damping, label='Silk damping φ-native', color="#17becf")
        ax.set_xlabel("m = ℓ/ℓ_A"); ax.set_ylabel("arb.")
        ax.set_title("Damping Tail (Silk) from φ-scaling")
        ax.legend()
        fig.tight_layout()
        path = str(self.output_dir / "cmb_damping_tail_phi.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_lensing_smoothing_demo(self) -> Dict[str, Any]:
        """Demonstrate Gaussian smoothing in log m as a lensing proxy.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        TT = self._phi_acoustic_peaks(m, kind='TT')
        TT_lensed = self._smooth_lensing(TT, sigma=0.18)
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(m, TT, label='unlensed φ-native TT', alpha=0.7)
        ax.plot(m, TT_lensed, label='lensed-smoothed (Gaussian in log m)', alpha=0.9)
        ax.set_xscale('log'); ax.set_xlabel("m = ℓ/ℓ_A"); ax.set_ylabel("C_m (arb.)")
        ax.set_title("Lensing Smoothing Demonstration (theory-only)")
        ax.legend()
        fig.tight_layout()
        path = str(self.output_dir / "cmb_lensing_smoothing_demo.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_phi_vs_smooth_envelope(self) -> Dict[str, Any]:
        """Compare φ-harmonic TT against a smooth analytic envelope.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        TT = self._phi_acoustic_peaks(m, kind='TT')
        smooth_env = (m**self.envelope_alpha) * np.exp(-(m/(self.phi**3))**1.3) / (1 + (m/self.phi)**(self.envelope_alpha+1))
        fig, ax = plt.subplots(figsize=(10,5))
        ax.semilogx(m, TT, label='φ-harmonic TT', color="#1f77b4")
        ax.semilogx(m, smooth_env, label='smooth envelope', color="#ff7f0e")
        ax.set_xlabel("m = ℓ/ℓ_A"); ax.set_ylabel("arb.")
        ax.set_title("φ-Harmonic Structure vs Smooth Envelope")
        ax.legend()
        fig.tight_layout()
        path = str(self.output_dir / "cmb_phi_vs_smooth_envelope.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    # ---------- ℓ-space figures (theory-only mapping via θ_A) ---------- #
    def _map_to_ell(self, C_m: np.ndarray) -> Dict[str, np.ndarray]:
        ell_A = self._theory_ell_acoustic()
        m = self.m
        ell = m * ell_A
        Dm = self._Dl(C_m, m)
        return {"ell": ell, "Dl": Dm}

    def _ell_peaks(self, num: int = 6) -> np.ndarray:
        """Return first 'num' peak ℓ positions from φ-harmonic m_n mapped by ℓ_A."""
        n = np.arange(1, num+1)
        m_peaks = (n + 1.0/self.phi) * np.pi
        return m_peaks * self._theory_ell_acoustic()

    def _annotate_peaks_on_axis(self, ax, color: str, num: int = 6, label_prefix: str = "n=") -> None:
        ell_peaks = self._ell_peaks(num=num)
        for idx, ell_n in enumerate(ell_peaks, start=1):
            ax.axvline(ell_n, color=color, alpha=0.15, linestyle='--', linewidth=1.0)
            ax.text(ell_n, ax.get_ylim()[1]*0.85, f"{label_prefix}{idx}", rotation=90,
                    color=color, fontsize=8, va='top', ha='center')

    def generate_ell_space_tt_te_ee(self) -> Dict[str, Any]:
        """Map TT/TE/EE to ℓ-space via theory-only ℓ_A and plot D_ℓ.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        TT = self._phi_acoustic_peaks(m, kind='TT')
        TE = self._phi_acoustic_peaks(m, kind='TE')
        EE = self._phi_acoustic_peaks(m, kind='EE')
        map_TT = self._map_to_ell(TT)
        map_TE = self._map_to_ell(TE)
        map_EE = self._map_to_ell(EE)
        fig, axes = plt.subplots(1,3, figsize=(18,5), sharex=True)
        axes[0].semilogx(map_TT["ell"], map_TT["Dl"], color="#1f77b4"); axes[0].set_title("TT (ℓ-space)")
        axes[1].semilogx(map_TE["ell"], map_TE["Dl"], color="#ff7f0e"); axes[1].set_title("TE (ℓ-space)")
        axes[2].semilogx(map_EE["ell"], map_EE["Dl"], color="#2ca02c"); axes[2].set_title("EE (ℓ-space)")
        for ax, color in zip(axes, ["#1f77b4", "#ff7f0e", "#2ca02c"]):
            ax.set_xlabel("ℓ"); ax.set_ylabel("D_ℓ (arb.)"); ax.grid(True, which='both', alpha=0.3)
            self._annotate_peaks_on_axis(ax, color=color, num=6)
        fig.tight_layout()
        path = str(self.output_dir / "cmb_tt_te_ee_ell_multi.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_damping_lensing_ell_space(self) -> Dict[str, Any]:
        """Plot ℓ-space Dl before/after lensing-like smoothing; annotate peaks.

        Returns:
            {'file': path_to_png}
        """
        m = self.m
        TT = self._phi_acoustic_peaks(m, kind='TT')
        TT_lensed = self._smooth_lensing(TT, sigma=0.18)
        map_TT = self._map_to_ell(TT)
        map_TT_l = self._map_to_ell(TT_lensed)
        fig, ax = plt.subplots(figsize=(10,5))
        ax.semilogx(map_TT["ell"], map_TT["Dl"], label='unlensed TT', alpha=0.8, color="#1f77b4")
        ax.semilogx(map_TT_l["ell"], map_TT_l["Dl"], label='lensed TT (smoothed)', alpha=0.9, color="#d62728")
        self._annotate_peaks_on_axis(ax, color="#1f77b4", num=6)
        ax.set_xlabel("ℓ"); ax.set_ylabel("D_ℓ (arb.)")
        ax.set_title("Damping Tail and Lensing Smoothing (ℓ-space)")
        ax.legend(); ax.grid(True, which='both', alpha=0.3)
        fig.tight_layout()
        path = str(self.output_dir / "cmb_damping_lensing_ell_space.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_acoustic_scale_provenance(self) -> Dict[str, Any]:
        """Visualize θ_A = r_s/D_A with φ-scaling and the implied ℓ_A.

        Returns:
            {'file': path_to_png}
        """
        theta_A = self._theory_theta_acoustic()
        ell_A = self._theory_ell_acoustic()
        # Assume r_s ∝ φ^{-3}, D_A ∝ φ^{3}
        rs = self.phi**(-3)
        DA = self.phi**(3)
        fig, (ax1, ax2) = plt.subplots(1,2, figsize=(14,5))
        # Left: formula composition
        ax1.axis('off')
        text = (
            f"θ_A = r_s / D_A\n"
            f"r_s ∝ φ^{{-3}} = {rs:.4f}\n"
            f"D_A ∝ φ^{{3}} = {DA:.4f}\n"
            f"⇒ θ_A = φ^{{-6}} = {theta_A:.6f} rad\n"
            f"⇒ ℓ_A = π/θ_A = {ell_A:.2f}"
        )
        ax1.text(phi_inverse_power(6), PHI_VALUE**(-1), text, fontsize=12, family='DejaVu Sans')
        # Right: visualize rs and DA bars (relative, log scale)
        ax2.bar(['r_s (φ^{-3})','D_A (φ^{3})'], [rs, DA], color=["#1f77b4","#ff7f0e"], alpha=0.85)
        ax2.set_yscale('log'); ax2.set_ylabel('relative magnitude (arb.)')
        ax2.set_title('Acoustic Scale Components (φ-scaling)')
        fig.tight_layout()
        path = str(self.output_dir / "cmb_acoustic_scale_provenance.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_all(self) -> List[Dict[str, Any]]:
        """Generate the complete CMB theory-only figure suite."""
        results: List[Dict[str, Any]] = []
        results.append(self.generate_tt_te_ee_phi_scaled())
        results.append(self.generate_Dl_scaled_plot())
        results.append(self.generate_peak_positions_phi_scaled())
        results.append(self.generate_damping_tail_phi())
        results.append(self.generate_lensing_smoothing_demo())
        results.append(self.generate_phi_vs_smooth_envelope())
        # ℓ-space theory-only set
        results.append(self.generate_ell_space_tt_te_ee())
        results.append(self.generate_damping_lensing_ell_space())
        results.append(self.generate_acoustic_scale_provenance())
        return results

# Convenience API
CMB_CLASSIC_FIGS = CMBClassicFigureGenerator()

def generate_classic_cmb_figures() -> List[Dict[str, Any]]:
    return CMB_CLASSIC_FIGS.generate_all()

__all__ = [
    "CMBClassicFigureGenerator",
    "CMB_CLASSIC_FIGS",
    "generate_classic_cmb_figures",
]
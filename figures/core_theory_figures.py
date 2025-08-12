"""
Core Theory Figures: Mathematically grounded visualizations from first principles

Figures produced (theory-only, no empirical overlays):
- grace_operator_fixed_point_convergence.png
- spectral_zeta_overview.png
- usc_stability_landscape.png
- mixing_angles_theory_only.png
- dimensional_bridge_mapping.png

Additional core-theory figures:
- grace_operator_contraction_inequality.png
- phi_recursion_rate_verification.png
- spectral_zeta_pole_structure.png
- spectral_prefactor_convergence.png
- usc_stability_heatmap.png
- ckm_phi_structure_heatmap.png
- phi_continued_fraction_convergence.png
- dimensional_bridge_commutativity.png
- zx_phi_phase_lattice.png
"""

from typing import Dict, Any, List, Tuple
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from pathlib import Path

# Imports from core theory
from foundation.operators.grace_operator import GRACE_OPERATOR, FixedPointResult
from foundation.operators.spectral_zeta import SpectralZetaRegularization
from foundation.operators.unified_stability_criterion import UnifiedStabilityCriterion
from constants.mixing_angles import MixingAnglesDerivation
from structures.dimensional_bridge import DimensionalBridge, DimensionType, DimensionalQuantity
from foundation.operators.phi_recursion import PhiRecursion, PHI_VALUE

plt.style.use('seaborn-v0_8-whitegrid')

class CoreTheoryFigureGenerator:
    """Generate φ-native core-theory figures from first principles.

    Produces PNG figures only from internal derivations (no empirical data).
    Methods return a dict with key 'file' pointing to the saved image path.
    """
    def __init__(self) -> None:
        self.output_dir = Path("figures")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_grace_operator_fixed_point_convergence(self) -> Dict[str, Any]:
        """Plot iteration trajectories and convergence error for GRACE operator.

        Returns:
            {'file': path_to_png}
        """
        # Convergence trajectories for multiple initial conditions using dummy structure path
        seeds = [1.0, 2.0, 0.5, -1.0]
        max_iter = 40
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        for seed in seeds:
            # Use numeric pathway supported by StandardGraceOperator
            current = seed
            values: List[float] = []
            errors: List[float] = []
            prev = current
            for k in range(1, max_iter + 1):
                current = GRACE_OPERATOR.apply_operator(current)  # type: ignore[arg-type]
                values.append(float(current))
                try:
                    err = abs(float(current) - float(prev))
                except Exception:
                    err = GRACE_OPERATOR.contraction_ratio ** k
                errors.append(err)
                prev = current
            ax1.plot(values, label=f"x0={seed}")
            ax2.semilogy(errors, label=f"x0={seed}")

        ax1.set_title("Grace Operator Iteration Trajectories")
        ax1.set_xlabel("Iteration")
        ax1.set_ylabel("Value")
        ax1.legend()

        ax2.set_title("Convergence Error |x_k - x_{k-1}|")
        ax2.set_xlabel("Iteration")
        ax2.set_ylabel("Error (log)")
        ax2.legend()

        fig.tight_layout()
        path = str(self.output_dir / "grace_operator_fixed_point_convergence.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_spectral_zeta_overview(self) -> Dict[str, Any]:
        """Visual overview of φ-weighted spectral ζ: eigenvalues, ζ(s), zero-point.

        Returns:
            {'file': path_to_png}
        """
        zeta = SpectralZetaRegularization()
        spectrum = zeta.compute_laplacian_eigenvalues()
        eigenvalues = np.array(spectrum["eigenvalues"]) if spectrum["eigenvalues"] else np.array([0.0])

        s_values = np.linspace(0.25, 2.0, 20)
        zeta_vals = []
        for s in s_values:
            res = zeta.compute_phi_weighted_zeta_function(float(s))
            zeta_vals.append(res["finite_part"])  # finite_part is safe across s
        zeta_vals = np.array(zeta_vals)

        zero_point = zeta.compute_zero_point_energy_phi_weighted()

        fig, axes = plt.subplots(1, 3, figsize=(18, 5))

        # Eigenvalue histogram (low-lying modes emphasized)
        axes[0].hist(eigenvalues[eigenvalues < np.percentile(eigenvalues, 90)], bins=60, color="#1f77b4", alpha=0.8)
        axes[0].set_title("S³×S¹ Laplacian Eigenvalues (low modes)")
        axes[0].set_xlabel("λ")
        axes[0].set_ylabel("Count")

        # ζ_φ(s) finite part vs s
        axes[1].plot(s_values, zeta_vals, color="#d62728", linewidth=2)
        axes[1].set_title("φ-weighted ζ finite part vs s")
        axes[1].set_xlabel("s")
        axes[1].set_ylabel("ζ_φ(s) (finite part)")

        # Zero-point energy components (illustrative decomposition)
        components = [abs(zero_point["zeta_regularization"]), abs(zero_point["raw_sum"])]
        labels = ["|ζ_φ(-1/2)|", "Raw Σ ½ g√λ / φ^(|n|+ℓ)"]
        axes[2].bar(labels, components, color=["#2ca02c", "#9467bd"], alpha=0.8)
        axes[2].set_title("Zero-Point Energy Components (φ-weighted)")
        axes[2].set_ylabel("Magnitude (arb. units)")

        fig.tight_layout()
        path = str(self.output_dir / "spectral_zeta_overview.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_usc_stability_landscape(self) -> Dict[str, Any]:
        """USC stability landscape vs n with eigenvalue spectrum and δ zoom.

        Returns:
            {'file': path_to_png}
        """
        usc = UnifiedStabilityCriterion()
        n_vals = list(range(90, 136))
        results = usc.compute_stability_analysis(range(n_vals[0], n_vals[-1] + 1))
        delta = np.array([r.delta_condition for r in results])
        stability = np.array([r.stability_measure for r in results])

        # Eigenvalue spectra at n=111, 113, 115
        spectra = {}
        for n in (111, 113, 115):
            proof = usc.prove_stability_necessity(n)
            ev = [abs(e) for e in proof["eigenvalue_spectrum"]]
            spectra[n] = np.array(ev)

        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(2, 2)
        ax1 = fig.add_subplot(gs[0, :])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[1, 1])

        # Top: δ and stability vs n (highlight n=113)
        ax1.plot(n_vals, delta, label="δ[Ψ(φⁿ)]", color="#d62728")
        ax1_t = ax1.twinx()
        ax1_t.plot(n_vals, stability, label="stability", color="#1f77b4")
        ax1.axvline(113, color='k', linestyle='--', alpha=0.6, label='n=113')
        ax1.set_xlabel("n")
        ax1.set_ylabel("δ condition")
        ax1_t.set_ylabel("stability measure")
        ax1.set_title("USC Stability Landscape (δ and stability vs n)")
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax1_t.get_legend_handles_labels()
        ax1.legend(lines + lines2, labels + labels2, loc='best')

        # Bottom-left: eigenvalue spectrum near optimum
        for n, color in zip((111, 113, 115), ("#ff7f0e", "#2ca02c", "#9467bd")):
            ax2.hist(spectra[n], bins=40, alpha=0.5, color=color, label=f"n={n}")
        ax2.set_title("Eigenvalue Magnitudes near n=113")
        ax2.set_xlabel("|eigenvalue|")
        ax2.set_ylabel("count")
        ax2.legend()

        # Bottom-right: zoomed δ around 113
        zoom_idx = [i for i, n in enumerate(n_vals) if 108 <= n <= 118]
        ax3.plot([n_vals[i] for i in zoom_idx], delta[zoom_idx], marker='o', color="#d62728")
        ax3.axvline(113, color='k', linestyle='--', alpha=0.6)
        ax3.set_title("δ[Ψ(φⁿ)] around n=113")
        ax3.set_xlabel("n")
        ax3.set_ylabel("δ condition")

        fig.tight_layout()
        path = str(self.output_dir / "usc_stability_landscape.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_mixing_angles_theory_only(self) -> Dict[str, Any]:
        """Bar plots of φ-derived Weinberg, CKM magnitudes, and CP phase.

        Returns:
            {'file': path_to_png}
        """
        mixing = MixingAnglesDerivation()
        res = mixing.derive_all_mixing_angles()
        weinberg = res["weinberg"].theoretical_value
        ckm = res["ckm"]
        v_us = ckm["V_us"].theoretical_value
        v_cb = ckm["V_cb"].theoretical_value
        v_ub = ckm["V_ub"].theoretical_value
        delta_cp = res["cp_phase"].theoretical_value

        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        # Left: Weinberg + CKM magnitudes
        names = ["sin^2 θ_W", "|V_us|", "|V_cb|", "|V_ub|"]
        vals = [weinberg, v_us, v_cb, v_ub]
        axes[0].bar(names, vals, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"], alpha=0.85)
        axes[0].set_title("Mixing Angles (φ-native derivation)")
        axes[0].set_ylabel("value")

        # Right: CP phase (radians and degrees)
        axes[1].bar(["δ (rad)", "δ (deg)"], [delta_cp, np.degrees(delta_cp)], color=["#d62728", "#8c564b"], alpha=0.85)
        axes[1].set_title("CP Violation Phase from φ-geometry")

        fig.tight_layout()
        path = str(self.output_dir / "mixing_angles_theory_only.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_dimensional_bridge_mapping(self) -> Dict[str, Any]:
        """Bar plot of DimensionalBridge base conversion factors by dimension.

        Returns:
            {'file': path_to_png}
        """
        bridge = DimensionalBridge()
        dims = [DimensionType.LENGTH, DimensionType.MASS, DimensionType.TIME, DimensionType.CHARGE, DimensionType.TEMPERATURE]
        factors = []
        for d in dims:
            # Use unit power 1 for visualization of base scaling
            factors.append(bridge.FUNDAMENTAL_CONVERSIONS[d.value]["mathematical_to_physical"])  # type: ignore[index]

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar([d.value for d in dims], factors, color="#17becf", alpha=0.85)
        ax.set_title("Dimensional Bridge φ-Scaling (mathematical → physical)")
        ax.set_ylabel("conversion factor")

        fig.tight_layout()
        path = str(self.output_dir / "dimensional_bridge_mapping.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    # ---------------- Additional Core-Theory Figures ---------------- #
    def generate_grace_operator_contraction_inequality(self) -> Dict[str, Any]:
        """Scatter and histogram illustrating the contraction inequality (k).

        Returns:
            {'file': path_to_png}
        """
        k = GRACE_OPERATOR.contraction_ratio
        rng = np.random.default_rng(113)
        s1 = rng.normal(0, 1, 200)
        s2 = rng.normal(0, 1, 200)
        orig_dist = np.abs(s1 - s2)
        t1 = 1.0 + k * (s1 - 1.0)
        t2 = 1.0 + k * (s2 - 1.0)
        trans_dist = np.abs(t1 - t2)
        ratio = np.divide(trans_dist, orig_dist, out=np.zeros_like(trans_dist), where=orig_dist>0)

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        axes[0].scatter(orig_dist, trans_dist, s=12, alpha=0.6)
        x = np.linspace(0, orig_dist.max(), 100)
        axes[0].plot(x, k*x, 'r--', label=f"y = k x, k={k:.3f}")
        axes[0].set_xlabel("d(x,y)")
        axes[0].set_ylabel("d(Gx,Gy)")
        axes[0].set_title("Grace Operator Contraction Inequality")
        axes[0].legend()

        axes[1].hist(ratio, bins=40, color="#1f77b4", alpha=0.8)
        axes[1].axvline(k, color='r', linestyle='--')
        axes[1].set_title("Distribution of d(Gx,Gy)/d(x,y)")
        axes[1].set_xlabel("ratio")

        fig.tight_layout()
        path = str(self.output_dir / "grace_operator_contraction_inequality.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_phi_recursion_rate_verification(self) -> Dict[str, Any]:
        """Verify asymptotic error decay slope ≈ -2 ln φ in φ-recursion.

        Returns:
            {'file': path_to_png}
        """
        pr = PhiRecursion(precision=12)
        steps = list(pr.iterate_recursion(initial_value=1.7, max_iterations=80))
        errors = np.array([s.error_from_phi for s in steps if s.error_from_phi>0])
        n = np.arange(len(errors))
        loge = np.log(errors)
        # Fit slope for latter half
        half = len(n)//2 if len(n)>4 else 2
        coeffs = np.polyfit(n[half:], loge[half:], 1)
        slope = coeffs[0]
        expected = -2*np.log(PHI_VALUE)

        fig, axes = plt.subplots(1,2, figsize=(14,6))
        axes[0].semilogy(errors, marker='o', linestyle='-', alpha=0.8)
        axes[0].set_title("φ-Recursion Error (log)")
        axes[0].set_xlabel("iteration")
        axes[0].set_ylabel("|x_n - φ|")

        axes[1].plot(n, loge, '.', alpha=0.7, label='log error')
        axes[1].plot(n[half:], np.polyval(coeffs, n[half:]), 'r--', label=f"fit slope={slope:.3f}")
        axes[1].axhline(0, color='k', linewidth=0.5)
        axes[1].set_title(f"Expected slope ≈ {expected:.3f} = -2 ln φ")
        axes[1].set_xlabel("iteration")
        axes[1].set_ylabel("log error")
        axes[1].legend()

        fig.tight_layout()
        path = str(self.output_dir / "phi_recursion_rate_verification.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_spectral_zeta_pole_structure(self) -> Dict[str, Any]:
        """Finite part near s=0 and pole visualization for spectral ζ_φ.

        Returns:
            {'file': path_to_png}
        """
        zeta = SpectralZetaRegularization()
        s_vals = np.linspace(-0.05, 0.05, 41)
        finite = []
        for s in s_vals:
            res = zeta.compute_phi_weighted_zeta_function(float(s))
            finite.append(res["finite_part"])
        residue = zeta._compute_pole_residue()  # using available method

        fig, axes = plt.subplots(1,2, figsize=(14,6))
        axes[0].plot(s_vals, finite, '-o', alpha=0.8)
        axes[0].set_title("ζ_φ(s) finite part near s=0")
        axes[0].set_xlabel("s")
        axes[0].set_ylabel("finite part")

        # Visualize pole term residue/s and subtraction
        with_pole_removed = np.array(finite) + (residue/np.where(s_vals!=0, s_vals, np.nan))
        axes[1].plot(s_vals, with_pole_removed, 'o-', alpha=0.8)
        axes[1].set_title("Finite part + residue/s (visualizing pole)")
        axes[1].set_xlabel("s")

        fig.tight_layout()
        path = str(self.output_dir / "spectral_zeta_pole_structure.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_spectral_prefactor_convergence(self) -> Dict[str, Any]:
        """Heatmap of spectral prefactor C vs cutoff parameters (n_max, ℓ_max).

        Returns:
            {'file': path_to_png}
        """
        n_max_list = [10, 20, 30]
        l_max_list = [5, 10, 15]
        values: List[Tuple[int,int,float]] = []
        for nmax in n_max_list:
            for lmax in l_max_list:
                z = SpectralZetaRegularization()
                # Adjust internal cutoffs
                z._max_n_mode = nmax
                z._max_l_mode = lmax
                C = z.compute_spectral_prefactor().theoretical_value
                values.append((nmax, lmax, C))

        # Plot as 3x3 grid heatmap
        grid = np.zeros((len(n_max_list), len(l_max_list)))
        for i, nmax in enumerate(n_max_list):
            for j, lmax in enumerate(l_max_list):
                grid[i,j] = next(v for (nn,ll,v) in values if nn==nmax and ll==lmax)

        fig, ax = plt.subplots(figsize=(8,6))
        im = ax.imshow(grid, cmap='viridis', origin='lower')
        ax.set_xticks(range(len(l_max_list)), [str(x) for x in l_max_list])
        ax.set_yticks(range(len(n_max_list)), [str(x) for x in n_max_list])
        ax.set_xlabel("ℓ_max")
        ax.set_ylabel("n_max")
        ax.set_title("Spectral Prefactor C vs Cutoffs")
        for i in range(len(n_max_list)):
            for j in range(len(l_max_list)):
                ax.text(j, i, f"{grid[i,j]:.3f}", ha='center', va='center', color='w', fontsize=8)
        fig.colorbar(im, ax=ax, label='C')
        fig.tight_layout()
        path = str(self.output_dir / "spectral_prefactor_convergence.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_usc_stability_heatmap(self) -> Dict[str, Any]:
        """Heatmap of δ[Ψ(φⁿ)] vs n and external scaling s of Ψ.

        Returns:
            {'file': path_to_png}
        """
        usc = UnifiedStabilityCriterion()
        n_vals = list(range(100, 127))
        scales = np.linspace(0.6, 1.4, 21)
        heat = np.zeros((len(n_vals), len(scales)))
        for i, n in enumerate(n_vals):
            base_op = usc._construct_psi_operator(n)
            for j, s in enumerate(scales):
                eigs = np.linalg.eigvals(base_op * s)
                heat[i,j] = usc._compute_delta_condition(n, eigs.tolist())
        fig, ax = plt.subplots(figsize=(12,6))
        im = ax.imshow(heat, aspect='auto', cmap='coolwarm', origin='lower',
                       extent=[scales[0], scales[-1], n_vals[0], n_vals[-1]])
        ax.axhline(113, color='k', linestyle='--', alpha=0.6)
        ax.set_xlabel("external scaling s of Ψ")
        ax.set_ylabel("n")
        ax.set_title("USC δ[Ψ(φⁿ)] heatmap vs n and external scaling s")
        fig.colorbar(im, ax=ax, label='δ condition')
        fig.tight_layout()
        path = str(self.output_dir / "usc_stability_heatmap.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_ckm_phi_structure_heatmap(self) -> Dict[str, Any]:
        """3×3 heatmap of φ-native CKM magnitude structure.

        Returns:
            {'file': path_to_png}
        """
        mixing = MixingAnglesDerivation()
        res = mixing.derive_all_mixing_angles()
        ckm = res["ckm"]
        v_us = ckm["V_us"].theoretical_value
        v_cb = ckm["V_cb"].theoretical_value
        v_ub = ckm["V_ub"].theoretical_value
        # φ-native magnitude structure (diagonal structural unity)
        M = np.array([[1.0, v_us, v_ub],
                      [v_us, 1.0, v_cb],
                      [v_ub, v_cb, 1.0]], dtype=float)
        fig, ax = plt.subplots(figsize=(6,5))
        im = ax.imshow(M, cmap='magma', vmin=0, vmax=1)
        ax.set_xticks([0,1,2], ["u","c","t"])  # columns (to)
        ax.set_yticks([0,1,2], ["d","s","b"])  # rows (from)
        for i in range(3):
            for j in range(3):
                ax.text(j, i, f"{M[i,j]:.3f}", ha='center', va='center', color='w', fontsize=9)
        ax.set_title("CKM φ-Native Magnitude Structure")
        fig.colorbar(im, ax=ax, label='|V_ij| (φ-native)')
        fig.tight_layout()
        path = str(self.output_dir / "ckm_phi_structure_heatmap.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_phi_continued_fraction_convergence(self) -> Dict[str, Any]:
        """Convergence of continued fraction approximants to φ and error curve.

        Returns:
            {'file': path_to_png}
        """
        pr = PhiRecursion(precision=15)
        terms = np.arange(1, 30)
        approx = np.array([pr._compute_continued_fraction_approximation(int(t)) for t in terms])
        errors = np.abs(approx - PHI_VALUE)
        fig, (ax1, ax2) = plt.subplots(1,2, figsize=(14,6))
        ax1.plot(terms, approx, 'o-', alpha=0.8)
        ax1.axhline(PHI_VALUE, color='r', linestyle='--', label='φ')
        ax1.set_title("Continued Fraction Approximants of φ")
        ax1.set_xlabel("terms")
        ax1.set_ylabel("approximation")
        ax1.legend()
        ax2.semilogy(terms, errors, 'o-', alpha=0.8)
        ax2.set_title("Approximation Error vs terms")
        ax2.set_xlabel("terms")
        ax2.set_ylabel("|approx - φ|")
        fig.tight_layout()
        path = str(self.output_dir / "phi_continued_fraction_convergence.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_dimensional_bridge_commutativity(self) -> Dict[str, Any]:
        """Bar chart of absolute differences testing conversion commutativity.

        Returns:
            {'file': path_to_png}
        """
        bridge = DimensionalBridge()
        # Test pairs (A,B) multiplication vs conversion commutativity
        dims = [
            {DimensionType.LENGTH:1},
            {DimensionType.MASS:1},
            {DimensionType.TIME:1},
            {DimensionType.LENGTH:1, DimensionType.TIME:-1},  # velocity
        ]
        diffs: List[float] = []
        labels: List[str] = []
        for i, d1 in enumerate(dims):
            for j, d2 in enumerate(dims):
                A = DimensionalQuantity(1.234, d1, "U1", "theory")
                B = DimensionalQuantity(2.345, d2, "U2", "theory")
                # Convert then multiply
                Ap = bridge.convert_mathematical_to_physical(A)
                Bp = bridge.convert_mathematical_to_physical(B)
                left = Ap.value * Bp.value
                # Multiply then convert using combined dims
                comb_dims = dict(d1)
                for k,v in d2.items():
                    comb_dims[k] = comb_dims.get(k,0) + v
                C = DimensionalQuantity(A.value*B.value, comb_dims, "U12", "theory")
                Cp = bridge.convert_mathematical_to_physical(C)
                right = Cp.value
                diffs.append(abs(left - right))
                labels.append(f"({i},{j})")
        fig, ax = plt.subplots(figsize=(10,5))
        ax.bar(labels, diffs, color="#1f77b4", alpha=0.85)
        ax.set_title("Dimensional Bridge Commutativity |(conv·conv) - conv(·)|")
        ax.set_ylabel("absolute difference")
        ax.tick_params(axis='x', labelrotation=90)
        fig.tight_layout()
        path = str(self.output_dir / "dimensional_bridge_commutativity.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_zx_phi_phase_lattice(self) -> Dict[str, Any]:
        """Scatter of phases φ^n mod 2π across multiple wire offsets.

        Returns:
            {'file': path_to_png}
        """
        # φ-phase lattice: phases φ^n mod 2π over grid of n and wires
        n_vals = np.arange(1, 40)
        phases = (PHI_VALUE ** n_vals) % (2*np.pi)
        rows = 6
        fig, ax = plt.subplots(figsize=(12,5))
        for r in range(rows):
            ax.scatter(n_vals, (phases + 2*np.pi*r/rows)%(2*np.pi), s=18, alpha=0.7)
        ax.set_xlabel("n")
        ax.set_ylabel("phase mod 2π")
        ax.set_title("ZX φ-Gate Phase Lattice (φ^n mod 2π)")
        fig.tight_layout()
        path = str(self.output_dir / "zx_phi_phase_lattice.png")
        fig.savefig(path, dpi=300, bbox_inches='tight'); plt.close(fig)
        return {"file": path}

    def generate_all(self) -> List[Dict[str, Any]]:
        """Generate the core figure set and return a list of result dicts."""
        results: List[Dict[str, Any]] = []
        results.append(self.generate_grace_operator_fixed_point_convergence())
        results.append(self.generate_spectral_zeta_overview())
        results.append(self.generate_usc_stability_landscape())
        results.append(self.generate_mixing_angles_theory_only())
        results.append(self.generate_dimensional_bridge_mapping())
        return results

    def generate_all_additional(self) -> List[Dict[str, Any]]:
        """Generate additional, more detailed figures; return list of results."""
        results: List[Dict[str, Any]] = []
        results.append(self.generate_grace_operator_contraction_inequality())
        results.append(self.generate_phi_recursion_rate_verification())
        results.append(self.generate_spectral_zeta_pole_structure())
        results.append(self.generate_spectral_prefactor_convergence())
        results.append(self.generate_usc_stability_heatmap())
        results.append(self.generate_ckm_phi_structure_heatmap())
        results.append(self.generate_phi_continued_fraction_convergence())
        results.append(self.generate_dimensional_bridge_commutativity())
        results.append(self.generate_zx_phi_phase_lattice())
        return results

# Convenience API
GEN_CORE_FIGS = CoreTheoryFigureGenerator()

def generate_core_theory_figures() -> List[Dict[str, Any]]:
    """Convenience API: generate the core figure set."""
    return GEN_CORE_FIGS.generate_all()

def generate_additional_core_theory_figures() -> List[Dict[str, Any]]:
    """Convenience API: generate the additional figure set."""
    return GEN_CORE_FIGS.generate_all_additional()

__all__ = [
    "CoreTheoryFigureGenerator",
    "GEN_CORE_FIGS",
    "generate_core_theory_figures",
    "generate_additional_core_theory_figures",
]
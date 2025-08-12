"""
Validation-Gated Overlays: Plot φ-native predictions alongside sealed experimental
metadata via the Experimental Firewall. No empirical values are embedded in code.
Figures render only when validation mode is enabled and sealed comparisons are available.
"""

from typing import Dict, Any, List
import matplotlib.pyplot as plt
from pathlib import Path

from validation.experimental_firewall import EXPERIMENTAL_FIREWALL

try:
    from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA
except Exception:
    FINE_STRUCTURE_ALPHA = None


class ValidationOverlayFigures:
    """Validation-gated overlays comparing sealed experimental to theory.

    Produces figures only when EXPERIMENTAL_FIREWALL validation is active.
    """
    def __init__(self) -> None:
        self.output_dir = Path("figures")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _try_get_sealed(self, key: str):
        try:
            return EXPERIMENTAL_FIREWALL.get_sealed_comparison(key)
        except Exception:
            return None

    def overlay_fine_structure_alpha(self) -> Dict[str, Any]:
        """Plot 1/α theory vs sealed experimental value with uncertainty.

        Requires validation mode. Returns empty dict if not available.
        """
        # Do not enable validation here; overlays must be externally gated.
        if not getattr(EXPERIMENTAL_FIREWALL, "_validation_phase_active", False):
            return {}
        sealed = self._try_get_sealed("fine_structure_alpha_inv")
        if not (sealed and sealed.get("sealed")):
            return {}

        if FINE_STRUCTURE_ALPHA is None:
            return {}
        theory = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
        theory_val = getattr(theory, "alpha_inverse_value", None)
        if theory_val is None:
            return {}

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.errorbar([0], [sealed["value"]], yerr=[sealed["uncertainty"]], fmt='o', color='black', label='Sealed exp')
        ax.scatter([0], [theory_val], color='gold', zorder=3, label='Theory (φ-native)')
        ax.set_xticks([])
        ax.set_ylabel("α^{-1}")
        ax.set_title("Fine Structure Constant: Theory vs Sealed Experimental (Validation-Gated)")
        ax.legend(loc='best')
        fig.tight_layout()
        out = str(self.output_dir / "overlay_alpha_inverse_validation.png")
        fig.savefig(out, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return {"file": out}

    def generate_all(self) -> List[Dict[str, Any]]:
        results: List[Dict[str, Any]] = []
        r = self.overlay_fine_structure_alpha()
        if r:
            results.append(r)
        # Proton/Electron mass ratio overlay
        r = self._overlay_generic_scalar(
            key="proton_electron_mass_ratio",
            ylabel="m_p/m_e",
            title="Proton-Electron Mass Ratio: Theory vs Sealed Experimental",
        )
        if r:
            results.append(r)
        # Weak mixing angle overlay
        r = self._overlay_generic_scalar(
            key="weak_mixing_angle_sin2",
            ylabel="sin^2(θ_W)",
            title="Weak Mixing Angle: Theory vs Sealed Experimental",
        )
        if r:
            results.append(r)
        return results

    def _overlay_generic_scalar(self, key: str, ylabel: str, title: str) -> Dict[str, Any]:
        """Generic overlay helper for single scalar comparisons (gated)."""
        if not getattr(EXPERIMENTAL_FIREWALL, "_validation_phase_active", False):
            return {}
        sealed = self._try_get_sealed(key)
        if not (sealed and sealed.get("sealed")):
            return {}
        # Try to obtain a theory value from our modules if present; otherwise, abort silently
        try:
            theory_val = None
            if key == "proton_electron_mass_ratio":
                from constants.mass_ratios import FUNDAMENTAL_MASSES
                theory_val = FUNDAMENTAL_MASSES.get_mass_ratio("proton", "electron")
            elif key == "weak_mixing_angle_sin2":
                from constants.mixing_angles import MixingAnglesDerivation
                theory_val = MixingAnglesDerivation().derive_weinberg_angle_sin2()
        except Exception:
            theory_val = None
        if theory_val is None:
            return {}
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.errorbar([0], [sealed["value"]], yerr=[sealed["uncertainty"]], fmt='o', color='black', label='Sealed exp')
        ax.scatter([0], [theory_val], color='gold', zorder=3, label='Theory (φ-native)')
        ax.set_xticks([])
        ax.set_ylabel(ylabel)
        ax.set_title(f"{title} (Validation-Gated)")
        ax.legend(loc='best')
        fig.tight_layout()
        out_name = f"overlay_{key}_validation.png"
        out = str(self.output_dir / out_name)
        fig.savefig(out, dpi=300, bbox_inches='tight')
        plt.close(fig)
        return {"file": out}


VALIDATION_OVERLAYS = ValidationOverlayFigures()

__all__ = ["ValidationOverlayFigures", "VALIDATION_OVERLAYS"]


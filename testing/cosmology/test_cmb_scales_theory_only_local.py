import math
import numpy as np

from cosmology.cmb_power_spectrum import AcousticPeakStructure


def test_acoustic_scale_and_silk_relation_phi_squared():
    cmb = AcousticPeakStructure()
    # Trigger internal scale computations
    _ = cmb.compute_cmb_power_spectrum(ell_max=256)
    theta_A = cmb._angular_acoustic_scale or cmb._compute_angular_acoustic_scale()
    l1 = math.pi / theta_A
    lsilk = cmb._silk_damping_scale or cmb._compute_silk_damping_scale()
    # Expect ℓ_silk ≈ ℓ1 / φ^2 within a modest tolerance (heuristic theory-only check)
    phi = (1 + 5**0.5) / 2
    assert abs(lsilk - l1 * phi ** (-2)) / max(1.0, l1) < 0.25


def test_isw_component_decays_with_ell():
    cmb = AcousticPeakStructure()
    ell = np.arange(2, 200)
    isw = cmb._compute_integrated_sachs_wolfe(ell)
    # Monotonic decay in aggregate (allow small numerical noise): first > median > last
    assert isw[0] > np.median(isw) > isw[-1]

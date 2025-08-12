import math
from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_spectral_zeta_small_modes_paths():
    sz = SpectralZetaRegularization()
    # tighten modes for speed
    sz._max_n_mode = 2
    sz._max_l_mode = 2
    spec = sz.compute_laplacian_eigenvalues()
    assert spec["total_modes"] > 0
    z = sz.compute_phi_weighted_zeta_function(s=1.0)
    assert "zeta_value" in z
    res = sz.compute_spectral_prefactor()
    assert isinstance(res.theoretical_value, float)
    assert math.isfinite(res.theoretical_value)


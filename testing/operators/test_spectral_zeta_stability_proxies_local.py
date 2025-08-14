from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_spectral_zeta_convergence_fields_are_finite():
    sz = SpectralZetaRegularization()
    res = sz.compute_spectral_prefactor()
    conv = res.convergence_analysis
    for k in ("zero_point_convergence", "zeta_function_convergence", "mode_cutoff_dependence", "phi_weighting_stability"):
        assert k in conv and isinstance(conv[k], float)
        assert conv[k] >= 0.0

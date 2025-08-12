from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_spectral_zeta_convergence_and_prefactor_shape():
    sz = SpectralZetaRegularization()
    z1 = sz.compute_phi_weighted_zeta_function(0.5)
    assert isinstance(z1["zeta_value"], float)
    res = sz.compute_spectral_prefactor()
    assert hasattr(res, "theoretical_value") and isinstance(res.theoretical_value, float)
    conv = res.convergence_analysis
    assert "zero_point_convergence" in conv and "zeta_function_convergence" in conv


from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_phi_weighted_zeta_analytic_continuation_near_zero():
    sz = SpectralZetaRegularization()
    r0 = sz.compute_phi_weighted_zeta_function(0.0)
    assert "finite_part" in r0 and isinstance(r0["finite_part"], float)
    assert any("Analytical continuation" in s for s in r0["derivation_steps"])
    r05 = sz.compute_phi_weighted_zeta_function(0.05)
    assert "finite_part" in r05 and isinstance(r05["finite_part"], float)

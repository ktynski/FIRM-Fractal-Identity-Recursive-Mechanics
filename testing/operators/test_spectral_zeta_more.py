from foundation.operators.spectral_zeta import SpectralZetaRegularization


def test_spectral_zeta_more_paths():
    sz = SpectralZetaRegularization()
    sz._max_n_mode = 1
    sz._max_l_mode = 1
    z2 = sz.compute_phi_weighted_zeta_function(s=2.0)
    assert "zeta_value" in z2
    # degeneracy helper indirectly via eigenvalues already hit; ensure prefactor fields exist
    pref = sz.compute_spectral_prefactor()
    # Check known keys present in convergence analysis
    keys = pref.convergence_analysis.keys()
    assert "zeta_function_convergence" in keys
    assert "mode_cutoff_dependence" in keys

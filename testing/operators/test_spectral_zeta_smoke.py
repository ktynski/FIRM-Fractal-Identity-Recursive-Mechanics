def test_spectral_zeta_basic_paths(monkeypatch):
    from foundation.operators.spectral_zeta import SpectralZetaRegularization
    sz = SpectralZetaRegularization()
    # dial down modes to keep runtime small
    monkeypatch.setattr(sz, "_max_n_mode", 5, raising=False)
    monkeypatch.setattr(sz, "_max_l_mode", 5, raising=False)
    spec = sz.compute_laplacian_eigenvalues()
    assert spec["total_modes"] > 0
    zeta = sz.compute_phi_weighted_zeta_function(0.5)
    assert "zeta_value" in zeta
    zpe = sz.compute_zero_point_energy_phi_weighted()
    assert "zero_point_energy" in zpe
    res = sz.compute_spectral_prefactor()
    assert hasattr(res, "theoretical_value")


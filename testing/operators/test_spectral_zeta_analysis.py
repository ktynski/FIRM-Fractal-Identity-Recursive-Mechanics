def test_spectral_zeta_internal_analyses(monkeypatch):
    from foundation.operators.spectral_zeta import SpectralZetaRegularization
    sz = SpectralZetaRegularization()
    monkeypatch.setattr(sz, "_max_n_mode", 3, raising=False)
    monkeypatch.setattr(sz, "_max_l_mode", 3, raising=False)
    # Exercise analysis helpers
    zc = sz._analyze_zero_point_convergence()
    zc2 = sz._analyze_zeta_convergence()
    ph = sz._analyze_phi_weighting_stability()
    # Compute other components
    main = sz._compute_main_spectral_contribution()
    ghost = sz._compute_ghost_mode_contribution_explicit()
    norm = sz._compute_zeta_normalization()
    assert all(isinstance(v, float) for v in (zc, zc2, ph, main, ghost, norm))

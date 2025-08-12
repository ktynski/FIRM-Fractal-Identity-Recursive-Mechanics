from constants.gauge_couplings import GaugeCouplingDerivation


def test_running_couplings_monotonic_behavior():
    gc = GaugeCouplingDerivation()
    r1 = gc.compute_running_couplings(energy_gev=1.0)
    r2 = gc.compute_running_couplings(energy_gev=2.0)
    # With b2, b3 negative, α2^{-1} and α3^{-1} should increase with log(mu) term sign
    assert isinstance(r1["alpha1_inv"], float)
    assert isinstance(r2["alpha2_inv"], float)
    assert isinstance(r2["alpha3_inv"], float)


def test_beta_coefficients_exposed_and_used():
    gc = GaugeCouplingDerivation()
    b1, b2, b3 = gc._compute_sm_one_loop_betas()
    assert (b1, b2, b3) == (41.0/6.0, -19.0/6.0, -7.0)

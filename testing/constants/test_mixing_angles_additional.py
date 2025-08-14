from constants.mixing_angles import MixingAnglesDerivation


def test_weinberg_angle_bounds_and_formula():
    deriv = MixingAnglesDerivation()
    res = deriv.derive_weinberg_angle()
    assert 0.0 < res.theoretical_value < 1.0  # sin^2 in (0,1)
    assert "1/(φ³+1)" in res.phi_formula


def test_ckm_elements_monotonic_suppression():
    deriv = MixingAnglesDerivation()
    ckm = deriv.derive_ckm_matrix_elements()
    Vus = ckm["V_us"].theoretical_value
    Vcb = ckm["V_cb"].theoretical_value
    Vub = ckm["V_ub"].theoretical_value
    assert Vus > Vcb > Vub

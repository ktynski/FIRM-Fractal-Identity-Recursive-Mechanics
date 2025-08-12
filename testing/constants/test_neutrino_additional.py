from constants.neutrino import NeutrinoParametersDerivation, MixingAngle


def test_neutrino_mass_hierarchy_and_splittings():
    deriv = NeutrinoParametersDerivation()
    results = deriv.derive_all_neutrino_parameters()
    ms = results["mass_scale"].theoretical_value
    assert ms > 0
    spl = results["mass_splittings"]
    assert spl["delta_m21_squared"].theoretical_value > 0
    assert spl["delta_m31_squared"].theoretical_value > 0


def test_neutrino_mixing_angles_ranges():
    deriv = NeutrinoParametersDerivation()
    a12 = deriv.derive_mixing_angle(MixingAngle.THETA_12)
    a23 = deriv.derive_mixing_angle(MixingAngle.THETA_23)
    a13 = deriv.derive_mixing_angle(MixingAngle.THETA_13)
    # Degrees in (0,90) by construction
    for a in (a12, a23, a13):
        assert 0.0 < a.theoretical_value < 90.0


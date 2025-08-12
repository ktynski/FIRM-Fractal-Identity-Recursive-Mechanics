from constants.neutrino import NeutrinoParametersDerivation, MixingAngle


def test_mass_scale_and_splittings_signs():
    d = NeutrinoParametersDerivation()
    scale = d.derive_neutrino_mass_scale()
    assert scale.theoretical_value > 0
    spl = d.derive_mass_splittings()
    assert spl["delta_m21_squared"].theoretical_value > 0
    assert spl["delta_m31_squared"].theoretical_value > 0


def test_mixing_angles_ranges_monotonicity():
    d = NeutrinoParametersDerivation()
    a12 = d.derive_mixing_angle(MixingAngle.THETA_12)
    a23 = d.derive_mixing_angle(MixingAngle.THETA_23)
    a13 = d.derive_mixing_angle(MixingAngle.THETA_13)
    # Reactor angle smallest
    assert a13.theoretical_value < a12.theoretical_value
    assert a13.theoretical_value < a23.theoretical_value
    # All positive degrees
    assert a12.theoretical_value > 0 and a23.theoretical_value > 0 and a13.theoretical_value > 0


def test_neutrino_full_parameters_summary():
    d = NeutrinoParametersDerivation()
    results = d.derive_all_neutrino_parameters()
    assert "summary" in results and isinstance(results["summary"], dict)
    assert results["summary"]["total_parameters"] == 7

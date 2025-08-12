from constants.neutrino import NeutrinoParametersDerivation, MixingAngle


def test_neutrino_mass_scale_provenance_builds():
    d = NeutrinoParametersDerivation()
    tree = d.build_mass_scale_provenance()
    assert tree is not None
    assert "m_ν" in tree.target_result


def test_neutrino_mixing_angle_provenance_builds():
    d = NeutrinoParametersDerivation()
    for ang in (MixingAngle.THETA_12, MixingAngle.THETA_23, MixingAngle.THETA_13):
        t = d.build_mixing_angle_provenance(ang)
        assert t is not None
        assert ang.value in t.target_result


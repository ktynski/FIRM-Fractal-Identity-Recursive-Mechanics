from theory.physics.forces.gluon_torsion_framework import GLUON_TORSION_FRAMEWORK, derive_qcd_integration


def test_gluon_torsion_smoke():
    res = derive_qcd_integration()
    assert res.strong_coupling_alpha_s > 0
    assert isinstance(res.color_charges, list) and len(res.color_charges) == 3
    assert isinstance(res.mathematical_derivation, list) and len(res.mathematical_derivation) >= 3

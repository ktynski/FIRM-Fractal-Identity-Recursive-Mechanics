import math

from constants.mixing_angles import MixingAnglesDerivation


def test_weinberg_angle_derivation_and_provenance():
    mad = MixingAnglesDerivation()
    res = mad.derive_weinberg_angle()
    assert isinstance(res.theoretical_value, float)
    # Basic sanity: sin^2(theta_W) in (0,1)
    assert 0.0 < res.theoretical_value < 1.0
    # Provenance tree builds
    tree = mad.build_weinberg_provenance()
    assert tree is not None
    assert "sin²θ_W" in tree.target_result or "sin^2" in tree.target_result


def test_ckm_elements_and_provenance_builders():
    mad = MixingAnglesDerivation()
    results = mad.derive_ckm_matrix_elements()
    for key in ("V_us", "V_cb", "V_ub"):
        assert key in results
        val = results[key].theoretical_value
        assert 0.0 < val < 1.0
        tree = mad.build_ckm_provenance(key)
        assert tree is not None
        assert key in tree.target_result


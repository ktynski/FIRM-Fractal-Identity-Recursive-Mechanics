from constants.mixing_angles import MixingAnglesDerivation


def test_weinberg_angle_properties_and_provenance():
    d = MixingAnglesDerivation()
    res = d.derive_weinberg_angle()
    assert 0.0 < res.theoretical_value < 1.0
    assert "1/(φ³+1)" in res.phi_formula
    assert isinstance(res.provenance_hash, str) and len(res.provenance_hash) > 0


def test_ckm_ordering_and_formulas():
    d = MixingAnglesDerivation()
    ckm = d.derive_ckm_matrix_elements()
    us = ckm["V_us"].theoretical_value
    cb = ckm["V_cb"].theoretical_value
    ub = ckm["V_ub"].theoretical_value
    assert us > cb > ub
    assert "φ⁻²" in ckm["V_us"].phi_formula
    assert "φ⁻⁴" in ckm["V_cb"].phi_formula
    assert "φ⁻⁶" in ckm["V_ub"].phi_formula


def test_cp_phase_symbol_and_units():
    d = MixingAnglesDerivation()
    res = d.derive_cp_violation_phase()
    assert res.symbol == "δ"
    assert res.theoretical_value > 0


def test_all_mixing_angles_summary_shape():
    d = MixingAnglesDerivation()
    results = d.derive_all_mixing_angles()
    assert "summary" in results and isinstance(results["summary"], dict)
    assert results["summary"]["total_parameters"] == 5
    assert results["summary"]["contamination_free"] is True

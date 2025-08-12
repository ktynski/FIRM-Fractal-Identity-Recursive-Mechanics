import math
import pytest
from constants.mixing_angles import MixingAnglesDerivation


def test_weinberg_angle_values_and_derivation_steps():
    d = MixingAnglesDerivation()
    res = d.derive_weinberg_angle()
    assert 0.0 < res.theoretical_value < 1.0
    assert "φ" in res.phi_formula or "phi" in res.phi_formula.lower()
    assert isinstance(res.derivation_steps, list) and len(res.derivation_steps) > 0
    assert isinstance(res.provenance_hash, str)


def test_ckm_elements_values_and_steps():
    d = MixingAnglesDerivation()
    ckm = d.derive_ckm_matrix_elements()
    assert set(["V_us", "V_cb", "V_ub"]).issubset(ckm.keys())
    for key, val in ckm.items():
        assert val.theoretical_value > 0
        assert isinstance(val.derivation_steps, list) and len(val.derivation_steps) > 0
        assert isinstance(val.provenance_hash, str)


def test_cp_phase_and_degrees_computation():
    d = MixingAnglesDerivation()
    cp = d.derive_cp_violation_phase()
    assert cp.theoretical_value > 0
    # Exercise math.degrees pathway indirectly present in derivation steps
    deg = math.degrees(cp.theoretical_value)
    assert deg > 0


def test_provenance_builders_and_invalid_element():
    d = MixingAnglesDerivation()
    w = d.build_weinberg_provenance()
    assert hasattr(w, "root_node") or hasattr(w, "target_result")
    for elem in ("V_us", "V_cb", "V_ub"):
        t = d.build_ckm_provenance(elem)
        assert t is not None
    with pytest.raises(ValueError):
        d.build_ckm_provenance("invalid")


def test_all_mixing_angles_and_summary_print(capsys):
    d = MixingAnglesDerivation()
    results = d.derive_all_mixing_angles()
    assert "summary" in results and isinstance(results["summary"], dict)
    d.print_results_summary(results)
    out = capsys.readouterr().out
    assert "FIRM MIXING ANGLES" in out

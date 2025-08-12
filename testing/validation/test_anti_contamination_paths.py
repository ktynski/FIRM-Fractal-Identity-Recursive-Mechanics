import pytest

from validation.anti_contamination import AntiContamination, ContaminationError


def test_scan_for_contamination_detects_patterns_and_values():
    code = "alpha_inv = 137.035999084  # suspicious"
    values = [137.035999084, 3.14159]
    with pytest.raises(ContaminationError):
        AntiContamination.scan_for_contamination(code, values)


def test_code_and_value_scanners_paths():
    ac = AntiContamination()
    code_hits = ac._scan_code_for_contamination("Observed value with codata reference 299792458")
    assert any("Empirical keyword" in h or "Pattern match" in h or "Hardcoded constant" in h for h in code_hits)

    val_hits = ac._scan_values_for_contamination([1.0, 299792458.0])
    assert any("matches" in h or "Suspicious precision" in h for h in val_hits)


def test_mathematical_justification_interface():
    ac = AntiContamination()
    ok = ac.check_mathematical_justification(value=1.0, justification="Derived from phi recursion")
    assert isinstance(ok, bool)

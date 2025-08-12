import pytest
from validation.anti_contamination import AntiContamination, ContaminationError


def test_numeric_literal_detection_flags_codatalike():
    code = "def f():\n  return 137.035999084\n"
    ac = AntiContamination()
    hits = ac._scan_code_for_contamination(code)
    assert any("137.035999084" in h for h in hits)


def test_whitelisted_trivial_literals_allowed():
    code = "def g(x):\n  return 1 if x>0 else -1 if x<0 else 0\n"
    ac = AntiContamination()
    hits = ac._scan_code_for_contamination(code)
    # Should not include hardcoded constant violations for trivial literals
    assert all("Hardcoded constant" not in h for h in hits)


def test_scan_for_contamination_combined_raises():
    code = "def h():\n  return 299792458\n"
    with pytest.raises(ContaminationError):
        AntiContamination.scan_for_contamination(code, [299792458])

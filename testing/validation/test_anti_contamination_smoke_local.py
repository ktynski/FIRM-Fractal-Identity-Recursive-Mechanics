from validation.anti_contamination import AntiContamination, ContaminationError


def test_anti_contamination_scans_and_flags():
    ac = AntiContamination()
    # Code scan should flag forbidden constants and keywords
    code = "alpha_inv = 137.035999084  # measured; CODATA"
    alerts = ac._scan_code_for_contamination(code)
    assert any("Hardcoded constant" in a for a in alerts)
    assert any("Empirical keyword" in a for a in alerts)

    # Values scan flags forbidden value and suspicious precision
    vals = [137.035999084, 1.234567890123]
    valerts = ac._scan_values_for_contamination(vals)
    assert any("matches" in a or "Suspicious precision" in a for a in valerts)

    # is_empirical_value on nested containers
    assert ac.is_empirical_value({"note": "measured", "v": 3.14}) is True
    assert ac.is_empirical_value([0.1184, 0.1]) is True

    # check_mathematical_justification
    assert ac.check_mathematical_justification(1.0, "derived from φ recursion and fixed point") is True
    assert ac.check_mathematical_justification(137.035999084, "derived mathematically") is False
    assert ac.check_mathematical_justification(1.0, "measured by experiment") is False

    # validate_derivation_purity
    assert ac.validate_derivation_purity([
        {"value": 1.0, "justification": "derived mathematically via axioms"}
    ]) is True
    assert ac.validate_derivation_purity([
        {"value": 137.035999084, "justification": "derived mathematically"}
    ]) is False

    # scan_for_contamination raises on combined issues
    try:
        AntiContamination.scan_for_contamination(code, vals)
        assert False, "expected contamination error"
    except ContaminationError:
        pass

from validation.anti_contamination import ANTI_CONTAMINATION


def test_generate_contamination_report_contains_sections():
    rep = ANTI_CONTAMINATION.generate_contamination_report()
    assert "ANTI-CONTAMINATION REPORT" in rep
    assert "FORBIDDEN CONSTANTS DATABASE" in rep
    assert "EMPIRICAL KEYWORDS" in rep
    assert "SUSPICIOUS PATTERNS" in rep
    assert "CONTAMINATION ALERTS" in rep

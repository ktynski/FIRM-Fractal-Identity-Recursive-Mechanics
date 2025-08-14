from validation.anti_contamination import ANTI_CONTAMINATION


def test_mutators_and_summary_paths():
    ANTI_CONTAMINATION.add_custom_forbidden_constant(42.0, "Test constant")
    ANTI_CONTAMINATION.add_custom_empirical_keyword("calibrated")
    ANTI_CONTAMINATION.add_custom_suspicious_pattern(r"42\.0")
    summary = ANTI_CONTAMINATION.get_forbidden_constants_summary()
    assert isinstance(summary, dict)
    assert sum(summary.values()) >= 1

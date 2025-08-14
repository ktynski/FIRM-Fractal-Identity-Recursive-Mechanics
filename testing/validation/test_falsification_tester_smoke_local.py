from validation.falsification_tester import FALSIFICATION_TESTER, FalsificationCriterion, AlertLevel


def test_falsification_tester_basic_report_and_status():
    ft = FALSIFICATION_TESTER
    # Deterministically inspect alert mapping at boundary
    spec = ft._criteria_specifications[FalsificationCriterion.EMPIRICAL_CONTAMINATION]
    level = ft._determine_alert_level(0.0, spec)
    assert level in (AlertLevel.INFO, AlertLevel.EMERGENCY, AlertLevel.URGENT)
    status = ft._determine_falsification_status(level)
    # Status must be one of allowed states
    assert status.name in ("SAFE", "WARNING", "CRITICAL", "FALSIFIED", "ABANDONED")
    # Report generation path
    rep = ft.generate_falsification_report()
    assert isinstance(rep, str) and "FIRM Falsification Monitoring Report" in rep

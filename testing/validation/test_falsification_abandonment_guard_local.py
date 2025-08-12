import os
from validation.falsification_tester import FalsificationTester, FalsificationCriterion, FalsificationStatus, AlertLevel


def test_abandonment_guard_and_alert_generation(monkeypatch):
    tester = FalsificationTester()
    monkeypatch.setenv('FIRM_SILENT_TESTS', '1')
    # Force an emergency alert via observed value above highest threshold for one spec
    # Pick a spec and monkeypatch its evaluation to return very large value
    # Choose a criterion with zero threshold to guarantee alert: EMPIRICAL_CONTAMINATION
    crit = FalsificationCriterion.EMPIRICAL_CONTAMINATION
    spec = tester._criteria_specifications[crit]
    # Force a positive observed value to exceed threshold 0.0
    monkeypatch.setattr(tester, '_evaluate_empirical_contamination', lambda: 0.5, raising=True)
    # Check triggers
    tester._check_falsification_criterion(crit, spec)
    status = tester.get_current_status()
    # At least one alert must be recorded
    assert status["total_alerts"] >= 1


import os
from validation.falsification_tester import FalsificationTester, FalsificationCriterion, AlertLevel


def test_alert_level_transitions_and_single_checker_alias(monkeypatch):
    tester = FalsificationTester()
    monkeypatch.setenv('FIRM_SILENT_TESTS', '1')
    # Create a dummy spec with thresholds
    spec = next(iter(tester._criteria_specifications.values()))
    # Sanity over mapping function
    assert isinstance(tester._determine_alert_level(0.0, spec), AlertLevel)
    # Alias should invoke underlying checker without raising
    tester._check_single_criterion(spec.criterion, spec)

from validation.falsification_tester import FalsificationTester, FalsificationCriterion


def test_emergency_path_no_abandonment_output(monkeypatch):
    tester = FalsificationTester()
    monkeypatch.setenv('FIRM_SILENT_TESTS', '1')
    # Force an emergency by setting categorical coherence very low
    monkeypatch.setattr(tester, '_evaluate_categorical_coherence', lambda: 0.0, raising=True)
    # Run a single check for that criterion
    spec = tester._criteria_specifications[FalsificationCriterion.CATEGORICAL_COHERENCE]
    tester._check_falsification_criterion(FalsificationCriterion.CATEGORICAL_COHERENCE, spec)
    # Ensure internal flags updated and history has at least one alert
    status = tester.get_current_status()
    assert status['total_alerts'] >= 1
    # Abandonment may be triggered; ensure report still generates
    report = tester.generate_falsification_report()
    assert 'FIRM Falsification Monitoring Report' in report

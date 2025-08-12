from validation.falsification_tester import FalsificationTester, AlertLevel


def test_falsification_evaluators_and_report(monkeypatch):
    tester = FalsificationTester()
    # Prevent abandonment side effects by muting abandonment path
    monkeypatch.setenv('FIRM_SILENT_TESTS', '1')

    # Force specific observed values via evaluator monkeypatching to hit branches
    monkeypatch.setattr(tester, '_evaluate_parameter_tuning', lambda: 0.15, raising=True)  # WARNING
    monkeypatch.setattr(tester, '_evaluate_mathematical_consistency', lambda: 0.0, raising=True)  # SAFE
    monkeypatch.setattr(tester, '_evaluate_phi_recursion', lambda: 1e-12, raising=True)  # SAFE
    monkeypatch.setattr(tester, '_evaluate_empirical_contamination', lambda: 0.0, raising=True)  # SAFE
    monkeypatch.setattr(tester, '_evaluate_categorical_coherence', lambda: 0.9, raising=True)  # SAFE
    monkeypatch.setattr(tester, '_evaluate_experimental_agreement', lambda: 1.2, raising=True)  # WARNING/URGENT depending on thresholds
    monkeypatch.setattr(tester, '_evaluate_consciousness_integration', lambda: 0.0, raising=True)  # SAFE

    # Run one monitoring sweep synchronously using internal method
    for spec in tester._criteria_specifications.values():
        # Directly invoke private check to avoid waiting on thread
        tester._check_falsification_criterion(spec.criterion, spec)

    # Generate report and check fields
    report = tester.generate_falsification_report()
    assert "FIRM Falsification Monitoring Report" in report
    # Ensure some alert summary fields appear deterministically
    assert "ALERT SUMMARY" in report

    # Alert level mapping sanity via helper
    level = tester._determine_alert_level(0.2, next(iter(tester._criteria_specifications.values())))
    assert isinstance(level, AlertLevel)


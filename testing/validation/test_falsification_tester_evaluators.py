from validation.falsification_tester import FALSIFICATION_TESTER


def test_evaluators_return_reasonable_ranges():
    t = FALSIFICATION_TESTER
    # These should return finite floats, and within conservative bounds
    assert isinstance(t._evaluate_parameter_tuning(), float)
    assert isinstance(t._evaluate_mathematical_consistency(), float)
    assert isinstance(t._evaluate_phi_recursion(), float)
    assert 0.0 <= t._evaluate_empirical_contamination() <= 1.0
    assert 0.0 <= t._evaluate_categorical_coherence() <= 1.0
    assert t._evaluate_experimental_agreement() >= 0.0
    assert 0.0 <= t._evaluate_consciousness_integration() <= 1.0


def test_generate_falsification_report_sections():
    t = FALSIFICATION_TESTER
    report = t.generate_falsification_report()
    assert "FIRM Falsification Monitoring Report" in report
    assert "FALSIFICATION CRITERIA STATUS" in report
    assert "ALERT SUMMARY" in report

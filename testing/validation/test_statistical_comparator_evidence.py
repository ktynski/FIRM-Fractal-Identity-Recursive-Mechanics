import numpy as np

from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_evidence_strength_buckets_and_report_shape():
    sc = StatisticalComparator()
    sc.enable_validation_mode()

    # Craft synthetic results to exercise global analysis without firewall
    def make_result(ts: float, p: float, bf: float | None) -> StatisticalResult:
        return StatisticalResult(
            test_name="t",
            theoretical_value=0.0,
            experimental_value=0.0,
            experimental_uncertainty=1.0,
            test_statistic=ts,
            p_value=p,
            confidence_interval=(0.0, 1.0),
            statistical_significance=0.0,
            degrees_of_freedom=1,
            test_type=StatisticalTest.CHI_SQUARED,
            hypothesis_type=HypothesisType.TWO_SIDED,
            bayes_factor=bf,
        )

    results = [
        make_result(0.1, 0.9, 1e6),     # decisive
        make_result(0.2, 0.8, 1e2),     # very_strong
        make_result(0.3, 0.7, 10.0),    # strong
        make_result(0.4, 0.6, 3.5),     # substantial
        make_result(0.5, 0.5, 0.8),     # weak_against/insufficient
    ]
    # Report generation should work on overrides
    report = sc.generate_statistical_report(results_override=results)
    assert "FIRM Statistical Validation Report" in report

    # Global analysis should compute and classify evidence
    analysis = sc._perform_global_analysis(results)
    assert set(["global_chi_squared", "global_p_value", "evidence_strength"]).issubset(analysis.keys())


import types
import pytest

import validation.__init__ as vinit


class _Stat:
    def __init__(self, name: str):
        self.test_type = "chi_squared"
        self.test_name = name
        self.p_value = 0.1
        self.statistical_significance = 1.0
        self.theoretical_value = 1.0
        self.experimental_value = 1.0
        self.experimental_uncertainty = 0.1


def test_validation_includes_ready_chi_squared(monkeypatch):
    # Provide comparator with one chi-squared test
    class DummyComp:
        _global_statistics = {}
        def enable_validation_mode(self):
            pass
        def comprehensive_validation_analysis(self):
            return {"total_tests": 1, "individual_tests": [_Stat("fine_structure_alpha_inv_chi_squared")], "metadata": {}}
    monkeypatch.setattr(vinit, "STATISTICAL_COMPARATOR", DummyComp(), raising=False)

    # Firewall marks fine structure as validation-ready
    class DummyFW:
        _validation_ready_keys = {"fine_structure_alpha_inv"}
        def generate_firewall_report(self):
            return "ACTIVE; ALL INTACT"
        def enable_validation_phase(self):
            pass
    monkeypatch.setattr(vinit, "EXPERIMENTAL_FIREWALL", DummyFW(), raising=False)

    results = vinit.validate_all_firm_predictions()
    # Should include our chi-squared item with a validation_status field
    key = "fine_structure_alpha_inv_chi_squared"
    assert key in results
    assert hasattr(results[key], "validation_status")

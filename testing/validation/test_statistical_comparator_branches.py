from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_chi_squared_and_bayesian_report_fields():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    chi = comp.perform_chi_squared_test(1.0, 0.0, 1.0, "x_chi_squared")
    bay = comp.perform_bayesian_comparison(1.0, 0.0, 1.0, "x_bayes")
    report = comp.generate_statistical_report([chi, bay])
    assert "GLOBAL ANALYSIS" in report
    # Ensure Bayesian branch populated likely fields
    assert ("Bayes" in report) or ("Bayesian" in report)
import numpy as np
import math

from validation.statistical_comparator import (
    StatisticalComparator,
    StatisticalResult,
    StatisticalTest,
    HypothesisType,
)


def make_result(name: str, p: float, stat: float, dof: int = 1, bf: float | None = None):
    return StatisticalResult(
        test_name=name,
        theoretical_value=1.0,
        experimental_value=1.0,
        experimental_uncertainty=1.0,
        test_statistic=stat,
        p_value=p,
        confidence_interval=(0.0, 0.0),
        statistical_significance=0.0 if p > 0 else float("inf"),
        degrees_of_freedom=dof,
        test_type=StatisticalTest.CHI_SQUARED,
        hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=bf,
        log_likelihood=None,
        aic_score=None,
        bic_score=None,
    )


def test_bayes_factor_and_posterior_paths():
    comp = StatisticalComparator()
    bf = comp._bayesian.compute_bayes_factor(likelihood_firm=0.8, likelihood_null=0.2, prior_firm=0.5, prior_null=0.5)
    assert bf == 4.0
    post = comp._bayesian.posterior_probability(bayes_factor=bf, prior_firm=0.5)
    assert 0.7 < post < 0.9


def test_credible_interval_computation():
    comp = StatisticalComparator()
    samples = np.linspace(-1.0, 1.0, 1001)
    lo, hi = comp._bayesian.credible_interval(samples, confidence=0.90)
    assert math.isfinite(lo) and math.isfinite(hi)
    assert lo < 0 < hi


def test_global_analysis_and_bonferroni_paths():
    comp = StatisticalComparator()
    # Build a mix of significant and non-significant results
    results = [
        make_result("t1", p=0.04, stat=2.0),
        make_result("t2", p=0.2, stat=0.5),
        make_result("t3", p=0.001, stat=10.0, bf=10.0),
    ]
    # Inject as computed results and generate report (covers aggregate paths)
    comp._statistical_results = results
    report = comp.generate_statistical_report()
    assert "GLOBAL ANALYSIS" in report


def test_likelihood_ratio_interface_shapes():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    # Minimal dataset for LR test; relies on comparator guarding internal math
    data = {"x": (1.0, 0.2)}
    res = comp.perform_likelihood_ratio_test(
        firm_params={"x": 1.0}, null_params={"x": 1.0}, data=data
    )
    assert res.test_type.value in {"likelihood_ratio", "chi_squared"}

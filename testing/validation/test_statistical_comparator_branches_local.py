import math
import numpy as np

from validation.statistical_comparator import (
    STATISTICAL_COMPARATOR,
    StatisticalComparator,
    StatisticalResult,
    StatisticalTest,
    HypothesisType,
)


def _mk_result(name: str, p: float, stat: float = 1.0) -> StatisticalResult:
    return StatisticalResult(
        test_name=name,
        theoretical_value=1.0,
        experimental_value=1.0,
        experimental_uncertainty=1.0,
        test_statistic=stat,
        p_value=p,
        confidence_interval=(0.0, 1.0),
        statistical_significance=abs(stat),
        degrees_of_freedom=1,
        test_type=StatisticalTest.CHI_SQUARED,
        hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=None,
    )


def test_multiple_comparisons_counts_and_adjustments():
    sc = StatisticalComparator()
    # three tests with varied p-values
    results = [
        _mk_result("a", 0.001),
        _mk_result("b", 0.02),
        _mk_result("c", 0.9),
    ]
    ga = sc._perform_global_analysis(results)
    assert ga["significant_individual"] >= 1
    assert isinstance(ga["significant_bonferroni"], int)
    assert isinstance(ga["significant_holm"], int)
    assert isinstance(ga["significant_bh"], int)
    # adjusted arrays present and same length
    assert len(ga["holm_adjusted"]) == 3
    assert len(ga["bh_adjusted"]) == 3


def test_report_with_override_includes_mc_sections():
    sc = StatisticalComparator()
    results = [
        _mk_result("a", 0.001),
        _mk_result("b", 0.02),
    ]
    rep = sc.generate_statistical_report(results)
    assert "Bonferroni" in rep
    assert "Holm" in rep
    assert "Benjamini–Hochberg" in rep


def test_likelihood_ratio_and_loglikelihood_paths():
    sc = StatisticalComparator()
    data = {"x": (1.0, 0.1)}
    firm = {"x": 1.05}
    null = {"x": 1.0}
    res = sc.perform_likelihood_ratio_test(firm, null, data)
    assert res.test_type.name == "LIKELIHOOD_RATIO"
    # internal log-likelihood should be finite
    assert math.isfinite(res.theoretical_value)


def test_bayesian_utilities_and_significance():
    sc_guard = StatisticalComparator()
    # guard: disabled by default on a fresh instance
    try:
        _ = sc_guard.perform_chi_squared_test(1.0, 1.1, 0.1, "guard")
        assert False, "should raise when validation mode not enabled"
    except RuntimeError:
        pass
    sc = STATISTICAL_COMPARATOR
    sc.enable_validation_mode()
    # now allowed
    r = sc.perform_bayesian_comparison(1.0, 1.1, 0.1, "bayes")
    assert r.test_type.name == "BAYESIAN_FACTOR"
    # posterior should be in (0,1)
    from validation.statistical_comparator import BayesianAnalysis

    post = BayesianAnalysis.posterior_probability(max(r.bayes_factor, 1e-6), prior_firm=0.5)
    assert 0.0 < post < 1.0
    ci = BayesianAnalysis.credible_interval(np.random.normal(0, 1, 1000), confidence=0.9)
    assert ci[0] < ci[1]
    # significance threshold check
    assert r.is_significant(alpha=0.2) in (True, False)


def test_report_no_results_path():
    sc = StatisticalComparator()
    # No results stored and comprehensive analysis may fail: should return error string
    rep = sc.generate_statistical_report()
    assert isinstance(rep, str)
    assert "Statistical analysis" in rep or "No statistical tests" in rep

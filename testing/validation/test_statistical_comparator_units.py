from validation.statistical_comparator import STATISTICAL_COMPARATOR


def test_chi_squared_and_bayes_and_global_stats():
    sc = STATISTICAL_COMPARATOR
    sc.enable_validation_mode()
    # perform a couple of tests to exercise result aggregation and evidence strength
    r1 = sc.perform_chi_squared_test(theoretical=1.0, experimental=1.1, uncertainty=0.1, test_name="t1_chi")
    r2 = sc.perform_bayesian_comparison(theoretical=1.0, experimental=1.1, uncertainty=0.1, test_name="t2_bayes")
    assert r1.test_type.name == "CHI_SQUARED"
    assert r2.test_type.name == "BAYESIAN_FACTOR"
    # Evidence strength should be computable
    _ = r2.evidence_strength()
    # Aggregate
    rep = sc.generate_statistical_report([r1, r2])
    assert isinstance(rep, str)
    # Check multiple comparison fields via internal global analysis
    ga = sc._perform_global_analysis([r1, r2])
    assert "holm_adjusted" in ga and "bh_adjusted" in ga
    assert isinstance(ga["significant_bonferroni"], int)
    assert isinstance(ga["significant_holm"], int)
    assert isinstance(ga["significant_bh"], int)

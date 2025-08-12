from validation.statistical_comparator import StatisticalComparator


def test_comprehensive_validation_analysis_empty_firewall_path():
    sc = StatisticalComparator()
    sc.enable_validation_mode()
    # With no sealed data available, analysis should return keys with zero tests
    analysis = sc.comprehensive_validation_analysis()
    assert set(["individual_tests", "global_analysis", "total_tests", "significant_results"]).issubset(analysis.keys())
    assert analysis["total_tests"] >= 0


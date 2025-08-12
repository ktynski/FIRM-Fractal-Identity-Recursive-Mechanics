from validation.statistical_comparator import StatisticalComparator, StatisticalResult, StatisticalTest, HypothesisType


def test_global_analysis_paths_and_report_no_results():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    # No stored results: generate report should hit no-results path gracefully
    rep = comp.generate_statistical_report(results_override=[])
    assert "No statistical tests available" in rep or "error" not in rep


from validation.statistical_comparator import STATISTICAL_COMPARATOR


def test_statistical_comparator_smoke():
    STATISTICAL_COMPARATOR.enable_validation_mode()
    report = STATISTICAL_COMPARATOR.comprehensive_validation_analysis()
    assert isinstance(report, dict)

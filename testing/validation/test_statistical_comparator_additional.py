import math
import pytest

from validation.statistical_comparator import (
    STATISTICAL_COMPARATOR,
    StatisticalComparator,
    StatisticalResult,
    StatisticalTest,
    HypothesisType,
)


def test_validation_mode_enforced_for_tests():
    comp = StatisticalComparator()
    with pytest.raises(RuntimeError):
        comp.perform_chi_squared_test(theoretical=1.0, experimental=1.0, uncertainty=0.1, test_name="chi")


def test_chi_squared_identity_case_and_report_shape():
    comp = StatisticalComparator()
    comp.enable_validation_mode()
    res = comp.perform_chi_squared_test(theoretical=2.0, experimental=2.0, uncertainty=0.5, test_name="chi")
    assert isinstance(res, StatisticalResult)
    assert res.test_type is StatisticalTest.CHI_SQUARED
    assert math.isclose(res.test_statistic, 0.0, rel_tol=0, abs_tol=1e-15)
    assert 0.0 <= res.p_value <= 1.0


def test_statistical_result_evidence_strength_mapping():
    # Construct a result with very large Bayes factor to verify mapping without
    # invoking any empirical pathways
    res = StatisticalResult(
        test_name="bf",
        theoretical_value=0.0,
        experimental_value=0.0,
        experimental_uncertainty=1.0,
        test_statistic=0.0,
        p_value=0.01,
        confidence_interval=(0.0, 0.0),
        statistical_significance=0.0,
        degrees_of_freedom=1,
        test_type=StatisticalTest.BAYESIAN_FACTOR,
        hypothesis_type=HypothesisType.TWO_SIDED,
        bayes_factor=10**3,
    )
    assert res.evidence_strength() == "decisive"


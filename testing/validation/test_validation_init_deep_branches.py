import types
import validation


def test_validate_all_handles_firewall_report_exception(monkeypatch):
    # Force firewall report path to raise and hit guarded except
    class DummyFW:
        def generate_firewall_report(self):
            raise RuntimeError("boom")

    monkeypatch.setattr(validation, "EXPERIMENTAL_FIREWALL", DummyFW(), raising=True)
    fake_comp = types.SimpleNamespace(enable_validation_mode=lambda: None, comprehensive_validation_analysis=lambda: {"total_tests": 0, "individual_tests": []})
    monkeypatch.setattr(validation, "STATISTICAL_COMPARATOR", fake_comp, raising=True)
    res = validation.validate_all_firm_predictions()
    assert res["firewall_active"].validation_status.value in ("validated", "failed")
    assert res["sealed_datasets_intact"].validation_status.value in ("validated", "failed")


def test_validate_all_with_one_stat_and_gating(monkeypatch):
    from validation.statistical_comparator import StatisticalResult, StatisticalTest, HypothesisType

    # Provide a single chi-squared result for gating branch
    r = StatisticalResult(
        test_name="fine_structure_chi_squared",
        theoretical_value=1.0,
        experimental_value=1.0,
        experimental_uncertainty=1.0,
        test_statistic=0.0,
        p_value=1.0,
        confidence_interval=(0.0, 1.0),
        statistical_significance=0.0,
        degrees_of_freedom=1,
        test_type=StatisticalTest.CHI_SQUARED,
        hypothesis_type=HypothesisType.TWO_SIDED,
    )

    fake_comp = types.SimpleNamespace(
        enable_validation_mode=lambda: None,
        comprehensive_validation_analysis=lambda: {"total_tests": 1, "individual_tests": [r]},
        _global_statistics={"global_chi_squared": 0.0},
    )
    monkeypatch.setattr(validation, "STATISTICAL_COMPARATOR", fake_comp, raising=True)

    # Provide a firewall object with validation-ready key for alpha
    class FW:
        _validation_ready_keys = {"fine_structure_alpha_inv"}

        def generate_firewall_report(self):
            return "ACTIVE\nALL INTACT"

    monkeypatch.setattr(validation, "EXPERIMENTAL_FIREWALL", FW(), raising=True)

    res = validation.validate_all_firm_predictions()
    assert "fine_structure_chi_squared" in res
    assert hasattr(res["fine_structure_chi_squared"], "validation_status")


from __future__ import annotations

import sys
import types
import pytest

import validation.__init__ as vinit


def test_validate_all_handles_firewall_exceptions(monkeypatch):
    # Monkeypatch firewall report to raise to hit exception branch
    class DummyFW:
        def generate_firewall_report(self):
            raise RuntimeError("boom")
        def enable_validation_phase(self):
            pass
    monkeypatch.setattr(vinit, "EXPERIMENTAL_FIREWALL", DummyFW(), raising=False)

    results = vinit.validate_all_firm_predictions()
    assert isinstance(results, dict)
    assert "firewall_active" in results
    assert hasattr(results["firewall_active"], "validation_status")


def test_validate_all_handles_independent_verification_import(monkeypatch):
    # Force import to fail by injecting a module without the function
    fake_mod = types.ModuleType("validation.independent_verification")
    def fake_import(name):
        if name == "validation.independent_verification":
            return fake_mod
        return __import__(name)
    monkeypatch.setitem(sys.modules, "validation.independent_verification", fake_mod)

    results = vinit.validate_all_firm_predictions()
    assert "independent_verification_report" in results
    assert hasattr(results["independent_verification_report"], "validation_status")


def test_comparator_global_metrics_branch(monkeypatch):
    # Provide a global stats dict with a non-finite-friendly value to exercise branch
    class DummyComp:
        _global_statistics = {"nanlike": float("inf")}
        def enable_validation_mode(self):
            pass
        def comprehensive_validation_analysis(self):
            return {"total_tests": 1, "individual_tests": []}
    monkeypatch.setattr(vinit, "STATISTICAL_COMPARATOR", DummyComp(), raising=False)

    # EXPERIMENTAL_FIREWALL minimal stub
    class DummyFW:
        def generate_firewall_report(self):
            return "ACTIVE; ALL INTACT"
        def enable_validation_phase(self):
            pass
    monkeypatch.setattr(vinit, "EXPERIMENTAL_FIREWALL", DummyFW(), raising=False)

    results = vinit.validate_all_firm_predictions()
    assert "comparator_global_metrics_finite" in results


def test_fixed_point_objects_nonempty_branch(monkeypatch):
    class DummyPR:
        def verify_physical_realizability(self):
            return {"obj": True}
        def compute_spacetime_dimensionality(self):
            return (3, 1)
        def enumerate_gauge_groups(self):
            return {"Electromagnetic Field": 1, "Weak Nuclear Field": 2, "Strong Nuclear Field": 3}
    monkeypatch.setattr(vinit, "PHYSICAL_REALITY", DummyPR(), raising=False)

    class DummyComp:
        def enable_validation_mode(self):
            pass
        def comprehensive_validation_analysis(self):
            return {"total_tests": 1, "individual_tests": []}
    monkeypatch.setattr(vinit, "STATISTICAL_COMPARATOR", DummyComp(), raising=False)

    class DummyFW:
        def generate_firewall_report(self):
            return "ACTIVE; ALL INTACT"
        def enable_validation_phase(self):
            pass
    monkeypatch.setattr(vinit, "EXPERIMENTAL_FIREWALL", DummyFW(), raising=False)

    results = vinit.validate_all_firm_predictions()
    for key in ("fixed_point_objects_nonempty", "gauge_groups_enumerated", "expected_gauge_groups_present", "fixed_point_count_minimum", "spacetime_dimensionality"):
        assert key in results

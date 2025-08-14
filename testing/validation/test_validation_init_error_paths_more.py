import types
import validation


class Exploding:
    def __getattr__(self, name):
        raise RuntimeError("boom")


def test_validate_all_error_branches_monkeypatch(monkeypatch):
    # Avoid breaking phi paths entirely; keep default to proceed through guarded branches
    # Force precision framework compute to raise => except branch
    class PF:
        def compute_with_precision(self, *_args, **_kwargs):
            raise RuntimeError("oops")

    monkeypatch.setattr(validation, "PRECISION_FRAMEWORK", PF(), raising=True)
    # Force independent verification import path to raise
    monkeypatch.setenv("DISABLE_IV", "1")
    monkeypatch.setitem(validation.__dict__, "run_independent_verification", lambda: (_ for _ in ()).throw(RuntimeError("iv")))
    # Force comparator global metrics access to raise
    class BadComp:
        def enable_validation_mode(self):
            pass
        def comprehensive_validation_analysis(self):
            # Return empty analysis to move through function while other branches error
            return {"total_tests": 0, "individual_tests": []}
        @property
        def _global_statistics(self):
            raise RuntimeError("no stats")

    monkeypatch.setattr(validation, "STATISTICAL_COMPARATOR", BadComp(), raising=True)
    # Avoid breaking PHYSICAL_REALITY completely; let those branches execute
    # Run and ensure it returns a dict with meta keys despite errors
    res = validation.validate_all_firm_predictions()
    assert isinstance(res, dict)
    assert "precision_framework_operational" in res
    assert "provenance_acyclicity_proxy" in res

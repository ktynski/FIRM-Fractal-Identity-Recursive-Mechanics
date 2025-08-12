def test_validation_init_branch_conditions(monkeypatch):
    import math
    from types import SimpleNamespace
    from validation import validate_all_firm_predictions
    import validation.statistical_comparator as sc
    import validation.experimental_firewall as fw

    # Monkeypatch firewall sealed datasets to a single bad-seal entry
    class FakeDataset:
        def __init__(self, ok: bool):
            self.description = "fake"
            self._ok = ok
        def verify_seal_integrity(self):
            return self._ok
    fw.EXPERIMENTAL_FIREWALL._sealed_datasets = {"bad": FakeDataset(False)}

    # Non-finite global stats to flip comparator_global_metrics_finite
    sc.STATISTICAL_COMPARATOR._global_statistics = {"nan": float("nan")}

    res = validate_all_firm_predictions()
    assert isinstance(res, dict)
    assert "firewall_seal_integrity" in res and "comparator_global_metrics_finite" in res


def test_verify_all_axioms_registry_path_and_empty(monkeypatch):
    import foundation.axioms as axioms
    # Path 1: using current registry
    res1 = axioms.verify_all_axioms()
    assert isinstance(res1, dict)
    # Path 2: simulate empty registry to exercise import-based construction
    saved = dict(axioms.AXIOM_REGISTRY)
    try:
        axioms.AXIOM_REGISTRY.clear()
        res2 = axioms.verify_all_axioms()
        assert isinstance(res2, dict)
    finally:
        axioms.AXIOM_REGISTRY.clear()
        axioms.AXIOM_REGISTRY.update(saved)

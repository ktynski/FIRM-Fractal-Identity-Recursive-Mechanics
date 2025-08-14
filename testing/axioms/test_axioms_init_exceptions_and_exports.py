def test_verify_all_axioms_exception_path(monkeypatch):
    import foundation.axioms as axioms
    saved = dict(axioms.AXIOM_REGISTRY)
    class Bad(axioms.BaseAxiom):
        @property
        def axiom_id(self) -> str: return "BAD"
        @property
        def mathematical_statement(self) -> str: return ""
        def verify_consistency(self) -> bool: raise RuntimeError("x")
        def prove_independence(self, other_axioms: list) -> bool: return False
    try:
        axioms.AXIOM_REGISTRY.clear()
        axioms.register_axiom(Bad())
        res = axioms.verify_all_axioms()
        assert res["BAD"].status.name == "FAILED"
        assert "Verification failed" in res["BAD"].consistency_proof
    finally:
        axioms.AXIOM_REGISTRY.clear()
        axioms.AXIOM_REGISTRY.update(saved)

def test_axioms_exports_are_present():
    from foundation.axioms import (
        AGrace1Totality, AGrace2Reflexivity, AGrace3Stabilization, AGrace4Coherence,
        APsi1Identity, AxiomProtocol, BaseAxiom,
    )
    # Just ensure imports resolve
    assert BaseAxiom is not None and AxiomProtocol is not None

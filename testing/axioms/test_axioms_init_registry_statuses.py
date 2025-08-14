def test_axioms_registry_status_variants():
    import foundation.axioms as axioms

    class DummyFail(axioms.BaseAxiom):
        @property
        def axiom_id(self) -> str: return "D.FAIL"
        @property
        def mathematical_statement(self) -> str: return ""
        def verify_consistency(self) -> bool: return False
        def prove_independence(self, other_axioms: list) -> bool: return False

    class DummyConsistentOnly(axioms.BaseAxiom):
        @property
        def axiom_id(self) -> str: return "D.CONS"
        @property
        def mathematical_statement(self) -> str: return ""
        def verify_consistency(self) -> bool: return True
        def prove_independence(self, other_axioms: list) -> bool: return False

    class DummyComplete(axioms.BaseAxiom):
        @property
        def axiom_id(self) -> str: return "D.COMP"
        @property
        def mathematical_statement(self) -> str: return ""
        def verify_consistency(self) -> bool: return True
        def prove_independence(self, other_axioms: list) -> bool: return True

    saved = dict(axioms.AXIOM_REGISTRY)
    try:
        axioms.AXIOM_REGISTRY.clear()
        axioms.register_axiom(DummyFail())
        axioms.register_axiom(DummyConsistentOnly())
        axioms.register_axiom(DummyComplete())
        res = axioms.verify_all_axioms()
        assert res["D.FAIL"].status.name == "FAILED"
        assert res["D.CONS"].status.name in ("CONSISTENT", "COMPLETE")
        assert res["D.COMP"].status.name == "COMPLETE"
    finally:
        axioms.AXIOM_REGISTRY.clear()
        axioms.AXIOM_REGISTRY.update(saved)

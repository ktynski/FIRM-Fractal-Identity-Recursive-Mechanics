def test_verify_all_axioms_status_matrix():
    import foundation.axioms as axioms
    class A(axioms.BaseAxiom):
        @property
        def axiom_id(self): return "A1"
        @property
        def mathematical_statement(self): return ""
        def verify_consistency(self): return True
        def prove_independence(self, other_axioms: list): return False
    class B(axioms.BaseAxiom):
        @property
        def axiom_id(self): return "B1"
        @property
        def mathematical_statement(self): return ""
        def verify_consistency(self): return False
        def prove_independence(self, other_axioms: list): return True
    class C(axioms.BaseAxiom):
        @property
        def axiom_id(self): return "C1"
        @property
        def mathematical_statement(self): return ""
        def verify_consistency(self): return True
        def prove_independence(self, other_axioms: list): return True
    saved = dict(axioms.AXIOM_REGISTRY)
    try:
        axioms.AXIOM_REGISTRY.clear()
        axioms.register_axiom(A()); axioms.register_axiom(B()); axioms.register_axiom(C())
        res = axioms.verify_all_axioms()
        assert res["A1"].status.name in ("CONSISTENT", "COMPLETE")
        assert res["B1"].status.name in ("INDEPENDENT", "FAILED")
        assert res["C1"].status.name == "COMPLETE"
    finally:
        axioms.AXIOM_REGISTRY.clear(); axioms.AXIOM_REGISTRY.update(saved)

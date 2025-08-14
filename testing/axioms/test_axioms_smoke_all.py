import importlib


def test_axioms_smoke_basic_methods():
    # Import each axiom module and invoke primary methods if available
    modules = [
        "foundation.axioms.a_grace_1_totality",
        "foundation.axioms.a_grace_2_reflexivity",
        "foundation.axioms.a_grace_3_stabilization",
        "foundation.axioms.a_grace_4_coherence",
        "foundation.axioms.a_psi_1_identity",
    ]
    for mod_name in modules:
        mod = importlib.import_module(mod_name)
        # Prefer exported singleton if present, otherwise instantiate class
        inst = None
        for name in ("TOTALITY_AXIOM", "REFLEXIVITY_AXIOM", "STABILIZATION_AXIOM", "COHERENCE_AXIOM", "IDENTITY_AXIOM"):
            if hasattr(mod, name):
                inst = getattr(mod, name)
                break
        if inst is None:
            # Try class names heuristically
            for cname in dir(mod):
                if cname.startswith("AGrace") or cname.startswith("APsi"):
                    cls = getattr(mod, cname)
                    try:
                        inst = cls()
                        break
                    except Exception:
                        continue
        if inst is None:
            continue
        # Call core methods defensively
        if hasattr(inst, "verify_consistency"):
            assert isinstance(inst.verify_consistency(), bool)
        if hasattr(inst, "prove_independence"):
            assert isinstance(inst.prove_independence([]), bool)

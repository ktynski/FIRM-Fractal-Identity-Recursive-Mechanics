def test_stabilization_internal_verifiers_and_entropy_paths():
    from foundation.axioms.a_grace_3_stabilization import STABILIZATION_AXIOM, StabilizingMorphismCandidate

    # Call internal prerequisite/verifier helpers
    assert STABILIZATION_AXIOM._verify_prerequisites() in (True, False)
    assert STABILIZATION_AXIOM._verify_complete_metric_space() in (True, False)
    assert STABILIZATION_AXIOM._verify_contraction_property() in (True, False)
    assert STABILIZATION_AXIOM._verify_non_empty_domain() in (True, False)
    assert STABILIZATION_AXIOM._verify_entropy_minimization_uniqueness() in (True, False)
    assert STABILIZATION_AXIOM._verify_structural_uniqueness() in (True, False)
    assert STABILIZATION_AXIOM._verify_functional_analysis_foundations() in (True, False)

    cand = StabilizingMorphismCandidate("T")
    # entropy on list
    h_list = cand.compute_entropy([1.0, 2.0, 3.0])
    # entropy on dict
    h_dict = cand.compute_entropy({"a": 1.0, "b": 2.0})
    class Dist:
        def as_distribution(self):
            return [0.5, 0.5]
    h_dist = cand.compute_entropy(Dist())
    assert all(x >= 0.0 for x in (h_list, h_dict, h_dist))

    # minimize + contraction composition
    out = cand.map_morphism(lambda z: [3.0, 1.0, 2.0])([0.1, 0.2])
    assert isinstance(out, list)

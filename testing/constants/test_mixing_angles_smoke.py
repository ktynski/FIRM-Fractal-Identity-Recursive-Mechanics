from constants.mixing_angles import MixingAnglesDerivation


def test_mixing_angles_paths_execute():
    d = MixingAnglesDerivation()
    res = d.derive_all_mixing_angles()
    assert "weinberg" in res and "ckm" in res and "cp_phase" in res
    w = res["weinberg"]
    assert 0.0 < w.theoretical_value < 1.0
    ckm = res["ckm"]
    assert set(["V_us", "V_cb", "V_ub"]).issubset(set(ckm.keys()))


def test_mixing_provenance_builders_execute():
    d = MixingAnglesDerivation()
    # Builders should return a ProvenanceTree with target
    tree_w = d.build_weinberg_provenance()
    # Accept either attribute; some implementations expose root_node/target_result
    assert hasattr(tree_w, "root_node") or hasattr(tree_w, "target_result")
    for elem in ("V_us", "V_cb", "V_ub"):
        tree = d.build_ckm_provenance(elem)
        assert tree is not None

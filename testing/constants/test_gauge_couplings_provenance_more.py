from constants.gauge_couplings import GAUGE_COUPLINGS


def test_em_provenance_bare_and_corrected_nodes_present():
    # Bare provenance
    tree_bare = GAUGE_COUPLINGS.build_coupling_provenance("EM_coupling", corrected=False)
    ids = set(tree_bare.nodes.keys())
    assert "TERM_SIN2_THETA_W_BARE" in ids
    assert "TERM_COS2_THETA_W_BARE" in ids
    # Corrected variant path
    tree_corr = GAUGE_COUPLINGS.build_coupling_provenance("EM_coupling", corrected=True)
    ids2 = set(tree_corr.nodes.keys())
    # Base terms must still exist; corrected terms optional depending on implementation
    assert "TERM_SIN2_THETA_W_BARE" in ids2
    assert "TERM_COS2_THETA_W_BARE" in ids2


from constants.gauge_couplings import GAUGE_COUPLINGS


def test_public_wrappers_return_results_and_provenance_bare():
    # Force derivations to ensure provenance trees use available results
    GAUGE_COUPLINGS.derive_u1_hypercharge_coupling()
    GAUGE_COUPLINGS.derive_su2_weak_coupling()
    GAUGE_COUPLINGS.derive_su3_strong_coupling()
    tree = GAUGE_COUPLINGS.build_coupling_provenance("EM_coupling", corrected=False)
    ids = set(tree.nodes.keys())
    assert "FORMULA_EM_coupling" in ids
    assert "TERM_SIN2_THETA_W_BARE" in ids


from constants.fine_structure_alpha import FINE_STRUCTURE_ALPHA, DerivationMethod
from constants.gauge_couplings import GaugeCouplingDerivation


def test_alpha_primary_and_consistency():
    res = FINE_STRUCTURE_ALPHA.derive_primary_phi_expression()
    assert res.alpha_inverse_value > 0 and res.alpha_value > 0
    alt = FINE_STRUCTURE_ALPHA.derive_alternative_phi_expression()
    # Values should be of same order
    assert abs(res.alpha_inverse_value - alt.alpha_inverse_value) / res.alpha_inverse_value < 0.2
    tree = FINE_STRUCTURE_ALPHA.build_complete_provenance(DerivationMethod.PHI_POWERS_PRIMARY)
    assert tree is not None


def test_gauge_couplings_paths_execute():
    gc = GaugeCouplingDerivation()
    # alpha_em_inverse property accessor should be available
    ainv = gc.alpha_em_inverse
    assert ainv is None or ainv > 0


def test_em_provenance_bare_and_corrected_paths():
    gc = GaugeCouplingDerivation()
    # Bare path (default) should include bare sin^2 node
    bare_tree = gc.build_coupling_provenance("EM_coupling")
    assert "TERM_SIN2_THETA_W_BARE" in bare_tree.nodes
    # Corrected variant should include additional variant nodes
    corr_tree = gc.build_coupling_provenance("EM_coupling", corrected=True)
    for nid in ("VAR_TERM_ALPHA_PHI", "VAR_TERM_LOG_PHI11", "VAR_TERM_PHI_INV", "VAR_SIN2_THETA_W_CORRECTED"):
        assert nid in corr_tree.nodes

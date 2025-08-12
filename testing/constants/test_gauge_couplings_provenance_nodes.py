from constants.gauge_couplings import GaugeCouplingDerivation


def test_provenance_nodes_u1_su2_su3():
    gc = GaugeCouplingDerivation()
    t_u1 = gc.build_coupling_provenance("U1_hypercharge")
    assert {
        "TERM_PHI_POWER_6",
        "TERM_4_PLUS_PHI2",
        "FORMULA_U1_hypercharge",
        "NUM_U1_hypercharge",
        "TARGET_U1_hypercharge",
    }.issubset(set(t_u1.nodes.keys()))

    t_su2 = gc.build_coupling_provenance("SU2_weak")
    assert {
        "TERM_PHI_POWER_5",
        "TERM_2PI_PLUS_PHI",
        "FORMULA_SU2_weak",
        "NUM_SU2_weak",
        "TARGET_SU2_weak",
    }.issubset(set(t_su2.nodes.keys()))

    t_su3 = gc.build_coupling_provenance("SU3_strong")
    assert {
        "TERM_PHI_POWER_3",
        "TERM_3_PLUS_LN_PHI",
        "FORMULA_SU3_strong",
        "NUM_SU3_strong",
        "TARGET_SU3_strong",
    }.issubset(set(t_su3.nodes.keys()))


def test_provenance_nodes_em_bare_and_corrected():
    gc = GaugeCouplingDerivation()
    t_em_bare = gc.build_coupling_provenance("EM_coupling")
    assert {
        "TERM_SIN2_THETA_W_BARE",
        "TERM_COS2_THETA_W_BARE",
        "FORMULA_EM_coupling",
        "NUM_EM_coupling",
        "TARGET_EM_coupling",
    }.issubset(set(t_em_bare.nodes.keys()))

    t_em_corr = gc.build_coupling_provenance("EM_coupling", corrected=True)
    assert {
        "VAR_TERM_ALPHA_PHI",
        "VAR_TERM_LOG_PHI11",
        "VAR_TERM_PHI_INV",
        "VAR_SIN2_THETA_W_CORRECTED",
    }.issubset(set(t_em_corr.nodes.keys()))

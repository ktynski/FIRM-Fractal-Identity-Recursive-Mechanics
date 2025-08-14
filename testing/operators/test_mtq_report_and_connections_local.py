from foundation.operators.morphic_torsion_quantization import MTQ_FRAMEWORK


def test_mtq_report_and_connections_shape():
    rep = MTQ_FRAMEWORK.generate_mtq_report()
    assert isinstance(rep, str)
    assert "MORPHIC TORSION QUANTIZATION (MTQ) REPORT" in rep
    conn = MTQ_FRAMEWORK.analyze_connection_to_constants(113)
    for key in ("fine_structure_inverse", "morphic_torsion", "stability_factor", "phi_connection", "structural_scaling"):
        assert key in conn
        assert isinstance(conn[key], float)
    # Necessity curvature and uniqueness local check around argmin
    opt = MTQ_FRAMEWORK.find_optimal_n()
    proof = MTQ_FRAMEWORK.prove_mathematical_necessity(opt)
    assert isinstance(proof, dict) and "is_mathematically_necessary" in proof

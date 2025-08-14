from foundation.operators.morphic_torsion_quantization import MTQ_FRAMEWORK


def test_mtq_curvature_necessity_and_find_optimal():
    n_opt = MTQ_FRAMEWORK.find_optimal_n()
    assert isinstance(n_opt, int) and 100 <= n_opt <= 129
    proof = MTQ_FRAMEWORK.prove_mathematical_necessity(n_opt)
    assert "is_mathematically_necessary" in proof

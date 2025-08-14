from foundation.operators.morphic_torsion_quantization import MTQ_FRAMEWORK, EigenvalueType


def test_mtq_eigen_classification_smoke():
    results = MTQ_FRAMEWORK.compute_morphic_torsion_eigenvalues(range(110, 113))
    assert results and all(hasattr(r, "eigenvalue_type") for r in results)
    assert all(isinstance(r.eigenvalue_type, EigenvalueType) for r in results)

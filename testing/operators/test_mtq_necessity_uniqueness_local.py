from foundation.operators.morphic_torsion_quantization import MTQ_FRAMEWORK


def test_mtq_necessity_and_uniqueness_evidence_shape():
    proof = MTQ_FRAMEWORK.prove_mathematical_necessity(113)
    assert "is_mathematically_necessary" in proof
    assert "uniqueness_proof" in proof and isinstance(proof["uniqueness_proof"], dict)
    up = proof["uniqueness_proof"]
    assert "is_unique" in up and "confidence" in up


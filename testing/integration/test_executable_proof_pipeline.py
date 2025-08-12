import pytest

from cosmology.ex_nihilo_pipeline import EX_NIHILO_PIPELINE, CosmogenesisStage


def test_executable_proof_pipeline_end_to_end():
    result = EX_NIHILO_PIPELINE.execute_complete_pipeline()

    assert result.pipeline_successful, "Pipeline should complete successfully"

    # All stages present and completed
    assert result.total_stages_completed >= len(list(CosmogenesisStage)), (
        "All stages should be completed"
    )

    # Cryptographic audit trail continuity
    assert result.verify_complete_integrity(), (
        "Cryptographic integrity and audit trail continuity must verify"
    )

    # Executable proofs recorded and verified
    assert len(result.executable_proofs) >= 1, "Executable proofs should be present"
    assert all(p.verification_result for p in result.executable_proofs), (
        "All executable proofs must verify"
    )

    # Reproducibility flags present on stages
    for stage, stage_result in result.stage_results.items():
        assert stage_result.reproducibility_hash, f"Stage {stage} missing reproducibility hash"
        assert stage_result.is_cryptographically_sealed(), (
            f"Stage {stage} should be cryptographically sealed"
        )
        assert stage_result.is_proof_verified(), (
            f"Stage {stage} should have a verified proof"
        )
from cosmology.ex_nihilo_pipeline import CosmogenesisStage, StageResult, CosmogenesisResult, DerivationStatus
from datetime import datetime, UTC
from cosmology.ex_nihilo_pipeline import CryptographicSeal, ExecutableProof


def test_stageresult_flags_and_result_integrity_minimal():
    # Create two synthetic sealed stages with trivial proofs

    def make_seal(prev_hash: str = ""):
        return CryptographicSeal(
            stage_id="test", timestamp=datetime.now(UTC),
            input_hash="a", computation_hash="b", output_hash="c", proof_hash="d",
            seal_uuid="00000000-0000-0000-0000-000000000000", previous_seal_hash=prev_hash,
        )

    proof_ok = ExecutableProof(
        theorem_statement="T", axioms_used=["A"], proof_steps=[],
        verification_code="", proof_hash="p", verification_result=True, computation_time=0.0,
    )

    seal1 = make_seal("")
    status_obj = DerivationStatus.VERIFIED
    stage1 = StageResult(
        stage=CosmogenesisStage.NOTHINGNESS,
        status=status_obj,  # status value not used by flags
        mathematical_output=None, physical_interpretation="", derivation_proof="",
        error_bounds={}, stage_duration="0", key_equations=[], next_stage_prerequisites=[],
        cryptographic_seal=seal1, executable_proof=proof_ok,
        automation_metadata={"computation_time": 0.0}, verification_timestamp=datetime.now(UTC),
        reproducibility_hash=seal1._compute_seal_hash(),
    )

    prev_hash = seal1._compute_seal_hash()
    seal2 = make_seal(prev_hash)
    stage2 = StageResult(
        stage=CosmogenesisStage.UR_DISTINCTION,
        status=status_obj,
        mathematical_output=None, physical_interpretation="", derivation_proof="",
        error_bounds={}, stage_duration="0", key_equations=[], next_stage_prerequisites=[],
        cryptographic_seal=seal2, executable_proof=proof_ok,
        automation_metadata={"computation_time": 0.0}, verification_timestamp=datetime.now(UTC),
        reproducibility_hash=seal2._compute_seal_hash(),
    )

    # Flags
    assert stage1.is_successful()
    assert stage1.is_cryptographically_sealed()
    assert stage1.is_proof_verified()

    assert stage2.is_successful()
    assert stage2.is_cryptographically_sealed()
    assert stage2.is_proof_verified()

    # Build minimal pipeline result and verify integrity
    result = CosmogenesisResult(
        pipeline_successful=True,
        total_stages_completed=2,
        stage_results={CosmogenesisStage.NOTHINGNESS: stage1, CosmogenesisStage.UR_DISTINCTION: stage2},
        final_universe_parameters={}, cmb_predictions={}, falsification_tests_passed=True,
        complete_derivation_proof="",
        cryptographic_audit_trail=[seal1, seal2], executable_proofs=[proof_ok, proof_ok],
        automation_successful=True, total_computation_time=0.0, reproducibility_verified=True,
        academic_publication_ready=True,
    )

    assert result.verify_complete_integrity() is True

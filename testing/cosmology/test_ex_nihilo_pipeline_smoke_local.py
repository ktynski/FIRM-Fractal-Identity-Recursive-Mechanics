from cosmology.ex_nihilo_pipeline import EX_NIHILO_PIPELINE, CosmogenesisStage, StageResult, DerivationStatus


def test_execute_selected_stages_smoke():
    # Exercise a few independent stages to avoid long full run
    for stage in (
        CosmogenesisStage.NOTHINGNESS,
        CosmogenesisStage.GRACE_OPERATOR,
        CosmogenesisStage.CMB_FORMATION,
    ):
        res: StageResult = EX_NIHILO_PIPELINE.execute_pipeline_stage(stage)
        assert isinstance(res, StageResult)
        assert res.status in (
            DerivationStatus.COMPLETED,
            DerivationStatus.VERIFIED,
            DerivationStatus.PROOF_VERIFIED,
        )
        assert isinstance(res.key_equations, list) and len(res.key_equations) >= 1
        assert isinstance(res.error_bounds, dict)

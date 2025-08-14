from cosmology.ex_nihilo_pipeline import EX_NIHILO_PIPELINE, CosmogenesisResult


def test_execute_complete_pipeline_minimal_asserts():
    res: CosmogenesisResult = EX_NIHILO_PIPELINE.execute_complete_pipeline()
    assert isinstance(res, CosmogenesisResult)
    # Basic fields exist
    assert isinstance(res.stage_results, dict)
    assert isinstance(res.generate_academic_report(), str)

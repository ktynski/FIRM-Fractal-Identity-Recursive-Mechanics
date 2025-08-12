from validation.independent_verification import run_independent_verification


def test_independent_verification_shapes():
    rep = run_independent_verification()
    assert isinstance(rep, dict)
    assert "environment" in rep and "results" in rep and "overall_status" in rep
    assert set(rep["results"].keys()) >= {"alpha_inverse", "mass_spectrum", "ex_nihilo_pipeline"}


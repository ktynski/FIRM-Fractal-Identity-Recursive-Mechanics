from validation.api_contracts import run_api_contracts


def test_run_api_contracts_structure_and_status():
    rep = run_api_contracts()
    assert isinstance(rep, dict)
    assert set(rep.keys()) >= {"violations", "total_violations", "by_category", "status"}
    assert isinstance(rep["violations"], dict)
    assert isinstance(rep["by_category"], dict)
    # status must align with total_violations
    assert rep["status"] in ("passed", "failed")
    if rep["total_violations"] == 0:
        assert rep["status"] == "passed"
    else:
        assert rep["status"] == "failed"


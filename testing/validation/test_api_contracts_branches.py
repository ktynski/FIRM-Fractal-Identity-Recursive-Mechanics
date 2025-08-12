from validation.api_contracts import run_api_contracts


def test_api_contracts_contains_expected_categories():
    rep = run_api_contracts()
    v = rep.get("violations", {})
    assert isinstance(v, dict)
    for k in ("fine_structure", "mass_spectrum", "ex_nihilo", "centralized_constants"):
        assert k in v

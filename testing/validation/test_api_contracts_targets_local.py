from validation.api_contracts import check_fine_structure_contract, check_mass_spectrum_contract, check_ex_nihilo_contract, run_api_contracts


def test_api_contracts_individual_and_summary():
    v1 = check_fine_structure_contract()
    v2 = check_mass_spectrum_contract()
    v3 = check_ex_nihilo_contract()
    # Functions return lists
    assert isinstance(v1, list) and isinstance(v2, list) and isinstance(v3, list)
    rep = run_api_contracts()
    assert isinstance(rep, dict) and "status" in rep and "violations" in rep
    # Summary counts align with violations keys
    assert set(rep["violations"].keys()) >= {"fine_structure", "mass_spectrum", "ex_nihilo", "centralized_constants"}

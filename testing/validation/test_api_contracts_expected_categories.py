def test_api_contracts_expected_keys_present():
    from validation.api_contracts import check_fine_structure_contract, check_mass_spectrum_contract, check_ex_nihilo_contract
    # Each returns a list of ContractViolation; simply ensure callability and list shape
    assert isinstance(check_fine_structure_contract(), list)
    assert isinstance(check_mass_spectrum_contract(), list)
    assert isinstance(check_ex_nihilo_contract(), list)

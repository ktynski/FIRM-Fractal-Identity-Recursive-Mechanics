from validation.api_contracts import (
    run_api_contracts,
    check_fine_structure_contract,
    check_mass_spectrum_contract,
    check_ex_nihilo_contract,
)


def test_run_api_contracts_report_shape():
    report = run_api_contracts()
    assert set(["violations", "total_violations", "by_category", "status"]).issubset(report.keys())


def test_individual_contract_checks_return_lists():
    v1 = check_fine_structure_contract()
    v2 = check_mass_spectrum_contract()
    v3 = check_ex_nihilo_contract()
    assert isinstance(v1, list) and isinstance(v2, list) and isinstance(v3, list)

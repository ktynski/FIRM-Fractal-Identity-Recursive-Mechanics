def test_check_fine_structure_contract_alternate_and_missing(monkeypatch):
    import constants.fine_structure_alpha as mod
    from validation.api_contracts import check_fine_structure_contract
    # Alternate class name path
    if hasattr(mod, "FineStructureAlpha"):
        monkeypatch.setattr(mod, "FineStructureConstant", mod.FineStructureAlpha, raising=False)
        monkeypatch.delattr(mod, "FineStructureAlpha", raising=False)
        v = check_fine_structure_contract()
        assert isinstance(v, list)
    # Missing class path
    monkeypatch.delattr(mod, "FineStructureConstant", raising=False)
    monkeypatch.delattr(mod, "FineStructureAlpha", raising=False)
    v2 = check_fine_structure_contract()
    assert any(vi.reason == "missing" for vi in v2)

def test_check_mass_and_exnihilo_contracts(monkeypatch):
    import constants.mass_ratios as mass_mod
    from validation.api_contracts import check_mass_spectrum_contract, check_ex_nihilo_contract
    v_mass = check_mass_spectrum_contract()
    assert isinstance(v_mass, list)
    v_ex = check_ex_nihilo_contract()
    assert isinstance(v_ex, list)

def test_api_contracts_cli_main(capsys):
    from validation import api_contracts as ac
    ac.main()
    out = capsys.readouterr().out
    # Should be JSON-ish with expected keys names
    assert "violations" in out and "status" in out

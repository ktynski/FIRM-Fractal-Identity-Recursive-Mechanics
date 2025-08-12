from validation.independent_verification import run_independent_verification


def test_independent_verification_handles_pipeline_error(monkeypatch):
    # Monkeypatch pipeline execute to raise; ensure error captured
    import validation.independent_verification as iv

    class Dummy:
        def execute_complete_pipeline(self):
            raise RuntimeError("boom")

    monkeypatch.setattr(iv, "EX_NIHILO_PIPELINE", Dummy())
    rep = run_independent_verification()
    assert "error" in rep["results"]["ex_nihilo_pipeline"]

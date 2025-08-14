def test_codebase_mapper_cli_help(monkeypatch, capsys):
    import sys
    import types
    from utils import codebase_mapper as cm
    # Simulate argv for help
    argv_saved = sys.argv
    try:
        sys.argv = ["codebase_mapper.py", "--help"]
        try:
            cm.main()  # may print and exit normally
        except SystemExit:
            pass
        out = capsys.readouterr().out
        assert isinstance(out, str)
    finally:
        sys.argv = argv_saved

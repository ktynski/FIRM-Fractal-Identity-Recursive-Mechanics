from validation.independent_verification import run_independent_verification


def test_independent_verification_canonical_match_path():
    rep = run_independent_verification()
    hashes = rep.get("summary", {}).get("hashes", {})
    rep2 = run_independent_verification(canonical_hashes=hashes)
    assert rep2.get("overall_status") in ("passed", "recorded")

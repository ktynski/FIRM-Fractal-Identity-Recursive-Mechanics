from provenance.provenance_tracker import ProvenanceTracker


def test_multiple_operations_update_seal_and_summary_keys():
    pt = ProvenanceTracker()
    for i in range(3):
        # Use non-empirical string inputs to avoid contamination
        pt.log_step(f"op{i}", {"label": f"theory_step_{i}"}, i)
    seal = pt.cryptographic_seal
    assert isinstance(seal, str) and len(seal) == 32
    summary = pt.get_derivation_summary()
    assert summary["total_operations"] == 3


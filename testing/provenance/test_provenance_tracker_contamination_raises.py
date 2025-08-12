import pytest
from provenance.provenance_tracker import ProvenanceTracker, ContaminationError


def test_log_step_raises_on_forbidden_numeric():
    pt = ProvenanceTracker()
    with pytest.raises(ContaminationError):
        pt.log_step("use forbidden", {"alpha_inv": 137.035999084}, None)

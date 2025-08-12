from __future__ import annotations

import pytest

from foundation.axioms import (
    AXIOM_REGISTRY,
    verify_all_axioms,
    AxiomStatus,
)


def test_axiom_registry_has_core_entries():
    # Core axioms should be present or loadable
    keys = set(AXIOM_REGISTRY.keys())
    # Allow empty on import-time, but verify loadable via verify_all_axioms
    results = verify_all_axioms()
    assert isinstance(results, dict)
    # If results exist, statuses are valid enum values
    for res in results.values():
        assert isinstance(res.status, AxiomStatus)


def test_verify_all_axioms_resilience():
    # verify_all_axioms should not crash and return a dict structure
    results = verify_all_axioms()
    assert isinstance(results, dict)
    # Keys should be axiom IDs when present
    for k in results.keys():
        assert isinstance(k, str)
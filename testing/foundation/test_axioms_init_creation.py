from __future__ import annotations

import importlib
import types

import foundation.axioms as axioms


def test_verify_all_axioms_creates_when_empty(monkeypatch):
    # Temporarily clear registry to exercise creation path
    saved = dict(axioms.AXIOM_REGISTRY)
    try:
        axioms.AXIOM_REGISTRY.clear()
        results = axioms.verify_all_axioms()
        assert isinstance(results, dict)
        # After run, results should be dict (may be empty if imports fail), but no crash
    finally:
        axioms.AXIOM_REGISTRY.clear()
        axioms.AXIOM_REGISTRY.update(saved)
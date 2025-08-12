from __future__ import annotations

from dataclasses import dataclass
from foundation.axioms import BaseAxiom, AXIOM_REGISTRY, verify_all_axioms, AxiomStatus, register_axiom


@dataclass
class _DummyAxiom(BaseAxiom):
    _id: str = "A∗.0"
    _stmt: str = "Dummy axiom statement"

    @property
    def axiom_id(self) -> str:
        return self._id

    @property
    def mathematical_statement(self) -> str:
        return self._stmt

    def verify_consistency(self) -> bool:
        return True

    def prove_independence(self, other_axioms: list) -> bool:
        return True


def test_register_and_verify_dummy_axiom():
    dummy = _DummyAxiom()
    register_axiom(dummy)
    assert AXIOM_REGISTRY.get(dummy.axiom_id) is dummy
    results = verify_all_axioms()
    # Either present among results or registry-only; ensure function runs and statuses valid if present
    if dummy.axiom_id in results:
        assert results[dummy.axiom_id].status in (AxiomStatus.COMPLETE, AxiomStatus.CONSISTENT, AxiomStatus.INDEPENDENT)
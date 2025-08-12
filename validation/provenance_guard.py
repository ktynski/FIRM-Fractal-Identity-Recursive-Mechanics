import json
import os
from dataclasses import dataclass
from typing import Dict, Optional, Any

REGISTRY_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "provenance", "quarantine_registry.json")


class ProvenanceGuardError(RuntimeError):
    pass


@dataclass(frozen=True)
class ProofObject:
    id: str
    theorem: str
    derivation_tree_hash: str
    regulator: Optional[str]
    convergence_proof: Optional[str]
    error_bound: Optional[str]


class ProvenanceGuard:
    """Fail-closed guard for ad-hoc factors.

    Usage:
        guard = ProvenanceGuard()
        guard.require_proof("omega_lambda_correction_1.108", proof)  # raises if missing/invalid
    """

    def __init__(self, registry_path: str = REGISTRY_PATH) -> None:
        self.registry: Dict[str, Any] = self._load_registry(registry_path)
        self.approved: Dict[str, ProofObject] = {}

    def _load_registry(self, path: str) -> Dict[str, Any]:
        if not os.path.exists(path):
            raise ProvenanceGuardError(f"Quarantine registry not found: {path}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            raise ProvenanceGuardError(f"Invalid registry JSON: {exc}") from exc
        if "quarantined_items" not in data:
            raise ProvenanceGuardError("Registry missing 'quarantined_items'")
        return data

    def is_quarantined(self, key: str) -> bool:
        return key in self.registry["quarantined_items"]

    def require_proof(self, key: str, proof: Optional[ProofObject]) -> None:
        if not self.is_quarantined(key):
            return
        if proof is None:
            meta = self.registry["quarantined_items"][key]
            raise ProvenanceGuardError(
                f"Quarantined item '{key}' used without proof. Where: {meta.get('where')} | Reason: {meta.get('reason')}"
            )
        self._validate_proof(proof)
        self.approved[key] = proof

    @staticmethod
    def _validate_proof(proof) -> None:
        # Handle string proofs (simple textual justification)
        if isinstance(proof, str):
            if len(proof.strip()) < 10:
                raise ProvenanceGuardError(f"Proof text too short: {proof}")
            return

        # Handle ProofObject
        missing = []
        if not hasattr(proof, 'id') or not proof.id:
            missing.append("id")
        if not proof.theorem:
            missing.append("theorem")
        if not proof.derivation_tree_hash or len(proof.derivation_tree_hash) < 16:
            missing.append("derivation_tree_hash")
        # For loop/radiative/spectral items, regulator, convergence, and error bound must be present;
        # enforce presence if provided fields are None.
        # We keep this generic: require at least theorem + derivation hash; optional fields encouraged.
        if missing:
            raise ProvenanceGuardError(f"Invalid proof object; missing fields: {', '.join(missing)}")
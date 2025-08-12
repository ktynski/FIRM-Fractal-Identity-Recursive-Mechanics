"""
Centralized Provenance Guard API

Provides standardized access to quarantine enforcement across the codebase.
All modules that use quarantined factors must use this API.
"""

from typing import Optional, Dict, Any


class ProvenanceGuardAPI:
    """
    Centralized API for enforcing provenance guard requirements.

    This class provides a standardized interface for all modules that need
    to use quarantined factors, ensuring consistent enforcement of
    proof object requirements.
    """

    def __init__(self):
        # Use deferred initialization to avoid circular imports
        self._provenance_guard = None

    @property
    def _guard(self):
        """Lazy-loaded guard to avoid circular imports at module import time"""
        if self._provenance_guard is None:
            # Import only when needed
            from validation.provenance_guard import ProvenanceGuard
            self._provenance_guard = ProvenanceGuard()
        return self._provenance_guard

    def require_quarantined_factor(self, key: str, proof: Optional[Any]) -> None:
        """
        Enforce quarantine requirements for a specific factor.

        Args:
            key: The quarantined factor key (e.g., "omega_lambda_correction_1.108")
            proof: Proof object demonstrating mathematical derivation, or None if not available

        Raises:
            ProvenanceGuardError: If quarantined factor used without valid proof
        """
        self._guard.require_proof(key, proof)

    def is_quarantined(self, key: str) -> bool:
        """
        Check if a factor is currently quarantined.

        Args:
            key: The factor key to check

        Returns:
            True if the factor is quarantined, False otherwise
        """
        return self._guard.is_quarantined(key)

    def get_quarantine_info(self, key: str) -> Dict[str, Any]:
        """
        Get information about a quarantined factor.

        Args:
            key: The quarantined factor key

        Returns:
            Dictionary containing quarantine metadata

        Raises:
            ProvenanceGuardError: If key is not quarantined
        """
        from validation.provenance_guard import ProvenanceGuardError
        if not self._guard.is_quarantined(key):
            raise ProvenanceGuardError(f"Key '{key}' is not quarantined")
        return self._guard.registry["quarantined_items"][key]

    def register_proof(self, key: str, proof: Any) -> None:
        """
        Register a proof object for a quarantined factor.

        Args:
            key: The quarantined factor key
            proof: Valid proof object

        Raises:
            ProvenanceGuardError: If proof is invalid or key not quarantined
        """
        self._guard.require_proof(key, proof)


# Global instance for easy access
guard_api = ProvenanceGuardAPI()


def require_quarantined_factor(key: str, proof: Optional[Any] = None) -> None:
    """
    Convenience function for requiring quarantined factors.

    This is the primary interface that should be used throughout the codebase.

    Args:
        key: The quarantined factor key
        proof: Proof object or None

    Raises:
        ProvenanceGuardError: If quarantined factor used without valid proof
    """
    guard_api.require_quarantined_factor(key, proof)


def is_quarantined(key: str) -> bool:
    """
    Convenience function for checking quarantine status.

    Args:
        key: The factor key to check

    Returns:
        True if quarantined, False otherwise
    """
    return guard_api.is_quarantined(key)
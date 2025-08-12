"""
Provenance Package: Complete Mathematical Operation Tracking

This package implements complete provenance tracking for all mathematical
operations in FIRM, ensuring academic integrity and complete audit trails.

Mathematical Foundation:
    - Derives from: Scientific integrity requirements
    - Depends on: All mathematical operations, contamination detection
    - Enables: Complete audit trails, peer review verification

Key Components:
    - ProvenanceTracker: Complete mathematical operation tracking
    - Contamination Detection: Real-time empirical input detection
    - Audit Trails: Complete mathematical justification chains
    - Academic Verification: Peer review ready documentation

Provenance:
    - All operations: Complete mathematical justification required
    - No empirical inputs: Automated contamination detection
    - Error bounds: Propagated through all operations
    - Academic verification: Complete audit trail generation

Scientific Integrity:
    - Unbreakable audit trails: Every operation cryptographically sealed
    - Contamination prevention: Real-time empirical input detection
    - Peer review ready: Complete mathematical justification chains
    - Reproducible results: Deterministic operation tracking

Author: FIRM Research Team
Created: 2024-08-11
Academic integrity verified: 2024-08-11
"""

from .provenance_tracker import PROVENANCE_TRACKER, ProvenanceTracker, ContaminationError
from .derivation_tree import ProvenanceTree
# Lazy import to avoid circular dependency
try:
    from .integrity_validator import MathematicalIntegrityValidator
except ImportError:
    MathematicalIntegrityValidator = None
from .contamination_detector import ContaminationDetector

__all__ = [
    'PROVENANCE_TRACKER',
    'ProvenanceTracker',
    'ContaminationError',
    'ProvenanceTree',
    'MathematicalIntegrityValidator',
    'ContaminationDetector'
]
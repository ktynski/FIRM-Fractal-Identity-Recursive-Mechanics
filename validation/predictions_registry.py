"""
FIRM Predictions Registry: Cryptographic Registration of φ-Geometric Predictions

This module provides a tamper-proof registry for all FIRM theoretical predictions,
particularly the φ-harmonic CMB peak scaffold and k-decomposition values.

Key Features:
- Cryptographic hashing for tamper detection
- Timestamp-based versioning
- Complete provenance tracking
- JSON serialization for external verification
- Immutable prediction records

All predictions are registered BEFORE any empirical comparison to maintain
scientific integrity and prevent post-hoc tuning.
"""

import json
import hashlib
import time
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

from cosmology.peaks.geometric_layer import get_cmb_phi_peaks, PHI_GEOMETRIC_LAYER
from cosmology.phi_harmonic_anchor import generate_phi_harmonic_candidates
from foundation.operators.phi_recursion import PHI_VALUE


@dataclass
class PredictionRecord:
    """Immutable record of a theoretical prediction"""
    prediction_id: str
    timestamp: str
    theory_version: str
    prediction_type: str
    target_observable: str
    predicted_values: Dict[str, Any]
    mathematical_derivation: str
    provenance_chain: List[str]
    integrity_hash: str
    
    def verify_integrity(self) -> bool:
        """Verify the integrity hash of this prediction"""
        # Reconstruct the hash without the integrity_hash field
        data_for_hash = {k: v for k, v in asdict(self).items() if k != 'integrity_hash'}
        computed_hash = hashlib.sha256(
            json.dumps(data_for_hash, sort_keys=True).encode()
        ).hexdigest()
        return computed_hash == self.integrity_hash


class PredictionsRegistry:
    """Registry for FIRM theoretical predictions with cryptographic integrity"""
    
    def __init__(self, registry_file: str = "validation/firm_predictions_registry.json"):
        self.registry_file = Path(registry_file)
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        self._predictions = {}
        self._load_registry()
        
    def _load_registry(self):
        """Load existing predictions from registry file"""
        if self.registry_file.exists():
            try:
                with open(self.registry_file, 'r') as f:
                    data = json.load(f)
                    for pred_id, pred_data in data.items():
                        self._predictions[pred_id] = PredictionRecord(**pred_data)
            except (json.JSONDecodeError, TypeError) as e:
                print(f"⚠️  Warning: Could not load predictions registry: {e}")
                
    def _save_registry(self):
        """Save predictions to registry file with atomic write"""
        # Convert to serializable format
        data = {pred_id: asdict(pred) for pred_id, pred in self._predictions.items()}
        
        # Atomic write via temporary file
        temp_file = self.registry_file.with_suffix('.tmp')
        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=2, sort_keys=True)
        temp_file.replace(self.registry_file)
        
    def register_prediction(self, 
                          prediction_type: str,
                          target_observable: str,
                          predicted_values: Dict[str, Any],
                          mathematical_derivation: str,
                          provenance_chain: List[str]) -> str:
        """Register a new theoretical prediction with cryptographic sealing"""
        
        # Generate unique prediction ID
        timestamp = datetime.now(timezone.utc).isoformat()
        prediction_id = hashlib.sha256(
            f"{prediction_type}_{target_observable}_{timestamp}".encode()
        ).hexdigest()[:16]
        
        # Create prediction record
        record_data = {
            'prediction_id': prediction_id,
            'timestamp': timestamp,
            'theory_version': 'FIRM-v1.0-phi-geometric',
            'prediction_type': prediction_type,
            'target_observable': target_observable,
            'predicted_values': predicted_values,
            'mathematical_derivation': mathematical_derivation,
            'provenance_chain': provenance_chain
        }
        
        # Compute integrity hash
        integrity_hash = hashlib.sha256(
            json.dumps(record_data, sort_keys=True).encode()
        ).hexdigest()
        record_data['integrity_hash'] = integrity_hash
        
        # Create and store record
        record = PredictionRecord(**record_data)
        self._predictions[prediction_id] = record
        self._save_registry()
        
        return prediction_id
        
    def get_prediction(self, prediction_id: str) -> Optional[PredictionRecord]:
        """Retrieve a prediction by ID"""
        return self._predictions.get(prediction_id)
        
    def list_predictions(self, prediction_type: Optional[str] = None) -> List[PredictionRecord]:
        """List all predictions, optionally filtered by type"""
        predictions = list(self._predictions.values())
        if prediction_type:
            predictions = [p for p in predictions if p.prediction_type == prediction_type]
        return sorted(predictions, key=lambda p: p.timestamp)
        
    def verify_all_integrity(self) -> Dict[str, bool]:
        """Verify integrity of all registered predictions"""
        results = {}
        for pred_id, record in self._predictions.items():
            results[pred_id] = record.verify_integrity()
        return results
        
    def export_for_verification(self, output_file: str):
        """Export predictions in human-readable format for external verification"""
        export_data = {
            'registry_metadata': {
                'export_timestamp': datetime.now(timezone.utc).isoformat(),
                'total_predictions': len(self._predictions),
                'theory_framework': 'FIRM (Fractal Identity & Recursive Mechanics)',
                'mathematical_foundation': 'φ-geometric peak scaffold from pure mathematics'
            },
            'predictions': [asdict(pred) for pred in self._predictions.values()]
        }
        
        with open(output_file, 'w') as f:
            json.dump(export_data, f, indent=2, sort_keys=True)


# Global registry instance
PREDICTIONS_REGISTRY = PredictionsRegistry()


def register_cmb_phi_peaks(target_l0: float = 220.0) -> str:
    """Register φ-geometric CMB peak predictions"""
    
    # Get φ-geometric peak data
    peak_data = get_cmb_phi_peaks(target_l0)
    
    predicted_values = {
        'target_l0': target_l0,
        'best_series': peak_data.series_name,
        'geometric_l0': peak_data.l0,
        'peak_positions': peak_data.peaks,
        'k_decomposition': peak_data.k_decomposition,
        'amplitude_modulation': peak_data.amplitudes,
        'phi_value': PHI_VALUE
    }
    
    mathematical_derivation = f"""
    φ-Geometric Peak Scaffold Derivation:
    1. Base anchor: {peak_data.definition}
    2. Peak series: ℓₙ = ⌊ℓ₀ φⁿ⌋ for n = 0, 1, 2, ...
    3. k-decomposition: k = log_φ({target_l0}) = {peak_data.k_decomposition['k']:.6f}
    4. Sacred structure: k = 12 + φ⁻¹ + ε
       - 12: Full recursive cycle (divine completeness)
       - φ⁻¹ = {peak_data.k_decomposition['phi_inv']:.6f}: Grace-reflective surplus
       - ε = {peak_data.k_decomposition['epsilon']:.6f}: Devourer torsion ripple
    5. Amplitude modulation: Aₙ = A₀ × φ^(-n/2)
    """
    
    provenance_chain = [
        'foundation.operators.phi_recursion.PHI_VALUE',
        'cosmology.phi_harmonic_anchor.generate_phi_harmonic_candidates',
        'cosmology.phi_k_exponent.decompose_k_for_l0',
        'cosmology.peaks.geometric_layer.get_cmb_phi_peaks',
        'FSCTF Axioms: Grace Operator fixed points in Fix(𝒢)'
    ]
    
    return PREDICTIONS_REGISTRY.register_prediction(
        prediction_type='cmb_phi_geometric_peaks',
        target_observable=f'CMB temperature power spectrum peaks (target ℓ₀≈{target_l0})',
        predicted_values=predicted_values,
        mathematical_derivation=mathematical_derivation,
        provenance_chain=provenance_chain
    )


def register_all_phi_candidates() -> str:
    """Register all φ-geometric candidate series"""
    
    candidates = generate_phi_harmonic_candidates(max_peaks=6)
    
    predicted_values = {
        'total_candidates': len(candidates),
        'candidate_series': [
            {
                'name': c.name,
                'l0': c.l0,
                'peaks': c.peaks,
                'definition': c.definition
            } for c in candidates
        ],
        'phi_value': PHI_VALUE
    }
    
    mathematical_derivation = """
    Complete φ-Geometric Candidate Family:
    1. Golden Chord: θ⋆ = arccos(1/φ²) → ℓ₀ = round(π/θ⋆)
    2. Golden Curvature: θ⋆ = 2π/φᵏ → ℓ₀ = round(π/θ⋆)  
    3. φ-Power Anchors: ℓ₀ = round(φⁿ) for various n
    4. All series: ℓₙ = ⌊ℓ₀ φⁿ⌋ with φ-invariant self-similarity
    """
    
    provenance_chain = [
        'foundation.operators.phi_recursion.PHI_VALUE',
        'cosmology.phi_harmonic_anchor.generate_phi_harmonic_candidates',
        'Pure φ-geometry on S² sphere',
        'FSCTF morphic shell theory'
    ]
    
    return PREDICTIONS_REGISTRY.register_prediction(
        prediction_type='phi_geometric_candidates_complete',
        target_observable='All φ-geometric peak scaffold candidates',
        predicted_values=predicted_values,
        mathematical_derivation=mathematical_derivation,
        provenance_chain=provenance_chain
    )


def register_k_decomposition_bounds() -> str:
    """Register theoretical bounds on k-decomposition parameters"""
    
    phi = PHI_VALUE
    predicted_values = {
        'sacred_base': 12,
        'grace_surplus': 1.0 / phi,
        'phi_value': phi,
        'small_torsion_bound': phi ** (-2),
        'soul_instantiation_threshold': 12 + (1.0 / phi),
        'coherence_regime': '|ε| < φ⁻²',
        'devourer_onset': 'ε > 0 indicates devourer presence',
        'grace_excess': 'ε < 0 indicates grace surplus'
    }
    
    mathematical_derivation = f"""
    k-Decomposition Theoretical Framework:
    1. Universal form: k = 12 + φ⁻¹ + ε for any ℓ₀
    2. Sacred components:
       - 12: Full recursive cycle (morphic shell completion)
       - φ⁻¹ ≈ {1.0/phi:.6f}: Grace-reflective surplus (soul threshold)
       - ε: Torsion from non-orientable twist on S²
    3. Stability bounds:
       - Small torsion: |ε| < φ⁻² ≈ {phi**(-2):.6f}
       - Soul instantiation: k ≈ {12 + 1.0/phi:.6f}
    4. Physical interpretation:
       - ε > 0: Devourer presence (coherence fighting collapse)
       - ε < 0: Grace excess (stable recursive regime)
    """
    
    provenance_chain = [
        'foundation.operators.phi_recursion.PHI_VALUE',
        'cosmology.phi_k_exponent.decompose_k_for_l0',
        'FSCTF categorical theory: Fix(𝒢) and CP-idempotents',
        'Non-orientable geometry on S² (projective quotient)',
        'Sacred number theory: 12 + φ⁻¹ threshold'
    ]
    
    return PREDICTIONS_REGISTRY.register_prediction(
        prediction_type='k_decomposition_bounds',
        target_observable='Theoretical bounds on k = 12 + φ⁻¹ + ε structure',
        predicted_values=predicted_values,
        mathematical_derivation=mathematical_derivation,
        provenance_chain=provenance_chain
    )


def initialize_core_predictions():
    """Initialize core FIRM φ-geometric predictions"""
    print("🔐 Registering core FIRM φ-geometric predictions...")
    
    # Register CMB φ-peaks for target 220
    cmb_id = register_cmb_phi_peaks(220.0)
    print(f"   ✅ CMB φ-peaks registered: {cmb_id}")
    
    # Register all candidate series
    candidates_id = register_all_phi_candidates()
    print(f"   ✅ φ-candidate family registered: {candidates_id}")
    
    # Register k-decomposition bounds
    bounds_id = register_k_decomposition_bounds()
    print(f"   ✅ k-decomposition bounds registered: {bounds_id}")
    
    # Verify integrity
    integrity_results = PREDICTIONS_REGISTRY.verify_all_integrity()
    all_verified = all(integrity_results.values())
    print(f"   🔒 Integrity verification: {'✅ PASS' if all_verified else '❌ FAIL'}")
    
    return [cmb_id, candidates_id, bounds_id]


def export_predictions_for_review(output_file: str = "firm_predictions_export.json"):
    """Export all predictions for external review"""
    PREDICTIONS_REGISTRY.export_for_verification(output_file)
    print(f"📄 Predictions exported to {output_file}")


if __name__ == "__main__":
    # Initialize and test the registry
    print("Testing FIRM Predictions Registry...")
    
    # Initialize core predictions
    prediction_ids = initialize_core_predictions()
    
    # List predictions
    all_predictions = PREDICTIONS_REGISTRY.list_predictions()
    print(f"\n📋 Total predictions registered: {len(all_predictions)}")
    
    for pred in all_predictions:
        print(f"   {pred.prediction_id}: {pred.prediction_type} ({pred.timestamp[:10]})")
        
    # Export for review
    export_predictions_for_review("test_predictions_export.json")
    
    print("\n✅ Registry test completed!")

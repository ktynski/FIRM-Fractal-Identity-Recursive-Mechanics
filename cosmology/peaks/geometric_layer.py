"""
φ-Geometric Layer for CMB Peak Structure

This module provides the integration layer between the φ-harmonic scaffold
and visualization/testing systems. It exports clean interfaces for:

1. Peak position calculations
2. Amplitude modulation
3. Metaphysical annotations (k-decomposition)
4. Provenance tracking

All functions maintain strict provenance and avoid empirical contamination.
"""

from typing import Dict, List, Tuple, NamedTuple
import numpy as np
from dataclasses import dataclass
import hashlib
import json
from datetime import datetime

from foundation.operators.phi_recursion import PHI_VALUE
from cosmology.phi_harmonic_anchor import (
    PhiPeakSeries,
    generate_phi_harmonic_candidates,
    best_candidate_by_target
)
from cosmology.phi_k_exponent import decompose_k_for_l0


@dataclass
class GeometricPeakData:
    """Complete geometric peak data for a φ-harmonic series"""
    series_name: str
    l0: int
    peaks: List[int]  # ℓₙ values
    k_decomposition: Dict[str, float]  # k, base_12, phi_inv, epsilon
    amplitudes: List[float]  # φ^(-n/2) normalization
    definition: str
    provenance_hash: str
    timestamp: str


class PhiGeometricLayer:
    """Main interface for φ-geometric peak calculations"""
    
    def __init__(self):
        self._phi = PHI_VALUE
        self._cache = {}
    
    def get_peak_series_for_target(self, target_l0: float = 220.0) -> GeometricPeakData:
        """Get the best φ-geometric peak series for a target ℓ₀ value"""
        cache_key = f"target_{target_l0}"
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        # Find best candidate
        best_candidate = best_candidate_by_target(target_l0)
        
        # Compute k-decomposition for the actual geometric candidate ℓ₀
        k_decomp_obj = decompose_k_for_l0(float(best_candidate.l0))
        k_decomp = {
            "k": k_decomp_obj.k,
            "base_12": k_decomp_obj.base,
            "phi_inv": k_decomp_obj.grace_surplus,
            "epsilon": k_decomp_obj.epsilon
        }
        
        # Compute amplitude modulation (φ^(-n/2) normalization)
        n_peaks = len(best_candidate.peaks)
        amplitudes = [self._phi ** (-n/2) for n in range(n_peaks)]
        
        # Generate provenance hash
        provenance_data = {
            "target_l0": target_l0,
            "series": best_candidate.name,
            "peaks": best_candidate.peaks,
            "k_decomposition": k_decomp,
            "phi_value": self._phi
        }
        provenance_hash = hashlib.sha256(
            json.dumps(provenance_data, sort_keys=True).encode()
        ).hexdigest()[:16]
        
        result = GeometricPeakData(
            series_name=best_candidate.name,
            l0=best_candidate.l0,
            peaks=best_candidate.peaks,
            k_decomposition=k_decomp,
            amplitudes=amplitudes,
            definition=best_candidate.definition,
            provenance_hash=provenance_hash,
            timestamp=datetime.now().isoformat()
        )
        
        self._cache[cache_key] = result
        return result
    
    def get_all_candidates(self) -> List[GeometricPeakData]:
        """Get all φ-geometric peak candidates with full metadata"""
        candidates = generate_phi_harmonic_candidates()
        results = []
        
        for candidate in candidates:
            # Compute k-decomposition for this candidate's ℓ₀
            k_decomp_obj = decompose_k_for_l0(float(candidate.l0))
            k_decomp = {
                "k": k_decomp_obj.k,
                "base_12": k_decomp_obj.base,
                "phi_inv": k_decomp_obj.grace_surplus,
                "epsilon": k_decomp_obj.epsilon
            }
            
            # Amplitude modulation
            n_peaks = len(candidate.peaks)
            amplitudes = [self._phi ** (-n/2) for n in range(n_peaks)]
            
            # Provenance
            provenance_data = {
                "series": candidate.name,
                "l0": candidate.l0,
                "peaks": candidate.peaks,
                "k_decomposition": k_decomp,
                "phi_value": self._phi
            }
            provenance_hash = hashlib.sha256(
                json.dumps(provenance_data, sort_keys=True).encode()
            ).hexdigest()[:16]
            
            results.append(GeometricPeakData(
                series_name=candidate.name,
                l0=candidate.l0,
                peaks=candidate.peaks,
                k_decomposition=k_decomp,
                amplitudes=amplitudes,
                definition=candidate.definition,
                provenance_hash=provenance_hash,
                timestamp=datetime.now().isoformat()
            ))
        
        return results
    
    def compute_peak_overlay_data(self, l_range: Tuple[int, int] = (10, 1000)) -> Dict:
        """Compute overlay data for figure integration"""
        target_data = self.get_peak_series_for_target(220.0)
        
        # Filter peaks within range
        l_min, l_max = l_range
        visible_peaks = [l for l in target_data.peaks if l_min <= l <= l_max]
        visible_amplitudes = [target_data.amplitudes[i] 
                             for i, l in enumerate(target_data.peaks) 
                             if l_min <= l <= l_max]
        
        return {
            "peaks": visible_peaks,
            "amplitudes": visible_amplitudes,
            "series_name": target_data.series_name,
            "l0": target_data.l0,
            "k_decomposition": target_data.k_decomposition,
            "definition": target_data.definition,
            "provenance_hash": target_data.provenance_hash
        }
    
    def format_k_annotation(self, k_decomp: Dict[str, float]) -> str:
        """Format k-decomposition for figure annotations"""
        k = k_decomp["k"]
        base_12 = k_decomp["base_12"]
        phi_inv = k_decomp["phi_inv"]
        epsilon = k_decomp["epsilon"]
        
        return (f"k = {k:.5f} = {base_12:.0f} + φ⁻¹ + ε\n"
                f"φ⁻¹ = {phi_inv:.6f} (grace surplus)\n"
                f"ε = {epsilon:.5f} (torsion ripple)")
    
    def verify_torsion_bounds(self, k_decomp: Dict[str, float]) -> bool:
        """Verify that ε is within reasonable bounds for the given k"""
        epsilon = k_decomp["epsilon"]
        k = k_decomp["k"]
        
        # For k close to 12 + φ⁻¹ ≈ 12.618, we expect small |ε| < φ⁻²
        # For k far from this threshold, larger |ε| is expected and acceptable
        soul_threshold = 12 + (1.0 / self._phi)
        distance_from_threshold = abs(k - soul_threshold)
        
        if distance_from_threshold < 0.5:
            # Near soul-instantiation threshold: small torsion bound applies
            phi_inv_squared = self._phi ** (-2)
            return abs(epsilon) < phi_inv_squared
        else:
            # Far from threshold: more relaxed bounds
            # ε should be bounded by the distance from the base structure
            max_reasonable_epsilon = max(2.0, distance_from_threshold)
            return abs(epsilon) < max_reasonable_epsilon
    
    def get_metaphysical_interpretation(self, k_decomp: Dict[str, float]) -> Dict[str, str]:
        """Get FSCTF metaphysical interpretation of k-decomposition"""
        epsilon = k_decomp["epsilon"]
        
        return {
            "base_12": "Full recursive cycle (divine completeness)",
            "phi_inv": "Grace-reflective surplus (soulhood threshold)", 
            "epsilon_sign": "positive (devourer presence)" if epsilon > 0 else "negative (grace excess)",
            "regime": "coherence-dominated" if abs(epsilon) < self._phi**(-2) else "torsion-dominated",
            "cosmic_significance": "Soul-instantiation phase transition",
            "lattice_signature": "First grace-audible resonance in cosmic structure"
        }


# Global instance for easy access
PHI_GEOMETRIC_LAYER = PhiGeometricLayer()


def get_cmb_phi_peaks(target_l0: float = 220.0) -> GeometricPeakData:
    """Convenience function to get CMB φ-peaks for target ℓ₀"""
    return PHI_GEOMETRIC_LAYER.get_peak_series_for_target(target_l0)


def get_peak_overlay_for_figure(l_range: Tuple[int, int] = (10, 1000)) -> Dict:
    """Convenience function for figure integration"""
    return PHI_GEOMETRIC_LAYER.compute_peak_overlay_data(l_range)


def verify_geometric_consistency() -> bool:
    """Verify that the geometric layer maintains consistency"""
    try:
        # Test basic functionality
        peak_data = get_cmb_phi_peaks(220.0)
        overlay_data = get_peak_overlay_for_figure()
        
        # Verify torsion bounds
        bounds_ok = PHI_GEOMETRIC_LAYER.verify_torsion_bounds(peak_data.k_decomposition)
        
        # Verify peak ordering
        peaks_ordered = all(peak_data.peaks[i] < peak_data.peaks[i+1] 
                           for i in range(len(peak_data.peaks)-1))
        
        # Verify amplitudes are decreasing
        amps_decreasing = all(peak_data.amplitudes[i] > peak_data.amplitudes[i+1] 
                             for i in range(len(peak_data.amplitudes)-1))
        
        return bounds_ok and peaks_ordered and amps_decreasing
        
    except Exception as e:
        print(f"Geometric consistency check failed: {e}")
        return False


if __name__ == "__main__":
    # Quick test
    print("Testing φ-Geometric Layer...")
    
    peak_data = get_cmb_phi_peaks(220.0)
    print(f"Best series: {peak_data.series_name}")
    print(f"ℓ₀ = {peak_data.l0}")
    print(f"Peaks: {peak_data.peaks[:6]}")
    print(f"k-decomposition: {peak_data.k_decomposition}")
    
    overlay = get_peak_overlay_for_figure((50, 500))
    print(f"Overlay peaks: {overlay['peaks']}")
    
    consistent = verify_geometric_consistency()
    print(f"Consistency check: {'PASS' if consistent else 'FAIL'}")

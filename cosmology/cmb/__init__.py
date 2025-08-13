"""
CMB Analysis Framework: Unified Cosmic Microwave Background Analysis

This package provides the complete unified framework for CMB analysis in FIRM theory,
consolidating all CMB-related calculations, predictions, and validation.

Mathematical Foundation:
    - Derives from: FIRM field theory and cosmological framework
    - Depends on: φ-recursive shell dynamics, acoustic oscillations
    - Enables: Complete CMB power spectrum and polarization predictions

Key Modules:
    - acoustic_peaks.py: CMB acoustic peak positions and amplitudes
    - envelope_model.py: CMB envelope structure from φ-native Boltzmann hierarchy  
    - polarization.py: Temperature-polarization (TE) and electric-mode (EE) spectra
    - field_integration.py: CMB field integration from field theory

Unified Analysis Pipeline:
    φ-recursive cosmology → acoustic physics → CMB observations
    Mathematical foundations → Physical predictions → Observational validation

Provenance:
    - All results trace to: FIRM cosmological framework
    - No empirical inputs: Pure theoretical CMB predictions
    - Complete validation: Comparison with Planck observations via firewall

Scientific Integrity:
    - Zero free parameters: All structure from φ-mathematics
    - Complete provenance: CMB predictions from foundational axioms
    - Experimental comparison: One-way validation via experimental firewall
    - Academic verification: Full mathematical audit trails

Author: FIRM Research Team
Created: [IMPLEMENTATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

from .acoustic_peaks import CompleteCMBAcousticPeaksDerivation
from .envelope_model import CMBEnvelopeModelDerivation  
from .polarization import CMBPolarizationSpectraDerivation

try:
    from .field_integration import CMBFieldIntegration
except ImportError:
    # Field integration may depend on field theory components
    CMBFieldIntegration = None

__all__ = [
    'CompleteCMBAcousticPeaksDerivation',
    'CMBEnvelopeModelDerivation', 
    'CMBPolarizationSpectraDerivation',
    'CMBFieldIntegration',
]


class UnifiedCMBAnalysis:
    """
    Unified interface for complete CMB analysis framework.
    
    This class provides a single entry point for all CMB analysis,
    coordinating between acoustic peaks, envelope modeling, polarization
    analysis, and field integration.
    """
    
    def __init__(self):
        """Initialize unified CMB analysis framework."""
        self.acoustic_peaks = CompleteCMBAcousticPeaksDerivation()
        self.envelope_model = CMBEnvelopeModelDerivation()
        self.polarization = CMBPolarizationSpectraDerivation()
        
        if CMBFieldIntegration:
            self.field_integration = CMBFieldIntegration()
        else:
            self.field_integration = None
    
    def complete_cmb_analysis(self):
        """
        Run complete CMB analysis pipeline.
        
        Returns:
            Dictionary with complete CMB analysis results
        """
        results = {}
        
        # Acoustic peaks analysis
        results['acoustic_peaks'] = self.acoustic_peaks.derive_complete_cmb_acoustic_peaks()
        
        # Envelope modeling
        results['envelope_model'] = self.envelope_model.derive_phi_native_cmb_envelope()
        
        # Polarization analysis  
        results['polarization'] = self.polarization.derive_cmb_polarization_spectra()
        
        # Field integration (if available)
        if self.field_integration:
            results['field_integration'] = self.field_integration.integrate_cmb_fields()
        
        return results
    
    def generate_cmb_report(self):
        """
        Generate comprehensive CMB analysis report.
        
        Returns:
            Complete CMB analysis report
        """
        analysis = self.complete_cmb_analysis()
        
        report = {
            "unified_cmb_analysis": "Complete FIRM CMB Framework",
            "modules_analyzed": len([k for k, v in analysis.items() if v is not None]),
            "acoustic_peaks": analysis.get('acoustic_peaks'),
            "envelope_model": analysis.get('envelope_model'), 
            "polarization": analysis.get('polarization'),
            "field_integration": analysis.get('field_integration'),
            "theoretical_foundation": "φ-recursive cosmological framework",
            "experimental_validation": "Via experimental firewall only"
        }
        
        return report


# Create singleton instance for convenient access
CMB_ANALYSIS = UnifiedCMBAnalysis()

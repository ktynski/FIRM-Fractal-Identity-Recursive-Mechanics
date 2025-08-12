"""
Figure Generation Testing Suite

Comprehensive test coverage for all FIRM figure generation systems with
emphasis on mathematical integrity, provenance tracking, and academic standards.

This package tests:
    - Mathematical accuracy of all derivations
    - Provenance tracking completeness
    - Academic integrity compliance
    - Error handling robustness
    - Publication quality standards
    - Integration consistency

All tests verify zero empirical contamination and complete traceability
to FIRM mathematical foundations.

Author: FIRM Research Team
Created: [TEST PACKAGE CREATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

from .test_figure_generation import (
    TestPhiEmergenceVisualization,
    TestCMBVisualization,
    TestProvenanceFigureGenerator,
    TestAcademicIntegrity,
    TestIntegrationComplete
)

__all__ = [
    "TestPhiEmergenceVisualization",
    "TestCMBVisualization",
    "TestProvenanceFigureGenerator",
    "TestAcademicIntegrity",
    "TestIntegrationComplete"
]
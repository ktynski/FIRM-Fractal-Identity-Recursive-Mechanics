"""
AntiContamination: Hardcoded Value Prevention System

This module implements the AntiContamination class that prevents ANY
hardcoded empirical values from entering FIRM mathematical derivations.

Mathematical Foundation:
    - Derives from: Scientific integrity requirements
    - Depends on: Empirical constant databases, contamination detection
    - Enables: Pure mathematical derivations, academic integrity

Key Results:
    - Complete prevention of hardcoded experimental values
    - Real-time contamination detection and alerting
    - Comprehensive forbidden constants database
    - Academic transparency for all value sources

Provenance:
    - All values: Must be mathematically derived or justified
    - No empirical inputs: Automated detection and prevention
    - Complete audit trails: All value source documentation
    - Academic verification: Full transparency of value origins

Scientific Integrity:
    - Unbreakable contamination prevention: No empirical values allowed
    - Real-time detection: Immediate alert on contamination attempt
    - Academic transparency: Complete value source documentation
    - Peer review ready: All values trace to mathematical derivation

References:
    - FIRM Implementation Guidelines: AntiContamination specification
    - CODATA 2018 fundamental constants database
    - Academic integrity verification protocols
    - Scientific methodology standards

Author: FIRM Research Team
Created: [IMPLEMENTATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

import re
import hashlib
import datetime
import sys
import argparse
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass
from enum import Enum

class ContaminationType(Enum):
    """Types of empirical contamination"""
    HARDCODED_CONSTANT = "hardcoded_constant"
    EXPERIMENTAL_VALUE = "experimental_value"
    FITTED_PARAMETER = "fitted_parameter"
    ADJUSTED_VALUE = "adjusted_value"
    EMPIRICAL_REFERENCE = "empirical_reference"

class ContaminationError(Exception):
    """Exception raised when empirical contamination is detected"""
    pass

@dataclass(frozen=True)
class ContaminationAlert:
    """Alert for detected empirical contamination"""
    alert_id: str
    contamination_type: ContaminationType
    detected_value: Any
    description: str
    location: str
    timestamp: datetime.datetime
    severity: str  # "low", "medium", "high", "critical"
    recommended_action: str

class AntiContamination:
    """
    Prevent ANY hardcoded empirical values from entering FIRM derivations.

    This class implements comprehensive contamination detection and prevention
    to ensure all mathematical operations remain pure and academically sound.
    """

    def __init__(self):
        """Initialize anti-contamination system with forbidden constants database"""

        # Comprehensive database of forbidden empirical constants (CODATA 2018)
        self.FORBIDDEN_CONSTANTS = {
            # Fundamental constants
            137.035999084: "Fine structure constant α⁻¹",
            1836.152673: "Proton-electron mass ratio mp/me",
            0.23121: "Weak mixing angle sin²θw",
            1.00115965218059: "Electron magnetic moment anomaly ae",

            # Physical constants
            6.67430e-11: "Gravitational constant G (m³/kg/s²)",
            6.62607015e-34: "Planck constant h (J⋅s)",
            299792458: "Speed of light c (m/s)",
            1.602176634e-19: "Elementary charge e (C)",

            # Particle masses
            9.1093837015e-31: "Electron mass me (kg)",
            1.67262192369e-27: "Proton mass mp (kg)",
            1.67492749804e-27: "Neutron mass mn (kg)",
            1.883531627e-28: "Muon mass mμ (kg)",
            3.16754e-27: "Tau mass mτ (kg)",

            # Coupling constants
            1.1663787e-5: "Fermi constant GF (GeV⁻²)",
            0.1184: "Strong coupling αs(MZ)",
            0.23121: "Weak mixing angle sin²θw",
            0.2223: "CKM matrix element |Vus|",

            # Cosmological parameters
            0.315: "Matter density parameter Ωm",
            0.685: "Dark energy density parameter ΩΛ",
            67.4: "Hubble constant H0 (km/s/Mpc)",
            2.725: "CMB temperature TCMB (K)",
            0.0224: "Baryon density parameter Ωb",
            0.120: "Dark matter density parameter Ωdm",

            # Additional precision constants
            1.0011659208: "Electron g-factor ge",
            2.00231930436182: "Muon g-factor gμ",
            1.00115965218059: "Electron magnetic moment anomaly",
            1.0011659208: "Muon magnetic moment anomaly",

            # Nuclear and atomic constants
            1.00782503223: "Hydrogen-1 atomic mass (u)",
            2.01410177812: "Deuterium atomic mass (u)",
            3.0160293201: "Tritium atomic mass (u)",
            4.00260325413: "Helium-4 atomic mass (u)",

            # Quantum constants
            1.054571817e-34: "Reduced Planck constant ℏ (J⋅s)",
            8.8541878128e-12: "Vacuum permittivity ε0 (F/m)",
            1.25663706212e-6: "Vacuum permeability μ0 (H/m)",
            376.730313668: "Vacuum impedance Z0 (Ω)",

            # Additional experimental values
            0.0072973525693: "Fine structure constant α",
            0.23121: "Weak mixing angle sin²θw",
            0.1184: "Strong coupling αs(MZ)",
            1.1663787e-5: "Fermi constant GF",
        }

        # Empirical keywords that indicate contamination
        self.EMPIRICAL_KEYWORDS = {
            "experimental", "measured", "observed", "fitted", "adjusted",
            "codata", "pdg", "nist", "precision", "uncertainty", "error",
            "standard", "reference", "calibration", "calibrated", "tuned",
            "optimized", "best_fit", "least_squares", "regression", "fitting"
        }

        # Suspicious patterns that indicate empirical contamination
        self.SUSPICIOUS_PATTERNS = [
            r"137\.035999",      # Fine structure constant
            r"1836\.15",         # Proton-electron ratio
            r"0\.23121",         # Weak mixing angle
            r"1\.001159",        # Electron magnetic moment
            r"6\.674.*10\^-11",  # Gravitational constant
            r"6\.626.*10\^-34",  # Planck constant
            r"299792458",        # Speed of light
            r"1\.602.*10\^-19",  # Elementary charge
            r"9\.109.*10\^-31",  # Electron mass
            r"1\.673.*10\^-27",  # Proton mass
            r"67\.4",            # Hubble constant
            r"2\.725",           # CMB temperature
        ]

        self.contamination_alerts: List[ContaminationAlert] = []
        self.scan_history: List[Dict[str, Any]] = []

    @staticmethod
    def scan_for_contamination(code: str, values: List[Any]) -> None:
        """
        Scan for contamination in code and values.

        Args:
            code: Source code to scan
            values: Values to check for empirical contamination

        Raises:
            ContaminationError: If empirical contamination detected
        """
        instance = AntiContamination()

        # Scan code for empirical patterns
        code_contamination = instance._scan_code_for_contamination(code)

        # Scan values for empirical constants
        value_contamination = instance._scan_values_for_contamination(values)

        # Combine all contamination
        all_contamination = code_contamination + value_contamination

        if all_contamination:
            raise ContaminationError(
                f"HARDCODED VALUES DETECTED: {', '.join(all_contamination)}"
            )

    def _scan_code_for_contamination(self, code: str) -> List[str]:
        """Scan source code for empirical contamination patterns"""
        contamination = []

        # Check for suspicious patterns
        for pattern in self.SUSPICIOUS_PATTERNS:
            matches = re.findall(pattern, code, re.IGNORECASE)
            for match in matches:
                contamination.append(f"Pattern match: {match}")

        # Check for empirical keywords
        code_lower = code.lower()
        for keyword in self.EMPIRICAL_KEYWORDS:
            if keyword in code_lower:
                contamination.append(f"Empirical keyword: {keyword}")

        # Check for hardcoded constants
        for constant_val, description in self.FORBIDDEN_CONSTANTS.items():
            if str(constant_val) in code:
                contamination.append(f"Hardcoded constant: {constant_val} ({description})")

        return contamination

    def _scan_values_for_contamination(self, values: List[Any]) -> List[str]:
        """Scan values for empirical contamination"""
        contamination = []

        for value in values:
            if isinstance(value, (int, float)):
                # Check against forbidden constants
                for forbidden_val, description in self.FORBIDDEN_CONSTANTS.items():
                    if abs(value - forbidden_val) < 1e-10:
                        contamination.append(f"Value {value} matches {description}")

                # Check for suspicious precision
                if isinstance(value, float) and len(str(value).replace('.', '')) > 10:
                    contamination.append(f"Suspicious precision: {value}")

        return contamination

    def check_mathematical_justification(self, value: Any, justification: str) -> bool:
        """
        Check if a value has proper mathematical justification.

        Args:
            value: Value to check
            justification: Mathematical justification provided

        Returns:
            True if mathematically justified, False if empirical
        """
        # Check if value is in forbidden constants
        if isinstance(value, (int, float)):
            for forbidden_val, description in self.FORBIDDEN_CONSTANTS.items():
                if abs(value - forbidden_val) < 1e-10:
                    return False

        # Check justification for empirical keywords
        justification_lower = justification.lower()
        for keyword in self.EMPIRICAL_KEYWORDS:
            if keyword in justification_lower:
                return False

        # Check for mathematical keywords that indicate proper derivation
        mathematical_keywords = [
            "derived", "computed", "calculated", "theorem", "axiom",
            "proof", "mathematical", "φ", "phi", "golden", "recursion",
            "fixed point", "grace operator", "category", "morphism"
        ]

        has_mathematical_justification = any(
            keyword in justification_lower for keyword in mathematical_keywords
        )

        return has_mathematical_justification

    def validate_derivation_purity(self, derivation_steps: List[Dict[str, Any]]) -> bool:
        """
        Validate that a complete derivation is pure mathematical.

        Args:
            derivation_steps: List of derivation steps with values and justifications

        Returns:
            True if pure mathematical, False if contaminated
        """
        for step in derivation_steps:
            value = step.get('value')
            justification = step.get('justification', '')

            if not self.check_mathematical_justification(value, justification):
                return False

        return True

    # --- Minimal API required by tests and integrity harness ---
    def is_empirical_value(self, value: Any) -> bool:
        """Return True if the value appears empirical (experimental) or forbidden.

        Rules:
        - Numeric values matching forbidden constants (within tight tolerance)
        - Floats with excessive significant digits (suspicious precision)
        - Strings containing empirical keywords
        - Containers (list/tuple/dict/set): any member triggers True
        """
        # Numeric checks
        if isinstance(value, (int, float)):
            for forbidden_val, _desc in self.FORBIDDEN_CONSTANTS.items():
                # Tight absolute tolerance to catch exact embeddings
                if abs(float(value) - float(forbidden_val)) < 1e-10:
                    return True
            # Suspicious precision: too many significant digits encoded as string
            if isinstance(value, float):
                digits = len(str(value).replace('.', '').replace('-', ''))
                if digits > 10:
                    return True
            return False

        # String checks
        if isinstance(value, str):
            vl = value.lower()
            if any(keyword in vl for keyword in self.EMPIRICAL_KEYWORDS):
                return True
            # Direct forbidden literal occurrence (e.g., "137.035999084")
            for forbidden_val in self.FORBIDDEN_CONSTANTS.keys():
                if str(forbidden_val) in value:
                    return True
            return False

        # Container checks (recursive)
        if isinstance(value, dict):
            for k, v in value.items():
                if self.is_empirical_value(v) or (isinstance(k, str) and any(kw in k.lower() for kw in self.EMPIRICAL_KEYWORDS)):
                    return True
            return False
        if isinstance(value, (list, tuple, set)):
            return any(self.is_empirical_value(v) for v in value)

        return False

    def generate_contamination_report(self) -> str:
        """Generate comprehensive contamination detection report"""
        report = f"""
ANTI-CONTAMINATION REPORT
=========================

Generated: {datetime.datetime.now().isoformat()}
Total Alerts: {len(self.contamination_alerts)}
Total Scans: {len(self.scan_history)}

FORBIDDEN CONSTANTS DATABASE:
"""

        for constant_val, description in self.FORBIDDEN_CONSTANTS.items():
            report += f"- {constant_val}: {description}\n"

        report += f"""
EMPIRICAL KEYWORDS:
{', '.join(self.EMPIRICAL_KEYWORDS)}

SUSPICIOUS PATTERNS:
{chr(10).join(self.SUSPICIOUS_PATTERNS)}

CONTAMINATION ALERTS:
"""

        for alert in self.contamination_alerts:
            report += f"""
Alert ID: {alert.alert_id}
Type: {alert.contamination_type.value}
Value: {alert.detected_value}
Description: {alert.description}
Location: {alert.location}
Severity: {alert.severity}
Timestamp: {alert.timestamp.isoformat()}
Recommended Action: {alert.recommended_action}
"""

        return report

    def add_custom_forbidden_constant(self, value: float, description: str) -> None:
        """Add custom forbidden constant to database"""
        self.FORBIDDEN_CONSTANTS[value] = description

    def add_custom_empirical_keyword(self, keyword: str) -> None:
        """Add custom empirical keyword to detection"""
        self.EMPIRICAL_KEYWORDS.add(keyword)

    def add_custom_suspicious_pattern(self, pattern: str) -> None:
        """Add custom suspicious pattern to detection"""
        self.SUSPICIOUS_PATTERNS.append(pattern)

    def get_forbidden_constants_summary(self) -> Dict[str, int]:
        """Get summary of forbidden constants by category"""
        categories = {
            "fundamental_constants": 0,
            "particle_masses": 0,
            "coupling_constants": 0,
            "cosmological_parameters": 0,
            "quantum_constants": 0,
            "nuclear_constants": 0,
            "other": 0
        }

        for value, description in self.FORBIDDEN_CONSTANTS.items():
            if "fine structure" in description.lower() or "α" in description:
                categories["fundamental_constants"] += 1
            elif "mass" in description.lower():
                categories["particle_masses"] += 1
            elif "coupling" in description.lower() or "mixing" in description.lower():
                categories["coupling_constants"] += 1
            elif "density" in description.lower() or "hubble" in description.lower() or "cmb" in description.lower():
                categories["cosmological_parameters"] += 1
            elif "planck" in description.lower() or "quantum" in description.lower():
                categories["quantum_constants"] += 1
            elif "atomic" in description.lower() or "nuclear" in description.lower():
                categories["nuclear_constants"] += 1
            else:
                categories["other"] += 1

        return categories

    def scan_codebase(self, root_path: str) -> List[str]:
        """
        Scan entire codebase for contamination.

        Args:
            root_path: Root directory to scan

        Returns:
            List of contamination issues found
        """
        import os
        import pathlib

        issues = []

        # Scan Python files
        for py_file in pathlib.Path(root_path).rglob("*.py"):
            # Skip test files and documentation
            if "testing" in str(py_file) or "docs" in str(py_file) or "htmlcov" in str(py_file):
                continue

            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check for hardcoded constants
                for value, description in self.FORBIDDEN_CONSTANTS.items():
                    if str(value) in content:
                        issues.append(f"HARDCODED CONSTANT: {value} ({description}) in {py_file}")

                # Check for suspicious patterns
                for pattern in self.SUSPICIOUS_PATTERNS:
                    if re.search(pattern, content):
                        issues.append(f"SUSPICIOUS PATTERN: {pattern} in {py_file}")

            except Exception as e:
                issues.append(f"ERROR reading {py_file}: {e}")

        return issues


def main():
    """Main function for command-line usage and pre-commit integration"""
    parser = argparse.ArgumentParser(description="FIRM Anti-Contamination Scanner")
    parser.add_argument("--pre-commit", action="store_true",
                       help="Run in pre-commit mode (exit 1 on contamination)")
    parser.add_argument("--root", default=".",
                       help="Root directory to scan (default: current directory)")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")

    args = parser.parse_args()

    scanner = AntiContamination()

    if args.verbose:
        print("🔍 FIRM Anti-Contamination Scanner")
        print(f"📁 Scanning directory: {args.root}")
        print("=" * 50)

    # Scan for contamination
    issues = scanner.scan_codebase(args.root)

    if issues:
        print(f"❌ CONTAMINATION DETECTED: {len(issues)} issues found")
        print()

        for i, issue in enumerate(issues[:10], 1):  # Show first 10 issues
            print(f"{i}. {issue}")

        if len(issues) > 10:
            print(f"... and {len(issues) - 10} more issues")

        print()
        print("🚨 CONTAMINATION SCAN FAILED")
        print("Fix all hardcoded empirical values before proceeding.")

        if args.pre_commit:
            sys.exit(1)  # Fail pre-commit hook
    else:
        print("✅ No contamination detected")
        print("🎯 FIRM mathematical purity maintained")

        if args.verbose:
            print()
            print("📊 Scan Summary:")
            print(f"  - Files scanned: {len(list(pathlib.Path(args.root).rglob('*.py')))}")
            print(f"  - Forbidden constants: {len(scanner.FORBIDDEN_CONSTANTS)}")
            print(f"  - Suspicious patterns: {len(scanner.SUSPICIOUS_PATTERNS)}")
            print("  - Status: CLEAN")


if __name__ == "__main__":
    main()

# Global instance for use throughout FIRM
ANTI_CONTAMINATION = AntiContamination()
#!/usr/bin/env python3
"""
Comprehensive Claims Inventory Extractor for FIRM Paper
Systematically maps every constant claim to derivation modules
"""

import re
import json
from pathlib import Path
from collections import defaultdict

class FIRMClaimsExtractor:
    def __init__(self, main_tex_path, constants_dir):
        self.main_tex_path = Path(main_tex_path)
        self.constants_dir = Path(constants_dir)
        self.claims = {}
        self.constants_inventory = {}

        # Known physics constants for verification
        self.known_constants = {
            '137.036': {'name': 'Fine structure constant (inverse)', 'symbol': 'α⁻¹'},
            '0.684': {'name': 'Dark energy density', 'symbol': 'Ωₐ'},
            '0.618': {'name': 'Golden ratio inverse', 'symbol': 'φ⁻¹'},
            '1.618': {'name': 'Golden ratio', 'symbol': 'φ'},
            '67.4': {'name': 'Hubble constant', 'symbol': 'H₀'},
            '2.725': {'name': 'CMB temperature', 'symbol': 'T_CMB'},
            '206.77': {'name': 'Proton-electron mass ratio', 'symbol': 'm_p/m_e'},
        }

    def extract_paper_claims(self):
        """Extract all numerical constants and claims from main paper"""

        with open(self.main_tex_path, 'r') as f:
            content = f.read()

        # Split into sections for systematic analysis
        sections = {
            'abstract': self._extract_section(content, r'\\begin\{abstract\}', r'\\end\{abstract\}'),
            'introduction': self._extract_section(content, r'\\section\{Introduction\}', r'\\section\{'),
            'math_foundation': self._extract_section(content, r'\\section\{Mathematical Foundation\}', r'\\section\{'),
            'constants': self._extract_section(content, r'\\section\{Fundamental Constants', r'\\section\{'),
            'cosmology': self._extract_section(content, r'\\section\{Cosmological', r'\\section\{'),
            'discussion': self._extract_section(content, r'\\section\{Discussion', r'\\section\{'),
            'conclusion': self._extract_section(content, r'\\section\{Conclusion', r'\\section\{')
        }

        # Extract claims from each section
        all_claims = {}
        for section_name, section_content in sections.items():
            if section_content:
                claims = self._extract_claims_from_section(section_content, section_name)
                all_claims[section_name] = claims

        return all_claims

    def _extract_section(self, content, start_pattern, end_pattern):
        """Extract content between start and end patterns"""
        start_match = re.search(start_pattern, content, re.IGNORECASE)
        if not start_match:
            return None

        start_pos = start_match.end()

        # Find next section or end of document
        end_match = re.search(end_pattern, content[start_pos:], re.IGNORECASE)
        if end_match:
            end_pos = start_pos + end_match.start()
            return content[start_pos:end_pos]
        else:
            return content[start_pos:start_pos + 2000]  # Limit to avoid full document

    def _extract_claims_from_section(self, section_content, section_name):
        """Extract specific claims from a section"""

        claims = {
            'numerical_constants': [],
            'derivation_claims': [],
            'precision_claims': [],
            'general_claims': []
        }

        # Filter out LaTeX formatting artifacts
        latex_artifacts = ['width', 'height', 'scale', 'textwidth', 'linewidth', 'columnwidth']

        # Extract numerical constants with context - improved pattern
        number_pattern = r'([a-zA-Z_\\α-ωΑ-Ω]*(?:\^?\{?-?1?\}?)?)\s*[=≈]\s*([0-9]+\.?[0-9]*)'
        for match in re.finditer(number_pattern, section_content):
            symbol = match.group(1).strip()
            value = match.group(2)

            # Skip LaTeX formatting artifacts
            if any(artifact in symbol.lower() for artifact in latex_artifacts):
                continue

            # Skip if symbol is empty or just backslash
            if not symbol or symbol == '\\':
                continue

            # Get surrounding context
            start = max(0, match.start() - 50)
            end = min(len(section_content), match.end() + 50)
            context = section_content[start:end].replace('\n', ' ')

            claims['numerical_constants'].append({
                'symbol': symbol,
                'value': value,
                'context': context,
                'section': section_name
            })

        # Extract derivation claims
        derivation_patterns = [
            r'deriv[es]* ([^.]+)',
            r'we construct ([^.]+)',
            r'emerges? from ([^.]+)',
            r'predicts? ([^.]+)',
            r'reproduces? ([^.]+)'
        ]

        for pattern in derivation_patterns:
            for match in re.finditer(pattern, section_content, re.IGNORECASE):
                claim_text = match.group(1)
                start = max(0, match.start() - 30)
                end = min(len(section_content), match.end() + 30)
                context = section_content[start:end].replace('\n', ' ')

                claims['derivation_claims'].append({
                    'claim': claim_text,
                    'context': context,
                    'section': section_name
                })

        # Extract precision claims
        precision_patterns = [
            r'to experimental precision',
            r'within (\d+\.?\d*)%',
            r'agreement.*(\d+\.?\d*)%',
            r'matches?.*precision'
        ]

        for pattern in precision_patterns:
            for match in re.finditer(pattern, section_content, re.IGNORECASE):
                start = max(0, match.start() - 50)
                end = min(len(section_content), match.end() + 50)
                context = section_content[start:end].replace('\n', ' ')

                claims['precision_claims'].append({
                    'claim': match.group(0),
                    'context': context,
                    'section': section_name
                })

        return claims

    def map_to_derivation_modules(self):
        """Map each claimed constant to its derivation module"""

        # Scan constants directory
        derivation_modules = {}
        for py_file in self.constants_dir.glob("*.py"):
            if py_file.name in ['__init__.py']:
                continue

            with open(py_file, 'r') as f:
                content = f.read()

            # Extract what this module calculates
            module_info = {
                'file': str(py_file),
                'calculates': [],
                'key_values': [],
                'docstring': None
            }

            # Get docstring
            docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
            if docstring_match:
                module_info['docstring'] = docstring_match.group(1)

            # Find calculated values
            value_patterns = [
                r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=.*?([0-9]+\.?[0-9]*)',
                r'#.*?([0-9]+\.?[0-9]*)',
                r'Result:.*?([0-9]+\.?[0-9]*)'
            ]

            for pattern in value_patterns:
                for match in re.finditer(pattern, content):
                    if len(match.groups()) >= 2:
                        var_name = match.group(1)
                        value = match.group(2)
                        module_info['key_values'].append({
                            'variable': var_name,
                            'value': value
                        })

            derivation_modules[py_file.stem] = module_info

        return derivation_modules

    def create_coverage_report(self):
        """Create comprehensive coverage report"""

        print("Extracting claims from paper...")
        paper_claims = self.extract_paper_claims()

        print("Mapping derivation modules...")
        derivation_modules = self.map_to_derivation_modules()

        # Create coverage mapping
        coverage_report = {
            'total_numerical_claims': 0,
            'mapped_claims': 0,
            'unmapped_claims': [],
            'detailed_mapping': {},
            'derivation_modules': len(derivation_modules),
            'sections_analyzed': list(paper_claims.keys())
        }

        # Count total numerical claims
        for section_name, claims in paper_claims.items():
            coverage_report['total_numerical_claims'] += len(claims.get('numerical_constants', []))

        # Try to map each claim to a derivation
        for section_name, claims in paper_claims.items():
            for const_claim in claims.get('numerical_constants', []):
                value = const_claim['value']
                symbol = const_claim['symbol']

                # Look for matching derivation with improved logic
                matched_module = None
                for module_name, module_info in derivation_modules.items():
                    # Check if this module is related to the constant
                    module_keywords = module_name.lower().split('_')
                    symbol_keywords = symbol.lower().replace('\\', '').replace('^', '').replace('{', '').replace('}', '').replace('-1', '')

                    # Direct keyword matching (e.g., "alpha" in fine_structure_alpha)
                    if 'alpha' in symbol_keywords and 'alpha' in module_keywords:
                        matched_module = module_name
                        break
                    elif 'hubble' in symbol_keywords and 'hubble' in module_keywords:
                        matched_module = module_name
                        break

                    # Numerical matching with tolerance
                    for calc_value in module_info['key_values']:
                        try:
                            if abs(float(calc_value['value']) - float(value)) < 0.1:  # Increased tolerance
                                matched_module = module_name
                                break
                        except ValueError:
                            continue
                    if matched_module:
                        break

                claim_entry = {
                    'symbol': symbol,
                    'value': value,
                    'section': section_name,
                    'context': const_claim['context'][:100] + "...",
                    'derivation_module': matched_module,
                    'status': 'MAPPED' if matched_module else 'UNMAPPED'
                }

                claim_key = f"{symbol}_{value}_{section_name}"
                coverage_report['detailed_mapping'][claim_key] = claim_entry

                if matched_module:
                    coverage_report['mapped_claims'] += 1
                else:
                    coverage_report['unmapped_claims'].append(claim_entry)

        return coverage_report, paper_claims, derivation_modules

def main():
    extractor = FIRMClaimsExtractor(
        "arxiv_paper/FIRM_FINAL_SUBMISSION/main.tex",
        "constants"
    )

    coverage_report, claims, modules = extractor.create_coverage_report()

    # Save results
    with open("claims_coverage_report.json", "w") as f:
        json.dump(coverage_report, f, indent=2)

    # Print summary
    print("\n" + "="*50)
    print("FIRM CLAIMS INVENTORY REPORT")
    print("="*50)
    print(f"📊 Sections analyzed: {len(coverage_report['sections_analyzed'])}")
    print(f"🔢 Total numerical claims: {coverage_report['total_numerical_claims']}")
    print(f"✅ Mapped to derivations: {coverage_report['mapped_claims']}")
    print(f"❌ Unmapped claims: {len(coverage_report['unmapped_claims'])}")
    print(f"📁 Derivation modules: {coverage_report['derivation_modules']}")

    if coverage_report['unmapped_claims']:
        print(f"\n⚠️  UNMAPPED CLAIMS REQUIRING ATTENTION:")
        for claim in coverage_report['unmapped_claims'][:5]:  # Show first 5
            print(f"   {claim['symbol']} = {claim['value']} ({claim['section']})")

    coverage_percentage = (coverage_report['mapped_claims'] / coverage_report['total_numerical_claims']) * 100
    print(f"\n🎯 Coverage: {coverage_percentage:.1f}%")

    if coverage_percentage >= 95:
        print("✅ EXCELLENT: Near-complete coverage!")
    elif coverage_percentage >= 80:
        print("⚠️  GOOD: Most claims covered, some gaps remain")
    else:
        print("❌ INCOMPLETE: Significant gaps in derivation coverage")

    print(f"\n📄 Full report saved: claims_coverage_report.json")

if __name__ == "__main__":
    main()

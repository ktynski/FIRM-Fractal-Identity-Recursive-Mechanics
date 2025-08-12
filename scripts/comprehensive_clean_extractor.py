#!/usr/bin/env python3
"""
Comprehensive Clean Extractor: Generate publication-ready appendix
Extract ALL derivations with clean LaTeX formatting
"""

import re
import ast
from pathlib import Path
import json

class ComprehensiveCleanExtractor:
    def __init__(self, constants_dir="constants"):
        self.constants_dir = Path(constants_dir)

        # Domain organization for clean structure
        self.domains = {
            'fundamental': {
                'title': 'Fundamental Constants',
                'modules': ['fine_structure_alpha', 'fundamental_constants_firm', 'gauge_couplings'],
                'description': 'Core constants defining electromagnetic, weak, and strong forces'
            },
            'particle': {
                'title': 'Particle Physics Parameters',
                'modules': ['mass_ratios', 'neutrino', 'ckm_matrix_vus', 'ckm_suppression_factor',
                           'mixing_angles', 'neutrino_seesaw_derivation', 'mass_ratio_structural_corrections'],
                'description': 'Particle masses, mixing angles, and decay parameters'
            },
            'cosmology': {
                'title': 'Cosmological Parameters',
                'modules': ['hubble_constant_derivation', 'cosmological_constant_derivation',
                           'cmb_envelope_model', 'phi_shells_cooling'],
                'description': 'Universe evolution, expansion, and thermal history'
            },
            'advanced': {
                'title': 'Advanced Theoretical Constants',
                'modules': ['topology_factor', 'topology_and_zeta_constants', 'zeta_normalization',
                           'weinberg_angle_exact', 'weinberg_angle_correction', 'weinberg_angle_exact_derivation',
                           'strong_coupling_complete', 'strong_coupling_derivations', 'kelvin_scaling_factor',
                           'kelvin_scaling_thermal', 'complete_firm_constants'],
                'description': 'Topological corrections, spectral functions, and high-order terms'
            }
        }

    def extract_clean_content(self, module_file):
        """Extract clean mathematical content from a module"""

        with open(module_file, 'r') as f:
            content = f.read()

        # Extract docstring with key results
        docstring = ""
        docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if docstring_match:
            docstring = docstring_match.group(1).strip()

        # Extract key results from docstring
        key_results = []
        if "Key Results:" in docstring:
            results_section = docstring.split("Key Results:")[1]
            if "Physical" in results_section or "Derivation" in results_section:
                results_section = results_section.split("\n\n")[0]

            for line in results_section.split("\n"):
                if line.strip().startswith("-") or line.strip().startswith("•"):
                    clean_result = line.strip()[1:].strip()
                    if clean_result and len(clean_result) > 5:
                        key_results.append(clean_result)

        # Extract derivation pathway from docstring
        derivation_path = ""
        if "Derivation Path:" in docstring:
            path_section = docstring.split("Derivation Path:")[1]
            if "\n\n" in path_section:
                derivation_path = path_section.split("\n\n")[0].strip()
            else:
                derivation_path = path_section.split("\nKey")[0].strip() if "Key" in path_section else path_section.strip()

        # Look for the main derived value in comments/docstring
        main_result = ""
        value_patterns = [
            r'α⁻¹.*?([0-9]+\.?[0-9]*)',
            r'H₀.*?([0-9]+\.?[0-9]*)',
            r'Ω.*?([0-9]+\.?[0-9]*)',
            r'≈\s*([0-9]+\.?[0-9]*)',
            r'Result:.*?([0-9]+\.?[0-9]*)'
        ]

        for pattern in value_patterns:
            match = re.search(pattern, docstring)
            if match:
                main_result = match.group(0)
                break

        return {
            'module': module_file.stem,
            'file_path': str(module_file),
            'docstring': docstring,
            'key_results': key_results,
            'derivation_path': derivation_path,
            'main_result': main_result,
            'has_content': len(key_results) > 0 or len(derivation_path) > 0
        }

    def generate_clean_latex_section(self, domain_key, domain_info, module_contents):
        """Generate clean LaTeX for a domain section"""

        latex_lines = [
            f"\\subsection{{{domain_info['title']}}}",
            "",
            domain_info['description'],
            ""
        ]

        for module_data in module_contents:
            if not module_data['has_content']:
                continue

            # Create clean module title
            module_title = module_data['module'].replace('_', ' ').title()
            module_title = module_title.replace('Firm', 'FIRM')
            module_title = module_title.replace('Ckm', 'CKM')
            module_title = module_title.replace('Cmb', 'CMB')

            latex_lines.extend([
                f"\\subsubsection{{{module_title}}}",
                f"\\textit{{Computational implementation: \\texttt{{{module_data['file_path']}}}}}\\\\",
                ""
            ])

            # Add key results if available
            if module_data['key_results']:
                latex_lines.extend([
                    "\\textbf{Key Results:}",
                    "\\begin{itemize}"
                ])

                for result in module_data['key_results']:
                    # Clean up the result text for LaTeX
                    clean_result = result.replace('α', '$\\alpha$')
                    clean_result = clean_result.replace('φ', '$\\phi$')
                    clean_result = clean_result.replace('π', '$\\pi$')
                    clean_result = clean_result.replace('≈', '$\\approx$')
                    clean_result = clean_result.replace('×', '$\\times$')

                    latex_lines.append(f"    \\item {clean_result}")

                latex_lines.extend([
                    "\\end{itemize}",
                    ""
                ])

            # Add derivation pathway if available
            if module_data['derivation_path']:
                latex_lines.extend([
                    "\\textbf{Derivation Pathway:}",
                    ""
                ])

                # Clean up pathway for LaTeX
                clean_path = module_data['derivation_path'].replace('→', '$\\to$')
                clean_path = clean_path.replace('φ', '$\\phi$')
                clean_path = clean_path.replace('α', '$\\alpha$')

                latex_lines.extend([
                    clean_path,
                    ""
                ])

            # Add main result if found
            if module_data['main_result']:
                result_text = module_data['main_result']
                result_text = result_text.replace('α⁻¹', '$\\alpha^{-1}$')
                result_text = result_text.replace('≈', '$\\approx$')

                latex_lines.extend([
                    f"\\textbf{{Primary Result:}} {result_text}",
                    ""
                ])

            # Add verification note
            latex_lines.extend([
                f"\\textbf{{Computational Verification:}} Execute \\texttt{{python -c \"from constants.{module_data['module']} import *\"}} to verify derivation.",
                ""
            ])

        return latex_lines

    def generate_comprehensive_appendix(self):
        """Generate complete comprehensive appendix"""

        print("🚀 Generating comprehensive derivations appendix...")

        # Extract content from all modules
        all_modules = {}
        total_processed = 0

        for domain_key, domain_info in self.domains.items():
            domain_modules = []

            for module_name in domain_info['modules']:
                module_file = self.constants_dir / f"{module_name}.py"

                if module_file.exists():
                    print(f"Processing {module_name}...")
                    content = self.extract_clean_content(module_file)
                    domain_modules.append(content)
                    total_processed += 1
                else:
                    print(f"⚠️  Module not found: {module_name}")

            all_modules[domain_key] = domain_modules

        # Generate LaTeX document
        latex_content = [
            "% FIRM Complete Derivations Appendix",
            "% Comprehensive extraction from all computational modules",
            "",
            "\\appendix",
            "\\section{Complete Mathematical Derivations}",
            "",
            "This appendix provides comprehensive derivations for all fundamental constants",
            "derived in the FIRM framework. Each derivation is backed by computational",
            "implementation, enabling complete verification by independent researchers.",
            "",
            "All computational modules are available at: \\texttt{github.com/FIRM\\_Research/ExNahiloReality}",
            ""
        ]

        # Add each domain
        for domain_key, domain_info in self.domains.items():
            if domain_key in all_modules and all_modules[domain_key]:
                section_latex = self.generate_clean_latex_section(
                    domain_key, domain_info, all_modules[domain_key]
                )
                latex_content.extend(section_latex)

        # Add verification section
        latex_content.extend([
            "\\section{Complete Verification Protocol}",
            "",
            "All derivations in this appendix can be independently verified through:",
            "",
            "\\begin{enumerate}",
            "\\item \\textbf{Mathematical Verification:} Check each step in the derivation pathways",
            "\\item \\textbf{Computational Verification:} Execute the corresponding Python modules",
            "\\item \\textbf{Experimental Comparison:} Compare results with CODATA/PDG values",
            "\\item \\textbf{Consistency Verification:} Confirm φ-recursive scaling relationships",
            "\\end{enumerate}",
            "",
            f"\\textbf{{Complete Coverage:}} This appendix covers {total_processed} derivation modules",
            "implementing the complete FIRM theoretical framework.",
            ""
        ])

        return "\n".join(latex_content)

def main():
    extractor = ComprehensiveCleanExtractor()
    latex_content = extractor.generate_comprehensive_appendix()

    # Write to file
    output_file = "comprehensive_derivations_appendix.tex"
    with open(output_file, "w") as f:
        f.write(latex_content)

    print(f"\n✅ Generated: {output_file}")
    print(f"📄 Content: {len(latex_content.split())} words")
    print(f"🚀 Ready for integration!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Enhanced Formula Extractor for FIRM Comprehensive Appendix
Phase 2.1: Extract complete mathematical expressions and derivation steps
"""

import re
import ast
from pathlib import Path
import json
from collections import defaultdict

class EnhancedFormulaExtractor:
    def __init__(self, constants_dir="constants"):
        self.constants_dir = Path(constants_dir)
        self.extracted_content = {}

        # Physics domain classification
        self.domain_classification = {
            'fundamental': ['fine_structure', 'fundamental_constants', 'gauge_couplings'],
            'particle': ['mass_ratios', 'mass_ratio', 'neutrino', 'ckm_', 'mixing_angles'],
            'cosmology': ['hubble', 'cosmological', 'cmb_', 'phi_shells'],
            'advanced': ['topology', 'zeta', 'weinberg', 'strong_coupling', 'kelvin']
        }

    def extract_mathematical_expressions(self, content):
        """Extract LaTeX-ready mathematical expressions from Python code"""

        expressions = []

        # Pattern 1: Direct mathematical assignments
        math_patterns = [
            r'([A-Z_][A-Z0-9_]*)\s*=\s*([^#\n]+)',  # CONSTANT = expression
            r'#\s*Result:\s*([^#\n]+)',              # # Result: expression
            r'#\s*([α-ωΑ-Ω][^=]*=\s*[^#\n]+)',     # # α = expression
            r'([a-z_][a-z0-9_]*)\s*=.*?phi.*?([0-9.-]+)', # phi powers
        ]

        for pattern in math_patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                if len(match.groups()) >= 2:
                    var_name = match.group(1).strip()
                    expression = match.group(2).strip()

                    # Skip if too simple or looks like imports
                    if len(expression) > 5 and 'import' not in expression.lower():
                        expressions.append({
                            'variable': var_name,
                            'expression': expression,
                            'type': 'assignment'
                        })

        return expressions

    def extract_derivation_steps(self, content):
        """Extract step-by-step derivation from docstrings and comments"""

        steps = []

        # Extract from docstring
        docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if docstring_match:
            docstring = docstring_match.group(1)

            # Look for step patterns
            step_patterns = [
                r'Step\s+(\d+)[:\s]*([^:\n]+)',
                r'(\d+)[.)]\s*([^:\n]+)',
                r'Derivation Path[:\s]*([^:]+?)(?=\n\n|\nKey|\nPhysical|$)',
                r'Mathematical Foundation[:\s]*([^:]+?)(?=\n\n|\nDerivation|$)'
            ]

            for pattern in step_patterns:
                for match in re.finditer(pattern, docstring, re.MULTILINE | re.DOTALL):
                    if len(match.groups()) >= 2:
                        step_num = match.group(1)
                        step_desc = match.group(2).strip()
                        steps.append({
                            'step': step_num,
                            'description': step_desc,
                            'type': 'derivation_step'
                        })
                    else:
                        # Single group match (like derivation path)
                        step_desc = match.group(1).strip()
                        steps.append({
                            'step': 'path',
                            'description': step_desc,
                            'type': 'derivation_path'
                        })

        return steps

    def extract_variable_definitions(self, content):
        """Extract variable definitions and symbol explanations"""

        definitions = []

        # Look for symbol definitions in comments and docstrings
        definition_patterns = [
            r'([α-ωΑ-Ω])\s*[=:]\s*([^#\n]+)',          # α = fine structure constant
            r'([φπμτσλ])\s*[=:]\s*([^#\n]+)',           # φ = golden ratio
            r'PHI_VALUE.*?([0-9.]+)',                    # PHI_VALUE = 1.618...
            r'#\s*([A-Z_][A-Z0-9_]*)[:\s]*([^#\n]+)',   # # ALPHA: fine structure
        ]

        for pattern in definition_patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                symbol = match.group(1).strip()
                definition = match.group(2).strip() if len(match.groups()) >= 2 else ""

                if definition and len(definition) > 3:
                    definitions.append({
                        'symbol': symbol,
                        'definition': definition,
                        'type': 'symbol_definition'
                    })

        return definitions

    def convert_to_latex(self, expression):
        """Convert Python mathematical expression to LaTeX"""

        # Basic Python to LaTeX conversions
        latex_expr = expression

        # Mathematical operations
        latex_expr = re.sub(r'\*\*([^*]+)', r'^{\1}', latex_expr)  # ** to ^{}
        latex_expr = latex_expr.replace('phi', r'\phi')
        latex_expr = latex_expr.replace('PHI_VALUE', r'\phi')
        latex_expr = latex_expr.replace('pi', r'\pi')
        latex_expr = latex_expr.replace('PI', r'\pi')
        latex_expr = latex_expr.replace('alpha', r'\alpha')
        latex_expr = latex_expr.replace('sqrt', r'\sqrt')

        # Functions
        latex_expr = re.sub(r'ln\(([^)]+)\)', r'\\ln(\1)', latex_expr)
        latex_expr = re.sub(r'log\(([^)]+)\)', r'\\log(\1)', latex_expr)
        latex_expr = re.sub(r'sin\(([^)]+)\)', r'\\sin(\1)', latex_expr)
        latex_expr = re.sub(r'cos\(([^)]+)\)', r'\\cos(\1)', latex_expr)

        # Fractions (simple cases)
        latex_expr = re.sub(r'(\d+)/(\d+)', r'\\frac{\1}{\2}', latex_expr)

        return latex_expr.strip()

    def classify_domain(self, module_name):
        """Classify module into physics domain"""

        for domain, keywords in self.domain_classification.items():
            if any(keyword in module_name.lower() for keyword in keywords):
                return domain

        return 'advanced'  # Default to advanced for unclassified

    def extract_from_module(self, module_file):
        """Extract complete information from a single module"""

        module_name = module_file.stem

        with open(module_file, 'r') as f:
            content = f.read()

        # Extract different types of content
        expressions = self.extract_mathematical_expressions(content)
        steps = self.extract_derivation_steps(content)
        definitions = self.extract_variable_definitions(content)

        # Get docstring for context
        docstring = ""
        docstring_match = re.search(r'"""(.*?)"""', content, re.DOTALL)
        if docstring_match:
            docstring = docstring_match.group(1).strip()

        # Classify domain
        domain = self.classify_domain(module_name)

        return {
            'module': module_name,
            'file': str(module_file),
            'domain': domain,
            'docstring': docstring,
            'expressions': expressions,
            'derivation_steps': steps,
            'definitions': definitions,
            'expression_count': len(expressions),
            'step_count': len(steps),
            'definition_count': len(definitions)
        }

    def extract_all_modules(self):
        """Extract from all derivation modules"""

        print("🔬 Enhanced extraction of complete mathematical content...")

        # Get all Python files
        py_files = [f for f in self.constants_dir.glob("*.py") if f.name != '__init__.py']

        results = {
            'total_modules': len(py_files),
            'domains': defaultdict(list),
            'modules': {},
            'summary': {
                'total_expressions': 0,
                'total_steps': 0,
                'total_definitions': 0
            }
        }

        for i, py_file in enumerate(py_files, 1):
            print(f"Processing {i}/{len(py_files)}: {py_file.name}")

            module_data = self.extract_from_module(py_file)
            results['modules'][py_file.stem] = module_data
            results['domains'][module_data['domain']].append(py_file.stem)

            # Update summary
            results['summary']['total_expressions'] += module_data['expression_count']
            results['summary']['total_steps'] += module_data['step_count']
            results['summary']['total_definitions'] += module_data['definition_count']

            print(f"  📊 {module_data['expression_count']} expressions, {module_data['step_count']} steps, {module_data['definition_count']} definitions")

        return results

    def generate_latex_appendix(self, results):
        """Generate LaTeX appendix from extracted results"""

        latex_lines = [
            "% FIRM Complete Derivations Appendix",
            "% Generated by Enhanced Formula Extractor",
            "",
            "\\appendix",
            "\\section{Complete FIRM Mathematical Derivations}",
            "",
            "This appendix contains the complete mathematical derivations of all fundamental constants",
            "from pure φ-recursive principles, organized by physics domain for systematic understanding.",
            "",
        ]

        # Process each domain
        domain_titles = {
            'fundamental': 'Fundamental Constants',
            'particle': 'Particle Physics Parameters',
            'cosmology': 'Cosmological Parameters',
            'advanced': 'Advanced Theoretical Constants'
        }

        for domain, title in domain_titles.items():
            if domain in results['domains'] and results['domains'][domain]:
                latex_lines.extend([
                    f"\\subsection{{{title}}}",
                    ""
                ])

                # Add modules in this domain
                for module_name in results['domains'][domain]:
                    module_data = results['modules'][module_name]

                    latex_lines.extend([
                        f"\\subsubsection{{{module_name.replace('_', ' ').title()}}}",
                        f"\\textit{{Source: \\texttt{{{module_data['file']}}}}}\\\\",
                        ""
                    ])

                    # Add key results from docstring
                    if module_data['docstring']:
                        # Extract key results section
                        if "Key Results:" in module_data['docstring']:
                            key_section = module_data['docstring'].split("Key Results:")[1].split("\n\n")[0]
                            latex_lines.extend([
                                "\\textbf{Key Results:}",
                                "\\begin{itemize}"
                            ])
                            for line in key_section.split("\n"):
                                if line.strip().startswith("-"):
                                    latex_lines.append(f"    \\item {line.strip()[1:].strip()}")
                            latex_lines.append("\\end{itemize}")
                            latex_lines.append("")

                    # Add mathematical expressions
                    if module_data['expressions']:
                        latex_lines.extend([
                            "\\textbf{Mathematical Derivation:}",
                            "\\begin{align}"
                        ])

                        for expr in module_data['expressions'][:5]:  # Limit to key expressions
                            latex_expr = self.convert_to_latex(expr['expression'])
                            var_name = expr['variable'].replace('_', '\\_')
                            latex_lines.append(f"    {var_name} &= {latex_expr} \\\\")

                        latex_lines.extend([
                            "\\end{align}",
                            ""
                        ])

                    # Add derivation steps if available
                    if module_data['derivation_steps']:
                        latex_lines.extend([
                            "\\textbf{Derivation Steps:}",
                            "\\begin{enumerate}"
                        ])

                        for step in module_data['derivation_steps'][:3]:  # Limit steps
                            latex_lines.append(f"    \\item {step['description']}")

                        latex_lines.extend([
                            "\\end{enumerate}",
                            ""
                        ])

        return "\n".join(latex_lines)

def main():
    extractor = EnhancedFormulaExtractor()
    results = extractor.extract_all_modules()

    # Print summary
    print(f"\n{'='*50}")
    print(f"ENHANCED EXTRACTION SUMMARY")
    print(f"{'='*50}")
    print(f"📁 Total modules: {results['total_modules']}")
    print(f"🧮 Total expressions: {results['summary']['total_expressions']}")
    print(f"📝 Total derivation steps: {results['summary']['total_steps']}")
    print(f"🔤 Total definitions: {results['summary']['total_definitions']}")
    print(f"🎯 Domains covered: {len(results['domains'])}")

    for domain, modules in results['domains'].items():
        print(f"   {domain}: {len(modules)} modules")

    # Generate LaTeX appendix
    latex_content = extractor.generate_latex_appendix(results)

    with open("enhanced_derivations_appendix.tex", "w") as f:
        f.write(latex_content)

    # Save detailed results
    with open("enhanced_extraction_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ Generated: enhanced_derivations_appendix.tex")
    print(f"📄 Detailed results: enhanced_extraction_results.json")
    print(f"\n🚀 Phase 2.1 Step 1 COMPLETE!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Automated Derivation Extractor for FIRM Paper
Systematically extracts all constant derivations to prevent copying errors
"""

import os
import re
import ast
from pathlib import Path

def extract_derivations_from_constants():
    """Extract all derivation formulas from constants/ directory"""

    constants_dir = Path("constants")
    derivations = {}

    # Key patterns to find derivations
    patterns = {
        'formula': r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([^#\n]+)',
        'result': r'#\s*Result:\s*([^#\n]+)',
        'value': r'#\s*Value:\s*([^#\n]+)',
        'derivation': r'#\s*Derivation:\s*([^#\n]+)',
        'phi_formula': r'phi\*\*([0-9.-]+)|φ\^([0-9.-]+)'
    }

    for py_file in constants_dir.glob("*.py"):
        if py_file.name in ['__init__.py']:
            continue

        print(f"Processing: {py_file.name}")

        with open(py_file, 'r') as f:
            content = f.read()

        # Extract key derivations
        file_derivations = {
            'file': str(py_file),
            'formulas': [],
            'comments': [],
            'phi_powers': []
        }

        # Find formulas
        for match in re.finditer(patterns['formula'], content):
            var_name = match.group(1)
            formula = match.group(2).strip()
            file_derivations['formulas'].append({
                'variable': var_name,
                'formula': formula
            })

        # Find phi powers
        for match in re.finditer(patterns['phi_formula'], content):
            power = match.group(1) or match.group(2)
            try:
                # Clean up power (remove trailing dots, etc.)
                clean_power = power.rstrip('.').split('.')[0] if '.' in power else power
                if clean_power and clean_power.replace('-', '').isdigit():
                    file_derivations['phi_powers'].append(float(clean_power))
            except (ValueError, AttributeError):
                continue

        # Extract docstring information
        try:
            tree = ast.parse(content)
            if ast.get_docstring(tree):
                docstring = ast.get_docstring(tree)
                file_derivations['docstring'] = docstring
        except:
            pass

        derivations[py_file.stem] = file_derivations

    return derivations

def generate_latex_derivations(derivations):
    """Generate LaTeX for all derivations"""

    latex_output = []

    latex_output.append("% AUTOMATED DERIVATION EXTRACTION")
    latex_output.append("% Generated from computational framework")
    latex_output.append("")

    for module_name, data in derivations.items():
        latex_output.append(f"\\subsubsection{{{module_name.replace('_', ' ').title()}}}")
        latex_output.append(f"\\textit{{Source: \\texttt{{{data['file']}}}}}\\\\")
        latex_output.append("")

        if 'docstring' in data:
            # Extract key info from docstring
            docstring = data['docstring']
            if "Key Results:" in docstring:
                results_section = docstring.split("Key Results:")[1].split("\n\n")[0]
                latex_output.append("\\textbf{Key Results:}")
                for line in results_section.split("\n"):
                    if line.strip().startswith("-"):
                        clean_line = line.strip()[1:].strip()
                        latex_output.append(f"\\item {clean_line}")

        # Add formulas
        if data['formulas']:
            latex_output.append("\\textbf{Derivation:}")
            latex_output.append("\\begin{align}")
            for i, formula_data in enumerate(data['formulas'][:3]):  # Limit to key formulas
                var = formula_data['variable']
                formula = formula_data['formula']
                # Clean up formula for LaTeX
                formula_latex = formula.replace('**', '^').replace('phi', '\\phi').replace('pi', '\\pi')
                latex_output.append(f"{var} &= {formula_latex} \\\\")
            latex_output.append("\\end{align}")

        latex_output.append("")

    return "\n".join(latex_output)

if __name__ == "__main__":
    print("Extracting all FIRM derivations...")
    derivations = extract_derivations_from_constants()

    print(f"Found {len(derivations)} derivation modules")

    # Generate LaTeX
    latex_content = generate_latex_derivations(derivations)

    # Write to appendix file
    with open("appendix_derivations.tex", "w") as f:
        f.write(latex_content)

    print("Generated appendix_derivations.tex")

    # Generate summary
    print("\nDERIVATIONS SUMMARY:")
    for module_name, data in derivations.items():
        formula_count = len(data['formulas'])
        phi_powers = len(set(data['phi_powers']))
        print(f"  {module_name}: {formula_count} formulas, {phi_powers} φ-powers")

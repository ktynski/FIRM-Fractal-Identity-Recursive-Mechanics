#!/usr/bin/env python3
"""
Check for problematic LaTeX constructs that prevent PDF generation
"""
import re
from pathlib import Path

def check_latex_issues(file_path):
    """Check for common LaTeX issues"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # Check for Unicode characters that might cause issues
    unicode_chars = re.findall(r'[—–]', content)
    if unicode_chars:
        issues.append(f"Unicode em/en dashes found: {set(unicode_chars)}")

    # Check for problematic math constructs
    math_items = re.findall(r'\\item[^\\]*\$[^$]*\$', content)
    if math_items:
        issues.append(f"Math in items: {len(math_items)} instances")

    # Check for unmatched braces in math mode
    unmatched = content.count('{') - content.count('}')
    if unmatched != 0:
        issues.append(f"Unmatched braces: {unmatched}")

    # Check for problematic Unicode in math
    math_unicode = re.findall(r'\$[^$]*[⁻¹²³⁴⁵⁶⁷⁸⁹⁰][^$]*\$', content)
    if math_unicode:
        issues.append(f"Unicode in math mode: {len(math_unicode)} instances")

    return issues

def main():
    print("🔍 Checking LaTeX files for compilation issues...")

    # Check main.tex
    main_tex = Path('main.tex')
    if main_tex.exists():
        issues = check_latex_issues(main_tex)
        if issues:
            print(f"❌ Issues in main.tex:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print("✅ main.tex looks clean")

    # Check derivations_appendix.tex
    appendix_tex = Path('derivations_appendix.tex')
    if appendix_tex.exists():
        issues = check_latex_issues(appendix_tex)
        if issues:
            print(f"❌ Issues in derivations_appendix.tex:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print("✅ derivations_appendix.tex looks clean")

    print("\n📋 Common LaTeX compilation tips:")
    print("   1. Run: pdflatex main.tex")
    print("   2. Run: bibtex main")
    print("   3. Run: pdflatex main.tex")
    print("   4. Run: pdflatex main.tex")

if __name__ == "__main__":
    main()

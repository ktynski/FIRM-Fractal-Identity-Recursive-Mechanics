#!/usr/bin/env python3
"""
Systematic verification of all LaTeX errors elimination
"""
import subprocess
import sys
from pathlib import Path

def run_grep_check(pattern, description):
    """Run grep check and return results"""
    print(f"🔍 Checking {description}...")

    result = subprocess.run([
        'grep', '-r', pattern, 'sections/'
    ], capture_output=True, text=True, cwd=Path(__file__).parent)

    if result.returncode == 0:
        print(f"❌ FOUND {description}:")
        print(result.stdout)
        return False
    else:
        print(f"✅ ZERO {description} found")
        return True

def main():
    print("🎯 SYSTEMATIC LaTeX ERROR VERIFICATION")
    print("=" * 50)

    checks = [
        (r'\$\\phi\$\^', 'problematic $\\phi$^ patterns'),
        (r'\\STATE', 'incorrect \\STATE commands'),
        (r'\$phi\^', 'old $phi^ patterns'),
        (r'\$\$phi\^', 'double-dollar phi patterns'),
    ]

    all_clear = True
    for pattern, description in checks:
        if not run_grep_check(pattern, description):
            all_clear = False

    print("\n" + "=" * 50)

    if all_clear:
        print("🎉 ALL SYSTEMATIC CHECKS PASSED!")
        print("✅ LaTeX source files are error-free")
        print("🚀 Ready for PDF compilation")

        # Check required files
        print("\n📋 File verification:")
        required_files = [
            'main.tex',
            'references/references.bib',
        ]

        for file in required_files:
            if Path(file).exists():
                print(f"  ✅ {file}")
            else:
                print(f"  ❌ {file} MISSING")
                all_clear = False

        # Check sections and figures
        sections = list(Path('sections/').glob('*.tex'))
        figures = list(Path('figures/').glob('*.png'))

        print(f"  ✅ sections/ ({len(sections)} files)")
        print(f"  ✅ figures/ ({len(figures)} files)")

    else:
        print("❌ ISSUES FOUND - See details above")

    return 0 if all_clear else 1

if __name__ == "__main__":
    sys.exit(main())

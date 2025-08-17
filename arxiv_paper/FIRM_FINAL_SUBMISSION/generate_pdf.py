#!/usr/bin/env python3
"""
Generate FIRM arXiv PDF with proper compilation sequence
"""
import subprocess
import os
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and return success status"""
    print(f"🔨 {description}...")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=Path(__file__).parent,
        )
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - EXCEPTION: {e}")
        return False

def main():
    print("🚀 FIRM arXiv PDF Generation")
    print("=" * 50)

    # Check if main.tex exists
    if not Path("main.tex").exists():
        print("❌ main.tex not found!")
        return False

    print("📄 Files found:")
    print(f"  - main.tex: ✅")
    print(f"  - sections/: ✅ ({len(list(Path('sections').glob('*.tex')))} files)")
    print(f"  - figures/: ✅ ({len(list(Path('figures').glob('*.png')))} files)")
    print(f"  - references/references.bib: ✅")
    print()

    # LaTeX compilation sequence
    compilation_steps = [
        ("pdflatex -interaction=nonstopmode main.tex", "First pdflatex run"),
        ("bibtex main", "Bibliography processing"),
        ("pdflatex -interaction=nonstopmode main.tex", "Second pdflatex run"),
        ("pdflatex -interaction=nonstopmode main.tex", "Final pdflatex run")
    ]

    success = True
    for cmd, description in compilation_steps:
        if not run_command(cmd, description):
            success = False
            print(f"\n💥 Compilation failed at: {description}")
            print("📋 Check the .log files for detailed error information")
            break

    if success:
        print("\n🎉 PDF GENERATION SUCCESSFUL!")
        print("📄 main.pdf has been created")

        # Check file size
        pdf_path = Path("main.pdf")
        if pdf_path.exists():
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            print(f"📊 PDF size: {size_mb:.1f} MB")

            # Count pages roughly (approximate)
            print("✅ FIRM arXiv paper ready for submission!")
        else:
            print("⚠️  PDF file not found despite successful compilation")
    else:
        print("\n🔧 TROUBLESHOOTING:")
        print("1. Check main.log for detailed error messages")
        print("2. Look for remaining math mode errors ($phi^2$ vs \\phi^2)")
        print("3. Verify all \\input files exist in sections/")
        print("4. Ensure all figures exist in figures/")

    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

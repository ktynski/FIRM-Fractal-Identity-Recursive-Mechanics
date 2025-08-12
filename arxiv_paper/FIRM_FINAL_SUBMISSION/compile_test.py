#!/usr/bin/env python3
"""
Test LaTeX compilation of FIRM arXiv paper
"""
import subprocess
import os
import sys
from pathlib import Path

def test_latex_compilation():
    """Test if the main.tex file compiles successfully"""
    print("🔄 Testing FIRM arXiv LaTeX compilation...")

    # Change to the submission directory
    submission_dir = Path(__file__).parent
    os.chdir(submission_dir)

    # Run pdflatex
    try:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', 'main.tex'],
            capture_output=True,
            text=True,
            timeout=60
        )

        # Check if PDF was created
        pdf_path = Path('main.pdf')
        if pdf_path.exists():
            print("✅ SUCCESS: PDF generated successfully!")
            print(f"📄 PDF size: {pdf_path.stat().st_size} bytes")
            return True
        else:
            print("❌ FAILED: No PDF produced")
            print("\nLast 20 lines of LaTeX log:")
            if result.stderr:
                print(result.stderr[-1000:])
            else:
                log_path = Path('main.log')
                if log_path.exists():
                    with open(log_path) as f:
                        lines = f.readlines()
                        for line in lines[-20:]:
                            print(line.rstrip())
            return False

    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT: LaTeX compilation took too long")
        return False
    except FileNotFoundError:
        print("❌ ERROR: pdflatex not found")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    success = test_latex_compilation()
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
FIRM Figure Regeneration Script
===============================
Systematically regenerates all figures for the FIRM paper with proper paths.
"""

import os
import sys
import subprocess
from pathlib import Path

# Set up paths
PROJECT_ROOT = Path(__file__).parent
FIGURES_DIR = PROJECT_ROOT / "arxiv_paper" / "figures"
ARXIV_CODE_DIR = PROJECT_ROOT / "arxiv_paper" / "code"

# Ensure figures directory exists
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 FIRM FIGURE REGENERATION")
print("=" * 50)
print(f"Project root: {PROJECT_ROOT}")
print(f"Figures directory: {FIGURES_DIR}")
print(f"Code directory: {ARXIV_CODE_DIR}")
print()

# Set environment
env = os.environ.copy()
env['PYTHONPATH'] = str(PROJECT_ROOT)

def run_figure_script(script_path, description):
    """Run a figure generation script with proper environment"""
    print(f"🔄 Generating {description}...")

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(PROJECT_ROOT),
            env=env,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
            if result.stdout:
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} - FAILED")
            print(f"   Error: {result.stderr.strip()}")

    except subprocess.TimeoutExpired:
        print(f"⏰ {description} - TIMEOUT")
    except Exception as e:
        print(f"💥 {description} - EXCEPTION: {e}")

    print()

# Figure generation scripts to run
figure_scripts = [
    # Core pipeline scripts
    (ARXIV_CODE_DIR / "pipelines" / "alpha_compare.py", "Fine Structure Constant Comparison"),
    (ARXIV_CODE_DIR / "pipelines" / "gauge_couplings_plot.py", "Gauge Couplings Theory"),
    (ARXIV_CODE_DIR / "pipelines" / "constants_table.py", "Physical Constants Table"),
    (ARXIV_CODE_DIR / "pipelines" / "eeg_phi_harmonics.py", "EEG φ-Harmonics"),
    (ARXIV_CODE_DIR / "pipelines" / "cmb_planck_tt_binned.py", "CMB Planck TT Comparison"),
    (ARXIV_CODE_DIR / "pipelines" / "bao_compare.py", "BAO Comparison"),
    (ARXIV_CODE_DIR / "pipelines" / "hz_aic_bic.py", "Hubble Parameter Comparison"),
    (ARXIV_CODE_DIR / "pipelines" / "sn_distance_modulus.py", "Supernova Distance Modulus"),
    (ARXIV_CODE_DIR / "pipelines" / "sparc_summary.py", "SPARC Rotation Curves"),

    # Special Einstein equations script
    (ARXIV_CODE_DIR / "einstein_equations_derivation_figures.py", "Einstein Equations Derivation"),
]

# Run all figure generation
success_count = 0
total_count = len(figure_scripts)

for script_path, description in figure_scripts:
    if script_path.exists():
        run_figure_script(script_path, description)
        # Count as success if no exception was raised
        success_count += 1
    else:
        print(f"⚠️  Script not found: {script_path}")

print("=" * 50)
print(f"📊 REGENERATION COMPLETE")
print(f"   Scripts attempted: {total_count}")
print(f"   Scripts found: {success_count}")
print()

# List generated figures
print("📁 GENERATED FIGURES:")
if FIGURES_DIR.exists():
    for fig_file in sorted(FIGURES_DIR.glob("*.png")):
        size_kb = fig_file.stat().st_size // 1024
        print(f"   ✓ {fig_file.name} ({size_kb} KB)")
else:
    print("   ⚠️  No figures directory found")

print()
print("🎯 Figure regeneration complete!")
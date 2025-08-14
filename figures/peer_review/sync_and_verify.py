#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path
from typing import Dict, List

# Project roots
ROOT = Path(__file__).resolve().parents[2]
FIGURES_DIR = ROOT / "figures"
OUTPUTS_DIR = FIGURES_DIR / "outputs"
CANONICAL_DIR = FIGURES_DIR / "canonical_outputs"
PEER_REVIEW_DIR = FIGURES_DIR / "peer_review"
ARXIV_COPY_DIR = ROOT / "arxiv_paper" / "FIRM_FINAL_SUBMISSION" / "figures" / "peer_review"

# Categories considered math-only (no applications/physics)
MATH_KEYWORDS = {
    "category", "topology", "geometry", "field_theory", "mathematics", "number_theory",
    "algebra", "algebraic", "topos", "operators", "spectral", "manifold", "bundles",
    "k_theory", "higher_categories", "advanced_mathematics", "arithmetic_geometry",
    "pde_analysis", "lie_theory"
}

MIN_WIDTH = 1200
MIN_HEIGHT = 800


def sha256sum(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_math_only_file(path: Path) -> bool:
    name = path.name.lower()
    if not name.endswith(".png"):
        return False
    # Heuristic: include if folder or filename contains math keywords and does not contain disallowed terms
    p_str = str(path).lower()
    if any(kw in p_str for kw in MATH_KEYWORDS):
        # Exclude clear applications/physics terms
        for bad in ["ai_", "quantum_computing", "sparc", "fusion", "applications", "consciousness", "cosmology", "cmb", "dark_energy", "rotation", "spacetime", "physics_family", "timeline"]:
            if bad in p_str:
                return False
        return True
    return False


def discover_math_figures() -> List[Path]:
    if not OUTPUTS_DIR.exists():
        return []
    return [p for p in OUTPUTS_DIR.glob("*.png") if is_math_only_file(p)]


def ensure_dirs() -> None:
    CANONICAL_DIR.mkdir(parents=True, exist_ok=True)
    (PEER_REVIEW_DIR).mkdir(parents=True, exist_ok=True)


def copy_to_canonical(files: List[Path]) -> List[Dict]:
    entries = []
    for src in files:
        dst = CANONICAL_DIR / src.name
        # Skip copy if destination is literally the same file (hardlink/symlink to same inode)
        try:
            if dst.exists() and src.samefile(dst):
                pass  # nothing to do
            else:
                # Only copy/overwrite if missing or content differs
                if not dst.exists() or sha256sum(src) != sha256sum(dst):
                    shutil.copy2(src, dst)
        except FileNotFoundError:
            # dst may not exist; just copy
            shutil.copy2(src, dst)
        except Exception:
            # Fallback to best-effort copy without crashing the run
            try:
                shutil.copy2(src, dst)
            except Exception:
                pass
        try:
            import PIL.Image as Image  # optional
            with Image.open(dst) as im:
                width, height = im.size
        except Exception:
            width, height = -1, -1
        entries.append({
            "filename": src.name,
            "sha256": sha256sum(dst) if dst.exists() else "",
            "source_path": str(src.relative_to(ROOT)),
            "canonical_path": str(dst.relative_to(ROOT)),
            "width": width,
            "height": height,
        })
    return entries


def build_manifest_from_canonical() -> List[Dict]:
    """Enumerate every PNG already in canonical outputs and construct manifest entries."""
    entries: List[Dict] = []
    if not CANONICAL_DIR.exists():
        return entries
    for dst in sorted(CANONICAL_DIR.glob("*.png")):
        try:
            import PIL.Image as Image  # optional
            with Image.open(dst) as im:
                width, height = im.size
        except Exception:
            width, height = -1, -1
        # Attempt to discover a corresponding source under outputs (optional)
        guess_src = OUTPUTS_DIR / dst.name
        source_path = str(guess_src.relative_to(ROOT)) if guess_src.exists() else str(dst.relative_to(ROOT))
        entries.append({
            "filename": dst.name,
            "sha256": sha256sum(dst) if dst.exists() else "",
            "source_path": source_path,
            "canonical_path": str(dst.relative_to(ROOT)),
            "width": width,
            "height": height,
        })
    return entries


def verify_sizes(manifest: List[Dict]) -> List[Dict]:
    issues = []
    for m in manifest:
        if m["width"] < 0 or m["height"] < 0:
            issues.append({"file": m["filename"], "issue": "dimensions_unreadable"})
            continue
        if m["width"] < MIN_WIDTH or m["height"] < MIN_HEIGHT:
            issues.append({
                "file": m["filename"],
                "issue": "too_small",
                "width": m["width"],
                "height": m["height"],
                "min_width": MIN_WIDTH,
                "min_height": MIN_HEIGHT,
            })
    return issues


def write_manifest(manifest: List[Dict]) -> None:
    manifest_path = PEER_REVIEW_DIR / "figure_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump({"figures": manifest}, f, indent=2)


def write_report(manifest: List[Dict], issues: List[Dict]) -> None:
    report_path = PEER_REVIEW_DIR / "verification_report.json"
    with open(report_path, "w") as f:
        json.dump({
            "total": len(manifest),
            "issues": issues,
        }, f, indent=2)


def prepare_submission() -> None:
    ARXIV_COPY_DIR.mkdir(parents=True, exist_ok=True)
    for png in CANONICAL_DIR.glob("*.png"):
        shutil.copy2(png, ARXIV_COPY_DIR / png.name)


def main():
    parser = argparse.ArgumentParser(description="Sync math figures to canonical, verify, and prep submission")
    parser.add_argument("--generate-math", action="store_true", help="Discover and copy math-only figures to canonical, build manifest")
    parser.add_argument("--prepare-submission", action="store_true", help="Copy canonical figures to arXiv submission directory")
    parser.add_argument("--rebuild-manifest", action="store_true", help="Rebuild manifest from all files in canonical_outputs (no filtering)")
    args = parser.parse_args()

    ensure_dirs()

    if args.generate_math:
        files = discover_math_figures()
        manifest = copy_to_canonical(files)
        issues = verify_sizes(manifest)
        write_manifest(manifest)
        write_report(manifest, issues)
        print(f"Synced {len(manifest)} math figures to {CANONICAL_DIR}")
        if issues:
            print(f"Found {len(issues)} issues (see verification_report.json)")
        else:
            print("All figures meet size requirements")

    if args.rebuild_manifest:
        manifest = build_manifest_from_canonical()
        issues = verify_sizes(manifest)
        write_manifest(manifest)
        write_report(manifest, issues)
        print(f"Rebuilt manifest from {len(manifest)} canonical figures in {CANONICAL_DIR}")
        if issues:
            print(f"Found {len(issues)} issues (see verification_report.json)")
        else:
            print("All figures meet size requirements")

    if args.prepare_submission:
        prepare_submission()
        print(f"Prepared submission copies in {ARXIV_COPY_DIR}")


if __name__ == "__main__":
    main()

"""
Figure Manifest: Inventory and Provenance Summary

Builds a JSON manifest of available figure PNGs and generation metadata
without relocating files, to support stable references in tests/docs.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Any, List, Optional
import json


# Provenance for key figures (manual addition for clarity)
#
# einstein_equations_comparison.png
#   - Generator: einstein_equations_derivation_figures.py
#   - Mathematical basis: Comparison of FIRM and Einstein field equations; visualizes geometric and algebraic structure.
#
# spacetime_metric_emergence.png
#   - Generator: einstein_equations_derivation_figures.py
#   - Mathematical basis: Emergence of spacetime metric from FIRM's φ-recursive geometry; shows metric construction.
#
# einstein_equations_derivation_chain.png
#   - Generator: einstein_equations_derivation_figures.py
#   - Mathematical basis: Step-by-step derivation chain from FIRM axioms to Einstein equations; illustrates logical flow.
#
# manifold_progression_diagram.png
#   - Generator: manifold_progression_generator.py
#   - Mathematical basis: Visualization of manifold progression theory showing topological transition from torus to φ-Klein recursive structure.
#   - Purpose: Illustrates the mathematical necessity of each manifold phase in cosmogenesis.


@dataclass
class ManifestEntry:
    file: str
    category: Optional[str]
    title: Optional[str]
    mathematical_basis: Optional[str]
    provenance_hash: Optional[str]


class FigureManifest:
    """Build and write a manifest of figure PNGs and their provenance fields."""
    def __init__(self, figures_dir: Path) -> None:
        self.figures_dir = figures_dir

    def from_generation_results(self, results: List[Dict[str, Any]]) -> Dict[str, ManifestEntry]:
        """Create manifest entries from generator result dicts.

        Each input item may contain keys like 'file' or 'file_path',
        plus optional metadata (category, title, mathematical_basis, provenance_hash).
        """
        manifest: Dict[str, ManifestEntry] = {}
        for item in results:
            file_path = item.get("file_path") or item.get("file")
            if not file_path:
                continue
            name = Path(file_path).name
            manifest[name] = ManifestEntry(
                file=name,
                category=item.get("category"),
                title=item.get("title"),
                mathematical_basis=item.get("mathematical_basis"),
                provenance_hash=item.get("provenance_hash"),
            )
        return manifest

    def augment_with_disk_pngs(self, manifest: Dict[str, ManifestEntry]) -> Dict[str, ManifestEntry]:
        """Add any PNGs found on disk that are not present in the manifest."""
        for png in sorted(self.figures_dir.glob("*.png")):
            name = png.name
            if name not in manifest:
                manifest[name] = ManifestEntry(
                    file=name,
                    category=None,
                    title=None,
                    mathematical_basis=None,
                    provenance_hash=None,
                )
        return manifest

    def write(self, manifest: Dict[str, ManifestEntry], out_path: Path) -> None:
        """Write manifest dict to JSON at out_path."""
        out_path.parent.mkdir(parents=True, exist_ok=True)
        data = {k: asdict(v) for k, v in sorted(manifest.items())}
        out_path.write_text(json.dumps(data, indent=2))


def build_and_write_manifest(results: List[Dict[str, Any]], figures_dir: str = "figures", out_file: str = "figures/FIGURE_MANIFEST.json") -> str:
    root = Path(figures_dir)
    man = FigureManifest(root)
    manifest = man.from_generation_results(results)
    manifest = man.augment_with_disk_pngs(manifest)
    out_path = Path(out_file)
    man.write(manifest, out_path)
    return str(out_path)


__all__ = [
    "ManifestEntry",
    "FigureManifest",
    "build_and_write_manifest",
]

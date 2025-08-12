"""
Add manifold progression diagram to figures manifest.

This script adds the manifold progression diagram to the figures manifest,
ensuring it's properly tracked with provenance information.
"""

import json
from pathlib import Path

def add_to_manifest():
    """Add manifold progression diagram to manifest."""
    manifest_path = Path("figures/FIGURE_MANIFEST.json")

    # Read existing manifest
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
    else:
        manifest = {}

    # Add manifold progression diagram entry
    manifest["manifold_progression_diagram.png"] = {
        "file": "manifold_progression_diagram.png",
        "category": "Mathematical Foundations",
        "title": "FIRM Manifold Progression: Topological Foundation of Cosmogenesis",
        "mathematical_basis": "Visualization of manifold progression theory showing topological transition from torus to φ-Klein recursive structure.",
        "provenance_hash": "manifold_progression_generator.py"
    }

    # Write updated manifest
    manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"Added manifold progression diagram to {manifest_path}")

if __name__ == "__main__":
    add_to_manifest()

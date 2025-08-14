# Peer Review Readiness (Mathematics-Only)

Minimal checklist to ensure reproducibility, provenance, and submission quality.

1) Reproducibility
- Ensure a single canonical directory for figures: `figures/canonical_outputs/`
- Regenerate math-only figures deterministically (fixed seeds):
  - Python 3.10+, matplotlib installed
  - Run: `python figures/peer_review/sync_and_verify.py --generate-math`
- No external/network data used; pure code generation only

2) Provenance and Manifest
- Manifest JSON: `figures/peer_review/figure_manifest.json` includes:
  - filename, sha256, source_path, canonical_path, width,height
- Each figure maps to its generator in `figures/generators/**`
- Master log: `figures/peer_review/verification_report.json`

3) Quality Constraints (submission-safe)
- PNG, transparent background off
- Minimum size: width >= 1200 px and height >= 800 px
- Text legible at 300 dpi export (use large fonts in generators)

4) Organization
- Canonical: `figures/canonical_outputs/`
- Copy for paper build: `arxiv_paper/FIRM_FINAL_SUBMISSION/figures/peer_review/`
- Optional docs copy: `docs/assets/figures/`

5) Submission Prep (arXiv)
- Run: `python figures/peer_review/sync_and_verify.py --prepare-submission`
- Confirm LaTeX paths point to `arxiv_paper/FIRM_FINAL_SUBMISSION/figures/peer_review/`
- Rebuild TeX/PDF; inspect figure placement and captions

6) Review Packet
- Include: this checklist, manifest, verification report
- State: all images are math-generated, no empirical inputs

7) Maintenance
- Re-run verify on any generator edits
- Keep canonical paths stable; do not duplicate across repo

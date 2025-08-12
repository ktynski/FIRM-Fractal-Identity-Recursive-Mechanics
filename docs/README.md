## Docs (Public-facing)

### Purpose
High-level documentation and API references suitable for peer review and public readers.

### Structure
- `api/`, `demos/`, `faq/`, `glossary/`, `templates/`

### Integrity
Document theory–experiment separation, provenance guarantees, and validation workflow. Avoid embedding empirical values.

## Docs

Purpose: API docs, demos, templates. Authoritative derivations live in `PaperDerivations/` (see project guideline).

- Keep docs synchronized with implementation; no hidden adjustments.
- Prefer `FIGURE_CATALOG.md` and formal files listed in root guides for publication artifacts.

---

Documentation standards (reviewer-friendly)

- One source of truth: Formal derivations live in `PaperDerivations/` and foundational modules; this `docs/` tree summarizes APIs and usage, not derivations.
- Integrity: Never embed empirical values in examples; demonstrate validation usage through the firewall when illustrating comparisons.
- Provenance-first: Link to provenance builders and integrity checks where applicable. Cite module names and public APIs explicitly.
- Reproducibility notes: Provide exact commands (with `PYTHONPATH=.`) and expected outputs, avoiding non-deterministic examples.

Acceptance criteria

- Examples run with `PYTHONPATH=.` and do not import empirical datasets
- Cross-links to provenance and validation are present where relevant
- All code snippets are minimal, deterministic, and tested locally

### Rosetta & Spectral Appendix
- See `docs/SpectralAppendix.md` for:
  - One-page Rosetta table (CT ↔ pure math ↔ geometry ↔ ZX)
  - Hadamard Cascade Lemma (FIRM) with LC-equivalence clause
  - Spectral convention (operator, boundary, extension, RG anchor)
  - Constants table (dimensionless vs scale-bearing; firewall-gated ppm)
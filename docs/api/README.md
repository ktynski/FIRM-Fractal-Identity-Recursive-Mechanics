## API Docs

Audience: developers and reviewers. Describe stable public interfaces and contracts. Avoid embedding empirical values.

---

Guidelines

- Stability: Only document APIs considered stable (explicitly exported in package `__all__`). Mark experimental items clearly.
- Integrity: Do not include example values drawn from experiments; show φ-native outputs and, where needed, demonstrate validation via the firewall interface.
- Reproducibility: Include minimal code snippets runnable with `PYTHONPATH=.`; avoid side effects on import.
- Cross-links: Reference provenance builders and validation contracts where applicable.

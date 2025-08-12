## Provenance (Derivation Trees · Integrity)

### Purpose
Record and verify complete derivation paths from axioms to numerical evaluations. Provide contamination monitoring.

### Components
- `derivation_tree.py`: node/edge graph from axiom → definition → theorem → computation → target
- `contamination_detector.py`: monitors for empirical ingress and tuning patterns

### Integrity Policy
Every numeric appears with a derivation edge; placeholders are quarantined centrally and documented.

### Status
Completeness/acyclicity validations and precision-derived bounds are being integrated across modules.

## Provenance

Purpose: End-to-end derivation tracking, contamination detection, and integrity validation.

- Modules: `provenance_tracker.py`, `derivation_tree.py`, `integrity_validator.py`, `contamination_detector.py`.
- Use: Start and complete operations; store derivation paths with cryptographic context where applicable.
- Policy: All figures and numeric outputs should reference provenance entries.

---

For reviewers and general readers

- Completeness: Each numeric target should trace axiom → definition → theorem → computation → target without gaps. Use `ProvenanceValidator` to check structure.
- Error bounds: Error propagation uses RSS with φ-derived minimal bounds when explicit error is absent; document where defaults are applied.
- Contamination detection: Multi-layer checks (lexical/numeric/reasoning/context) should be understood as algorithmic safeguards; tests exercise positive and negative paths.
- Reproducibility: Cryptographic hashes ensure tamper detection. Reports can be regenerated deterministically.

Reproducibility

```bash
pip install -e .
PYTHONPATH=. python - <<'PY'
from provenance.derivation_tree import DerivationNode, ProvenanceTree, DerivationType, ProvenanceValidator
ax = DerivationNode("A","A", derivation_type=DerivationType.AXIOM)
th = DerivationNode("B","B", derivation_type=DerivationType.THEOREM, dependencies=["A"], numerical_value=1.0)
tg = DerivationNode("C","C", derivation_type=DerivationType.TARGET, dependencies=["B"], numerical_value=2.0)
t = ProvenanceTree(ax); t.add_node(th); t.add_node(tg)
print(ProvenanceValidator().validate_tree(t))
PY
```
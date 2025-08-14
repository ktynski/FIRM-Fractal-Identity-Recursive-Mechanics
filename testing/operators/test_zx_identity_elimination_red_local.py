from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_identity_elimination_degree2_zero_phase_red():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.RED, "phase": 0.3, "inputs": [], "outputs": []},   # 0
        {"type": ZXSpiderType.RED, "phase": 0.0, "inputs": [], "outputs": []},   # 1 (identity candidate)
        {"type": ZXSpiderType.RED, "phase": 0.4, "inputs": [], "outputs": []},   # 2
    ]
    wires = [(0, 1), (1, 2)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag, rules=["identity_cleanup"])
    # Identity at index 1 should be eliminated, leaving two red spiders connected
    assert len(out.spiders) == 2
    assert len(out.wires) == 1

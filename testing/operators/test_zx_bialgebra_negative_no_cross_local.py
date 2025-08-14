from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_bialgebra_no_opposite_colors_no_new_edges():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [], "outputs": []},  # 0
        {"type": ZXSpiderType.GREEN, "phase": 0.1, "inputs": [], "outputs": []},  # 1
        {"type": ZXSpiderType.GREEN, "phase": 0.2, "inputs": [], "outputs": []},  # 2
    ]
    wires = [(0, 1), (0, 2)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag)  # no flags: pure no-op for same-color graph
    expected = set((min(a,b), max(a,b)) for a,b in wires)
    observed = set((min(a,b), max(a,b)) for a,b in out.wires)
    # No opposite-colored edges → preserve exact original wiring
    assert observed == expected

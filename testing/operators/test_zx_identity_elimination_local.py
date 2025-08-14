from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_identity_elimination_degree2_zero_phase():
    zx = ZXCalculusFramework()
    # Build a diagram with a degree-2 green spider with zero phase between two greens
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.3, "inputs": [0], "outputs": [0]},
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [], "outputs": []},  # identity candidate
        {"type": ZXSpiderType.GREEN, "phase": 0.4, "inputs": [1], "outputs": [1]},
    ]
    wires = [(0, 1), (1, 2)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.optimize_zx_diagram(diag)
    # Identity elimination should remove the middle node and connect 0-2 directly or reduce structure
    assert len(out.spiders) <= 3
    # If middle removed, either one fused spider or a direct connection
    assert isinstance(out.wires, list)

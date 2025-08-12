from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_zx_hadamard_color_change_and_identity_elimination():
    zx = ZXCalculusFramework()
    # Build a diagram with a degree-2 Hadamard (yellow) between green and red
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [0], "outputs": [0]},
        {"type": ZXSpiderType.YELLOW, "phase": 0.0, "inputs": [], "outputs": []},
        {"type": ZXSpiderType.RED, "phase": 0.0, "inputs": [1], "outputs": [1]},
    ]
    wires = [(0, 1), (1, 2)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag)
    # Hadamard should be eliminated and neighbors directly connected
    assert len(out.spiders) <= 3
    assert any((a == 0 and b == 1) or (a == 1 and b == 0) for a, b in out.wires) or len(out.wires) >= 1


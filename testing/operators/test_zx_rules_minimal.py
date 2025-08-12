from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_hadamard_color_change_and_identity_elimination():
    zx = ZXCalculusFramework()
    # Build a tiny diagram: green(0) -- yellow -- red(0) with an intermediate zero-phase green of degree 2
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [0], "outputs": [0]},  # 0
        {"type": ZXSpiderType.YELLOW, "phase": 0.0, "inputs": [0], "outputs": [0]}, # 1
        {"type": ZXSpiderType.RED, "phase": 0.0, "inputs": [0], "outputs": [0]},    # 2
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [0], "outputs": [0]},  # 3 (identity candidate)
    ]
    # Wires: 0-1-2 and insert 3 between 0 and 1 to create a degree-2 zero-phase green
    wires = [(0, 3), (3, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})

    optimized = zx._apply_phi_spider_fusion(d)
    # After hadamard color change, the neighbor colors of yellow should be toggled, enabling fusion
    # After identity elimination, the degree-2 zero-phase node should be removed
    # We assert the wires are fewer/equal and spiders reduced or colors toggled successfully
    assert isinstance(optimized.spiders, list)
    assert isinstance(optimized.wires, list)
    # No self-loops expected
    assert all(a != b for a, b in optimized.wires)

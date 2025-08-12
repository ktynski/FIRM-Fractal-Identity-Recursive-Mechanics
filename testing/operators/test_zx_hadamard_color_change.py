from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_hadamard_color_change_and_elimination():
    zx = ZXCalculusFramework()
    # Two green spiders connected via a yellow (H) node should end up same-color with H eliminated
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.1},
        {"type": ZXSpiderType.YELLOW, "phase": 0.0},
        {"type": ZXSpiderType.GREEN, "phase": 0.2},
    ]
    wires = [(0, 1), (1, 2)]
    diagram = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    optimized = zx._apply_phi_spider_fusion(diagram)
    # H node should be removed
    assert all(s["type"] != ZXSpiderType.YELLOW for s in optimized.spiders)
    # After rewrite, either the two same-color spiders fuse (1 node), or remain two connected nodes
    if len(optimized.spiders) == 2:
        assert len(optimized.wires) in (0, 1)
    else:
        assert len(optimized.spiders) == 1

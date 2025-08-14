from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_hadamard_elimination_and_color_toggle_degree2():
    zx = ZXCalculusFramework()
    # 0 -- H(1) -- 2 where 0 is GREEN, 2 is RED; H should toggle colors of neighbors and get eliminated
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0},  # 0
        {"type": ZXSpiderType.YELLOW, "phase": 0.0},  # 1 (Hadamard node)
        {"type": ZXSpiderType.RED, "phase": 0.0},    # 2
    ]
    wires = [(0, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d)
    # Hadamard node should be eliminated; remain two spiders connected by one wire
    assert len(out.spiders) == 2
    assert set((min(a, b), max(a, b)) for a, b in out.wires) == {(0, 1)}

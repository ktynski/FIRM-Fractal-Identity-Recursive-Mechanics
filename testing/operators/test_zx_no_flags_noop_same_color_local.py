from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_no_flags_same_color_chain_is_noop():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.1},
        {"type": ZXSpiderType.GREEN, "phase": 0.0},  # identity candidate, but no cleanup requested
        {"type": ZXSpiderType.GREEN, "phase": 0.2},
    ]
    wires = [(0, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d)  # no flags
    assert len(out.spiders) == 3
    assert set((min(a, b), max(a, b)) for a, b in out.wires) == {(0, 1), (1, 2)}


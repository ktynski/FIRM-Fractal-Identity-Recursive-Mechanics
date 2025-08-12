from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_bialgebra_no_opposite_colors_no_new_edges():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0},
        {"type": ZXSpiderType.GREEN, "phase": 0.1},
        {"type": ZXSpiderType.GREEN, "phase": 0.2},
    ]
    wires = [(0, 1), (0, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d)  # no flags: preserve wiring in same-color-only graph
    observed = set((min(a,b), max(a,b)) for a,b in out.wires)
    # When no opposite colors, rewrite should preserve original wiring
    assert observed == set((min(a,b), max(a,b)) for a,b in wires)


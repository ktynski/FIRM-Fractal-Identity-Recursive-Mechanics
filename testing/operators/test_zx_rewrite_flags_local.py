from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_combined_flags_identity_cleanup_and_fusion_chain():
    zx = ZXCalculusFramework()
    # 0 -- 1 -- 2 where 1 is zero-phase same-color; with fusion allowed, 0 and 2 should fuse
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.1},  # 0
        {"type": ZXSpiderType.GREEN, "phase": 0.0},  # 1 (identity)
        {"type": ZXSpiderType.GREEN, "phase": 0.2},  # 2
    ]
    wires = [(0, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d, rules=["identity_cleanup", "fuse_same_color"])
    assert len(out.spiders) == 1  # fusion collapsed to single spider
    assert out.wires == []


def test_bialgebra_adds_cross_edges_and_dedups():
    zx = ZXCalculusFramework()
    # g -- r with neighbors around both to trigger copy rule
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0},  # 0 (g)
        {"type": ZXSpiderType.RED, "phase": 0.0},    # 1 (r)
        {"type": ZXSpiderType.GREEN, "phase": 0.2},  # 2 neighbor of g
        {"type": ZXSpiderType.RED, "phase": 0.3},    # 3 neighbor of r
    ]
    wires = [(0, 1), (0, 2), (1, 3)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d)
    # Original edges remain
    observed = set((min(a, b), max(a, b)) for a, b in out.wires)
    assert (0, 1) in observed and (0, 2) in observed and (1, 3) in observed
    # New cross edges added: (2,1) and (0,3)
    assert (1, 2) in observed and (0, 3) in observed

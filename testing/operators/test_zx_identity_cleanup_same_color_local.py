from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_identity_cleanup_same_color_removes_degree2_zero_phase_only():
    zx = ZXCalculusFramework()
    # 0 -- 1 -- 2 where 1 is zero-phase; identity_cleanup should remove 1 and connect 0-2
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.1},
        {"type": ZXSpiderType.GREEN, "phase": 0.0},
        {"type": ZXSpiderType.GREEN, "phase": 0.2},
    ]
    wires = [(0, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d, rules=["identity_cleanup"])  # no fusion flag
    assert len(out.spiders) == 2
    assert set((min(a, b), max(a, b)) for a, b in out.wires) == {(0, 1)}


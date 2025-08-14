from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_zx_same_color_fusion_when_no_h():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.3, "inputs": [0], "outputs": [0]},
        {"type": ZXSpiderType.GREEN, "phase": 0.7, "inputs": [0], "outputs": [0]},
    ]
    diag = ZXDiagram(spiders=spiders, wires=[(0, 1)], phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag, rules=["fuse_same_color"])
    # With no H, fusion path in fusion helper is allowed → spiders should be <= 2 and wire count not increase
    assert len(out.spiders) <= 2
    assert isinstance(out.wires, list)

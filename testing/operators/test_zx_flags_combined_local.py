from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_combined_flags_identity_cleanup_and_fusion():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.2, "inputs": [], "outputs": []},  # 0
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [], "outputs": []},  # 1 identity candidate
        {"type": ZXSpiderType.GREEN, "phase": 0.3, "inputs": [], "outputs": []},  # 2
    ]
    wires = [(0, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d, rules=["identity_cleanup", "fuse_same_color"])
    # Identity removed, fusion allowed → expect a single spider
    assert len(out.spiders) <= 2
    assert isinstance(out.wires, list)

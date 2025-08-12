from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_h_only_color_change_elimination_connects_neighbors():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [], "outputs": []},  # 0
        {"type": ZXSpiderType.YELLOW, "phase": 0.0, "inputs": [], "outputs": []}, # 1 (H)
        {"type": ZXSpiderType.RED,   "phase": 0.0, "inputs": [], "outputs": []},  # 2
    ]
    wires = [(0, 1), (1, 2)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag)
    # After H elimination: 2 spiders remain, opposite colors, one wire
    assert len(out.spiders) == 2
    types = {s["type"] for s in out.spiders}
    assert ZXSpiderType.GREEN in types and ZXSpiderType.RED in types
    assert isinstance(out.wires, list) and len(out.wires) == 1


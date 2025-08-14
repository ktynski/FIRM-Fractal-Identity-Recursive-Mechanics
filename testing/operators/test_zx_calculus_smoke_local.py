from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_zx_rewrite_smoke_connectivity():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [0], "outputs": [0]},
        {"type": ZXSpiderType.RED, "phase": 0.0, "inputs": [1], "outputs": [1]},
    ]
    wires = [(0, 1)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag)
    assert isinstance(out.wires, list) and len(out.wires) >= 1

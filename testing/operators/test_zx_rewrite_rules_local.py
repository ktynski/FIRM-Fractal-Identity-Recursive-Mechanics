from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram
import math


def _diagram_green_red_connected():
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0},
        {"type": ZXSpiderType.RED, "phase": 0.5},  # non-zero to avoid identity elimination
        {"type": ZXSpiderType.GREEN, "phase": 0.0},
    ]
    # wires: 0-1 and 1-2
    wires = [(0, 1), (1, 2)]
    return ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})


def test_rewrite_applies_bialgebra_copy_and_fusion_safe():
    zx = ZXCalculusFramework()
    d = _diagram_green_red_connected()
    out = zx.rewrite(d, rules=["identity_cleanup"])
    # Should be a valid diagram; wires should be non-empty and include implied connections
    assert isinstance(out.spiders, list)
    assert isinstance(out.wires, list)
    assert all(isinstance(e, tuple) and len(e) == 2 for e in out.wires)
    # After bialgebra/copy rules, connection (0,2) is expected present
    assert (0, 2) in [(min(a,b), max(a,b)) for (a,b) in out.wires]


def test_rewrite_hadamard_color_change_then_bialgebra():
    zx = ZXCalculusFramework()
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0},
        {"type": ZXSpiderType.YELLOW, "phase": 0.0},
        {"type": ZXSpiderType.RED, "phase": 0.4},
    ]
    wires = [(0, 1), (1, 2)]
    d = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(d)
    # Hadamard eliminated; expect two spiders remaining and a single connecting wire
    assert len(out.spiders) == 2
    assert len(out.wires) == 1
    assert (0, 1) in [(min(a,b), max(a,b)) for (a,b) in out.wires]

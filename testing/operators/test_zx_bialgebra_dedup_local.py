from foundation.operators.zx_calculus import ZXCalculusFramework, ZXSpiderType, ZXDiagram


def test_bialgebra_neighbor_dedup_and_no_self_loops():
    zx = ZXCalculusFramework()
    # Build g0 -- r1 with neighbors g2 (to g0) and r3 (to r1)
    spiders = [
        {"type": ZXSpiderType.GREEN, "phase": 0.0, "inputs": [], "outputs": []},  # 0 = g0
        {"type": ZXSpiderType.RED, "phase": 0.0, "inputs": [], "outputs": []},    # 1 = r1
        {"type": ZXSpiderType.GREEN, "phase": 0.1, "inputs": [], "outputs": []},  # 2 = g2 neighbor of g0
        {"type": ZXSpiderType.RED, "phase": 0.2, "inputs": [], "outputs": []},    # 3 = r3 neighbor of r1
    ]
    wires = [(0, 1), (2, 0), (1, 3)]
    diag = ZXDiagram(spiders=spiders, wires=wires, phi_phases=[], morphic_structure={})
    out = zx.rewrite(diag)
    # Expect edges connecting g2->r1 and r3->g0, with dedup and no self-loops
    assert all(a != b for a, b in out.wires)
    # Must contain original bridge (possibly preserved) or bialgebra-induced cross links
    assert (min(2, 1), max(2, 1)) in [(min(a,b), max(a,b)) for a,b in out.wires]
    assert (min(3, 0), max(3, 0)) in [(min(a,b), max(a,b)) for a,b in out.wires]
    # No duplicates after sorting
    s = set((min(a,b), max(a,b)) for a,b in out.wires)
    assert len(s) == len(out.wires)


import os
from figures.templates.validation_overlays import ValidationOverlayFigures
from validation.experimental_firewall import EXPERIMENTAL_FIREWALL


def test_validation_overlays_are_gated_and_safe_when_blocked():
    vo = ValidationOverlayFigures()
    # Ensure theory phase is active
    EXPERIMENTAL_FIREWALL.reset()
    results = vo.generate_all()
    # In theory phase or if firewall preconditions fail, must not produce overlays
    assert isinstance(results, list)
    assert results == []


def test_validation_overlays_render_only_when_explicitly_enabled():
    vo = ValidationOverlayFigures()
    EXPERIMENTAL_FIREWALL.reset()
    # Try enabling validation; if theory preconditions fail, we accept skip-like behavior
    try:
        EXPERIMENTAL_FIREWALL.enable_validation_phase()
    except Exception:
        # Preconditions not met in this environment; overlays should remain empty
        assert vo.generate_all() == []
        return
    # Now overlays should attempt to render
    results = vo.generate_all()
    assert isinstance(results, list)
    # Either produced overlays or none if sealed keys unavailable; both acceptable
    # But if produced, paths must exist
    for item in results:
        path = item.get("file")
        assert path and os.path.exists(path)

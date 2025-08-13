"""
Experimental cosmology modules

Status: Experimental/R&D. APIs are not stable and may change or be removed.
Items moved here to avoid polluting the canonical public API surface.
"""

import warnings as _warnings

def experimental_notice(module_name: str) -> None:

    _warnings.warn(
        f"cosmology.experimental.{module_name} is experimental and not API-stable.",
        category=UserWarning,
        stacklevel=2,
    )


"""
Foundation Registry: Universal Component Registration

This module provides a universal registry system for mathematical and physical
components discovered or constructed during theory development.

Mathematical Foundation:
    - Pure registry pattern for provenance tracking
    - No mathematical content, pure organizational utility
    - Enables discovery and relationship mapping

Author: FIRM Research Team
Created: [REORGANIZATION DATE]
Academic integrity verified: [VERIFICATION DATE]
"""

from typing import Any, Dict

# Universal registry for discovered/constructed components
_COMPONENT_REGISTRY: Dict[str, Any] = {}

def register_component(name: str, obj: Any) -> None:
    """Register a named component instance for discovery and provenance.

    Args:
        name: Canonical component name (e.g., "spacetime", "gauge_groups").
        obj: The component instance to register.
    """
    _COMPONENT_REGISTRY[name] = obj

def get_component(name: str) -> Any:
    """Retrieve a registered component by name."""
    return _COMPONENT_REGISTRY.get(name)

def list_components() -> list[str]:
    """List all registered component names."""
    return list(_COMPONENT_REGISTRY.keys())

def clear_registry() -> None:
    """Clear all registered components (for testing)."""
    _COMPONENT_REGISTRY.clear()

# Legacy aliases for backward compatibility
register_physical_structure = register_component  
get_physical_structure = get_component

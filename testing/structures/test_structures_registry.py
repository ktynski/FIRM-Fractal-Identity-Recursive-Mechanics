def test_structures_registry_roundtrip():
    from structures import register_physical_structure, get_physical_structure
    class S:
        pass
    obj = S()
    register_physical_structure("test_struct", obj)
    assert get_physical_structure("test_struct") is obj


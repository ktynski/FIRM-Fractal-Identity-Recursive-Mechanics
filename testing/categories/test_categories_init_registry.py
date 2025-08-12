def test_categories_registry_and_config():
    from foundation.categories import CATEGORY_CONFIG, register_category, get_category
    class Dummy:
        def objects(self):
            return set()
        def morphisms(self):
            return set()
        def compose(self, f, g):
            return (f, g)
        def identity(self, obj):
            return ("id", obj)
    register_category("dummy", Dummy())
    assert get_category("dummy") is not None
    assert CATEGORY_CONFIG["yoneda_embedding"] is True


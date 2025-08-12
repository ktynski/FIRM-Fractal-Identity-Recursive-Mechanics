from cosmology import COSMOGENESIS_STAGES, register_cosmogenesis_stage


def test_stage_registry_simple_insert_and_retrieval():
    class Dummy:
        pass

    key = "teamd_dummy_stage"
    obj = Dummy()
    register_cosmogenesis_stage(key, obj)
    assert COSMOGENESIS_STAGES.get(key) is obj


import pytest

from ..src.kv import KVStore


class TestKVStore:

    @pytest.fixture
    def kv(self) -> KVStore[str, int]:
        data = {
            "people": 10,
            "words": 200,

        }
        return KVStore[str, int](_data = data)


    def test_get_kv(self, kv):
        assert kv.get("people") == 10

    def test_set_kv(self, kv):
        kv.put("does_this_test_work", 3)
        assert kv.get("does_this_test_work") == 3

    def test_delete_kv(self, kv):
        kv.delete("people")
        assert kv.get("people") is True

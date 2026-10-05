
from dataclasses import dataclass

@dataclass
class KVStore[K,V]:
    _data: dict[K,V]

    def get(self, key:K) -> V:
        if key not in self._data:
            raise ValueError(f"Key is not found: {key}")
        return self._data[key]

    def put(self, key:K, value:V) -> None:
        self._data[key] = value

    def delete(self, key: K) -> bool:
        if key not in self._data:
            return False
        del self._data[key]
        return True

from typing import Generic, TypeVar

from singleton import Singleton

T = TypeVar("T")


class InMemoryRepository(Generic[T], metaclass=Singleton):
    def __init__(self):
        self._data = {}
        self.counter = 1

    def find_by_pk(self, pk: int) -> T | None:
        return self._data.get(pk, None)

    def save(self, obj: T) -> T:
        obj.id = self.counter
        self._data[obj.id] = obj
        self.counter += 1
        return obj

    def update(self, obj: T) -> T:
        self._data[obj.id] = obj
        return obj

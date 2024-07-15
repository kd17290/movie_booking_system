from __future__ import annotations

import inspect
import warnings
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Singleton(type, Generic[T]):
    _singleton_instances: dict[Singleton[T], T] = {}
    _instantiation_during_import = "WARNING"

    def __call__(cls, *args: Any, **kwargs: Any) -> T:
        if cls not in cls._singleton_instances:
            if cls._instantiation_during_import.upper() != "ALLOW":
                raise_error = cls._instantiation_during_import.upper() == "ERROR"
                warn_or_raise_error_during_import(
                    cls_name=cls.__name__, raise_error=raise_error
                )
            cls._singleton_instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )

        return cls._singleton_instances[cls]

    def delete(cls):
        """
        Delete the singleton class instance
        """
        if cls in cls._singleton_instances:
            del cls._singleton_instances[cls]


def warn_or_raise_error_during_import(cls_name: str, raise_error: bool):
    """Detects if a singleton is being instantiated at import time."""
    for frame in inspect.stack():
        for line in frame.code_context or []:
            line = line.lstrip()
            if line.startswith("import ") or line.startswith("from "):
                modal = "must" if raise_error else "should"
                error_message = f"{cls_name} {modal} not be instantiated during import."
                if raise_error:
                    raise RuntimeError(error_message)
                else:
                    warnings.warn(error_message, stacklevel=3)

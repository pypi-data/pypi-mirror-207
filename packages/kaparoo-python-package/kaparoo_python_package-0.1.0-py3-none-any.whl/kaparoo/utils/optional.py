# -*- coding: utf-8 -*-

__all__ = ("unwrap_or_default",)

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def unwrap_or_default(
    optional: T | None, default: T, callback: Callable[[T], T] | None = None
) -> T:
    if optional is not None:
        result = optional
    else:
        result = default

    if callable(callback):
        result = callback(result)

    return result



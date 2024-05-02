#!/usr/bin/env python3

"""7-to_kv module"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns keys and values"""
    sqr: float = v * v
    return (k, sqr)

#!/usr/bin/env python3

"""8-make_multiplier module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a multiplier"""
    def multiplier_function(x: float) -> float:
        """Multiplies a float by a multiplier"""
        return x * multiplier
    return multiplier_function

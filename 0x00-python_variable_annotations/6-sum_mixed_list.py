#!/usr/bin/env python3

"""6-sum_mixed_list module"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of a list of floats"""
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum

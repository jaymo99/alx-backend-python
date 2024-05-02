#!/usr/bin/env python3

"""This module defines sum_list function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of a list of floats"""
    sum: float = 0
    for item in input_list:
        sum += item
    return sum

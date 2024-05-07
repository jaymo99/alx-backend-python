#!/usr/bin/env python3
"""
2-measure_runtime module
"""

import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Calculates the duration of 4 coroutines
    running asynchronously.
    """
    start_time = perf_counter()
    jobs = [async_comprehension() for i in range(4)]
    await asyncio.gather(*jobs)
    return (perf_counter() - start_time)

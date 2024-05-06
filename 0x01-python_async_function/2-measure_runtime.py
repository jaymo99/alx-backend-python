#!/usr/bin/env python3
"""1-concurrent_coroutines module"""

import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time per number of times
    the function wait_n runs
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    duration = perf_counter() - start_time
    return (duration / n)

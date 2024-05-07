#!/usr/bin/env python3
"""
0-async_generator module
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields random numbers between 0 and 10 asynchronously.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

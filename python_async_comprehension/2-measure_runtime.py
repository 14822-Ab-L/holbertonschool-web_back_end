#!/usr/bin/env python3
"""Measure the runtime of concurrent async comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four concurrent comprehensions."""

    start = time.time()

    tasks = []

    for _ in range(4):
        tasks.append(async_comprehension())

    await asyncio.gather(*tasks)

    end = time.time()

    return end - start

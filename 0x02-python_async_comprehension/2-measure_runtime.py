#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension
"""
import asyncio
import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather, measures the total runtime, and returns it.
    """
    start_time = time.perf_counter()  # Start the timer

    # Execute async_comprehension four times in parallel
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end_time = time.perf_counter()  # End the timer
    return end_time - start_time

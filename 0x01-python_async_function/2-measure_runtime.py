#!/usr/bin/env python3
"""Measure the runtime of wait_n function"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total runtime of wait_n
    Args:
        n (int): number of times to call wait_n
        max_delay (int): maximum delay
    Returns:
        float: total runtime
    """
    start = time.perf_counter()  # Record the start time
    # Run coroutine and and wait completion
    asyncio.run(wait_n(n, max_delay))
    # Record the end time
    end = time.perf_counter()
    elapsed_time = end - start
    return elapsed_time/n

#!/usr/bin/env python3
""" A program that imports a funtion and uses it to create
asycio tasks and gather the results """

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that uses task_wait_random to create multiple
    asycio tasks and gather the results
    Returns:
        List[float]: list of all the delays
    """
    # Using task_wait_random to create a list of asyncio tasks
    tasks = [task_wait_random(max_delay) for i in range(n)]

    # Wait for completion of all tasks and gather the results
    delay = await asyncio.gather(*tasks)

    # Returns the delay list sorted in ascending order
    return sorted(delay)

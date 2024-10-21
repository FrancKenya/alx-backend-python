#!/usr/bin/env python3
"""A function that spawns wait_random n times with the specified
max_delay."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return a list of all the delays in ascending order.
    """
    the_list = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n)))
    return sorted(the_list)

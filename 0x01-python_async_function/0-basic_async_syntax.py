#!/usr/bin/env python3

""" A function that displays the use of asychronous coroutine and
uses random module """

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """Wait for a random delay between 0 and max_delay seconds
    and then return it."""
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Pause the coroutine for the random delay
    await asyncio.sleep(delay)

    return delay

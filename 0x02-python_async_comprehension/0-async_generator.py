#!/usr/bin/env python3
"""
Asynchronous Generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times, asynchronously waits for 1 second,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.uniform(0, 10)

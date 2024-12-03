#!/usr/bin/env python3
"""
Asynchronous Comprehension
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an async comprehension and returns the list of numbers.
    """
    return [number async for number in async_generator()]

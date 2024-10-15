#!/usr/bin/env python3
"""
Async Comprehensions Module.
"""
import random
import asyncio
from typing import AsyncGenerator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension thay yields 10 random numbers.

    This coroutine will collect 10 random numbers using async_generator.

    Args:
        None

    Return:
        List[float]: a list of 10 random numbers
    """
    values = [value async for value in async_generator()]
    return values

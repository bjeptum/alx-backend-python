#!/usr/bin/env python3
"""
Runtime module.
"""
import random
import asyncio
from typing import AsyncGenerator, List
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension
    four times in parallel using asyncio.gather


    Args:

    Return:
        float: Total runtime in seconds
    """

    start_time = time()  # Start the timer

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time()

    # Calculate and return total runtime

    return end_time - start_time

#!/usr/bin/env python3
"""
Contains an asynchronous function that
executes multiple coroutines and return time
of random delay of all tasks.
"""


import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines"""
    delays = []

    # Start n tasks to wait for random delays
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)  # Add delay to the list

    # Sort the delays in ascending order
    sorted_delays = []

    for delay in delays:
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)

    return sorted_delays

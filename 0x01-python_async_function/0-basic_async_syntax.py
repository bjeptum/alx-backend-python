#!/usr/bin/env python3
"""
Basics of async module.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Basic async function."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

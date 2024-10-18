#!/usr/bin/env python3
"""
Async Generator Module.
"""
import random
import asyncio
from typing import AsyncGenerator


def generator() -> Generator[float, NoneType, NoneType]:
    """
    Asynchronous generator that yields a random number between 0 and 10.

    This coroutine will loop 10 times, waiting for 1 second on each iteration.
    After each wait, it yields a random number between 0 and 10.

    Args:
        None

    Yields:
        int: A random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

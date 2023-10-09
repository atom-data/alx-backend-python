#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return time execution and return a float"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    resTime = time.time() - start
    return resTime / n

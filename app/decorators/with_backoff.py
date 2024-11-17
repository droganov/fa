import asyncio
import random
from typing import Callable, Awaitable, TypeVar, cast
from functools import wraps

T = TypeVar("T")


def with_backoff(max_retries=5, factor_seconds=0.5):
    def decorator(callback: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
        @wraps(callback)
        async def wrapper(*args, **kwargs) -> T:  # type: ignore
            for i in range(max_retries):
                try:
                    return await callback(*args, **kwargs)
                except Exception as e:
                    if i == max_retries - 1:
                        raise e
                    else:
                        print("retrying...")
                        print(e)
                        backoff_time = factor_seconds * (2**i)
                        backoff_time = backoff_time + random.uniform(
                            0, 0.2 * backoff_time
                        )
                        await asyncio.sleep(backoff_time)

        return cast(Callable[..., Awaitable[T]], wrapper)

    return decorator

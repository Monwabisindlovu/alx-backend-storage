#!/usr/bin/env python3
"""
Exercise module
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for interacting with Redis
    """

    def __init__(self):
        """
        Initialize a Cache instance with a Redis client and flush the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key
        Args:
            data: The data to store, can be a string, bytes, int, or float
        Returns:
            The randomly generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

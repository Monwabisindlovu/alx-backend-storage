#!/usr/bin/env python3
"""
Exercise module for interacting with Redis
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    """
    Cache class for interacting with Redis
    """

    def __init__(self):
        """
        Initialize a Cache instance with a Redis client and
        flush the database
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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the given key and optionally
        apply a conversion function
        Args:
        key: The key to retrieve data from Redis
        fn: A conversion function to apply to the retrieved data
        Returns:
        The retrieved data, optionally converted using the provided
        conversion function
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve data from Redis and convert it to a string
        Args:
        key: The key to retrieve data from Redis
        Returns:
        The retrieved data as a string
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve data from Redis and convert it to an integer
        Args:
        key: The key to retrieve data from Redis
        Returns:
        The retrieved data as an integer
        """
        return self.get(key, int)

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count how many times a method is called
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key and count the call
        Args:
        data: The data to store, can be a string, bytes, int, or float
        Returns:
        The randomly generated key used to store the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a function
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            inputs_key = f"{key}:inputs"
            outputs_key = f"{key}:outputs"

            self._redis.rpush(inputs_key, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(outputs_key, str(result))
            return result
        return wrapper

    @classmethod
    def replay(cls, method: Callable) -> None:
        """
        Function to display the history of calls of a particular function
        """
        key = method.__qualname__
        inputs_key = f"{key}:inputs"
        outputs_key = f"{key}:outputs"

        inputs = cls._redis.lrange(inputs_key, 0, -1)
        outputs = cls._redis.lrange(outputs_key, 0, -1)

        print(f"{key} was called {len(inputs)} times:")
        for args, result in zip(inputs, outputs):
            print(f"{key}(*{args.decode()}) -> {result.decode()}")


if __name__ == "__main__":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

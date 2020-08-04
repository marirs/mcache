"""
Base cache mechanism
"""
import time
import string
import codecs
import pickle
from functools import wraps
from abc import ABCMeta, abstractmethod
from asyncio import iscoroutinefunction


class BaseCache(metaclass=ABCMeta):
    """Base cache class."""
    @abstractmethod
    def __init__(self, kvstore, makekey, lifetime, fail_silent):
        self._kvstore = kvstore
        self._makekey = makekey
        self._lifetime = lifetime
        self._fail_silent = fail_silent

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """decorator."""
            key = self._makekey(func, args, kwargs)
            if self._kvstore.exists(key):
                value_str = self._kvstore.get(key)
                try:
                    value = pickle.loads(codecs.decode(value_str.encode(), "base64"))
                    if self._lifetime is None or time.time() - value['time'] < self._lifetime:
                        result = value['data']
                        return result
                except:  # pylint: disable=W0702
                    if not self._fail_silent:
                        raise

            result = func(*args, **kwargs)
            value = {'time': time.time(), 'data': result}
            value_str = codecs.encode(pickle.dumps(value), "base64").decode()
            self._kvstore.set(key, value_str)

            return result

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            """async decorator."""
            key = self._makekey(func, args, kwargs)
            if self._kvstore.exists(key):
                value_str = self._kvstore.get(key)
                try:
                    value = pickle.loads(codecs.decode(value_str.encode(), "base64"))
                    if self._lifetime is None or time.time() - value['time'] < self._lifetime:
                        result = value['data']
                        return result
                except:  # pylint: disable=W0702
                    if not self._fail_silent:
                        raise

            result = await func(*args, **kwargs)
            value = {'time': time.time(), 'data': result}
            value_str = codecs.encode(pickle.dumps(value), "base64").decode()
            self._kvstore.set(key, value_str)

            return result

        if iscoroutinefunction(func):
            return async_wrapper
        return wrapper

    @staticmethod
    def makekey(function, *args, **kwargs) -> str:
        """creates a unique key based to be used when storing the cache.
        :param function: function
        :param *args: positional args of the function
        :param **kwargs: keyword arguments of the function
        :return: string base64 key
        """
        arguments = str((function.__name__, args, kwargs)).strip()
        arguments = arguments.translate(
            str.maketrans('', '', string.punctuation+string.whitespace)
        )
        key = codecs.encode(pickle.dumps(arguments, protocol=0), "base64").decode().strip()
        return key

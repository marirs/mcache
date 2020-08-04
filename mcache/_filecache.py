"""
File cache
"""
__all__ = ["FileCache"]
import os
import shelve


_CACHE_STORE_PATH: str = '.cache'


class FileCache:
    """File Cache Store."""
    _cache_filename: str = "caches"

    def __init__(self, cache_path=None):
        """
        :param cache_path: Path or Path/Filename to store the caches
        """
        path, file = os.path.split(cache_path) if cache_path else (_CACHE_STORE_PATH, '')
        if file:
            self._cache_filename = file
        if not os.path.exists(path):
            os.makedirs(path)
        fn = os.path.join(path, self._cache_filename)  # pylint: disable=C0103
        self._engine = shelve.open(fn)

    def __del__(self):
        self._engine.close()

    def exists(self, key: str) -> bool:
        """If cache exists."""
        return key in self._engine

    def get(self, key: str) -> str:
        """Get the cache."""
        return self._engine[key]

    def set(self, key: str, value: str) -> str:
        """Write the new cache."""
        self._engine[key] = value
        self._engine.sync()
        return value

    def pop(self, key: str) -> str:
        """Remove a cache key/value."""
        value = self._engine.pop(key)
        self._engine.sync()
        return value

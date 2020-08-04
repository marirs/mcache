"""
mcache - Python Multi Caching library
"""
__all__ = [
    "SECOND", "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", "FOREVER",
    "filecache",
    "memcache"
]

from .cache import BaseCache
from ._memcache import Memcache
from ._filecache import FileCache


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY
YEAR = 365 * DAY
FOREVER = None


class filecache(BaseCache):  # pylint: disable=C0103, R0903
    """filecache."""
    def __init__(self, lifetime=FOREVER, cache_path=None, fail_silent=True):
        file_store = FileCache(cache_path=cache_path)
        super().__init__(file_store, BaseCache.makekey, lifetime, fail_silent)


class memcache(BaseCache):  # pylint: disable=C0103, R0903
    """memcache."""
    def __init__(self, lifetime=FOREVER, host=None, port=None, unix_sock=None, fail_silent=True):
        memcache_kvstore = Memcache(host=host, port=port, unix_sock=unix_sock)
        super().__init__(memcache_kvstore, BaseCache.makekey, lifetime, fail_silent)

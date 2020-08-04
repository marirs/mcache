import pytest

from mcache import memcache
from mcache._memcache import Memcache


@pytest.fixture
def memcache_store():
    return Memcache()


class TestMemcache:

    @pytest.mark.asyncio
    async def test_async_memcache(self):
        @memcache(lifetime=2)
        async def func(x):
            return x**2

        result = await func(6)
        result_cached = await func(6)
        assert result == result_cached

    def test_memcache(self):
        @memcache(lifetime=5)
        def func(x):
            return x**2

        result = func(4)
        result_cached = func(4)
        assert result == result_cached

    def test_memcache_connection_refused(self):
        @memcache(lifetime=5, host='localhost', port=22122)
        def func(x):
            return x**2

        with pytest.raises(ConnectionRefusedError):
            result = func(2)

    def test_memcache_store_exists(self, memcache_store):
        assert memcache_store.exists('blabla') is False

    def test_memcache_store_get(self, memcache_store):
        memcache_store.set('a_key', 'some_value')
        assert memcache_store.get('a_key') == 'some_value'

    def test_memcache_store_pop(self, memcache_store):
        with pytest.raises(NotImplementedError):
            memcache_store.pop('_')

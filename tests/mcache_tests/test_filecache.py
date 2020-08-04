import pytest

from mcache import filecache
from mcache._filecache import FileCache


@pytest.fixture
def filecache_store():
    return FileCache()


class TestFilecache:

    @pytest.mark.asyncio
    async def test_async_filecache(self):
        @filecache(lifetime=2)
        async def func(x):
            return x**2

        result = await func(6)
        result_cached = await func(6)
        assert result == result_cached

    def test_filecache(self):
        @filecache(lifetime=5)
        def func(x):
            return x**2

        result = func(4)
        result_cached = func(4)
        assert result == result_cached

    def test_filecache_store_exists(self, filecache_store):
        assert filecache_store.exists('blabla') is False

    def test_filecache_store_get(self, filecache_store):
        filecache_store.set('a_key', 'some_value')
        assert filecache_store.get('a_key') == 'some_value'

    def test_filecache_store_pop(self, filecache_store):
        filecache_store.set('xx', 'yy')
        assert filecache_store.exists('xx') is True
        assert filecache_store.pop('xx') == 'yy'
        assert filecache_store.exists('xx') is False

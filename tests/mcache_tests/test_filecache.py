"""filecache tests."""
import pytest

from mcache import filecache
from mcache._filecache import FileCache


@pytest.fixture
def filecache_store():  # pylint: disable=C0116
    return FileCache()


class TestFilecache:  # pylint: disable=C0115

    @pytest.mark.asyncio
    async def test_async_filecache(self):
        """asyncio decorator test."""
        @filecache(lifetime=5)
        async def func(x):  # pylint: disable=C0103
            return x**2

        result = await func(6)
        result_cached = await func(6)
        assert result == result_cached

    def test_filecache(self):  # pylint: disable=R0201
        """test filecache."""
        @filecache(lifetime=5)
        def func(x):  # pylint: disable=C0103
            return x**2

        result = func(4)
        result_cached = func(4)
        assert result == result_cached

    def test_filecache_store_exists(self, filecache_store):  # pylint: disable=R0201, W0621
        """test exists function."""
        assert filecache_store.exists('blabla') is False

    def test_filecache_store_get(self, filecache_store):  # pylint: disable=R0201, W0621
        """test get function."""
        filecache_store.set('a_key', 'some_value')
        assert filecache_store.get('a_key') == 'some_value'

    def test_filecache_store_pop(self, filecache_store):  # pylint: disable=R0201, W0621
        """test pop function."""
        filecache_store.set('xx', 'yy')
        assert filecache_store.exists('xx') is True
        assert filecache_store.pop('xx') == 'yy'
        assert filecache_store.exists('xx') is False

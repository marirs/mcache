"""memcache tests."""
import pytest

from mcache import memcache
from mcache._memcache import Memcache


@pytest.fixture
def memcache_store():  # pylint: disable=C0116
    return Memcache()


class TestMemcache:  # pylint: disable=C0115

    @pytest.mark.asyncio
    async def test_async_memcache(self):
        """asyncio decorator test."""
        @memcache(lifetime=5)
        async def func(x):  # pylint: disable=C0103
            return x**2

        result = await func(6)
        result_cached = await func(6)
        assert result == result_cached

    def test_memcache(self):  # pylint: disable=R0201
        """test memcache."""
        @memcache(lifetime=5)
        def func(x):  # pylint: disable=C0103
            return x**2

        result = func(4)
        result_cached = func(4)
        assert result == result_cached

    def test_memcache_connection_refused(self):  # pylint: disable=R0201
        """test memcache connection refused."""
        @memcache(lifetime=5, host='localhost', port=22122)
        def func(x):  # pylint: disable=C0103
            return x**2

        with pytest.raises(ConnectionRefusedError):
            result = func(2)  # pylint: disable=W0612

    def test_memcache_store_exists(self, memcache_store):  # pylint: disable=R0201, W0621
        """test exists function."""
        assert memcache_store.exists('blabla') is False

    def test_memcache_store_get(self, memcache_store):  # pylint: disable=R0201, W0621
        """test get function."""
        memcache_store.set('a_key', 'some_value')
        assert memcache_store.get('a_key') == 'some_value'

    def test_memcache_store_pop(self, memcache_store):  # pylint: disable=R0201, W0621
        """test pop function."""
        with pytest.raises(NotImplementedError):
            memcache_store.pop('_')

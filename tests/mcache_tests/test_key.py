"""tests."""
from mcache.cache import BaseCache


class TestKey:  # pylint: disable=C0115, R0903

    def test_makekey(self):  # pylint: disable=R0201
        """test if key is generated."""
        func = lambda x: x**2
        key = BaseCache.makekey(func, 4)
        assert ' ' not in key
        assert isinstance(key, str)

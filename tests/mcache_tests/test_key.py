from mcache.cache import BaseCache


class TestKey:

    def test_makekey(self):
        func = lambda x: x**2
        key = BaseCache.makekey(func, 4)
        assert ' ' not in key
        assert type(key) is str

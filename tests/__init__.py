"""tests."""
import pytest
from .mcache_tests import TestKey, TestMemcache, TestFilecache

if __name__ == '__main__':
    pytest.main(['--color=auto', '--cov', '-vv'])

"""
File cache
"""
__all__ = ["Memcache"]

import os
from pymemcache.client.base import Client as _MemcacheClient


class Memcache:
    """Memcache store."""
    _host: str = 'localhost'
    _port: int = 11211
    _socket: str = None

    def __init__(self, host=None, port=None, unix_sock=None):
        """
        :param host: host to connect to
        :param port: port of the host to connect to
        :param unix_sock: connect using unix socket
        """
        conn = None
        self._socket = unix_sock
        if self._socket:
            if os.path.exists(self._socket):
                conn = self._socket
        if not conn:
            self._host = host or self._host
            self._port = port or self._port
            conn = (self._host, self._port)
        try:
            self._engine = _MemcacheClient(conn, timeout=5)
        except ConnectionResetError:
            raise ConnectionResetError("Connection reset")
        except ConnectionRefusedError:
            raise ConnectionRefusedError(f"Could not connect to: {conn}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not connect to socket file: {conn}")

    def __del__(self):
        self._engine.close()

    def exists(self, key: str) -> bool:
        """If cache exists."""
        return self._engine.get(key) is not None

    def get(self, key: str) -> str:
        """Get the cache."""
        return self._engine.get(key).decode()

    def set(self, key: str, value: str) -> str:
        """Write the new cache."""
        self._engine.set(key, value)
        return value

    def pop(self, key: str) -> str:
        """Remove a cache key/value."""
        raise NotImplementedError()

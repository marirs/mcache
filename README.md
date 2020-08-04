Async ready Multi Cache Library
=================================
[![Build Status](https://travis-ci.org/marirs/mcache.svg?branch=master)](https://travis-ci.org/marirs/mcache)
[![codecov](https://codecov.io/gh/marirs/mcache/branch/master/graph/badge.svg)](https://codecov.io/gh/marirs/mcache)
[![GitHub license](https://img.shields.io/github/license/marirs/mcache)](https://github.com/marirs/mcache/blob/master/LICENSE)
![PyPI - Status](https://img.shields.io/pypi/status/mcache)

A python package to use a async ready decorator for caching outputs.

#### Currently supported cache stores:
- Filecache
- Memcached

#### Requirements
- memcached 
  
On osx
```bash
brew install memcached
brew services start memcached
```
  
On Linux
```bash
sudo apt-get -y install memcached libmemcached-tools
sudo systemctl enable memcached
sudo systemctl start memcached
```

#### Installing the package

```bash
pip install mcache
```

#### Using it in your application

```python
from mcache import filecache, DAY

@filecache(lifetime=DAY*2)
def add(x):
    return x+4 

print(add(10))
```

Async
```python
import asyncio
from mcache import filecache, DAY

@filecache(lifetime=DAY*2)
async def add(x):
    return x+4 

print(asyncio.run(add(10)))
```

---
Sriram
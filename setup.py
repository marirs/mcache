"""
mcache
---------
Multi Caching library, and use as a decorator.
Async Ready
Source code is hosted on `GitHub <https://github.com/marirs/mcache>`
Contributions are welcome!
"""
from setuptools import find_packages, setup

keywords = [
    'Python 3', 'caching', 'memcache', 'filecache', 'redis', 'async',
    'asyncio', 'cache'
]

tests_require = [
    'coverage>=4.5',
    'codecov>=2.1.7',
    'pytest>=5.2',
    'pytest-async>=0.1.1',
    'pytest-asyncio>=0.14.0',
    'pytest-cov>=2.8',
]

extras_require = {
    'tests': tests_require,
}

extras_require['all'] = [req for exts, reqs in extras_require.items()
                         for req in reqs]

setup_requires = [
    'pytest-runner>=5.2',
]

with open('README.md') as f:
    long_description = f.read()

install_requires = [
    'pymemcache>=3.2.0'
]

setup(
    name='mcache',
    version='1.0.0',
    description='Async ready Multi Caching Library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sriram G',
    author_email='marirs@gmail.com',
    license='MIT',
    url='https://github.com/marirs/mcache/',
    zip_safe=False,
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    keywords=keywords,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Operating System :: MacOS :: MacOS X",
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)
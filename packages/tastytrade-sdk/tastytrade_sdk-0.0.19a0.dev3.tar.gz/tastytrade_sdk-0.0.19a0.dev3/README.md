[![Read the Docs (version)](https://img.shields.io/readthedocs/tastytrade-sdk/latest)](https://tastytrade-sdk.readthedocs.io/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tastytrade-sdk)](https://pypi.org/project/tastytrade-sdk/)
[![PyPI - License](https://img.shields.io/pypi/l/tastytrade-sdk)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# tastytrade-sdk-python

A python wrapper around the [tastytrade open API](https://developer.tastytrade.com/)

## Getting Started

### Install
```shell
pip install tastytrade-sdk
```

### Use It
```python
from tastytrade_sdk import Tastytrade

tastytrade = Tastytrade()

tastytrade.login(
    username='jane.doe@email.com',
    password='password'
)

tastytrade.instruments.get_active_equities()
```


## Read the Docs
https://tastytrade-sdk.readthedocs.io/
# WxPusher

[![PyPI version](https://badge.fury.io/py/wxpusher.svg)](https://badge.fury.io/py/wxpusher)
[![PyPI license](https://img.shields.io/pypi/l/wxpusher.svg)](https://pypi.python.org/pypi/wxpusher/)
[![Python Versions](https://img.shields.io/pypi/pyversions/wxpusher.svg)](https://pypi.python.org/pypi/wxpusher/)
[![Downloads](https://pepy.tech/badge/wxpusher)](https://pepy.tech/project/wxpusher)

WxPusher Python SDK.

*Read this in other languages: [English](README-en.md), [简体中文](README.md).*

## Getting Started

### Installation

```shell
pip install -U wxpusher
```

### Usage

```python
from wxpusher import WxPusher
WxPusher.send_message('<content>',
                      uids=['<uids>'],
                      topic_ids=['<topic_ids>'],
                      token='<appToken>')
WxPusher.query_message('<messageId>')
WxPusher.create_qrcode('<extra>', '<validTime>', '<appToken>')
WxPusher.query_user('<page>', '<page_size>', '<appToken>')
```

## Running the tests

### Setup configuration

Configuration is necessary since the tests depend on VALID `appToken` and `uids`.

Frist, copy the configuration sample `config.sample.py` under `wxpusher/tests/` to `config.py`

```shell
cd wxpusher/tests
cp config.sample.py config.py
```

Then, fill in the corresponding information in `config.py`.

### Trigger the tests

With proper configuration, you can run the tests with tox

```shell
tox
```

or nose directly

```shell
nosetests
```

## TODO

- [x] Basic structure with PyPI uploaded.
- [x] Send Message.
- [x] Query Message.
- [x] Create QRCode.
- [x] Query User.
- [ ] More client validators.
- [ ] Command line scripts.
- [ ] Better documentation.
- [ ] More robust unittest.

## Contribution

- Comments or suggestions via github issues.
- Pull requests are welcome absolutely.

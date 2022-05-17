# WxPusher

[![PyPI version](https://badge.fury.io/py/wxpusher.svg)](https://badge.fury.io/py/wxpusher)
[![PyPI license](https://img.shields.io/pypi/l/wxpusher.svg)](https://pypi.python.org/pypi/wxpusher/)
[![Python Versions](https://img.shields.io/pypi/pyversions/wxpusher.svg)](https://pypi.python.org/pypi/wxpusher/)
[![Downloads](https://pepy.tech/badge/wxpusher)](https://pepy.tech/project/wxpusher)

WxPusher Python SDK.

*其他语言版本: [English](README-en.md), [简体中文](README.md).*

## 入门指南

### 安装

```shell
pip install -U wxpusher
```

### 使用

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

## 运行测试

### 配置

运行测试需要配置好 `appToken` 和 `uids`。

首先，将 `wxpusher/tests/` 文件夹下的配置样例 `config.sample.py` 复制并命名为 `config.py`。

```shell
cd wxpusher/tests
cp config.sample.py config.py
```

然后，填写 `config.py` 中的相应信息。

### 启动测试

配置好后就可以使用 `tox` 来运行测试了。

```shell
tox
```

或者直接使用 `nose` 也可以

```shell
nosetests
```

## TODO

- [x] 基本架构并上传到 PyPI
- [x] 发送消息.
- [x] 查询消息.
- [x] 创建二维码.
- [x] 查询用户.
- [ ] 更完备的客户端验证.
- [ ] 命令行脚本.
- [ ] 更完善的文档.
- [ ] 更完备的单元测试.

## 贡献

- 通过 Github Issues 提交评论或建议。
- 直接提交 Pull Requests 必须没问题。

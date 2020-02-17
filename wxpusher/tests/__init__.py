#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Init for unittest.

File: __init__.py
Author: huxuan
Email: i(at)huxuan.org
"""
from . import exceptions

try:
    from . import config
except ImportError:
    raise exceptions.WxPusherTestNoConfigException

__all__ = ['config']

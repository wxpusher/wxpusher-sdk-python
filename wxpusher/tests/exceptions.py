#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom exceptions for unittest.

File: exceptions.py
Author: huxuan
Email: i(at)huxuan.org
"""
from wxpusher import WxPusherException


class WxPusherTestNoConfigException(WxPusherException):
    """Raised when no unittest configuration exists."""

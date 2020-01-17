#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: test_send_message.py
Author: huxuan
Email: i(at)huxuan.org
Description: Unittest for sending message.
"""
import unittest

from wxpusher import WxPusher

from . import config


class TestSendMessage(unittest.TestCase):
    """Unittest for sending message."""

    @classmethod
    def setUpClass(cls):
        WxPusher.default_token = config.TOKEN

    def test_send_message(self):
        """Positive case for sending message."""
        res = WxPusher.send_message(
            self.test_send_message.__doc__,
            config.UIDS,
            url='http://example.com/'
        )
        self.assertIsInstance(res, dict)
        self.assertIn('code', res)
        self.assertEqual(1000, res['code'])

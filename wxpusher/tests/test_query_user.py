#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittest for querying user.

File: test_send_message.py
Author: huxuan
Email: i(at)huxuan.org
"""
import random
import unittest

from wxpusher import WxPusher

from . import config


class TestSendMessage(unittest.TestCase):
    """Unittest for querying user."""

    @classmethod
    def setUpClass(cls):
        """Set up for class."""
        WxPusher.default_token = config.TOKEN

    def test_query_user(self):
        """Positive case for querying user."""
        res = WxPusher.query_user(
            1, random.randint(1, 99),
        )
        self.assertIsInstance(res, dict)
        self.assertIn('code', res)
        self.assertEqual(1000, res['code'])

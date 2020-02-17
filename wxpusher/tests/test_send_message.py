#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittest for sending message.

File: test_send_message.py
Author: huxuan
Email: i(at)huxuan.org
"""
import unittest

from wxpusher import WxPusher

from . import config


class TestSendMessage(unittest.TestCase):
    """Unittest for sending message."""

    @classmethod
    def setUpClass(cls):
        """Set up for class."""
        WxPusher.default_token = config.TOKEN

    def test_send_message_uid(self):
        """Positive case for sending message with uid."""
        res = WxPusher.send_message(
            self.test_send_message_uid.__doc__,
            uids=config.UIDS,
            url='http://example.com/',
        )
        self.assertIsInstance(res, dict)
        self.assertIn('code', res)
        self.assertEqual(1000, res['code'])

    def test_send_message_topic_id(self):
        """Positive case for sending message with topic_id."""
        res = WxPusher.send_message(
            self.test_send_message_topic_id.__doc__,
            topic_ids=config.TOPIC_IDS,
            url='http://example.com/',
        )
        self.assertIsInstance(res, dict)
        self.assertIn('code', res)
        self.assertEqual(1000, res['code'])

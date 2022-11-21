#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WxPusher Python SDK.

File: wxpusher.py
Author: huxuan
Email: i(at)huxuan.org
"""
import requests

from . import exceptions

BASEURL = 'http://wxpusher.zjiecode.com/api'


class WxPusher():
    """WxPusher Python SDK."""

    default_token = None

    @classmethod
    def send_message(cls, content, **kwargs):
        """Send Message."""
        payload = {
            'appToken': cls._get_token(kwargs.get('token')),
            'content': content,
            'summary': kwargs.get('summary'),
            'contentType': kwargs.get('content_type', 1),
            'topicIds': kwargs.get('topic_ids', []),
            'uids': kwargs.get('uids', []),
            'verifyPay': kwargs.get('verify'),
            'url': kwargs.get('url'),
        }
        url = f'{BASEURL}/send/message'
        return requests.post(url, json=payload).json()

    @classmethod
    def query_message(cls, message_id):
        """Query message status."""
        url = f'{BASEURL}/send/query/{message_id}'
        return requests.get(url).json()

    @classmethod
    def create_qrcode(cls, extra, valid_time=1800, token=None):
        """Create qrcode with extra callback information."""
        payload = {
            'appToken': cls._get_token(token),
            'extra': extra,
            'validTime': valid_time,
        }
        url = f'{BASEURL}/fun/create/qrcode'
        return requests.post(url, json=payload).json()

    @classmethod
    def query_user(cls, page, page_size, token=None):
        """Query users."""
        payload = {
            'appToken': cls._get_token(token),
            'page': page,
            'pageSize': page_size,
        }
        url = f'{BASEURL}/fun/wxuser'
        return requests.get(url, params=payload).json()

    @classmethod
    def _get_token(cls, token=None):
        """Get token with validation."""
        token = token or cls.default_token
        if not token:
            raise exceptions.WxPusherNoneTokenException()
        return token

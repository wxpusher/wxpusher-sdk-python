#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python packaging for wxpusher.

File: setup.py
Author: huxuan
Email: i(at)huxuan.org
"""
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution

from setuptools import setup

NAME = 'wxpusher'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities',
]

INSTALL_REQUIRES = [
    'requests',
]

DESCRIPTION = (
    'WxPusher Python SDK.'
)

KEYWORDS = [
    'wxpusher',
    'wechat',
    'weixin',
    'notification',
    'push-notification',
    'python-sdk',
]

try:
    VERSION = f'v{get_distribution(NAME).version}'
except DistributionNotFound:
    VERSION = 'master'

PROJECT_URL = 'https://github.com/wxpusher/wxpusher-sdk-python'
BASE_URL = f'{PROJECT_URL}/blob/{VERSION}'


def readme():
    """Parse README for long_description."""
    content = open('README.md').read()
    content = content.replace('README.md', f'{BASE_URL}/README.md', 1)
    content = content.replace('README-en.md', f'{BASE_URL}/README-en.md', 1)
    return content


setup(name=NAME,
      description=DESCRIPTION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=CLASSIFIERS,
      keywords=' '.join(KEYWORDS),
      url=PROJECT_URL,
      author='Xuan (Sean) Hu',
      author_email='i+wxpusher@huxuan.org',
      license='Apache License 2.0',
      packages=['wxpusher'],
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      install_requires=INSTALL_REQUIRES,
      python_requires='>=3',
      include_package_data=True)

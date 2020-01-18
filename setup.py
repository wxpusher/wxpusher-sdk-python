#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: setup.py
Author: huxuan
Email: i(at)huxuan.org
Description: Python packaging for wxpusher.
"""
from setuptools import setup

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Utilities'
]

INSTALL_REQUIRES = [
    'requests'
]

DEV_REQUIRES = [
    'pycodestyle',
    'pyflakes',
    'pylint'
]

TEST_REQUIRES = [
    'coverage',
    'nose'
]

EXTRAS_REQUIRE = {
    'dev': DEV_REQUIRES,
    'test': TEST_REQUIRES
}

DESCRIPTION = (
    'WxPusher Python SDK.'
)

VERSION = open('VERSION').read().strip()
PROJECT_URL = 'https://github.com/wxpusher/wxpusher-sdk-python'
BASE_URL = f'{PROJECT_URL}/blob/v{VERSION}'


def readme():
    """Parse README for long_description."""
    content = open('README.md').read()
    content = content.replace('README.md', f'{BASE_URL}/README.md', 1)
    content = content.replace('README-en.md', f'{BASE_URL}/README-en.md', 1)
    return content


setup(name='wxpusher',
      version=VERSION,
      description=DESCRIPTION,
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=CLASSIFIERS,
      keywords='wxpusher wechat push-notification',
      url='https://github.com/wxpusher/wxpusher-sdk-python',
      author='Xuan (Sean) Hu',
      author_email='i+wxpusher@huxuan.org',
      license='Apache License 2.0',
      packages=['wxpusher'],
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      python_requires='>=3',
      include_package_data=True)

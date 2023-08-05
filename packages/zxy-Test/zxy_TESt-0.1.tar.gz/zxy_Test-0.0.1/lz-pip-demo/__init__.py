# coding: utf-8

"""pip-demo codes. 测试pip发包.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

from .__version__ import __version__  # NOQA
from .client import Client

__author__ = 'liuzhe.inf <liuzhe.inf@bytedance.com>'

__all__ = ['Client']

# coding: utf-8

"""TODO: 增加模块级注释"""

from __future__ import absolute_import, division, print_function, unicode_literals

import six


@six.python_2_unicode_compatible
class Client(object):
    def __init__(self, url=None):
        """
        :param url: target url for this client
        :type url: str
        """
        self.url = url or 'http://localhost:1234'

    def add(self, x, y):
        """
        Caculate sum of input.

        :param x: first input for caculate
        :type x: int
        :param y: second input for caculate
        :type y: int
        :rtype: int
        """
        return x + y

    def __str__(self):
        return '<client for {}>'.format(self.url)

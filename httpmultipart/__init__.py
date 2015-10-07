# -*- coding:utf-8 -*-
"""
httpmultipart
~~~~~~~~~~~~~~~
This is a small tool for post multipart requests;

Homepage:
    https://github.com/tao12345666333/httpmultipart
"""

__title__ = 'httpmultipart'
__author__ = 'TaoBeier'
__version__ = '0.1.0'
__license__ = 'GPL'
__copyright__ = 'Copyright 2015 TaoBeier'


import logging
from logging import NullHandler
from .main import PostMultipart

logging.getLogger(__name__).addHandler(NullHandler())

# -*- coding: utf-8 -*-
"""
Stream Sender
author: niub
email: niub@jzkjgroup.com
"""
import os
import sys

# 软件版本信息
VERSION = "v0.0.0000"
RUNTIMEENV = None
LOGLEVEL = 2

ROOT_PATH = os.getcwd()
if getattr(sys, 'frozen', False):
    BUNDLE_DIR = sys._MEIPASS
    RUNTIMEENV = "pyinstaller"
else:
    BUNDLE_DIR = os.path.dirname(os.path.abspath(__file__))

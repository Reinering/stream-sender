# -*- coding: utf-8 -*-
"""
Stream Sender
author: niub
email: niub@jzkjgroup.com
"""
import os
import sys

# 软件版本信息
VERSION = "v0.0.01"RUNTIMEENV = None
LOGLEVEL = 2



ROOT_PATH = os.getcwd()
if getattr(sys, 'frozen', False):
    BUNDLE_DIR = sys._MEIPASS
    RUNTIMEENV = "pyinstaller"
else:
    BUNDLE_DIR = os.path.dirname(os.path.abspath(__file__))


TASKLIST_CONFIG = {}
"""
For Example
TASKLIST_CONFIG = {
    "1": {
        "playlist": [],
        "protocol": '',
        "dst_ip": '',
        "dst_port": '',
        “src_ip": '',
        "send_mode": '',
        "out_video_format"'": '',
        "state": True,
        "current_index" 0,
        "thread": None
    }
}
"""
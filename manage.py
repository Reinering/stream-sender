# -*- coding: utf-8 -*-
"""
Stream Sender
author: niub
email: niub@jzkjgroup.com
"""
import os
import sys

# 软件版本信息
VERSION = "v0.1.00"PackageTime = "202109031554"RUNTIMEENV = None
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
        "playlist": [
            {
                "videoFile": '',
                "subtitleFile": '',
                "setting": {
                  "volume": ["dB", "12.1", "增大"],
                  "subtitle": {"addMode": ''}
                },
                "inputs": '',
                "outputs": '',
                "globalputs": '',
                
            }
        ],
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

# ffmpeg config
FFMPEG_OPTIONS_DEFAULT = {
    "inputs": '-re',
    "outputs": '-c copy',       # 等于 -vcodec copy -acodec copy
    "globalputs": '',
}

FFMPEG_ERRORS = [
    'Conversion failed!',
    "Protocol not found",
    "Filtering and streamcopy cannot be used together",
    "Invalid argument",
    "I/O error",
    "is not a suitable output format",
    "Option not found",
    "Bitstream filter not found"
]
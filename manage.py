# -*- coding: utf-8 -*-
"""
Stream Sender
author: Reiner New
email: nbxlhc@hotmail.com
"""
import os
import sys

# 软件版本信息
VERSION = "v0.1.00"PackageTime = "202209032337"RUNTIMEENV = None
LOGLEVEL = 4


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
                  "audio": {"coding": '', "volume": ["dB", "12.1", "增大"]},
                  "video": {"scale": '', "resolution": '', "bitrate": ''},
                  "subtitle": {"addMode": ''}
                },
                videoInfo:'',
                "inputs": '',
                "outputs": '',
                "globalputs": ''
                
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

playConfig = {
    "streams": [
        {
            "info": '',
            "": ''
        }
    ],
    "videoFile": '',
    "subtitleFile": '',
    "setting": {
        "audio": {"coding": '', "volume": ["dB", "12.1", "增大"]},
        "video": {"scale": '', "resolution": '', "bitrate": ''},
        "subtitle": {"addMode": ''}
    },
    "videoInfo": '',
    "inputs": '',
    "outputs": '',
    "globalputs": '',
    "type": "2"
}


# ffmpeg config
FFMPEG_OPTIONS_DEFAULT = {
    "inputs": '-re',
    "outputs": '-c copy',       # 等于 -vcodec copy -acodec copy
    "globalputs": '',
    "urlputs": ''
}

FFMPEG_ERRORS = [
    'Conversion failed!',
    "Protocol not found",
    "Filtering and streamcopy cannot be used together",
    "Invalid argument",
    "I/O error",
    "is not a suitable output format",
    "Option not found",
    "Bitstream filter not found",
    "Invalid data found when processing input",
    "EBML header parsing failed",
    "Error reading log file"
    "'utf-8' codec can't decode byte 0xb3 in position 0: invalid start byte"
]
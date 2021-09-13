# -*- coding: utf-8 -*-

"""
Module implementing SettingDialog.
"""

import subprocess
import ffmpy3
from manage import FFMPEG_ERRORS


def checkVideo(file):
    ff = ffmpy3.FFprobe(inputs={file: None},
                        global_options="-v quiet -print_format json -show_format -show_streams")
    return ff.run(stdout=subprocess.PIPE)


def checkOutputErr(p0):
    for err in FFMPEG_ERRORS:
        if err in p0:
            return True
    return False
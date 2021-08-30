# -*- coding: utf-8 -*-

"""
Module implementing SettingDialog.
"""

import subprocess
import ffmpy3


def checkVideo(file):
    ff = ffmpy3.FFprobe(inputs={file: None},
                        global_options="-v quiet -print_format json -show_format -show_streams")
    return ff.run(stdout=subprocess.PIPE)

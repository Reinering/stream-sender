# -*- coding: utf-8 -*-

"""
Module implementing.
author: Reiner New
email: nbxlhc@hotmail.com
"""

import subprocess
import ffmpy3
import re
import logging


def getFileVolume(file):
    try:
        ff = ffmpy3.FFmpeg(inputs={file: None},
                           global_options="-filter_complex volumedetect -c:v copy -f null /dev/null")
        stderr = ff.run(stderr=subprocess.PIPE)
        logging.debug(stderr)
        if stderr[-1]:
            result = re.findall(r'mean_volume: ([-.\d]*) dB', str(stderr[-1]))
            return result[0]
    except ffmpy3.FFExecutableNotFoundError as e:
        print("错误", "文件中音频音量识别失败", e)

    return
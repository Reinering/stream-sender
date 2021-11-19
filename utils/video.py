# -*- coding: utf-8 -*-

"""
Module implementing SettingDialog.
"""

import subprocess
import ffmpy3
import simplejson
from manage import FFMPEG_ERRORS
import logging


def checkVideo(file):
    ff = ffmpy3.FFprobe(inputs={file: None},
                        global_options="-v quiet -print_format json -show_format -show_streams")
    return ff.run(stdout=subprocess.PIPE)


def checkOutputErr(p0):
    for err in FFMPEG_ERRORS:
        if err in p0:
            return True
    return False

def calcScale(config):
    if not config.__contains__("videoInfo") or not config["videoInfo"]:
        try:
            fileInfo = checkVideo(config["videoFile"])[0]
            config["videoInfo"] = simplejson.loads(fileInfo)
        except Exception as e:
            logging.error(e)
            return

    width = int(config["videoInfo"]["streams"][0]["coded_width"])
    height = int(config["videoInfo"]["streams"][0]["coded_height"])

    # [w, h, [lw, rw], [th, bh]
    out = []

    if config["setting"]["video"].__contains__("scale"):
        try:
            tmp = config["setting"]["video"]["scale"].split(':')
            if len(tmp) != 2:
                return
            scale = int(tmp[0])/int(tmp[1])
            if width/height < scale:
                widthTmp = height * scale
                bw = abs(width - widthTmp)
                out = [width, height, bw, 0]
            elif width / height > scale:
                heightTmp = width / scale
                bh = abs(heightTmp - height)
                out = [width, height, 0, bh]
            else:
                out = [width, height, 0, 0]
        except Exception as e:
            logging.error(e)
            return

    if config["setting"]["video"].__contains__("resolution"):
        resolution = config["setting"]["video"]["resolution"]
        heightTmp = 0
        if resolution == "4K":
            heightTmp = 1080
        elif resolution == "2K":
            heightTmp = 1080
        if resolution == "1080P":
            heightTmp = 1080
        elif resolution == "720P":
            heightTmp = 720

        if heightTmp:
            if out:
                scale = heightTmp / out[1]
                out = [out[0] * scale, heightTmp, out[2] * scale, out[3] * scale]
            else:
                scale = heightTmp / height
                out = [width * scale, heightTmp, 0, 0]

    # return "-vf scale={}x{},pad={}:{}:{}:{}:black".format(int(out[0] - out[2]), int(out[1] - out[3]), int(out[0]), int(out[1]), int(out[2]/2), int(out[3]/2))
    if out:
        result = {}
        if out[0] != width or out[1] != height:
            result["scale"] = "{}x{}".format(int(out[0] - out[2]), int(out[1] - out[3]))
        if out[2] != 0 or out[3] != 0:
            result["pad"] = "{}:{}:{}:{}:black".format(int(out[0]), int(out[1]), int(out[2]/2), int(out[3]/2))

        if result:
            return result
        else:
            return
    else:
        return



if __name__ == "__main__":

    config = {
        "setting": {
            "video": {
                "scale": "16:9",
                "resolution": "1080P"
            }
        },
        "videoInfo": {
            "streams": [
                {
                    "coded_width": 1920,
                    "coded_height": 804,
                }
            ]
        }
    }
    print(calcScale(config))


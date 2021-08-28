# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSignal, QThread
import subprocess
import ffmpy3
import asyncio
import re
import time
import sys
import logging

from manage import FFMPEG_ERRORS


def checkOutputErr(p0):
    for err in FFMPEG_ERRORS:
        if err in p0:
            return True
    return False


# Coroutine
class FfmpegCorThread(QThread):

    signal_state = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(FfmpegCorThread, self).__init__(parent)
        self.stopBool = False
        self.loop = asyncio.new_event_loop()
        self.processList = {}       # {row: {ff: ffprocess, stopBool: False, stopCode: 0}}
        self.resultRE = r'frame=[ ]*(\d*) fps=[ ]*([.\d]*) q=([-.\d]*) size=[ ]*([\d]*kB) time=(\d{2}:\d{2}:\d{2}.\d{2}) bitrate=[ ]*([.\d]*kbits/s) speed=[ ]*([.\d]*x)'

    def stop(self):
        print("结束线程", self.loop.is_running())
        self.stopBool = True
        try:
            for key, value in self.processList.items():
                self.stopCoroutine(key)
            self.processList.clear()
            self.loop.stop()
            print(self.loop.is_running())
        except Exception as e:
            print(e)

    def stopCoroutine(self, row):
        self.processList[row]["stopCode"] = 0
        self.processList[row]["stopBool"] = True
        self.killFF(row)

    def pauseCoroutine(self, row):
        self.processList[row]["stopCode"] = 2
        self.processList[row]["stopBool"] = True
        self.killFF(row)

    def next(self, row):
        self.killFF(row)

    def killFF(self, row):
        print("结束协程", row)
        try:
            pid = self.processList[row]["ff"].process.pid
            print("pid", pid)
            cmd = "taskkill /pid {} -t -f".format(str(pid))
            pp = subprocess.Popen(args=cmd,
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  shell=True)
            # out = str(pp.stdout.read(), encoding="utf-8")
            # print('out:', out)
        except Exception as e:
            print(e)

    def run(self):
        try:
            asyncio.set_event_loop(self.loop)
            self.loop.run_forever()
        except Exception as e:
            print(e)
        finally:
            self.loop.close()

    def addCoroutine(self, row, CONFIG):
        self.row = row
        self.config = CONFIG
        self.processList[row] = {"stopBool": False, "stopCode": 0}
        asyncio.run_coroutine_threadsafe(self.sendCoroutine(row, CONFIG), self.loop)

    async def sendCoroutine(self, row, config):
        self.signal_state.emit((row, 1))

        loopType = True

        while not self.processList[row]["stopBool"] and loopType:
            if config["send_mode"] == "单次":
                loopType = False

            i = config["current_index"]
            loopBool = False
            while not self.processList[row]["stopBool"] and i < len(config["playlist"]):
                self.signal_state.emit((row, config["playlist"][i]["videoFile"].split('/')[-1]))

                ff = self.send(config)
                await ff.run_async(stderr=asyncio.subprocess.PIPE)
                self.processList[row]["ff"] = ff

                line_buf = bytearray()
                while not self.processList[row]["stopBool"]:
                    in_buf = (await ff.process.stderr.read(128)).replace(b'\r', b'\n')
                    if not in_buf:
                        break
                    line_buf.extend(in_buf)
                    while b'\n' in line_buf:
                        line, _, line_buf = line_buf.partition(b'\n')
                        line = str(line)
                        print(line, file=sys.stderr)

                        if checkOutputErr(line):
                            loopBool = True
                            break
                        else:
                            result = re.findall(self.resultRE, line)
                            if result:
                                self.signal_state.emit((row, result[0]))

                print("mark", self.processList[row]["stopBool"])
                if not self.processList[row]["stopBool"]:
                    i += 1
                    config["current_index"] = i
                # elif not loopBool:
                #     await ff.wait()

            config["current_index"] = 0
            if loopBool:
                loopType = False

        self.signal_state.emit((row, self.processList[row]["stopCode"]))

    def send(self, config):
        inputs = {}
        outputs = {}
        globalputs = None

        file = config["playlist"][config["current_index"]]["videoFile"]

        inParams = ''
        # inputs
        if config["playlist"][config["current_index"]].__contains__("inputs") \
                and config["playlist"][config["current_index"]]["inputs"]:
            inParams = inParams + ' ' + config["playlist"][config["current_index"]]["inputs"]

        outParams = ''
        if config["protocol"] != "UDP" and config["protocol"] != "RTP" and config["protocol"] != "RTMP":
            logging.critical("协议匹配错误")
            return

        outurl = '{}://{}:{}{}'.format(config["protocol"].lower(),
                                       config["dst_ip"],
                                       str(config["dst_port"]),
                                       config["uri"])

        # subtitle
        if config["playlist"][config["current_index"]].__contains__("subtitleFile") \
                and config["playlist"][config["current_index"]]["subtitleFile"]:
            subtitle = config["playlist"][config["current_index"]]["subtitleFile"]
            if subtitle.split('.')[-1].upper() == "SRT":
                # outParams += ' -vf subtitles={}'.format(subtitle)
                inputs[subtitle] = None

        # outputs
        if config["playlist"][config["current_index"]].__contains__("outputs") \
                and config["playlist"][config["current_index"]]["outputs"]:
            outParams = outParams + ' ' + config["playlist"][config["current_index"]]["outputs"]

        # out_video_format
        if config["out_video_format"] == "MP4":
            outParams += ' -f mpeg4'
        elif config["out_video_format"] == "TS":
            outParams += ' -f mpegts'

        # globalputs
        if config["playlist"][config["current_index"]].__contains__("globalputs") \
                and config["playlist"][config["current_index"]]["globalputs"]:
            globalputs.append(config["playlist"][config["current_index"]]["globalputs"])
        else:
            globalputs = None

        inputs[file] = inParams
        outputs[outurl] = outParams

        ff = ffmpy3.FFmpeg(inputs=inputs,
                           outputs=outputs,
                           global_options=globalputs)
        print("cmd: ", ff.cmd, '\n')
        return ff

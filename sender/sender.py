# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSignal, QThread
import subprocess
import ffmpy3
import asyncio
import re
import shutil
import sys
import os
import logging

from manage import ROOT_PATH, BUNDLE_DIR
from utils.file import modifyFileCode
from utils.video import calcScale, checkOutputErr


# Coroutine
class FfmpegCorThread(QThread):

    signal_state = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(FfmpegCorThread, self).__init__(parent)
        self.subDir = None
        self.stopBool = False
        self.loop = asyncio.new_event_loop()
        self.processList = {}       # {row: {ff: ffprocess, stopBool: False, stopCode: 0, "subtitleFile": '', mvBool: False, }}
        self.resultRE = r'frame=[ ]*(\d*) fps=[ ]*([.\d]*) q=([-.\d]*) size=[ ]*([\d]*kB) time=(\d{2}:\d{2}:\d{2}.\d{2}) bitrate=[ ]*([.\d]*kbits/s) speed=[ ]*([.\d]*x)'

    def setParams(self, **kwargs):
        if kwargs.__contains__("subDir"):
            self.subDir = kwargs["subDir"]

    def stop(self):
        print("结束线程", self.loop.is_running())
        self.stopBool = True
        try:
            for key, value in self.processList.items():
                self.stopCoroutine(key)
            self.processList.clear()
            self.loop.stop()
            shutil.rmtree("subs")
        except Exception as e:
            print(e)

    def run(self):
        try:
            if not os.path.exists(self.subDir):
                os.makedirs(self.subDir)

            asyncio.set_event_loop(self.loop)
            self.loop.run_forever()
        except Exception as e:
            print(e)
        finally:
            self.loop.close()

    def stopCoroutine(self, row):
        print("结束协程", row)
        if not self.processList.__contains__(row):
            return
        self.processList[row]["stopCode"] = 0
        self.processList[row]["stopBool"] = True
        self.killFFByRow(row)

    def pauseCoroutine(self, row):
        if not self.processList.__contains__(row):
            return
        self.processList[row]["stopCode"] = 2
        self.processList[row]["stopBool"] = True
        self.killFFByRow(row)

    def next(self, row):
        self.processList[row]["mvCode"] = 1
        self.processList[row]["mvBool"] = True
        self.killFFByRow(row)

    def previous(self, row):
        self.processList[row]["mvCode"] = 0
        self.processList[row]["mvBool"] = True
        self.killFFByRow(row)

    def killFFByRow(self, row):
        if self.processList[row].__contains__("ff"):
            self.killFFByP(self.processList[row]["ff"])

    def killFFByP(self, ff):
        try:
            pid = ff.process.pid
            cmd = "taskkill /pid {} -t -f".format(str(pid))
            pp = subprocess.Popen(args=cmd,
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  shell=True)
            out = str(pp.stdout.read(), encoding="utf-8")
            print('out:', out)
        except Exception as e:
            print(e)

    def addCoroutine(self, row, CONFIG):
        self.row = row
        self.config = CONFIG
        if self.processList.__contains__(row):
            self.processList[row]["stopBool"] = False
            self.processList[row]["stopCode"] = 0
        else:
            self.processList[row] = {"stopBool": False, "stopCode": 0, "mvCode": 0, "mvBool": False}
        asyncio.run_coroutine_threadsafe(self.sendCoroutine(row, CONFIG), self.loop)

    async def sendCoroutine(self, row, config):
        loopType = True

        while not self.processList[row]["stopBool"] and loopType:
            if config["send_mode"] == "单次":
                loopType = False

            i = config["current_index"]
            loopBool = False
            while not self.processList[row]["stopBool"] and i < len(config["playlist"]):
                self.signal_state.emit((row, config["playlist"][i]["videoFile"].split('/')[-1]))

                # subtitle file
                if config["playlist"][i].__contains__("subtitleFile"):
                    if os.path.exists(config["playlist"][i]["subtitleFile"]):
                        if not self.processList[row].__contains__("subtitleFile") or not os.path.exists(self.processList[row]["subtitleFile"]):
                            subName = os.path.join(self.subDir, "{}_{}{}".format(row, i, '')).replace('\\', '/')
                            if not os.path.exists(subName):
                                modifyFileCode(config["playlist"][i]["subtitleFile"], subName, "utf-8")
                            self.processList[row]["subtitleFile"] = subName
                    else:
                        logging.error("字幕文件 {} 不存在".format(config["playlist"][i]["subtitleFile"]))

                ff = self.createFFmpy3(row, config)
                await ff.run_async(stderr=asyncio.subprocess.PIPE)
                self.processList[row]["ff"] = ff
                self.signal_state.emit((row, 1))

                line_buf = bytearray()
                while not self.processList[row]["stopBool"]:
                    in_buf = (await ff.process.stderr.read(128)).replace(b'\r', b'\n')
                    if not in_buf:
                        break
                    line_buf.extend(in_buf)
                    while b'\n' in line_buf:
                        line, _, line_buf = line_buf.partition(b'\n')
                        print(line, file=sys.stderr)
                        if not line:
                            continue
                        line = str(line)
                        if checkOutputErr(line):
                            loopBool = True
                            break
                        else:
                            result = re.findall(self.resultRE, line)
                            if result:
                                self.signal_state.emit((row, result[0]))

                if not self.processList[row]["stopBool"]:
                    if self.processList[row]["mvBool"]:
                        self.processList[row]["mvBool"] = False
                        if self.processList[row]["mvCode"]:
                            i += 1
                        else:
                            i -= 1
                    else:
                        i += 1
                        if not loopBool:
                            await ff.wait()
                        self.killFFByP(ff)
                    config["current_index"] = i

            if not self.processList[row]["stopBool"]:
                config["current_index"] = 0
                if loopBool:
                    loopType = False

        self.signal_state.emit((row, self.processList[row]["stopCode"]))

    def createFFmpy3(self, row, config):
        inputs = {}
        outputs = {}
        globalputs = []
        vfs = {}

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
            if config["playlist"][config["current_index"]]["setting"]["subtitle"]["addMode"] == 0:
                inputs[self.processList[row]["subtitleFile"]] = None
            elif config["playlist"][config["current_index"]]["setting"]["subtitle"]["addMode"] == 1:
                if subtitle.split('.')[-1].upper() == "SRT":
                    vfs["subtitles"] = self.processList[row]["subtitleFile"].replace("\\", "/")
                    # outParams = outParams + ' -vf subtitles={}'.format(self.processList[row]["subtitleFile"].replace("\\", "/"))
                elif subtitle.split('.')[-1].upper() == "ASS":
                    # outParams = outParams + ' -vf "ass={}"'.format(self.processList[row]["subtitleFile"].replace("\\", "/"))
                    vfs["ass"] = self.processList[row]["subtitleFile"].replace("\\", "/")

        # outputs
        if config["playlist"][config["current_index"]].__contains__("outputs") \
                and config["playlist"][config["current_index"]]["outputs"]:
            outParams = outParams + ' ' + config["playlist"][config["current_index"]]["outputs"]

        # video setting
        if config["playlist"][config["current_index"]].__contains__("setting") \
            and config["playlist"][config["current_index"]]["setting"].__contains__("video") \
                and config["playlist"][config["current_index"]]["setting"]["video"]:

            # video scale
            out = calcScale(config["playlist"][config["current_index"]])
            if out:
                # outParams = outParams + ' ' + out
                vfs.update(out)

            # video bitrate
            if config["playlist"][config["current_index"]]["setting"]["video"].__contains__("bitrate"):
                outParams = outParams + ' -b {}k'.format(config["playlist"][config["current_index"]]["setting"]["video"]["bitrate"])

        # out_video_format

        vfsStr = ''
        for (key, value) in vfs.items():
            vfsStr += "{}={},".format(key, value)
        if vfsStr:
            outParams = outParams + " -vf " + vfsStr[:-1]
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

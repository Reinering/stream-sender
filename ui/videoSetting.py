# -*- coding: utf-8 -*-

"""
Module implementing SettingDialog.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QCloseEvent
import time
import subprocess
import ffmpy3
import re
import sys
import asyncio
import logging

from utils.audio import getFileVolume
from utils.video import checkOutputErr
from manage import FFMPEG_OPTIONS_DEFAULT
from .Ui_videoSetting import Ui_Dialog


class SettingDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    signal_setting = pyqtSignal(tuple)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(SettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.row = None
        self.config = None
        self.tabWidget.setCurrentIndex(0)
        self.doubleSpinBox_dB.setHidden(True)
        self.comboBox_dB_direction.setHidden(True)
        self.plainTextEdit_params_in.setPlainText(FFMPEG_OPTIONS_DEFAULT["inputs"])
        self.plainTextEdit_params_out.setPlainText(FFMPEG_OPTIONS_DEFAULT["outputs"])
        self.plainTextEdit_params_global.setPlainText(FFMPEG_OPTIONS_DEFAULT["globalputs"])

        self.initWidgetTh = InitWidgetThread()
        self.initWidgetTh.send_volume.connect(self.setVolume)

    def setParams(self, row, out_video_format, config):
        self.row = row
        self.out_video_format = out_video_format
        self.config = config
        # self.initWidget()
        self.initWidgetTh.setParams(self, out_video_format, config)
        self.initWidgetTh.start()

    def initWidget(self):
        # if self.config.__contains__("inputs") and self.config["inputs"]:
        #     self.plainTextEdit_params_in.setPlainText(self.config["inputs"])
        #
        # if self.config.__contains__("outputs") and self.config["outputs"]:
        #     self.plainTextEdit_params_out.setPlainText(self.config["outputs"])
        #
        # if self.config.__contains__("globalputs") and self.config["globalputs"]:
        #     self.plainTextEdit_params_global.setPlainText(self.config["globalputs"])
        volume = getFileVolume(self.config["videoFile"])
        if volume:
            self.label_current_volume.setText(volume)

        if not self.config.__contains__("setting") or not self.config["setting"]:
            return

        # 音频设置
        ## 编码设置


        ## 音量设置
        self.comboBox_volume_unit.setCurrentText(self.config["setting"]["audio"]["volume"][0])
        if '%' == self.config["setting"]["audio"]["volume"][0]:
            self.spinBox_volume_percent.setValue(self.config["setting"]["audio"]["volume"][1])
        elif "dB" == self.config["setting"]["audio"]["volume"][0]:
            self.doubleSpinBox_dB.setValue(self.config["setting"]["audio"]["volume"][1])
            self.comboBox_dB_direction.setCurrentText(self.config["setting"]["audio"]["volume"][2])

        # 字幕设置
        if self.out_video_format == "TS" or self.out_video_format == "MP4":
            self.comboBox_sub_addmode.setEnabled(False)
        if self.config.__contains__("subtitleFile") and self.config["subtitleFile"]:
            self.label_sub.setText(self.config["subtitleFile"])
            if self.config["setting"].__contains__("subtitle"):
                if self.config["setting"]["subtitle"].__contains__("addMode"):
                    self.comboBox_sub_addmode.setCurrentIndex(self.config["setting"]["subtitle"]["addMode"])
            else:
                self.comboBox_sub_addmode.setCurrentIndex(1)

        else:
            if self.out_video_format == "TS" or self.out_video_format == "MP4":
                self.comboBox_sub_addmode.setCurrentIndex(1)

        # 视频设置

        ## 图像设置
        if self.config["setting"].__contains__("video"):
            if self.config["setting"]["video"].__contains__("scale"):
                self.comboBox_scale.setCurrentText(self.config["setting"]["video"]["scale"])
            if self.config["setting"]["video"].__contains__("resolution"):
                self.comboBox_resolution.setCurrentText(self.config["setting"]["video"]["resolution"])


    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            self.initWidgetTh.stop()
        except Exception as e:
            print(e)

    def setVolume(self, p0):
        if p0:
            self.label_current_volume.setText(p0)
        # if self.out_video_format == "TS" or self.out_video_format == "MP4":
        #     self.comboBox_sub_addmode.setEnabled(False)

    @pyqtSlot()
    def on_pushButton_sub_add_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            file = QFileDialog.getOpenFileName(self, u"选择字幕文件", "/",
                                                 "subtitle Files(*.srt);;"
                                                 "subtitle Files(*.ssa);;"
                                                 "subtitle Files(*.ass)")
            if file[0]:
                self.label_sub.setText(file[0])
        except Exception as e:
            print(e)

    @pyqtSlot(str)
    def on_comboBox_volume_unit_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if p0 == '%':
            self.spinBox_volume_percent.setHidden(False)
            self.doubleSpinBox_dB.setHidden(True)
            self.comboBox_dB_direction.setHidden(True)
        elif p0 == "dB":
            self.spinBox_volume_percent.setHidden(True)
            self.doubleSpinBox_dB.setHidden(False)
            self.comboBox_dB_direction.setHidden(False)

    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        inputs = self.plainTextEdit_params_in.toPlainText()
        outputs = self.plainTextEdit_params_out.toPlainText()
        globalputs = self.plainTextEdit_params_global.toPlainText()

        if not self.config.__contains__("setting"):
            self.config["setting"] = {}

        # 视频设置
        if not self.config["setting"].__contains__("video"):
            self.config["setting"]["video"] = {}

        ## 码率
        if self.checkBox_video_bitrate.isChecked():
            self.config["setting"]["video"]["bitrate"] = self.spinBox_video_bitrate.value()
        else:
            if self.config["setting"]["video"].__contains__("bitrate"):
                self.config["setting"]["video"].pop("bitrate")

        ## 图像尺寸 scale
        scale = self.comboBox_scale.currentText()

        if scale == "原始":
            if self.config["setting"]["video"].__contains__("scale"):
                self.config["setting"]["video"].pop("scale")
        else:
            self.config["setting"]["video"]["scale"] = scale

        # 图像分辨率 resolution
        resolution = self.comboBox_resolution.currentText()
        if resolution == "原始":
            if self.config["setting"]["video"].__contains__("resolution"):
                self.config["setting"]["video"].pop("resolution")
        else:
            self.config["setting"]["video"]["resolution"] = resolution

        # 音频设置
        if not self.config["setting"].__contains__("audio"):
            self.config["setting"]["audio"] = {}
        ## 音频编码
        audioCoding = self.comboBox_audioCoding.currentText()
        if audioCoding == "原始":
            if self.config["setting"]["audio"].__contains__("coding"):
                self.config["setting"]["audio"].pop("coding")
        else:
            self.config["setting"]["audio"]["coding"] = audioCoding
            if outputs:
                outputs = outputs.replace("-c copy", "-vcodec copy").replace("-acodec copy", "") + ' -acodec ' + audioCoding.lower() + ' '
        ## 音量设置
        self.config["setting"]["audio"]["volume"] = [self.comboBox_volume_unit.currentText()]
        if "%" in self.comboBox_volume_unit.currentText():
            volume = self.spinBox_volume_percent.value()
            self.config["setting"]["audio"]["volume"].append(volume)
            if 100 != self.spinBox_volume_percent.value():
                volume = '-filter:a "volume={}"'.format(str(volume/100))
                if outputs:
                    outputs = volume + ' ' + outputs.replace("-c copy", "-vcodec copy").replace("-acodec copy", "")
                else:
                    outputs = volume
        elif "dB" == self.comboBox_volume_unit.currentText():
            volume = self.doubleSpinBox_dB.value()
            self.config["setting"]["audio"]["volume"].append(volume)
            self.config["setting"]["audio"]["volume"].append(self.comboBox_dB_direction.currentText())

            if 0.00 != self.doubleSpinBox_dB.value():
                if "增大" == self.comboBox_dB_direction.currentText():
                    dB_direction = ''
                elif "减小" == self.comboBox_dB_direction.currentText():
                    dB_direction = '-'

                volume = '-filter:a "volume={}{}dB"'.format(dB_direction, str(volume))
                if outputs:
                    outputs = volume + ' ' + outputs.replace("-c copy", "-vcodec copy").replace("-acodec copy", "")
                else:
                    outputs = volume

        # 字幕设置
        subFile = self.label_sub.text()
        if subFile:
            self.config["subtitleFile"] = subFile
            self.config["setting"]["subtitle"] = {}
            self.config["setting"]["subtitle"]["addMode"] = self.comboBox_sub_addmode.currentIndex()
            if outputs:
                outputs = outputs.replace("-c copy", "-acodec copy").replace("-vcodec copy", "")

        # 其他设置

        # 全局设置

        self.config["inputs"] = inputs.replace('\n', ' ')
        self.config["outputs"] = outputs.replace('\n', ' ')
        self.config["globalputs"] = globalputs.replace('\n', ' ')

        self.signal_setting.emit((self.row,))

        time.sleep(1)
        self.close()
    
    @pyqtSlot(bool)
    def on_checkBox_video_bitrate_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.spinBox_video_bitrate.setEnabled(checked)




class InitWidgetThread(QThread):

    send_volume = pyqtSignal(str)

    def __init__(self, parent=None):
        super(InitWidgetThread, self).__init__(parent)

    def setParams(self, mainWindow, out_video_format, config):
        self.mainWindow = mainWindow
        self.out_video_format = out_video_format
        self.config = config
        self.stopBool = False

    def stop(self):
        try:
            self.stopBool = True
            pid = self.ff.process.pid
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

    def run(self):
        self.stopBool = False

        # 参数设置
        if self.config["inputs"]:
            self.mainWindow.label_params_in.setText(self.config["inputs"])
        if self.config["outputs"]:
            self.mainWindow.label_params_out.setText(self.config["outputs"])
        if self.config["globalputs"]:
            self.mainWindow.label_params_global.setText(self.config["globalputs"])

        if self.config.__contains__("setting") and self.config["setting"]:

            # 音频设置
            if self.config["setting"].__contains__("audio") and self.config["setting"]["audio"]:
                ## 编码设置
                if self.config["setting"]["audio"].__contains__("coding") and self.config["setting"]["audio"]["coding"]:
                    self.mainWindow.comboBox_audioCoding.setCurrentText(self.config["setting"]["audio"]["coding"])

                ## 音量设置
                if self.config["setting"]["audio"].__contains__("volume") and self.config["setting"]["audio"]["volume"]:
                    self.mainWindow.comboBox_volume_unit.setCurrentText(self.config["setting"]["audio"]["volume"][0])
                    if '%' == self.config["setting"]["audio"]["volume"][0]:
                        self.mainWindow.spinBox_volume_percent.setValue(self.config["setting"]["audio"]["volume"][1])
                    elif "dB" == self.config["setting"]["audio"]["volume"][0]:
                        self.mainWindow.doubleSpinBox_dB.setValue(self.config["setting"]["audio"]["volume"][1])
                        self.mainWindow.comboBox_dB_direction.setCurrentText(self.config["setting"]["audio"]["volume"][2])

            # 字幕设置
            if self.config.__contains__("subtitleFile") and self.config["subtitleFile"]:
                self.mainWindow.label_sub.setText(self.config["subtitleFile"])
                if self.config["setting"].__contains__("subtitle"):
                    if self.config["setting"]["subtitle"].__contains__("addMode"):
                        self.mainWindow.comboBox_sub_addmode.setCurrentIndex(self.config["setting"]["subtitle"]["addMode"])
                else:
                    self.mainWindow.comboBox_sub_addmode.setCurrentIndex(1)
            else:
                if self.out_video_format == "TS" or self.out_video_format == "MP4":
                    self.mainWindow.comboBox_sub_addmode.setCurrentIndex(1)

            # 视频设置
            if self.config["setting"].__contains__("video"):
                ## 码率
                if self.config["setting"]["video"].__contains__("bitrate"):
                    self.mainWindow.checkBox_video_bitrate.setChecked(True)
                    self.mainWindow.spinBox_video_bitrate.setEnabled(True)
                    self.mainWindow.spinBox_video_bitrate.setValue(self.config["setting"]["video"]["bitrate"])
                ## 图像设置
                if self.config["setting"]["video"].__contains__("scale"):
                    self.mainWindow.comboBox_scale.setCurrentText(self.config["setting"]["video"]["scale"])
                if self.config["setting"]["video"].__contains__("resolution"):
                    self.mainWindow.comboBox_resolution.setCurrentText(self.config["setting"]["video"]["resolution"])

        self.mainWindow.pushButton_ok.setEnabled(True)

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.getFileVolume(self.config["videoFile"]))


    # def getFileVolume(self, file):
    #     try:
    #         self.ff = ffmpy3.FFmpeg(inputs={file: None},
    #                            global_options="-filter_complex volumedetect -c:v copy -f null /dev/null")
    #         stderr = self.ff.run(stderr=subprocess.PIPE)
    #         print(stderr)
    #         if stderr[-1]:
    #             result = re.findall(r'mean_volume: ([-.\d]*) dB', str(stderr[-1]))
    #             return result[0]
    #     except ffmpy3.FFExecutableNotFoundError as e:
    #         print("错误", "文件中音频音量识别失败", e)
    #
    #     return

    async def getFileVolume(self, file):
        self.ff = ffmpy3.FFmpeg(inputs={file: None},
                                global_options="-filter_complex volumedetect -c:v copy -f null /dev/null")

        await self.ff.run_async(stderr=asyncio.subprocess.PIPE)

        line_buf = bytearray()
        loopBool = False
        while not self.stopBool:
            in_buf = (await self.ff.process.stderr.read(128)).replace(b'\r', b'\n')
            if not in_buf:
                break
            line_buf.extend(in_buf)
            while b'\n' in line_buf and not self.stopBool:
                line, _, line_buf = line_buf.partition(b'\n')
                print(line, file=sys.stderr)
                if not line:
                    continue
                line = str(line)
                result = re.findall(r'mean_volume: ([-.\d]*) dB', str(line))
                if checkOutputErr(line):
                    loopBool = True
                    break
                else:
                    if result and result[0]:
                        self.send_volume.emit(result[0])
                        break
        if not self.stopBool and not loopBool:
            await self.ff.wait()


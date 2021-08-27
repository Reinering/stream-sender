# -*- coding: utf-8 -*-

"""
Module implementing SettingDialog.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog
import subprocess
import ffmpy3
import time
import re
import logging

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

    def setParams(self, row, config):
        self.row = row
        self.config = config
        self.initWidget()

    def initWidget(self):
        self.tabWidget.setCurrentIndex(0)
        self.doubleSpinBox_dB.setHidden(True)
        self.comboBox_dB_direction.setHidden(True)
        if self.config.__contains__("subtitleFile"):
            self.label_sub.setText(self.config["subtitleFile"])

        if self.config.__contains__("inputs") and self.config["inputs"]:
            self.plainTextEdit_params_in.setPlainText(self.config["inputs"])

        if self.config.__contains__("outputs") and self.config["outputs"]:
            self.plainTextEdit_params_out.setPlainText(self.config["outputs"])

        if self.config.__contains__("globalputs") and self.config["globalputs"]:
            self.plainTextEdit_params_global.setPlainText(self.config["globalputs"])

        if self.config.__contains__("setting") and self.config["setting"]:
            self.spinBox_volume.setValue(self.config["setting"]["volume"])

        volume = self.getFileVolume(self.config["videoFile"])
        if volume:
            self.label_current_volume.setText(volume)

    def getFileVolume(self, file):
        try:
            ff = ffmpy3.FFmpeg(inputs={file: None},
                                global_options="-filter_complex volumedetect -c:v copy -f null /dev/null")
            stderr = ff.run(stderr=subprocess.PIPE)
            if stderr[-1]:
                result = re.findall(r'mean_volume: ([-.\d]*) dB', str(stderr[-1]))
                return result[0]
        except ffmpy3.FFExecutableNotFoundError as e:
            logging.critical(self, "错误", "文件中音频音量识别失败")

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

        # 音频设置
        volume = self.spinBox_volume.value()
        if volume != 100:
            self.config["setting"]["volume"] = volume
            volume = '-filter:a "volume={}"'.format(str(volume/100))
            if outputs:
                outputs = volume + ' ' + outputs
            else:
                outputs = volume

        # 字幕设置
        subFile = self.label_sub.text()
        if subFile:
            self.config["subtitleFile"] = subFile

        # 其他设置

        # 全局设置

        if inputs:
            self.config["inputs"] = inputs.replace('\n', ' ')

        if outputs:
            self.config["outputs"] = outputs.replace('\n', ' ')

        if outputs:
            self.config["globalputs"] = globalputs.replace('\n', ' ')

        self.signal_setting.emit((self.row,))

        time.sleep(2)
        self.close()
    

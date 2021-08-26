# -*- coding: utf-8 -*-

"""
Module implementing SettingDialog.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog
import time
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
        if self.config.__contains__("subtitleFile"):
            self.label_sub.setText(self.config["subtitleFile"])

        if self.config.__contains__("inputs") and self.config["inputs"]:
            self.plainTextEdit_params_in.setPlainText(self.config["inputs"])

        if self.config.__contains__("outputs") and self.config["outputs"]:
            self.plainTextEdit_params_out.setPlainText(self.config["outputs"])

        if self.config.__contains__("globalputs") and self.config["globalputs"]:
            self.plainTextEdit_params_global.setPlainText(self.config["globalputs"])
    
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
    
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        subFile = self.label_sub.text()
        if subFile:
            self.config["subtitleFile"] = subFile

        inputs = self.plainTextEdit_params_in.toPlainText()
        if inputs:
            self.config["inputs"] = inputs.replace('\n', ' ')

        outputs = self.plainTextEdit_params_out.toPlainText()
        if outputs:
            self.config["outputs"] = outputs.replace('\n', ' ')

        globalputs = self.plainTextEdit_params_global.toPlainText()
        if outputs:
            self.config["globalputs"] = globalputs.replace('\n', ' ')

        self.signal_setting.emit((self.row,))

        time.sleep(2)
        self.close()




# -*- coding: utf-8 -*-

"""
Module implementing.
author: Reiner New
email: nbxlhc@hotmail.com
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCloseEvent

from Ui_FileTypeAsk import Ui_Dialog


class AskDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    signal_file = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(AskDialog, self).__init__(parent)
        self.setupUi(self)
        self.fileType = ''
    
    @pyqtSlot()
    def on_pushButton_video_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # self.fileType = "video"
        self.signal_file.emit("video")
        self.close()

    @pyqtSlot()
    def on_pushButton_audio_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.fileType = "audio"
        self.signal_file.emit("audio")
        self.close()

    @pyqtSlot()
    def on_pushButton_pic_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.fileType = "pic"
        self.signal_file.emit("pic")
        self.close()

    @pyqtSlot()
    def on_pushButton_sub_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.fileType = "sub"
        self.signal_file.emit("sub")
        self.close()

    # def closeEvent(self, a0: QCloseEvent) -> None:
    #     self.signal_file.emit(self.fileType)

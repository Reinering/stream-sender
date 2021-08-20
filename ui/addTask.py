# -*- coding: utf-8 -*-

"""
Module implementing tkDialog.
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_addTask import Ui_addTask


class addTask(QDialog, Ui_addTask):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(addTask, self).__init__(parent)
        self.setupUi(self)
        self._translate = QtCore.QCoreApplication.translate
        self.videoFormat = ".ts"

    @pyqtSlot()
    def on_pushButton_openPath_clicked(self):
        """
        Slot documentation goes here.
        """
        print("点击选择文件")
        try:
            download_path = QtWidgets.QFileDialog.getOpenFileName(self, u"选择视频文件", "/", "vedio Files(*" + self.videoFormat + ")")
            print(download_path[0])
            # self.lineEdit_path.clear()
            self.lineEdit_path.setText(download_path[0])
            print(self.lineEdit_path.text())
        except Exception as e:
            print(e)

    @pyqtSlot(str)
    def on_comboBox_videoFormat_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type str
        """
        if p0 == "TS":
            self.videoFormat = ".ts"
        if p0 == "MPEG4":
            self.videoFormat = ".mp4"
        print(self.videoFormat)


    @pyqtSlot()
    def on_pushButton_cancel_clicked(self):
        """
        Slot documentation goes here.
        """
        print("关闭")
        self.exec()
        self.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tk = QtWidgets.QDialog()
    ui = addTask()
    ui.setupUi(tk)
    ui.show()
    sys.exit(app.exec_())
    


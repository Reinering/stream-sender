# -*- coding: utf-8 -*-

"""
Module implementing.
author: Reiner New
email: nbxlhc@hotmail.com
"""

from PyQt5.QtCore import pyqtSlot, QCoreApplication, pyqtSignal, QRect
from PyQt5.QtWidgets import QDialog, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QMouseEvent, QFont
import platform

from manage import VERSION, PackageTime
from .Ui_about import Ui_Dialog



class Dialog_about(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    signal_result = pyqtSignal(bool)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog_about, self).__init__(parent)
        self.setupUi(self)
        self.translate = QCoreApplication.translate
        self.setWindowTitle(self.translate("Printer_Dialog", "关于"))
        del self.label_4
        self.label_4 = MyLabel(self)
        self.label_4.setGeometry(QRect(80, 200, 401, 31))
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText(self.translate("Dialog", "Copyright © 2018-2021  Xi\'an Jizhong Intelligent Technology co.,Ltd."))
        self.label_4.signal_click.connect(self.on_label_version_click)
        self.count = 0
        self.state = False
        self.initWidget()

    def initWidget(self):
        self.label_version.setText(self.label_version.text() + ' ' + VERSION)
        self.label_package.setText(self.label_package.text() + ' ' + PackageTime)
        self.label_py.setText(self.label_py.text() + ' ' + platform.python_version())

    def setLogLevel(self, p0):
        self.state = p0

    @pyqtSlot()
    def on_label_version_click(self):
        self.count += 1

        # if self.count == 7:
        #     self.count = 0
        #     self.state = not self.state
        #     self.signal_result.emit(self.state)



class MyLabel(QLabel):

    signal_click = pyqtSignal()

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        self.signal_click.emit()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = Dialog_about()
    Dialog.show()
    sys.exit(app.exec_())



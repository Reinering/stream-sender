# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\git\streamer\streamer-sender\ui\FileTypeAsk.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(194, 117)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_video = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_video.setObjectName("pushButton_video")
        self.gridLayout.addWidget(self.pushButton_video, 0, 0, 1, 1)
        self.pushButton_audio = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_audio.setObjectName("pushButton_audio")
        self.gridLayout.addWidget(self.pushButton_audio, 0, 1, 1, 1)
        self.pushButton_pic = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_pic.setObjectName("pushButton_pic")
        self.gridLayout.addWidget(self.pushButton_pic, 1, 0, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择对话框"))
        self.groupBox.setTitle(_translate("Dialog", "请选择添加的文件类型"))
        self.pushButton_video.setText(_translate("Dialog", "视频文件"))
        self.pushButton_audio.setText(_translate("Dialog", "音频文件"))
        self.pushButton_pic.setText(_translate("Dialog", "图像文件"))
        self.pushButton_sub.setText(_translate("Dialog", "字幕文件"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

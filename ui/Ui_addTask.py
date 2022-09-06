# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\git\streamer-sender\ui\addTask.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addTask(object):
    def setupUi(self, addTask):
        addTask.setObjectName("addTask")
        addTask.resize(655, 430)
        font = QtGui.QFont()
        addTask.setFont(font)
        addTask.setSizeGripEnabled(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(addTask)
        self.gridLayout_3.setContentsMargins(0, 3, 0, 3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(addTask)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.lineEdit_task = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_task.setFont(font)
        self.lineEdit_task.setObjectName("lineEdit_task")
        self.horizontalLayout_6.addWidget(self.lineEdit_task)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(32, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.comboBox_ip = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ip.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ip.setFont(font)
        self.comboBox_ip.setEditable(True)
        self.comboBox_ip.setObjectName("comboBox_ip")
        self.horizontalLayout_7.addWidget(self.comboBox_ip)
        self.pushButton_refresh = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_refresh.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout_7.addWidget(self.pushButton_refresh)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.comboBox_ipType = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_ipType.setFont(font)
        self.comboBox_ipType.setObjectName("comboBox_ipType")
        self.comboBox_ipType.addItem("")
        self.comboBox_ipType.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_ipType)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox_protocol = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_protocol.setFont(font)
        self.comboBox_protocol.setObjectName("comboBox_protocol")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_protocol)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_dst_ip = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_dst_ip.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_dst_ip.setFont(font)
        self.comboBox_dst_ip.setEditable(True)
        self.comboBox_dst_ip.setObjectName("comboBox_dst_ip")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.setItemText(0, "")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_dst_ip)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spinBox_port = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_port.setFont(font)
        self.spinBox_port.setMinimum(1000)
        self.spinBox_port.setMaximum(65535)
        self.spinBox_port.setProperty("value", 1234)
        self.spinBox_port.setObjectName("spinBox_port")
        self.horizontalLayout.addWidget(self.spinBox_port)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_uri = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_uri.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_uri.setFont(font)
        self.comboBox_uri.setEditable(True)
        self.comboBox_uri.setObjectName("comboBox_uri")
        self.comboBox_uri.addItem("")
        self.comboBox_uri.setItemText(0, "")
        self.horizontalLayout_2.addWidget(self.comboBox_uri)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.comboBox_videoFormat = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_videoFormat.setFont(font)
        self.comboBox_videoFormat.setObjectName("comboBox_videoFormat")
        self.comboBox_videoFormat.addItem("")
        self.comboBox_videoFormat.addItem("")
        self.comboBox_videoFormat.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_videoFormat)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.comboBox_sendMode = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_sendMode.setFont(font)
        self.comboBox_sendMode.setObjectName("comboBox_sendMode")
        self.comboBox_sendMode.addItem("")
        self.comboBox_sendMode.addItem("")
        self.comboBox_sendMode.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_sendMode)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(addTask)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(3, -1, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_openPath = QtWidgets.QPushButton(addTask)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_openPath.setFont(font)
        self.pushButton_openPath.setObjectName("pushButton_openPath")
        self.horizontalLayout_3.addWidget(self.pushButton_openPath)
        self.pushButton_up = QtWidgets.QPushButton(addTask)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_up.setFont(font)
        self.pushButton_up.setObjectName("pushButton_up")
        self.horizontalLayout_3.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(addTask)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_down.setFont(font)
        self.pushButton_down.setObjectName("pushButton_down")
        self.horizontalLayout_3.addWidget(self.pushButton_down)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.pushButton_ok = QtWidgets.QPushButton(addTask)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(addTask)
        QtCore.QMetaObject.connectSlotsByName(addTask)

    def retranslateUi(self, addTask):
        _translate = QtCore.QCoreApplication.translate
        addTask.setWindowTitle(_translate("addTask", "添加任务"))
        self.groupBox.setTitle(_translate("addTask", "配置任务"))
        self.label_9.setText(_translate("addTask", "任务名："))
        self.lineEdit_task.setText(_translate("addTask", "TASK"))
        self.label_8.setText(_translate("addTask", "IP地址："))
        self.pushButton_refresh.setText(_translate("addTask", "刷新"))
        self.comboBox_ipType.setItemText(0, _translate("addTask", "IPv4"))
        self.comboBox_ipType.setItemText(1, _translate("addTask", "IPv6"))
        self.label_3.setText(_translate("addTask", "协议："))
        self.comboBox_protocol.setItemText(0, _translate("addTask", "UDP"))
        self.comboBox_protocol.setItemText(1, _translate("addTask", "RTP"))
        self.comboBox_protocol.setItemText(2, _translate("addTask", "RTMP"))
        self.label_2.setText(_translate("addTask", "目的地址："))
        self.comboBox_dst_ip.setItemText(1, _translate("addTask", "224.1.1.1"))
        self.comboBox_dst_ip.setItemText(2, _translate("addTask", "224.1.1.2"))
        self.comboBox_dst_ip.setItemText(3, _translate("addTask", "224.1.1.3"))
        self.comboBox_dst_ip.setItemText(4, _translate("addTask", "224.1.1.4"))
        self.comboBox_dst_ip.setItemText(5, _translate("addTask", "224.1.1.5"))
        self.comboBox_dst_ip.setItemText(6, _translate("addTask", "224.1.1.6"))
        self.comboBox_dst_ip.setItemText(7, _translate("addTask", "224.1.1.7"))
        self.comboBox_dst_ip.setItemText(8, _translate("addTask", "224.1.1.8"))
        self.comboBox_dst_ip.setItemText(9, _translate("addTask", "224.1.1.9"))
        self.comboBox_dst_ip.setItemText(10, _translate("addTask", "224.1.1.10"))
        self.comboBox_dst_ip.setItemText(11, _translate("addTask", "238.1.238.1"))
        self.comboBox_dst_ip.setItemText(12, _translate("addTask", "238.1.238.2"))
        self.comboBox_dst_ip.setItemText(13, _translate("addTask", "238.1.238.3"))
        self.comboBox_dst_ip.setItemText(14, _translate("addTask", "238.1.238.4"))
        self.comboBox_dst_ip.setItemText(15, _translate("addTask", "238.1.238.5"))
        self.comboBox_dst_ip.setItemText(16, _translate("addTask", "238.1.238.6"))
        self.comboBox_dst_ip.setItemText(17, _translate("addTask", "238.1.238.7"))
        self.comboBox_dst_ip.setItemText(18, _translate("addTask", "238.1.238.8"))
        self.comboBox_dst_ip.setItemText(19, _translate("addTask", "238.1.238.9"))
        self.comboBox_dst_ip.setItemText(20, _translate("addTask", "238.1.238.10"))
        self.comboBox_dst_ip.setItemText(21, _translate("addTask", "238.1.238.11"))
        self.comboBox_dst_ip.setItemText(22, _translate("addTask", "238.1.238.12"))
        self.label_4.setText(_translate("addTask", "端口号："))
        self.label_5.setText(_translate("addTask", "URI："))
        self.label_6.setText(_translate("addTask", "输出视频格式："))
        self.comboBox_videoFormat.setItemText(0, _translate("addTask", "TS"))
        self.comboBox_videoFormat.setItemText(1, _translate("addTask", "MP4"))
        self.comboBox_videoFormat.setItemText(2, _translate("addTask", "FLV"))
        self.label_10.setText(_translate("addTask", "发送模式："))
        self.comboBox_sendMode.setItemText(0, _translate("addTask", "循环"))
        self.comboBox_sendMode.setItemText(1, _translate("addTask", "单次"))
        self.comboBox_sendMode.setItemText(2, _translate("addTask", "单个循环"))
        self.groupBox_2.setTitle(_translate("addTask", "发送列表"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("addTask", "视频文件"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("addTask", "字幕文件"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("addTask", "参数"))
        self.pushButton_openPath.setText(_translate("addTask", "添加文件"))
        self.pushButton_up.setText(_translate("addTask", "上移"))
        self.pushButton_down.setText(_translate("addTask", "下移"))
        self.pushButton_ok.setText(_translate("addTask", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addTask = QtWidgets.QDialog()
    ui = Ui_addTask()
    ui.setupUi(addTask)
    addTask.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\git\stream_sender\ui\ffmpeg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 558)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_ip = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ip.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_ip.setFont(font)
        self.comboBox_ip.setEditable(True)
        self.comboBox_ip.setObjectName("comboBox_ip")
        self.horizontalLayout.addWidget(self.comboBox_ip)
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_filePath = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_filePath.setFont(font)
        self.lineEdit_filePath.setText("")
        self.lineEdit_filePath.setObjectName("lineEdit_filePath")
        self.horizontalLayout_5.addWidget(self.lineEdit_filePath)
        self.pushButton_openPath = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_openPath.setFont(font)
        self.pushButton_openPath.setObjectName("pushButton_openPath")
        self.horizontalLayout_5.addWidget(self.pushButton_openPath)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_protocol = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_protocol.setFont(font)
        self.comboBox_protocol.setObjectName("comboBox_protocol")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.comboBox_protocol.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_protocol)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_multiIp = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_multiIp.setFont(font)
        self.comboBox_multiIp.setEditable(True)
        self.comboBox_multiIp.setObjectName("comboBox_multiIp")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.comboBox_multiIp.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_multiIp)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox_port = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox_port.setFont(font)
        self.spinBox_port.setMinimum(1000)
        self.spinBox_port.setMaximum(65535)
        self.spinBox_port.setProperty("value", 50001)
        self.spinBox_port.setObjectName("spinBox_port")
        self.horizontalLayout_4.addWidget(self.spinBox_port)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.comboBox_videoFormat = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_videoFormat.setFont(font)
        self.comboBox_videoFormat.setObjectName("comboBox_videoFormat")
        self.comboBox_videoFormat.addItem("")
        self.comboBox_videoFormat.addItem("")
        self.comboBox_videoFormat.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_videoFormat)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_2.addWidget(self.pushButton_del)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_2.addWidget(self.pushButton_clear)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_stop)
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")
        self.horizontalLayout_2.addWidget(self.pushButton_open)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FFMPEG"))
        self.label_2.setText(_translate("MainWindow", "配置推流任务"))
        self.label.setText(_translate("MainWindow", "IP地址："))
        self.pushButton_refresh.setText(_translate("MainWindow", "刷新"))
        self.label_7.setText(_translate("MainWindow", "选择文件路径："))
        self.pushButton_openPath.setText(_translate("MainWindow", "浏览"))
        self.label_3.setText(_translate("MainWindow", "协议："))
        self.comboBox_protocol.setItemText(0, _translate("MainWindow", "UDP"))
        self.comboBox_protocol.setItemText(1, _translate("MainWindow", "RTP"))
        self.comboBox_protocol.setItemText(2, _translate("MainWindow", "RTMP"))
        self.label_4.setText(_translate("MainWindow", "组播地址："))
        self.comboBox_multiIp.setItemText(0, _translate("MainWindow", "238.1.238.1"))
        self.comboBox_multiIp.setItemText(1, _translate("MainWindow", "238.1.238.2"))
        self.comboBox_multiIp.setItemText(2, _translate("MainWindow", "238.1.238.3"))
        self.comboBox_multiIp.setItemText(3, _translate("MainWindow", "238.1.238.5"))
        self.comboBox_multiIp.setItemText(4, _translate("MainWindow", "238.1.238.6"))
        self.comboBox_multiIp.setItemText(5, _translate("MainWindow", "238.1.238.7"))
        self.comboBox_multiIp.setItemText(6, _translate("MainWindow", "238.1.238.8"))
        self.comboBox_multiIp.setItemText(7, _translate("MainWindow", "238.1.238.9"))
        self.comboBox_multiIp.setItemText(8, _translate("MainWindow", "238.1.238.10"))
        self.comboBox_multiIp.setItemText(9, _translate("MainWindow", "238.1.238.11"))
        self.comboBox_multiIp.setItemText(10, _translate("MainWindow", "238.1.238.12"))
        self.comboBox_multiIp.setItemText(11, _translate("MainWindow", "238.1.238.51"))
        self.comboBox_multiIp.setItemText(12, _translate("MainWindow", "238.1.238.52"))
        self.comboBox_multiIp.setItemText(13, _translate("MainWindow", "238.1.238.53"))
        self.comboBox_multiIp.setItemText(14, _translate("MainWindow", "238.1.238.54"))
        self.label_5.setText(_translate("MainWindow", "端口号："))
        self.label_6.setText(_translate("MainWindow", "视频格式："))
        self.comboBox_videoFormat.setItemText(0, _translate("MainWindow", "TS"))
        self.comboBox_videoFormat.setItemText(1, _translate("MainWindow", "MPEG4"))
        self.comboBox_videoFormat.setItemText(2, _translate("MainWindow", "MKV"))
        self.pushButton_add.setText(_translate("MainWindow", "添加任务"))
        self.pushButton_del.setText(_translate("MainWindow", "删除任务"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空任务"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止"))
        self.pushButton_open.setText(_translate("MainWindow", "打开配置"))
        self.pushButton_save.setText(_translate("MainWindow", "保存配置"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "视频文件名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "协议"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "源IP"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "目的IP"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "目的端口"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "发送速率"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "状态"))
        self.menu.setTitle(_translate("MainWindow", "关于"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

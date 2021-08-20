# -*- coding: utf-8 -*-

"""
Module implementing tkDialog.
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QMenu, QMessageBox ,QFileDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtGui import QFont
import socket
import re
import datetime
import decimal
import time
import logging

from .Ui_addTask import Ui_addTask


class addTask(QDialog, Ui_addTask):
    """
    Class documentation goes here.
    """

    send_data = pyqtSignal(dict)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(addTask, self).__init__(parent)
        self.setupUi(self)
        self.translate = QtCore.QCoreApplication.translate
        self.videoFormat = ".ts"
        self.taskInfo = {"playlist": []}
        self.on_pushButton_refresh_clicked()

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.setColumnWidth(0, 500)
        self.tableWidget.setColumnWidth(1, 150)

    def modifyInfo(self, row, tableWidget):
        print(row, tableWidget)
        self.setWindowTitle("修改任务")
        

    # 查询信息添加至tableWidget中
    def addInfo(self, tableWidget, *args):
        row = tableWidget.rowCount()
        tableWidget.setRowCount(row + 1)
        i = 0
        for arg in args:
            argType = type(arg)
            if argType == int:
                self.addTableWidgetEntry(row, i, str(arg), tableWidget)
            elif argType == float:
                self.addTableWidgetEntry(row, i, str(arg), tableWidget)
            elif argType == datetime.datetime:
                self.addTableWidgetEntry(row, i, self.datetime_toString(arg), tableWidget)
            elif argType == decimal.Decimal:
                self.addTableWidgetEntry(row, i, str(arg), tableWidget)
            else:
                self.addTableWidgetEntry(row, i, arg, tableWidget)
            i += 1

    def addTableWidgetEntry(self, x, y, p0, tbWidget):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setText(self.translate("MainWindow", p0))
        # item.setFont(self.setCellFont())
        tbWidget.setItem(x, y, item)

    def clearTableWidgetEntry(self, tbWidget):
        row = tbWidget.rowCount()
        for i in range(row):
            tbWidget.removeRow(0)

    def createLeftMenu(self, row, tableWidget, pos):
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)

        _menu = QMenu()
        # modify_item = _menu.addAction("修改")
        # modify_item.setFont(font)
        # modify_item.triggered.connect(self.modifyUser)
        del_item = _menu.addAction("删除")
        del_item.setFont(font)
        # del_item.triggered.connect(self.deluser)
        action_menu = _menu.exec_(pos)
        if not action_menu:
            return

        if action_menu.text() == "选择":
            self.redirectPage(True, tableWidget, row)
        else:
            if action_menu.text() == "修改":
                pass
            elif action_menu.text() == "删除":
                button = QMessageBox.information(self, "提示", "确认删除？", QMessageBox.Yes | QMessageBox.No)
                if button == QMessageBox.Yes:
                    self.taskInfo["playlist"].remove(tableWidget.item(row, 0).text())
                    tableWidget.removeRow(row)
            else:
                pass

    # def createRightMenu(self, tableWidget, pos):
    #     font = QFont()
    #     font.setFamily("微软雅黑")
    #     font.setPointSize(10)
    #
    #     _menu = QMenu()
    #     if 'store_keep' not in tableWidget.objectName():
    #         new_item = _menu.addAction("新建")
    #         new_item.setFont(font)
    #     # new_item.triggered.connect(self.newUser)
    #     if 'products' in tableWidget.objectName() and (USERINFO["isadmin"] or USERINFO["isroot"]):
    #         new__item = _menu.addAction("新建产品类别")
    #         new__item.setFont(font)
    #     if self.redirectFunc["state"]:
    #         modify_item = _menu.addAction("返回")
    #         modify_item.setFont(font)
    #
    #     action_menu = _menu.exec_(pos)
    #     if not action_menu:
    #         return
    #     if action_menu.text() == "返回":
    #         self.redirectPage(False, tableWidget)
    #     else:
    #         self.userDialog = User_Dialog()
    #         self.userDialog.setAttribute(Qt.WA_DeleteOnClose, True)
    #         self.userDialog.setModal(True)
    #         if action_menu.text() == "新建":
    #             self.userDialog.newInfo(tableWidget)
    #         elif action_menu.text() == "新建产品类别":
    #             self.userDialog.newProdctModel()
    #         else:
    #             return
    #         self.userDialog.show()

    @pyqtSlot()
    def on_pushButton_openPath_clicked(self):
        """
        Slot documentation goes here.
        """
        print("点击选择文件")
        try:
            files = QFileDialog.getOpenFileNames(self, u"选择视频文件", "/",
                                                           "vedio Files(*" + self.videoFormat + ")")
            for file in files[0]:
                self.addInfo(self.tableWidget, file, files[1])
                self.taskInfo["playlist"].append(file)
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
    def on_pushButton_refresh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        addrs = socket.getaddrinfo(socket.gethostname(), None)
        i = 0
        for addr in addrs:
            ipAddr = addr[-1][0]
            ipv4 = re.findall(r"\d+\.\d+\.\d+\.\d+", ipAddr)
            if len(ipv4) == 0 or not ipv4[0]:
                continue
            self.comboBox_ip.addItem("")
            self.comboBox_ip.setItemText(i, self.translate("MainWindow", ipv4[0]))
            i += 1
    
    # @pyqtSlot(QPoint)
    # def on_tableWidget_customContextMenuRequested(self, pos):
    #     """
    #     Slot documentation goes here.
    #
    #     @param pos DESCRIPTION
    #     @type QPoint
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError
    #     self.createRightMenu(self.tableWidget_store_keep, self.tableWidget_store_keep.mapToGlobal(pos))
    
    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        
        @param row DESCRIPTION
        @type int
        @param column DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        pos = self.cursor().pos()
        self.createLeftMenu(row, self.tableWidget, pos)
    
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        sendMode = self.comboBox_sendMode.currentText()
        if not sendMode:
            return

        protocol = self.comboBox_protocol.currentText()
        if not protocol:
            return

        multiIp = self.lineEdit_multiIp.text()
        if not multiIp:
            QMessageBox.critical(self, "错误", "组播地址不能为空")
            return

        port = self.spinBox_port.value()
        if not port:
            QMessageBox.critical(self, "错误", "端口号不能为空或0")
            return

        videoFormat = self.comboBox_videoFormat.currentText()
        if not videoFormat:
            return

        if not self.taskInfo["playlist"]:
            QMessageBox.critical(self, "错误", "视频文件不能为空")
            return

        src_ip = self.comboBox_ip.currentText()

        self.taskInfo["bingAddr"] = src_ip
        self.taskInfo["protocol"] = protocol
        self.taskInfo["dst_ipaddr"] = multiIp
        self.taskInfo["dst_port"] = port
        self.taskInfo["video_format"] = videoFormat
        self.taskInfo["src_ip"] = src_ip
        self.taskInfo["send_mode"] = sendMode

        self.send_data.emit(self.taskInfo)
        time.sleep(2)
        self.close()








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tk = QtWidgets.QDialog()
    ui = addTask()
    ui.setupUi(tk)
    ui.show()
    sys.exit(app.exec_())
    


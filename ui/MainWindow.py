# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QCoreApplication, Qt
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMenu, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QFont
import datetime
import decimal
import simplejson
import re
import subprocess
import time
import ffmpy3
import logging

from manage import TASKLIST_CONFIG
from .Ui_MainWindow import Ui_MainWindow
from .addTask import addTask


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.translate = QCoreApplication.translate

        self.videoFormat = ".ts"
        self.taskkey = 0
        self.tasklist = []
        self.threadList = []

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

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
        modify_item = _menu.addAction("修改")
        modify_item.setFont(font)
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
                self.addDialog = addTask()
                self.addDialog.setAttribute(Qt.WA_DeleteOnClose, True)
                self.addDialog.setModal(True)
                self.addDialog.modifyInfo(row, tableWidget)
                self.addDialog.show()
            elif action_menu.text() == "删除":
                button = QMessageBox.information(self, "提示", "确认删除此任务？", QMessageBox.Yes | QMessageBox.No)
                if button == QMessageBox.Yes:
                    key = self.tasklist[row]
                    self.tasklist.remove(key)
                    TASKLIST_CONFIG.pop(key)
                    tableWidget.removeRow(row)
            else:
                pass

    @pyqtSlot()
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.addDialog = addTask()
        self.addDialog.setAttribute(Qt.WA_DeleteOnClose, True)
        self.addDialog.setModal(True)
        self.addDialog.send_data.connect(self.addTask)
        self.addDialog.show()

    def addTask(self, p0):
        key = "task_" + str(self.taskkey)
        TASKLIST_CONFIG[key] = p0
        self.tasklist.append(key)
        self.taskkey += 1
        self.addInfo(self.tableWidget, p0["playlist"][0].split('/')[-1], p0["send_mode"], p0["protocol"],
                     p0["src_ip"], p0["dst_ipaddr"], p0["dst_port"], '', '')

    def clearConfig(self):
        self.taskkey = 0
        self.tasklist.clear()
        TASKLIST_CONFIG.clear()

    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        # stop


        # clear
        self.clearConfig()
        self.clearTableWidgetEntry(self.tableWidget)

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        pass

    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        pass

    @pyqtSlot()
    def on_pushButton_open_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            filePath = QFileDialog.getOpenFileName(self, u"选择配置文件", "/",
                                                           "json file(*.json)")
            if not filePath[0]:
                return

            self.parseConfigFile(filePath[0])
        except Exception as e:
            print(e)

    def parseConfigFile(self, file):
        try:
            with open(file, 'r', encoding="utf-8") as f:
                config = simplejson.load(f, encoding="utf-8")
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "错误", "配置文件解析错误")
            return
        if len(config) == 0:
            return

        self.on_pushButton_clear_clicked()

        for key, value in config.items():
            try:
                self.addInfo(self.tableWidget, value["playlist"][0].split('/')[-1], value["send_mode"], value["protocol"],
                             value["src_ip"], value["dst_ipaddr"], value["dst_port"], '', '')
                key = "task_" + str(self.taskkey)
                TASKLIST_CONFIG[key] = value
                self.tasklist.append(key)
                self.taskkey += 1
            except Exception as e:
                print(e)
                continue

    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        filePath = QFileDialog.getSaveFileName(self, "保存", '', "json file(*.json)")
        if not filePath:
            return
        configJson = simplejson.dumps(TASKLIST_CONFIG)
        with open(filePath[0], 'w', encoding="utf-8") as f:
            f.write(configJson)
            f.flush()

        QMessageBox.information(self, "提示", "文件已保存")

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
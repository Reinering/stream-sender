# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QCoreApplication, Qt
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMenu, QMessageBox, QTableWidgetItem, QFileDialog, QToolTip
from PyQt5.QtGui import QFont, QCloseEvent, QCursor
import datetime
import decimal
import simplejson
import copy
import logging

from manage import TASKLIST_CONFIG
from .Ui_MainWindow import Ui_MainWindow
from .addTask import addTask
from .ffmpegHelp import FFmpegHelpDialog
from sender.sender import FfmpegCorThread


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

        self.ffmpegPath = ''
        self.configPath = ''

        self.videoFormat = ".ts"
        self.taskkey = 0
        self.tasklist = []

        self.ffTh = FfmpegCorThread()
        self.ffTh.signal_state.connect(self.setTaskState)
        self.ffTh.start()

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # tooltip
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.cellEntered.connect(self.cellEntered)

    def cellEntered(self, row, column):
        if column == 0:
            try:
                content = self.tableWidget.item(row, column).text()
            except Exception as e:
                return
            if content:
                QToolTip.showText(QCursor.pos(), content)

    @pyqtSlot()
    def on_action_exePath_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        print("path")

    @pyqtSlot()
    def on_action_open_triggered(self):
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

    @pyqtSlot()
    def on_action_save_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.configPath:
            self.saveConfig(self.configPath)
            QMessageBox.information(self, "提示", "文件已保存")
        else:
            self.on_action_saveas_triggered()

    @pyqtSlot()
    def on_action_saveas_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        filePath = QFileDialog.getSaveFileName(self, "保存", '', "json file(*.json)")
        if not filePath[0]:
            return

        self.saveConfig(filePath[0])

        self.configPath = filePath[0]
        QMessageBox.information(self, "提示", "文件已保存")

    @pyqtSlot()
    def on_action_ffmpeg_help_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.ffHelpDialog = FFmpegHelpDialog()
        self.ffHelpDialog.setAttribute(Qt.WA_DeleteOnClose, True)
        self.ffHelpDialog.setModal(False)
        self.ffHelpDialog.show()

    @pyqtSlot()
    def on_action_exit_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.close()

    def saveConfig(self, filePath):
        tmpConfig = copy.copy(TASKLIST_CONFIG)
        for key, value in tmpConfig.items():
            if value.__contains__("state"):
                value.pop("state")
        with open(filePath, 'w', encoding="utf-8") as f:
            f.write(simplejson.dumps(tmpConfig))
            f.flush()

    def closeEvent(self, a0: QCloseEvent) -> None:
        self.ffTh.stop()

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
                self.addDialog.modifyInfo(row, self.tasklist[row], tableWidget)
                self.addDialog.show()
            elif action_menu.text() == "删除":
                button = QMessageBox.information(self, "提示", "确认删除此任务？", QMessageBox.Yes | QMessageBox.No)
                if button == QMessageBox.Yes:
                    key = self.tasklist[row]
                    self.ffTh.stopCoroutine(row)
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
        TASKLIST_CONFIG[key]["current_index"] = 0
        self.tasklist.append(key)
        self.taskkey += 1
        self.addInfo(self.tableWidget, p0["playlist"][0]["videoFile"].split('/')[-1], p0["send_mode"], p0["protocol"],
                     p0["src_ip"], p0["dst_ip"], p0["dst_port"], p0["out_video_format"], '', '')

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
        row = self.tableWidget.currentRow()
        if row >= 0:
            config = TASKLIST_CONFIG[self.tasklist[row]]
            if not config.__contains__("state") or config["state"] != 1:
                self.ffTh.addCoroutine(row, config)
        elif row == -1:
            for i in range(len(self.tasklist)):
                config = TASKLIST_CONFIG[self.tasklist[i]]
                if not config.__contains__("state") or config["state"] != 1:
                    self.ffTh.addCoroutine(i, config)

    def setTaskState(self, p0):
        print(p0)
        config = TASKLIST_CONFIG[self.tasklist[p0[0]]]
        if isinstance(p0[1], int):
            config["state"] = p0[1]
            item = self.tableWidget.item(p0[0], 8)
            if p0[1] == 1:
                item.setText(self.translate("MainWindow", "是"))
            elif p0[1] == 0:
                item.setText(self.translate("MainWindow", "否"))
                config["current_index"] = 0
                item = self.tableWidget.item(p0[0], 7)
                item.setText(self.translate("MainWindow", ''))
            elif p0[1] == 2:
                item.setText(self.translate("MainWindow", "暂停"))
        elif isinstance(p0[1], str):
            item = self.tableWidget.item(p0[0], 0)
            item.setText(self.translate("MainWindow", p0[1]))
        elif isinstance(p0[1], tuple):
            item = self.tableWidget.item(p0[0], 7)
            item.setText(self.translate("MainWindow", p0[1][5]))

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
                self.addInfo(self.tableWidget, value["playlist"][0]["videoFile"].split('/')[-1], value["send_mode"], value["protocol"],
                             value["src_ip"], value["dst_ip"], value["dst_port"], value["out_video_format"], '', '')
                key = "task_" + str(self.taskkey)
                TASKLIST_CONFIG[key] = value
                TASKLIST_CONFIG[key]["current_index"] = 0
                self.tasklist.append(key)
                self.taskkey += 1
            except Exception as e:
                print(e)
                continue
        self.configPath = file

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
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            row = self.tableWidget.currentRow()
            if row >= 0:
                self.ffTh.stopCoroutine(row)
        except Exception as e:
            print(e)

    @pyqtSlot()
    def on_pushButton_stop_all_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        for i in range(len(self.tasklist)):
            self.ffTh.stopCoroutine(i)

    @pyqtSlot()
    def on_pushButton_pause_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            row = self.tableWidget.currentRow()
            if row >= 0:
                self.ffTh.pauseCoroutine(row)
            elif row == -1:
                for i in range(len(self.tasklist)):
                    self.ffTh.pauseCoroutine(i)
        except Exception as e:
            print(e)
    
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            row = self.tableWidget.currentRow()
            if row >= 0:
                if not TASKLIST_CONFIG[self.tasklist[row]].__contains__("state") or TASKLIST_CONFIG[self.tasklist[row]]["state"] != 1:
                    TASKLIST_CONFIG[self.tasklist[row]]["current_index"] += 1
                    if TASKLIST_CONFIG[self.tasklist[row]]["current_index"] >= len(TASKLIST_CONFIG[self.tasklist[row]]["playlist"]):
                        TASKLIST_CONFIG[self.tasklist[row]]["current_index"] = 0
                    item = self.tableWidget.item(row, 0)
                    item.setText(self.translate("MainWindow", TASKLIST_CONFIG[self.tasklist[row]]["playlist"][TASKLIST_CONFIG[self.tasklist[row]]["current_index"]]["videoFile"].split('/')[-1]))
                else:
                    self.ffTh.next(row)
        except Exception as e:
            print(e)
    


# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QCoreApplication, Qt, QThread
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QMenu, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QFont, QCloseEvent
import datetime
import decimal
import simplejson
import subprocess
import ffmpy3
import asyncio
import sys
import re
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

        self.ffTh = FfmpegCorThread()
        self.ffTh.signal_state.connect(self.setTaskState)
        self.ffTh.start()

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

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
                    self.ffTh.stop(row)
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
        print("row", row)
        if row >= 0:
            config = TASKLIST_CONFIG[self.tasklist[row]]
            self.ffTh.addCoroutine(row, config)
        elif row == -1:
            for i in range(len(self.tasklist)):
                config = TASKLIST_CONFIG[self.tasklist[i]]
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
        for key, value in TASKLIST_CONFIG.items():
            value.pop("thread")
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
            elif row == -1:
                for i in range(len(self.tasklist)):
                    self.ffTh.stopCoroutine(i)
        except Exception as e:
            print(e)

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
                self.ffTh.pause(row)
            elif row == -1:
                for i in range(len(self.tasklist)):
                    self.ffTh.pause(i)
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
                config = TASKLIST_CONFIG[self.tasklist[row]]
                self.ffTh.pause(row)
                config["current_index"] += 1
                self.ffTh.addCoroutine(row, config)
        except Exception as e:
            print(e)

# Coroutine
class FfmpegCorThread(QThread):

    signal_state = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(FfmpegCorThread, self).__init__(parent)
        self.stopBool = False
        self.loop = asyncio.new_event_loop()
        self.processList = {}
        self.resultRE = r'frame=[ ]*(\d*) fps=[ ]*([.\d]*) q=([-.\d]*) size=[ ]*([\d]*kB) time=(\d{2}:\d{2}:\d{2}.\d{2}) bitrate=[ ]*([.\d]*kbits/s) speed=[ ]*([.\d]*x)'

    def stop(self):
        print("结束线程", self.loop.is_running())
        self.stopBool = True
        try:
            for key, value in self.processList.items():
                self.stopCoroutine(key)
            self.processList.clear()
            self.loop.stop()
            print(self.loop.is_running())
        except Exception as e:
            print(e)

    def stopCoroutine(self, row):
        print("结束协程", row)
        try:
            self.killFF(self.processList[row])
        except Exception as e:
            print(e)
        self.signal_state.emit((row, 0))

    def pause(self, row):
        self.stopCoroutine(row)
        self.signal_state.emit((row, 2))

    def killFF(self, ff):
        try:
            pid = ff.process.pid
            print("pid", pid)
            cmd = "taskkill /pid " + str(pid) + " -t -f"
            pp = subprocess.Popen(args=cmd,
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  shell=True)
            out = str(pp.stdout.read(), encoding="utf-8")
            print('out:', out)
        except Exception as e:
            print(e)

    def run(self):
        try:
            asyncio.set_event_loop(self.loop)
            self.loop.run_forever()
        except Exception as e:
            print(e)
        finally:
            self.loop.close()

    def addCoroutine(self, row, CONFIG):
        self.row = row
        self.config = CONFIG
        asyncio.run_coroutine_threadsafe(self.sendCoroutine(row, CONFIG), self.loop)

    async def sendCoroutine(self, row, config):
        self.signal_state.emit((row, 1))
        loopType = True

        while loopType:
            if config["send_mode"] == "单次":
                loopType = False

            i = config["current_index"]
            loopBool = False
            while i < len(config["playlist"]):
                self.signal_state.emit((row, config["playlist"][i]["videoFile"]))
                ff = self.send(config)
                await ff.run_async(stderr=asyncio.subprocess.PIPE)
                self.processList[row] = ff
                line_buf = bytearray()
                while True:
                    in_buf = (await ff.process.stderr.read(128)).replace(b'\r', b'\n')
                    if not in_buf:
                        break
                    line_buf.extend(in_buf)
                    while b'\n' in line_buf:
                        line, _, line_buf = line_buf.partition(b'\n')
                        line = str(line)
                        # print(line, file=sys.stderr)
                        if 'Conversion failed!' in line:
                            loopBool = True
                            break
                        else:
                            result = re.findall(self.resultRE, line)
                            if result:
                                self.signal_state.emit((row, result[0]))

                if not loopBool:
                    await ff.wait()

                i += 1
                config["current_index"] = i

            config["current_index"] = 0
            if loopBool:
                loopType = False

        self.signal_state.emit((self.row, 0))

    def send(self, config):
        file = config["playlist"][config["current_index"]]["videoFile"]
        if config["protocol"] == "UDP":
            if config["out_video_format"] == "MPEG4":
                ff = ffmpy3.FFmpeg(
                    inputs={file: '-re'},
                    outputs={'udp://' + config["dst_ip"] + ':' + str(config["dst_port"]): '-vcodec libx264 -acodec copy -f mpegts'}
                )
            elif config["out_video_format"] == "TS":
                if file.split('.')[-1].upper() == "TS":
                    ff = ffmpy3.FFmpeg(
                        inputs={file: '-re'},
                        outputs={'udp://' + config["dst_ip"] + ':' + str(config["dst_port"]): '-vcodec copy -f mpegts'}
                    )
                else:
                    ff = ffmpy3.FFmpeg(
                        inputs={file: '-re'},
                        # outputs={'udp://' + config["dst_ip"] + ':' + str(config["dst_port"]): '-vcodec libx264 -acodec copy -f mpegts'}
                        outputs={'udp://' + config["dst_ip"] + ':' + str(config["dst_port"]): '-c:v libx264 -b:v 10M -pass 2 -acodec copy -f mpegts'}
                    )
        elif config["protocol"] == "RTP":
            return
        elif config["protocol"] == "RTMP":
            return
        else:
            print("协议匹配错误")
            return

        return ff


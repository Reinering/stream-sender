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
                    if TASKLIST_CONFIG[key].__contains__("thread"):
                        TASKLIST_CONFIG[key].__contains__("thread").stop()

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
        self.addInfo(self.tableWidget, p0["playlist"][0].split('/')[-1], p0["send_mode"], p0["protocol"],
                     p0["src_ip"], p0["dst_ip"], p0["dst_port"], p0["out_video_format"], '', '')

    def clearConfig(self):
        self.taskkey = 0
        self.tasklist.clear()
        for key, value in TASKLIST_CONFIG.items():
            if value.__contains__("thread"):
                value.__contains__("thread").stop()
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

    # @pyqtSlot()
    # def on_pushButton_start_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     # raise NotImplementedError
    #     row = self.tableWidget.currentRow()
    #     print("row", row)
    #
    #     if row >= 0:
    #         config = TASKLIST_CONFIG[self.tasklist[row]]
    #         if not config.__contains__("thread"):
    #             config["thread"] = FfmpegThread(row, config)
    #             config["thread"].signal_state.connect(self.setTaskState)
    #         elif config["thread"].isRunning():
    #             return
    #         config["thread"].start()
    #     elif row == -1:
    #         i = 0
    #         for key in self.tasklist:
    #             config = TASKLIST_CONFIG[key]
    #             if not config.__contains__("thread"):
    #                 config["thread"] = FfmpegThread(i, config)
    #                 config["thread"].signal_state.connect(self.setTaskState)
    #             if not config["thread"].isRunning():
    #                 config["thread"].start()
    #             i += 1

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
            self.ffTh.addGevent(row, config)
        elif row == -1:
            i = 0
            for key in self.tasklist:
                config = TASKLIST_CONFIG[key]
                self.ffTh.addGevent(i, config)
                i += 1

    def setTaskState(self, p0):
        print(p0)
        config = TASKLIST_CONFIG[self.tasklist[p0[0]]]
        if isinstance(p0[1], bool):
            config["state"] = p0[1]
            item = self.tableWidget.item(p0[0], 8)
            if p0[1]:
                item.setText(self.translate("MainWindow", "是"))
            else:
                item.setText(self.translate("MainWindow", "否"))
                # item.setFont(self.setCellFont())
        elif isinstance(p0[1], str):
            item = self.tableWidget.item(p0[0], 0)
            item.setText(self.translate("MainWindow", p0[1]))
            config["current_index"] += 1

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
            value["thread"] = None
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
                config = TASKLIST_CONFIG[self.tasklist[row]]
                if config.__contains__("thread") and config["thread"].isRunning():
                    config["thread"].stop()
            elif row == -1:
                for key in self.tasklist:
                    config = TASKLIST_CONFIG[key]
                    if config.__contains__("thread") and config["thread"].isRunning():
                        config["thread"].stop()
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
                config = TASKLIST_CONFIG[self.tasklist[row]]
                if config.__contains__("thread") and config["thread"].isRunning():
                    config["thread"].pause()
            elif row == -1:
                for key in self.tasklist:
                    config = TASKLIST_CONFIG[key]
                    if config.__contains__("thread") and config["thread"].isRunning():
                        config["thread"].pause()
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
                if config.__contains__("thread") and config["thread"].isRunning():
                    config["thread"].next()
        except Exception as e:
            print(e)


class FfmpegThread(QThread):

    signal_state = pyqtSignal(tuple)

    def __init__(self, row, CONFIG, parent=None):
        super(FfmpegThread, self).__init__(parent)
        self.row = row
        self.config = CONFIG
        self.stopBool = False

    # ffmpeg -re -stream_loop -1 -i E:\BaiduYunDownload\zuiyufa.mp4  -vcodec libx264 -acodec copy -f mpegts udp://238.1.238.1:50001
    # ffmpeg -re -stream_loop -1 -i C:\Users\Reiner\Desktop\SNC智取威虎山_截取.ts -vcodec copy -f mpegts udp://238.1.238.1:50001

    def stop(self):
        self.stopBool = True
        try:
            self.killFF()
        except Exception as e:
            print(e)
        # self.signal_state.emit((self.row, False))

    def next(self):
        self.killFF()

    def pause(self):
        self.stop()

    def killFF(self):
        try:
            pid = self.ff.process.pid
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
        self.stopBool = False
        self.signal_state.emit((self.row, True))

        if self.config["send_mode"] == "循环":
            loopType = True
        elif self.config["send_mode"] == "单次":
            loopType = False

        self.send()
        while not self.stopBool and loopType:
            self.send()
        self.signal_state.emit((self.row, False))

    def send(self):
        files = self.config["playlist"]
        for file in files:
            if self.stopBool:
                return
            self.signal_state.emit((self.row, file))
            if self.config["protocol"] == "UDP":
                if self.config["out_video_format"] == "MPEG4":
                    self.ff = ffmpy3.FFmpeg(
                        inputs={file: '-re'},
                        outputs={'udp://' + self.config["dst_ip"] + ':' + str(self.config["dst_port"]): '-vcodec libx264 -acodec copy -f mpegts'}
                    )
                elif self.config["out_video_format"] == "TS":
                    self.ff = ffmpy3.FFmpeg(
                        inputs={file: '-re'},
                        outputs={'udp://' + self.config["dst_ip"] + ':' + str(self.config["dst_port"]): '-vcodec copy -f mpegts'}
                    )
            elif self.config["protocol"] == "RTP":
                return
            elif self.config["protocol"] == "RTMP":
                return
            else:
                print("协议匹配错误")
                return

            print(self.ff.cmd)
            try:
                self.ff.run()
            except Exception as e:
                logging.critical(e)


# Coroutine
class FfmpegCorThread(QThread):

    signal_state = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(FfmpegCorThread, self).__init__(parent)
        self.stopBool = False
        self.loop = asyncio.new_event_loop()
        self.processList = {}

    def stop(self):
        print("结束线程")
        self.stopBool = True
        try:
            self.loop.stop()
            self.loop.close()
        except Exception as e:
            print(e)

    def next(self, row):
        self.killFF()

    def pause(self, row):
        # self.loop.
        try:
            self.processList[row].kill()
        except Exception as e:
            print(e)

    def killFF(self):
        try:
            pid = self.ff.process.pid
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

    def addGevent(self, row, CONFIG):
        self.row = row
        self.config = CONFIG
        asyncio.run_coroutine_threadsafe(self.send(row, CONFIG), self.loop)

    def run1(self):
        self.stopBool = False
        self.signal_state.emit((self.row, True))

        if self.config["send_mode"] == "循环":
            loopType = True
        elif self.config["send_mode"] == "单次":
            loopType = False

        self.send()
        while not self.stopBool and loopType:
            self.send()
        self.signal_state.emit((self.row, False))

    async def send(self, row, config):
        files = config["playlist"]
        for file in files:
            self.signal_state.emit((row, file))
            if config["protocol"] == "UDP":
                if config["out_video_format"] == "MPEG4":
                    ff = ffmpy3.FFmpeg(
                        inputs={file: '-re'},
                        outputs={'udp://' + config["dst_ip"] + ':' + str(config["dst_port"]): '-vcodec libx264 -acodec copy -f mpegts'}
                    )
                elif config["out_video_format"] == "TS":
                    ff = ffmpy3.FFmpeg(
                        inputs={file: '-re'},
                        outputs={'udp://' + config["dst_ip"] + ':' + str(config["dst_port"]): '-vcodec copy -f mpegts'}
                    )
            elif config["protocol"] == "RTP":
                return
            elif config["protocol"] == "RTMP":
                return
            else:
                print("协议匹配错误")
                return

            process = await ff.run_async()
            self.processList[row] = process
            # line_buf = bytearray()
            # while True:
            #     in_buf = (await my_stderr.read(128)).replace(b'\r', b'\n')
            #     if not in_buf:
            #         break
            #     line_buf.extend(in_buf)
            #     while b'\n' in line_buf:
            #         line, _, line_buf = line_buf.partition(b'\n')
            #         print(str(line), file=sys.stderr)
            await ff.wait()
            print("mark")
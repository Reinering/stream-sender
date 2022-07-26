# -*- coding: utf-8 -*-

"""
Module implementing.
author: Reiner New
email: nbxlhc@hotmail.com
"""

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMenu, QMessageBox, QFileDialog, QToolTip
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtGui import QFont, QCursor
import socket
import re
import datetime
import decimal
import time
import ffmpy3
import logging

from manage import TASKLIST_CONFIG, FFMPEG_OPTIONS_DEFAULT
from utils.video import checkVideo
from .Ui_addTask import Ui_addTask
from .videoSetting import SettingDialog
from .showVideoInfo import ShowInfoDialog


class addTask(QDialog, Ui_addTask):
    """
    Class documentation goes here.
    """

    send_data = pyqtSignal(tuple)

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(addTask, self).__init__(parent)
        self.setupUi(self)
        self.translate = QtCore.QCoreApplication.translate
        self.rex_ip = [
            r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$',
            r'^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$'
        ]
        self.videoFormat = ".ts"
        self.ipType = "IPv4"
        self.row = None
        self.key = None
        self.taskInfo = {"playlist": []}
        self.on_pushButton_refresh_clicked()
        self.action = "new"

        self.dstIpList = (
            (
                "238.1.238.1",
                "238.1.238.2",
                "238.1.238.3",
                "238.1.238.4",
                "238.1.238.5",
                "238.1.238.6",
                "238.1.238.7",
                "238.1.238.8",
                "238.1.238.9",
                "238.1.238.10"
            ),
            (
                "FE1E::101:101",
                "FE1E::101:102",
                "FE1E::101:103",
                "FE1E::101:104",
                "FE1E::101:105",
                "FE1E::101:106",
                "FE1E::101:107",
                "FE1E::101:108",
                "FE1E::101:109",
                "FE1E::101:110",
            )
        )

        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 180)
        self.tableWidget.setColumnWidth(2, 180)
        # tooltip
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.cellEntered.connect(self.cellEntered)

        self.params_default = ''
        if FFMPEG_OPTIONS_DEFAULT.__contains__("inputs") and FFMPEG_OPTIONS_DEFAULT["inputs"]:
            self.params_default = "inputs: " + FFMPEG_OPTIONS_DEFAULT["inputs"]

        if FFMPEG_OPTIONS_DEFAULT.__contains__("outputs") and FFMPEG_OPTIONS_DEFAULT["outputs"]:
            if self.params_default:
                self.params_default += ', '
            self.params_default = self.params_default + "outputs: " + FFMPEG_OPTIONS_DEFAULT["outputs"]

        if FFMPEG_OPTIONS_DEFAULT.__contains__("globalputs") and FFMPEG_OPTIONS_DEFAULT["globalputs"]:
            if self.params_default:
                self.params_default += ', '
            self.params_default = self.params_default + "globalputs: " + FFMPEG_OPTIONS_DEFAULT["globalputs"]

    def cellEntered(self, row, column):
        try:
            content = self.tableWidget.item(row, column).text()
        except Exception as e:
            return
        if content:
            QToolTip.showText(QCursor.pos(), content)

    def modifyInfo(self, row, key, tableWidget):
        self.action = "modify"
        self.row = row
        self.key = key
        self.tableWidget_task = tableWidget
        self.setWindowTitle("修改任务")
        self.lineEdit_task.setText(key)
        self.lineEdit_task.setEnabled(False)
        self.comboBox_ip.setCurrentText(TASKLIST_CONFIG[key]["src_ip"])
        self.comboBox_sendMode.setCurrentText(TASKLIST_CONFIG[key]["send_mode"])
        self.comboBox_protocol.setCurrentText(TASKLIST_CONFIG[key]["protocol"])
        self.comboBox_ipType.setCurrentText(TASKLIST_CONFIG[key]["ipType"])
        self.on_pushButton_refresh_clicked()
        self.comboBox_dst_ip.setCurrentText(TASKLIST_CONFIG[key]["dst_ip"])
        self.spinBox_port.setValue(int(TASKLIST_CONFIG[key]["dst_port"]))
        self.comboBox_videoFormat.setCurrentText(TASKLIST_CONFIG[key]["out_video_format"])
        self.comboBox_uri.setCurrentText(TASKLIST_CONFIG[key]["uri"])
        for file in TASKLIST_CONFIG[key]["playlist"]:
            params = ''
            if file.__contains__("inputs") and file["inputs"]:
                params = "inputs: " + file["inputs"]

            if file.__contains__("outputs") and file["outputs"]:
                if params:
                    params += ', '
                params = params + "outputs: " + file["outputs"]

            if file.__contains__("globalputs") and file["globalputs"]:
                if params:
                    params += ', '
                params = params + "globalputs: " + file["globalputs"]

            self.addInfo(self.tableWidget, file["videoFile"],
                         file["subtitleFile"] if file.__contains__("subtitleFile") else '', params)

            self.taskInfo["playlist"].append(file)
        if TASKLIST_CONFIG[key].__contains__("state") and TASKLIST_CONFIG[key]["state"]:
            self.comboBox_ip.setEnabled(False)
            self.pushButton_refresh.setEnabled(False)
            self.comboBox_protocol.setEnabled(False)
            self.comboBox_ipType.setEnabled(False)
            self.comboBox_dst_ip.setEnabled(False)
            self.spinBox_port.setEnabled(False)
            self.comboBox_videoFormat.setEnabled(False)
            self.comboBox_uri.setEnabled(False)

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
        # modify_item.setFont(font)checkVideo
        # modify_item.triggered.connect(self.modifyUser)
        del_item = _menu.addAction("删除")
        del_item.setFont(font)
        check_item = _menu.addAction("查看信息")
        check_item.setFont(font)
        setting_item = _menu.addAction("设置")
        setting_item.setFont(font)

        if self.key and TASKLIST_CONFIG[self.key].__contains__("state") and TASKLIST_CONFIG[self.key]["state"] == 1:
            del_item.setEnabled(False)
            setting_item.setEnabled(False)

        action_menu = _menu.exec_(pos)
        if not action_menu:
            return

        if action_menu.text() == "选择":
            self.redirectPage(True, tableWidget, row)
        else:
            if action_menu.text() == "设置":
                self.settingDialog = SettingDialog()
                self.settingDialog.setParams(row, self.comboBox_videoFormat.currentText(), self.taskInfo["playlist"][row])
                self.settingDialog.setAttribute(Qt.WA_DeleteOnClose, True)
                self.settingDialog.setModal(True)
                self.settingDialog.signal_setting.connect(self.updateTableWidget)
                self.settingDialog.show()
            elif action_menu.text() == "删除":
                button = QMessageBox.information(self, "提示", "确认删除？", QMessageBox.Yes | QMessageBox.No)
                if button == QMessageBox.Yes:
                    self.taskInfo["playlist"].pop(row)
                    tableWidget.removeRow(row)
            elif action_menu.text() == "查看信息":
                try:
                    stdout = checkVideo(self.taskInfo["playlist"][row]["videoFile"])
                    self.showInfoDialog = ShowInfoDialog()
                    self.showInfoDialog.setAttribute(Qt.WA_DeleteOnClose, True)
                    self.showInfoDialog.setModal(True)
                    self.showInfoDialog.textBrowser.setText(str(stdout[0], encoding="utf-8"))
                    self.taskInfo["playlist"][row]["videoInfo"] = stdout[0]
                    self.showInfoDialog.show()
                except ffmpy3.FFExecutableNotFoundError as e:
                    logging.error("错误, 未找到ffprobe {}".format(e))
                    QMessageBox.critical(self, "错误", "未找到ffprobe")
                except ffmpy3.FFRuntimeError as e:
                    logging.error("错误, ffprobe执行错误 {}".format(e))
                    QMessageBox.critical(self, "错误", "ffprobe执行错误")
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
    #
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

    def updateTableWidget(self, p0):
        if isinstance(p0, tuple):
            if self.taskInfo["playlist"][p0[0]].__contains__("subtitleFile") and self.taskInfo["playlist"][p0[0]]["subtitleFile"]:
                self.tableWidget.item(p0[0], 1).setText(self.taskInfo["playlist"][p0[0]]["subtitleFile"])
            else:
                self.tableWidget.item(p0[0], 1).setText('')

            params = ''
            if self.taskInfo["playlist"][p0[0]].__contains__("inputs") \
                and self.taskInfo["playlist"][p0[0]]["inputs"]:
                params = "inputs: " + self.taskInfo["playlist"][p0[0]]["inputs"]

            if self.taskInfo["playlist"][p0[0]].__contains__("outputs") \
                    and self.taskInfo["playlist"][p0[0]]["outputs"]:
                if params:
                    params += ', '
                params = params + "outputs: " + self.taskInfo["playlist"][p0[0]]["outputs"]

            if self.taskInfo["playlist"][p0[0]].__contains__("globalputs") \
                    and self.taskInfo["playlist"][p0[0]]["globalputs"]:
                if params:
                    params += ', '
                params = params + "globalputs: " + self.taskInfo["playlist"][p0[0]]["globalputs"]

            if params:
                self.tableWidget.item(p0[0], 2).setText(params)

    def getFiles(self, p0):
        print("p0", p0)

    @pyqtSlot()
    def on_pushButton_openPath_clicked(self):
        """
        Slot documentation goes here.
        """
        print("点击选择文件")
        try:
            # self.fileDialog = QFileDialog()
            # self.fileDialog.setAttribute(Qt.WA_DeleteOnClose, True)
            # self.fileDialog.setModal(True)
            # self.fileDialog.setFileMode(3)
            # self.fileDialog.filesSelected.connect(self.getFiles)
            # self.fileDialog.setNameFilters(["vedio Files(*.ts)",
            #                                "vedio Files(*.mp4)",
            #                                "vedio Files(*.avi)",
            #                                "vedio Files(*.mkv)",
            #                                "vedio Files(*.flv)",
            #                                "all Files(*.*)"])
            # self.fileDialog.show()

            files = QFileDialog.getOpenFileNames(self, u"选择视频文件", "/",
                                                           "vedio Files(*.ts);;"
                                                           "vedio Files(*.mp4);;"
                                                           "vedio Files(*.avi);;"
                                                           "vedio Files(*.mkv);;"
                                                           "vedio Files(*.flv);;"
                                                           "all Files(*.*)")
            for file in files[0]:
                self.addInfo(self.tableWidget, file, '', self.params_default)
                tmp = {"videoFile": file}
                tmp.update(FFMPEG_OPTIONS_DEFAULT)
                self.taskInfo["playlist"].append(tmp)
        except Exception as e:
            print(e)

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
            if self.ipType == "IPv4":
                result = re.match(self.rex_ip[0], ipAddr)
            elif self.ipType == "IPv6" and ipAddr[:4] != "fe80" and ipAddr[:4] != "FE80":
                result = re.match(self.rex_ip[1], ipAddr)
            else:
                continue
            if not result:
                continue
            self.comboBox_ip.addItem("")
            self.comboBox_ip.setItemText(i, self.translate("MainWindow", ipAddr))
            i += 1

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

        task = self.lineEdit_task.text()
        if not task:
            QMessageBox.critical(self, "错误", "任务名不能为空")
            return
        if self.action == "new" and task != "TASK" and TASKLIST_CONFIG.__contains__(task):
            QMessageBox.critical(self, "错误", "任务名不能重复")
            return

        sendMode = self.comboBox_sendMode.currentText()
        if not sendMode:
            return

        protocol = self.comboBox_protocol.currentText()
        if not protocol:
            return

        ipType = self.comboBox_ipType.currentText()

        dst_ip = self.comboBox_dst_ip.currentText()
        if not dst_ip:
            QMessageBox.critical(self, "错误", "组播地址不能为空")
            return
        if self.ipType == "IPv4" and not re.match(self.rex_ip[0], dst_ip) or self.ipType == "IPv6" and not re.match(self.rex_ip[1], dst_ip):
            QMessageBox.critical(self, "错误", "IP地址格式错误，请重新输入")
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
        uri = self.comboBox_uri.currentText()

        if self.action == "new":
            self.taskInfo["protocol"] = protocol
            self.taskInfo["ipType"] = ipType
            self.taskInfo["dst_ip"] = dst_ip
            self.taskInfo["dst_port"] = port
            self.taskInfo["src_ip"] = src_ip
            self.taskInfo["send_mode"] = sendMode
            self.taskInfo["out_video_format"] = videoFormat
            self.taskInfo["uri"] = uri

            self.send_data.emit((task, self.taskInfo))
        elif self.action == "modify":
            TASKLIST_CONFIG[self.key]["protocol"] = protocol
            TASKLIST_CONFIG[self.key]["ipType"] = ipType
            TASKLIST_CONFIG[self.key]["dst_ip"] = dst_ip
            TASKLIST_CONFIG[self.key]["dst_port"] = port
            TASKLIST_CONFIG[self.key]["src_ip"] = src_ip
            TASKLIST_CONFIG[self.key]["send_mode"] = sendMode
            TASKLIST_CONFIG[self.key]["out_video_format"] = videoFormat
            TASKLIST_CONFIG[self.key]["playlist"] = self.taskInfo["playlist"]
            TASKLIST_CONFIG[self.key]["out_video_format"] = videoFormat
            TASKLIST_CONFIG[self.key]["uri"] = uri

            if not TASKLIST_CONFIG[self.key].__contains__("state") or TASKLIST_CONFIG[self.key]["state"]:
                self.tableWidget_task.item(self.row, 1).setText(TASKLIST_CONFIG[self.key]["playlist"][TASKLIST_CONFIG[self.key]["current_index"]]["videoFile"].split('/')[-1])
            self.tableWidget_task.item(self.row, 2).setText(TASKLIST_CONFIG[self.key]["send_mode"])
            self.tableWidget_task.item(self.row, 3).setText(TASKLIST_CONFIG[self.key]["protocol"])
            self.tableWidget_task.item(self.row, 4).setText(TASKLIST_CONFIG[self.key]["src_ip"])
            self.tableWidget_task.item(self.row, 5).setText(TASKLIST_CONFIG[self.key]["dst_ip"])
            self.tableWidget_task.item(self.row, 6).setText(str(TASKLIST_CONFIG[self.key]["dst_port"]))
            self.tableWidget_task.item(self.row, 7).setText(TASKLIST_CONFIG[self.key]["out_video_format"])

        time.sleep(1)
        self.close()
    
    @pyqtSlot(str)
    def on_comboBox_dst_ip_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if p0 == "224.1.1.1":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.2":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.3":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.4":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.5":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.6":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.7":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.8":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.9":
            self.spinBox_port.setValue(1234)
        elif p0 == "224.1.1.10":
            self.spinBox_port.setValue(1234)
        elif p0 == "238.1.238.1" or p0 == "FE1E::101:101":
            self.spinBox_port.setValue(50001)
        elif p0 == "238.1.238.2" or p0 == "FE1E::101:102":
            self.spinBox_port.setValue(50002)
        elif p0 == "238.1.238.3" or p0 == "FE1E::101:103":
            self.spinBox_port.setValue(50003)
        elif p0 == "238.1.238.4" or p0 == "FE1E::101:104":
            self.spinBox_port.setValue(50004)
        elif p0 == "238.1.238.5" or p0 == "FE1E::101:105":
            self.spinBox_port.setValue(50005)
        elif p0 == "238.1.238.6" or p0 == "FE1E::101:106":
            self.spinBox_port.setValue(50006)
        elif p0 == "238.1.238.7" or p0 == "FE1E::101:107":
            self.spinBox_port.setValue(50007)
        elif p0 == "238.1.238.8" or p0 == "FE1E::101:108":
            self.spinBox_port.setValue(50008)
        elif p0 == "238.1.238.9" or p0 == "FE1E::101:109":
            self.spinBox_port.setValue(50009)
        elif p0 == "238.1.238.10" or p0 == "FE1E::101:110":
            self.spinBox_port.setValue(50010)
        elif p0 == "238.1.238.11":
            self.spinBox_port.setValue(50011)
        elif p0 == "238.1.238.12":
            self.spinBox_port.setValue(50012)
        elif p0 == "238.1.238.51":
            self.spinBox_port.setValue(5051)
        elif p0 == "238.1.238.52":
            self.spinBox_port.setValue(5052)
        elif p0 == "238.1.238.53":
            self.spinBox_port.setValue(5053)
        elif p0 == "238.1.238.54":
            self.spinBox_port.setValue(5054)
    
    @pyqtSlot()
    def on_pushButton_up_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        row = self.tableWidget.currentRow()
        if row <= 0:
            return
        for i in range(self.tableWidget.columnCount()):
            try:
                item1 = self.tableWidget.item(row, i).text()
            except Exception as e:
                item1 = None
            try:
                item0 = self.tableWidget.item(row-1, i).text()
            except Exception as e:
                item0 = None

            if item1 != None and item0 != None:
                if item0 == item1:
                    continue
                self.tableWidget.item(row, i).setText(item0)
                self.tableWidget.item(row-1, i).setText(item1)
            elif item1 == None and item0 == None:
                continue
            else:
                if item1 == None:
                    self.tableWidget.item(row, i).setText(item0)
                    self.tableWidget.removeCellWidget(row-1, i)
                else:
                    self.tableWidget.item(row-1, i).setText(item1)
                    self.tableWidget.removeCellWidget(row, i)

        tmp = self.taskInfo["playlist"][row]
        self.taskInfo["playlist"][row] = self.taskInfo["playlist"][row-1]
        self.taskInfo["playlist"][row-1] = tmp

    @pyqtSlot()
    def on_pushButton_down_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        row = self.tableWidget.currentRow()
        if row < 0 or row >= self.tableWidget.rowCount() - 1:
            return
        for i in range(self.tableWidget.columnCount()):
            try:
                item0 = self.tableWidget.item(row, i).text()
            except Exception as e:
                item0 = None
            try:
                item1 = self.tableWidget.item(row+1, i).text()
            except Exception as e:
                item1 = None

            if item1 != None and item0 != None:
                if item0 == item1:
                    continue
                self.tableWidget.item(row, i).setText(item1)
                self.tableWidget.item(row+1, i).setText(item0)
            elif item1 == None and item0 == None:
                continue
            else:
                if item0 == None:
                    self.tableWidget.item(row, i).setText(item1)
                    self.tableWidget.removeCellWidget(row+1, i)
                else:
                    self.tableWidget.item(row+1, i).setText(item0)
                    self.tableWidget.removeCellWidget(row, i)

        tmp = self.taskInfo["playlist"][row]
        self.taskInfo["playlist"][row] = self.taskInfo["playlist"][row+1]
        self.taskInfo["playlist"][row+1] = tmp
    
    @pyqtSlot(str)
    def on_comboBox_ipType_currentTextChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.ipType = p0
        self.comboBox_dst_ip.clear()
        self.comboBox_ip.clear()
        self.addDstIp()
        self.on_pushButton_refresh_clicked()

    def addDstIp(self):
        if self.ipType == "IPv4":
            index = 0
        elif self.ipType == "IPv6":
            index = 1
        else:
            return

        i = 1
        self.comboBox_dst_ip.addItem("")
        self.comboBox_dst_ip.setItemText(i, self.translate("MainWindow", ''))
        for ip in self.dstIpList[index]:
            self.comboBox_dst_ip.addItem("")
            self.comboBox_dst_ip.setItemText(i, self.translate("MainWindow", ip))
            i += 1








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tk = QtWidgets.QDialog()
    ui = addTask()
    ui.setupUi(tk)
    ui.show()
    sys.exit(app.exec_())
    


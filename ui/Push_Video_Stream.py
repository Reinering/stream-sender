# -*- coding: utf-8 -*-

"""
Module implementing mainWindow.
"""
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread
from PyQt5 import QtGui

from Ui_Push_Video_Stream import Ui_MainWindow
import socket
import re
import subprocess
import time
import ffmpy3


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self._translate = QtCore.QCoreApplication.translate

        self.videoFormat = ".ts"
        self.threadList = []

        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 70)
        self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.setColumnWidth(6, 50)

        self.on_pushButton_refresh_clicked()


    #添加任务
    @pyqtSlot()
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        IP和Port必须加校验
        """
        filePath = self.lineEdit_filePath.text()
        if filePath == "":
            warning = QtWidgets.QMessageBox.warning(self, u"提示", u"请选择流文件")
            return

        videoFormat = self.comboBox_videoFormat.currentText()
        if videoFormat == "":
            warning = QtWidgets.QMessageBox.warning(self, u"提示", u"请选择视频格式")
            return

        protocol = self.comboBox_protocol.currentText()
        if protocol == "":
            warning = QtWidgets.QMessageBox.warning(self, u"提示", u"请选择协议")
            return

        source_ip = self.comboBox_ip.currentText()
        if source_ip == "":
            warning = QtWidgets.QMessageBox.warning(self, u"提示", u"请选择输入源IP地址")
            return

        multiCast_ip = self.comboBox_multiIp.currentText()
        if multiCast_ip == "":
            warning = QtWidgets.QMessageBox.warning(self, u"提示", u"请选择输入组播IP地址")
            return

        port = self.spinBox_port.text()
        if port == "":
            warning = QtWidgets.QMessageBox.warning(self, u"提示", u"请选择输入组播端口")
            return

        ffTh = FfmpegThread(filePath, videoFormat, protocol, source_ip, multiCast_ip, port)
        ffTh.signal_stop.connect(self.on_pushButton_stop_clicked)
        self.threadList.append(ffTh)
        # print(self.threadList)
        self.addTableWidget(filePath, videoFormat, protocol, source_ip, multiCast_ip, port, "是")
        # ffTh.signal_textBroser.connect(self.setTextBrowser)
        ffTh.start()
        # self.textBrowser.append(filePath + videoFormat + protocol + source_ip + multiCast_ip + port + "是")

    #刷新，获取设备上所有IPv4接口地址
    @pyqtSlot()
    def on_pushButton_refresh_clicked(self):
        """
        Slot documentation goes here.
        """
        addrs = socket.getaddrinfo(socket.gethostname(), None)
        i = 0
        for addr in addrs:
            ipAddr = addr[-1][0]
            print(ipAddr)
            ipv4 = re.findall(r"\d+\.\d+\.\d+\.\d+", ipAddr)
            if len(ipv4) != 0 :
                print("combox add", ipv4[0])
                self.comboBox_ip.addItem("")
                self.comboBox_ip.setItemText(i, self._translate("MainWindow", ipv4[0]))
            i += 1

    #获取文件路径
    @pyqtSlot()
    def on_pushButton_openPath_clicked(self):
        """
        Slot documentation goes here.
        """
        print("点击选择文件")
        try:
            download_path = QtWidgets.QFileDialog.getOpenFileName(self, u"选择视频文件", "/",
                                                                  "vedio Files(*" + self.videoFormat + ")")
            # print(download_path[0])
            self.lineEdit_filePath.clear()
            self.lineEdit_filePath.setText(self._translate("MainWindow", download_path[0]))
        except Exception as e:
            print(e)

    #更改视频文件格式
    @pyqtSlot(str)
    def on_comboBox_videoFormat_currentTextChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type str
        """
        if p0 == "TS":
            self.videoFormat = ".ts"
        elif p0 == "MPEG4" or p0 == "MKV":
            self.videoFormat = ".mp4"
        # print(self.videoFormat)
        self.comboBox_videoFormat.clear()

    # tableWidget添加任务
    def addTableWidget(self, filePath, videoFormat, protocol, source_ip, multiCast_ip, port, state):
        print("TableWidget增加一行")
        tmpList = filePath.split('/')
        row = len(self.threadList) -1
        self.tableWidget.setRowCount(row+1)
        # print("row", row)

        # print(tmpList[-1])
        item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(self._translate("MainWindow", tmpList[-1]))
        item.setFont(self.setCellFont())
        self.tableWidget.setItem(row, 0, item)

        # print(protocol)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(self._translate("MainWindow", protocol))
        item.setFont(self.setCellFont())
        self.tableWidget.setItem(row, 1, item)

        # print(source_ip)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(self._translate("MainWindow", source_ip))
        item.setFont(self.setCellFont())
        self.tableWidget.setItem(row, 2, item)

        # print(multiCast_ip)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(self._translate("MainWindow", multiCast_ip))
        item.setFont(self.setCellFont())
        self.tableWidget.setItem(row, 3, item)

        # print(port)
        item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(self._translate("MainWindow", port))
        item.setFont(self.setCellFont())
        self.tableWidget.setItem(row, 4, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText(self._translate("MainWindow", state))
        item.setFont(self.setCellFont())
        self.tableWidget.setItem(row, 6, item)

    def setCellFont(self):
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        return font


    # 线程开始启动
    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        row = self.tableWidget.currentRow()
        # print('row', row)
        if row >= 0:
            self.threadList[row].start()
            item = self.tableWidget.item(row, 6)
            item.setText(self._translate("MainWindow", "是"))
            # item.setFont(self.setCellFont())
            self.tableWidget.setItem(row, 6, item)

    # 线程停止
    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        try:
            row = self.tableWidget.currentRow()
            # print('row', row)
            self.threadList[row].stop()
            item = self.tableWidget.item(row, 6)
            item.setText(self._translate("MainWindow", "否"))
            # item.setFont(self.setCellFont())
            self.tableWidget.setItem(row, 6, item)
        except Exception as e:
            print(e)


    # 任务删除
    @pyqtSlot()
    def on_pushButton_del_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        print("任务删除")
        row = self.tableWidget.currentRow()
        print('row', row)
        if row >= 0:
            try:
                self.threadList[row].stop()
                time.sleep(0.5)
                self.threadList.pop(row)
            except IndexError as e:
                print(e)
            finally:
                self.tableWidget.removeRow(row)

    # 清除所有任务
    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError

        for i in range(0,len(self.threadList)):
            self.threadList[0].stop()

            try:
                self.threadList.pop(0)
            except IndexError as e:
                print(e)
            finally:
                self.tableWidget.removeRow(0)
    # 打开配置
    @pyqtSlot()
    def on_pushButton_open_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        try:
            filepath = QtWidgets.QFileDialog.getOpenFileName(self, u"打开文件", "/", "*.cfg")
            # print(filepath)
            filename = filepath[0]
            if filename != '':
                f = open(filename, 'r')
                lines = f.readlines()
                if len(lines) > 0:
                    self.on_pushButton_clear_clicked()
                    for line in lines:
                        cfg = line.split(',')
                        # print(cfg)
                        ffTh = FfmpegThread(cfg[0], cfg[1], cfg[2], cfg[3], cfg[4], cfg[5])
                        self.threadList.append(ffTh)
                        self.addTableWidget(cfg[0], cfg[1], cfg[2], cfg[3], cfg[4], cfg[5], "否")
        except Exception as e:
            print(e)


    #保存配置
    @pyqtSlot()
    def on_pushButton_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # raise NotImplementedError
        try:
            filepath = QtWidgets.QFileDialog.getSaveFileName(self, u"保存文件", "/", ".cfg")
            filename = filepath[0] + filepath[1]
            print(filename)
            if filename != '':
                f = open(filename, 'w+')
                for th in self.threadList:
                    line = th.filePath + ',' + th.videoFormat + ',' + th.protocol + ',' + th.source_ip + ',' + th.multiCast_ip + ',' + th.port + '\n'
                    f.write(line)
                f.close()
        except TypeError as e:
            print(e)

    @pyqtSlot(str)
    def on_comboBox_multiIp_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # raise NotImplementedError
        print(p0)
        if p0 == "238.1.238.1":
            self.spinBox_port.setValue(50001)
        elif p0 == "238.1.238.2":
            self.spinBox_port.setValue(50002)
        elif p0 == "238.1.238.3":
            self.spinBox_port.setValue(50003)
        elif p0 == "238.1.238.4":
            self.spinBox_port.setValue(50004)
        elif p0 == "238.1.238.5":
            self.spinBox_port.setValue(50005)
        elif p0 == "238.1.238.6":
            self.spinBox_port.setValue(50006)
        elif p0 == "238.1.238.7":
            self.spinBox_port.setValue(50007)
        elif p0 == "238.1.238.8":
            self.spinBox_port.setValue(50008)
        elif p0 == "238.1.238.9":
            self.spinBox_port.setValue(50009)
        elif p0 == "238.1.238.10":
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

    def closeEvent(self, *args, **kwargs):
        print("关闭窗口")
        self.on_pushButton_clear_clicked()

    # def setTextBrowser(self, p0):
    #     self.textBrowser.append(p0)


class FfmpegThread(QThread):
    signal_stop = pyqtSignal()
    def __init__(self, filePath, videoFormat, protocol, source_ip, multiCast_ip, port, parent=None):
        super(FfmpegThread, self).__init__(parent)
        self.filePath = filePath
        self.videoFormat =videoFormat
        self.protocol = protocol
        self.source_ip = source_ip
        self.multiCast_ip = multiCast_ip
        self.port = port

        # ffmpeg -re -stream_loop -1 -i E:\BaiduYunDownload\zuiyufa.mp4  -vcodec libx264 -acodec copy -f mpegts udp://238.1.238.1:50001
        # ffmpeg -re -stream_loop -1 -i C:\Users\Reiner\Desktop\SNC智取威虎山_截取.ts -vcodec copy -f mpegts udp://238.1.238.1:50001

    def run(self):
        if self.protocol == "UDP":
            if self.videoFormat == "MPEG4":
                self.ff = ffmpy3.FFmpeg(
                    inputs={self.filePath: '-re -stream_loop -1'},
                    outputs={'udp://' + self.multiCast_ip + ':' + self.port: '-vcodec libx264 -acodec copy -f mpegts'}
                )
            elif self.videoFormat == "TS":
                self.ff = ffmpy3.FFmpeg(
                    inputs={self.filePath: '-re -stream_loop -1'},
                    outputs={'udp://' + self.multiCast_ip + ':' + self.port: '-vcodec copy -f mpegts'}
                )
        elif self.protocol == "RTP":
            return
        elif self.protocol == "RTMP":
            return
        else:
            print("协议匹配错误")
            return

        # self.ff.cmd
        try:
            self.ff.run()
        except Exception as e:
            print(e)
            self.signal_stop.emit()

    def stop(self):
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    


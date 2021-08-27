# -*- coding: utf-8 -*-

"""
Module implementing FFmpegHelpDialog.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QTextDocument, QTextCursor, QTextCharFormat

from .Ui_ffmpegHelp import Ui_Dialog


class FFmpegHelpDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(FFmpegHelpDialog, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.searchText = ''
        self.searchIter = None

    # 搜索文本框中特定的字符串并改变为红色
    def search(self, edit, search_str):
        foundBool = False
        # document = QTextDocument()
        document = edit.document()
        highlight_cursor = QTextCursor(document)
        cursor = QTextCursor(document)
        cursor.beginEditBlock()
        color_format = QTextCharFormat(highlight_cursor.charFormat())
        color_format.setForeground(Qt.red)
        while (not highlight_cursor.isNull()) and (not highlight_cursor.atEnd()):
            highlight_cursor = document.find(search_str, highlight_cursor)
            if not highlight_cursor.isNull():
                foundBool = True
                highlight_cursor.mergeCharFormat(color_format)
        cursor.endEditBlock()
        if not foundBool:
            QMessageBox.information(self, "提示", "未找到相关文本")

    # 清楚文本框状态
    def clearChartFormat(self, textBrowser):
        cursor = textBrowser.textCursor()
        color_format = QTextCharFormat(cursor.charFormat())
        color_format.setForeground(Qt.black)
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(color_format)
        cursor.clearSelection()
        # textBrowser.setTextCursor(cursor)

    # 找到下一个
    def searchNext(self,  textBrowser, search_str):
        document = textBrowser.document()
        highlight_cursor = QTextCursor(document)
        cursor = QTextCursor(document)
        cursor.beginEditBlock()
        color_format = QTextCharFormat(highlight_cursor.charFormat())
        color_format.setForeground(Qt.red)

        while True:
            if not highlight_cursor.isNull():
                highlight_cursor.mergeCharFormat(color_format)
                # highlight_cursor.setCharFormat(color_format)

            highlight_cursor = document.find(search_str, highlight_cursor)
            if highlight_cursor.isNull():
                cursor.beginEditBlock()
            else:
                textBrowser.setTextCursor(highlight_cursor)

            yield highlight_cursor.position()

    @pyqtSlot()
    def on_lineEdit_search_returnPressed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        search = self.lineEdit_search.text()
        if self.searchText != search:
            if self.searchText:
                self.clearChartFormat(self.textBrowser)
            if not search:
                return

            self.search(self.textBrowser, search, )
            self.searchIter = self.searchNext(self.textBrowser, search)
            self.searchText = search
        else:
            if not self.searchIter:
                return

            next(self.searchIter)


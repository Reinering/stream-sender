# -*- coding: utf-8 -*-

"""
Module implementing AdvanceSettingDialog.
author: Reiner New
email: nbxlhc@hotmail.com.com
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox

from FileTypeAsk import AskDialog
from Ui_AdvanceSetting import Ui_Dialog


class AdvanceSettingDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(AdvanceSettingDialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        print("点击添加文件")
        self.askDialog = AskDialog()
        self.askDialog.setAttribute(Qt.WA_DeleteOnClose, True)
        self.askDialog.setModal(True)
        self.askDialog.signal_file.connect(self.receiverFileType)
        self.askDialog.show()

    def receiverFileType(self, a0):
        try:
            if a0 == "video":
                files = QFileDialog.getOpenFileNames(self, u"选择视频文件", "/",
                                                     "video Files(*.ts);;"
                                                     "video Files(*.mp4);;"
                                                     "video Files(*.avi);;"
                                                     "video Files(*.mkv);;"
                                                     "video Files(*.flv);;"
                                                     "all Files(*.*)")
            elif a0 == "audio":
                files = QFileDialog.getOpenFileNames(self, u"选择音频文件", "/",
                                                     "audio Files(*.mp3);;"
                                                     "audio Files(*.wav);;"
                                                     "audio Files(*.ape);;"
                                                     "audio Files(*.flac);;"
                                                     "audio Files(*.acc);;"
                                                     "all Files(*.*)")
            elif a0 == "pic":
                files = QFileDialog.getOpenFileNames(self, u"选择图像文件", "/",
                                                     "pic Files(*.jpg);;"
                                                     "pic Files(*.jpeg);;"
                                                     "pic Files(*.bmp);;"
                                                     "pic Files(*.png);;"
                                                     "all Files(*.*)")
            elif a0 == "sub":
                files = QFileDialog.getOpenFileNames(self, u"选择字幕文件", "/",
                                                     "sub Files(*.srt);;"
                                                     "sub Files(*.ass);;"
                                                     "all Files(*.*)")
            else:
                return

            for file in files[0]:
                self.addInfo(self.tableWidget, file, '', self.params_default)
                tmp = {"videoFile": file}
                # tmp.update(FFMPEG_OPTIONS_DEFAULT)
                self.taskInfo["playlist"].append(tmp)

        except Exception as e:
            print(e)

    @pyqtSlot()
    def on_pushButton_del_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        pass






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = AdvanceSettingDialog()
    ui.show()
    sys.exit(app.exec_())

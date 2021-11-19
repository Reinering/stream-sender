# -*- coding: utf-8 -*-

"""
Module implementing AdvanceSettingDialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication

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






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = AdvanceSettingDialog()
    ui.show()
    sys.exit(app.exec_())

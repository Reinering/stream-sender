# -*- coding: utf-8 -*-

"""
Module implementing ShowInfoDialog.
author: Reiner New
email: nbxlhc@hotmail.com.com
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_showVideoInfo import Ui_Dialog


class ShowInfoDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(ShowInfoDialog, self).__init__(parent)
        self.setupUi(self)

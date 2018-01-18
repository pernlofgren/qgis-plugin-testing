# -*- coding: utf-8 -*-

import os

from PyQt4 import uic
from PyQt4.QtGui import QDialog, QFileDialog
from PyQt4.QtCore import pyqtSignal, pyqtSlot, QSettings

from qgis.core import QgsApplication


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), "dialog.ui"))


class Dialog(QDialog, FORM_CLASS):

    closingDialog = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.init_gui()

        # Button signals
        # self.chk_default.clicked.connect()

        # Dropdown signals
        self.box_layer.currentIndexChanged.connect(self.populate_field_list)
        self.box_upd_layer.currentIndexChanged.connect(self.populate_field_list)

    def init_gui(self):
        """Setup initial state of dialog box"""
        pass

    @pyqtSlot()
    def populate_field_list(self, combo_box):
        """Updates the field list available"""
        pass

    def closeEvent(self, event):
        self.closingDialog.emit()
        event.accept()

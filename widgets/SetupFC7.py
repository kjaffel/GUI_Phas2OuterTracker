from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class SetupFC7(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        ui = loadUi('widgets_ui/setup_FC7.ui', self) 
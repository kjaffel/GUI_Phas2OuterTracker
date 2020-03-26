from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class NewIssue(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        ui = loadUi('widgets_ui/new_issue.ui', self) 
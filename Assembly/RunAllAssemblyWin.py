import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)


class Ui_Assembly(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Assembly, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('/home/jaffel/Phas2OuterTracker/GUI_Phase2OuterTracker/Assembly/assembly.ui', self) # Load the .ui file
        #self.MainWindow.hide()             # hide the main window and open the 2nd one 
        self.setCentralWidget(StackedWidget())
        self.show()


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



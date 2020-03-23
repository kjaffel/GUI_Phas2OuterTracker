#References
#https://www.devdungeon.com/content/python3-qt5-pyqt5-tutorial#toc-15

"""
Work in progress :
    This script should get all .ui files from Help/ FC7/ ModulesNavigator/ and more ...
    get a logic in opening each window and pushing each button  
"""


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

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap('/Icons/digitaal60.jpg'))
        QStackedWidget.paintEvent(self, event)

class MdiArea(QMdiArea):
    def __init__(self, parent=None):
        QMdiArea.__init__(self, parent=parent)

    def paintEvent(self, event):
        QMdiArea.paintEvent(self, event)
        painter = QPainter(self.viewport())
        painter.drawPixmap(self.rect(), QPixmap('/Icons/digitaal60.jpg'))

class Ui_ModulesNavigator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_ModulesNavigator, self).__init__() 
        uic.loadUi('/ModulesNavigator/modulesnavigator.ui', self) 
        #self.MainWindow.hide()              
        self.setCentralWidget(StackedWidget())
        self.show()
        self.pushButton_2.clicked.connect(QApplication.instance().quit)
        self.pushButton.clicked.connect(self.OpenEvent)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plotwidget = PlotWidget(self.centralwidget)
        self.plotwidget.setObjectName("plotwidget")
        self.gridLayout.addWidget(self.plotwidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class Ui_setupFC7(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_setupFC7, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('FC7/setupfc7.ui', self) # Load the .ui file
        #self.MainWindow.hide()             # hide the main window and open the 2nd one 
        self.setCentralWidget(StackedWidget())
        self.show()

    #def __init__(self, parent):
    #    QtWidgets.__init__(self)
    #    self.ui = Ui_DialogFC7config()
    #    self.ui.setupUi(self)
    #    self.parent = parent
    #    #try ...
    #    self.tree = ET.parse('D19CDescription.xml')
    #    self.root = self.tree.getroot()
    #    connection_str = self.root[0][0].get('uri')
    #    self.connection_param = re.split(":",connection_str)
    #    host = self.connection_param[1][2:]
    #    self.target = re.split("=", self.connection_param[2])
    #    fc7IP = self.target[1]

    #    self.ui.lineEdit.setText(host)
    #    self.ui.lineEdit_2.setText(fc7IP)
    #    self.show()

    #def accept(self):
    #    host = self.ui.lineEdit.text()
    #    fc7IP = self.ui.lineEdit_2.text()
    #    connection_str = f'{self.connection_param[0]}://{host}:{self.target[0]}={fc7IP}:{self.connection_param[3]}'
    #    self.root[0][0].set('uri',connection_str)
    #    self.tree.write('D19CDescription.xml')
    #    self.parent.ui.statusBar.showMessage("New settings saved",5000)
    #    self.close()

    #def reject(self):
    #    self.close()


class Ui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__() 
        uic.loadUi('Login/ssh.ui', self) 
        #QMainWindow.__init__(self, parent=parent)
        #self.setCentralWidget(StackedWidget())
        #self.setCentralWidget(MdiArea())
        self.show() # Show the GUI
        self.pushButton_2.clicked.connect(QApplication.instance().quit)
        self.pushButton.clicked.connect(self.OpenEvent)

    
    def OpenEvent(self):
        self.fc7window=QtWidgets.QMainWindow()
        self.ui=Ui_setupFC7()
        #self.fc7window.hide()
        #self.fc7window.show()
        
        self.modulesNavigator=QtWidgets.QMainWindow()
        self.ui=Ui_ModulesNavigator()


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




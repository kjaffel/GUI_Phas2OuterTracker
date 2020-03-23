import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_Help(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Help, self).__init__()
        uic.loadUi('IssuesWin.ui', self) 
        #self.setCentralWidget(stackedWidget())
        self.show()
        
        self.PushButton1.clicked.connect(self.OpenWindow1)
        self.new_issue.clicked.connect(self.ON_NewIssue)



        self.PushButton2.clicked.connect(self.OpenWindow2)

    def OpenWindow1(self):
        self.QtStack.setCurrentIndex(1)

    def OpenWindow2(self):
        self.QtStack.setCurrentIndex(2)
        
        
        
        
        self.cancel_issue.clicked.connect(QApplication.instance().quit)
        self.new_issue.clicked.connect(self.ON_NewIssue)
        self.attach_file.clicked.connect(self.ON_AttachFile)

    def ON_AttachFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home', "All Files (*);;Python Files (*.py)", options=options)

    def ON_NewIssue(self):
        self.QStackWidgets.page.QWidget()
        #setCurrentIndex(1)
        #self.page=QtWidgets.QMainWindow()
        #self.page.show()
    #    self.ui=Ui_setupFC7()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Ui_Help()
    window.show()
    sys.exit(application.exec_())


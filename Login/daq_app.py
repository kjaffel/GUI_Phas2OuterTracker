# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daq_app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Ui_DAQ_APP(object):
    def setupUi(self, DAQ_APP):
        DAQ_APP.setObjectName("DAQ_APP")
        #DAQ_APP.resize(800, 600)
        DAQ_APP.resize(500,250)
        DAQ_APP.move(300,300)
        self.centralwidget = QtWidgets.QWidget(DAQ_APP)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 150, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(QApplication.instance().quit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 81, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 161, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 100, 161, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        DAQ_APP.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(DAQ_APP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        DAQ_APP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DAQ_APP)
        self.statusbar.setObjectName("statusbar")
        DAQ_APP.setStatusBar(self.statusbar)

        self.retranslateUi(DAQ_APP)
        QtCore.QMetaObject.connectSlotsByName(DAQ_APP)

    def retranslateUi(self, DAQ_APP):
        _translate = QtCore.QCoreApplication.translate
        DAQ_APP.setWindowTitle(_translate("DAQ_APP", "DAQ_APP"))
        self.pushButton.setText(_translate("DAQ_APP", "submit"))
        self.pushButton_2.setText(_translate("DAQ_APP", "cancel"))
        self.label_2.setText(_translate("DAQ_APP", "Password"))
        self.label_3.setText(_translate("DAQ_APP", "Username"))
#-------------- To check it doesn't seems work 
    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def setWindowFlags(self, flags):
        super(PreviewWindow, self).setWindowFlags(flags)

        flag_type = (flags & Qt.WindowType_Mask)

        if flag_type == Qt.Window:
            text = "Qt.Window"
        elif flag_type == Qt.Dialog:
            text = "Qt.Dialog"
        elif flag_type == Qt.Sheet:
            text = "Qt.Sheet"
        elif flag_type == Qt.Drawer:
            text = "Qt.Drawer"
        elif flag_type == Qt.Popup:
            text = "Qt.Popup"

# https://techwithtim.net/tutorials/pyqt5-tutorial/messageboxes/
    def show_popup(self, DAQ_APP):
        msg = QMessageBox()
        msg.setGeometry(300, 300, 250, 150)
        msg.setWindowTitle("EXIT")
        msg.setText("This is the main text!")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("LogOut !")

        msg.setDetailedText("details")
        msg.buttonClicked.connect(self.closeEvent)
    def closeEvent(self, event):
        print(event.text())
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.submit | 
            QMessageBox.cancel)

        if reply == QMessageBox.Retry:
            event.accept()
        else:
            event.ignore()

#-----------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DAQ_APP = QtWidgets.QMainWindow()
    ui = Ui_DAQ_APP()
    ui.setupUi(DAQ_APP)
    DAQ_APP.show()
    sys.exit(app.exec_())

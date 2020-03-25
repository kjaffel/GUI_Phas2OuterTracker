# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assembly/guide_assembly.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Assembly(object):
    def setupUi(self, Assembly):
        Assembly.setObjectName("Assembly")
        Assembly.resize(1562, 714)
        self.centralwidget = QtWidgets.QWidget(Assembly)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1060, 80, 461, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_3)
        self.commandLinkButton.setGeometry(QtCore.QRect(150, 270, 141, 41))
        self.commandLinkButton.setStyleSheet("font: 11pt \"Ubuntu\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Icons/technical-support-customer-service-computer-icons-call-center.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(1370, 610, 171, 31))
        self.commandLinkButton_2.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(570, 80, 471, 321))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(138, 290, 211, 25))
        self.pushButton.setStyleSheet("background-color: rgb(127, 127, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 430, 1531, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 1511, 151))
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(80, 80, 471, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 91, 31))
        self.label.setObjectName("label")
        Assembly.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Assembly)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1562, 22))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuDescription = QtWidgets.QMenu(self.menubar)
        self.menuDescription.setObjectName("menuDescription")
        self.menuAssembly_Status = QtWidgets.QMenu(self.menubar)
        self.menuAssembly_Status.setObjectName("menuAssembly_Status")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAssembly_and_Tests = QtWidgets.QMenu(self.menubar)
        self.menuAssembly_and_Tests.setObjectName("menuAssembly_and_Tests")
        Assembly.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(Assembly)
        self.toolBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar.setObjectName("toolBar")
        Assembly.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUser = QtWidgets.QAction(Assembly)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Icons/login-background-images-clipart-1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUser.setIcon(icon1)
        self.actionUser.setObjectName("actionUser")
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuDescription.menuAction())
        self.menubar.addAction(self.menuAssembly_Status.menuAction())
        self.menubar.addAction(self.menuAssembly_and_Tests.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionUser)

        self.retranslateUi(Assembly)
        QtCore.QMetaObject.connectSlotsByName(Assembly)

    def retranslateUi(self, Assembly):
        _translate = QtCore.QCoreApplication.translate
        Assembly.setWindowTitle(_translate("Assembly", "Assembly"))
        self.commandLinkButton.setText(_translate("Assembly", "Call an Expert "))
        self.commandLinkButton_2.setText(_translate("Assembly", "Save and Continue"))
        self.pushButton.setText(_translate("Assembly", "Watch "))
        self.textEdit.setHtml(_translate("Assembly", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-style:italic; color:#888a85;\">     </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-style:italic; color:#888a85;\">     Keep Track of your work ...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-style:italic; color:#888a85;\">    Write your Elog down before your proceed please !</span></p></body></html>"))
        self.label.setText(_translate("Assembly", " UserGuide : "))
        self.menuConnection.setTitle(_translate("Assembly", "Connection"))
        self.menuDescription.setTitle(_translate("Assembly", "Description"))
        self.menuAssembly_Status.setTitle(_translate("Assembly", "Assembly Status"))
        self.menuSettings.setTitle(_translate("Assembly", "Settings"))
        self.menuHelp.setTitle(_translate("Assembly", "Help"))
        self.menuAssembly_and_Tests.setTitle(_translate("Assembly", "Assembly and Tests"))
        self.toolBar.setWindowTitle(_translate("Assembly", "toolBar"))
        self.actionUser.setText(_translate("Assembly", "User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Assembly = QtWidgets.QMainWindow()
    ui = Ui_Assembly()
    ui.setupUi(Assembly)
    Assembly.show()
    sys.exit(app.exec_())

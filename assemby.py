# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Assembly/assembly.ui'
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 50, 20, 641))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 50, 251, 601))
        self.treeWidget.setObjectName("treeWidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 40, 1561, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(260, 50, 491, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(10, 11, 471, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(260, 330, 491, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 471, 301))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 10, 431, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 10, 41, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(770, 10, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(1410, 610, 131, 31))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
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
        Assembly.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(Assembly)
        self.toolBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar.setObjectName("toolBar")
        Assembly.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionUser = QtWidgets.QAction(Assembly)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Icons/login-background-images-clipart-1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUser.setIcon(icon)
        self.actionUser.setObjectName("actionUser")
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuDescription.menuAction())
        self.menubar.addAction(self.menuAssembly_Status.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionUser)

        self.retranslateUi(Assembly)
        QtCore.QMetaObject.connectSlotsByName(Assembly)

    def retranslateUi(self, Assembly):
        _translate = QtCore.QCoreApplication.translate
        Assembly.setWindowTitle(_translate("Assembly", "Assembly"))
        self.treeWidget.headerItem().setText(0, _translate("Assembly", "    Modules"))
        self.textBrowser.setHtml(_translate("Assembly", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Assembly", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\';\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Assembly", "Exit"))
        self.pushButton_2.setText(_translate("Assembly", "Search"))
        self.label.setText(_translate("Assembly", "  In:"))
        self.comboBox.setItemText(0, _translate("Assembly", "    PS"))
        self.comboBox.setItemText(1, _translate("Assembly", "    2S"))
        self.commandLinkButton_2.setText(_translate("Assembly", "Start Assembly"))
        self.menuConnection.setTitle(_translate("Assembly", "Connection"))
        self.menuDescription.setTitle(_translate("Assembly", "Description"))
        self.menuAssembly_Status.setTitle(_translate("Assembly", "Assembly Status"))
        self.menuSettings.setTitle(_translate("Assembly", "Settings"))
        self.menuHelp.setTitle(_translate("Assembly", "Help"))
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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setupfc7.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setupFC7(object):
    def setupUi(self, setupFC7):
        setupFC7.setObjectName("setupFC7")
        setupFC7.resize(1451, 716)
        self.centralwidget = QtWidgets.QWidget(setupFC7)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(190, 160, 321, 89))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.verticalLayout.addWidget(self.frame)
        setupFC7.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(setupFC7)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1451, 22))
        self.menubar.setObjectName("menubar")
        self.menuConffiguration = QtWidgets.QMenu(self.menubar)
        self.menuConffiguration.setObjectName("menuConffiguration")
        self.menuDebug = QtWidgets.QMenu(self.menubar)
        self.menuDebug.setObjectName("menuDebug")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        setupFC7.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(setupFC7)
        self.toolBar.setObjectName("toolBar")
        setupFC7.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionFC7 = QtWidgets.QAction(setupFC7)
        self.actionFC7.setObjectName("actionFC7")
        self.actionHybride = QtWidgets.QAction(setupFC7)
        self.actionHybride.setObjectName("actionHybride")
        self.actionlog = QtWidgets.QAction(setupFC7)
        self.actionlog.setObjectName("actionlog")
        self.actionSetting_up_the_FC7 = QtWidgets.QAction(setupFC7)
        self.actionSetting_up_the_FC7.setObjectName("actionSetting_up_the_FC7")
        self.actionFC7_2 = QtWidgets.QAction(setupFC7)
        self.actionFC7_2.setCheckable(False)
        self.actionFC7_2.setEnabled(True)
        self.actionFC7_2.setObjectName("actionFC7_2")
        self.menuConffiguration.addAction(self.actionFC7)
        self.menuDebug.addAction(self.actionlog)
        self.menuHelp_2.addAction(self.actionSetting_up_the_FC7)
        self.menubar.addAction(self.menuConffiguration.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())
        self.toolBar.addAction(self.actionFC7_2)
        self.label.setBuddy(self.label)

        self.retranslateUi(setupFC7)
        QtCore.QMetaObject.connectSlotsByName(setupFC7)

    def retranslateUi(self, setupFC7):
        _translate = QtCore.QCoreApplication.translate
        setupFC7.setWindowTitle(_translate("setupFC7", "setupFC7"))
        self.label.setText(_translate("setupFC7", "Host address:"))
        self.label_2.setText(_translate("setupFC7", "FC7 address:"))
        self.menuConffiguration.setTitle(_translate("setupFC7", "Configuration"))
        self.menuDebug.setTitle(_translate("setupFC7", "Debug"))
        self.menuHelp_2.setTitle(_translate("setupFC7", "Help"))
        self.toolBar.setWindowTitle(_translate("setupFC7", "toolBar"))
        self.actionFC7.setText(_translate("setupFC7", "FC7"))
        self.actionFC7.setStatusTip(_translate("setupFC7", "Steps to set up the FC7"))
        self.actionHybride.setText(_translate("setupFC7", "Hybride"))
        self.actionlog.setText(_translate("setupFC7", "log"))
        self.actionSetting_up_the_FC7.setText(_translate("setupFC7", "Setting up the FC7..."))
        self.actionFC7_2.setText(_translate("setupFC7", "FC7"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setupFC7 = QtWidgets.QMainWindow()
    ui = Ui_setupFC7()
    ui.setupUi(setupFC7)
    setupFC7.show()
    sys.exit(app.exec_())

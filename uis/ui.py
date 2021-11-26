from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import sys
import time


import main


def run_ui():
    app = QtWidgets.QApplication(sys.argv)
    WebActuary = QtWidgets.QDialog()
    ui = Ui_WebActuary()
    ui.setupUi(WebActuary)
    WebActuary.show()
    sys.exit(app.exec_())

"""def exit_ui(app):
    sys.exit(app.exec_())"""


class Ui_WebActuary(object):

    def __init__(self):
        self.url = ""

    def setupUi(self, WebActuary):
        WebActuary.setObjectName("WebActuary")
        WebActuary.resize(627, 333)
        WebActuary.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        WebActuary.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(WebActuary)
        self.label.setGeometry(QtCore.QRect(130, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(WebActuary)
        self.lineEdit.setGeometry(QtCore.QRect(240, 100, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(WebActuary)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(WebActuary)
        self.pushButton.setGeometry(QtCore.QRect(250, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(WebActuary)
        self.line.setGeometry(QtCore.QRect(30, 230, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line.setObjectName("line")

        self.progressBar = QtWidgets.QProgressBar(WebActuary)
        self.progressBar.setGeometry(QtCore.QRect(200, 270, 271, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(WebActuary)
        self.label_3.setGeometry(QtCore.QRect(260, 270, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(WebActuary)
        QtCore.QMetaObject.connectSlotsByName(WebActuary)

        self.pushButton.clicked.connect(self.on_click)

    def retranslateUi(self, WebActuary):
        _translate = QtCore.QCoreApplication.translate
        WebActuary.setWindowTitle(_translate("WebActuary", "Auditor"))
        self.label.setText(_translate("WebActuary", "Enter URL : "))
        self.label_2.setText(_translate("WebActuary", "WebActuary"))
        self.pushButton.setText(_translate("WebActuary", "AUDIT"))
        self.label_3.setText(_translate("WebActuary", "Auditing URL..."))

    def on_click(self):
        """for i in range(101):
            # slowing down the loop
            time.sleep(0.05)

            # setting value to progress bar
            self.progressBar.setValue(i)"""
        self.url = self.lineEdit.text()
        main.run_program(self.url)
        #exit_ui(self)





run_ui()

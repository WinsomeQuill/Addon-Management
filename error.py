# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorUI(object):
    def setupUi(self, ErrorUI):
        ErrorUI.setObjectName("ErrorUI")
        ErrorUI.resize(401, 300)
        self.ErrorLabel = QtWidgets.QLabel(ErrorUI)
        self.ErrorLabel.setEnabled(True)
        self.ErrorLabel.setGeometry(QtCore.QRect(10, 10, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ErrorLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"")
        self.ErrorLabel.setTextFormat(QtCore.Qt.AutoText)
        self.ErrorLabel.setScaledContents(False)
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.ErrorOkButton = QtWidgets.QPushButton(ErrorUI)
        self.ErrorOkButton.setGeometry(QtCore.QRect(10, 271, 381, 20))
        self.ErrorOkButton.setStyleSheet("QPushButton {    \n"
"    background-color: #9c83aa;\n"
"    border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"    color: #fff;\n"
"    width: 25px; /* Ширина кнопки */\n"
"    height: 25px; /* Высота */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:Hover {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"    color: #fff\n"
"}\n"
"\n"
"QPushButton:Pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"    box-shadow: 0 0 10px 20px #000;\n"
"}\n"
"\n"
"  \n"
"")
        self.ErrorOkButton.setAutoDefault(True)
        self.ErrorOkButton.setFlat(False)
        self.ErrorOkButton.setObjectName("ErrorOkButton")
        self.ErrorConsole = QtWidgets.QTextBrowser(ErrorUI)
        self.ErrorConsole.setGeometry(QtCore.QRect(10, 40, 381, 221))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorConsole.setFont(font)
        self.ErrorConsole.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ErrorConsole.setObjectName("ErrorConsole")

        self.retranslateUi(ErrorUI)
        QtCore.QMetaObject.connectSlotsByName(ErrorUI)

    def retranslateUi(self, ErrorUI):
        _translate = QtCore.QCoreApplication.translate
        ErrorUI.setWindowTitle(_translate("ErrorUI", "Error"))
        self.ErrorLabel.setText(_translate("ErrorUI", "ERROR"))
        self.ErrorOkButton.setText(_translate("ErrorUI", "OK"))
        self.ErrorConsole.setHtml(_translate("ErrorUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">ERROR MESSAGE!</span></p></body></html>"))

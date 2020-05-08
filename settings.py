# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\artem\Desktop\gmad\other\3.8\settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(403, 344)
        Settings_Dialog.setSizeGripEnabled(False)
        Settings_Dialog.setModal(False)
        self.SelectGmodSave = QtWidgets.QToolButton(Settings_Dialog)
        self.SelectGmodSave.setGeometry(QtCore.QRect(320, 60, 71, 31))
        self.SelectGmodSave.setStyleSheet("")
        self.SelectGmodSave.setObjectName("SelectGmodSave")
        self.SelectGmodLabel = QtWidgets.QLabel(Settings_Dialog)
        self.SelectGmodLabel.setEnabled(True)
        self.SelectGmodLabel.setGeometry(QtCore.QRect(10, 10, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.SelectGmodLabel.setFont(font)
        self.SelectGmodLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SelectGmodLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"")
        self.SelectGmodLabel.setTextFormat(QtCore.Qt.AutoText)
        self.SelectGmodLabel.setScaledContents(False)
        self.SelectGmodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectGmodLabel.setObjectName("SelectGmodLabel")
        self.SelectGmodText = QtWidgets.QTextBrowser(Settings_Dialog)
        self.SelectGmodText.setGeometry(QtCore.QRect(10, 60, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SelectGmodText.setFont(font)
        self.SelectGmodText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.SelectGmodText.setObjectName("SelectGmodText")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Settings_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 270, 381, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SelectGmodReset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SelectGmodReset.setStyleSheet("QPushButton {    \n"
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
        self.SelectGmodReset.setAutoDefault(True)
        self.SelectGmodReset.setFlat(False)
        self.SelectGmodReset.setObjectName("SelectGmodReset")
        self.horizontalLayout.addWidget(self.SelectGmodReset)
        self.SelectGmodApply = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SelectGmodApply.setStyleSheet("QPushButton {    \n"
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
        self.SelectGmodApply.setAutoDefault(True)
        self.SelectGmodApply.setFlat(False)
        self.SelectGmodApply.setObjectName("SelectGmodApply")
        self.horizontalLayout.addWidget(self.SelectGmodApply)
        self.SelectGmodLabel_2 = QtWidgets.QLabel(Settings_Dialog)
        self.SelectGmodLabel_2.setEnabled(True)
        self.SelectGmodLabel_2.setGeometry(QtCore.QRect(10, 36, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.SelectGmodLabel_2.setFont(font)
        self.SelectGmodLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SelectGmodLabel_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"")
        self.SelectGmodLabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.SelectGmodLabel_2.setScaledContents(False)
        self.SelectGmodLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectGmodLabel_2.setObjectName("SelectGmodLabel_2")

        self.retranslateUi(Settings_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

    def retranslateUi(self, Settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Settings_Dialog.setWindowTitle(_translate("Settings_Dialog", "Settings"))
        self.SelectGmodSave.setText(_translate("Settings_Dialog", "Folder"))
        self.SelectGmodLabel.setText(_translate("Settings_Dialog", "Indicate the path to the Garry\'s Mod"))
        self.SelectGmodText.setHtml(_translate("Settings_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Game not found!</span></p></body></html>"))
        self.SelectGmodReset.setText(_translate("Settings_Dialog", "Reset"))
        self.SelectGmodApply.setText(_translate("Settings_Dialog", "Apply"))
        self.SelectGmodLabel_2.setText(_translate("Settings_Dialog", "Example: C:/Steam/steamapps/common/GarrysMod"))

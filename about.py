# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\artem\Desktop\gmad\other\3.8\about.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About_Dialog(object):
    def setupUi(self, About_Dialog):
        About_Dialog.setObjectName("About_Dialog")
        About_Dialog.setEnabled(True)
        About_Dialog.resize(402, 300)
        self.DrElroyLabel = QtWidgets.QLabel(About_Dialog)
        self.DrElroyLabel.setGeometry(QtCore.QRect(10, 40, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.DrElroyLabel.setFont(font)
        self.DrElroyLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"color: #fff;\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 5px;")
        self.DrElroyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DrElroyLabel.setObjectName("DrElroyLabel")
        self.SpecialThanksLabel = QtWidgets.QLabel(About_Dialog)
        self.SpecialThanksLabel.setGeometry(QtCore.QRect(10, 11, 381, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.SpecialThanksLabel.setFont(font)
        self.SpecialThanksLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;")
        self.SpecialThanksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SpecialThanksLabel.setObjectName("SpecialThanksLabel")
        self.SpecialThanksOk = QtWidgets.QPushButton(About_Dialog)
        self.SpecialThanksOk.setGeometry(QtCore.QRect(10, 260, 381, 21))
        self.SpecialThanksOk.setStyleSheet("QPushButton {    \n"
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
        self.SpecialThanksOk.setAutoDefault(True)
        self.SpecialThanksOk.setFlat(False)
        self.SpecialThanksOk.setObjectName("SpecialThanksOk")

        self.retranslateUi(About_Dialog)
        QtCore.QMetaObject.connectSlotsByName(About_Dialog)

    def retranslateUi(self, About_Dialog):
        _translate = QtCore.QCoreApplication.translate
        About_Dialog.setWindowTitle(_translate("About_Dialog", "About"))
        self.DrElroyLabel.setText(_translate("About_Dialog", "Dr.Elroy"))
        self.SpecialThanksLabel.setText(_translate("About_Dialog", "Special Thanks"))
        self.SpecialThanksOk.setText(_translate("About_Dialog", "OK"))


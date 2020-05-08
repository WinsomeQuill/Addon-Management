# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Dialog(object):
    def setupUi(self, Main_Dialog):
        Main_Dialog.setObjectName("Main_Dialog")
        Main_Dialog.resize(639, 714)
        self.gridLayoutWidget = QtWidgets.QWidget(Main_Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 640, 621, 64))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttom_create = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buttom_create.setStyleSheet("QPushButton {    \n"
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
        self.buttom_create.setAutoDefault(True)
        self.buttom_create.setFlat(False)
        self.buttom_create.setObjectName("buttom_create")
        self.gridLayout.addWidget(self.buttom_create, 0, 0, 1, 1)
        self.button_public_steam = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_public_steam.setStyleSheet("QPushButton {    \n"
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
        self.button_public_steam.setObjectName("button_public_steam")
        self.gridLayout.addWidget(self.button_public_steam, 0, 2, 1, 1)
        self.button_extract = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_extract.setStyleSheet("QPushButton {    \n"
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
        self.button_extract.setObjectName("button_extract")
        self.gridLayout.addWidget(self.button_extract, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Main_Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 550, 621, 91))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.check_fun_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_fun_box.setObjectName("check_fun_box")
        self.gridLayout_2.addWidget(self.check_fun_box, 0, 0, 1, 1)
        self.check_roleplay_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_roleplay_box.setObjectName("check_roleplay_box")
        self.gridLayout_2.addWidget(self.check_roleplay_box, 1, 0, 1, 1)
        self.check_scenic_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_scenic_box.setObjectName("check_scenic_box")
        self.gridLayout_2.addWidget(self.check_scenic_box, 2, 0, 1, 1)
        self.check_realism_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_realism_box.setObjectName("check_realism_box")
        self.gridLayout_2.addWidget(self.check_realism_box, 1, 1, 1, 1)
        self.check_comic_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_comic_box.setObjectName("check_comic_box")
        self.gridLayout_2.addWidget(self.check_comic_box, 1, 2, 1, 1)
        self.check_movie_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_movie_box.setObjectName("check_movie_box")
        self.gridLayout_2.addWidget(self.check_movie_box, 0, 1, 1, 1)
        self.check_cartoon_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_cartoon_box.setObjectName("check_cartoon_box")
        self.gridLayout_2.addWidget(self.check_cartoon_box, 2, 1, 1, 1)
        self.check_water_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_water_box.setObjectName("check_water_box")
        self.gridLayout_2.addWidget(self.check_water_box, 0, 2, 1, 1)
        self.check_build_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.check_build_box.setAcceptDrops(False)
        self.check_build_box.setAutoFillBackground(False)
        self.check_build_box.setCheckable(True)
        self.check_build_box.setChecked(False)
        self.check_build_box.setAutoRepeat(False)
        self.check_build_box.setAutoExclusive(False)
        self.check_build_box.setTristate(False)
        self.check_build_box.setObjectName("check_build_box")
        self.gridLayout_2.addWidget(self.check_build_box, 2, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Main_Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 420, 621, 91))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tags_map = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_map.setObjectName("tags_map")
        self.gridLayout_3.addWidget(self.tags_map, 2, 0, 1, 1)
        self.tags_gamemode = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_gamemode.setObjectName("tags_gamemode")
        self.gridLayout_3.addWidget(self.tags_gamemode, 1, 0, 1, 1)
        self.tags_npc = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_npc.setObjectName("tags_npc")
        self.gridLayout_3.addWidget(self.tags_npc, 2, 1, 1, 1)
        self.tags_server_content = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_server_content.setObjectName("tags_server_content")
        self.gridLayout_3.addWidget(self.tags_server_content, 0, 0, 1, 1)
        self.tags_effects = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_effects.setObjectName("tags_effects")
        self.gridLayout_3.addWidget(self.tags_effects, 1, 2, 1, 1)
        self.tags_vehicle = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_vehicle.setObjectName("tags_vehicle")
        self.gridLayout_3.addWidget(self.tags_vehicle, 1, 1, 1, 1)
        self.tags_weapon = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_weapon.setObjectName("tags_weapon")
        self.gridLayout_3.addWidget(self.tags_weapon, 0, 1, 1, 1)
        self.tags_tool = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_tool.setObjectName("tags_tool")
        self.gridLayout_3.addWidget(self.tags_tool, 0, 2, 1, 1)
        self.tags_model = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.tags_model.setObjectName("tags_model")
        self.gridLayout_3.addWidget(self.tags_model, 2, 2, 1, 1)
        self.text_path_select = QtWidgets.QTextBrowser(Main_Dialog)
        self.text_path_select.setGeometry(QtCore.QRect(10, 280, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_path_select.setFont(font)
        self.text_path_select.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.text_path_select.setObjectName("text_path_select")
        self.button_selector_file = QtWidgets.QToolButton(Main_Dialog)
        self.button_selector_file.setGeometry(QtCore.QRect(530, 280, 101, 31))
        self.button_selector_file.setStyleSheet("")
        self.button_selector_file.setObjectName("button_selector_file")
        self.winsomequill = QtWidgets.QLabel(Main_Dialog)
        self.winsomequill.setGeometry(QtCore.QRect(10, 10, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.winsomequill.setFont(font)
        self.winsomequill.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"color: #fff;\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 5px;")
        self.winsomequill.setAlignment(QtCore.Qt.AlignCenter)
        self.winsomequill.setObjectName("winsomequill")
        self.AuthorInVkButton = QtWidgets.QPushButton(Main_Dialog)
        self.AuthorInVkButton.setGeometry(QtCore.QRect(10, 41, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.AuthorInVkButton.setFont(font)
        self.AuthorInVkButton.setStyleSheet("QPushButton {    \n"
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
"")
        self.AuthorInVkButton.setObjectName("AuthorInVkButton")
        self.VersionLabel = QtWidgets.QLabel(Main_Dialog)
        self.VersionLabel.setGeometry(QtCore.QRect(470, 11, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.VersionLabel.setFont(font)
        self.VersionLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"color: #fff;\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 5px;")
        self.VersionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VersionLabel.setObjectName("VersionLabel")
        self.text_path_select_save = QtWidgets.QTextBrowser(Main_Dialog)
        self.text_path_select_save.setGeometry(QtCore.QRect(10, 210, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_path_select_save.setFont(font)
        self.text_path_select_save.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.text_path_select_save.setObjectName("text_path_select_save")
        self.button_selector_folder_save = QtWidgets.QToolButton(Main_Dialog)
        self.button_selector_folder_save.setGeometry(QtCore.QRect(530, 210, 101, 31))
        self.button_selector_folder_save.setStyleSheet("")
        self.button_selector_folder_save.setObjectName("button_selector_folder_save")
        self.SetNameFileString = QtWidgets.QTextEdit(Main_Dialog)
        self.SetNameFileString.setGeometry(QtCore.QRect(10, 350, 621, 31))
        self.SetNameFileString.setObjectName("SetNameFileString")
        self.SetNameFileLabel = QtWidgets.QLabel(Main_Dialog)
        self.SetNameFileLabel.setGeometry(QtCore.QRect(10, 320, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.SetNameFileLabel.setFont(font)
        self.SetNameFileLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;")
        self.SetNameFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SetNameFileLabel.setObjectName("SetNameFileLabel")
        self.label_text_type_3 = QtWidgets.QLabel(Main_Dialog)
        self.label_text_type_3.setEnabled(True)
        self.label_text_type_3.setGeometry(QtCore.QRect(10, 390, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_text_type_3.setFont(font)
        self.label_text_type_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_type_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;")
        self.label_text_type_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_text_type_3.setScaledContents(False)
        self.label_text_type_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_type_3.setObjectName("label_text_type_3")
        self.label_text_type_2 = QtWidgets.QLabel(Main_Dialog)
        self.label_text_type_2.setEnabled(True)
        self.label_text_type_2.setGeometry(QtCore.QRect(10, 520, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_text_type_2.setFont(font)
        self.label_text_type_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_type_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;")
        self.label_text_type_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_text_type_2.setScaledContents(False)
        self.label_text_type_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_type_2.setObjectName("label_text_type_2")
        self.progressBar = QtWidgets.QProgressBar(Main_Dialog)
        self.progressBar.setGeometry(QtCore.QRect(470, 60, 161, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.AuthorInSteamButton = QtWidgets.QPushButton(Main_Dialog)
        self.AuthorInSteamButton.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.AuthorInSteamButton.setFont(font)
        self.AuthorInSteamButton.setStyleSheet("QPushButton {    \n"
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
"")
        self.AuthorInSteamButton.setObjectName("AuthorInSteamButton")
        self.SettingsButton = QtWidgets.QToolButton(Main_Dialog)
        self.SettingsButton.setGeometry(QtCore.QRect(360, 10, 91, 21))
        self.SettingsButton.setStyleSheet("")
        self.SettingsButton.setObjectName("SettingsButton")
        self.AboutButton = QtWidgets.QToolButton(Main_Dialog)
        self.AboutButton.setGeometry(QtCore.QRect(260, 10, 91, 21))
        self.AboutButton.setStyleSheet("")
        self.AboutButton.setObjectName("AboutButton")
        self.label_text_type_6 = QtWidgets.QLabel(Main_Dialog)
        self.label_text_type_6.setEnabled(True)
        self.label_text_type_6.setGeometry(QtCore.QRect(10, 180, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_text_type_6.setFont(font)
        self.label_text_type_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_type_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"")
        self.label_text_type_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_text_type_6.setScaledContents(False)
        self.label_text_type_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_type_6.setObjectName("label_text_type_6")
        self.label_text_type_5 = QtWidgets.QLabel(Main_Dialog)
        self.label_text_type_5.setEnabled(True)
        self.label_text_type_5.setGeometry(QtCore.QRect(10, 250, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_text_type_5.setFont(font)
        self.label_text_type_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_text_type_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;")
        self.label_text_type_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_text_type_5.setScaledContents(False)
        self.label_text_type_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_type_5.setObjectName("label_text_type_5")
        self.SelectAddonCreateLabel = QtWidgets.QLabel(Main_Dialog)
        self.SelectAddonCreateLabel.setEnabled(True)
        self.SelectAddonCreateLabel.setGeometry(QtCore.QRect(10, 110, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.SelectAddonCreateLabel.setFont(font)
        self.SelectAddonCreateLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SelectAddonCreateLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 122, 54, 255), stop:1 rgba(252, 66, 100, 255));\n"
"border: 0px solid #7a7b7e; /* Параметры рамки */\n"
"width: 25px; /* Ширина кнопки */\n"
"height: 25px; /* Высота */\n"
"border-radius: 10px;\n"
"color: #fff;\n"
"")
        self.SelectAddonCreateLabel.setTextFormat(QtCore.Qt.AutoText)
        self.SelectAddonCreateLabel.setScaledContents(False)
        self.SelectAddonCreateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectAddonCreateLabel.setObjectName("SelectAddonCreateLabel")
        self.SelectAddonCreateButton = QtWidgets.QToolButton(Main_Dialog)
        self.SelectAddonCreateButton.setGeometry(QtCore.QRect(530, 140, 101, 31))
        self.SelectAddonCreateButton.setStyleSheet("")
        self.SelectAddonCreateButton.setObjectName("SelectAddonCreateButton")
        self.SelectAddonCreatePath = QtWidgets.QTextBrowser(Main_Dialog)
        self.SelectAddonCreatePath.setGeometry(QtCore.QRect(10, 140, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SelectAddonCreatePath.setFont(font)
        self.SelectAddonCreatePath.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.SelectAddonCreatePath.setObjectName("SelectAddonCreatePath")
        self.SetIconWorkShopSteam = QtWidgets.QToolButton(Main_Dialog)
        self.SetIconWorkShopSteam.setGeometry(QtCore.QRect(260, 40, 191, 21))
        self.SetIconWorkShopSteam.setStyleSheet("")
        self.SetIconWorkShopSteam.setObjectName("SetIconWorkShopSteam")

        self.retranslateUi(Main_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Main_Dialog)

    def retranslateUi(self, Main_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Main_Dialog.setWindowTitle(_translate("Main_Dialog", "Addon Management [Garry\'s Mod]"))
        self.buttom_create.setText(_translate("Main_Dialog", "Create GMA"))
        self.button_public_steam.setText(_translate("Main_Dialog", "Public (Steam)"))
        self.button_extract.setText(_translate("Main_Dialog", "Extract GMA"))
        self.check_fun_box.setText(_translate("Main_Dialog", "Fun"))
        self.check_roleplay_box.setText(_translate("Main_Dialog", "RolePlay"))
        self.check_scenic_box.setText(_translate("Main_Dialog", "Scenic"))
        self.check_realism_box.setText(_translate("Main_Dialog", "Realism"))
        self.check_comic_box.setText(_translate("Main_Dialog", "Comic"))
        self.check_movie_box.setText(_translate("Main_Dialog", "Movie"))
        self.check_cartoon_box.setText(_translate("Main_Dialog", "Cartoon"))
        self.check_water_box.setText(_translate("Main_Dialog", "Water"))
        self.check_build_box.setText(_translate("Main_Dialog", "Build"))
        self.tags_map.setText(_translate("Main_Dialog", "Map"))
        self.tags_gamemode.setText(_translate("Main_Dialog", "Gamemode"))
        self.tags_npc.setText(_translate("Main_Dialog", "NPC"))
        self.tags_server_content.setText(_translate("Main_Dialog", "ServerContent"))
        self.tags_effects.setText(_translate("Main_Dialog", "Effects"))
        self.tags_vehicle.setText(_translate("Main_Dialog", "Vehicle"))
        self.tags_weapon.setText(_translate("Main_Dialog", "Weapon"))
        self.tags_tool.setText(_translate("Main_Dialog", "Tool"))
        self.tags_model.setText(_translate("Main_Dialog", "Model"))
        self.text_path_select.setHtml(_translate("Main_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Path not found!</span></p></body></html>"))
        self.button_selector_file.setText(_translate("Main_Dialog", "File"))
        self.winsomequill.setText(_translate("Main_Dialog", "Author: WinsomeQuill"))
        self.AuthorInVkButton.setText(_translate("Main_Dialog", "Автор в ВК *клик*"))
        self.VersionLabel.setText(_translate("Main_Dialog", "Version: Beta1.0"))
        self.text_path_select_save.setHtml(_translate("Main_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Path not found!</span></p></body></html>"))
        self.button_selector_folder_save.setText(_translate("Main_Dialog", "Folder"))
        self.SetNameFileString.setHtml(_translate("Main_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Unnamed</span></p></body></html>"))
        self.SetNameFileLabel.setText(_translate("Main_Dialog", "Change  Name"))
        self.label_text_type_3.setText(_translate("Main_Dialog", "Type:"))
        self.label_text_type_2.setText(_translate("Main_Dialog", "Tags:"))
        self.AuthorInSteamButton.setText(_translate("Main_Dialog", "Author in Steam *click*"))
        self.SettingsButton.setText(_translate("Main_Dialog", "Settings"))
        self.AboutButton.setText(_translate("Main_Dialog", "About"))
        self.label_text_type_6.setText(_translate("Main_Dialog", "Select folder for save"))
        self.label_text_type_5.setText(_translate("Main_Dialog", "Select .gma file for Extract mode or Public mode"))
        self.SelectAddonCreateLabel.setText(_translate("Main_Dialog", "Select Addon for Create mode"))
        self.SelectAddonCreateButton.setText(_translate("Main_Dialog", "Folder"))
        self.SelectAddonCreatePath.setHtml(_translate("Main_Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Path not found!</span></p></body></html>"))
        self.SetIconWorkShopSteam.setText(_translate("Main_Dialog", "Set Icon (WorkShop Steam)"))

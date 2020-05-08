from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import configparser
import os
import time
import psutil
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import webbrowser

from ui import Ui_Main_Dialog
from about import Ui_About_Dialog
from settings import Ui_Settings_Dialog
from error import Ui_ErrorUI



#Create Main
ui = Ui_Main_Dialog()
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()#(None, QtCore.Qt.WindowTitleHint)
ui = Ui_Main_Dialog()
ui.setupUi(Dialog)
Dialog.setFixedSize(639, 714)
Dialog.show()
#sys.exit(app.exec_())
#Create About
aboutDialog = QtWidgets.QDialog()
aboutui = Ui_About_Dialog()
aboutui.setupUi(aboutDialog)
aboutDialog.setFixedSize(402, 300)
#Create Settings
settingsDialog = QtWidgets.QDialog()
settingsui = Ui_Settings_Dialog()
settingsui.setupUi(settingsDialog)
settingsDialog.setFixedSize(403, 344)
#Create Error
ErrorDialog = QtWidgets.QWidget()
Errorui = Ui_ErrorUI()
Errorui.setupUi(ErrorDialog)
ErrorDialog.setFixedSize(401, 300)

#Logic
#######################
type_buttons = [ui.tags_map, ui.tags_gamemode, ui.tags_vehicle, ui.tags_server_content, ui.tags_weapon, ui.tags_npc, ui.tags_effects, ui.tags_tool, ui.tags_model]
tags_buttons = [ui.check_fun_box, ui.check_roleplay_box, ui.check_scenic_box, ui.check_realism_box, ui.check_comic_box, ui.check_movie_box, ui.check_cartoon_box, ui.check_water_box, ui.check_build_box]
type_text = ['map', 'gamemode', 'vehicle', 'ServerContent', 'weapon', 'npc', 'effects', 'tool', 'model']
tags_text = ['fun', 'roleplay', 'scenic', 'realism', 'comic', 'movie', 'cartoon', 'water', 'build']

tags1 = 0
tags2 = 0
type1 = 0
foldersave = 'Unnamed'
name_addon = 0
FileAddon = 0
GAME_FOLDER = 0
IconAddon = 0

config = configparser.ConfigParser()
#######################
def SelectorFile():
	root = tk.Tk()
	root.withdraw()
	global FileAddon
	file_name = askopenfilename(initialdir="C:/", filetypes =(("Addon File", "*.gma"),("All Files","*.*")), title = "Choose a file.")
	FileAddon = file_name
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
	    #with open(name,'r') as UseFile:
	        ui.text_path_select.setText( FileAddon )
	except:
	    ui.text_path_select.setText( "None" )
	    FileAddon = 0

def SelectGmodSaveFolder():
	root = tk.Tk()
	root.withdraw()
	global GAME_FOLDER
	GAME_FOLDER = askdirectory(initialdir="C:/",title = "Choose a folder.")
	settingsui.SelectGmodText.setText( GAME_FOLDER )

def SelectorFolder():
	root = tk.Tk()
	root.withdraw()
	name_select = askdirectory(initialdir="C:/",title = "Choose a folder.")
	ui.text_path_select.setText( name_select )

def SelectorFolderSave():
	root = tk.Tk()
	root.withdraw()
	name_save = askdirectory(initialdir="C:/",title = "Choose a folder.")
	global foldersave
	foldersave = name_save
	ui.text_path_select_save.setText( name_save )

def SelectAddonCreate():
	root = tk.Tk()
	root.withdraw()
	name_save_path = askdirectory(initialdir="C:/",title = "Choose a folder.")
	global AddonCreatePath
	AddonCreatePath = name_save_path
	ui.SelectAddonCreatePath.setText( AddonCreatePath )

def AuthorVK():
	webbrowser.open_new_tab('https://vk.com/winsomequill')

def AuthorSteam():
	webbrowser.open_new_tab('https://steamcommunity.com/id/doshikplayer/')

def ErrorDialogUi():
	ErrorDialog.show()

def ErrorClose():
	ErrorDialog.close()

def AboutDialog():
	aboutDialog.show()

def SettingsDialog():
	settingsDialog.show()

def OnClickedApplySettigns():
	CheckConfige()
	try:
		config.set("Settings", "game_folder", "{0}" .format(GAME_FOLDER))

		with open("settings.ini", "w") as config_file:
			config.write(config_file)

		settingsDialog.close()
	except NameError:
		print('Error #10 (Game folder not found)')


def CreateConfig():
	config.add_section("Settings")
	config.set("Settings", "game_folder", "{0}" .format(GAME_FOLDER))
	config.set("Settings", "version", "1.0")

	with open("settings.ini", "w") as config_file:
		config.write(config_file)

def ReadConfige():
	try:
		config.read('settings.ini')
		GAME_FOLDER = config.get("Settings", "game_folder")
		print('Game added!')
	except KeyError:
		print('Error #6 (Game not found)')
	except configparser.NoSectionError:
		print('Error #7 (Section not found)')

def CheckConfige():
	if not os.path.exists('settings.ini'):
		CreateConfig()
	else:
		ReadConfige()

def StartProgrammCheckConfige():
	if not os.path.exists('settings.ini'):
		print('Error #8 (settings.ini file not found)')
	else:
		config.read('settings.ini')
		global GAME_FOLDER
		GAME_FOLDER = config.get("Settings", "game_folder")
		settingsui.SelectGmodText.setText( GAME_FOLDER )

def OnClickedResetSettigns():
	if not os.path.exists('settings.ini'):
		print('Error #8 (settings.ini file not found)')
	else:
		config.set("Settings", "game_folder", "None")
		with open("settings.ini", "w") as config_file:
			config.write(config_file)
		settingsui.SelectGmodText.setText( 'Path not found!' )

def AboutDialogClose():
	aboutDialog.close()

StartProgrammCheckConfige()

#[----------------------------TYPE----------------------------] #Здесь должен быть только один флаг
def TypeSelect():
	enable_type = []
	for i in range(9):
		if type_buttons[i].isChecked() == True:
			enable_type.append(type_buttons[i])
			global type1	
			type1 = type_text[i]

	total = len(enable_type)
	return total

def TypeOn():
	for i in range(9):
		type_buttons[i].setDisabled(False)
		global type1
		type1 = 0

def TypeOff():
	for i in range(9):
		if type_buttons[i].isChecked() == False:
			type_buttons[i].setDisabled(True)

def Type():
	if TypeSelect() == 1:
		TypeOff()
	else:
		TypeOn()

#[-----------------------------------------------------------]

#[----------------------------TAG----------------------------] #Здесь должено быть только два флага
def TagSelect():
	enable_tag = []
	for i in range(9):
		if tags_buttons[i].isChecked() == True:
			enable_tag.append(tags_buttons[i])
			global tags1, tags2
			tags1 = tags_text[i]
			if len(enable_tag) == 1:
				tags2 = tags_text[i]

	
	total_tag = len(enable_tag)
	return total_tag


def TagOn():
	for i in range(9):
		tags_buttons[i].setDisabled(False)
		global tags1, tags2
		tags1 = 0
		tags2 = 0

def TagOff():
	for i in range(9):
		if tags_buttons[i].isChecked() == False:
			tags_buttons[i].setDisabled(True)

def Tag():
	if TagSelect() == 2:
		TagOff()
	else:
		TagOn()
#[------------------------------------------------------------]
'''def CheckSteam():
	for proc in psutil.process_iter():
		steam = proc.name()
		if steam == "steam.exe":
			return True'''


def TryCreate():
	try:
		#os.mkdir("{0}/{1}" .format(AddonCreatePath, name_addon))
		f = open("{0}/addon.json" .format(AddonCreatePath),"w+")
		f.write("{\n")
		f.write("	\"title\"		:	\"{0}\",\n" .format(name_addon))
		f.write("	\"type\"		:	\"{0}\",\n" .format(type1))
		f.write("	\"tags\"		:	[ \"{0}\", \"{1}\" ],\n" .format(tags1, tags2))
		ui.progressBar.setValue( 45 )
		f.write("	\"ignore\"	:\n")
		f.write("	[\n")
		f.write("		\"*.psd\",\n")
		f.write("		\"*.vcproj\",\n")
		f.write("		\"*.svn*\"\n")
		f.write("	]\n")
		f.write("}\n")
		ui.progressBar.setValue( 55 )
		f.close()
		return True
	except FileNotFoundError:
		#print('Error #5 (Path not found)')
		Errorui.ErrorConsole.setText( 'Error #5 (Path not found)' )
		ErrorDialogUi()
		return False
	except FileExistsError:
		#print('Error #11 (Addon already created)')
		Errorui.ErrorConsole.setText( 'Error #11 (Addon already created)' )
		ErrorDialogUi()
		return False
	except NameError:
		Errorui.ErrorConsole.setText( 'Error #21 (Bad Name Addon or Folder)' )
		ErrorDialogUi()
		return False

def GoCreate():
	if type1 == 0:
		#print('Error #1 (Type not selected)')
		Errorui.ErrorConsole.setText( 'Error #1 (Type not selected)' )
		ErrorDialogUi()
	else:
		if tags1 == 0 or tags2 == 0:
			#print('Error #2 (Tags not selected)')
			Errorui.ErrorConsole.setText( 'Error #2 (Tags not selected)' )
			ErrorDialogUi()
		else:
			global name_addon
			name_addon = ui.SetNameFileString.toPlainText()
			if name_addon == 0 or name_addon == '' or name_addon == ' ':
				#print('Error #3 (Bad name Addon)')
				Errorui.ErrorConsole.setText( 'Error #3 (Bad name Addon)' )
				ErrorDialogUi()
			else:
				if GAME_FOLDER == 'None' or GAME_FOLDER == 0 or GAME_FOLDER == '' or GAME_FOLDER == ' ':
					#print('Error #9 (Bad Game Folder)')
					Errorui.ErrorConsole.setText( 'Error #9 (Bad Game Folder)' )
					ErrorDialogUi()
				else:
					ui.progressBar.setValue( 75 )
					if TryCreate() == True:
						os.system(r'{0}/bin/gmad.exe create -folder {1} -out {2}/{3}' .format(GAME_FOLDER, AddonCreatePath, foldersave, name_addon))
						ui.progressBar.setValue( 100 )
						time.sleep(0.3)
						ui.progressBar.setValue( 0 )
					else:
						print('Error #4 (Function \'TryCreate()\' not return True)')
						ui.progressBar.setValue( 75 )

def GoExtract():
	name_addon = ui.SetNameFileString.toPlainText()
	ui.progressBar.setValue( 25 )
	if name_addon == 0 or name_addon == '' or name_addon == ' ':
		#print('Error #12 (Bad name Addon)')
		Errorui.ErrorConsole.setText( 'Error #12 (Bad name Addon)' )
		ErrorDialogUi()
	else:
		if foldersave == 0 or foldersave == '' or foldersave == ' ':
			#print('Error #13 (Folder Save not found)')
			Errorui.ErrorConsole.setText( 'Error #13 (Folder Save not found)' )
			ErrorDialogUi()
		else:
			ui.progressBar.setValue( 55 )
			if GAME_FOLDER == 'None' or GAME_FOLDER == 0 or GAME_FOLDER == '' or GAME_FOLDER == ' ':
				#print('Error #14 (Bad Game Folder)')
			 	Errorui.ErrorConsole.setText( 'Error #14 (Bad Game Folder)' )
			 	ErrorDialogUi()
			else:
				ui.progressBar.setValue( 75 )
				if FileAddon == '' or FileAddon == 0 or FileAddon == ' ':
					#print('Error #15 (Addon not found (.gma))')
					Errorui.ErrorConsole.setText( 'Error #15 (Addon not found (.gma))' )
					ErrorDialogUi()
				else:
					ui.progressBar.setValue( 85 )
					os.system(r'{0}/bin/gmad.exe extract -file {1} -out {2}/{3}' .format(GAME_FOLDER, FileAddon, foldersave, name_addon))
					ui.progressBar.setValue( 100 )
					time.sleep(0.3)
					ui.progressBar.setValue( 0 )
def SetIconAddon():
	root = tk.Tk()
	root.withdraw()
	global IconAddon
	icon_name = askopenfilename(initialdir="C:/", filetypes =(("Default", "*.jpg"),("JPG","*.jpg*")), title = "Choose a file.")
	IconAddon = icon_name
	from PIL import Image
	im = Image.open(IconAddon)
	w, h = im.size

	if w > 512 or h > 512:
		Errorui.ErrorConsole.setText( 'Error #19 (Max Size Icon 512x512)' )
		ErrorDialogUi()
		IconAddon = 0

def GoPublicSteam():
	name_addon = ui.SetNameFileString.toPlainText()
	ui.progressBar.setValue( 25 )
	if name_addon == 0 or name_addon == '' or name_addon == ' ':
		#print('Error #16 (Bad name Addon)')
		Errorui.ErrorConsole.setText( 'Error #16 (Bad name Addon)' )
		ErrorDialogUi()
		ui.progressBar.setValue( 0 )
	else:
		ui.progressBar.setValue( 55 )
		if GAME_FOLDER == 'None' or GAME_FOLDER == 0 or GAME_FOLDER == '' or GAME_FOLDER == ' ':
			#print('Error #17 (Bad Game Folder)')
			Errorui.ErrorConsole.setText( 'Error #17 (Bad Game Folder)' )
			ErrorDialogUi()
			ui.progressBar.setValue( 0 )
		else:
			ui.progressBar.setValue( 75 )
			if FileAddon == '' or FileAddon == 0 or FileAddon == ' ':
				#print('Error #18 (Addon not found (.gma))')
				Errorui.ErrorConsole.setText( 'Error #18 (Addon not found (.gma))' )
				ErrorDialogUi()
				ui.progressBar.setValue( 0 )
			else:
				if IconAddon == 0 or IconAddon == '' or IconAddon == ' ':
					#print('Error #20 (Bad Icon)')
					Errorui.ErrorConsole.setText( 'Error #20 (Bad Icon)' )
					ErrorDialogUi()
					ui.progressBar.setValue( 0 )
				else:
					ui.progressBar.setValue( 85 )
					os.system(r'{0}/bin/gmpublish.exe create -addon {1} -icon {2}' .format(GAME_FOLDER, FileAddon, IconAddon))
					ui.progressBar.setValue( 100 )
					time.sleep(0.3)
					ui.progressBar.setValue( 0 )

						#Errorui.ErrorConsole.setText( 'Error #22 (You are not in Steam)' )
						#ErrorDialogUi()
						#ui.progressBar.setValue( 0 )

#[--------------TYPE--------------]
ui.tags_map.clicked.connect( Type )
ui.tags_gamemode.clicked.connect( Type )
ui.tags_vehicle.clicked.connect( Type )
ui.tags_weapon.clicked.connect( Type )
ui.tags_npc.clicked.connect( Type )
ui.tags_effects.clicked.connect( Type )
ui.tags_tool.clicked.connect( Type )
ui.tags_model.clicked.connect( Type )
ui.tags_server_content.clicked.connect( Type )
#[-------------------------------]

#[--------------TAG--------------]
ui.check_fun_box.clicked.connect( Tag )
ui.check_roleplay_box.clicked.connect( Tag )
ui.check_scenic_box.clicked.connect( Tag )
ui.check_realism_box.clicked.connect( Tag )
ui.check_comic_box.clicked.connect( Tag )
ui.check_movie_box.clicked.connect( Tag )
ui.check_cartoon_box.clicked.connect( Tag )
ui.check_water_box.clicked.connect( Tag )
ui.check_build_box.clicked.connect( Tag )
#[-------------------------------]

#[--------------Create Addon--------------]
ui.buttom_create.clicked.connect( GoCreate )
ui.button_extract.clicked.connect( GoExtract )
#[----------------------------------------]

#[--------------Settings GUI--------------]
settingsui.SelectGmodSave.clicked.connect( SelectGmodSaveFolder ) #Выбор игры
settingsui.SelectGmodApply.clicked.connect( OnClickedApplySettigns ) #Применить
settingsui.SelectGmodReset.clicked.connect( OnClickedResetSettigns ) #Очистить путь
ui.SettingsButton.clicked.connect( SettingsDialog ) #Открыть окно настроек
#[----------------------------------------]

#[----------------About GUI---------------]
ui.AboutButton.clicked.connect( AboutDialog ) #Открыть меню информации
aboutui.SpecialThanksOk.clicked.connect( AboutDialogClose ) #Закрыть меню информации
#[----------------------------------------]

#[----------------Create Addon(*.gma)---------------]
ui.SelectAddonCreateButton.clicked.connect( SelectAddonCreate )
#[--------------------------------------------------]

#[----------------Public Addon.gma in Steam WorkShop----------------]
ui.button_public_steam.clicked.connect( GoPublicSteam )
#[------------------------------------------------------------------]

Errorui.ErrorOkButton.clicked.connect( ErrorClose )

ui.button_selector_file.clicked.connect( SelectorFile ) #Выбор файла
ui.SetIconWorkShopSteam.clicked.connect( SetIconAddon ) #Выбор папки для загрузки
ui.button_selector_folder_save.clicked.connect( SelectorFolderSave ) #Выбор папки для сохранения
ui.AuthorInVkButton.clicked.connect( AuthorVK ) #VK ссылка
ui.AuthorInSteamButton.clicked.connect( AuthorSteam ) #Steam ссылка

#Run Main
sys.exit(app.exec_())  
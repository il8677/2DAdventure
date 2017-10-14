# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
import pickle
from os.path import expanduser

from game import time, day, areaMap, playerX, playerY, inventory, cheats


def formTempBackup():
	return (time, day, areaMap, playerX, playerY, inventory, cheats)


def loadTempBackup(backup):
	global time
	global day
	global areaMap
	global playerX
	global playerY
	global inventory
	global cheats
	time = backup[0]
	day = backup[1]
	areaMap = backup[2]
	inventory = backup[3]
	cheats = backup[4]


def loadGame():
	global time
	global day
	global areaMap
	global playerX
	global playerY
	global inventory
	global cheats
	loadFailBackup = formTempBackup()
	try:
		loadedData = pickle.load(open(expanduser("~/adventure.adgf"), "rb+"))
		time = loadedData[0]
		day = loadedData[1]
		areaMap = loadedData[2]
		playerX = loadedData[3]
		playerY = loadedData[4]
		inventory = loadedData[5]
		cheats = loadedData[6]

		assert isinstance(time, int)
		assert isinstance(day, int)
		assert isinstance(areaMap, list)
		assert isinstance(inventory, list)
		assert isinstance(cheats, bool)

	except (pickle.UnpicklingError, EOFError):  # anything could fail!
		print("Load failed - save file may be corrupt. Sorry about that.")
		print("Reloading pre-load state from backup...")
		loadTempBackup(loadFailBackup)

	except (AssertionError, IndexError):
		print("Load failed - save file may be from an older version of this game. Sorry about that.")
		print("Reloading pre-load state from backup...")
		loadTempBackup(loadFailBackup)

	except FileNotFoundError:
		print("Load failed - save file does not exist. Sorry about that.")
		print("Reloading pre-load state from backup...")
		loadTempBackup(loadFailBackup)
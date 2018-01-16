import os.path
import pickle
from time import sleep


def loadGame(filepath, currentState):
	failBackup = currentState
	try:
		loadedData = pickle.load(open(os.path.abspath(os.path.expanduser(filepath)), "rb+"))
		assert isinstance(loadedData[0], int)  # time
		assert isinstance(loadedData[1], int)  # day
		assert isinstance(loadedData[2], list)  # areaMap
		assert isinstance(loadedData[3], int)  # playerX
		assert isinstance(loadedData[4], int)  # playerY
		assert isinstance(loadedData[5], list)  # inventory
		assert isinstance(loadedData[6], bool)  # cheats
		return loadedData

	except (pickle.UnpicklingError, EOFError):
		print("Load failed - save file may be corrupt. Sorry about that.")
		print("Reloading pre-load state from backup...")
		sleep(3)
		return failBackup

	except (AssertionError, IndexError) as e:
		print("Load failed - save file may be from an older version of this game. Sorry about that.")
		print("Reloading pre-load state from backup...")
		print(e)
		sleep(3)
		return failBackup

	except FileNotFoundError:
		print("Load failed - save file does not exist. Sorry about that.")
		print("Reloading pre-load state from backup...")
		sleep(3)
		return failBackup

	except IsADirectoryError:
		print("Load failed - you seem to be pointing to a directory OR have not supplied a path.")
		print("Reloading pre-load state from backup...")
		sleep(3)
		return failBackup


def save(filepath, gameSave):
	assert isinstance(gameSave, tuple)
	try:
		pickle.dump(gameSave, open(os.path.abspath(os.path.expanduser(filepath)), "wb+"))
		print("Saved gamefile at " + filepath)

	except (pickle.PickleError, pickle.PicklingError, EOFError):
		print("Save failed - we're having problems encoding the gamefile.")
		sleep(3)

	except IsADirectoryError:
		print("Save failed - you seem to be pointing to a directory.")
		print("Please supply a notional file.")
# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
# Licensed under the MIT License.
import pickle
from os.path import expanduser
from sys import exit
from time import sleep as wait
import biomes

###########
#  SETUP  #
###########
print()
print()
xMax = 7  # maximum X length
yMax = 7  # maximum Y length
playerX = int(round(xMax / 2))  # as close as possible to the middle of the areaMap
playerY = int(round(yMax / 2))  # as close as possible to the middle of the areaMap
areaMap = biomes.generateMap(xMax, yMax)
time = -1  # hours passed so goes up to 24. incremented at start of gameplay, starts at 0.
day = 0  # we will increment this at the very start of gameplay so's not to confuse the user
inventory = []
maxInventory = 50  # how many items can the player have?
cheats = False
health = 1.0
hunger = 1.0
weaponDamage = None


def die(cause, killer="animal"):
	if cause == "suicide":
		print("You jump off a cliff.")

	elif cause == "animal":
		print("Your attempt to find food was rudely interupted by a gang of " + killer + "s.")
		print("Aware of their cousin's distress, they attack you. They come in such numbers that you are helpless.")

	print("Goodbye, cruel world.")
	e = exit()


def generateAreaMap():
	ret = ""
	for yLine in areaMap:
		mapLine = []
		for item in yLine:
			mapLine.append(str(item))
		ret += (str(mapLine).replace("[", "").replace("]", "").replace("'", "").replace(", ", "") + "\n")

	return ret


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




while True:
	###################
	#  GETTING READY  #
	###################
	time += 1
	if time > 23:
		time = 0  # hours reset every day
		day += 1

	print("MAP:")
	print(generateAreaMap())

	print()

	# print player position
	print("Your position: X" + str(playerX) + " Y" + str(playerY))

	# print time/day
	print("The time:      " + str(time) + "hrs")
	print("Day:           " + str(day))



	##############
	#  GAMEPLAY  #
	##############
	action = input(">")
	action = action.lower().strip(" ")  # lower and strip of whitespace

	if action == "exit":
		die("suicide")
		wait(3)
	elif action == "help":
		print("exit")
		print("	kill yourself and exit the game")
		print("wait")
		print("	do nothing and stay where you are")
		print("go north  /  gn")
		print("	head north (positive Y)")
		print("go south  /  gs")
		print("	head south (negative Y)")
		print("go east  /  ge")
		print("	head east (positive X)")
		print("go west  /  gw")
		print("	head west (negative X)")
		wait(4)
	elif action == "wait":
		pass
	elif action == "go north" or action == "gn":
		if playerY >= yMax:
			print("Can't go north from here!")
			wait(2)
		else:
			playerY += 1
	elif action == "go south" or action == "gs":
		if playerY <= 1:
			print("Can't go south from here!")
			wait(2)
		else:
			playerY -= 1
	elif action == "go east" or action == "ge":
		if playerX >= xMax:
			print("Can't go east from here!")
			wait(2)
		else:
			playerX += 1
	elif action == "go west" or action == "gw":
		if playerX <= 1:
			print("Can't go south from here!")
			wait(2)
		else:
			playerX -= 1
	elif action == "save":
		pickle.dump((time, day, areaMap, playerX, playerY, inventory, cheats), open(expanduser("~/adventure.adgf"), "wb+"))
		print("Saved gamefile at ~/adventure.adgf - DO NOT RENAME! You can only save one gamefile!")
		wait(2)
	elif action == "load":
		loadGame()
		wait(2)
	else:
		print("Didn't understand. Try 'help' for a list of commands.")
		wait(2)

	print()
	print()

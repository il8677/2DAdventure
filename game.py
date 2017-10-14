# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
import pickle
from os.path import expanduser
from random import randrange as randInt
from sys import exit
from time import sleep as wait

import animals
###########
#  SETUP  #
###########
from saveload import loadGame

print()
print()
xMax = 7  # maximum X length
yMax = 7  # maximum Y length
playerX = int(round(xMax / 2))  # as close as possible to the middle of the areaMap
playerY = int(round(yMax / 2))  # as close as possible to the middle of the areaMap
areaMap = []
time = -1  # hours passed so goes up to 24. incremented at start of gameplay, starts at 0.
day = 0  # we will increment this at the very start of gameplay so's not to confuse the user
inventory = []
maxInventory = 50  # how many items can the player have?
cheats = False
health = 1.0
hunger = 1.0
weaponDamage = None

xSampleData = []  # this will be cloned on the X axis for every Y-line
for i in range(0, xMax):
	xSampleData.append("_")  # fill it with None for now, we will generate a areaMap later
for i in range(0, yMax):
	areaMap.append(xSampleData)  # fill up the areaMap with Nones


class baseBiome:
	def __init__(self):
		self.biomeName = "Void"  # will be replaced in all subclasses
		self.mineralName = "VoidMineral"  # will be replaced
		self.mineralQuant = 0  # will be replaced
		self.animals = []  # will be replaced

	def __str__(self):
		return self.biomeType


class woodsBiome(baseBiome):
	def __init__(self):
		self.mineralName = "Trees"
		self.mineralQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(5)


def die(cause, killer="animal"):
	if cause == "suicide":
		print("You jump off a cliff.")

	elif cause == "animal":
		print("Your attempt to find food was rudely interupted by a gang of " + killer + "s.")
		print("Aware of their cousin's distress, they attack you. They come in such numbers that you are helpless.")

	print("Goodbye, cruel world.")
	e = exit()


while True:
	###################
	#  GETTING READY  #
	###################
	time += 1
	if time > 23:
		time = 0  # hours reset every day
		day += 1

	# print areaMap
	print("MAP:")
	for yLine in areaMap:
		print(str(yLine).replace("[", "").replace("]", "").replace("'", "").replace(", ", ""))

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
	elif action == "help":
		print("exit")
		print("	kill yourself and exit the game")
		print("wait")
		print("	do nothing and stay where you are")
		print("go north")
		print("	head north (positive Y)")
		print("go south")
		print("	head south (negative Y)")
		print("go east")
		print("	head east (positive X)")
		print("go west")
		print("	head west (negative X)")
	elif action == "wait":
		pass
	elif action == "go north":
		if playerY >= yMax:
			print("Can't go north from here!")
		else:
			playerY += 1
	elif action == "go south":
		if playerY <= 1:
			print("Can't go south from here!")
		else:
			playerY -= 1
	elif action == "go east":
		if playerX >= xMax:
			print("Can't go east from here!")
		else:
			playerX += 1
	elif action == "go west":
		if playerX <= 1:
			print("Can't go south from here!")
		else:
			playerX -= 1
	elif action == "save":
		pickle.dump((time, day, areaMap, playerX, playerY, inventory, cheats), open(expanduser("~/adventure.adgf"), "wb+"))
		print("Saved gamefile at ~/adventure.adgf - DO NOT RENAME! You can only save one gamefile!")
	elif action == "load":
		loadGame()
	else:
		print("Didn't understand. Try 'help' for a list of commands.")

	wait(2)
	print()
	print()

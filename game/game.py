# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
# Licensed under the MIT License.

titletext = """
 ____     ___       _       _                 _                  
|___ \   /   \     /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
  __) | / /\ /    //_\\\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \\
 / __/ / /_//    /  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/
|_____/___,'     \_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
                                                                  
"""
from sys import exit
from time import sleep as wait
import animals
from backstory import showBackstory
import biomes
import saveload
import player as mPlayer

###########
#  SETUP  #
###########
print()
print()
xMax = 30  # maximum X length
yMax = int(round(xMax / 2))  # maximum Y length
playerX = int(round(xMax / 2))  # as close as possible to the middle of the areaMap
playerY = int(round(yMax / 2))  # as close as possible to the middle of the areaMap
areaMap = biomes.generateMap(xMax, yMax)
time = -1  # hours passed so goes up to 24. incremented at start of gameplay, starts at 0.
day = 0  # we will increment this at the very start of gameplay so's not to confuse the user
weapon = None
food = 0
inventory = []
player = mPlayer.Player("")


def generateAreaMap():
	ret = ""
	yCounter = yMax
	for yLine in areaMap:
		mapLine = []
		xCounter = 0
		for item in yLine:
			if xCounter == playerX and yCounter == playerY:
				mapLine.append("●")
			else:
				mapLine.append(item.__str__())
			xCounter += 1
		ret += (str(mapLine).replace("[", "").replace("]", "").replace("'", "").replace(", ", "") + "\n")
		yCounter -= 1

	return ret


try:
	###############
	#  BACKSTORY  #
	###############
	showBackstory()

	print(titletext)

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

		areaMap[yMax - playerY][playerX].printInfo()
		print()
		print("What do you want to do? Type it in and press <Enter>.")
		print("For help, use 'help'<Enter>.")



		##############
		#  GAMEPLAY  #
		##############
		action = input(">")
		action = action.lower().strip(" ")  # lower and strip of whitespace

		if action == "exit" or action == "q":
			die("suicide")
			wait(3)
		elif action == "help":
			print("exit  /  q")
			print("	kill yourself and exit the game")
			print("wait  /  x")
			print("	do nothing and stay where you are")
			print("go north  /  n")
			print("	head north (positive Y)")
			print("go south  /  s")
			print("	head south (negative Y)")
			print("go east  /  e")
			print("	head east (positive X)")
			print("go west  /  w")
			print("	head west (negative X)")
			print("save  /  v")
			print("	save your game")
			print("load  /  l")
			print("	load from your save")
			print("hunt  /  h")
			print("	hunt and kill areaAnimals around you for food")
			print("	becomes easier with a better sword")
			wait(6)
		elif action == "wait" or action == "x":
			pass
		elif action == "go north" or action == "n":
			if playerY >= yMax:
				print("Can't go north from here!")
				wait(2)
			else:
				playerY += 1
		elif action == "go south" or action == "s":
			if playerY <= 1:
				print("Can't go south from here!")
				wait(2)
			else:
				playerY -= 1
		elif action == "go east" or action == "e":
			if playerX >= xMax:
				print("Can't go east from here!")
				wait(2)
			else:
				playerX += 1
		elif action == "go west" or action == "w":
			if playerX <= 0:
				print("Can't go west from here!")
				wait(2)
			else:
				playerX -= 1
		elif action.startswith("save") or action.startswith("v "):
			action = action.strip("save ")
			action = action.strip("v ")
			action = action.strip(" ")
			saveload.save(action, (time, day, areaMap, playerX, playerY, inventory, cheats))
			wait(2)
		elif action.startswith("load") or action.startswith("l"):
			action = action.strip("load ")
			action = action.strip("l ")
			action = action.strip(" ")
			load = saveload.loadGame(action, (time, day, areaMap, playerX, playerY, inventory, cheats))
			time = load[0]
			day = load[1]
			areaMap = load[2]
			playerX = load[3]
			playerY = load[4]
			inventory = load[5]
			cheats = load[6]
			wait(2)
		elif action == "hunt" or action == "h":
			areaAnimals = areaMap[playerY][playerX].animals
			if len(areaAnimals) == 0:
				print("There are no animals to hunt here!")
				wait(2)
			elif len(areaAnimals) == 1:
				print("There is one animal here. It is a " + areaAnimals[0].animalName + ".")
				validInput = False
				while validInput is not True:
					hunt = input("Do you want to hunt it? (y/N) >").lower()
					if hunt == "n":
						hunt = False
						validInput = True
					elif hunt == "y":
						hunt = True
						validInput = True
					else:
						print("Please use valid input (y or n).")
				if hunt:
					attackResult = areaAnimals[0].attack()
				else:
					print("You decide not to hunt it. Huh. Chicken.")
					wait(2)
			else:
				print("Which animal do you want to hunt?")
				counter = 0
				for animal in areaAnimals:
					if animal.__str__().startswith("a") or animal.__str__().startswith("e") \
							or animal.__str__().startswith("i") or animal.__str__().startswith("o") \
							or animal.__str__().startswith("u"):
						print(str(counter + 1) + ". An " + str(animal))
					else:
						print(str(counter + 1) + ". A " + str(animal))
					counter += 1
				validInput = False
				while not validInput:
					try:
						prompt = int(input("Choose an animal: "))
						if prompt < 1 or prompt > counter: raise ValueError
						validInput = True
					except ValueError:
						print("Please use a number representing an animal shown above.")
				attackResult = areaAnimals[prompt - 1].attack()
		else:
			print("Didn't understand. Try 'help' for a list of commands.")
			wait(2)

		print()
		print()

except (KeyboardInterrupt, EOFError):
	print()
	die("suicide")

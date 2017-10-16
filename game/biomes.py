# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
from random import randrange as randInt
import animals


class baseBiome:
	def __init__(self):
		self.biomeName = "Void"  # will be replaced in all subclasses
		self.resourceName = "VoidMineral"  # will be replaced
		self.resourceQuant = 0  # will be replaced
		self.mapIcon = "_"
		self.animals = []  # will be replaced

	def __str__(self):
		return self.mapIcon

	def printInfo(self):
		print("You are in a " + self.biomeName + ".")
		print("There are " + str(self.resourceQuant) + " " + self.resourceName + " here.")
		print("A few metres in front of you, you see a group of animals:")
		for animal in animals:
			if animal.__str__().startswith("a") or animal.__str__().startswith("e") \
				or animal.__str__().startswith("i") or animal.__str__().startswith("o") \
				or animal.__str__().startswith("u"):
				print("- An " + animal)
			else:
				print("- A " + animal)


class woodsBiome(baseBiome):
	def __init__(self):
		self.biomeName = "Woods"
		self.mapIcon = "^"
		self.resourceName = "trees"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(5)


class desertBiome(baseBiome):
	def __init__(self):
		self.biomeName = "Desert"
		self.mapIcon = "~"
		self.resourceName = "square metres of sand"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(2)


class fieldBiome(baseBiome):
	def __init__(self):
		self.biomeName = "Field"
		self.mapIcon = "-"
		self.resourceName = "flowers"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(7)

		if self == fieldBiome:
			print("hi")



def generateMap(xMax, yMax):
	areaMap = []

	# first, fill the map with Voids
	xSampleData = []  # this will be cloned on the X axis for every Y-line
	for i in range(0, xMax):
		biomeInstance = baseBiome()
		xSampleData.append(biomeInstance)  # fill it with Void for now, we will generate a areaMap later
	for i in range(0, yMax):
		areaMap.append(xSampleData)  # fill up the areaMap with Void

	# now we generate some biomes
	yCounter = yMax
	for yi in areaMap:
		xCounter = 0
		for xi in yi:
			pass

	return areaMap
# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
from random import randrange as randInt
import animals
import numpy as np


class baseBiome:
	def __init__(self):
		self.biomeName = "Void"  # will be replaced in all subclasses
		self.resourceName = "VoidMineral"  # will be replaced
		self.resourceQuant = 0  # will be replaced
		self.mapIcon = "_"
		self.animals = animals.generateAnimals(5)

	def __str__(self):
		return "_"

	def printInfo(self):
		print("You are in a " + self.biomeName + ".")
		print("There are " + str(self.resourceQuant) + " " + self.resourceName + " here.")
		if len(self.animals) != 1:
			print("A few metres in front of you, you see a group of " + str(len(self.animals)) + " animals.")
		else:
			print("A few metres in front of you, you see a " + self.animals[0].animalName + ".")


class woodsBiome(baseBiome):
	def __init__(self):
		self.biomeName = "Woods"
		self.mapIcon = "^"
		self.resourceName = "trees"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(5)

	def __str__(self):
		return "^"


class desertBiome(baseBiome):
	def __init__(self):
		self.biomeName = "Desert"
		self.mapIcon = "~"
		self.resourceName = "square metres of sand"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(randInt(0, 2))

	def __str__(self):
		return "~"


class fieldBiome(baseBiome):
	def __init__(self):
		self.biomeName = "Field"
		self.mapIcon = "-"
		self.resourceName = "flowers"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(7)

		def __str__(self):
			return "-"



def generateMap(xMax, yMax):
	areaMap = []
	# first, fill the map with Voids
	xSampleData = []  # this will be cloned on the X axis for every Y-line
	for i in range(0, xMax):
		biomeInstance = baseBiome()
		xSampleData.append(biomeInstance)  # fill it with Void for now, we will generate a areaMap later
	for i in range(0, yMax):
		areaMap.append(list(xSampleData))  # fill up the areaMap with Void
	# now we generate some biomes
	yCounter = yMax
	for yi in areaMap:
		xCounter = 0
		for xi in yi:
			# here be hardcoding - MUST be updated after adding biomes!
			biomeList = [woodsBiome(), desertBiome(), fieldBiome()]
			biomeProbabilities = np.array([0.1, 0.1, 0.1])
			# O.O this code is BAD!!!
			# initiate biggest bodge i have ever written
			if isinstance(areaMap[yCounter-1][xCounter-1], woodsBiome):
				biomeProbabilities[0] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], woodsBiome):
				biomeProbabilities[0] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], woodsBiome):
				biomeProbabilities[0] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], woodsBiome):
				biomeProbabilities[0] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], desertBiome):
				biomeProbabilities[1] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], desertBiome):
				biomeProbabilities[1] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], desertBiome):
				biomeProbabilities[1] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], desertBiome):
				biomeProbabilities[1] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], fieldBiome):
				biomeProbabilities[2] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], fieldBiome):
				biomeProbabilities[2] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], fieldBiome):
				biomeProbabilities[2] += 0.2
			if isinstance(areaMap[yCounter-1][xCounter-1], fieldBiome):
				biomeProbabilities[2] += 0.2
			biomeProbabilities = biomeProbabilities / biomeProbabilities.sum()
			choice = np.random.choice(biomeList, 1, p=biomeProbabilities)[0]
			areaMap[yCounter - 1][xCounter - 1] = choice
			xCounter += 1
		yCounter -= 1
	return areaMap
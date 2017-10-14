# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
from random import randrange as randInt
import animals


class baseBiome:
	def __init__(self):
		self.biomeName = "Void"  # will be replaced in all subclasses
		self.resourceName = "VoidMineral"  # will be replaced
		self.resourceQuant = 0  # will be replaced
		self.animals = []  # will be replaced

	def __str__(self):
		return self.biomeName

	def printInfo(self):
		print("You are in a " + self.biomeName + ".")
		print("There are " + str(self.resourceQuant) + " " + self.resourceName + "s here.")
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
		self.resourceName = "Tree"
		self.resourceQuant = randInt(7, 18)

		# generate animals
		self.animals = animals.generateAnimals(5)
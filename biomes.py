# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
from random import randrange as randInt
import animals


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
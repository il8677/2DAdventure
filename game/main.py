#!/usr/local/bin/python3
# 2D Adventure

import random


class Biome:
	name = "Void"
	icon = "X"


class Field(Biome):
	name = "Field"
	icon = "-"


class Desert(Biome):
	name = "Desert"
	icon = "~"


class Forest(Biome):
	name = "Forest"
	icon = "^"


class River(Biome):
	name = "River"
	icon = "="


BIOMES = [Field, Desert, Forest, River]  # Used for terrain gen in Map. Avoids hardcoding biome types to add to our terrain.


class Map:
	width = 8  # How far along does the x axis go?
	height = 5  # How far down does the y axis go?

	def __init__(self):
		self.map = []  # 2D Array representing 2D map.

	def isIncomplete(self):
		for xslice in self.map:
			for biome in xslice:
				if (biome.name == "Void"):
					return True
		return False

	def expandGeneration(self):
		"""
		Finds seeds and replaces their surroundings with the same biome.
		This will be run multiple times to generate the map until no Voids are left.
		"""
		newseeds = self.seeds
		while (self.isIncomplete()):
			self.seeds = newseeds
			for seed in self.seeds:
				print(self.getReadout())
				surroundings = [
					(seed[2], (seed[1] - 1) % self.height),  # above
					(seed[2], (seed[1] + 1) % self.height),  # below
					((seed[2] - 1) % self.width, (seed[1]) % self.height),  # left
					((seed[2] + 1) % self.width, (seed[1]) % self.height)  # right
				]

				for location in surroundings:
					if self.map[location[1]][location[0]].name is not "Void":
						print(f"Replacing {seed[1]}, {seed[2]} with {seed[0].name}")
						self.map[location[1]][location[0]] = seed[0]()
						newseeds.append((seed[0], location[0], location[1]))

	def generateTerrain(self):
		self.map = [[Biome() for j in range(self.width)] for i in range(self.height)]
		self.seeds = [(biome, random.randint(0, self.width), random.randint(0, self.height)) for biome in BIOMES]
		for seed in self.seeds:
			self.map[seed[2] - 1][seed[1] - 1] = seed[0]()
		self.expandGeneration()

	def getReadout(self):
		readableMap = ""
		for xslice in self.map:
			for biome in xslice:
				readableMap += f"{biome.icon} "
			readableMap += "\n"
		return readableMap


testMap = Map()
testMap.generateTerrain()
print(testMap.getReadout())

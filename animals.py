# adventure by @DyingEcho
# Copyright ©2017 @DyingEcho. Some rights reserved.
# Licensed under the MIT License.
from random import uniform as randFloat
from game import die


class baseAnimal:
	def __init__(self, animalID):
		self.animalName = "Herobrine"  # will be replaced in all subclasses (probably with 99.9% chance to freak people out)
		self.health = 999999  # unkillable
		# TODO: Replace "Herobrine" with "The Lord Maxi"
		self.animalID = animalID  # to be replaced. will be based on biome, so there will be multiple ID 1s, 2s, etc.
		self.deadliness = 100  # percentage

	def __str__(self):
		return self.animalName

	def attack(self, weapon):
		if weapon is None:
			probability = randFloat(0, 100)
			if probability < self.deadliness:
				die("animal", self.animalName)


class pigAnimal(baseAnimal):
	def __init__(self, animalID):
		self.animalName = "Pig"
		self.health = 4
		self.animalID = animalID
		self.deadliness = 6  # percentage chance


class chickenAnimal(baseAnimal):
	def __init__(self, animalID):
		self.animalName = "Chicken"
		self.health = 2
		self.animalID = animalID
		self.deadliness = 3  # percentage chance


class cowAnimal(baseAnimal):
	def __init__(self, animalID):
		self.animalName = "Cow"
		self.health = 6
		self.animalID = animalID
		self.deadliness = 10  # percentage chance


class sheepAnimal(baseAnimal):
	def __init__(self, animalID):
		self.animalName = "Sheep"
		self.health = 6
		self.animalID = animalID
		self.deadliness = 8  # percentage chance


def generateAnimals(quantity):
	animals = []
	counter = 0
	for i in quantity:
		probability = randFloat(0, 100)
		if probability <= 40:
			animals.append(chickenAnimal(counter))
		elif 40 < probability < 70:
			animals.append(pigAnimal(counter))
		elif 70 < probability < 90:
			animals.append(cowAnimal(counter))
		elif 90 < probability < 99.9:
			animals.append()
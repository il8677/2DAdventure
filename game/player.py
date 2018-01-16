class Player:
	def __init__(self, name):
		self.name = name
		self.inventory = []
		self.inventoryMax = 10  # how much stuff can the player have?
		self.health = 0.75  # percentage fof 100. under 25 is critical.
		self.satiation = 0.75  # percentage of 100. player loses minimum 0.5 each turn, sometimes more.

	def die(cause, killer="animal", doExit=True):
		if cause == "suicide":
			print("You jump off a cliff.")

		elif cause == "animal":
			print("Your attempt to find food was rudely interupted by a gang of " + killer + "s.")
			print("Aware of their cousin's distress, they attack you. They come in such numbers that you are helpless.")

		print("Goodbye, cruel world.")
		e = exit() if doExit else False  # exit if doExit is true
		return e
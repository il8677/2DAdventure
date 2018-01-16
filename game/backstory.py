def showBackstory():
	from os import system as sysShell
	from time import sleep as wait

	validInput = False
	while validInput is not True:
		showBS = input("Play the backstory (recommended to new players)? (y/N) >").lower()
		if showBS == "n":
			showBS = False
			validInput = True
		elif showBS == "y":
			showBS = True
			validInput = True
		else:
			print("Please use valid input (y or n).")
	if showBS:
		sysShell("reset")
		print('BLACK ALERT. BLACK ALERT.')
		wait(2)
		print('"...reactor is overloaded!"')
		wait(2)
		print('"...quantum containment field has failed, and the..."')
		wait(2)
		print('BLACK ALERT. BLACK ALERT.')
		wait(2)
		print('"...20 seconds from total breach..."')
		wait(1)
		print('"...somebody, you have to..."')
		wait(1)
		print('"...can\'t hold it in..."')
		wait(0.5)
		print('"...supposed to lead us to utopia!"')
		wait(0.5)
		print('"...all doomed, we\'re all doomed, we\'re all doomed..."')
		wait(0.4)
		print('"...continuum destabilisation imminent..."')
		wait(0.3)
		print('"...all meant to be safe last June..."')
		wait(3)
		print('')
		print('')
		print('BLACK ALERT.')
		wait(0.75)
		print('BLACK ALERT.')
		wait(0.75)
		print('BLACK ALERT.')
		wait(7)

		sysShell("reset")
		print('Ugh.')
		wait(4)
		print('Your head hurts.')
		wait(2)
		print('You have no idea where you are.')
		wait(2)
		print('More importantly, you have no idea who you are.')
		wait(2)
		print('You know something happened, but you\'re not sure what.')
		wait(3)
		print('Judging by your headache - and lack of memory - it probably wasn\'t great.')
		wait(3)
		print('Apart from that, you are in fairly good shape. You are not hungry, and you are unhurt.')
		wait(3)
		print('You are wearing a t-shirt (is that what it\'s called?) that reads "NASA - Temporal Research Dept."')
		wait(4)
		print("Phew. At least you can still read. What that text means, however, is a mystery.")

		wait(7)
	sysShell("reset")
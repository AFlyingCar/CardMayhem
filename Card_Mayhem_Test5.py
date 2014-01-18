#################
#Tyler Robbins	#
#1/5/13		#
#CardMayhemTest5#
#################
#######################################
#CardMayhem Test for Wild Card System.#
#######################################

print 'Initializing Card Mayhem', '.', '.', '.'

import random
import time
import sys, pdb

cardValues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Cards = ['a', '2','3','4','5','6','7','8','9','10','j','q','k']
Suits = ['hearts', 'spades', 'diamonds', 'clubs']
Wild = ['X2Multiplier', 'MasterSpark', 'AceTo11', 'DeckSwap']
Deck = []
playerDeck = []
cpuDeck = []
playerDisplayed = []
cpuDisplayed = []
playerScore, cpuScore = 0, 0
playerNumTurn, cpuNumTurn = 5, 5
cpuTurn, playerTurn = True, True
playerChoice = ''
cpuChoice = 0
finish = False
restart, exit = True, True
flipcheck = 1

def shuffle(): #makes main deck
	foo = 0
	time.sleep(1);print 'Making Deck'
	newdeck = []

	while len(newdeck) < 56: #makes card deck
		if random.randint(1,2) == 1: #chooses
			tempDeck = [random.choice(Suits), random.choice(cardValues)]
		else:
			tempDeck = random.choice(Wild)
		
		if tempDeck not in newdeck: #puts card in newdeck
			newdeck.append(tempDeck)
	
	random.shuffle(newdeck) #Note: Look at C:/Users/Tyler/Dropbox/FamilyRobbins/Tyler/usbstuff/Python/yearone/
	
	return newdeck #Deck=shuffle()

def deck_maker(run, message): #makes player and cpu decks
	time.sleep(1)
	print message
	
	deckchoice = []
	tempHand = []

	while len(deckchoice) < run: #gets card from main Deck
		tempHand = random.choice(Deck)

		if tempHand in Deck: #removes card from Deck
			Deck.remove(tempHand)

		deckchoice.append(tempHand) #adds card to player/cpu hand

	return deckchoice #player/cpuDeck=deck_maker(5)

def flipper(deck, message): #flips card in player hand
	"""tempGrab=flipper(playerDeck), tempGrab=flipper(cpuDeck), tempGrab=flipper(Deck)
	playerDisplayed=tempGrab[0]
	playerDeck=tempGrab[1]"""
	flipcheck, flipcheck1 = 1, 0
	tempHand = []

	print message,
	time.sleep(0.33);print ".",
	time.sleep(0.33);print ".",
	time.sleep(0.34);print "."

	try:
		while flipcheck == 1:
			try:
				tempHand = random.choice(deck) #grab card from player/cpu hand
				flipcheck = 0

			except(TypeError):
				flipcheck1 += 1

				if flipcheck1 == 5:
					sys.exit(TypeError)

		if tempHand in deck:
			deck.remove(tempHand) #removes tempHand from player/cpu hand

	except(IndexError):
		pass

	if type(tempHand) == list:
		print "The card was a " + str(tempHand[1]) + " of " + str(tempHand[0]) + "!\n"

	else:
		print "The card was the " + tempHand + " wild card!"

		if tempHand == 'MasterSpark': #MasterSpark Wild Card
			if deck == playerDeck:
				playerScore -= 10
				print 'MasterSpark!'
				playerDisplayed.remove('MasterSpark')
			elif deck == cpuDeck:
				playerScore -= 10
				print 'MasterSpark!'
				cpuDisplayed.remove('MasterSpark')

	return [tempHand, deck] #returns two values. use arrays to get correct values with tempGrab[]

def AT11(deck):
	#AceTo11 Wild Card
	#changes all 1's to 11's in user's deck
	print 'Ace to 11'
	
	for item in deck:
		if item[1] == 1:
			loc = deck.index(item)
			item[1] = 11
			deck[loc] = list(item)

	return deck

def DeSw(deck):
	#DeckSwap Wild Card
	#allows the player to swap their deck with the cpu
	#CPU will not be able to use this card
	print 'DeckSwap'

	tempDeck = []

	while True:
		
		print "Type 'C' to swap your deck with the CPU Deck, and 'D' to pull new cards from the main Deck.\n"
		swap = raw_input("(Note: Choosing 'D' will erase your Deck and put it back in the deck) ")
		swap = swap.upper()

		if swap == 'C': #What to do if player chooses 'C'
			tempDeck = cpuDeck
			cpuDeck = playerDeck
			playerDeck = cpuDeck
			return False

		elif swap == 'D': #What to do if player chooses 'D'
			tempDeck = playerDeck
			playerDeck = deck_maker(5, 'Rebuilding playerDeck')
			Deck.append(tempDeck)
			random.shuffle(Deck)
			
while restart: #loop to allow the player can restart the game
	playerTurn, cpuTurn = True, True
	playerNumTurn, cpuNumTurn = 5, 5
	playerScore = 0
	cpuScore = 0
	playerChoice = ''
	cpuChoice = 0
	playerDisplayed = []
	cpuDisplayed = []

	Deck = shuffle()
	playerDeck = deck_maker(5, 'Building Player/CPU Decks\n')
	cpuDeck = deck_maker(5, '',)

	while playerNumTurn > 0 and cpuNumTurn > 0 and not finish: #main game loop
		flipcheck = 0
		deckTop = Deck[0]

		if 'DeckSwap' in cpuDeck: #Remove the DeckSwap WildCard from the cpuDeck
			cpuDeck.remove('DeckSwap') #CPU not smart enough to properly use it
			tempGrab = flipper(Deck, '')
			cpuDeck.append(tempGrab[0])
			Deck = tempGrab[1]

		while playerTurn:
			print "Your score is", str(playerScore), "and the other player's score is", str(cpuScore), "."
			print "You have", len(playerDeck), "cards unflipped, and", len(playerDisplayed), "cards flipped."
			print "The other player has", len(cpuDeck), "cards unflipped, and", len(cpuDisplayed), "cards flipped.\n"

			playerChoice = raw_input("Type 'F' to flip a card, 'D' to draw a card, 'E' to exit, or 'HELP' for help. ") #tells the player what to do
			playerChoice = playerChoice.upper()

			if playerChoice == 'F': #flip a card in the player's hand
				tempGrab = flipper(playerDeck, 'Flipping card')
				playerDeck = tempGrab[1]
				playerDisplayed.append(tempGrab[0])
				playerNumTurn -= 1
				playerTurn = False
				cpuTurn = True

			elif playerChoice == 'D': #draw a card from the main Deck
				tempGrab = flipper(Deck, 'Drawing card from main Deck')
				playerDisplayed.append(tempGrab[0])
				Deck = tempGrab[1]
				playerNumTurn -= 1
				playerTurn = False
				cpuTurn = True

			elif playerChoice == 'E': #

				while True:
					ask = raw_input("\nAre you sure you want to exit?(y/n)")
					ask = ask.upper()

					if ask == "Y":
						playerTurn = False
						cpuTurn = False
						finish = True
						break

					elif ask == "N":
						break

					else:
						print "'Y' or 'N' please!"

			elif playerChoice == 'HELP':
				help = open("HELP.md", "r")
				print(help.read())
				help.close()
				help = raw_input("Press 1 to show commands, and any key to return to the game: ")

				if help == '1':
					print """
>>> 'F'			---->	Flips a card in your deck.
>>> 'D'			---->	Draws a card from the main deck.
>>> 'E'			---->	Exits from the game.
>>> 'HELP'		---->	Displays information about the game, as well as debugging commands.
				"""
					help = raw_input("Press 1 to show additional commands and 2 to continue with the game: ")

					if help == '1':
						print """
>>> 'DECK'		---->	Shows all cards in the main deck.
>>> 'PDECK'		---->	Shows all cards in the player's deck.
>>> 'CDECK'		---->	Shows all cards in the cpu's deck.
>>> 'PDISP'		---->	Shows all cards in the player's hand.
>>> 'CDISP'		---->	Shows all cards in the cpu's hand.
>>> 'ADD'		---->	Adds a specified card.
>>> 'TURNRESET' 	---->	Resets player and cpu turns. Has the same effect of restarting the game
>>> 'TRACE'		---->	Actiivates the pdb debugging traceback.
"""
						raw_input("Press any key to continue: ")

			#Cheat codes for debugging
			elif playerChoice == 'DECK':
				print ">>>", Deck
			elif playerChoice == 'PDECK':
				print ">>>", playerDeck
			elif playerChoice == 'CDECK':
				print ">>>", cpuDeck
			elif playerChoice == 'PDISP':
				print ">>>", playerDisplayed
			elif playerChoice == 'CDISP':
				print ">>>", cpuDisplayed

			elif playerChoice == 'ADD':
				choice = [raw_input(">>> Enter the card to add(Example: hearts, 3): ")]
				tempHand = choice.split()
				if choice in str(Deck):
					playerDisplayed.append(choice)
					Deck.remove(choice)
				elif choice not in str(Deck):
					print "Could not find" + choice + "in Deck."
			
			elif playerChoice == 'TURNRESET':
				print ">>> Resetting turns",
				time.sleep(.33);print ".",
				time.sleep(.33);print ".",
				time.sleep(.33);print ".",;time.sleep(.33)
				playerNumTurn, cpuNumTurn = 5, 5 #resets player/cpu turns to 5
			
			elif playerChoice == 'TRACE':
				print ">>> Beginning Debug Traceback",
				time.sleep(.33);print ".",
				time.sleep(.33);print ".",
				time.sleep(.33);print ".",;time.sleep(.33)
				pdb.set_trace() #begins traceback
			
			else:
				print "Please choose an item from the list!\n"

		while cpuTurn: #CPU loop
			print "Please wait, the cpu is making its decision",
			time.sleep(0.3)
			print ".",
			time.sleep(0.3)
			print ".",
			time.sleep(0.3)
			print "."
			time.sleep(0.4)

			cpuChoice = random.randint(1,2)

			if cpuChoice == 1: #If cpu decides to flip a card
				tempGrab = flipper(cpuDeck, 'Flipping card')
				cpuDeck = tempGrab[1]
				cpuDisplayed = tempGrab[0]
				cpuNumTurn -= 1
				cpuTurn = False
				playerTurn = True

			else: #if cpu decides to draw a card
				tempGrab = flipper(Deck, 'Drawing card from main Deck')
				Deck = tempGrab[1]
				cpuDisplayed.append(tempGrab[0])
				cpuNumTurn -= 1
				cpuTurn = False
				playerTurn = True

		while flipcheck < 5: #calculates player and cpu scores
			#breaks out of loop if it catches an IndexError 5 times
			try:
				if 'X2Multiplier' in playerDisplayed:
					playerScore = (sum(map(lambda x: x[1], playerDisplayed))) * 2
				elif 'X2Multiplier' in cpuDisplayed:
					cpuScore = (sum(map(lambda x: x[1], cpuDisplayed))) * 2
				else:
					playerScore = sum(map(lambda x: x[1], playerDisplayed))
					
					cpuScore = sum(map(lambda x: x[1], cpuDisplayed))

				flipcheck = 6

			except(IndexError, TypeError):
				flipcheck += 1

	if playerNumTurn <= 0 and cpuNumTurn <= 0:
		if playerScore > cpuScore:
			print "Congratulations! You won " + str(playerScore) + " to " + str(cpuScore) + "!"

		elif cpuScore > playerScore:
			print "Too bad, the computer beat you " + str(cpuScore) + "to" + str(playerScore) + "."

		else:
			print "It was a tie. Oh well."
			print "The final scores were " + playerScore + "and" + str(cpuScore) + "."

		while True:
			ask = raw_input("\nDo you wish to play again?(y/n)");
			ask = ask.upper()

			if ask == "Y":
				restart = True
				break

			elif ask == "N":
				restart = False
				print "Thanks for playing!"
				break

			else:
				print "'Y' or 'N' please!"

	else:
		print "Thanks for playing!"
		restart = False

nuclear = u'\u2622'
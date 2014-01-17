#################
#Tyler Robbins	#
#1/5/13			#
#CardMayhemTest3#
#################

print 'Initializing Card Mayhem', '.', '.', '.'

import random
import time
import sys

cardValues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Cards = ['a', '2','3','4','5','6','7','8','9','10','j','q','k']
Suits = ['hearts', 'spades', 'diamonds', 'clubs']
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
	time.sleep(1)
	print 'Making Deck'
	newdeck = []
	while len(newdeck) < 52: #makes card
		tempDeck = (random.choice(Suits), random.choice(cardValues))

		if tempDeck not in newdeck: #puts card in newdeck
			newdeck += [tempDeck]

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

		deckchoice += [tempHand] #adds card to player/cpu hand

	return deckchoice #player/cpuDeck=deck_maker(5)

def flipper(deck, message): #flips card in player hand
	"""tempGrab=flipper(playerDeck), tempGrab=flipper(cpuDeck), tempGrab=flipper(Deck)
	playerDisplayed=tempGrab[0]
	playerDeck=tempGrab[1]"""

	print message,
	time.sleep(0.33)
	print ".",
	time.sleep(0.33)
	print ".",
	time.sleep(0.34)
	print "."

	tempHand = ()

	try:
		flipcheck = 1

		while flipcheck == 1:
			try:
				tempHand += (random.choice(deck)) #grab card from player/cpu hand
				flipcheck = 0

			except(TypeError):
				flipcheck1 = 0
				flipcheck1 += 1
				if flipcheck1 == 5:
					sys.exit(TypeError)

		if tempHand in deck:
			deck.remove(tempHand) #removes tempHand from player/cpu hand

	except(IndexError):
		pass

	print "The card was a " + str(tempHand[1]) + " of " + str(tempHand[0]) + "!\n"

	tempHand = [tempHand]

	return [(tempHand), deck] #returns two values. use arrays to get correct values with tempGrab[]

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
		
		#Calculates player and cpu scores
		flipcheck = 1

		while flipcheck == 1:
			try:
        			playerScore = sum(map(lambda x: x[1], playerDisplayed))
				cpuScore = sum(map(lambda x: x[1], cpuDisplayed))

				flipcheck = 0

			except(IndexError):
				pass

		while playerTurn:
			print "Your score is", str(playerScore), "and the other player's score is", str(cpuScore), "."
			print "You have", len(playerDeck), "cards unflipped, and", len(playerDisplayed), "cards flipped."
			print "The other player has", len(cpuDeck), "cards unflipped, and", len(cpuDisplayed), "cards flipped.\n"

			playerChoice = raw_input("Type 'F' to flip a card, 'D' to draw a card, and 'E', to exit. ") #tells the player what to do
			playerChoice = playerChoice.upper()

			if playerChoice == 'F': #flip a card in the player's hand
				tempGrab = flipper(playerDeck, 'Flipping card')
				playerDeck = tempGrab[1]
				playerDisplayed += (tempGrab[0])
				playerNumTurn -= 1
				playerTurn = False
				cpuTurn = True

			elif playerChoice == 'D': #draw a card from the main Deck
				tempGrab = flipper(Deck, 'Drawing card from main Deck')
				playerDisplayed += tempGrab[0]
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
				choice = raw_input(">>> Enter the card to add: ")
				if choice in Deck:
					playerDisplayed += [choice]
					Deck.remove(choice)
				elif choice not in Deck:
					print "Could not find" + choice + "in Deck."

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
				cpuDisplayed += tempGrab[0]
				cpuNumTurn -= 1
				cpuTurn = False
				playerTurn = True

			else: #if cpu decides to draw a card
				tempGrab = flipper(Deck, 'Drawing card from main Deck')
				Deck = tempGrab[1]
				cpuDisplayed += tempGrab[0]
				cpuNumTurn -= 1
				cpuTurn = False
				playerTurn = True

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

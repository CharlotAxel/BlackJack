#!/usr/bin/python3

from random import randrange

Blackjack = 21
argent = 1000

#Loops in order to keep the game going.
continuerPartie = True

regle = input("Souhaitez-vous avoir un rappel des règles du blackjack ? (o/n)")
if regle == "o" or regle == "O":
	print("Le blackjack est un jeu de carte ou pour gagner vous devez atteindre le nombre 21 en combinant la valeur de vos cartes.")

print("Vous vous installez à table avec", argent, "$")

while continuerPartie:

	#On défini une mise de depart.
	mise = 0
	while mise <= 0 or mise > argent:
		mise = input("Combien misez-vous ?")
		try:
			mise = int(mise)
		except ValueError:
			print("Vous n'avez pas entre un nombre.")
			mise =- 1
			continue
		if mise < 0:
			print("Votre mise ne peut être nulle.")
		if mise > argent:
			print("Votre mise ne peut depasser vos ", argent, "$ actuels.")
		
		
	#On tire les cartes Joueurs au hasard.
	carte1 = randrange(2, 12)
	carte2 = randrange(2, 12)
	totalCarte = carte1 + carte2
	print("Vous avez recu : ", carte1, "et ", carte2,".")
	
	#On tire les cartes du croupier
	croupier1 = randrange(2,12)
	croupier2 = 11
	croupier3 = randrange(2,9)
	totalCroupier = croupier1 + croupier2
	print("Le croupier a recu : ", croupier1, "et ", croupier2, ".")
	
	#We checks the cards from the player and the Casino
	if totalCarte == Blackjack:
		print("Felicitations, vous remportez la manche! Vos gains sont de", mise * 3, "$")
		argent += mise * 3
		
	elif totalCarte > Blackjack:
		print("Dommage, ca sera pour une prochaine fois.")
		argent -= mise			
	elif totalCarte < Blackjack:
		carte3 = input("Souhaitez-vous rechoisir une carte (o/n)")#On propose une 3eme carte au joueur
		if carte3 == "o" or carte3 == "O":
			carte3 = randrange(2, 12)
			print("Vous avez tirez :", carte3, ".")
			totalCarte = carte1 + carte2 + carte3
			if totalCarte == Blackjack:
				print("Felicitations, vous remportez la manche! Vos gains sont de ", mise * 3, "$")
				argent += mise * 3
			elif totalCarte > Blackjack or totalCarte < Blackjack:
				print("Dommage, ca sera pour une prochaine fois.")
				argent -= mise
		else:
			if totalCroupier < 17: #On fait tirer une 3eme carte au croupier
				print("Le croupier tire une nouvelle carte : ", croupier3, ".")
				totalCroupier = totalCroupier + croupier3
			elif totalCroupier == Blackjack:
				print("Le croupier l'emporte.")
		
				if totalCroupier > Blackjack:
					print("Le croupier saute. Vous remportez la manche. Vos gains sont de ", mise,"$")
					argent += mise
			
				elif totalCroupier > totalCarte: #Si le croupier a un plus haut score que le joueur, il gagne.
					print("Dommage, ca sera pour une prochaine fois.")
					argent -= mise
	
				else:
					totalCroupier < totalCarte or totalCroupier == totalCarte
					print("Vous emporter votre mise : ", mise, ".")
					argent += mise
	
	if argent <= 0:
		print("Vous êtes ruine. C'est la fin de la partie.")
		continuerPartie = False
	
	else:
		print("Vous avez a present :", argent, "$")
	quitter = input("Voulez - vous quitter (o/n)")
	
	if quitter == "o" or quitter == "O":
		print("Au revoir.")
		continuerPartie = False

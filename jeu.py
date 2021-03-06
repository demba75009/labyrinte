import pygame
from pygame.locals import *
import os
import pygame.mixer

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("p.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.jpg").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

#Rafraîchissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(400, 30)

#BOUCLE INFINIE
 
pygame.mixer.music.load("02.Ninho - Fendi.mp3")   # chargement de la musique
pygame.mixer.music.play(-1)  
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if  event.key == K_DOWN :	#Si "flèche bas"
				#On descend le perso
				position_perso = position_perso.move(0,22)
			if  event.key == K_RIGHT :	#Si "flèche droite "
				#On descend le perso
				position_perso = position_perso.move(22,0)
			if  event.key == K_LEFT :	#Si "flèche droite "
				#On descend le perso
				position_perso = position_perso.move(-22,0)
			if  event.key == K_UP :	#Si "flèche droite "
				#On descend le perso
				position_perso = position_perso.move(0,-22)

	
	#Re-collage
	fenetre.blit(fond, (0,0))	
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()

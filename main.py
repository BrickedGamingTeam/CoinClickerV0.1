import pygame, sys
from pygame.locals import QUIT, K_a
import sys

coins = 0
mult = 1
auto = 0
running = True
blue=(0,0,255)
height = 600
width = 800

# Going to be used later for upgrades
multUPG = 10
autoUPG = 100

pygame.init()
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cookie Game v0.1')

font = pygame.font.Font('freesansbold.ttf', 32)
x = 200
y = 200

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				coins += 1*(mult)

	wn.fill((255,255,255))

	coinss = font.render("Coins: ", str(coins), 1)
	coinRender = font.render(str(coins), 1, (0,0,0))
	wn.blit(coinss, (x, y))
	wn.blit(coinRender, (230,230))
	pygame.display.flip()

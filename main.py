import pygame
from pygame.locals import QUIT, K_a, K_SPACE, RESIZABLE, FULLSCREEN
import sys

coins = 0
mult = 1
running = True

# setting the texts coordinates. Change before release.
text1X = 683
text1Y = 200
text2X = 737
text2Y = 200

pygame.init()

# initializing the font.
font = pygame.font.Font('freesansbold.ttf', 16)

info = pygame.display.Info()
white = (255, 255, 255)
size = width, height = info.current_w, info.current_h
print(width, height)

# setting the screen up for size and setting up the caption
screen = pygame.display.set_mode((size), RESIZABLE, FULLSCREEN)
pygame.display.set_caption("Coin Clicker v0.1")

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                coins += 1*(mult)

    screen.fill(white)

    coinsText = font.render('Coins:', True, (0, 0, 0))
    screen.blit(coinsText, (text1X, text1Y))
    coinsValueRender = font.render(str(coins), True, (0, 0, 0))
    screen.blit(coinsValueRender, (text2X, text2Y))
    pygame.display.update()

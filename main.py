import pygame, sys, os
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tetris Game")
art = pygame.image.load("art.png")
screen = pygame.display.get_surface()
screen.blit(art, (50,20))
pygame.display.flip()
pygame.mouse.set_cursor(pygame.cursors.tri_left)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()

#pygame.FULLSCREEN



def update():
    art.left += 2
    art.top += 2
    if art.top > 400:
        art.pos = (0,0)

def input(events):
    for event in events:
        if event.type() == QUIT:
            sys.exit(0)
        else:
            print(event)



while True:
    input(pygame.event.get(()))

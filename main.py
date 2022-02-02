import pygame, sys, os
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((550, 400))

pygame.display.set_caption("Tetris Game")

def input(events):
    for event in events:
        if event.type() == QUIT:
            sys.exit(0)
        else:
            print(event)

while True:
    input(pygame.event.get(()))

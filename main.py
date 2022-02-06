import pygame, sys, os
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((680, 480), 0, 32)
pygame.display.set_caption("Tetris Game")
pygame.mouse.set_cursor(pygame.cursors.tri_left)

white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red = (255,   0,   0)
art = pygame.image.load("art.png")
artx = 360
arty = 180
direction = "left"
#screen2 = pygame.display.get_surface()
#screen2.blit(art, (50,20))
#pygame.display.flip()

pygame.draw.polygon(screen, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.rect(screen, red, (200, 150, 100, 50))
pygame.display.flip()


if direction == "right":
    artx += 5
    if artx == 360:
        direction = "down"
elif direction == "down":
    arty += 5
    if arty == 460:
        direction = "left"

screen.blit(art, (artx, arty))
pygame.display.flip()




done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()

#rectangle = pygame.Rect(24, 24, 72, 48)
#screen.fill([0,0,0])
#pygame.draw.rect(window, [255,0,0], rectangle)
#pygame.display.flip()


'''def update():
    art.left += 2
    art.top += 2
    if art.top > 400:
        art.pos = (0,0)'''

def input(events):
    for event in events:
        if event.type() == QUIT:
            sys.exit(0)
        else:
            print(event)


while True:
    input(pygame.event.get(()))

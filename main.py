import pygame, sys, os
from pygame.locals import *

width = 680
height = 480
x = 0
y = 0
w = 20
h = 20
step = 50
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 180)
red = (255, 0, 0)

artx = 160
arty = 180
#screen.blit(art, (artx, arty))
#pygame.display.flip()
screen2 = pygame.display.get_surface()

#screen = {}
screen = pygame.display.set_mode((width, height))
#screen = {'surf': False}


def main_tetris():
    pygame.init()
    pygame.display.set_caption("Tetris Game")
    pygame.mouse.set_cursor(pygame.cursors.tri_left)
    art = pygame.image.load("art-2.png")
    screen.blit(art, (artx, arty))
    pygame.display.flip()
    while True:
        checkEvents()
        screen.fill(white)
        drawRect()
        drawGrid(4)
        pygame.display.flip()



'''def drawRect():
    pygame.draw.line(
        screen, black,
        (0 + step, 0 + step),
        (width - step, 0 + step), 2)
    pygame.draw.line(
        screen, black,
        (0 + step, height - step),
        (width - step, height -step), 2)
    pygame.draw.line(
        screen, black,
        (0 + step, 0 + step),
        (0 + step, height - step), 2)
    pygame.draw.line(
        screen, black,
        (width - step, 0 + step),
        (width - step, height - step), 2)'''

def drawRect():
    pygame.draw.rect(
        screen, red,
        (18, 18, 60, 60)
    )


def drawGrid(divisions):
    size_grid = 300
    grid_x, grid_y = 10, 10
    pygame.draw.line(
        screen, green,
        (grid_x, grid_y),
        (size_grid + grid_x, grid_y), 2)
    pygame.draw.line(
        screen, green,
        (grid_x, size_grid + grid_y),
        (size_grid + grid_x, size_grid + grid_y), 2)
    pygame.draw.line(
        screen, green,
        (grid_x, grid_y),
        (grid_x, size_grid + grid_y), 2)
    pygame.draw.line(
        screen, green,
        (size_grid + grid_x, grid_y),
        (size_grid + grid_x, size_grid + grid_y), 2)

    cell_size = size_grid/divisions

    for x in range(divisions):
        pygame.draw.line(
            screen, green,
            (grid_x + (cell_size * x), grid_y),
            (grid_x + (cell_size * x), size_grid + grid_y), 2)
        pygame.draw.line(
            screen, green,
            (grid_x, grid_y + (cell_size * x)),
            (size_grid + grid_x, grid_y + (cell_size * x)), 2)









'''a = 5
b = 5
running = 1

while running:
    a += 1
    b += 1
    screen2.blit(art, (a, b))
    pygame.display.flip()'''


# Podzielic okno na siatke i na niej rysowac tablicą? figury

#pygame.draw.polygon(screen, green, ((20, 20), (20, 100), (70, 100), (70, 70), (50, 70), (50, 20), (20, 20)))
#pygame.draw.polygon(screen, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
#pygame.draw.rect(screen, red, (200, 150, 100, 50))
#pygame.display.flip()

'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= step
    if keys[pygame.K_RIGHT]:
        x += step
    if keys[pygame.K_UP]:
        y -= step
    if keys[pygame.K_DOWN]:
        y += step

    #pygame.draw.rect(screen, white, (x, y, w, h))
    #pygame.display.flip()


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
pygame.quit()'''

#rectangle = pygame.Rect(24, 24, 72, 48)
#screen.fill([0,0,0])
#pygame.draw.rect(window, [255,0,0], rectangle)
#pygame.display.flip()


'''def update():
    art.left += 2
    art.top += 2
    if art.top > 400:
        art.pos = (0,0)'''

'''def input(events):
    for event in events:
        if event.type() == QUIT:
            sys.exit(0)
        else:
            print(event)'''

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()

#while True:
#    input(pygame.event.get(()))
main_tetris()
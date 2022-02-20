import sys
import pygame
import numpy as np
from pygame.locals import KEYDOWN, K_q

screensize = width, height = 1000, 800
black = (0, 0, 0)
grey = (160, 160, 160)
white = (250, 250, 250)
blue = (0, 0, 180)

#cellmap = np.random.randint(2, size=(15, 15))
#print(cellmap)

tab = []
for x in range(10):
    add = [0] * 10
    tab.append(add)
print(tab)

screen = pygame.display.set_mode(screensize, pygame.RESIZABLE)
gridWH = 500
gridOrigin = (50, 50)
#gridCell = cellmap.shape[0]


def main():
    pygame.init()
    pygame.display.set_caption('TETRIS')
    while True:
        checkEvents()
        screen.fill(grey)
        drawSquareGrid(
            gridOrigin, gridWH, 10) #gridCell) #10
        #placeCells()
        pygame.display.flip()


def drawSquareCell(x, y, dimX, dimY):
    pygame.draw.rect(
        screen, black,
        (x, y, dimX, dimY))


def drawSquareGrid(origin, gridWH, cells):
    gridWH = gridWH
    grid_x, grid_y = origin

    pygame.draw.line(
        screen, black,
        (grid_x, grid_y),
        (gridWH + grid_x, grid_y), 2)
    pygame.draw.line(
        screen, black,
        (grid_x, gridWH + grid_y),
        (gridWH + grid_x, gridWH + grid_y), 2)
    pygame.draw.line(
        screen, black,
        (grid_x, grid_y),
        (grid_x, gridWH +  grid_y), 2)
    pygame.draw.line(
        screen, black,
        (gridWH + grid_x, grid_y),
        (gridWH + grid_x, gridWH + grid_y), 2)
    cellSize = 50 #gridWH / cells

    for x in range(cells):
        pygame.draw.line(
            screen, black,
            (grid_x + (cellSize * x), grid_y),
            (grid_x + (cellSize * x), gridWH + grid_y), 2)
        pygame.draw.line(
            screen, black,
            (grid_x, grid_y + (cellSize * x)),
            (grid_x + gridWH, grid_y + (cellSize * x)), 2)


'''def placeCells():
    cellBorder = 5
    cell_x = cell_y = gridWH / gridCell - cellBorder * 2
    for row in range(cellmap.shape[0]):
        for column in range(cellmap.shape[1]):
            if (cellmap[column][row] == 1):
                drawSquareCell(
                    gridOrigin[0] + (cell_y * row)
                    + cellBorder + (2 * row * cellBorder) + 2/2,
                    gridOrigin[1] + (cell_x * column)
                    + cellBorder + (2 * column * cellBorder) + 2/2,
                    cell_x, cell_y)'''


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()



if __name__ == '__main__':
    main()






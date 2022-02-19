import sys
import pygame
import numpy as np
from pygame.locals import KEYDOWN, K_q

screensize = width, height = 1000, 1000
black = (0, 0, 0)
grey = (160, 160, 160)

cellmap = np.random.randint(2, size = (6, 6))
print(cellmap)

screen = pygame.display.set_mode(screensize)
gridWH = 400
gridOrigin = (200, 100)
gridCell = cellmap.shape[0]


def main():
    pygame.init()
    while True:
        checkEvents()
        screen.fill(grey)
        drawSquareGrid(
            gridOrigin, gridWH, gridCell)
        placeCells()
        pygame.display.flip()


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


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
    cellSize = gridWH / cells

    for x in range(cells):
        pygame.draw.line(
            screen, black,
            (grid_x + (cellSize * x), grid_y),
            (grid_x + (cellSize * x), gridWH + grid_y), 2)
        pygame.draw.line(
            screen, black,
            (grid_x, grid_y + (cellSize * x)),
            (grid_x + gridWH, grid_y + (cellSize * x)), 2)

def placeCells():
    cellBorder = 6
    cell_x = cell_y = gridWH / gridCell - cellBorder * 2
    for row in range(cellmap.shape[0]):
        for column in range(cellmap.shape[1]):
            if (cellmap[column][row] == 1):
                drawSquareCell(
                    gridOrigin[0] + (cell_y * row)
                    + cellBorder + (2 * row * cellBorder) + 2/2,
                    gridOrigin[1] + (cell_x * column)
                    + cellBorder + (2 * column * cellBorder) + 2/2,
                    cell_x, cell_y)


if __name__ == '__main__':
    main()




